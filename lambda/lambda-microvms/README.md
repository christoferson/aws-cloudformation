
## Lambda MicroVMs

| Template | What it shows |
|---|---|
| [lambda-microvm-basic.yaml](lambda-microvm-basic.yaml) | One image from a Dockerfile, build + execution roles. Launch with the CLI, call it with a token, watch suspend/resume |
| [lambda-microvm-multi-tenant.yaml](lambda-microvm-multi-tenant.yaml) | A per-tenant Python code sandbox: one isolated MicroVM per tenant, a session broker Lambda, DynamoDB mapping, all six lifecycle hooks |
| [lambda-microvm-vpc-networking.yaml](lambda-microvm-vpc-networking.yaml) | VPC egress connector that limits tenant code to one internal destination, and a private `lambda-microvm` ingress endpoint |

| Code | |
|---|---|
| [app/basic](app/basic/) | Node.js server on 8080 that exposes the snapshot-uniqueness trap |
| [app/sandbox](app/sandbox/) | Python server: tenant API on 8080, lifecycle hooks on 9000 |
| [broker/broker.py](broker/broker.py) | Session broker: tenant -> MicroVM, launch / reuse / close, port-scoped tokens |
| [package.py](package.py) | Builds the three zips into `dist/` and uploads them |

Offline docs: [../../docs/lambda-microvms/README.md](../../docs/lambda-microvms/README.md)

----------------------------------------------------------------------------------

## What a MicroVM is

A Firecracker VM you start with one API call, reach over its own HTTPS URL, and that remembers everything while it sleeps. It is built for one job: running code you don't trust (users', or an AI's) without it touching anyone else.

| | Lambda function | Lambda MicroVM |
|---|---|---|
| Unit | An invocation (event in, response out) | A long-lived environment for one tenant / session / job |
| Lifetime | Up to 15 min per invocation | Up to **8 hours**, running + suspended |
| Who you talk to | Any warm environment | **The** MicroVM: one endpoint = one VM, never load-balanced |
| State | Lost whenever Lambda recycles the environment | Memory + disk kept across **suspend/resume** |
| Interface | Handler function | Any HTTP server: HTTP/2, WebSockets, gRPC, SSE, any port |
| OS | Managed runtime | AL2023, `dnf install` whatever you need, optional elevated capabilities |
| Isolation unit | Per function | Per MicroVM: own kernel, memory, disk |

The lifecycle you control:

```
 create image (Dockerfile -> run app -> snapshot)          once per release
        │
 run-microvm ──► PENDING ──/run──► RUNNING ◄──────────────┐  traffic or resume-microvm
                                     │ idle > maxIdle      │  (/resume hook)
                                     ▼                     │
                               SUSPENDING ─/suspend─► SUSPENDED   no compute charges
                                     │ terminate-microvm, suspendedDuration or
                                     ▼ maximumDuration exceeded
                               TERMINATING ─/terminate─► TERMINATED
```

**The snapshot is the key idea.** Lambda builds your image by actually running your app, then freezes memory and disk. Every MicroVM restores that frozen state, so there's no boot and no app start. The consequence: anything your app computed at build time (random numbers, IDs, timestamps, open connections) is **identical in every MicroVM**. Generate per-VM values in the `/run` hook. `app/basic` shows the trap on purpose.

### What CloudFormation can and can't do

| Resource | In CloudFormation? |
|---|---|
| `AWS::Lambda::MicrovmImage` | Yes. Updating any build input builds a new image version |
| `AWS::Lambda::NetworkConnector` | Yes (VPC egress) |
| A running MicroVM | **No**. MicroVMs are per-session runtime objects; you start them with `run-microvm` (CLI) or the SDK. That's why the multi-tenant template has a broker |
| Ingress / internet egress connectors | AWS-managed, referenced by ARN: `...:aws:network-connector:aws-network-connector:HTTP_INGRESS`, `SHELL_INGRESS`, `INTERNET_EGRESS` |

**Every property of `AWS::Lambda::MicrovmImage` is required in CloudFormation,** even ones the API treats as optional. The [registry schema](../../docs/lambda-microvms/cfn-registry-schema-aws-lambda-microvmimage.json) lists all 13 as required. So the templates pass `AdditionalOsCapabilities: []`, `Hooks: {}` and so on; the schema accepts empty values.

