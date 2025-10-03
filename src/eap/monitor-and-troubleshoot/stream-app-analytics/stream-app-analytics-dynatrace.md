---
summary: Stream observability data from OutSystems Developer Cloud (ODC) apps to Dynatrace with required subscriptions and API tokens.
tags: observability data,dynatrace,api token,streaming setup,subscription
guid: 6dbc455b-8f0f-4b24-a10d-33c564d53835
locale: en-us
app_type: mobile apps,reactive web apps
platform-version: odc
figma: 
api-render: false
outsystems-tools:
  - odc portal
coverage-type:
  - apply
  - understand
content-type: 
audience:
  - platform administrators
  - infrastructure managers
  - tech leads
  - architects
helpids: 
---

# Stream observability data to Dynatrace

This article explains how you can stream observability data from ODC apps to the **Dynatrace** APM tool.

## Prerequisites

Before streaming observability data to **Dynatrace**, ensure you have a subscription to the **Analytics Stream**. Contact your account manager for provisioning.

## Set up streaming observability data to Dynatrace

To enable streaming observability data using **Dynatrace** as the destination tool, follow these steps:

1. Get the Dynatrace SaaS endpoint.

1. Get the Dynatrace API token (must have the ingest logs permissions).

Once you've completed these steps, go to the ODC Portal and [configure a stream](stream-app-analytics-configure.md). 

<div class="info" markdown="1">

Large 'content' and 'exception.stacktrace' attribute values are truncated to 4,000 characters before streaming. For more information regarding limits followed while streaming to Dynatrace's ingestion API, refer to Dynatrace's documentation on [Ingest OpenTelemetry logs](https://docs.dynatrace.com/docs/extend-dynatrace/opentelemetry/getting-started/logs/ingest#ingestion-limits).

</div>

## Additional resources

[Export with OLTP](https://www.dynatrace.com/support/help/extend-dynatrace/opentelemetry/getting-started/otlp-export)

## Related resources

* [Streaming observability data](stream-app-analytics-overview.md)

* [Streaming observability data to APM tools](stream-app-analytics-apm.md)

* [Set up the OpenTelemetry Collector](stream-app-analytics-opentelemetry.md)

* [Configure analytics streams in the ODC Portal](stream-app-analytics-configure.md)
