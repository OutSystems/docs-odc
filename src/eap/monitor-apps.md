---
summary: Monitor and troubleshoot applications.
tags: 
---

# Monitor Apps

OutSystems provides a unified experience where you can monitor your systems and apps. And then, from the same section you can identify any unexpected behaviors that might impact your systems or apps.

As a best practice, monitor systems and apps during all stages of development.

Several log files are available to help you identify problems like performance or availability, determine the root cause, and then fix the problem. The goal is to help you understand what's causing the anomaly in your application such as an integration error.

At the top of each log file, you can set filters to narrow the scope of your results. In most cases,to the right of each log entry, a Detail link provides stack trace information.

Currently, the following log files are available:

**Error Log** - helps you understand errors that are occurring during runtime. This log shows the following information:

* System related issues or exceptions from an application due to issues in its logic
* Errors from user devices trying to access the app
* Security exceptions such as when an unregistered user tries to access a page

**General Log** - helps you understand the probable causes slowing down your app. This log shows the following information:

* System errors that force a process to terminate
* Application issues such as a slow query warnings
* Activity logs showing which users are logging into an app as well as publishing or deploying

**Integration Log** - helps you understand how quickly your app is responding to incoming requests and external services. This log shows the the amount of time it takes to complete actions in a given period. For example, this log shows how long it takes to get:

* User information for a Rest (consume) action
* HTML for a SOAP (Expose) action