----------------------------------------------------------------------------------

## Prepare the artifacts

The image build reads a zip from S3 with the `Dockerfile` **at the zip root**, in the **same Region**. The broker Lambda also ships from S3, with its own boto3: the docs don't say which boto3 the Lambda Python runtime bundles, and only recent releases have the `lambda-microvms` client.

```bash
# any Python works; a venv keeps the build away from your global packages
py -3.12 -m venv .venv && source .venv/Scripts/activate      # Windows Git Bash
# python3.12 -m venv .venv && source .venv/bin/activate      # macOS / Linux

aws s3 mb s3://my-microvm-artifacts-123456789012 --region us-east-1
python package.py my-microvm-artifacts-123456789012
# -> s3://.../microvms/basic-app.zip, sandbox-app.zip, broker.zip
```

`package.py` resolves boto3 1.44.0 for the Lambda runtime (`--python-version 3.13`), not for the Python that runs it.

To pick a base image version:

```bash
aws lambda-microvms list-managed-microvm-image-versions \
  --image-identifier arn:aws:lambda:us-east-1:aws:microvm-image:al2023-1
```

The templates default to version `3`, the first with `X86_64`. CloudFormation requires a version, so you upgrade the OS by changing `BaseImageVersion`. Versions go `AVAILABLE` -> `DEPRECATED` (60 days) -> `EXPIRING` (30 days, can't build) -> `EXPIRED` (can't run).

----------------------------------------------------------------------------------

## 1. Basic

```bash
aws cloudformation create-stack --stack-name myapp-dev-microvm-basic \
  --template-body file://lambda-microvm-basic.yaml --capabilities CAPABILITY_IAM \
  --parameters ParameterKey=CodeArtifactBucket,ParameterValue=my-microvm-artifacts-123456789012
```

Creation waits for the image build. If the build fails, the logs are in `/lambda-microvms/myapp/dev/basic`.

Copy the `RunMicrovmCommand` output and run it, then connect:

```bash
ID=mvm-...                       # microvmId from run-microvm
ENDPOINT=$(aws lambda-microvms get-microvm --microvm-identifier $ID --query endpoint --output text)
TOKEN=$(aws lambda-microvms create-microvm-auth-token --microvm-identifier $ID \
  --expiration-in-minutes 30 --allowed-ports '[{"port":8080}]' --query 'authToken."X-aws-proxy-auth"' --output text)

curl -s https://$ENDPOINT/ -H "X-aws-proxy-auth: $TOKEN"
# {"message":"hello from a Lambda MicroVM", "builtAt":"...", "snapshotValue":"k3j9...", "requestCount":1, ...}
```

Three things to try:

| Try | You'll see |
|---|---|
| `curl` a few times | `requestCount` goes up: in-memory state |
| `aws lambda-microvms suspend-microvm --microvm-identifier $ID`, then `curl` again | The first request waits for the resume, then `requestCount` continues where it was. Memory survived |
| Run a **second** MicroVM and `curl` it | `requestCount` starts at 1, but `builtAt` and `snapshotValue` are **the same as the first one**. They were computed at build time and frozen in the snapshot |

```bash
aws lambda-microvms terminate-microvm --microvm-identifier $ID
```

Without `--execution-role-arn`, the MicroVM's stdout/stderr never reaches CloudWatch, which is why the output command includes it.

----------------------------------------------------------------------------------

## 2. Multi-tenant code sandbox

The scenario is a SaaS product where each customer runs Python in the browser (or an AI agent runs it for them), like a code interpreter.

### Why a MicroVM per tenant

Running tenants' code in one container, or one Lambda function, means a kernel exploit, a fork bomb or a `cat /proc/*/environ` in tenant A's code can reach tenant B. Hardening that yourself (gVisor, seccomp, per-tenant clusters) is a project. Here **the tenant boundary is the VM**: own kernel, memory and disk. Inside it, the tenant can do anything.

### How it fits together

