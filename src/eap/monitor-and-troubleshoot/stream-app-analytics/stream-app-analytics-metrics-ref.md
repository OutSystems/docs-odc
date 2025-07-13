---
summary: Streamed metrics data attributes from OutSystems Developer Cloud (ODC) to APM tools include status, tenant key, and various app and agent details.
tags: metrics data,attribute list,apm integration,app details,agent details
guid: 53d9c0ea-11bd-41d9-b4e2-74eb5c3076b8
locale: en-us
app_type: mobile apps,reactive web apps
platform-version: odc
figma: 
api-render: false
outsystems-tools:
  - odc portal
coverage-type:
  - remember
  - understand
content-type: 
audience:
  - platform administrators
  - infrastructure managers
  - tech leads
  - architects
helpids: 
---

# Streamed metrics data

OutSystems Developer Cloud (ODC) automatically streams performance metrics from your apps to Application Performance Monitoring (APM) tools, enabling real-time monitoring and analysis. These metrics provide visibility into request patterns, response times, and system invocations across your architecture. The streamed data includes both high-level counters and detailed timing distributions to help you identify performance bottlenecks and optimize your applications. All metrics are prefixed with ``outsystems`` to clearly distinguish them from other telemetry data in your APM environment.

The following metrics are streamed from your ODC app to APM tools:

* `outsystems_total_requests`
* `outsystems_request_duration_millis`
* `outsystems_total_invocations`
* `outsystems_invocation_duration_millis`

