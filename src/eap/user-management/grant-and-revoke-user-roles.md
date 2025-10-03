---
guid: df369b59-5c40-4954-9622-722503ee54d1
locale: en-us
summary: Learn how to grant and revoke user roles in OutSystems Developer Cloud (ODC) to manage access and permissions effectively.
figma: 
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - full stack developers
  - platform administrators
tags: user roles,permissions
outsystems-tools:
  - odc portal
coverage-type:
  - apply
topic:
  - manage-users
  - assign-to-org-roles
  - updating-users
  - authorization
  - user-management
---

# Grant and revoke user roles

This article explains how to grant and revoke user roles in OutSystems Developer Cloud (ODC). Assigning and revoking roles helps you manage the [authorization](intro.md#authorization) for both members (IT-users) and end-users, ensuring they have the appropriate level of access to your organization’s resources and applications.

<div class="info" markdown="1">

To manage roles programmatically, refer to [User and access management API](../reference/apis/identity-v1.md) and [ODC REST APIs](../reference/apis/public-rest-apis/overview.md).

</div>

## Prerequisites

Before you can grant or revoke user roles, make sure you meet the following conditions:

* **Users must be registered:** Users must already be created in your ODC organization (tenant) before you can grant or revoke roles. For instructions on creating users and assigning roles during creation, refer to [Create, activate, deactivate, and delete users](create-deactivate-and-delete-users.md).
* **Required permissions:** To manage roles, you need the appropriate permissions. For details, refer to [Roles and permissions for members (IT-Users)](roles.md).
* **Roles must be created**:

    * For more details on how to create custom roles for members (IT-users), refer to [Roles and permissions for IT Users](roles.md).

    * For more details on how to create end-user roles, refer to [Secure your app with end-user roles](secure-app-with-roles.md).

## Granting or revoking users roles

You can manage user roles for both members [(IT-users)](#grant-roles-to-members) and [end-users](#grant-roles-to-end-users) in the ODC Portal.

## Grant or revoke roles for members (IT-users) { #grant-roles-to-members }

To grant or revoke a role for a member (IT-user):

1. Go to the **ODC Portal**.
1. Under **Manage**, go to **Users**.
1. Search for the member you want to update, and then click anywhere in their row.

1. To grant or revoke a role at the [**Organization scope**](intro.md#organization-app-stage-and-app-scope):

    1. On the **Organization access** tab, click **Edit role**.
    1. Change the role:
        * To grant a role, pick one option from the dropdown list.
        * To revoke a role, pick **No role** from the dropdown list.
    
    <div class="info" markdown="1">

    You can't have more than one role for the organization scope. Consider to add a [custom role](roles.md#custom-roles) with the permissions you want instead.

    </div>

1. To grant or revoke roles at the [**Assets scope**](intro.md#organization-app-stage-and-app-scope):

    1. On the **Organization access** tab, click **Assign roles**.
    1. Change the roles:
        * To grant a role, pick the role you want for each app from the dropdown list.  
        * To revoke a role, pick **Unassigned** for the relevant app from the dropdown list.

1. Click **Save**.

The user immediately receives or loses the permissions associated with the chosen roles.

<div class="info" markdown="1">

If you remove all roles from a user, they may lose access to the ODC Portal, Studio, or specific apps, depending on your configuration.

</div>

## Grant or revoke roles from end-users { #grant-roles-to-end-users }

To grant or revoke a role from an end-user:

1. Go to the **ODC Portal**.
1. Under **Manage**, go to **Users**.
1. Search for the end-user you want to update, and then click anywhere in their row.
1. Go to the **End-user access** tab, and then click **Assign roles**.
1. Select or clear the checkbox for the roles corresponding to each app and stage (**Development**, **QA**, or **Production**) to which you want to assign or revoke a role to the user.

    For more information on how to create end-user roles, refer to [Secure your app with end-user roles](secure-app-with-roles.md#create-end-user-roles).

1. Click **Save**.

The end-user immediately receives or loses the roles you assign or remove. If your applications already use these roles to control access or behavior, the changes take effect right away, and the end-user’s access or experience will update accordingly.

<div class="info" markdown="1">

If you remove all roles from an end-user, they may lose access to the associated apps.

</div>

## Related resources

* [Best practices for user governance](best-practices-user-management.md)
* [Managing members (IT-users)](it-users/intro.md)
* [Managing end-users](end-users/intro.md)
* [Password management in ODC](passwords.md)
* [User management](intro.md)
