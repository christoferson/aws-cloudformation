> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-daemon.html
> Downloaded: 2026-10-20

# AWS::ECS::Daemon

Information about a daemon resource.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::ECS::Daemon",
  "Properties" : {
      "CapacityProviderArns" : [ String, ... ],
      "ClusterArn" : String,
      "Critical" : Boolean,
      "DaemonName" : String,
      "DaemonTaskDefinitionArn" : String,
      "DeploymentConfiguration" : DaemonDeploymentConfiguration,
      "EnableECSManagedTags" : Boolean,
      "EnableExecuteCommand" : Boolean,
      "PropagateTags" : String,
      "Tags" : [ Tag, ... ]
    }
}

```

### YAML

```
Type: AWS::ECS::Daemon
Properties:
  CapacityProviderArns: 
    - String
  ClusterArn: String
  Critical: Boolean
  DaemonName: String
  DaemonTaskDefinitionArn: String
  DeploymentConfiguration: 
    DaemonDeploymentConfiguration
  EnableECSManagedTags: Boolean
  EnableExecuteCommand: Boolean
  PropagateTags: String
  Tags: 
    - Tag

```

## Properties

**`CapacityProviderArns`** 

The Amazon Resource Names (ARNs) of the capacity providers associated with the daemon. 

Required: No

Type: Array of String

Minimum: `1`

Update requires: No interruption

**`ClusterArn`** 

The Amazon Resource Name (ARN) of the cluster that the daemon is running in. 

Required: No

Type: String

Update requires: Replacement

**`Critical`** 

If the `critical` parameter of this daemon revision is `true`, and the daemon task fails, stops, or becomes unhealthy, Amazon ECS drains the container instance and stops the other tasks running on it. If the parameter is `false`, the daemon task failure doesn't affect the other tasks on the instance, and doesn't block instance registration. The default value is `true`. 

Required: No

Type: Boolean

Update requires: No interruption

**`DaemonName`**

Property description not available.

Required: No

Type: String

Update requires: Replacement

**`DaemonTaskDefinitionArn`** 

The Amazon Resource Name (ARN) of the daemon task definition used by this revision. 

Required: No

Type: String

Update requires: No interruption

**`DeploymentConfiguration`** 

The deployment configuration used for this daemon deployment. 

Required: No

Type: DaemonDeploymentConfiguration

Update requires: No interruption

**`EnableECSManagedTags`** 

Specifies whether Amazon ECS managed tags are turned on for the daemon tasks. 

Required: No

Type: Boolean

Update requires: No interruption

**`EnableExecuteCommand`** 

Specifies whether the execute command functionality is turned on for the daemon tasks. 

Required: No

Type: Boolean

Update requires: No interruption

**`PropagateTags`** 

Specifies whether tags are propagated from the daemon to the daemon tasks. 

Required: No

Type: String

Allowed values: `DAEMON | NONE`

Update requires: No interruption

**`Tags`**

Property description not available.

Required: No

Type: Array of Tag

Update requires: No interruption

## Return values

### Ref

### Fn::GetAtt

#### 

**`CreatedAt`** 

The Unix timestamp for the time when the daemon was created. 

**`DaemonArn`** 

The Amazon Resource Name (ARN) of the daemon. 

**`DaemonStatus`** 

The status of the daemon. 

**`DeploymentArn`** 

The Amazon Resource Name (ARN) of the most recent daemon deployment. 

**`UpdatedAt`** 

The Unix timestamp for the time when the daemon was last updated.
