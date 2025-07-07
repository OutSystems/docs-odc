---
summary: Learn how to stream observability data from ODC to Amazon S3 by setting up the OpenTelemetry Collector and configuring the log streaming service.
tags: aws s3, opentelemetry, observability
guid: 96ba49a9-328c-49ca-8530-d61b9a1a7cfe
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
outsystems-tools: 
  - odc portal
coverage-type:
  - apply 
figma: 
content-type: 
  - procedure
audience: 
  - platform administrators
  - infrastructure managers
  - tech leads
  - architects
---

# Stream observability data to Amazon S3

This article explains how you can stream observability data from ODC apps to **Amazon S3**.

## Prerequisites

Before streaming observability data to **Amazon S3**, ensure you have a subscription to the **App Analytics Stream**. Contact your account manager for provisioning.

<div class="info" markdown="1">

Stream to Amazon S3 requires an [OpenTelemetry Collector](stream-app-analytics-opentelemetry.md) with a specific [AWS S3 contrib exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/awss3exporter#aws-s3-exporter-for-opentelemetry-collector/). As of June 2024, the [AWS S3 contrib exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/awss3exporter#aws-s3-exporter-for-opentelemetry-collector/) is in [Alpha stability](https://github.com/open-telemetry/opentelemetry-collector#alpha/). Customers are advised to assess their use case and learn more before adopting it.

</div>

## Set up streaming observability data to Amazon S3

To set up streaming observability data, using **Amazon S3** as the destination storage, follow these steps:

1. Set up the [OpenTelemetry Collector](stream-app-analytics-opentelemetry.md).

1. Configure a receiver that accepts HTTP or gRPC connections and uses the [AWS S3 contrib exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/awss3exporter#aws-s3-exporter-for-opentelemetry-collector/).

1. Get the OpenTelemetry Collector endpoint and authentication credentials.

Once you've completed these steps, go to the ODC Portal and [configure a stream](stream-app-analytics-configure.md). 

## Additional resources

Here are some additional helpful documents:

* [OpenTelemetry Collector contrib exporter for Amazon S3](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/awss3exporter#aws-s3-exporter-for-opentelemetry-collector/)

* [OpenTelemetry Collector configuration](https://opentelemetry.io/docs/collector/configuration/)

## Related resources

* [Streaming observability data](stream-app-analytics-overview.md)

* [Streaming observability data to APM tools](stream-app-analytics-apm.md)

* [Set up the OpenTelemetry Collector](stream-app-analytics-opentelemetry.md)

* [Configure app analytics streams in Portal](stream-app-analytics-configure.md)


