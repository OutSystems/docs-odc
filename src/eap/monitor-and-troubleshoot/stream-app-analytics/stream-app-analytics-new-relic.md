---
summary: Stream observability data from OutSystems Developer Cloud (ODC) apps to New Relic using the App Analytics Stream subscription.
tags: observability data,new relic,apm tool,opentelemetry,api keys
guid: 0142e89a-6164-41b9-bf04-3e41868496b8
locale: en-us
app_type: mobile apps,reactive web apps
platform-version: odc
figma: 
api-render: false
outsystems-tools:
  - odc portal
coverage-type:
  - apply
content-type: 
audience:
  - backend developers
  - platform administrators
  - tech leads
helpids: 
---

# Stream observability data to New Relic

This article explains how you can stream observability data from ODC apps to the **New Relic** APM tool.

## Prerequisites

Before streaming observability data to **New Relic**, ensure you have a subscription to the **App Analytics Stream**. Contact your account manager for provisioning.

## Set up streaming observability data to New Relic

To enable streaming observability data using **New Relic** as the destination tool, you must retrieve the New Relic API key and the location for the **New Relic** account (U.S. or EU).

Once you have these values, go to the ODC Portal and [configure a stream](stream-app-analytics-configure.md).

<div class="info" markdown="1">

Large ``message`` and ``exception.stacktrace`` attribute values are truncated to 4,000 characters before streaming in order to follow New Relic's ingestion API limits. For more information, refer to New Relic's documentation on [Send custom events with our Event API](https://docs.newrelic.com/docs/data-apis/ingest-apis/event-api/introduction-event-api/#limits).

</div>

## Additional resources

Here are some additional helpful documentation, links, and articles:

* [New Relic API keys](https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/)

* [Getting started with OpenTelemetry](https://docs.newrelic.com/docs/opentelemetry/get-started/opentelemetry-get-started-intro/)

* [OpenTelemetry Collector configuration](https://opentelemetry.io/docs/collector/configuration/)


## Related resources

* [Streaming observability data](stream-app-analytics-overview.md)

* [Streaming observability data to APM tools](stream-app-analytics-apm.md)

* [Set up the OpenTelemetry Collector](stream-app-analytics-opentelemetry.md)

* [Configure app analytics streams in Portal](stream-app-analytics-configure.md)

