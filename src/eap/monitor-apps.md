---
summary: Monitor and troubleshoot applications.
tags: 
---

# Monitor apps

<div class="info" markdown="1">

Project Neo documentation is under construction. It's frequently updated and expanded. Leave your feedback and help us building the most usefull content.

</div>

OutSystems provides a unified experience where you can monitor your systems and apps and identify any unexpected behaviors. As a best practice, monitor systems and apps during all stages of development.

Several log files are available to help you identify problems like performance or availability, determine the root cause, and then fix the problem. The goal is to help you understand what's causing the anomaly in your application such as an integration error.

At the top of each log file, you can set filters to narrow the scope of your results. Some log entries have a link to the stack trace information.

Currently, the following log files are available:

**Error Log** - helps you understand errors that are occurring during runtime. This log shows the following information:

* System related issues or exceptions from an application due to issues in its logic
* Errors from user devices trying to access the app
* Security exceptions such as when an unregistered user tries to access a page

**General Log** - helps you understand the probable causes slowing down your app. This log shows the following information:

* System errors that force a process to terminate
* Application issues such as a slow query warnings
* Activity logs with miscellaneous information 

**Integration Log** - helps you understand how quickly your app is responding to incoming requests and external services. This log shows the amount of time it takes to complete an action.
