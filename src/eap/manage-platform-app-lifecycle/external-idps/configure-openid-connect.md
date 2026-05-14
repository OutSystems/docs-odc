---
summary: OpenID Connect (OIDC) identity provider setup in OutSystems Developer Cloud (ODC), covering discovery endpoint, credentials, PKCE, and claim mapping.
locale: en-us
guid: fbdf0874-6c92-41ec-8188-bc7b97bd7878
app_type: mobile apps, reactive web apps
platform-version: odc
tags:
  - Authentication
  - End-user Authentication
  - External Authentication
  - IdP
  - OIDC
  - Security
audience:
  - Platform administrator
outsystems-tools:
  - odc studio
  - odc portal
figma:
coverage-type:
  - apply
topic:
  - external-idps
  - idp-openidp
isautopublish: true
---

# Add an OpenID Connect identity provider

This article provides step-by-step instructions for adding an OpenID Connect (OIDC) identity provider in ODC.

<div class="info" markdown="1">

If you're adding [Microsoft Entra ID](azure-ad.md) or [Okta](okta.md), you can use the specific guides for detailed provider setup instructions.

</div>

## Prerequisites

Before you begin, make sure you have:

* A setup that meets ODC's [System considerations](intro.md#system-considerations) for external IdPs (for example, static issuer URIs and `client_secret_post`).
* The [**Manage authentication**](../../user-management/roles.md#permissions-registry) permission.
* A registered app in your provider portal, with the following values ready:

    * OpenID configuration URL (**Discovery endpoint**).
    * Provider credentials (**Client ID** and **Client secret**).

    Some providers use different field names, such as **Application ID** for **Client ID** or **Value** for **Client secret**. Refer to the provider's documentation for guidance.

* Your identity provider's endpoints (Discovery, JWKS, token, and userinfo) must be reachable by ODC. ODC validates tokens by retrieving signing keys from the JWKS endpoint. Either expose these endpoints publicly, or restrict access by allowlisting the ODC identity egress IP addresses in your firewall. For the list of IPs, refer to [Allowlisting ODC public IP addresses](../odc-public-ips.md#authentication-external-idp). For background on the network requirements and the protocol-based security model, refer to [Network considerations](intro.md#network-considerations).

* When registering your web app in your identity provider’s portal, if you're prompted to provide redirect URIs, leave the fields empty or use placeholder URIs. You’ll update these with the correct values in a later step of this guide.

## Add an OpenID Connect provider

To add a new OpenID Connect provider, follow these steps:

1. In the ODC Portal, go to **Manage** > **Identity providers**.
1. To open the **New provider** configuration screen, click the **Add Provider** dropdown and select **OpenID Connect**.
1. Enter a name for the new provider in the **Provider name** field. This can be any name less than 255 characters and must only include letters, numbers, and spaces.

1. Enter the URL of the OpenID configuration in the **Discovery endpoint** field.

1. Click **Get details**.

    ODC retrieves the JSON of the OpenID configuration and shows a preview.

1. Enter the credentials for the provider in the **Client ID** and **Client secret (secret value)** fields. Then select **PKCE** if your provider supports it.

    <div class="info" markdown="1">

    ODC safely stores the configuration details in a secret manager.

    </div>

1. In the **Organization user email verification** section, choose one of the options for handling email verification. For more information about email verification methods, refer to [Email verification logic](identity-claims-email-verification.md#email-verification-logic).

1. In the **User profile matching** section, select the attribute (fallback option) ODC uses to match external logins to ODC profiles when a subject match isn't found.
    For more information about the options and when to use each one, refer to [Profile matching for external IdPs](identity-claims-email-verification.md#profile-matching-external-idps).

1. Configure claim mapping in the **Claim Mapping** section.

    If your provider uses different attribute names, overwrite the prefilled **Username**, **Email**, **Name**, and **Photo URL** values. For more guidance, refer to your provider's support documentation.

    <div class="info" markdown="1">

    For more information about claim mapping and profile matching, refer to [Claim mapping and profile matching](identity-claims-email-verification.md#claim-mapping-logic).

    </div>

1. Click **Save**.

ODC adds the provider to the list of available providers.

<div class="warning" markdown="1">

If you make any changes to the client secret after it has been applied, the changes may take up to one hour to take effect due to caching. During this period, the previously applied client secret remains in use. To prevent downtime, keep the old client secret configured in your external IdP for at least one hour after the change.

</div>

## Next step

* [Set up redirect URIs for an external IdP](redirect-uris.md)

## Related resources

* [Add a SAML 2.0 identity provider](configure-saml2.md)
* [Add a social identity provider with accelerators](configure-social-accelerators.md)
* [Add Microsoft Entra ID for use as external identity provider](azure-ad.md)
* [Add Okta for use as an external identity provider](okta.md)
