---
summary: Stream observability data from ODC apps to Elastic APM tool by configuring Elastic URL and Secret token in OutSystems Developer Cloud (ODC).
tags: observability data,elastic apm,streaming setup,opentelemetry
guid: 02175353-584b-47e2-b2ba-fc50e64b86eb
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

# Stream observability data to Elastic

This article explains how you can stream observability data from ODC apps to the Elastic APM tool.

## Prerequisites

Before streaming observability data to **Elastic**, ensure you have a subscription to the **Analytics Stream**. Contact your account manager for provisioning.

## Set up streaming observability data to Elastic

<div class="info" markdown="1">

* The Elastic Observability services and Kibana plugins must be deployed alongside the Elasticsearch cluster to complete the following steps. 

</div>

To enable streaming observability data using **Elastic** as the destination tool,  you need the **Elastic URL** and **Secret token** values. Once you have these, go to the ODC Portal and [configure a stream](stream-app-analytics-configure.md). 

## Additional resources

Here are some additional helpful documents, links, and articles:

* [Elastic Observability](https://www.elastic.co/observability)

* [OpenTelemetry integration in Elastic](https://www.elastic.co/guide/en/apm/guide/8.6/open-telemetry.html)

* [OpenTelemetry Collector configuration](https://opentelemetry.io/docs/collector/configuration/)


## Related resources

* [Streaming observability data](stream-app-analytics-overview.md)

* [Streaming observability data to APM tools](stream-app-analytics-apm.md)

* [Set up the OpenTelemetry Collector](stream-app-analytics-opentelemetry.md)

* [Configure analytics streams in the ODC Portal](stream-app-analytics-configure.md)
