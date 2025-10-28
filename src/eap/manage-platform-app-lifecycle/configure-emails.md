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

# Configure SMTP settings for emails

The ODC apps sends emails using SMTP. For secure SMTP authentication, ODC supports both basic username/password and the more modern OAuth 2.0 authorization framework. Given the increasing security risks associated with basic authentication many providers are phasing out username/password authentication in favor of OAuth 2.0.

Here are some of the advantages of using OAuth 2.0 for SMTP authentication:

* Replaces long-lived passwords with short-lived access tokens. These tokens have limited scope and expiry, reducing the risk of credential misuse.

* Allows you to grant specific permissions (scopes) to an app. For SMTP, this means an app can be authorized only to send emails without gaining access to read, delete, or manage your mailbox in other ways.

* Access tokens can be revoked or rotated without impacting a user's main credentials, allowing for more flexible access control.

* Widely supported by SMTP providers such as Google and Microsoft and is the modern industry standard for secure authorization.

This article explains how to:

* [Set up email for the first time](#set-up-email-for-the-first-time)
* [Create a test list](#create-a-test-list)

## Set up email for the first time

To send emails, you must configure the SMTP settings for the emails in the ODC portal. These settings can be configured one for each stage and each stage can have different configuration.

### Prerequisites

Before configuring the SMTP settings for the email, ensure that you have the organization role that includes the **Manage Email Configurations** permission.

### Configure email settings

To configure the SMTP settings for the email, follow these steps:

1. Go to ODC Portal.

1. Select **CONFIGURE** > **Emails**.
The Emails configurations page is displayed  

1. Select the stage where you want to configure the email settings.

1. (Mandatory) Enter the **SMTP server** IP address.

1. Enter the **SMTP port**. The default SMTP port is 587.  

    <div class="info" markdown="1">

    SMTP port 25 isn't supported due to security risks which can impact the domain's reputation. Port 25 is often targeted for spam and unauthorized access, leading to restrictions by ISPs.

    </div>

1. Select the authentication type from the drop-down.

    For **OAuth 2.0 - client credentials** authentication, enter the following fields:

    <div class="info" markdown="1">

    The configuration fields can be obtained from the infrastructure admin who is responsible to configure the SMTP server.

    </div>

    * **Server Token URL**: (Mandatory) URL of the authorization server that is used to obtain an OAuth 2.0 access token and refresh token. It is also used to refresh the token.

    * **Client ID**: (Mandatory) Used to identify the ODC app when it requests authorization and access tokens from the OAuth 2.0 authorization server such as Google or Microsoft.

    * **Client Secret**: (Mandatory) Secure credential used along with the client id to identify the ODC app when it requests authorization and access tokens from the OAuth 2.0 authorization server.

    * **Scopes**: The level of permission and access granted to the ODC app for the email account.
    The access token issued to the app by the authorization server is only valid for the permissions defined by the scopes. For example, the default scope for Microsoft Exchange is `https://outlook.office365.com/.default`, which provides broad access to read emails, send emails, and access all mailboxes.

      <div class="info" markdown="1">

      Different email providers might define their own scopes for SMTP access. You must consult the documentation of the specific provider you are using to identify the correct scope(s) required for sending emails via SMTP using OAuth 2.0.

      </div>

    For **Basic** authentication, enter the **Username** and **Password** to authenticate.

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

## Related resources

* [Emails](../building-apps/sending-emails/intro.md)

* [Sending emails](../building-apps/sending-emails/sending.md)
