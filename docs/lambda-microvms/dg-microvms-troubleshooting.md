<!-- Source: https://docs.aws.amazon.com/lambda/latest/dg/microvms-troubleshooting.html -->
<!-- Downloaded: 2026-11-12 -->

# Troubleshooting

This section describes how to debug and troubleshoot common issues when working with AWS Lambda MicroVMs.

## Shell access

Use shell access to connect directly to a running MicroVM for debugging and troubleshooting.

You can connect to a MicroVM shell in two ways:

-

**Console** – Select your MicroVM in the Lambda console and choose Connect.
-

**CLI** – Generate a shell token with `create-microvm-shell-auth-token`, then use the token to establish a connection.

Generate a shell token, then connect:

```
aws lambda-microvms create-microvm-shell-auth-token \
  --microvm-identifier <id> --expiration-in-minutes 30
# In Console: select MicroVM -> Connect
# In shell: ctr task ls, then ctr task exec -t --exec-id shell <id> /bin/sh
```

The MicroVM must have been run with the `SHELL_INGRESS` network connector (`arn:aws:lambda:`us-east-1`:aws:network-connector:aws-network-connector:SHELL_INGRESS`). If the MicroVM was not launched with this connector, `create-microvm-shell-auth-token` returns a `ValidationException`.

For other issues:

-

Check the `terminationMessage` field in the `get-microvm` response for terminated MicroVMs.
-

Check CloudWatch build logs for image creation issues.
-

Check the `StateReason` field for network connectors in `FAILED` state.

## Troubleshooting

This section provides solutions for common issues when working with Lambda MicroVMs.

|  Symptom |  Possible cause and resolution |
|---|---|
|  Image build fails (`CREATION_FAILED`) |  Check build logs at `/aws/lambda-microvms/<image-name>`. Verify `Dockerfile` syntax, Amazon S3 permissions, and base image availability. Run `docker build` locally to reproduce. |
|  `ValidationException` |

The error message reads `The requested CPU architecture ... is not available for base MicroVM image`. The base image version doesn't support the architecture in `cpuConfigurations`.

To choose a base image version that supports your architecture, see [Supported CPU architectures for base image versions](https://docs.aws.amazon.com/lambda/latest/dg/microvms-images.html#microvms-images-base-images-architectures).  |
|  MicroVM stuck in `PENDING` |  Wait and retry. If persistent, check service health. Verify your concurrency quota is not exhausted. |
|  Application not responding after resume |  Implement the `/resume` lifecycle hook to re-establish connections and validate state. Check that your app binds to port 8080 (or configured port) after resume. |
|  502 Bad Gateway from endpoint |  Application crashed or is not listening. Check runtime logs. Verify `EXPOSE` and `CMD` in `Dockerfile`. If auto-resume, the MicroVM may have failed to resume (check state by using `get-microvm`). |
|  429 Too Many Requests |  Request rate exceeded. Retry with exponential backoff and jitter. |
|  Connections dropping |  Idle timeout triggered. Implement ping/pong keepalives. Or extend `maxIdleDurationSeconds` in the idle policy. |
|  High latency on endpoint |  Bandwidth saturation. Check if traffic exceeds the bandwidth capability for your MicroVM size. Scale up to a larger size. |
|  Auth token expired (403) |  Tokens have a configurable expiration. Generate a new token before the old one expires. Implement token refresh logic in your client. |
|  VPC egress not working |  Verify network connector is in `ACTIVE` state. Check security group rules allow outbound traffic. Confirm subnets have routes to your target resources. |

## Common errors (image creation)

|  Error |  Cause |  Solution |
|---|---|---|
|  `S3_ACCESS_DENIED` |  Build role lacks permissions to retrieve Amazon S3 artifact. |  Add `s3:GetObject` permission for your artifact bucket. |
|  `S3_NO_SUCH_KEY` |  Artifact key does not exist in the bucket. |  Verify the Amazon S3 path is correct. |
|  `S3_NO_SUCH_BUCKET` |  Amazon S3 bucket does not exist. |  Check the bucket name and confirm it has been created. |
|  `S3_INVALID_OBJECT` |  Artifact in Glacier or non-directly-accessible storage class. |  Move the artifact to Standard storage class. |
|  `S3_CROSS_REGION_ACCESS_DENIED` |  Artifact is in a different Region than the MicroVM image. |  Ensure your artifact is in the same Region as your MicroVM image. |
|  `ARCHIVE_DOCKERFILE_NOT_FOUND` |  Zip archive is missing a `Dockerfile` in the root directory. |  Add a `Dockerfile` to the root of your zip archive. |
|  `ARCHIVE_INVALID` |  Archive file is not a valid ZIP or is corrupted. |  Re-create the zip archive and re-upload. |
|  `CONTAINER_BUILD_FAILED` |  Invalid `Dockerfile` instructions, missing files, or syntax errors. |  Debug your `Dockerfile` locally using `docker build`. |
|  `DISK_STORAGE_FULL` |  MicroVM ran out of storage during build. |  Reduce artifact size or contact support. |
|  `INTERNAL_PLATFORM_ERROR` |  An internal error occurred. |  Retry the operation. If persistent, contact support. |

## Network connector troubleshooting

|  Error code |  Cause |  Solution |
|---|---|---|
|  `DisallowedByVpcEncryptionControl` |  The VPC has an encryption control policy that prevents unencrypted network interfaces or traffic. Lambda cannot create ENIs that satisfy the encryption requirements. |  Add Lambda to the VPC encryption control exclusion list. If exclusion is not possible, use a VPC or subnet that does not have restrictive encryption controls applied. |
|  `Ec2RequestLimitExceeded` |  Lambda makes EC2 API calls (for example, `CreateNetworkInterface`, `DescribeSubnets`) to set up connectivity. Too many concurrent EC2 API calls causes throttling. |  Retry the operation after a short delay. If persistent, reduce concurrent network connector operations or request an EC2 API throttling limit increase through AWS Support. |
|  `InsufficientRolePermissions` |  The operator role lacks required EC2 permissions. |  Ensure the IAM role has necessary EC2 networking permissions. |
|  `InternalError` |  An unexpected error occurred within the Lambda service while processing the network connector request. |  Retry the operation. If it persists after multiple retries, contact AWS Support with the network connector ARN and approximate timestamp. |
|  `InvalidSecurityGroup` |  The security group ID does not exist, has been deleted, or does not belong to the same VPC as the specified subnets. |  Verify all security group IDs exist and belong to the same VPC as the subnets. Use `aws ec2 describe-security-groups --group-ids <sg-id>` to validate. |
|  `InvalidSubnet` |  The subnet ID does not exist, has been deleted, or belongs to a different VPC than expected. |  Verify all subnet IDs exist and belong to the correct VPC. Use `aws ec2 describe-subnets --subnet-ids <subnet-id>` to validate. |
|  `SubnetOutOfIPAddresses` |  The subnet's CIDR block is exhausted – all IPs are allocated to ENIs, instances, and other resources, so Lambda cannot create a network interface. |  Free up IP addresses by removing unused ENIs/instances, or use a different subnet with available capacity. Consider larger subnets (for example, /24 or larger) for network connectors. |