For more information about these metrics, refer to the [Streamed metrics table](#streamed-metrics).

These metrics streamed from your ODC app to APM tools have metric-specific attributes. For more information about the `outsystems_total_requests` and `outsystems_request_duration_millis` specific attributes, refer to the [Request attributes table](#request-attributes). For more information about `outsystems_total_invocations` and `outsystems_invocation_duration_millis` specific attributes, refer to the [Invocation attributes table](#invocation-attributes).

Additionally, all of these metrics share common resource attributes. Resource attributes are key-value pairs that describe the entity producing telemetry data (for example, a service, host, or container), providing essential context for filtering, grouping, and analyzing metrics, traces, and logs in APM tools. For more information about these common resource attributes, refer to the [Resource attributes table](#resource-attributes).


## Streamed metrics

The following table outlines the metrics streamed from your ODC app to APM tools.

|                             |           |                                        |
| --------------------------- | --------- | -------------------------------------- |
| **Metric name**             | **Type**  | **Description**                        |
|  `outsystems_total_requests`  |  `Counter`   | Number of requests made to any asset, originating from elements, such as `SCREEN`, `REST_EXPOSE_ACTION`, `SERVICE_ACTION`, `TIMER`, `GLOBAL_EVENT_HANDLER` |
|  `outsystems_request_duration_millis`    |  `Histogram` |  Number of requests made to any asset, originating from elements such as `SCREEN`, `REST_EXPOSE_ACTION`, `SERVICE_ACTION`, `TIMER`, `GLOBAL_EVENT_HANDLER` distributed into millisecond buckets. |
|  `outsystems_total_invocations`  |  `Counter`   |  Number of invocations of  elements such as `REST_CONSUME_ACTION, SERVICE_ACTION_CALL, SCREEN_SERVICE_AGGREGATE, SCREEN_SERVICE_DATA_ACTION, SERVER_QUERY_AGGREGATE, SERVER_QUERY_SQL, SERVER_ENTITY_ACTION, SERVER_QUERY_EXTERNAL_ACTION, EXTERNAL_LIBRARY_ACTION, SEND_EMAIL, GLOBAL_EVENT_TRIGGER`  |
|  `outsystems_invocation_duration_millis` |  `Histogram` |  Number of invocations elements such as `REST_CONSUME_ACTION, SERVICE_ACTION_CALL, SCREEN_SERVICE_AGGREGATE, SCREEN_SERVICE_DATA_ACTION, SERVER_QUERY_AGGREGATE, SERVER_QUERY_SQL, SERVER_ENTITY_ACTION, SERVER_QUERY_EXTERNAL_ACTION, EXTERNAL_LIBRARY_ACTION, SEND_EMAIL, GLOBAL_EVENT_TRIGGER` distributed into millisecond buckets. |

# Request attributes

The following table outlines the request attributes streamed from your ODC app to APM tools for the `outsystems_total_requests` and `outsystems_request_duration_millis` metrics.

|                                |                              | 
| ------------------------------ | ---------------------------- |
|  **Attribute name**            | **Possible values/Example**  |
| `status`                       | <li>`success`</li> <li>`failure` </li>   | 
| `outsystems.element.type`      | <li>`REST_EXPOSE_ACTION` (`Backend Runtime`)</li><li>`SERVICE_ACTION` (`Backend Runtime`)</li><li>`TIMER` (`Backend Runtime`)</li><li>`GLOBAL_EVENT_HANDLER` (`Backend Runtime`) </li>| 
|`outsystems.origin.element.name` |  `OnClickAction` | 
| `outsystems.origin.element.key` |  `bc82cc28-6ad4-4cd2-ac6c-a584330d1291.ac82cc28-6ad4-4cd2-ac6c-a584330d1292` |
| `outsystems.element.name`  |  `LandingScreen`      | 
| `outsystems.element.key`   | `bc82cc28-6ad4-4cd2-ac6c-a584330d1291.bc82cc28-6ad4-4cd2-ac6c-a584330d1293`      |
| `country`                           | `PT`    | 
| `browser`                           | <li> `Chrome`</li><li>`Safari`</li><li> `Edge`</li><li>`Firefox`</li><li> `Opera`</li><li>`Other` </li>  |

### Invocation attributes

The following table outlines the invocation attributes streamed from your ODC app to APM tools for the `outsystems_total_invocations` and `outsystems_invocation_duration_millis` metrics.

|                                       |                                |                  
| ------------------------------------- | ------------------------------ | 
|  **Attribute name**                   |  **Possible values/Example**   | 
|  `status`                            | <li> `success`</li><li> `failure`  </li>   |  
|  `outsystems.element.type`           | <li>`REST_CONSUME_ACTION`</li><li> `SERVICE_ACTION_CALL`</li><li> `SCREEN_SERVICE_AGGREGATE`</li><li>`SCREEN_SERVICE_DATA_ACTION`</li><li> `SERVER_QUERY_AGGREGATE`</li><li>`SERVER_QUERY_SQL`</li><li>`SERVER_ENTITY_ACTION`</li><li>`SERVER_QUERY_EXTERNAL_ACTION`</li><li>`EXTERNAL_LIBRARY_ACTION`</li><li>`SEND_EMAIL`</li><li>`GLOBAL_EVENT_TRIGGER`</li> | 
|  `outsystems.element.name`   | `FetchOrders`   | 
| `outsystems.element.key` | `bc82cc28-6ad4-4cd2-ac6c-a584330d1291.bc82cc28-6ad4-4cd2-ac6c-a584330d1293`|

# Resource attributes

The following table details the common resource attributes streamed from your ODC app to APM tools.

|                             |           |                                        |
| --------------------------- | --------- | -------------------------------------- |
| **Name**                    | **Type**  | **Possible values/Example**            |
| `service.name`              | `string`  | `App Name`                             |
| `outsystems.tenant.key`     | `guid`    | `43814ec0-70cf-4460-ad02-077ef7a4cb3c` |
| `outsystems.env.key`        | `guid`    | `ee835ae5-9100-4792-bb6f-cb1c0907ebc0` |
| `outsystems.workload.type`  | `string`  | `app`, `agent`                         |
| `outsystems.app.key`        | `guid`    | `Bc82cc28-6ad4-4cd2-ac6c-a584330d1291` |
| `outsystems.app.name`       | `string`  | `App Name`                             |
| `outsystems.app.revision`   | `integer` | `4`                                    |
| `outsystems.agent.key`      | `guid`    | `Bc82cc28-6ad4-4cd2-ac6c-a584330d1291` |
| `outsystems.agent.name`     | `string`  | `Agent Name`                           |
| `outsystems.agent.revision` | `integer` | `5`                                    |
| `ring`                      | `string`  | `Ga`                                   |
| `stamp`                     | `string`  | `Runp-ga-eu-ce-1-01`                   |

## Related resources

* [Streamed log data](stream-app-analytics-log-ref.md)

* [Streamed trace data](stream-app-analytics-traces-ref.md)