```
 your backend (already knows which tenant the user belongs to)
    │  lambda:Invoke {"action":"open","tenantId":"acme"}
    ▼
 SessionBrokerFunction ──GetItem──► TenantSessionTable  acme -> mvm-..., generation 3
    │   live? ──yes──► reuse it (even SUSPENDED: auto-resume wakes it on the first request)
    │   no ──► RunMicrovm(runHookPayload={"tenantId":"acme"}, clientToken="acme-4") + PutItem
    │  CreateMicrovmAuthToken(port 8080 only, 15 min)
    ▼
 {"url":"https://mvm-....lambda-microvm.us-east-1.on.aws", "headers":{"X-aws-proxy-auth":"..."}}
    │
 client ──POST /exec {"code":"..."}──► that tenant's MicroVM, directly. No load balancer
```

| Design choice | Why |
|---|---|
| Only the broker can `RunMicrovm` / mint tokens | Its IAM policy is scoped to the sandbox image ARN; MicroVM actions are authorized against the image they run from |
| Tenant ID goes in `runHookPayload`, not env vars | Env vars are image-wide and identical for every tenant. The payload is per MicroVM and arrives in the `/run` hook |
| Hooks on port **9000**, tokens open only **8080** | The hook paths are plain HTTP on the app. If they shared 8080, a client could POST to `/aws/lambda-microvms/runtime/v1/run` itself. A token for 8080 gets 403 on 9000 |
| `generation` + `clientToken = tenant-generation` | A retried broker call can't start a second MicroVM. Two concurrent `open`s race on a conditional write; the loser terminates its MicroVM and returns the winner's |
| Execution role writes logs only | It is shared by every tenant's MicroVM. Assume code inside can use it, so data access never goes here |
| `AdditionalOsCapabilities: []`, code runs as user `sandbox` | `ALL` would let tenant code mount filesystems and load eBPF |
| Container base `public.ecr.aws/lambda/microvms:al2023-minimal` | Ships a snapshot-safe OpenSSL. Tenant code makes TLS connections, and every MicroVM is a clone of one snapshot |
| `/validate` runs code once | Lambda records which snapshot pages that touches and prefetches them, so the first real `/exec` is faster |

### Lifecycle hooks used

| Hook | When | Timeout | In `server.py` |
|---|---|---|---|
| `/ready` | Build, after `CMD` starts | 1-3600 s | 200 once both listeners are up -> snapshot |
| `/validate` | Build, on a MicroVM from the new snapshot | 1-3600 s | Runs `print(sum(range(10)))` and checks for `45` |
| `/run` | Each new MicroVM, **before any traffic** | 1-60 s | Stores `tenantId` and `microvmId` |
| `/suspend` | Before suspend | 1-60 s | Logs; real apps flush and close connections |
| `/resume` | After resume, before traffic | 1-60 s | Logs; real apps refresh credentials and reconnect |
| `/terminate` | Final termination only | 1-60 s | Logs; last chance to copy `/workspace` out |

If `/run` fails or times out, the MicroVM can go straight to `TERMINATING` without ever being `RUNNING`.

### Deploy and use

```bash
aws cloudformation create-stack --stack-name myapp-dev-microvm-sandbox \
  --template-body file://lambda-microvm-multi-tenant.yaml --capabilities CAPABILITY_IAM \
  --parameters ParameterKey=CodeArtifactBucket,ParameterValue=my-microvm-artifacts-123456789012

aws lambda invoke --function-name myapp-dev-session-broker --cli-binary-format raw-in-base64-out \
  --payload '{"action":"open","tenantId":"acme"}' acme.json && cat acme.json
```

```bash
URL=$(python -c "import json;print(json.load(open('acme.json'))['url'])")
TOKEN=$(python -c "import json;print(json.load(open('acme.json'))['headers']['X-aws-proxy-auth'])")

curl -s -X POST $URL/exec -H "X-aws-proxy-auth: $TOKEN" \
  -d '{"code":"open(\"notes.txt\",\"w\").write(\"acme secret\"); print(\"saved\")"}'
curl -s -X POST $URL/exec -H "X-aws-proxy-auth: $TOKEN" -d '{"code":"print(open(\"notes.txt\").read())"}'
curl -s $URL/health -H "X-aws-proxy-auth: $TOKEN"
```

Things to try:

