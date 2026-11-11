import json
import os
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

APP_PORT = int(os.environ.get("APP_PORT", "8080"))
HOOK_PORT = int(os.environ.get("HOOK_PORT", "9000"))
WORKSPACE = os.environ.get("WORKSPACE", "/workspace")
EXEC_TIMEOUT_SECONDS = int(os.environ.get("EXEC_TIMEOUT_SECONDS", "30"))
MAX_OUTPUT_BYTES = 64 * 1024
HOOK_PREFIX = "/aws/lambda-microvms/runtime/v1/"

# Filled in by the /run hook. At build time these are None, and that None is
# what the snapshot holds, so no tenant data is ever baked into the image.
state = {"tenantId": None, "microvmId": None, "startedAt": None, "execCount": 0, "suspendCount": 0}
state_lock = threading.Lock()


def log(event, **fields):
    print(json.dumps({"event": event, "tenantId": state["tenantId"], "microvmId": state["microvmId"], **fields}), flush=True)


def truncate(text):
    data = text.encode("utf-8", "replace")
    if len(data) <= MAX_OUTPUT_BYTES:
        return text
    return data[:MAX_OUTPUT_BYTES].decode("utf-8", "ignore") + "\n...[truncated]"


def run_code(code, timeout):
    # A fresh interpreter per request. Files in WORKSPACE persist between
    # requests and across suspend/resume; Python variables do not.
    try:
        completed = subprocess.run(
            [sys.executable, "-c", code],
            cwd=WORKSPACE,
            capture_output=True,
            text=True,
            timeout=timeout,
            env={"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": WORKSPACE, "PYTHONUNBUFFERED": "1"},
        )
        return {"exitCode": completed.returncode, "stdout": truncate(completed.stdout), "stderr": truncate(completed.stderr)}
    except subprocess.TimeoutExpired:
        return {"exitCode": None, "stdout": "", "stderr": "timed out after %d seconds" % timeout}


class JsonHandler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass

    def read_json(self):
        length = int(self.headers.get("Content-Length") or 0)
        if not length:
            return {}
        try:
            return json.loads(self.rfile.read(length))
        except ValueError:
            return None

    def send_json(self, status, body):
        payload = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


class TenantApiHandler(JsonHandler):
    def do_GET(self):
        if self.path == "/health":
            with state_lock:
                return self.send_json(200, dict(state, workspaceFiles=sorted(os.listdir(WORKSPACE))))
        self.send_json(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/exec":
            return self.send_json(404, {"error": "not found"})
        body = self.read_json()
        if not body or not isinstance(body.get("code"), str):
            return self.send_json(400, {"error": "body must be JSON with a 'code' string"})
        timeout = min(int(body.get("timeoutSeconds", EXEC_TIMEOUT_SECONDS)), EXEC_TIMEOUT_SECONDS)
        result = run_code(body["code"], timeout)
        with state_lock:
            state["execCount"] += 1
            result["execCount"] = state["execCount"]
        log("exec", exitCode=result["exitCode"])
        self.send_json(200, result)


class HookHandler(JsonHandler):
    def do_POST(self):
        if not self.path.startswith(HOOK_PREFIX):
            return self.send_json(404, {"error": "not found"})
        hook = self.path[len(HOOK_PREFIX):]
        body = self.read_json() or {}

        if hook == "ready":
            # Build time: everything is imported and both listeners are up
            log("hook.ready")
            return self.send_json(200, {})

        if hook == "validate":
            # Runs on a MicroVM started from the new snapshot. Exercising the exec
            # path lets Lambda record which snapshot pages it touches and prefetch them
            result = run_code("print(sum(range(10)))", 10)
            ok = result["exitCode"] == 0 and result["stdout"].strip() == "45"
            log("hook.validate", ok=ok)
            return self.send_json(200 if ok else 500, {})

        if hook == "run":
            # Per-MicroVM initialization. runHookPayload is the opaque string the
            # session broker passed to RunMicrovm
            try:
                payload = json.loads(body.get("runHookPayload") or "{}")
            except ValueError:
                payload = {}
            with state_lock:
                state["tenantId"] = payload.get("tenantId")
                state["microvmId"] = body.get("microvmId")
                state["startedAt"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            log("hook.run")
            return self.send_json(200, {})

        if hook == "suspend":
            with state_lock:
                state["suspendCount"] += 1
            log("hook.suspend")
            return self.send_json(200, {})

        if hook == "resume":
            log("hook.resume")
            return self.send_json(200, {})

        if hook == "terminate":
            # Last chance to copy anything worth keeping out of WORKSPACE
            log("hook.terminate", workspaceFiles=len(os.listdir(WORKSPACE)))
            return self.send_json(200, {})

        self.send_json(404, {"error": "unknown hook"})


def serve(port, handler):
    ThreadingHTTPServer(("0.0.0.0", port), handler).serve_forever()


if __name__ == "__main__":
    os.makedirs(WORKSPACE, exist_ok=True)
    threading.Thread(target=serve, args=(HOOK_PORT, HookHandler), daemon=True).start()
    log("listening", appPort=APP_PORT, hookPort=HOOK_PORT)
    serve(APP_PORT, TenantApiHandler)
