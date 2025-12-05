---
summary: Social provider accelerator requirements for authentication in OutSystems Developer Cloud (ODC).
locale: en-us
guid: 3080f31e-088b-4278-a2b8-1134a5a40255
app_type: mobile apps,reactive web apps
platform-version: odc
tags: authentication,identity provider,openid connect,security,social login
figma: 
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
topic:
  - external-idps
  - idp-saml
outsystems-tools:
  - odc portal
coverage-type:
  - apply
  - understand
helpids: 30711
---

# Add a social identity provider with accelerators

This article provides step-by-step instructions for adding social providers with accelerators in ODC.

## Prerequisites

Before you begin, make sure you have:

* A setup that meets ODC's [System considerations](intro.md#system-considerations) for external IdPs (for example, static issuer URIs and `client_secret_post`).
* Enabled refresh tokens: If your provider allows it, ensure your provider issues refresh tokens and that the `offline_access` scope is enabled and consented (when available). For behavior details, refer to [Refresh token-driven user revalidation (OIDC only)](intro.md#refresh-token-sync-oidc).
* The [**Manage authentication**](../../user-management/roles.md#permissions-registry) permission.
* A registered app in your social provider portal, with the required values for your provider ready (refer to [Social provider requirements](#social-provider-requirements); for example, Client ID and Client Secret).

<div class="info" markdown="1">

When registering your web app in your identity provider’s portal, if you're prompted to provide redirect URIs, leave the fields empty or use placeholder URIs. You'll update these with the correct values in a later step of this guide.

</div>

## Add a social provider with accelerators

To add a new social identity provider with accelerators, follow these steps:

1. In the ODC Portal, go to **Manage** > **Identity providers**.
1. To open the **New provider** configuration screen, click the **Add Provider** dropdown and select the social provider (Apple, Google, Facebook, or LinkedIn).
1. Enter a name for the new provider in the **Provider name** field.
1. Complete the configuration fields with the information required from your provider (refer to [Social provider requirements](#social-provider-requirements).

    <div class="info" markdown="1">

    ODC safely stores the configuration details in a secret manager.

    </div>

1. In the **Organization user email verification** section, choose one of the options for handling email verification. For more information about email verification methods, refer to [Email verification logic](identity-claims-email-verification.md#email-verification-logic).

1. Click **Save**.

ODC adds the provider to the list of available providers.

## Social provider requirements

To add a new social provider using an accelerator, you need to get the following information from your provider:

### Apple

| Accelerator field | Information required | Description |
| ---|---|--- |
| Client ID | Identifier | A public identifier your app on the provider side. It's a string type value available to any registered developer on Apple Developer. You can access the Identifier value on the Certificates, Identifiers, and Profiles pages of your app. |
| Key ID | Key ID | Key ID corresponding to your Secret (`.p8`). |
| Team ID | Team ID | Identifier of your team on Apple Developer. |
| Client secret | Private key (`.p8`) | The private key generated and downloaded from Apple (refer to [Create a private key to access a service](https://developer.apple.com/help/account/manage-keys/create-a-private-key)). The downloaded file is in .p8 format, but can be opened with a text editor. Copy the entire text content and paste it directly into the **Client Secret** field in the ODC Portal. This private key is used to create the required client secret. |

For further guidance, check [Configure app capabilities - About Sign in with Apple](https://developer.apple.com/help/account/configure-app-capabilities/about-sign-in-with-apple).

## Google

| Accelerator field | Information required | Description |
| ---|---|--- |
| Client ID | Client ID | A public identifier for your app on the provider side. It's a string type value available to any registered developer on the Google Cloud Platform. You can access the ClientID value on the OAuth Consent tab on your app's Credentials screen. |
| Client Secret | Client Secret | A confidential code known only to your app and the authorization server. It's a string type value available to any registered developer on the Google Cloud Platform. In the **API & Services** product, you can access the **ClientID** value on the **Credentials** tab on your app's **Credentials** screen. For your app, select **Download OAuth client**.  |

 You must have the **Identity Platform** API enabled in the Google Console.

For further guidance, check [Google Identity - Authentication](https://developers.google.com/identity/gsi/web/guides/overview).

### Facebook

| Accelerator field | Information required | Description |
| ---|---|--- |
| App ID | App ID | A public identifier for your app on the provider side. It's a string type value available to any registered developer on Meta for Developers. You can access the AppID value in your app's settings. |
| App Secret | App Secret | A confidential code known only to your app and the authorization server. It's a string type value available to any registered developer on Meta for Developers. You can access the **AppSecret** value in your app's settings. |

For further guidance, check [Facebook Login - Documentation - Facebook for Developers](https://developers.facebook.com/docs/facebook-login/).

### LinkedIn

| Accelerator field | Information required | Description |
| ---|---|--- |
| Client ID | Client ID | A public identifier for your app on the provider side. It's a string-type value available to any registered developer on LinkedIn. You can access the **ClientID** value on the **Auth** tab on your app's Credentials screen. |
| Client Secret | Client Secret | A confidential code known only to your app and the authorization server. It's a string-type value type value available to any registered developer on LinkedIn. You can access the **ClientSecret** value on the **Auth** tab on your app's **Credentials** screen. |

For further guidance, check [Sign In with LinkedIn using OpenID Connect](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin-v2).

## Next step

* [Set up redirect URIs for an external IdP](redirect-uris.md)

## Related resources

* [Add an OpenID Connect identity provider](configure-openid-connect.md)
* [Add a SAML 2.0 identity provider](configure-saml2.md)
* [Add Microsoft Entra ID for use as external identity provider](azure-ad.md)
* [Add Okta for use as an external identity provider](okta.md)
