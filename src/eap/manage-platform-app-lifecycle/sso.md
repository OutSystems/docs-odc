---
summary: Learn more about Single sign-on in ODC. Add an SSO button for external providers.
tags: 
locale: en-us
guid: fe13e0ec-b375-4b07-946e-4ee1850436a4
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/AOyPMm22N6JFaAYeejDoge/Configuration-management?type=design&node-id=3401%3A734&t=hXGTDybYCg38Lul5-1
platform-version: odc
---

# Single sign-on

Single sign-on (SSO) is an authentication method that lets you give your users access to multiple applications or services with a single set of login credentials. Developers use the OutSystems Developer Cloud (ODC) Portal to connect to an Identify Provider (IdP) and use ODC Studio to set their apps up for SSO.

SSO simplifies the login process for your users and provides a seamless experience because your users don't have to remember multiple login credentials. When using SSO, users must accept cookies during the login process.

In an SSO system, users authenticate once, then they can access every application that uses the same identity provider. ODC shares the authentication information between apps when the apps use the same provider. In ODC, you can have one or more identity providers available in your apps. You can use the ODC built-in identity provider or a supported external provider.

Implementing SSO provides you with the following benefits:

* **Increased Security** because you reduce the number of passwords users need, making it easier to enforce security policies across all applications.
* **Improved User Experience** because users can access multiple applications with a single set of credentials.
* **Reduced Administrative Overhead** because Admins no longer need to manage multiple sets of login credentials for each application.
* **Simplified Compliance** by providing a centralized view of user access and authentication across multiple applications; organizations can ensure they meet regulatory requirements and industry standards.

## Add the social login button to the login screen

ODC provides a login flow with the app template. Part of that flow is the screen to enter the credentials, and it's where you can add the social login button. The login process runs on the client side (the DoLogin action), so that no email and password go through any of the OutSystems servers.

<div class="info" markdown="1">

Before adding the social login button you must [configure an external identity provider](external-idps/intro.md).

</div>

To add the social login button in the app, do the following in ODC Studio:

1. From the **Interface** tab, go to **UI Flows** > **Common** and double-click **Login**. The login screen opens for editing.
1. On the **Interface** tab, go to **OutSystems UI** > **Utilities**, and drag **ProviderLoginButton** to the login screen.
1. On the properties for the **ProviderLoginButton**, select the provider from the **IdentityProvider** list.

![Screenshot showing how to add a social login button to the login screen in ODC Studio](images/sso-button-odcs.png "SSO Button in ODC Studio")
