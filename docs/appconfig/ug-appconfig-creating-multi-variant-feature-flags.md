> Source: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-multi-variant-feature-flags.html
> Downloaded: 2026-10-21

# Creating multi-variant feature flags

Feature flag variants enable you to define a set of possible flag values to return for a request. You can also configure different statuses (enabled or disabled) for multi-variant flags. When requesting a flag configured with variants, your application provides context that AWS AppConfig evaluates against a set of user-defined rules. Depending on the context specified in the request and the rules defined for the variant, AWS AppConfig returns different flag values to the application.

The following screenshot shows an example of a feature flag with three user-defined variants and the default variant.  Topics
Understanding multi-variant feature flag concepts and common use cases
Understanding multi-variant feature flag rules
Creating a multi-variant feature flag
