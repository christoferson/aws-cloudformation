"""Build the three zip artifacts into ./dist and optionally upload them to S3.

    python package.py                      # build only
    python package.py my-artifact-bucket   # build and upload under microvms/
"""
import os
import shutil
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(HERE, "dist")
# A boto3 release verified to include the lambda-microvms client. The Lambda
# Python runtime's bundled boto3 version is not documented, so vendor our own.
BOTO3 = "boto3==1.44.0"


def zip_dir(source, target):
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for root, _, files in os.walk(source):
            for name in files:
                if "__pycache__" in root or name.endswith(".pyc"):
                    continue
                path = os.path.join(root, name)
                # Dockerfile must sit at the zip root, not under a folder
                archive.write(path, os.path.relpath(path, source))
    print("built", os.path.relpath(target, HERE), os.path.getsize(target), "bytes")


def main():
    shutil.rmtree(DIST, ignore_errors=True)
    os.makedirs(DIST)

    zip_dir(os.path.join(HERE, "app", "basic"), os.path.join(DIST, "basic-app.zip"))
    zip_dir(os.path.join(HERE, "app", "sandbox"), os.path.join(DIST, "sandbox-app.zip"))

    build = os.path.join(DIST, "broker-build")
    # Resolve for the Lambda runtime (python3.13), not the local interpreter
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "--quiet", "--target", build,
        "--python-version", "3.13", "--only-binary", ":all:", BOTO3,
    ])
    shutil.copy(os.path.join(HERE, "broker", "broker.py"), build)
    zip_dir(build, os.path.join(DIST, "broker.zip"))
    shutil.rmtree(build)

    if len(sys.argv) > 1:
        bucket = sys.argv[1]
        for name in ("basic-app.zip", "sandbox-app.zip", "broker.zip"):
            subprocess.check_call(["aws", "s3", "cp", os.path.join(DIST, name), "s3://%s/microvms/%s" % (bucket, name)])


if __name__ == "__main__":
    main()
