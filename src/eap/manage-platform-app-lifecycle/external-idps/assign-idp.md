---
summary: Assign an external identity provider to your organization or app stages in OutSystems Developer Cloud (ODC).
locale: en-us
guid: 883c4583-27f6-4617-bcba-9cb26c4abd9e
audience:
  - platform administrators
  - full stack developers
platform-version: odc
topic:
  - external-idps
  - idp-openidp
  - idp-saml
coverage-type:
  - apply
  - understand
figma: 
app_type: reactive web apps,mobile apps
tags: authentication,identity provider,saml,external idp assignment,odc
outsystems-tools:
  - odc portal
helpids: 
---

# Assign an external identity provider

After you add an external identity provider (IdP), assign it to one or more [scopes](intro.md#scopes-for-assigning-idps) so users can authenticate with it.

## Prerequisites

Before you begin, ensure the following:

* The IdP configuration exists (refer to [Add an external IdP](intro.md#add-an-external-idp)).
* You must have the [**Manage authentication**](../../user-management/roles.md#permissions-registry) permission.

## Assign an IdP to your organization or to a stage

To assign an existing external IdP, follow these steps:

1. In the ODC Portal go to **Manage** > **Identity providers**.

1. Click on the provider card you want to assign.

1. Check the summary in the **Configurations** tab. The available button depends on the provider type and current assignment status:

    * For SAML 2.0, click **Assign**.

    * Otherwise, click **Manage assignments**.

1. Check the boxes for the scopes where you want to assign the provider, and then click **Next**.

    <div class="info" markdown="1">

    For scope behavior and options, refer to [Scopes for assigning IdPs](intro.md#scopes-for-assigning-idps).

    </div>

    <div class="info" markdown="1">

    When you switch the IdP for your organization or apps, all signed-in users are automatically logged out and prompted to log in again.

    For providers that use a client secret, changes can take up to 1 hour to take effect due to caching. During this time, ODC continues to use the old client secret. Keep the old client secret configured in your external IdP for at least 1 hour to prevent downtime.

    </div>

1. Read the confirmation pop-up and then do one of the following:

    * Click **Confirm changes** to proceed.

    * Click **Cancel** to exit.

    Once ODC applies the provider successfully, a notification displays.

When you assign a provider for the organization's use, you don't need to do anything else. The option to log in with the provider becomes immediately available for users on the ODC Portal and ODC Studio login screens.

## Next steps

Choose your next step depending on your use case:

* For end-users: [Use an IdP in your apps](intro.md#use-an-idp-in-your-apps)

* Optional: [Add an end-user group mapping](end-user-group-mapping.md)

## Related resources

* [Manage external identity providers](manage-external-idps.md): Replace, unassign, edit, or delete IdPs
* [Identity claims, email verification, and profile matching logic](identity-claims-email-verification.md)
* [Configuring authentication with external identity providers](intro.md)
* [Set up redirect URIs](redirect-uris.md)
