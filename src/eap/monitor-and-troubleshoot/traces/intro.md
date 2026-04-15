---
summary: OutSystems Developer Cloud(ODC) features traces to monitor requests and pinpoint issues
tags: performance monitoring, debugging, distributed tracing, application logs, troubleshooting
guid: c5a60355-80a4-439d-a811-703cf59a70cd
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3457-10&t=VbpYriya8ET1cuRr-1
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - understand
  - apply
  - evaluate
---

# Traces

OutSystems Developer Cloud (ODC) uses distributed tracing to capture the complete lifecycle of an application request. A single user action, such as clicking a button, often triggers a cascade of events across multiple components. A trace is a record that groups every related event for a specific request.

While logs record **what** happened, traces provide the context of **when** and **where** it happened. This context allows you to visualize the request's full lifecycle, helping you troubleshoot issues faster and pinpoint performance bottlenecks.

## Spans {#spans}

The events contained by the trace that represent individual units of work, such as a database query, an API call, or a server action are called spans. Each span includes timing information such as its start time and duration.

Spans are organized hierarchically. For example, a client action (span A) may call a server action (span B), which then executes an aggregate (span C). In this chain, span C is a child of span B, which is a child of span A.

![Diagram showing hierarchical spans in a trace with client action, server action, and aggregate.](images/trace-span-example-os-elements-diag.png "Trace Span Example")

Due to issues like network failures or incomplete data collection, spans can end up without a clear parent. These are called orphan spans, and can be found at the root of the trace.

ODC calculates the total duration of a trace from the start time of the first span to the end time of the last span. However, the following scenarios may cause the trace duration to deviate from this standard calculation:

* Keep-alive elements such as carousels.
* Asynchronous operations, where the parent span does not wait for the child span to complete.

## Trace retention and sampling {#retention-sampling}

In order to prevent information overload from too much data, traces are retained or discarded according to various criteria.

All traces matching the following criteria are retained:

* Traces with error spans.
* Traces with timers lasting more than 5 seconds.
* Traces with Aggregates lasting more than 200 ms.
* Traces with REST APIs (Consume, Expose) lasting more than 200 ms.
* Traces with a duration of more than 1 second.

ODC further retains 2 percent of the total traces that do not meet any of the negative criteria. These traces demonstrate correct execution flows.

Consider an example of an app that had 110 traces captured. These included 5 traces with errors, 5 slow traces (>1 second duration), and 100 healthy traces (<1 second duration, no errors). In this scenario, ODC retains all 10 of the error and slow traces, and a sample of 2 out of the 100 healthy traces.

## Set up traces {#set-up-traces}

ODC supports capture of [server-side traces](server-side-traces.md) and [client-side traces](client-side-traces.md). To turn this functionality on and off, make sure you have the **Edit asset configurations** permission.

Server-side traces are enabled by default, you [can switch them on or off](server-side-traces.md#turn-on-off) in your app configuration section in the ODC Portal. If you have server-side traces enabled, you can also [enable capture of client-side traces](client-side-traces.md#enable-client-side) in the app configuration section in the ODC Portal.

<div class="info" markdown="1">

Turning on client-side traces requires server-side being on first. Disabling server-side traces, disables client-side traces too.

</div>

## Access traces {#access-traces}

You can access trace data in the ODC Portal. Ensure that as an IT user you have the **Access app logs and traces** and **Access user information** permissions.

1. From the ODC Portal menu, go to **Monitor** > **Traces**.

    ![Screenshot of the ODC Portal menu highlighting the Traces option under the Monitor section.](images/monitor-traces-pl.png "Monitor Traces Menu")

1. The traces page displays the most recent traces. Select the desired stage and use the filters to help locate a specific trace. Traces are not available instantly and may be in a processing state. To fetch newly processed traces, select **Refresh**.

1. Select the timestamp in the **Started on** column to open the trace details page.

    ![Screenshot of the traces page showing the most recent traces with a timestamp in the Started on column.](images/select-trace-pl.png "Select Trace")

1. In the trace details page, you can browse the list of spans of the current trace. The spans are displayed in a nested structure to visualize the parent-child relationships between spans. By clicking any row on the list pane, you can see attributes and details for the chosen span on the details pane.

    ![Screenshot of the trace details page showing a nested structure of spans and details for the selected span.](images/trace-detail-pl.png "Trace Details Page")

1. Spans linked to logs are marked with a **document icon**. Select the span and navigate to the **Related logs** section in the details pane to view the entries.

    ![Screenshot showing spans linked to logs marked with a document icon and related logs section in the details pane.](images/trace-related-log-pl.png "Trace Related Logs")

1. To view internal ODC spans, toggle **Show details** (eye icon).
  
    ![Screenshot showing a list of all spans in the ODC Portal, including details like start time, app, element, status, duration, and related logs.](images/eye-all-spans-pl.png "List of All Spans in ODC Portal")

## Considerations and constraints {#considerations-constraints}

As you work with traces, keep in mind that traces may cause performance degradation in complex apps. OutSystems recommends turning off client-side traces to mitigate the issue.

Find more about limits and retention policies of traces in [System requirements](../../getting-started/system-requirements.md#logs-and-traces).

For information on how to stream traces from ODC to third-party application performance monitoring tools, refer to [Streaming observability data](../stream-app-analytics/stream-app-analytics-overview.md).

## Related resources

[Streamed trace data](../stream-app-analytics/stream-app-analytics-traces-ref.md)
