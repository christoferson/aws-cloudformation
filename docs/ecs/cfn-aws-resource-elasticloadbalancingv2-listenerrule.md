> Source: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listenerrule.html
> Downloaded: 2026-10-18

# AWS::ElasticLoadBalancingV2::ListenerRule

Specifies a listener rule. The listener must be associated with an Application Load Balancer. Each rule consists of a priority, one or more actions, and one or more conditions.

For more information, see Quotas for your Application Load Balancers in the User Guide for Application Load Balancers.

## Syntax

To declare this entity in your CloudFormation template, use the following syntax:

### JSON

```
{
  "Type" : "AWS::ElasticLoadBalancingV2::ListenerRule",
  "Properties" : {
      "Actions" : [ Action, ... ],
      "Conditions" : [ RuleCondition, ... ],
      "ListenerArn" : String,
      "Priority" : Integer,
      "Tags" : [ Tag, ... ],
      "Transforms" : [ Transform, ... ]
    }
}

```

### YAML

```
Type: AWS::ElasticLoadBalancingV2::ListenerRule
Properties:
  Actions: 
    - Action
  Conditions: 
    - RuleCondition
  ListenerArn: String
  Priority: Integer
  Tags: 
    - Tag
  Transforms: 
    - Transform

```

## Properties

**`Actions`** 

The actions. 

The rule must include exactly one of the following types of actions: `forward`, `fixed-response`, or `redirect`, and it must be the last action to be performed. If the rule is for an HTTPS listener, it can also optionally include an authentication action. 

Required: Yes

Type: Array of Action

Update requires: No interruption

**`Conditions`** 

The conditions. 

The rule can optionally include up to one of each of the following conditions: `http-request-method`, `host-header`, `path-pattern`, and `source-ip`. A rule can also optionally include one or more of each of the following conditions: `http-header` and `query-string`. 

Required: Yes

Type: Array of RuleCondition

Update requires: No interruption

**`ListenerArn`** 

The Amazon Resource Name (ARN) of the listener. 

Required: No

Type: String

Update requires: Replacement

**`Priority`** 

The rule priority. A listener can't have multiple rules with the same priority. 

If you try to reorder rules by updating their priorities, do not specify a new priority if an existing rule already uses this priority, as this can cause an error. If you need to reuse a priority with a different rule, you must remove it as a priority first, and then specify it in a subsequent update. 

Required: Yes

Type: Integer

Minimum: `1`

Maximum: `50000`

Update requires: No interruption

**`Tags`**

Property description not available.

Required: No

Type: Array of Tag

Update requires: No interruption

**`Transforms`**

Property description not available.

Required: No

Type: Array of Transform

Update requires: No interruption

## Return values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the listener rule.

For more information about using the `Ref` function, see `Ref`.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using the `Fn::GetAtt` intrinsic function, see `Fn::GetAtt`.

#### 

**`IsDefault`** 

Indicates whether this is the default rule. 

**`RuleArn`** 

The Amazon Resource Name (ARN) of the rule. 

## Examples

You can define rules for your listener in addition to the default action. Each rule must specify an action and a condition. 
Forward action with a host-header condition
Fixed-response action with a source-ip condition
Redirect action with an http-header condition
 

### Forward action with a host-header condition

The following example creates a rule with a `forward` action and a `host-header` condition.

#### YAML

```
myForwardListenerRule:
   Type: 'AWS::ElasticLoadBalancingV2::ListenerRule'
   Properties:
     ListenerArn: !Ref myListener
     Priority: 10
     Conditions:
       - Field: host-header
         Values:
           - example.com
           - www.example.com
     Actions:
       - Type: forward
         TargetGroupArn: !Ref myTargetGroup
```

#### JSON

```
{
    "myForwardListenerRule": {
        "Type": "AWS::ElasticLoadBalancingV2::ListenerRule",
        "Properties": {
            "ListenerArn": {
                "Ref": "myListener"
            },
            "Priority": 10,
            "Conditions": [
                {
                    "Field": "host-header",
                    "Values": [
                        "example.com",
                        "www.example.com"
                    ]
                }
            ],
            "Actions": [
                {
                    "Type": "forward",
                    "TargetGroupArn": {
                        "Ref": "myTargetGroup"
                    }
                }
            ]
        }
    }
}
```
 

### Fixed-response action with a source-ip condition

The following example creates a rule with a `fixed-response` action and a `source-ip` condition.

#### YAML

```
myFixedResponseListenerRule:
   Type: 'AWS::ElasticLoadBalancingV2::ListenerRule'
   Properties:
     ListenerArn: !Ref myListener
     Priority: 20
     Conditions:
       - Field: source-ip
         SourceIpConfig:
           Values:
             - 192.168.1.0/24
             - 10.0.0.0/16
     Actions:
       - Type: fixed-response
         FixedResponseConfig:
           StatusCode: 403
           ContentType: text/plain
           MessageBody: "Access denied"
```

#### JSON

```
{
    "myFixedResponseListenerRule": {
        "Type": "AWS::ElasticLoadBalancingV2::ListenerRule",
        "Properties": {
            "ListenerArn": {
                "Ref": "myListener"
            },
            "Priority": 20,
            "Conditions": [
                {
                    "Field": "source-ip",
                    "SourceIpConfig": {
                        "Values": [
                            "192.168.1.0/24",
                            "10.0.0.0/16"
                        ]
                    }
                }
            ],
            "Actions": [
                {
                    "Type": "fixed-response",
                    "FixedResponseConfig": {
                        "StatusCode": 403,
                        "ContentType": "text/plain",
                        "MessageBody": "Access denied"
                    }
                }
            ]
        }
    }
}
```
 

### Redirect action with an http-header condition

The following example creates a rule with a `redirect` action and an `http-header` condition.

#### YAML

```
myRedirectListenerRule:
   Type: 'AWS::ElasticLoadBalancingV2::ListenerRule'
   Properties:
     ListenerArn: !Ref myListener
     Priority: 30
     Conditions:
       - Field: http-header
         HttpHeaderConfig:
           HttpHeaderName: User-Agent
           Values: 
             - "*Mobile*"
             - "*Android*"
             - "*iPhone*"
     Actions:
       - Type: redirect
         RedirectConfig:
           Host: m.example.com
           StatusCode: HTTP_302
```

#### JSON

```
{
    "myRedirectListenerRule": {
        "Type": "AWS::ElasticLoadBalancingV2::ListenerRule",
        "Properties": {
            "ListenerArn": {
                "Ref": "myListener"
            },
            "Priority": 30,
            "Conditions": [
                {
                    "Field": "http-header",
                    "HttpHeaderConfig": {
                        "HttpHeaderName": "User-Agent",
                        "Values": [
                            "*Mobile*",
                            "*Android*",
                            "*iPhone*"
                        ]
                    }
                }
            ],
            "Actions": [
                {
                    "Type": "redirect",
                    "RedirectConfig": {
                        "Host": "m.example.com",
                        "StatusCode": "HTTP_302"
                    }
                }
            ]
        }
    }
}
```
 

## See also 
CreateRule in the Elastic Load Balancing API Reference (version 2015-12-01) 
Listener Rules in the User Guide for Application Load Balancers
