---
summary: Stream observability data from OutSystems Developer Cloud (ODC) apps to Splunk APM by setting up the HTTP Event Collector and OpenTelemetry Collector.
tags: observability data,streaming,splunk,opentelemetry
guid: 24060b42-fd25-47b6-a6ae-e3a85c46fc28
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
  - backend developers
  - data engineers
  - platform administrators
helpids: 
---

# Stream observability data to Splunk

This article explains how you can stream observability data from ODC apps to the **Splunk** APM tool.

## Prerequisites

Before streaming observability data to **Splunk**, ensure you have a subscription to the **App Analytics Stream**. Contact your account manager for provisioning.

## Set up streaming observability data to Splunk

To configure streaming observability data, using **Splunk** as the destination tool, follow these steps:

1. Set up the HTTP Event Collector on Splunk. 

    Refer to the instructions [here](https://docs.splunk.com/Documentation/Splunk/9.2.1/Data/UsetheHTTPEventCollector).

1. Set up the [OpenTelemetry Collector](stream-app-analytics-opentelemetry.md)

1. Configure a receiver that accepts HTTP or gRPC connections (refer to [OTLP Receiver](https://github.com/open-telemetry/opentelemetry-collector/blob/main/receiver/otlpreceiver/README.md) for an example) and that uses the Splunk Exporter 

    Refer to [Splunk HEC Example](https://github.com/signalfx/splunk-otel-collector/tree/main/examples/otel-logs-splunk) for an example.

1. Change the collector version to the most recent release in the **docker-compose.yml** file and change the image parameter [http://quay.io/signalfx/splunk-otel-collector:0.67.0](https://quay.io/repository/signalfx/splunk-otel-collector?tab=tags&tag=0.67.0) to the latest numerated image found.

1. Get the OpenTelemetry Collector endpoint and authentication credentials.

Once you've completed these steps, go to the ODC Portal and [configure a stream](stream-app-analytics-configure.md). 

## Additional resources

[Get started with the Splunk Distribution of the OpenTelemetry Collector](https://docs.splunk.com/observability/en/gdi/opentelemetry/opentelemetry.html)


## Related resources

* [Streaming observability data](stream-app-analytics-overview.md)

* [Streaming observability data to APM tools](stream-app-analytics-apm.md)

* [Set up the OpenTelemetry Collector](stream-app-analytics-opentelemetry.md)

* [Configure app analytics streams in Portal](stream-app-analytics-configure.md)
