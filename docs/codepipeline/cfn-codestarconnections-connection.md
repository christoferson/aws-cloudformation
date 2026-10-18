> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codestarconnections-connection.html
> Downloaded: 2026-10-18

# AWS::CodeStarConnections::Connection

The AWS::CodeStarConnections::Connection resource can be used to connect external source providers with services like AWS CodePipeline.

Note: A connection created through CloudFormation is in `PENDING` status by default. You can make its status `AVAILABLE` by updating the connection in the console.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::CodeStarConnections::Connection",
  "Properties" : {
      "ConnectionName" : String,
      "HostArn" : String,
      "ProviderType" : String,
      "Tags" : [ Tag, ... ]
    }
}

```

### YAML

```
Type: AWS::CodeStarConnections::Connection
Properties:
  ConnectionName: String
  HostArn: String
  ProviderType: String
  Tags: 
    - Tag

```

## Properties

**`ConnectionName`** 

The name of the connection. Connection names must be unique in an AWS account. 

Required: Yes

Type: String

Minimum: `1`

Maximum: `32`

Update requires: Replacement

**`HostArn`** 

The Amazon Resource Name (ARN) of the host associated with the connection. 

Required: No

Type: String

Pattern: `arn:aws(-[\w]+)*:.+:.+:[0-9]{12}:.+`

Minimum: `0`

Maximum: `256`

Update requires: Replacement

**`ProviderType`** 

The name of the external provider where your third-party code repository is configured. 

Required: No

Type: String

Allowed values: `Bitbucket | GitHub | GitHubEnterpriseServer | GitLab | GitLabSelfManaged`

Update requires: Replacement

**`Tags`** 

Specifies the tags applied to the resource. 

Required: No

Type: Array of Tag

Minimum: `0`

Maximum: `200`

Update requires: No interruption

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the connection. The ARN is used as the connection reference when the connection is shared between AWS services. For example:

 `arn:aws:codestar-connections:us-west-2:123456789012:connection/39e4c34d-e13a-4e94-a886-ea67651bf042` 

For more information about using the `Ref` function, see `Ref`.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using the `Fn::GetAtt` intrinsic function, see `Fn::GetAtt`.

#### 

**`ConnectionArn`** 

The Amazon Resource Name (ARN) of the connection. The ARN is used as the connection reference when the connection is shared between AWS services. For example: `arn:aws:codestar-connections:us-west-2:123456789012:connection/39e4c34d-e13a-4e94-a886-ea67651bf042`. 

**`ConnectionStatus`** 

The current status of the connection. For example: `PENDING`, `AVAILABLE`, or `ERROR`. 

**`OwnerAccountId`** 

The AWS account ID of the owner of the connection. For Bitbucket, this is the account ID of the owner of the Bitbucket repository. For example: `123456789012`. 

## Examples
Bitbucket Connection Configuration
GitHub Enterprise Server Connection Configuration
 

### Bitbucket Connection Configuration

The following example creates a connection with Bitbucket.

#### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "SampleConnection": {
            "Type": "AWS::CodeStarConnections::Connection",
            "Properties": {
                "ConnectionName": "MyConnection",
                "ProviderType": "Bitbucket",
                "Tags": [
                    {
                        "Key": "Project",
                        "Value": "ProjectB"
                    }
                ]
            }
        }
    }
}
```

#### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  SampleConnection:
    Type: AWS::CodeStarConnections::Connection
    Properties:
      ConnectionName: MyConnection
      ProviderType: Bitbucket
      Tags:
      - Key: Project
        Value: ProjectB
```
 

### GitHub Enterprise Server Connection Configuration

The following example creates a connection with GitHub Enterprise Server.

#### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "SampleConnection": {
            "Type": "AWS::CodeStarConnections::Connection",
            "Properties": {
                "ConnectionName": "MyConnection",
                "ProviderType": "GitHubEnterpriseServer",
                "HostArn": "arn:aws:codestar-connections:us-west-2:123456789123:host/abc123-example",
                "Tags": [
                    {
                        "Key": "Project",
                        "Value": "ProjectB"
                    }
                ]
            }
        }
    }
}
```

#### YAML

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  SampleConnection:
    Type: AWS::CodeStarConnections::Connection
    Properties:
      ConnectionName: MyConnection
      ProviderType: GitHubEnterpriseServer
      HostArn: arn:aws:codestar-connections:us-west-2:123456789123:host/abc123-example
      Tags:
      - Key: Project
        Value: ProjectB
```
