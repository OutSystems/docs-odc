---
summary: Social provider accelerator requirements for authentication in OutSystems Developer Cloud (ODC).
locale: en-us
guid: 3080f31e-088b-4278-a2b8-1134a5a40255
app_type: mobile apps, reactive web apps
platform-version: odc
tags: authentication, identity provider, openid connect, security, social login
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
---

# Configure social providers with accelerators

ODC admins can configure social providers with accelerators by navigating to the **ODC Portal** > **Manage** > **Identity providers** tab.

To launch the **New provider** configuration screen, click the **Add Provider** dropdown and select **the social provider** (Apple, Google, Facebook, or LinkedIn). Then follow these steps:

1. Enter a name for the new provider in the **Provider name** field.

1. Fill in the configuration fields with the information required from your provider (see provider-specific requirements below).

    <div class="info" markdown="1">

    ODC safely stores the configuration details in a secret manager.

    </div>

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
| Client secret | Private key (`.p8`) | The private key generated and downloaded from Apple (refer to [Create a private key to access a service](https://developer.apple.com/help/account/manage-keys/create-a-private-key)). The downloaded file is in .p8 format but can be opened with a text editor - copy the entire text content and paste directly in the Client Secret field on ODC Portal. This private key will be used to create the required client secret. |

For further guidance, check [Configure app capabilities - About Sign in with Apple](https://developer.apple.com/help/account/configure-app-capabilities/about-sign-in-with-apple).

### Google

| Accelerator field | Information required | Description |
| ---|---|--- |
| Client ID | Client ID | A public identifier for your app on the provider side. It's a string type value available to any registered developer on the Google Cloud Platform. You can access the ClientID value on the OAuth Consent tab on your app's Credentials screen. |
| Client Secret | Client Secret | A confidential code known only to your app and the authorization server. It's a string type value available to any registered developer on the Google Cloud Platform. You can access the ClientSecret value on the OAuth Consent tab on your app's Credentials screen. |

For further guidance, check [Google Identity - Authentication](https://developers.google.com/identity/gsi/web/guides/overview).

### Facebook

| Accelerator field | Information required | Description |
| ---|---|--- |
| Client ID | App ID | A public identifier for your app on the provider side. It's a string type value available to any registered developer on Meta for Developers. You can access the AppID value in your app's settings. |
| Client Secret | App Secret | A confidential code known only to your app and the authorization server. It's a string type value available to any registered developer on Meta for Developers. You can access the AppSecret value in your app's settings. |

For further guidance, check [Facebook Login - Documentation - Facebook for Developers](https://developers.facebook.com/docs/facebook-login/).

### LinkedIn

| Accelerator field | Information required | Description |
| ---|---|--- |
| Client ID | Client ID | A public identifier for your app on the provider side. It's a string-type value available to any registered developer on LinkedIn. You can access the ClientID value on the Auth tab on your app's Credentials screen. |
| Client Secret | Client Secret | A confidential code known only to your app and the authorization server. It's a string-type value type value available to any registered developer on LinkedIn. You can access the ClientSecret value on the Auth tab on your app's Credentials screen. |

For further guidance, check [Sign In with LinkedIn using OpenID Connect](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin-v2).

## Next steps

* [Assign the provider](intro.md#assign-an-external-idp)
* [Implement the authentication logic](apps.md)

## Related resources

* [Configure OpenID Connect identity providers](configure-openid-connect.md)
* [Configure SAML 2.0 identity providers](configure-saml2.md)
* [Microsoft Entra ID configuration](azure-ad.md)
* [Okta configuration](okta.md)
