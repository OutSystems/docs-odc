---
summary: Replace, unassign, edit, or delete external identity providers and avoid lockout scenarios in OutSystems Developer Cloud (ODC).
locale: en-us
guid: d1584f5d-164f-4411-9846-77651e486d89
audience:
  - platform administrators
platform-version: odc
topic:
  - external-idps
  - idp-openidp
  - idp-saml
coverage-type:
  - apply
  - understand
tags: external identity providers,idp management,odc authentication,idp replacement,idp lifecycle
outsystems-tools:
  - odc studio
  - odc portal
figma: 
app_type: mobile apps,reactive web apps
helpids: 
---

# Manage external identity providers

This article covers the lifecycle management of your external IdPs, including replacing, unassigning, and deleting them.

## Prerequisites

You must have the [**Manage authentication**](../../user-management/roles.md#permissions-registry) permission.

## Replace an external IdP {#replace-idp}

To replace an external identity provider (IdP) in ODC, follow these steps:

1. Complete steps 1–3 (up to and including “Assign an IdP”) in [Configuring and using an external IdP](intro.md#configuring-using-idp) for your new provider.

1. If any apps implement custom login logic (for example, use a setting or explicitly set the **IdentityProvider** property), update those apps to use the new provider:

    * If you use a setting with the IdP name, [update the setting in the ODC Portal](../configure-app-settings.md#view-and-edit-default-values-of-the-app-settings) so all your apps are directed to the new IdP. There's no need to republish the apps.

    * If you don’t use a setting with the IdP name, in each app in ODC Studio set the **IdentityProvider** property to your IdP name (instead of `GetMyProvider.MyProvider`) wherever you set it (refer to [Delete the built-in login screen and redirect to an external provider](apps-delete-login-screen.md) or [Modify the built-in login screen for external provider login](apps.md)). Then, republish the apps.

    <div class="info" markdown="1">

    If your apps rely only on the pre-built login screen with stage-assigned IdPs and don’t have custom login logic, you typically don’t need to change the apps when you replace a provider. Updating the IdP assignments in the ODC Portal is enough.

    </div>

1. After verifying successful authentication with the new IdP, [unassign the old IdP](#unassign-idp).

By following these steps, you help ensure continuous authentication, preserve user profile associations, and minimize the risk of authentication failures or loss of user access.

<div class="info" markdown="1">

These instructions also apply if you need to change the issuer for an external IdP.

The issuer is a unique identifier for your external IdP. ODC relies on it to associate user profiles with the correct IdP configuration. If you must change the issuer, always configure a new IdP in ODC rather than editing the existing one. This approach maintains proper user profile linkage and ensures authentication continuity.

</div>

## Unassign an external IdP {#unassign-idp}

When you need to remove an existing external identity provider from your organization or apps, use the following options:

* **OpenID Connect providers**: Use the **Manage assignments** button to modify or remove assignments.

* **SAML 2.0 providers**: Use the **Unassign** button to remove the provider assignment.

## Edit or delete an external IdP

You can only edit or delete a provider that is not in use. To edit or delete an external IdP, navigate to the **ODC Portal** > **Manage** > **Identity providers** . Then, follow these steps:

1. Click on the provider card you want to edit or delete.

1. Click the **ellipsis** (3-dots) to the right of the **Assign** button. Then click the **Edit configurations** or **Delete provider** button to launch the edit page or launch the delete confirm pop-up.

<div class="info" markdown="1">

To edit an identity provider, you must submit the correct **client secret** again.

</div>

<div class="info" markdown="1">

For SAML 2.0 providers, the **scope cannot be changed** after the provider is created. If you need to assign a different scope, add a new SAML identity provider and select the desired scope during setup.

</div>

## Avoid lockout scenarios {#lockout}

A lockout occurs when all users lose access to the ODC Portal and ODC Studio, or any apps developed in ODC.

This can happen if you remove the built-in IdP assignment on the **Identity Providers** page in the ODC Portal, either for the organization (for IT-users) or an app stage (for end-users), and your external IdP isn't working correctly.

<div class="warning" markdown="1">

If you plan to remove the built-in IdP assignment from the **Identity providers** page in the ODC Portal, make sure to fully test the external IdPs before you remove the built-in IdP assignment.

</div>

To avoid lockouts when changing providers, refer to [Replace an external IdP](#replace-idp).

There are a few reasons why your external IdP might not be working correctly. It could be because you didn't set it up correctly or assign it to the appropriate stage. It could also be due to an issue on the provider's side.

If you encounter a lockout scenario, open a support ticket. A support agent can sign in to the tenant and reactivate the built-in provider. This allows users to log in or reset passwords for accounts using the built-in provider.

## Related resources

* [Configuring authentication with external identity providers](intro.md)
* [Assign an external identity provider](assign-idp.md)
* [Identity claims, email verification, and profile matching logic](identity-claims-email-verification.md)
