---
summary: OutSystems Developer Cloud(ODC) features server-side traces to monitor server-side elements
tags: server-side performance, error handling, server-side monitoring, debugging techniques
guid: 116ccfe6-45f1-420b-aca9-e4de767ae280
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3749-809&t=oLvR9wNssF7BzJFX-1
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
  - odc portal
content-type:
  - conceptual
  - process
---
# Server-side traces

Server-side traces help you analyze server-side execution. This provides insights into elements such as events or service actions. Use server-side traces to:

* Identify which [span](intro.md#spans) contains an error. Use the ODC Portal to find the root cause, then go to ODC Studio to fix it.
* Get detailed information about user interactions by monitoring requests.
* Understand the performance of each span in the app and its dependencies. Modify the elements associated with slower spans to improve the app's performance.

The following are different types of server-side traces:

* Consume REST API: Track request methods, durations, and URLs to identify performance issues or errors in API consumption.
* Entity Action: Track entity actions, such as create, read, update, and delete (CRUD) operations.
* Event: Track the sequence and duration of custom and system events.
* Expose REST API: Track performance and errors in exposed REST APIs, including request handling and response times.
* Screen Aggregate: Track the execution of aggregates on screens to identify slow queries or data retrieval issues affecting performance.
* Screen Data Action: Track the execution of data actions on screens to debug and optimize data fetching and manipulation.
* Service Action: Monitor the execution, performance, and errors in service actions.
* System Event: Monitor system events such as ApplicationReady and ApplicationResume.
* Timer: Track scheduled tasks, including execution duration and errors, to ensure timers run as expected.

For more information about backend traces, refer to [Traces](intro.md).

## Turn server-side traces on or off

All apps have their server-side traces on by default. Follow these steps to turn server-side traces off or on:

1. In the ODC portal, select Apps and choose the app for which you want to turn server-side traces on or off.\

1. Under the **Configuration** tab, go to **Monitoring & Troubleshooting**. Then, toggle **Capture server-side traces and metrics** to turn server-side traces on or off.

    ![Screenshot of deactivating server-side traces in ODC Portal.](images/disable-server-side-traces-pl.png "Activating Server-Side Traces in ODC Portal")
