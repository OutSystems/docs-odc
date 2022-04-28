---
summary: Monitor and troubleshoot applications by reviewing logs and activities.
tags: 
locale: en-us
guid: ca7cae65-c466-4d93-bab6-85ac740519c0
app_type: mobile apps, reactive web apps
---

# Monitor apps

<div class="info" markdown="1">

Project Neo documentation is under construction. It's frequently updated and expanded.

</div>

OutSystems provides a unified experience for monitoring your systems and apps and identifying unexpected behaviors. As a best practice, you should monitor systems and apps during all stages. The **Activities** and **Logs** screens are available in Project Neo Portal.

This document provides an overview of using log files and activities to ensure your apps are working correctly. 

## Logs

Apps generate logs to help you identify issues and determine the root cause of the problem. At the top of each log file, you can set filters to narrow the scope of your results. You can filter by stage, app, user, severity, date/time, and free text. The logs include a Log Detail page that shows more information. Some log entries have a link to the stack trace information. By default, you see the logs from the development stage.

Error log helps you understand the errors that are occurring during runtime. The error log shows the following information:

* System-related issues or exceptions from an application due to issues in its logic
* Errors from user devices trying to access the app
* Security exceptions such as when an unregistered user tries to access a page

General log helps you understand the probable causes of why your app is slow. The general log  shows the following information:

* System errors that force a process to terminate
* Application issues such as a slow query warning
* Activity logs with miscellaneous information

Integration log helps you understand how quickly your app is responding to incoming requests and external services. This log shows the amount of time it takes to complete an action.

<div class="info" markdown="1">

Access the logs screen from **Portal** > **Logs**.

</div>

## Activities

Apps generate activities to ensure your apps are working as expected. Reviewing the activities, enables you to troubleshoot:
 
* Issues by reviewing the activities that run
* The performance of the app and any issues by checking for slow queries, screens, and integrations
* Tracing related to the user requests

By default, activities run in the development stage for any activity that started in the last 12 hours. The lists show the app, the type of activity, the action that run, when the action started, and how long it took to run. The list displays a maximum of 100 activities in descending order sorted by start date/time. You can set filters to narrow the scope of your results. You can filter by stage, apps, free text, date/time, activity type, and duration.

Some activities that show in the list include: 

* Consumed and Exposed Integration
* Service actions
* Screen data actions
* Server actions
* Client actions

<div class="info" markdown="1">

Access the activities screen from **Portal** > **Activities**.

</div>
