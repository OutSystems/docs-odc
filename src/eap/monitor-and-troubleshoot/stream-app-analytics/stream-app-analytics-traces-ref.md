---
summary: Stream trace span attributes from OutSystems Developer Cloud (ODC) to APM tools, including span ID, name, duration, and HTTP method.
tags: trace span,apm tools,data type,execution duration
guid: 5f974b57-1381-4552-b535-e127e122b9f1
locale: en-us
app_type: mobile apps,reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - none
coverage-type:
  - apply
  - remember
content-type:
audience:
  - platform administrators
  - infrastructure managers
  - tech leads
  - architects
helpids:
---
# Streamed trace data

The following table lists the trace span attributes that are streamed from your ODC app to APM tools.

|                             |               |                                                            |
| --------------------------- | ------------- | ---------------------------------------------------------- |
| **Attribute name**          | **Data type** | **Description**                                            |
| id                          | String        | Span ID                                                    |
| name                        | String        | Name of the span                                           |
| span\_id                    | GUID          | Span ID                                                    |
| trace\_id                   | GUID          | Trace ID                                                   |
| parent\_id                  | String        | Parent span ID                                             |
| span\_kind                  | String        | Span type. Example: server, internal                       |
| duration\_ms                | Decimal       | Duration of the execution in milliseconds                  |
| db\_statement               | String        | SQL query statement involved in the execution              |
| code\_function              | String        | Function name                                              |
| http\_request\_method       | String        | Request method. Example: POST, GET                         |
| http.response.status\_code​  | Int           | HTTP status code for the response                          |
| url\_path                   | String        | Path of request                                            |
| endpoint                    | String        | Path of request                                            |
| outsystems\_tenant\_key     | GUID          | ID of the tenant where the message is logged               |
| outsystems\_env\_key        | GUID          | ID of the tenant stage where the message is logged.        |
| outsystems\_app\_key        | GUID          | ID of the app where the message is logged                  |
| outsystems\_app\_name       | String        | Name of the app where the message is logged                |
| outsystems\_app\_version    | String        | Version of the app where the message is logged             |
| outsystems\_app\_revision   | Int           | ID of the application revision where the message is logged |
| outsystems\_service\_type   | String        | Type of service involved in the execution                  |
| outsystems\_service\_name   | String        | Name of the service involved in the execution              |

## Related resources

* [Streamed log data](stream-app-analytics-log-ref.md)

* [Streamed metric data](stream-app-analytics-metrics-ref.md)
