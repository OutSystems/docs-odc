---
summary: Learn more about how you apps can send emails in OutSystems Developer Cloud (ODC).  
tags:
locale: en-us
guid: F826D84E-BF79-4287-9322-1E00E198A06E
app_type: mobile apps, reactive web apps
---

# Emails

In OutSystems Developer Cloud (ODC), email is a way to get information from your apps and send it to users. For example, you can send alerts to administrators or send a copy of a form to an end user for submission. Before you can create emails and set up logic in your apps to send the emails, make sure you have the configuration for the SMTP server. 

In OutSystems, email is a UI element that lets you design and manage the content of email messages. To create, send, and configure emails, you use both ODC Studio and ODC Portal. Emails are sent using SMTP. In ODC Portal, you can define the configuration and can create different configurations for each stage. At the app level you can change the test email addresses. 

In **ODC Studio** you define how you want to send emails. When working with the display of the content, you can use or define new templates. By default, ODC uses a light theme which is an industry standard and is automatically set for you.

When defining how to send the email, developers can:

* Create server and service actions to send emails.
* Create parameters in actions to pass information.
* Define timers to send an email at a specific time.
* Define manual triggers by creating a send email button or automate the sending of emails such as a confirmation of registration. 

Developers can also use **widgets** (GUI elements to create and display the content) in an email to:

* Evaluate expressions and display values.
* Show or hide content based on a condition.
* Embed an image.
* Show information in columns and rows.

To configure ODC to send emails, see [Configure sending emails](../../configuration-management/configure-emails.md)