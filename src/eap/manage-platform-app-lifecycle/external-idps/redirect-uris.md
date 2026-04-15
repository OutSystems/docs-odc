---
summary: Set up redirect URIs for OpenID Connect external identity providers in OutSystems Developer Cloud (ODC).
locale: en-us
guid: 52d83cda-27cb-4f02-aad6-c8b0876e5d10
audience:
  - frontend developers
  - full stack developers
  - platform administrators
platform-version: odc
topic:
  - external-idps
  - idp-openidp
coverage-type:
  - apply
  - remember
  - understand
figma:
app_type: reactive web apps,mobile apps
tags: openid connect, external identity provider, identity management, redirect uris, authentication setup
outsystems-tools:
  - odc portal
helpids:
---
# Configure redirect URIs for an external IdP { #idp-configure-uri }

This procedure applies to OpenID Connect (OIDC) providers, including social providers added with accelerators, because they use OIDC flows.

Redirect URIs tell the identity provider where to send users after login or logout. You must register these URIs in your IdP so ODC can complete authentication.

## Prerequisites

Before you begin, ensure the following:

* You already [added the external IdP](intro.md#add-an-external-idp) in the ODC Portal.
* You have access to the external IdP application registration (for example, a Microsoft Entra ID app registration or an Okta application).

## Set up redirect URIs for your provider

1. In the ODC Portal go to **Manage** > **Identity providers**.

1. Click the provider for which you want to configure the redirect URIs.

1. Go to the **Redirect URLs** tab, and copy the **Login URL** and **Logout URL** for the built-in domain.  

   If you're using a [custom domain](../custom-domains.md), copy the corresponding **Login URL** and **Logout URL** as well.

    <div class="info" markdown="1">

    Copy the URLs for either your **Organization** or the app stage you want (for example, **Apps in Development**, **Apps in QA**, or **Apps in Production**). You can add more later.

    </div>

1. In your provider's portal, open your app registration and paste the redirect URIs.

    <div class="info" markdown="1">

    If you are prompted to choose a platform, select **web**.

    </div>

    If you're configuring [Okta](okta.md#setup-redirect-urls), you can follow the embedded link for specific guidance. Otherwise, refer to your provider's support documentation for further guidance (for example, [Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app#add-a-redirect-uri)).

1. Save the app registration changes in your provider's portal.

## Next step

Proceed to assign the provider to the desired scopes: [Assign an external identity provider](assign-idp.md).

## Related resources

* [Configuring authentication with external identity providers](intro.md)
* [Assign an external identity provider](assign-idp.md)
* [Use external identity providers in an app](apps.md)
