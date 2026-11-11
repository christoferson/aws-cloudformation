<!-- Source: https://docs.aws.amazon.com/lambda/latest/dg/microvms-base-image-release-notes.html -->
<!-- Downloaded: 2026-11-12 -->

# Base image release notes

This page lists the changes in each version of the AWS Lambda MicroVMs managed base image. For information about how base image versioning and deprecation works, see [MicroVM base images](https://docs.aws.amazon.com/lambda/latest/dg/microvms-images.html#microvms-images-base-images).

## Version 3

-

**x86_64 architecture support** – You can now build MicroVM images for the `x86_64` architecture, in addition to `ARM64`. For more information, see [CPU architecture](https://docs.aws.amazon.com/lambda/latest/dg/microvms-images.html#microvms-images-cpu-architecture).

## Version 2

**Released:** November 5, 2026

-

**Higher ingress bandwidth limits** – Raised ingress bandwidth limit from 1 MB/s to 2 MB/s per vCPU, with a burst allowance of 10 MB per vCPU.
-

**Higher connection limits** – Per-MicroVM concurrent connection and request limits are raised from a flat 8 per vCPU to a floor of 150, plus 50 per additional vCPU, up to a maximum of 600. This change better supports high-concurrency workloads.
-

**Live build log streaming** – Output logs during MicroVM image build now stream to CloudWatch Logs in real time, instead of appearing after the build completes. If you build large or multi-stage images, you no longer have to wait for the build to complete before viewing logs.
-

**Updated kernel** – Images now run on kernel 6.1.166-24.303.amzn2023.
-

**Snapshot and memory optimizations** – Reduced MicroVM image snapshot size by up to 65 MB through optimizing image build artifacts and the memory reclamation process.
-

**Error handling** – More comprehensive and verbose error handling and exception reporting.
