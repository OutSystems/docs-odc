---
summary: Learn to configure and manage SMTP email settings in OutSystems Developer Cloud (ODC) for app stages.
tags: email configuration, smtp settings, security multi-stage configuration, cloud services
locale: en-us
guid: 48490651-74d0-459b-a0c4-4b40df93d56e
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - apply
  - understand
topic:
  - how-to-send-emails
---

# Configure emails

The ODC apps sends emails using SMTP (Simple Mail Transfer Protocol).To send emails, you must configure the SMTP settings for the emails in the ODC portal. These settings can be configured one for each stage and each stage can have different configuration.

To create and manage an email configuration, you must have organization role that includes the **Manage Email Configurations** permission.

This article explains how to:

* [Set up email for the first time](#set-up-email-for-the-first-time)
* [Create a test list](#create-a-test-list) 

## Set up email for the first time

Before apps can send emails, you must create the email in ODC Studio. For detailed information, refer to [Emails](../building-apps/sending-emails/intro.md#getting-started).

To configure the SMTP settings for the email, follow these steps:

1. Go to ODC Portal.

1. Select **Configurations** > **Emails**. 
The **Email configurations** page is displayed  

1. Select the stage where you want to configure the email settings.

1. (Mandatory) Enter the **SMTP server** IP address.

1. Enter the **SMTP port**. The default SMTP port is 587.  

    <div class="info" markdown="1">

    SMTP port 25 isn't supported due to security risks which can impact the domain's reputation. Port 25 is often targeted for spam and unauthorized access, leading to restrictions by ISPs.

    </div>

1. Choose if you require authentication. If you require authentication, enter the **Username** and **Password** to authenticate.

1. Enter the email address and name of the sender.

1. Click **Save** to save your configuration. The change applies to all apps automatically.

At any time you can modify these settings for that stage by clicking **Edit**.

## Create a test list

You can create email test lists, which are helpful for testing email functionality in your apps. For every app that uses email, you can set up a dedicated test list - a group of email addresses that receives all outgoing emails during testing.

For example, if you're developing an app and want to test an email feature, the app sends messages to the addresses in the test list instead of real users.

You can configure this in the ODC Portal under the app **Configurations** screen. To activate the test list for your app, turn on the Active toggle.

<div class="info" markdown="1">

If your email test list is inactive, the email configuration uses the email list in ODC Studio to test the email.

</div>

To create a test list:

1. From the ODC Portal, select your app.

1. On the **Configuration** page, open the email section.

1. Click on the Test list and then click **Edit**. The test list opens.

1. From the list you can add or remove users and then use the toggle to activate the list.  

1. Click **Save**. Remember the test list must be set to **Active** to use it.

## Additional resources

* [Emails](../building-apps/sending-emails/intro.md)

