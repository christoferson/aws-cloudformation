
## Transfer Family


### Transfer SFTP



### SSH Keys

- https://docs.aws.amazon.com/transfer/latest/userguide/key-management.html

ssh-keygen -t rsa -b 4096 -N "" -f key_name
You need to add private key to winscp

### References

-  https://aws.amazon.com/jp/blogs/storage/monitoring-your-aws-sftp-environment/

- https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/AWS_Transfer.html

- https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html

- https://www.ssh.com/academy/ssh/putty/windows/puttygen

- https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html

### Errors

no supported authentication methods available (server sent publickey)



The server does not support the operation.
Error code: 8
Error message from server (US-ASCII): SETSTAT unsupported

https://docs.aws.amazon.com/transfer/latest/userguide/transfer-file.html

```
Commands that attempt to change attributes of remote files, including timestamps, are not compatible with object storage systems such as Amazon S3. Therefore, if you are using Amazon S3 for storage, be sure to disable WinSCP timestamp settings (or use the SetStatOption as described in Avoid setstat errors) before you perform file transfers. To do so, in the WinSCP Transfer settings dialog box, disable the Set permissions upload option and the Preserve timestamp common option.
```