---
summary: Learn how to configure external identity providers for authentication in OutSystems Developer Cloud (ODC), supporting OpenID Connect and social logins.
locale: en-us
guid: fbdf0874-6c92-41ec-8188-bc7b97bd7878
app_type: mobile apps, reactive web apps
platform-version: odc
tags: authentication, identity provider, openid connect, security, social login
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - odc studio
  - odc portal
figma:
coverage-type:
  - understand
  - apply
  - remember
topic:
  - external-idps
  - idp-openidp
---

# Configure OpenID Connect identity providers

This article provides step-by-step instructions for configuring OpenID Connect (OIDC) identity providers in ODC.

<div class="info" markdown="1">

If you're configuring [Microsoft Entra ID](azure-ad.md) or [Okta](okta.md), you can use the specific guides for detailed provider setup instructions.

</div>

## Configure OpenID Connect provider

ODC admins can configure an OpenID Connect provider by navigation to the **ODC Portal** > **Manage** > **Identity providers**.

To launch the **New provider** configuration screen, click the **Add Provider** dropdown and select **OpenID Connect**. Then follow these steps:

1. Enter a name for the new provider in the **Provider name** field. This can be any name less than 255 characters and can't include special characters.

1. Enter the URL of the OpenID configuration in the **Discovery endpoint** field.

1. Click **Get details**.

    ODC retrieves the JSON of the OpenID configuration and shows a preview.

1. Enter the credentials for the provider in the **Client ID** and **Client secret (secret value)** fields. Then select **PKCE** if your provider supports it.

    <div class="info" markdown="1">

    ODC safely stores the configuration details in a secret manager.

    </div>

1. In the **Organization user email verification** section, choose one of the options for handling email verification. For more information about email verification methods, refer to [Email verification logic](intro.md#email-verification-logic).

1. Configure claim mapping in the **Claim Mapping** section.

    If your provider uses different attribute names, overwrite the prefilled **Username**, **Email**, **Name**, and **Photo URL** values. For more guidance, refer to your provider's support documentation.

    <div class="info" markdown="1">

    For more details about mapping claims when configuring an IdP, refer to [Understand the user creation and claim mapping logic](intro.md#claim-mapping-logic).

    </div>

1. Click **Save**.

ODC adds the provider to the list of available providers.

## Next steps

* [Assign the provider](intro.md#assign-an-external-idp)
* [Implement the authentication logic](apps.md)

## Related resources

* [Configure SAML 2.0 identity providers](configure-saml2.md)
* [Configure social providers with accelerators](configure-social-accelerators.md)
* [Microsoft Entra ID configuration](azure-ad.md)
* [Okta configuration](okta.md)
