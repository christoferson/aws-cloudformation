> Source: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-multi-variant-feature-flags-rules.html
> Downloaded: 2026-10-21

# Understanding multi-variant feature flag rules

When you create a feature flag variant, you specify a rule for it. Rules are expressions that take context values as input and produce a boolean result as output. For example, you could define a rule to select a flag variant for beta users, identified by their account ID, testing a user interface refresh. For this scenario, you do the following: 
Create a new feature flag configuration profile called UI Refresh. 
Create a new feature flag called ui_refresh. 
Edit the feature flag after you create it to add variants. 
Create and enable a new variant called BetaUsers. 
Define a rule for BetaUsers that selects the variant if the account ID from the request context is in a list of account IDs approved to view the new beta experience. 
Confirm that the default variant’s status is set to Disabled. 
Note

Variants are evaluated as an ordered list based on the order they are defined in the console. The variant at the top of the list is evaluated first. If no rules match the supplied context, AWS AppConfig returns the Default variant.

When AWS AppConfig processes the feature flag request, it compares the supplied context, which includes the AccountID (for this example) to the BetaUsers variant first. If the context matches the rule for BetaUsers, AWS AppConfig returns the configuration data for the beta experience. If the context doesn’t include an account ID or if the account ID ends in anything other than 123, AWS AppConfig returns configuration data for the Default rule, which means the user views the current experience in production.Note

For information about retrieving multi-variant feature flags, see Retrieving basic and multi-variant feature flags. 

## Understanding the split operator 

The following section describes how the `split` operator behaves when used in different scenarios. As a reminder, `split` evaluates to `true` for a given percentage of traffic based on a consistent hash of the provided context value. To understand this better, consider the following baseline scenario that uses split with two variants: 

```
A: (split by::$uniqueId pct::20)
C: <no rule>
```
 

As expected, providing a random set of `uniqueId` values produces a distribution that's approximately: 

```
A: 20%
C: 80%
```
 

If you add a third variant, but use the same split percentage like so: 

```

A: (split by::$uniqueId pct::20)
B: (split by::$uniqueId pct::20)
C: <default>
```
 

You end up with the following distribution: 

```
A: 20%
B: 0%
C: 80%
```
 

This potentially unexpected distribution happens because each variant rule is evaluated in order and the first match determines the returned variant. When rule A is evaluated, 20% of `uniqueId` values match it, so the first variant is returned. Next, rule B is evaluated. However, all of the `uniqueId` values that would have matched the second split statement were already matched by variant rule A, so no values match B. The default variant is returned instead. 

Now consider a third example. 

```
A: (split by::$uniqueId pct::20)
B: (split by::$uniqueId pct::25)
C: <default>
```
 

As with the previous example, the first 20% of `uniqueId` values match rule A. For variant rule B, 25% of all `uniqueId` values would match, but most of those previously matched rule A. That leaves 5% of the total for variant B, with the remainder receiving variant C. The distribution would look like the following: 

```
A: 20%
B: 5%
C: 75%
```
 Using the `seed` property 

You can use the `seed` property to ensure traffic is split consistently for a given context value irrespective of where the split operator is used. If you don't specify `seed`, the hash is locally consistent, meaning traffic will be split consistently for that flag, but other flags receiving the same context value may split traffic differently. If `seed` is provided, each unique value is guaranteed to split traffic consistently across feature flags, configuration profiles, and AWS accounts. 

Typically, customers use the same `seed` value across variants within a flag when splitting traffic on the same context property. However, it may occasionally make sense to use a different seed value. Here is an example that uses different seeds for rules A and B: 

```
A: (split by::$uniqueId pct::20 seed::"seed_one")
B: (split by::$uniqueId pct::25 seed::"seed_two")
C: <default>
```
 

As before, 20% of the matching `uniqueId` values match rule A. That means 80% of values fall through and are tested against variant rule B. Because the seed is different, there is no correlation between the values that matched A and the values that match B. There are, however, only 80% as many `uniqueId` values to split with 25% of that number matching rule B and 75% not. That works out to the following distribution: 

```
A: 20%
B: 20% (25% of what falls through from A, or 25% of 80%) 
C: 60%
```
