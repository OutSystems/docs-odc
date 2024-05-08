---
summary: Monitor and analyze timer logs in OutSystems Developer Cloud (ODC) through the ODC Portal to track execution times and troubleshoot issues effectively.
tags:
locale: en-us
guid: 95C30236-ADCA-464E-AD86-A3437E9F3FEF
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---
# Monitor Timers

OutSystems logs enable you to display information for a stage, an app, or all apps.

Timer logs display the following:

* If a timer is running and when it started
* The last time a timer executed
* How long the action took to compete

You can sort the log list by severity and display any combination of errors, warnings, and informational messages.  

To view the logs go to the ODC (OutSystems Developer Cloud) Portal and then from the left Nav panel select **Monitoring** > **Logs**.

Logs also provide detail information for each message. To access the detail information for a message, click on the **message time**. The detail page opens, and you can see:

* The name of the message and the date and time it occurred
* The severity level, the app, and the user (if applicable)
* The error message
* Stack information
  
Toward the bottom of the page there is a list of related logs and activities. You can use this information to continue to research the root cause of the problem.

To better understand how Timers work  in OutSystems, see [Use Timers](intro.md).
