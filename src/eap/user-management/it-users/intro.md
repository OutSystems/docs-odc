---
guid: 543d1a8f-c7cf-4bdb-8b67-28634a6f750a
locale: en-us
summary: Learn how to manage the authorization and authentication of IT users in OutSystems Developer Cloud (ODC), including role assignments and access control.
figma:
coverage-type:
  - apply
  - understand
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - platform administrators
  - full stack developers
tags: authorization, authentication, role assignments, access control, user management
outsystems-tools:
  - odc portal
  - odc studio
topic:
  - authentication-mechanisms
  - built-in-mechanisms
  - external-auth-mechanisms
  - user-roles
---

# Managing authorization and authentication for members (IT-users)

This article provides a high-level overview of how to manage [authentication and authorization](../intro.md#authentication-and-authorization-in-odc) for [members (IT-users)](../intro.md#members-it-users) in OutSystems Developer Cloud (ODC).

You can use either ODC's built-in authentication or integrate with an external Identity Provider (IdP) that supports OpenID Connect.

## Managing members (IT-users) with built-in authentication

With built-in authentication, you manage members (IT-users) directly in the ODC Portal.

To manage members using built-in authentication, follow these steps:

1. (Optional) [Create custom roles](../roles.md#create-custom-roles-for-members-it-users): Define [roles](../roles.md) with specific permissions in the ODC Portal.

1. [Create members](../create-deactivate-and-delete-users.md#create-new-members-it-users): Add new users in the ODC Portal at the organization or app level during creation. You can also [create users programmatically using APIs](../../reference/apis/identity-v1.md), without assigning roles.

1. [Grant or revoke roles](../grant-and-revoke-user-roles.md#grant-roles-to-members): Assign or remove roles as needed. If roles were assigned during creation, use this step only to make changes. You can also assign roles using [APIs](../../reference/apis/identity-v1.md).

## Managing members (IT-users) with external IdP authentication

You can configure ODC to use an external IdP (such as Microsoft Entra ID or Google) for authentication.

To manage members with external IdP authentication, follow these steps:

1. (Optional) [Create custom roles](../roles.md#create-custom-roles-for-members-it-users): Define [roles](../roles.md) with specific permissions in the ODC Portal.

1. [Configure an IdP](../../manage-platform-app-lifecycle/external-idps/intro.md): Set up an IdP and [assign](../../manage-platform-app-lifecycle/external-idps/intro.md#assign-an-external-idp) it to your organization (tenant) or stage you want in the ODC Portal.

1. Add members. Choose one of the following options:

    * Manually: [Invite users](../create-deactivate-and-delete-users.md#create-new-members-it-users) by using the email associated with their IdP account.

    * Programmatically: [Create users via API](../../reference/apis/identity-v1.md).

    * Automatically: Wait for the member to be created after their first successful login through the IdP.

    <div class="info" markdown="1">

    Members who haven't been manually added or added via API can still sign in through the IdP.

    When users log in using an external IdP, ODC automatically registers them after their first successful login.

    For more details about mapping claims when configuring an IdP, refer to [Understand the user creation and claim mapping logic](../../manage-platform-app-lifecycle/external-idps/intro.md#claim-mapping-logic).

    </div>

1. [Grant or revoke roles](../grant-and-revoke-user-roles.md#grant-roles-to-members): After creation, assign roles to members manually in the ODC Portal. If you assigned roles during manual user creation, you only need to use this step if you want to change the assigned roles later. You can also assign roles using [APIs](../../reference/apis/identity-v1.md).

## Related resources

* [Best practices for user management](../best-practices-user-management.md)
* [Roles and permissions for members (IT-users)](../roles.md)
* [Create, activate, deactivate, and delete users](../create-deactivate-and-delete-users.md)
* [Grant and revoke user roles](../grant-and-revoke-user-roles.md#grant-roles-to-members)
* [Configure authentication with external identity providers](../../manage-platform-app-lifecycle/external-idps/intro.md)
* [Managing authorization and authentication for end-users](../end-users/intro.md)
* [Password reset](../passwords.md#reset)
