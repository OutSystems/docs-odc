---
summary: This article explains how to configure sending emails in OutSystems Developer Cloud.
tags:
locale: en-us
guid: 48490651-74d0-459b-a0c4-4b40df93d56e
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Configure sending emails

Emails are an integral part of any app you develop because you can send app users such things as invitations or notifications. An OutSystems app sends emails using SMTP (Simple Mail Transference Protocol). In OutSystems Developer Cloud (ODC), you configure emails in ODC Portal.

Emails include a feature that lets you test emails before sending them. This helps eliminate errors by giving you the chance to review the text and format.

You create an email configuration for a stage. You can have different configurations for each stage, but you can only have one configuration per stage.

Admins with access to the Configurations  can create an email configuration

This document describes how to:

* Set up email for first the first time.
* Apply the email configuration.
* Change the email configuration at the stage level.

## Set up email for the first time

Before apps can send emails, you must create the email in ODC Studio.

1. To begin, open ODC Portal, and from the navigation menu, select **Configurations** > **Emails**. The **Email configurations** page opens.
   
1. Complete the following fields. Required fields display with an asterisk.
   
      * **Stage** - from the drop down select one or more stages.
      * **Server** - enter the IP address, the port number. The SMTP port number defaults to 25. 
      * **Requires Authentication** - Check to require authentication and then enter the user name and password to authenticate.
      * **Recipients** -  the email address and name of the people receiving this email. Select **Set in app** to use the email addresses from ODC Studio or select **Test List** to display fields to enter email test recipients.

2. Click **Save** to save your configuration. You can now apply the configuration to your app.

## Apply an email configuration

Once you define an email configuration, you can apply it to your app. Select the same stage in which you created the configuration.

1. Open ODC Portal. 
1. From the **Configurations** tab, scroll down and click **Email** to open the section.
1. Select the Configuration you want to apply to the emails.

## Modify an email configuration

You can make changes to an email configuration on a stage.

1. To change an email configuration, go to ODC Portal and select **Configurations** > **Email**.
1. Locate the configuration you want to change and click **Edit**.  
1. Make the change, and click **Save**.
1. Verify your change.
1. Open the App, go to the Configurations page, scroll down to the Email section, and apply the new configuration to your app.  