| Try | Expected |
|---|---|
| `open` for `globex`, then list files there | A different MicroVM with an empty `/workspace`. `acme`'s file isn't there |
| `open` for `acme` again | `"reused": true`, same `microvmId`, fresh token |
| Wait past `MaxIdleSeconds` (10 min), then `curl` | First request is slower (auto-resume), `notes.txt` is still there, `/health` shows `suspendCount: 1` |
| `curl -H "X-aws-proxy-port: 9000" ...` | 403. The token doesn't cover the hook port |
| `{"code":"import time; time.sleep(60)"}` | Killed after `EXEC_TIMEOUT_SECONDS` (30) |
| `{"action":"close","tenantId":"acme"}` | MicroVM terminated, record deleted |

Logs: `/lambda-microvms/myapp/dev/sandbox`, one stream per launch (`tenant/<tenantId>/<generation>`), with the JSON events from the hooks.

**In production**, put your own authenticated API in front of the broker. It must derive `tenantId` from the logged-in user, never from the request body, and the client calls `open` again before the 15-minute token expires.

----------------------------------------------------------------------------------

## 3. VPC networking

By default a MicroVM's outbound traffic goes **to the internet**. For tenant- or AI-written code, that's the exfiltration path. There is no "no egress" connector; the way to control it is a VPC egress connector:

```bash
aws cloudformation create-stack --stack-name myapp-dev-microvm-network \
  --template-body file://lambda-microvm-vpc-networking.yaml --capabilities CAPABILITY_IAM \
  --parameters ParameterKey=VpcId,ParameterValue=vpc-0abc ParameterKey=VpcCidrBlock,ParameterValue=10.0.0.0/16 \
               ParameterKey=VpcSubnetIdList,ParameterValue=\"subnet-0aaa,subnet-0bbb\" \
               ParameterKey=AllowedDestinationCidr,ParameterValue=10.0.20.0/24 \
               ParameterKey=AllowedDestinationPort,ParameterValue=443

# lock the sandbox down: tenant code reaches only 10.0.20.0/24:443
aws cloudformation update-stack --stack-name myapp-dev-microvm-sandbox --use-previous-template --capabilities CAPABILITY_IAM \
  --parameters ParameterKey=CodeArtifactBucket,UsePreviousValue=true \
               ParameterKey=RuntimeEgressConnectorArn,ParameterValue=<NetworkConnectorArn output>
```

| Piece | Role |
|---|---|
| `MicrovmNetworkConnector` | ENIs in your subnets; all MicroVM egress goes through them. Reusable by many MicroVMs |
| `MicrovmEgressSecurityGroup` | **One** egress rule. Declaring it removes the default allow-all, so there's no internet even if the subnet has a NAT gateway |
| `NetworkConnectorOperatorRole` | Lambda assumes it to create the ENIs (`ec2:CreateNetworkInterface`, tag with `ec2:ManagedResourceOperator`). Not the execution role |
| Destination side | Allow inbound from `MicrovmEgressSecurityGroupId` |
| `MicrovmConnectivityEndpoint` | `com.amazonaws.<region>.lambda-microvm` over PrivateLink. With private DNS, `*.lambda-microvm.<region>.on.aws` resolves to it inside the VPC |
| Its endpoint policy | `lambda:ConnectMicrovm` (valid only in endpoint policies). Connections use a MicroVM token, not SigV4, so the principal is anonymous: `Principal` and `Resource` must be `"*"`. Scope with `aws:ResourceAccount` |

The connector's compute type (`MicroVm`) is fixed. Updates create a new immutable version; the unqualified ARN follows the latest version and `NetworkConnectorLatestVersionArn` pins one. The docs say to terminate MicroVMs that use a connector before updating or deleting it.

The MicroVM management APIs (`run-microvm` and so on) use the normal Lambda endpoint, `com.amazonaws.<region>.lambda`, not this one.

----------------------------------------------------------------------------------

## Sizing and cost

You pick a **baseline**; the MicroVM can burst to **4x** it. You pay the baseline per second while running, plus actual use above it. vCPU = memory / 2 GB.

| Baseline | Peak | Disk | Endpoint bandwidth (sustained / burst) |
|---|---|---|---|
| 512 MiB, 0.25 vCPU | 2 GB, 1 vCPU | 8 GB | 0.5 MB/s / 2.5 MB |
| 1 GB, 0.5 vCPU | 4 GB, 2 vCPU | 8 GB | 1 MB/s / 5 MB |
| 2 GB, 1 vCPU (API default) | 8 GB, 4 vCPU | 8 GB | 2 MB/s / 10 MB |
| 4 GB, 2 vCPU | 16 GB, 8 vCPU | 16 GB | 4 MB/s / 20 MB |
| 8 GB, 4 vCPU | 32 GB, 16 vCPU | 32 GB | 8 MB/s / 40 MB |

