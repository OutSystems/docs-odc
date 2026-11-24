---
guid: 28cb958d-4a47-442d-9e1a-8ad15d2d70ca
locale: en-us
summary: Understand which OutSystems Developer Cloud capabilities aren't available in ODC EU Sovereign Cloud at general availability.
figma:
coverage-type:
  - remember
  - understand
  - evaluate
topic:
  - eu-sovereign-cloud
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - Platform administrator
  - Tech lead
  - Architect
tags:
  - Architecture
  - Infrastructure
  - Logging
  - Monitoring
  - Performance
  - Private Gateway
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---

# ODC EU Sovereign Cloud limitations

ODC EU Sovereign Cloud doesn't include every capability available in standard ODC Cloud. Review these limitations before choosing ODC EU Sovereign Cloud, to confirm it fits your requirements. For what the offering does include, refer to [ODC EU Sovereign Cloud](esc-overview.md).

Most ODC Cloud add-ons, such as additional asset portfolios, additional non-production stages, AppShield, and compute and database add-ons, are also available for ODC EU Sovereign Cloud.

## Platform capabilities

The following platform capabilities differ from standard ODC Cloud:

| Capability | ODC EU Sovereign Cloud | ODC Cloud |
| --- | --- | --- |
| Compute and scalability | Fixed capacity with hard limits | Automatic scaling with soft limits |
| App observability | Application logs and traces are sent in OpenTelemetry format to an EU-hosted APM. | Full observability in ODC Cloud |
| External data connectivity | Data Fabric only | Data Fabric, plus Private Gateway for secure connectivity |

Compute, database compute, and database storage add-ons are provisioned in fixed tiers rather than scaled continuously, so plan your capacity around the nearest tier above your expected usage.

## Capabilities not available

The following capabilities aren't available in ODC EU Sovereign Cloud:

* High availability
* Sentry
* App Analytics streaming
* Extended custom code execution duration
* Private Gateway
* Semantic Search
* AI Guardrails
* Agent Evaluations
* File data type
* 24x7 support

For the support hours and service levels that apply, refer to [Support terms and service level agreements (SLA)](https://www.outsystems.com/legal/success/support-terms-and-service-level-agreements-sla-of-the-outsystems-software).

## Subscription console usage data

The Subscription Console doesn't show real compute and add-on usage data for ODC EU Sovereign Cloud tenants, since this infrastructure isn't metered through that system.

## Related resources

Refer to the following resources for related concepts:

* [ODC EU Sovereign Cloud](esc-overview.md)
* [Shared responsibility model for ODC EU Sovereign Cloud](esc-shared-responsibility.md)
