> Source: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-multi-variant-feature-flags-rules-operators.html
> Downloaded: 2026-10-21

# Defining rules for multi-variant feature flags

A variant rule is an expression comprised of one or more operands and an operator. An operand is a specific value used during the evaluation of a rule. Operand values can be either static, such as a literal number or string, or variable, such as the value found in a context or the result of another expression. An operator, such as "greater than", is a test or action applied to its operands that produces a value. A variant rule expression must produce either a "true" or "false" to be valid.

Operands 
|  Type |  Description |  Example |    
|   

String  |   

A sequence of UTF-8 characters, enclosed in double-quotes.  |   

```
"apple", "Ḽơᶉëᶆ ȋṕšᶙṁ"
```
  |   
|   

Integer  |   

A 64-bit integer value.  |   

```
-7, 42 
```
  |   
|   

Float  |   

A 64-bit IEEE-754 floating-point value.  |   

```
3.14, 1.234e-5
```
  |   
|   

Timestamp  |   

A specific moment in time as described by the W3C note on date and time formats.  |   

```
2012-03-04T05:06:07-08:00, 2024-01
```
  |   
|   

Boolean  |   

A true or false value.  |   

```
true, false
```
  |   
|   

Context value  |   

A parameterized value in the form of $`key` that is retrieved from the context during rule evaluation.  |   

```
$country, $userId
```
  |   

Comparison operators 
|  Operator |  Description |  Example |    
|   

eq  |   

Determines whether a context value is equal to a given value.  |   

```
(eq $state "Virginia")
```
  |   
|   

gt  |   

Determines whether a context value is greater than a given value.  |   

```
(gt $age 65)
```
  |   
|   

gte  |   

Determines whether a context value is greater than or equal to a given value.  |   

```
(gte $age 65)
```
  |   
|   

lt  |   

Determines whether a context value is less than a given value.  |   

```
(lt $age 65)
```
  |   
|   

lte  |   

Determines whether a context value is less than or equal to a given value.  |   

```
(lte $age 65)
```
  |   

Logical operators 
|  Operator |  Description |  Example |    
|   

and  |   

Determines if both operands are true.  |   

```
(and 
    (eq $state "Virginia") 
    (gt $age 65)
)
```
  |   
|   

or  |   

Determines if at least one of the operands is true.  |   

```
(or
    (eq $state "Virginia") 
    (gt $age 65)
)
```
  |   
|   

not  |   

Reverses the value of an expression.  |   

```
(not (eq $state "Virginia"))
```
  |   

Custom operators 
|  Operator |  Description |  Example |    
|   

begins_with  |   

Determines whether a context value begins with a given prefix.  |   

```
(begins_with $state "A")
```
  |   
|   

ends_with  |   

Determines whether a context value ends with a given prefix.  |   

```
(ends_with $email "amazon.com")
```
  |   
|   

contains  |   

Determines whether a context value contains a given substring.  |   

```
(contains $promoCode "WIN")
```
  |   
|   

in  |   

Determines whether a context value is contained within a list of constants.  |   

```
(in $userId ["123", "456"])
```
  |   
|   

matches  |   

Determines whether a context value matches a given regex pattern.  |   

```
(matches in::$greeting pattern::"h.*y")
```
  |   
|   

exists  |   

Determines whether any value was provided for a context key.  |   

```
(exists key::"country")
```
  |   
|   

split  |   

Evaluates to `true` for a given percentage of traffic based on a consistent hash of the provided context value(s). For a detailed explanation of how `split` works, see the next section in this topic, Understanding the split operator. 

Note that `seed` is an optional property. If you don't specify `seed`, the hash is locally consistent, meaning traffic will be split consistently for that flag, but other flags receiving the same context value may split traffic differently. If `seed` is provided, each unique value is guaranteed to split traffic consistently across feature flags, configuration profiles, and AWS accounts.  |   

```
(split pct::10 by::$userId seed::"abc")
```
  |
