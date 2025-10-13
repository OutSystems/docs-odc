---
summary: Set up the OpenTelemetry Collector in OutSystems platform for receiving logs in Datadog, Splunk, or Amazon S3.
tags: opentelemetry collector,apm tools,logs ingestion,datadog,splunk
guid: 9c440428-9e95-4e19-b96a-4bc0dd9ef098
locale: en-us
app_type: mobile apps,reactive web apps
platform-version: odc
figma:
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
# Set up the OpenTelemetry Collector

This article explains how to set up the OpenTelemetry collector for application performance monitoring (APM) tools that don't support native ingestion of OpenTelemetry data.

## Prerequisites

Before setting up the OpenTelemetry collector, ensure you have a subscription to the **Analytics Stream**. Contact your account manager for provisioning.

## Set up the OpenTelemetry collector

To receive logs in Datadog, Splunk, or Amazon S3, you must set up an OpenTelemetry Collector:

1. Download the latest release of the OpenTelemetry Collector Contrib distribution from [OpenTelemetry's GitHub repository](https://github.com/open-telemetry/opentelemetry-collector-releases/releases).  

1. Install and deploy the OpenTelemetry Collector.  

1. Set up the OpenTelemetry Collector.  

   Add the APM tool exporter and security information to the collector config file. The configuration information varies depending on the type of APM tool.  

1. Run the OpenTelemetry Collector.

<div class="info" markdown="1">

If the OpenTelemetry Collector implementation is OLTP over HTTP, according to the [OpenTelemetry specification](https://opentelemetry.io/docs/specs/otlp/#otlphttp-request), standard paths must be used. The URL provided in the ODC Portal will be automatically manipulated to send logs, traces, and metrics to the following distinct paths: Logs: `v1/logs` Traces: `v1/traces` Metrics: `v1/metrics` To avoid unexpected connection failure, you should keep track and renew the SSL/TLS certificate used in the OpenTelemetry collector before the expiration date.  

</div>

## Example file with a basic configuration

The following configuration provides a basic working example for **Datadog**. It secures the OpenTelemetry Collector with basic authentication.

Remember to edit the following:

* Replace **DD\_SITE** with your **Datadog site**. The default is **datadoghq.com**.  
* Replace **DD\_API\_KEY** with your **Datadog API key**.

```
 extensions: 
    basicauth/server:
       htpasswd:
         inline:
           user:password

 receivers: 
    otlp:
       protocols:
         grpc:
           auth:
              authenticator: basicauth/server
 
 exporters:
   datadog:
     api:
       site: <DD_SITE>
       key: <DD_API_KEY>

 service:
   extensions: [basicauth/server]
   pipelines:
     traces: 
       receivers: [otlp]
       exporters: [datadog]
     metrics:  
       receivers: [otlp]
       exporters: [datadog]
     logs:
       receivers: [otlp]
       exporters: [datadog]

```

## Related resources

* [Streaming observability data](stream-app-analytics-overview.md)

* [Streaming observability data to APM tools](stream-app-analytics-apm.md)  

* [Configure analytics streams in the ODC Portal](stream-app-analytics-configure.md)
