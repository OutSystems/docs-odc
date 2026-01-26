---
helpids: 30493, 30704
summary: OutSystems Developer Cloud (ODC) features organization and end-user roles to manage access and permissions within its development environment.
locale: en-us
guid: 766ab743-31f2-4f58-ad91-a4cd0db8ab93
app_type: mobile apps,reactive web apps
figma: https://www.figma.com/design/KpEoUxciqaFLGLlZxo7Hiu/User-management?node-id=3717-132
platform-version: odc
tags: access management,permissions,user onboarding,user roles,organization management
audience:
  - full stack developers
  - platform administrators
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - understand
  - apply
topic:
  - role-assignment
  - create-a-team
---

# Roles and permissions for members (IT-users)

This article covers permissions for [members (IT-users)](intro.md#members-it-users) who build and manage apps in ODC. For information about end-user roles, refer to [Secure your app with end-user roles](secure-app-with-roles.md).

In ODC, you control what your members (IT-users) can do by assigning them roles. A role is a set of permissions that you can grant at the **organization** and **asset** (**app**) [**scopes**](intro.md#organization-app-stage-and-app-scope).

ODC allows implementing user access control policies on these domains:

* Asset (apps and libraries) management
* Stage visibility
* Release management
* Application monitoring
* Analyze
* Configuration and connection management
* User management
* Forge access
* Support cases management
* Subscription management

## Effective permissions calculation { #effective-permissions-calculation }

Permissions are applied at the **organization** or **app stage** [scope](intro.md#organization-app-stage-and-app-scope). A user's total permissions are the sum of all roles assigned to them at both the **organization** and **asset** (**app**) [**scopes**](intro.md#organization-app-stage-and-app-scope). You can assign one role for the organization scope, and one role for each app.

![Diagram illustrating scopes with roles and permissions](images/role-permission-diag.png "Scopes for roles and permissions")

The fundamental rule is that permissions are cumulative. A role assigned at the app scope adds to the permissions granted at the organization scope.

<div class="info" markdown="1">

An app-level role can grant additional permissions for that specific app, but it can't revoke permissions a user already has from an organization-level role.

</div>

### Permission scenarios

Here's how this principle works in practice.

**Scenario 1: A more permissive role is assigned at the app level**
:   A user has a general role for the organization but needs elevated permissions for one app:

    * Organization Role: Developer.
    * App Role: Administrator.
    * Result: The user has Developer permissions across the organization. For the specific app where they're an Administrator, they gain the additional permissions of that role. For example, they can now manage that app's configurations in Production stage, a permission the Developer role doesn't have.

**Scenario 2: A less permissive role is assigned at the app level**
:   A user has a high-level role for the organization, and a more restrictive role is assigned for one app:

    * Organization Role: **Administrator**.
    * App Role: **Developer**.
    * Result: The organization-level permissions prevail. Since app-level roles can't remove permissions, the user remains an Administrator for the entire organization, including the specific app. The Developer role at the app level has no effect.

## Types of roles for members (IT-users) {#types-of-roles}

ODC provides two types of roles for members (IT-users), built-in roles, and custom roles.

<div class="info" markdown="1">

For details on how to assign or remove roles for members, refer to [Grant and revoke user roles](grant-and-revoke-user-roles.md#grant-roles-to-members).

</div>

### Built-in roles

ODC includes two built-in organization roles:

| Role | Description |
| ---------------- | --------------------------------------------------------------------------------------------- |
| Administrator | Full access to all platform features, including user management, deployment, and configuration. |
| Developer | Access to build and manage apps. Can invite new users and grant end-user roles, but only for the **Development** stage. |

You can't delete or modify built-in roles, but you can duplicate them to create custom roles.

To see the full list of permissions for the **Admin** or **Developer** role, in the ODC Portal, go to **Organization roles**, and then click **Admin** or **Developer**. Both roles display the **Built-in role** label.

### Custom roles {#custom-roles}

You can create custom roles to tailor permissions to your organization's needs. Custom roles let you select specific [permissions](#permissions-registry) and apply them at **organization** or **app stage** [scope](intro.md#organization-app-stage-and-app-scope). After creating a custom role, you need to assign it to users either at **organization scope** or to specific **apps**. For more details on creating custom roles and assigning roles to users, refer to [Create custom roles for members](#create-custom-roles-for-it-users) and [Grant or revoke roles to members](grant-and-revoke-user-roles.md#grant-roles-to-members).

For more details about recommended custom roles, refer to [Recommended custom roles for members (IT-users)](#recommended-custom-roles).

## Create custom roles for members (IT-users) {#create-custom-roles-for-it-users}

To create a custom role for members, follow these steps:

1. In the ODC Portal, under **Manage**, go to **Organization roles**.
1. Click **Create role**.
1. Enter a name for the role.
1. Select the permissions you want to assign. You may limit some [permissions](#permissions-registry) to specific stages if needed.  
1. Click **Create** to save the role.

## ODC permissions {#permissions-registry}

The following table lists the permissions you can assign to custom roles. For more details on **organization** (global) and **asset** (**app**) scope, refer to [Organization, app stage, and app scope](intro.md#organization-app-stage-and-app-scope).

<div class="info" markdown="1">

Some permissions are automatically inherited by others to ensure consistent behavior and prevent errors. When you configure custom roles in the ODC Portal, selecting a permission may automatically select additional related permissions due to these dependencies.

</div>

| Category | Permission Name | Purpose | Scope |
| --------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| Asset management | Open | Users can open assets. | Organization <br/> Asset |
| Asset management | Create | Users can create new assets. | Organization |
| Asset management | Debug | Users can view, open and debug assets. | Organization <br/> Asset |
| Asset management | Change | Users can view, open, debug and publish assets. | Organization <br/> Asset |
| Asset management | Delete | Users can delete assets. | Organization <br/> Asset |
| Portfolio management | View stage | Users can view a given stage. | Organization |
| Release management | Deploy assets | Users can initiate asset deployments to a specified stage and undeploy from the production stage. | Organization <br/> Asset |
| Release management | Release | Users can release an asset, assign a version number (1.0.0), and add release notes. | Organization <br/> Asset |
| Monitoring | Access asset logs and traces | Users can view asset logs and traces in a given stage. | Organization <br/> Asset |
| Monitoring | Access user information | Users can view user information connected to a given log or activity. | Organization <br/> Asset |
| Analyze | Manage code quality findings | Provides access to a Code Quality Console and interactive capabilities, including the ability to modify the status of findings and manage comments. Additionally, if permissions are set at the organizational level, users will see which organizational users have introduced those findings, change status, and add comments. | Organization <br/> Asset |
| Analyze | View code quality findings | Users can view code quality findings in apps they have permissions to open. | Organization <br/> Asset |
| Configuration management | View configurations | Users can view all configurations within this category for the selected stages. | Organization <br/> Asset |
| Configuration management | Edit configurations | Users can change app or library configurations in a given stage. | Organization <br/> Asset |
| Configuration management | Configure connections | Users can edit connection configurations in a given stage. | Organization |
| Configuration management | Manage domains | Users can create, edit, and delete stage level domains for end-user access. | Organization |
| Configuration management | Manage Email configuration | Users can create, edit, and delete SMTP emails. | Organization |
| Configuration management | Manage API clients | Users can manage API Clients, create, suspend, delete, change permissions, and rotate secrets.  <br/>**Note:** This permission allows users to create API clients that can modify their own permissions. | Organization |
| Configuration management | Manage CSP | The user can create, edit, and delete CSP (Content Security Policy) rules at each stage. | Organization |
| Configuration management | Manage app analytics stream | Users can view, create, edit, and delete streams. | Organization |
| Configuration management | Manage audit trail stream | Users can view, create, edit, and delete audit trail streams. | Organization |
| Configuration management | Manage IP filters | Users can create, edit, delete and assign IP rules to apps. | Organization |
| Configuration management | Manage private gateways | Users can activate and deactivate private gateways as well as renew a gateway's access token. | Organization |
| Connection management | Create | Users can create connections. | Organization |
| Connection management | Change | Users can edit entities, name, and description. | Organization |
| Connection management | Delete | Users can delete connections. | Organization |
| User management | View end-users | View users with end-user roles. | Organization <br/> Asset |
| User management | View members | Users can view users with organization roles. | Organization |
| User management | Manage users | View, activate, deactivate, and delete other organization members and end-users. | Organization |
| User management | Manage end-user access | Users can invite users and grant or revoke end-user roles. | Organization <br/> Asset |
| User management | Manage end-user groups | View, create, edit, and delete end-user groups. | Organization |
| User management | Manage member access | Users can invite organization members and grant or revoke organization roles. | Organization |
| User management | Manage organization roles | Users can create, edit, and delete organization roles. | Organization |
| User management | Manage authentication | The user with this permission can view and manage the authentication providers to access the organization and apps. | Organization |
| User management | View audit trail | This permission enables users to view the audit logs. | Organization |
| Forge | Install/Update assets | Users can install or update assets from Forge. | Organization |
| Forge | Submit/Edit assets | Users can submit assets to Forge and edit them. | Organization |
| Support | Open support cases | Users can open and view their support cases. | Organization |
| Support | View all support cases | Users can view all the organization's support cases. | Organization |
| Subscriptions | View subscription | Users can view the organization's subscription information. | Organization |
| Maintenance | View platform updates | Users can view the list of asset and platform updates. | Organization <br/> Asset |
| OutSystems 11 | Manage O11 configuration | Provides users access to OutSystems 11 configurations, allowing connectivity to the Conversion Assessment Tool on the O11 infrastructure and enabling Code Conversion and Data Migration. | Organization |

## Recommended custom roles for members (IT-users) {#recommended-custom-roles}

As a general guideline, you can create these custom roles based on the scope to use when assigning roles to a member:

* **App scope**: Basic Developer, Tech Lead.
* **Organization scope**: Basic Member, Architect, Tenant Admin.

In this reference model, the **Architect** role owns and manages the asset portfolio lifecycle, including creating, deleting, and installing assets from Forge, as well as managing releases. The **Tenant Admin** role focuses on global infrastructure configurations, not on asset or release management. If a user needs both sets of permissions, assign the built-in **Admin** role, which combines all capabilities.  

This approach supports a DevOps-oriented model, where delivery teams (**Tech Lead** + **Developers**) have full ownership of their assigned assets (and only theirs).

The following table outlines the permissions you can configure for each of these recommended custom roles:

| Category | Basic Developer | Tech Lead | Basic | Architect | Tenant Admin |
| ---------------------------------------- | --------------------------------------------------- | -------------------------------------------------------- | ------------------------- | --------------------------------------------------- | ----------------------------------------------------- |
| Asset management | Change assets | Change assets | Not allowed | Create and delete assets | Not allowed |
| Stage visibility | View all stages | View all stages | View Development Stage | View all stages | View all stages |
| Release management | Release Assets<br/>Deploy to Development | Release Assets<br/>Deploy to all stages | Not allowed | Release Assets<br/>Deploy to all stages | Not allowed |
| Monitoring | Monitor all stages | Monitor all stages<br/>View security vulnerabilities | Not allowed | Monitor all stages<br/>View security vulnerabilities | Monitor all stages<br/>View security vulnerabilities |
| Analyze | View <br/>Code Quality findings | Edit <br/>Code Quality finding | Not allowed | Edit <br/>Code Quality finding | Edit <br/>Code Quality finding |
| Configuration <br/>Connection management | Apply app configurations <br/>in Development | Apply app configurations <br/>in all stages<br/>Configure external entities | Not allowed | View app configurations <br/>in all stages<br/>Configure external entities | Apply infra configurations in all stages<br/>Create and delete connections <br/>Manage API Clients |
| User management | View end-users | Manage <br/>end-user access and groups | Not allowed | View organization users | Manage users and organization roles<br/>Manage authentication providers |
| Forge access | Not allowed | Submit assets | Not allowed | Install and submit assets | Not allowed |
| Support | Open support cases | Open support cases | Not allowed | Open and view <br/>all support cases | Open and view <br/>all support cases |
| Subscriptions | Not allowed | Not allowed | Not allowed | Not allowed | Allowed |

## Related resources

* [Managing authorization and authentication for members (IT-users)](it-users/intro.md)
* [Create, activate, deactivate, and delete users](create-deactivate-and-delete-users.md)
* [Grant or revoke roles to members](grant-and-revoke-user-roles.md#grant-roles-to-members)
* [Best practices for user governance](best-practices-user-management.md)
* [Role-based security](https://learn.outsystems.com/training/journeys/role-based-security-575) online course
* [Managing authorization and authentication for end-users](end-users/intro.md)
* [User management](intro.md)
