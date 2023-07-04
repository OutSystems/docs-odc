---
summary: Learn how to configure emails in OutSystems Developer Cloud.
tags:
locale: en-us
guid: 48490651-74d0-459b-a0c4-4b40df93d56e
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# Configure emails

Emails are an integral part of any app you develop because you can send app users such things as invitations or notifications. An OutSystems app sends emails using SMTP (Simple Mail Transference Protocol). In OutSystems Developer Cloud (ODC), you configure emails in the ODC Portal.

You create an email configuration for a stage. You can have different configurations for each stage, but you can only have one configuration per stage.

Admins with access to the Configurations can create  or update an email configuration.
This document describes how to:

* Create a test list.
* Set up email for the first time.
* Modify an email configuration.

## Create a test list

ODC enables you to create email test lists, which are very useful for testing. For each app that uses the email feature, you can create an email test list. This list of email addresses gets used whenever your app sends an email. For example, if you have an app in development, and want to test a feature you can send an email to your test list team. You configure your app in the ODC Portal using the App configurations screen. To use the test list you must set the toggle to **active**.

<div class="info" markdown="1">

If your email test list is inactive, the email configuration uses the email list in ODC Studio. to test the email.

</div>

To create a test list:

1. From the ODC Portal, select your App.
1. On the Configuration page, open the email section.
1. Click on the Test list and then click **Edit**. The test list opens.
1. From the list you can add or remove users and then use the toggle to activate the list.  
1. Click **Save**. Remember the test list must be set to **Active** to use it.

## Set up email for the first time

Before apps can send emails, you must create the email in ODC Studio.

1. To begin, open the ODC Portal, and from the Navigation menu, select **Configurations** > **Emails**. The **Email configurations** page opens.  
1. Complete the following fields. Required fields display with an asterisk.
      * **Stage** - from the drop down select one or more stages.
      * **Server** - enter the IP address of the SMTP server and the port number. The SMTP port number defaults to 587, but you can change it. Note that port 25 isn't supported.
      * **Requires Authentication** - Check to require authentication and then enter the user name and password to authenticate.

1. Click **Save** to save your configuration. The change applies to all apps automatically.

## Modify an email configuration

You can make changes to an email configuration on a stage.

1. To change an email configuration, go to ODC Portal and select **Configurations** > **Email**.
1. Locate the configuration you want to change and click **Edit**.  
1. Select or verify the stage.
1. Make the change, and click **Save**. The change applies to all apps automatically.
