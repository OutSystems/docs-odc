---
summary: Learn how to manage end-user roles in OutSystems Developer Cloud (ODC) to control access to app functionalities, screens, and data.
tags: user role management, access control, security, outsystems developer cloud, user permissions
locale: en-us
guid: BDA3A144-0EB0-4C04-953F-9DED85A477FE
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3101%3A11327&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - apply
  - remember
topic:
  - secure-screen
  - app-roles
  - create-app-role
  - assign-roles
---

# Secure your app with end-user roles

When you create a role, and assign it to a user, you can control access to screens, data and functionalities of your app. Use ODC Studio to create roles and design logic to control access. Use the ODC Portal to assign roles to users.

When setting up roles for end-users, consider the following:

* What do the end-users need to accomplish?
* What screens do they need to access?
* What tasks do you want them to be able to do?
* What information can end-users see, and what needs to remain inaccessible?

## Managing end-user roles

This is an overview of how to use roles:

1. In ODC Studio, create end-user roles and publish the app.
1. In the ODC Portal, assign end-user roles to users per app and stage (for example, **Development**, **QA** or **Production**).
1. In ODC Studio, use end-user roles in your logic to control what end-users can do or access. You can also grant and revoke roles programmatically.

![Diagram illustrating the process of using roles in OutSystems Developer Cloud](images/overview-how-to-use-roles-diag.png "How you can use roles")

You can also use the ODC [User management REST APIs](../reference/apis/identity-v1.md) to manage users and access programmatically. For detailed information about how to use these APIs, refer to [Getting started](../reference/apis/public-rest-apis/getting-started.md).

### Create end-user roles {#create-end-user-roles}

To create end-user roles in ODC Studio, follow these steps:

1. In the **Logic** tab, right-click the **Roles** folder, and select **Add Role**.
1. In the new role properties, enter **Name** and **Description**.
1. If you want the role to be available in other apps or libraries, set **Public** to `Yes`. The default is `No`.
1. Publish the app so the role appears in the ODC Portal.

When you create a role, ODC Studio creates a set of related actions you can use to [manage roles](#manage-roles-in-app-runtime) during runtime.

### Assign end-user roles to users

After you publish an app, its end-user roles are available in the ODC Portal. For more details on how to assign end-user roles, refer to [Grant or revoke roles to end-users](grant-and-revoke-user-roles.md#grant-roles-to-end-users).

### Use end-user roles to control access in app runtime {#manage-roles-in-app-runtime}

After you create a role, ODC Studio also creates the following actions to let you manage the roles during the app runtime. These actions let you programmatically check, grant, or revoke a role in the app logic.

|Action|Example|Description|
|:-----|:------|:----------|
|Check&lt;ROLENAME&gt;Role*|CheckManagerRole|Returns `True` if the current user has the &lt;ROLENAME&gt; role.|
|Grant&lt;ROLENAME&gt;Role|GrantManagerRole|Grants the &lt;ROLENAME&gt; role to the user with the UserId.|
|Revoke&lt;ROLENAME&gt;Role|RevokeManagerRole|Revokes the &lt;ROLENAME&gt; role from the user with the UserId.|

(*) Available for both client and server logic. The light icon denotes the client-side version. The action applies to the currently logged-in user if the UserId parameter isn't specified.

## Control access in your app with end-user roles {#control-access-in-your-app-with-end-user-roles}

After you assign roles to your end-users, you can:

* Allow or block access to a screen
* Restrict access to data
* Restrict logic flows

![Diagram showing how to control access in your app with end-user roles](images/control-access-in-your-app-end-user-roles-diag.png "Control access in your app")

### Understanding role updates

Role changes take effect at different times depending on how and where you apply them:

* **Changes to current user's own role**: When you change your own role in the app runtime using `GrantROLENAMERole()` or `RevokeROLENAMERole()`, the changes take effect immediately.

* **Changes to other users' roles**: When you change another user's role using `GrantROLENAMERole(UserId)` or `RevokeROLENAMERole(UserId)` in the app runtime, or by applying changes in the ODC Portal or using the [User and Access Management API](../reference/apis/identity-v1.md), the changes take effect at different times:
    * In server-side logic, the updated role is available immediately.
    * In client-side logic, the updated role becomes available when the affected user's session token renews (every 5 minutes) or when they log in again.

<div class="info" markdown="1">

Logged-in users need to log out and log back in for changes in their assigned roles or role permissions to become effective.

</div>

### Restrict access to a screen

To allow only users with a certain role to access a screen in ODC Studio, you need to [create the role first](#create-end-user-roles). You can then allow only registered users to access screens in the app, which is a [best practice to protect your screens](../building-apps/ui/creating-screens/best-practices-screens.md#roles).

1. In the **Interface** > **Elements** tabs, select the screen.
1. From the screen properties, from the **Accessible by** dropdown, select **Authenticated users**. The **Authorization** section lists all roles set as **public** in the apps of your organization.
1. In the **Authorization** section, select the checkbox of at least one end-user role to grant access to the screen.

### Restrict logic flows

To restrict what a user can do in your app, verify their role on server-side logic. This is a [best practice to protect your app](../building-apps/logic/best-practices-logic.md#validate-permissions-server-side) against malicious users attempting to access or modify unauthorized data.

1. In ODC Studio, open the action where you want to restrict the logic.
1. Add an **If** element to the action flow.
1. In the **Condition** field of the **If** element, use `Check<ROLENAME>Role()`.

For example, set the condition to `CheckManagerRole()`. The logic of the **True** branch runs only if the current user has the Manager role.

### Restrict access to data

To verify that the user has a role in ODC Studio, use `Check<ROLENAME>Role()` in expressions.

For example, add a filter to an aggregate with `CheckManagerRole() = True`. The aggregate returns data only if the signed-in user has the Manager role, which is a [best practice to protect sensitive data](../building-apps/ui/creating-screens/best-practices-fetch-display-data.md#restrict-access).

## Related resources

* [Best practices for user management in ODC](best-practices-user-management.md)
* [Grant and revoke user roles](grant-and-revoke-user-roles.md#grant-roles-to-end-users)
* [Manage end-user groups](end-users/groups.md)
* [Create, activate, deactivate, and delete users](create-deactivate-and-delete-users.md)
* [Best practices for logic](../building-apps/logic/best-practices-logic.md)
* [Role-based Security](https://learn.outsystems.com/training/journeys/role-based-security-575) online course
