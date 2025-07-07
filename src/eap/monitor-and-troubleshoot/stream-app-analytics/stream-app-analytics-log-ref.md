---
summary: Log attributes streamed from OutSystems Developer Cloud (ODC) apps to APM tools include details like action name, app key, timer name, and trace ID.
tags: log attributes,apm tools,app logging,trace id
guid: 277b6c56-aff5-4d8d-9fa7-9711ffd47c4d
locale: en-us
app_type: mobile apps,reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - none
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
# Streamed log data

The following table lists the log attributes that are streamed from your ODC app to APM tools. 

| **Attribute name**        | **Data type** | **Description**                                            |
| ------------------------- | ------------- | ---------------------------------------------------------- |
| Action\_Name              | String        | Name of the action being called                            |
| TimerName                 | String        | Name of the timer being called                             |
| message                   | String        | Log message                                                |
| outsystems\_app\_key      | GUID          | ID of the app where the message is logged                  |
| outsystems\_app\_name     | String        | Name of the application where the message is logged        |
| outsystems\_app\_version  | String        | Version of the app where the message is logged             |
| outsystems\_app\_revision | Int           | ID of the application revision where the message is logged |
| outsystems\_tenant\_key   | GUID          | ID of the tenant where the message is logged               |
| outsystems\_env\_key      | GUID          | ID of the tenant stage where the message is logged         |
| span\_id                  | GUID          | Span ID associated with the log record                     |
| trace\_id                 | GUID          | Trace ID associated with the log record                    |
| outsystems\_timer\_key    | GUID          | ID of the timer where the message is logged                |
| service\_name             | String        | Name of the service where the message is logged            |
| RequestPath               | String        | Path of the request that originated the log                |
| exception\_stacktrace     | String        | Stack trace from the error                                 |
| exception\_message        | String        | Error message                                              |


## Related resources

* [Streamed trace data](stream-app-analytics-traces-ref.md)

* [Streaming metrics data](stream-app-analytics-metrics-ref.md)