| State | Charged |
|---|---|
| `RUNNING` | Compute |
| `SUSPENDED` | Snapshot storage only |
| `TERMINATED` | Nothing |

Always set an idle policy and `maximumDurationInSeconds`; a forgotten MicroVM runs for 8 hours. The account quota is on total memory across RUNNING **and** SUSPENDED MicroVMs (`ServiceQuotaExceededException` from `run-microvm`).

----------------------------------------------------------------------------------

## Errors

| Symptom | Cause |
|---|---|
| Image `CREATION_FAILED`, `S3_ACCESS_DENIED` | Build role can't read the key. With a new role, also IAM propagation: retry the stack |
| `ARCHIVE_DOCKERFILE_NOT_FOUND` | `Dockerfile` not at the zip root. `package.py` zips folder contents, not the folder |
| `S3_CROSS_REGION_ACCESS_DENIED` | Bucket in another Region than the image |
| `ValidationException ... CPU architecture ... not available` | That `BaseImageVersion` doesn't support the architecture (X86_64 needs version 3+) |
| `Exec format error` at start | Container or binaries built for the other architecture |
| 403 from the endpoint | Token missing/expired, or the port isn't in `allowedPorts` |
| 502 from the endpoint | App not listening on the port, crashed, or auto-resume failed. `get-microvm` -> `stateReason` |
| MicroVM went to TERMINATING right after run | `/run` hook failed or timed out |
| Connector `FAILED` | `StateReason`: `InsufficientRolePermissions`, `InvalidSubnet`, `SubnetOutOfIPAddresses`, `DisallowedByVpcEncryptionControl` |
| Broker: `AccessDeniedException` on RunMicrovm | Missing `lambda:PassNetworkConnector` or `iam:PassRole` |
| Before deleting a stack | Terminate its MicroVMs first (`list-microvms --image-identifier ...`). The docs don't say what happens to MicroVMs whose image is deleted |

### Not verified

I couldn't deploy this, and this IAM user lacks `cloudformation:ValidateTemplate`. What **was** checked:
- The `AWS::Lambda::MicrovmImage` and `AWS::Lambda::NetworkConnector` properties validate against the CloudFormation registry schemas.
- `server.py` was run locally: hooks, `/exec`, files persisting, timeouts.
- `broker.py` passed 7 scenarios with botocore's Stubber, inside the packaged `broker.zip`. Every API call was validated against the `lambda-microvms` and DynamoDB service models.

Not checked: real builds, that `dnf install python3` works in `al2023-minimal`, Region availability, and whether the run-hook payload limit is the documented 16 KB or the 4,096 characters the service model allows. The broker payload is about 20 characters.

## Docs

- [../../docs/lambda-microvms/dg-microvms-how-it-works.md](../../docs/lambda-microvms/dg-microvms-how-it-works.md) (concepts, build, states)
- [../../docs/lambda-microvms/dg-microvms-images.md](../../docs/lambda-microvms/dg-microvms-images.md) (sizing, architecture, base images, build hooks, versions)
- [../../docs/lambda-microvms/dg-microvms-images-snapshots.md](../../docs/lambda-microvms/dg-microvms-images-snapshots.md) (uniqueness, OpenSSL)
- [../../docs/lambda-microvms/dg-microvms-launching.md](../../docs/lambda-microvms/dg-microvms-launching.md) (run, tokens, ports, lifecycle hooks, suspend/resume)
- [../../docs/lambda-microvms/dg-microvms-networking.md](../../docs/lambda-microvms/dg-microvms-networking.md) (ingress, egress connectors, PrivateLink, endpoint policy)
- [../../docs/lambda-microvms/dg-microvms-security.md](../../docs/lambda-microvms/dg-microvms-security.md) (roles, tokens, IAM actions)
- [../../docs/lambda-microvms/sar-lambda-microvm-actions.md](../../docs/lambda-microvms/sar-lambda-microvm-actions.md) (IAM actions, resource types, `PassNetworkConnector`)
