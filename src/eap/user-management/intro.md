---
summary: An overview of organization users and end-user roles in OutSystems Developer Cloud (ODC).
tags: user-management; authentication; lifecycle-management
locale: en-us
guid: 9e0fb9b7-d2b0-419f-a5d8-5b5ed730da5e
app_type: mobile apps, reactive web apps
---

# User management

User management in OutSystems Developer Cloud (ODC) is about setting up users so that they can develop, create, modify or access apps in your organization. A key part of user management is ensuring that the users have access to organization resources and apps in accordance with the access rules.

Before you begin, it's important that you understand these terms:

* **Organization user**. A technical user in ODC, such as an administrator or a developer, that belongs to an organization. These users can have permissions for tasks such as creating and managing users and apps, monitoring or troubleshooting apps.
* **End user**. A person who uses apps made with ODC. The level of access of these users to the app depends on the tasks they need to complete.
* **Organization role**. A set of permissions to control access within an organization.
* **End-user role**. A set of permissions to control access to an app and within an app.
* **Permission**. An authorization within a role to perform an action.

In ODC the **ODC Portal** is the central place to manage users. In the ODC Portal you can:

* Invite a new user
* Search for a user
* Turn on or off organization permissions
* Assign and revoke end-user roles

![User management](images/manage-users-in-portal-diag.png "User management")

## Add new users to your organization

From the **ODC Portal**, select **Users & Access** > **Users** > then click **Invite users**. Enter the email of the user, and then select:

* **Organization role**, if you want the user to be part of your organization as an administrator or developer.
* **End-user role**, if you want that the user has access to an app with an end-user role, deployed to a particular stage in your organization.

Users can have both organization and end-user roles.

New users must set up their password. The password must be at least 12 characters long, and contain at least:

* One upper case letter
* One lower case letter
* One numeric digit
* One special character from this set: `!` `\` `#` `$` `%` `&` `'` `(` `)` `*` `+` `,` `-` `.` `/` `:` `;` `<` `=` `>` `?` `@` `[`

## Organization roles

An organization role groups permissions that you can assign to users in your organization. With a role, permissions are applicable separately for each stage in the organization. To see the organization roles, go to **ODC Portal** > **Users & access** > **Organization roles**. Select a role to see the table of permissions. Hover the mouse pointer over the permissions in the table to reveal more information.

An organization role groups permissions in the following sections:

* App management
* Stage
* Deployment management
* Monitoring
* Configurations
* User management
* Forge

### Administrator and developer as built-in organization roles

The **Administrator** and **Developers** are the built-in organization roles in ODC. You can view these roles, assign them to users, but you cannot delete or modify them.

### Give or revoke organization role for a user

You can assign or revoke the organization role for a user. From the ODC Portal, select **Users & Access** > **Users**.

* For an existing user - search for a user, then under **Organization role** select **Manage role**. Select the organization role and save your changes. 
* For a new user - click **Invite user** and under **Organization role** select a role.

## End-user roles

End-user roles are specific to apps. You create end-user roles in ODC Studio while you develop an app. After you publish the app, you can then use ODC Portal to assign the end-user role to users. Go to **Users & Access** > **Users**. Search for the user, and in the user page under **End user roles** select **Manage roles**.

For more information see: [Secure your app with end-user roles](../building-apps/secure-app-with-roles.md).