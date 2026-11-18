---
guid: df369b59-5c40-4954-9622-722503ee54d1
locale: en-us
summary: Grant and revoke user roles in OutSystems Developer Cloud (ODC) for members and end-users across organization, asset, and stage scopes.
figma: https://www.figma.com/design/KpEoUxciqaFLGLlZxo7Hiu/User-management?node-id=3883-106&t=9snmrSiMZOFs7g77-1
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - Platform administrator
tags:
  - Authorization
  - End-users
  - IT Roles
  - IT Teams
  - IT Users
  - Roles
outsystems-tools:
  - odc portal
coverage-type:
  - apply
topic:
  - assign-asset-scope-roles
  - assign-end-user-roles-odc
  - assign-org-scope-role
isautopublish: true
---

# Grant and revoke user roles

This article explains how to grant and revoke user roles in OutSystems Developer Cloud (ODC). Assigning and revoking roles helps you manage the [authorization](intro.md#authorization) for both members (IT-users) and end-users, ensuring they have the appropriate level of access to your organization's resources and applications.

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

## Grant or revoke user roles

You can manage user roles for both members [(IT-users)](#grant-roles-to-members) and [end-users](#grant-roles-to-end-users) in the ODC Portal. The process varies depending on the type of user and the scope of access you want to manage.

### Grant or revoke roles for members (IT-users) {#grant-roles-to-members}

Members (IT-users) can have roles at different scopes within your organization. You can assign organization-level roles for tenant-wide access, team roles for every asset a team owns, or app-specific roles for granular permissions. In a multi-portfolio organization, you assign roles per portfolio. For more information, refer to [User management with multiple portfolios](../manage-platform-app-lifecycle/portfolios/portfolios-user-management.md).

To grant or revoke a role for a member (IT-user):

1. Go to the **ODC Portal**.

1. Go to **Management** > **Govern** > **Users**.

1. Search for the member you want to update, and then click anywhere in the user's row.

1. Go to the **Organization access** tab.

1. To grant or revoke a role at the [**Organization scope**](intro.md#organization-app-stage-and-app-scope):

    1. On the **Organization scope** area, click **Edit role**.

    ![Screenshot of the ODC Portal showing the option to edit roles at the Organization scope for a user.](images/organization-scope-pl.png "Edit role at Organization scope")

    1. Change the role:
        * To grant a role, pick one option from the dropdown list.  
        * To revoke a role, pick **No role** from the dropdown list.

    1. Click **Save**.

    <div class="info" markdown="1">

    You can't have more than one role for the organization scope. Consider adding a [custom role](roles.md#custom-roles) with the permissions you want instead, or [adding the member to a team](it-users/manage-teams.md#add-members) to grant them access on the assets the team owns.

    </div>

1. To grant or revoke roles at the **Team scope**:

    1. The **Team scope** area lists the teams the user is already a member. If the user if not assign to any team yet, click **assign teams** to add the user to teams.

        ![Screenshot of the ODC Portal showing the Team scope area with no teams yet.](images/team-scope-assign-teams-pl.png "Assign teams to a user")

        Otherwise, click **Manage roles** to change or revoke the member's role on a team.

        To add the member to another team, refer to [Add members to a team](it-users/manage-teams.md#add-members).

        ![Screenshot of the ODC Portal showing the Team scope area with a member's teams and roles, and the Manage roles button highlighted.](images/team-scope-pl.png "Manage roles in the Team scope")

    1. Change the roles:
        * To change the member's role in a team, pick the new team role from the dropdown list.  
        * To revoke the member's role in a team, pick **No role** from the dropdown list. By revoking the member's role in a team, you remove that member from the team.

    1. Click **Save**.

1. To grant or revoke roles at the [**Assets scope**](intro.md#organization-app-stage-and-app-scope):
    1. On the **Assets scope** area, click **Manage roles**.

        ![ODC Portal user details page on the Organization access tab, with the Manage roles button highlighted in the Assets scope section.](images/asset-scope-pl.png "Manage roles in the Assets scope")

    1. Change the roles:
        * To grant a role, pick the role you want for each asset from the dropdown list. You can use the **Search assets** box to find the asset, or filter by **Portfolio**, if your organization uses [multiple portfolios](../manage-platform-app-lifecycle/portfolios/portfolios-overview.md).  
        * To revoke a role, pick **No role** for the relevant asset from the dropdown list.

    1. Click **Save**.

The user immediately receives or loses the permissions associated with the chosen roles.

<div class="info" markdown="1">

If you remove all roles from a user, the user may lose access to the ODC Portal, Studio, or assets, depending on your configuration.

</div>

### Grant or revoke roles for end-users {#grant-roles-to-end-users}

End-users can have roles that control their access to specific applications and stages. These roles determine what features and data end-users can access within your applications.

To grant or revoke a role for an end-user:

1. Go to the **ODC Portal**.

1. Go to **Management** > **Govern** > **Users**.

1. Search for the end-user you want to update, and then click anywhere in the user's row.

1. Go to the **End-user access** tab, and then click **Manage roles**.

1. In the **Manage roles** dialog, search for the app by name. To show one stage only, select it in the **Stage** dropdown.

1. Select or clear the checkbox for each role and stage (**Development**, **QA**, or **Production**) that you want to assign to or revoke from the user. The **Pending changes** tab lists your changes before you save them.
  
    ![Screenshot of the ODC Portal showing the option to assign roles to end-users for different apps and stages.](images/end-user-roles-pl.png "Assign roles to end-users")

    For more information on how to create end-user roles, refer to [Secure your app with end-user roles](secure-app-with-roles.md#create-end-user-roles).

1. Click **Save**.

The end-user immediately receives or loses the roles you assign or remove. If your applications already use these roles to control access or behavior, the changes take effect right away, and the end-user's access or experience updates accordingly.

<div class="info" markdown="1">

If you remove all roles from an end-user, the user may lose access to the associated apps.

</div>

## Related resources

* [Teams and asset ownership](it-users/teams.md)
* [Create and manage teams](it-users/manage-teams.md)
* [Best practices for user governance](best-practices-user-management.md)
* [Managing members (IT-users)](it-users/intro.md)
* [Managing end-users](end-users/intro.md)
* [Password management in ODC](passwords.md)
* [User management](intro.md)
