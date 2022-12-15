---
summary: Information about external IdPs and how to use them.
tags: 
locale: en-us
guid: 5aa8692d-68bf-41a1-89ec-5e8fc7069e29
app_type: mobile apps, reactive web apps
---

# Configuring authentication with external identity providers

OutSystems Developer Cloud (ODC) comes bundled with Identity Service, a built-in Identity Provider (IdP). It provides authentication, authorization, and user management for your [organization](../architecture/intro.md#platform) and apps. You access your organization services through ODC Portal and ODC Studio. As the default IdP, Identity Service is always available.

In addition, you can use an external, self-managed IdP as an authentication provider for your organization and your apps. You can use any IdP that follows the OpenID Connect (OIDC) standard. You can configure most commercial IdPs, such as AzureAD and Okta, to support this standard. ODC supports using **PKCE** (Proof Key for Code Exchange) with external IdPs for an additional layer of security.

You can easily add a [supported social provider](#supported-social-providers) to use social authentication for your organization and your apps.

When you successfully configure and save an external IdP to ODC, it becomes an option for use as an active provider for your organization, your apps, or both. You can use multiple active providers for your organization and each stage your apps are deployed to. You must use the same provider(s) for all the apps deployed to a given stage. The following diagram shows an example setup.

![External IdPs concept](images/external-idps-example-diag.png "External IdPs concept")

## Before you begin

<div class="info" markdown="1">

If you're configuring [Azure AD](azure-ad.md) or [Okta](okta.md) you can skip this section and follow the specific guidance by following one of the embedded links.

</div>

Before you begin configuring an external identity provider for use in ODC, you need to get the following information from the provider:

* URL of the OpenID configuration
* Provider credentials. Your provider might use different names for these fields such as **Application ID** for the **Client ID** field and **Client secret** or **Value** for the **Client secret (secret value)** field. For more guidance, see your provider's support documentation.

If you want a user associated with an external provider to retain their profile and associated roles, they should use the same email address as on the built-in provider.

## Add an external IdP

ODC admins can configure an external IdP by going to the ODC Portal and selecting the **Identity providers** tab. A list of built-in providers and any external IdPs already added displays.

To launch the **New provider** configuration screen, click the **Add Provider** dropdown and select **OpenID Connect** or a supported social provider. Now follow these steps:

### OpenID Connect

1. Enter a name for the new provider in the **Provider name** field. This can be any name less than 255 characters and can't include special characters.

1. Enter the URL of the OpenID configuration in the **Discovery endpoint** field. 

1. Click **Get details**. ODC retrieves the JSON of the OpenID configuration and shows a preview. 

1. Enter the credentials for the provider in the **Client ID** and **Client secret (secret value)** fields. Then, select **PKCE** if your provider supports it.

    <div class="info" markdown="1">
    ODC safely stores the configuration details in a secret manager.
    </div>

1. If your provider uses different attribute names, then in the **Claim Mapping** section overwrite the prefilled **Name** and **Email** fields. Otherwise, skip this step. For more guidance, see your provider's support documentation.

1. Click **Save configuration**. ODC tests the configuration and, on success, adds the provider to the list of available providers. If the test fails, a notification with the error displays.

### Supported social provider

1. Enter a name for the new provider in the **Provider name** field. This can be any name less than 255 characters and can't include special characters.

1. Enter the credentials for the provider in the **Client ID** and **Client secret** fields.

    <div class="info" markdown="1">

    ODC safely stores the configuration details in a secret manager.

    </div>

1. Click **Save configuration**. ODC tests the configuration and, on success, adds the provider to the list of available providers. If the test fails, a notification with the error displays.

## Assign an external IdP

To assign an added external IdP, navigate to the **Identity providers** tab in ODC Portal. Then follow these steps:

1. Click on the provider card you want to assign as a provider for your organization, your apps, or both.

1. Check the summary in **Configuration details**. If you want to proceed, click the **Assign** button (when provider not assigned anywhere yet) or **Manage assignments** (when already assigned).

    <div class="info" markdown="1">

    You can assign a maximum of two identity providers to each app stage.

    </div>

1. Check the boxes of where you want to assign the provider and then click **Next**.

    <div class="info" markdown="1">

    When you switch the IdP for your organization or apps, all signed-in users get logged out when their current access token expires. Users have to log back in using the newly assigned provider. Users may have to wait up to a minute to log back in while new certificates are processed. 
    
    </div>

1. Read the confirmation pop-up and then do one of the following:

    * Click the **Confirm changes** button to proceed.
    * Click the **Cancel** to exit.

    Once ODC applies the provider successfully, a notification displays.

1. Copy the pair(s) of **Redirect URLs** to the list of permitted redirects in the setup page of your external provider. You should copy the pair(s) for both the built-in domain and any active [custom domains](../custom-domains.md). If you're configuring [Okta](okta.md#setup-redirect-urls) you can follow the embedded link for specific guidance. Otherwise see your provider's support documentation for further guidance (for example, [Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#add-a-redirect-uri)). Click **Next**.

When a provider is assigned for use by the apps, you need to create the logic in ODC Studio for each app you want to use it. Follow the guidance on how to do that [here](apps.md).

## Edit the configuration of an external IdP

You can only edit a provider not in use. Navigate to the **Identity providers** tab in ODC Portal. Then:

1. Click on the provider card you want to edit.

1. Click the ellipsis button to the right of the **Assign** button. Then click the **Edit configurations** button to launch the edit page.

## Supported social providers

ODC provides accelerators to add the following social providers easily.

| Provider    |
| ----------- |
| Facebook    |
| Google      |  
