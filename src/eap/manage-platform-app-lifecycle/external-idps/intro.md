---
summary: Configure external identity providers for authentication in OutSystems Developer Cloud (ODC), supporting OpenID Connect, SAML 2.0, and social logins.
locale: en-us
guid: 5aa8692d-68bf-41a1-89ec-5e8fc7069e29
app_type: mobile apps,reactive web apps
figma: https://www.figma.com/design/KpEoUxciqaFLGLlZxo7Hiu/User-management?node-id=3405-24
platform-version: odc
tags: authentication,identity provider,openid connect,saml,security
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - understand
  - apply
  - remember
topic:
  - external-idps
  - idp-openidp
  - idp-saml
helpids: 30707
---

# Configuring authentication with external identity providers

OutSystems Developer Cloud (ODC) comes bundled with Identity Service, a built-in Identity Provider (IdP). It provides authentication, authorization, and user management for your [organization](../platform-architecture/intro.md#platform) and apps. You access your organization's services through the ODC Portal and ODC Studio. As the default IdP, Identity Service is always available.

In addition, you can use an external, self-managed IdP as an authentication provider for your organization and your apps. ODC supports two main authentication protocols:

* **OpenID Connect (OIDC)** - An identity layer on top of OAuth 2.0. ODC supports using **proof key for code exchange** (PKCE) with OIDC providers for an additional layer of security.

* **SAML 2.0** - An XML-based standard for exchanging authentication and authorization data between identity providers and service providers.

You can configure most commercial IdPs to support these standards.

ODC also provides accelerators for [commonly used social providers](configure-social-accelerators.md) that use OpenID Connect for social authentication. These accelerators simplify the process of adding social login options for both your organization and your apps.

## Scopes for assigning IdPs {#scopes-for-assigning-idps}

IdPs are assigned to the organization or to a stage, never to an individual app:

* **Organization scope**: Members (IT-users) can sign in to the ODC Portal and ODC Studio with the IdP.
* **Stage scope**: All apps in that stage can use the IdP for end-user sign-in. For apps created with ODC Studio version 1.3.0 or later, the pre-built login screen automatically shows the IdPs assigned to the stage, so you usually don’t need to change the app’s login logic. For apps created before this behavior was introduced, or if you want to customize the default behavior, refer to [Step 4: Use an IdP in your apps (for end-users only)](#use-an-idp-in-your-apps).

The following diagram shows an example setup.

![External IdPs concept](images/external-idps-example-diag.png "External IdPs concept")

You can assign more than one identity provider to the same scope. A single stage can have multiple active IdPs at once, including multiple custom external IdPs, and you can keep the built-in provider active. If you want users to authenticate only through external IdPs for a scope, remove the built-in identity provider assignment. For more information, refer to [Manage identity providers](manage-external-idps.md#remove-built-in-idp-assignment).

If you want users associated with an external provider to retain their profile and associated roles, they should use the same email address as on the built-in provider. For more details, refer to [User matching and profile creation](identity-claims-email-verification.md#claim-mapping-logic).

The way you configure scopes differs slightly depending on the authentication protocol:

* **OpenID Connect providers**: You can apply the same IdP configuration to multiple scopes (both organization and any number of stages).
* **SAML 2.0 providers**: You can only define one scope (organization **or** a specific stage) per configuration. However, you can still create and assign multiple SAML 2.0 providers to the same scope if needed.

## System considerations {#system-considerations}

ODC has the following limitations for external identity providers:

### System considerations for OpenID Connect

* ODC doesn't support dynamic issuer URIs, usually found in multi-tenant configurations of IdP apps. The Discovery endpoint needs to return static URIs. If you use dynamic URIs, the authentication process throws an error similar to:

    ```
    Wrong issuer from token.
    Got: https://login.microsoftonline.com/<customer-tenant-id>/v2.0
    Expected: https://login.microsoftonline.com/{tenantid}/v2.0
    ```

* Only the `client_secret_post` authentication method is supported.

### System considerations for SAML 2.0

* Only SAML 2.0 SP-initiated flows are supported.
* OutSystems recommends that SAML responses are signed.

<div class="info" markdown="1">

For the supported external identity providers, refer to the [OutSystems system requirements for ODC](../../getting-started/system-requirements.md#supported-external-identity-providers).

</div>

## Adding and using an external IdP {#configuring-using-idp}

This section guides you through the process of adding, assigning, and using an external IdP in your apps.

### Step 1: Add an external IdP {#add-an-external-idp}

ODC admins can configure an external IdP by navigating to the **ODC Portal** > **Manage** > **Identity providers** tab. A list of built-in providers and any external IdPs already added displays.

The configuration process depends on the authentication protocol your identity provider uses:

* **[Add an OpenID Connect provider](configure-openid-connect.md)**

    Use this option for identity providers that support the OpenID Connect standard. This includes most commercial IdPs such as Microsoft Entra ID, Microsoft Entra External ID (formerly known as Azure AD B2C), Okta, and Google.

* **[Add a SAML 2.0 provider](configure-saml2.md)**

    Use this option for enterprise identity providers that use the SAML 2.0 standard.

* **[Add a Social provider with accelerators](configure-social-accelerators.md)**

    Use this option to add social authentication providers such as Apple, Google, Facebook, or LinkedIn using ODC's built-in accelerators.

For specific guidance on popular providers, refer to:

* [Microsoft Entra ID (OpenID Connect)](azure-ad.md)

* [Okta (OpenID Connect)](okta.md)

### Step 2: Configure the redirect URIs {#idp-configure-uri}

<div class="info" markdown="1">

Applies to OIDC only, including social providers with accelerators, as they use OIDC.

</div>

Copy the Login and Logout URLs from the ODC Portal and paste them in your provider's portal. Refer to [Set up redirect URIs for an external IdP](redirect-uris.md) for full instructions.

### Step 3: Assign an external IdP {#assign-an-external-idp}

Refer to the dedicated article for assignment steps: [Assign an external identity provider](assign-idp.md).

### Step 4: Use an external IdP in your apps (for end-users only) {#use-an-idp-in-your-apps}

After you assign a provider to a stage, apps in that stage can use it for end-user sign-in. For apps created with ODC Studio version 1.3.0 or later, the pre-built login screen already includes the IdPs assigned to the stage (for example, Development), so you typically don’t need to change any login logic in the app. Make sure that only the IdPs you want to expose to all apps in a stage are assigned to that stage.

If you’re working with apps that were created before this built-in logic was added, or if you want to customize or override the default behavior, you can choose one of the following options:

**Option 1: Do nothing (default behavior)**
:   Rely on the pre-built login screen that ODC Studio provides. The login screen automatically lists the IdPs assigned to the app’s stage. You manage which IdPs are shown to end-users by assigning or unassigning them from the stage in the ODC Portal.

**Option 2: Delete the built-in login screen and redirect to an external provider**  
:   Use this option when you want to completely replace the built-in login experience and always redirect users to a single external IdP. For detailed steps, refer to [Delete the built-in login screen and redirect to an external provider](apps-delete-login-screen.md).

**Option 3: Modify the built-in login screen to add buttons for external provider login**  
:   Use this option when you want to keep the built-in login (for example, the built-in provider) and add one or more buttons for external IdPs, or when you want to customize how external providers appear. For detailed steps, refer to [Modify the built-in login screen to add buttons for external provider login](apps.md).

<div class="info" markdown="1">

If an app doesn't include the pre-built login logic (for example, an older app created before the pre-built login screen was available, or an app where the login flows were heavily customized), you can either follow Option 2 or Option 3 to implement or update the required login flows, or create a new app, inspect its pre-built login screen and related flows, and copy the relevant logic into your existing app.

</div>

### (Optional) Step 5: Add an end-user group mapping

Mapping groups from your identity provider to end-user groups in ODC can automate the assignment of roles to end-users based on their group membership, streamlining access management. For more details about how these groups are mapped and for setup instructions and best practices, refer to [IdP and end-user group mapping](end-user-group-mapping.md).

## Related resources

* [Manage identity providers](manage-external-idps.md): Replace, unassign, edit, or delete external IdPs and remove the built-in identity provider assignment
* [Identity claims, email verification, and profile matching logic](identity-claims-email-verification.md)
* [Best practices for user management](../../user-management/best-practices-user-management.md)
* [Managing authorization and authentication for end-users](../../user-management/end-users/intro.md)
* [Managing authorization and authentication for members (IT-users)](../../user-management/it-users/intro.md)
