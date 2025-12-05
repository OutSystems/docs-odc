---
guid: 32f57458-d846-40e5-bef8-154c0bca4e41
locale: en-us
summary: Learn how to create, deactivate, and delete users in the system.
figma: https://www.figma.com/design/KpEoUxciqaFLGLlZxo7Hiu/User-management?node-id=3704-89
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - platform administrators
  - full stack developers
tags: user management,create user,deactivate user,delete user,user roles
outsystems-tools:
  - odc portal
coverage-type:
  - apply
topic:
  - manage-users
  - deleting-users
  - assign-to-user-groups
  - built-in-authentication
  - creating-users
helpids: 30703
---

# Create, activate, deactivate, and delete users

This article explains how to create, activate, deactivate, and delete users in OutSystems Developer Cloud (ODC), covering both members (IT-users) and end-users. These actions help you manage access to your organization’s resources and applications efficiently and securely.

<div class="info" markdown="1">

To manage users programmatically, refer to [User and access management API](../reference/apis/identity-v1.md) and [ODC REST APIs](../reference/apis/public-rest-apis/overview.md).

</div>

## Required permissions

To view the permissions required for managing users, refer to [Roles and permissions for members (IT-Users)](roles.md).

## Creating users

You can add users to your ODC organization (tenant) as either [members (IT-users)](#create-new-members) or [end-users](#create-new-end-users).

<div class="info" markdown="1">

When users log in using an external IdP, ODC automatically registers them after their first successful login.

For more details about mapping claims when configuring an IdP, refer to [Understand the user creation and claim mapping logic](../manage-platform-app-lifecycle/external-idps/intro.md#claim-mapping-logic).

For more information about granting roles, refer to [Grant and revoke user roles](grant-and-revoke-user-roles.md).

</div>

### Create new members (IT-users) {#create-new-members}

To manually register [members (IT-users)](intro.md#members-it-users), follow these steps:

1. Go to the **ODC Portal**.

1. Under **Manage**, go to **Users**.

1. Click **Invite user**.

1. Enter the user’s email address, and then expand **Organization access**.

1. Assign roles to the user. Choose a [scope](intro.md#organization-app-stage-and-app-scope):

    * **Organization**: Choose a role for the tenant.

    * **Apps**: For each app, choose a role or leave it as **Unassigned** if you don't want to assign a role to the user for that app.

      ![Screenshot of the Invite user screen in ODC Portal showing fields for email, organization access, and scope selection.](images/create-new-member-pl.png "Invite new member in ODC Portal")

    <div class="info" markdown="1">

    For more details about how permissions are applied at the **organization** or **apps** scope, refer to [effective permissions](roles.md#effective-permissions-calculation) calculation.

    </div>

1. Click **Send invite**.

    The invited user receives an email with a verification code and a link to join your tenant in the ODC Portal.

    <div class="info" markdown="1">

    To edit the roles you assigned during the creation process, refer to [Grant and revoke user roles](grant-and-revoke-user-roles.md).

    </div>

### Create new end-users {#create-new-end-users}

<div class="info" markdown="1">

 You can enable self-registration in your app to allow end-users to sign up on their own. For more information, see the [Self-registration flow](../building-apps/ui/self-registration/intro.md).

</div>

To manually register [end-users](intro.md#end-users), follow these steps:

1. Go to the **ODC Portal**.
1. Under **Manage**, go to **Users**.
1. Click **Invite user**.
1. Enter the user’s email address, and then expand **End-user access**.
1. Select the [end-user groups](./end-users/groups.md) you want to assign to the user.
1. From the list of roles available for each app, select all applicable roles.  

    For more information on how to create end-user roles, refer to [Secure your app with end-user roles](secure-app-with-roles.md#create-end-user-roles).

1. Click **Send invite**.

    The invited user receives an email with a verification code and a link to join your tenant in the ODC Portal.

    <div class="info" markdown="1">

    To edit the roles you assigned during the creation process, refer to [Grant and revoke user roles](grant-and-revoke-user-roles.md).

    </div>

## Deactivate and activate users

You can deactivate users to temporarily prevent them from accessing the ODC Portal, Studio, or any apps, while retaining their data and assignments for auditing or future reactivation. You can reactivate users at any time to restore their access.

To deactivate or activate a user, follow these steps:

1. Go to the **ODC Portal**.
1. Under **Manage**, go to **Users**.
1. For each user you want to update, under **Actions**, click the three dots (**...**).
1. Click **Deactivate user** or **Activate user** as appropriate, and then confirm the action.

    ![Screenshot illustrating the deactivation of users in the ODC Portal with the Deactivate user option highlighted.](images/deactivate-pl.png "Deactivate users in ODC Portal")

    The user's status updates to **Inactive** or **Active** based on your action.

## Delete users

Deleting a user permanently removes their access and all related data from the system. This action can't be undone.

1. Go to the **ODC Portal**.
1. Under **Manage**, go to **Users**.
1. For each user you want to delete, under **Actions**, click the three dots (**...**).
1. Click **Delete**, and then confirm the action.

    ![Screenshot illustrating the deletion of users in the ODC Portal with the Delete user option highlighted.](images/delete-pl.png "Delete users in ODC Portal")

<div class="warning" markdown="1">

Deleting a user can't be undone. If you may need to restore access in the future, consider deactivating the user instead.

</div>

<div class="info" markdown="1">

When users are deleted at the external IdP, ODC logs them out at the next refresh when using OIDC with refresh tokens (the `offline_access` scope). Refer to [Refresh token-driven user revalidation (OIDC only)](../manage-platform-app-lifecycle/external-idps/intro.md#refresh-token-sync-oidc).

</div>

## Related resources

* [Best practices for user governance](best-practices-user-management.md)
* [Managing members (IT-users)](it-users/intro.md)
* [Managing end-users](end-users/intro.md)
* [Password management in ODC](passwords.md)
* [Grant and revoke roles](grant-and-revoke-user-roles.md)
* [Create custom roles for members (IT-users)](roles.md)
* [Create end-user roles](secure-app-with-roles.md)
* [User management](intro.md)
