---
summary: Monitor and troubleshoot applications.
tags: 
locale: en-us
guid: ca7cae65-c466-4d93-bab6-85ac740519c0
app_type: mobile apps, reactive web apps
---

# Monitor apps

<div class="info" markdown="1">

Project Neo documentation is under construction. It's frequently updated and expanded. Leave your feedback and help us build the most useful content.

</div>

OutSystems provides a unified experience for monitoring your systems and apps and identifying unexpected behaviors. As a best practice, you should monitor systems and apps during all stages of development.

Log files are available to help you identify issues, determine the root cause of the problem, and then fix it. At the top of each log file, you can set filters to narrow the scope of your results. Some log entries have a link to the stack trace information.

Currently, the following log files are available:

**Error Log** - helps you understand errors that are occurring during runtime. This log shows the following information:

* System related issues or exceptions from an application due to issues in its logic
* Errors from user devices trying to access the app
* Security exceptions such as when an unregistered user tries to access a page

**General Log** - helps you understand the probable causes of why your app is slow. This log shows the following information:

* System errors that force a process to terminate
* Application issues such as a slow query warning
* Activity logs with miscellaneous information 

**Integration Log** - helps you understand how quickly your app is responding to incoming requests and external services. This log shows the amount of time it takes to complete an action.
