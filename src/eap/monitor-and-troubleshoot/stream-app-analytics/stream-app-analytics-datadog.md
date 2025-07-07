---
summary: Stream observability data from ODC apps to Datadog APM by configuring the OpenTelemetry Collector.
tags: observability data,datadog,opentelemetry
guid: 20f1240d-56e7-4a1a-a3db-a800e9799d6d
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
  - data engineers
  - platform administrators
helpids: 
---

# Stream observability data to Datadog

This article explains how you can stream observability data from ODC apps to the **Datadog** APM tool.

## Prerequisites

Before streaming observability data to **Datadog**, ensure you have a subscription to the **App Analytics Stream**. Contact your account manager for provisioning.

## Set up streaming observability data to Datadog

To configure streaming observability data, using **Datadog** as the destination tool, follow these steps:

1. Get the Datadog API key.

1. Set up the [OpenTelemetry Collector](stream-app-analytics-opentelemetry.md) with Datadog as the exporter.

1. Get the OpenTelemetry Collector endpoint and authentication credentials.

Once you've completed these steps, go to the ODC Portal and [configure a stream](stream-app-analytics-configure.md). 

## Additional resources

Here are some additional helpful documents, links, and articles:

* [Datadog API and Application Keys](https://docs.datadoghq.com/account_management/api-app-keys/)

* [OpenTelemetry in Datadog](https://docs.datadoghq.com/opentelemetry/)

* [OpenTelemetry Collector configuration](https://opentelemetry.io/docs/collector/configuration/)

## Related resources

* [Streaming observability data](stream-app-analytics-overview.md)

* [Streaming observability data to APM tools](stream-app-analytics-apm.md)

* [Set up the OpenTelemetry Collector](stream-app-analytics-opentelemetry.md)

* [Configure streams in the ODC Portal](stream-app-analytics-configure.md)
