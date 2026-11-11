<!-- Source: https://docs.aws.amazon.com/linux/al2023/ug/minimal-container.html -->
<!-- Downloaded: 2026-11-12 -->

# AL2023 Minimal container image

###### Note

 The standard AL2023 container images are suitable for most use cases, and adapting to the minimal container image is likely to be more work than adapting to the AL2023 base container image.

 The AL2023 minimal container image, introduced in AL2023.2, differs from the base container image because it contains only the bare minimum packages needed to install other packages. The minimal container image is designed to be a minimal set of packages, not a convenient set of packages .

 The AL2023 minimal container image is built from software components already available in AL2023. The key difference in the minimal container image is using `microdnf` to provide the `dnf` package manager rather than the fully featured Python based `dnf`. This enables the minimal container image to be smaller with the trade-off of not having the full feature set of the `dnf` package manager which is included in the AL2023 AMIs and base container image.

 The AL2023 minimal container image forms the base of the `provided.al2023` AWS Lambda runtime environment.

 For a detailed list of packages included in the minimal container image, see [Comparing packages installed on Amazon Linux 2023 Container Images](https://docs.aws.amazon.com/linux/al2023/ug/al2023-container-image-types.html).

## Minimal Container image size

 Because the AL2023 minimal container image contains fewer packages than the AL2023 base container image, it is also significantly smaller. The following table compares the container image options of current and past releases of Amazon Linux.

###### Note

 Image Size is as-shown on [ Amazon Linux on Amazon ECR Public Gallery](https://gallery.ecr.aws/amazonlinux/amazonlinux).

|  Image |  Version |  Image Size |  Note |
|---|---|---|---|
|  Amazon Linux 1 (AL1) |  2018.03.0.20230918.0 |  62.3MB |  `x86-64` only |
|  Amazon Linux 2 |  2.0.20230926.0 |  64.2MB |  `aarch64` is 1.6MB larger than `x86-64` |
|  Amazon Linux 2023 base container image |  2023.12.20260831.0 |  54.6MB |   |
|  Amazon Linux 2023 minimal container image |  2023.12.20260831.0-minimal |  37.4MB |   |

## Using the AL2023 Minimal Container image

 The AL2023 minimal container image is available on ECR and the `2023-minimal` tag will always point to the latest AL2023 based minimal container image, while the `minimal` tag may be updated to a newer version of Amazon Linux than AL2023.

 You can pull these tags using `docker` with the following example:

```
$ docker pull public.ecr.aws/amazonlinux/amazonlinux:minimal
```

```
$ docker pull public.ecr.aws/amazonlinux/amazonlinux:2023-minimal
```

The following example shows a `Dockerfile` that takes the minimal container image and installs GCC on top of it :

```

FROM public.ecr.aws/amazonlinux/amazonlinux:2023-minimal
RUN dnf install -y gcc && dnf clean all

```
