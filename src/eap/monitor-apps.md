---
summary: Monitor and troubleshoot apps by reviewing logs and traces
tags: 
locale: en-us
guid: ca7cae65-c466-4d93-bab6-85ac740519c0
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Monitor and troubleshoot apps

OutSystems Developer Cloud (ODC) provides a unified experience for monitoring and troubleshooting your apps. The **Logs** and **Traces** screens are available in ODC Portal under the **Monitoring** section in the left nav menu.

Logs and traces are complimentary for getting to the root cause of a problem with an app. While a log helps you identify the problem, the associated trace helps you locate the problem. You can then use this information to help resolve the problem. 

Traces are also helpful for troubleshooting a performance issue with an app.

## Logs

Apps have associated logs. Logs are either automatically generated (a log generated when a timer fails to execute, for example) or triggered by app logic built by a developer (an [exception](building-apps/handle-exceptions.md#exception-logs--exception-logs) triggered by the failure of an end-user to provide a required input, for example). Developers can also use the LogMessage system action.

Each log has a level of severity: **Error**, **Warning**, and **Information**.

By default, when you open the **Logs** screen you see error logs from the development stage ordered by time in descending order. Use the filter inputs to filter logs by stage, app, severity, date/time, user, and message. You can filter logs by date back up to four weeks in an interval of up to two weeks.

When you click the embedded link of a log's date/time, you open the detail page for that unique log. You see the log message, stack trace, and any logs related to the same request. Go to the log's associated trace by clicking the **Go to trace** button. When a log doesn't have an associated trace the button is disabled. Currently, you only see traces for requests using server-side elements.

## Traces

When an app makes a request using a server-side element, it generates a trace. A trace is an end-to-end view of a request comprised of a series of intervals known as spans. Each span is a logical unit of work and has a duration. You review a trace to:

* Identify which span threw an error to get to the root cause.
* Understand the performance of each span in the app and dependent apps.

For example, you could quickly identify that the issue with a Service Action request as an SQL query (a span of the trace) has invalid syntax.

<div class="info" markdown="1">

Traces take a few minutes to generate and display. It takes time for ODC to aggregate all the spans within the request.

</div>

By default, when you open the **Traces** screen you see traces from the development stage ordered by time in descending order. The stage filter of the Logs and Traces screens are synchronized. This means if you were viewing production logs in the Logs screen, you see production logs in the Traces screen.

Use the filter inputs to filter traces by stage, app, element type, trace status, total duration, date/time and user. You can filter traces by date back up to four weeks in an interval of up to two weeks. 

When you click the embedded link of a trace's date/time, you open the detail page for that unique trace. On the left side of the screen you see each span of the trace in order of execution alongside its duration. A red bar next to a span indicates an error. If any span of a trace has an error then the status of the trace is **Error**. Else the trace status is **OK**.

You use the **Show all** toggle to show ODC internal spans. This may provide additional context for your troubleshooting, but you can't action a problem with an ODC internal span. 

When you click a span you see its attributes and any related logs on the right side of the screen.

## Sharing logs and traces

Each log and each trace has a unique ID contained in the URL (`...?id=x...`). If you need to share a log or trace with a team member, share the URL. The team member needs access to the ODC organization and permission to view.

## Retention of logs and traces

You can view logs and traces up to four weeks old within the Portal. For logs and traces between four and ten weeks old, you can retrieve by opening a support ticket. Logs and traces are deleted after ten weeks.
