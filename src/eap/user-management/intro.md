---
summary: An overview of organization users and end-user roles in OutSystems Developer Cloud (ODC).
tags: user-management; authentication; lifecycle-management; custom roles
locale: en-us
guid: 9e0fb9b7-d2b0-419f-a5d8-5b5ed730da5e
app_type: mobile apps, reactive web apps
---

# User management

User management in OutSystems Developer Cloud (ODC) is about setting up and providing access to a person who uses ODC. People are assigned **roles** such as administrator, developer, architect, or end user (also known as an app user).  A key part of user management is ensuring that users have the correct access to organization resources and apps in accordance with your access rules.

Users with organization roles can access the ODC Portal and use the ODC Studio to build apps. Users with end-user roles only have access to your apps.

All users are members of the Organization. To use ODC all users are assigned roles with different permissions.

The ODC Portal is the central place to manage users, and you can:

* Invite a new user
* Assign, revoke, or change roles for all users
* View and manage all users that have organization and end-user roles
  
![User management](images/manage-users-in-portal-diag.png "User management")

## Permissions

Permissions enable users to perform a task in the ODC Portal, ODC Studio, or an app.  Everything a user does in ODC is based on their role and the permissions given to that role. In ODC, only one user is created for each person. But, a single person can have different roles and types of access.

 When you assign a role to a person, they're automatically granted the permissions selected for that role. You can associate permissions to one or more stages (Development, QA, or Production) and apps. This helps to limit, for example, what a user can do in production.

ODC has **Organization** roles and **End user** roles to limit access. Organization roles are for users that need access to both the ODC Portal and ODC Studio. End user roles are for those users accessing the apps you create in ODC. You can assign built-in or custom roles at the organization or app levels.

You define permissions based on tasks you want to allow a user to perform. You then grant permissions to the roles and assign users to the roles. You can apply permissions to a specific app.

It's important that when you define permissions, you define them at the lowest level. Only give users access to what they must be able to do to complete a particular task. For  example, you might want a user to be able to view all apps, but only be able to make changes to a single app.

A single permission can belong to multiple roles. Some **permissions inherit other permissions** automatically. For example, if you grant a role in the Development stage such as the **Change Application** permission, that role automatically gets the **Debug and Deploy Application** permission. So, the person now has three permissions.

## Organization roles

An organization role groups a set of permissions that you can assign to users in your organization. You can apply these permissions to a stage, but you don't need to apply all permissions to a stage.

To see the organization roles, go to **ODC Portal** > **Users & access** > **Organization roles**. Select a role to see the table of permissions. Hover the mouse pointer over the permission in the table to display more information.

An organization role groups permissions in the following sections:

* App management
* Configurations
* Deployment management
* Forge
* Monitoring
* Stage
* User management

### Built-in organization roles

ODC comes with two built-in Organization roles: **Administrators** and **Developers**. Both roles can invite new users, but Developers can only grant access to applications (end-user roles) and only for the Development stage.

You can view these roles and assign them to users, but you can't **delete or modify** them. You can **duplicate** these roles. When you duplicate a built-in role, you make a copy of that role. ODC adds the word **copy** to the end of the current name (Developer-copy). You can't use the same name as the existing built-in role. You should give your new role a name that makes it easy to identify the permissions, such as **Developer-cloud**. Once you duplicate (copy) the role, you can make any modifications you want to the role.

### Custom organization roles

A custom organization role is any role that you create. You can create a brand new role, or you can duplicate an existing role and then make changes. At a minimum, you must give the role a new name and at least one permission. As soon as you add a role name and one permission, the **Create** button is available.

From the **Create role** screen, within each section, such as **Deployment Management** > **Deploy apps** select the stage (Development, QA, or Production) for which you want to enable the permission. You can always come back to this screen to make adjustments to the permissions.

## End-user roles

End-user roles are specific to apps. You create end-user roles in ODC Studio while you develop an app. After you publish the app, you use ODC Portal to assign the end-user role to users. Go to **Users & Access** > **Users**. Search for the user, and in the user page below End-user roles, select **Manage roles**.

For more information about app dev development and end-user roles, see: [Secure your app with end-user roles](../building-apps/secure-app-with-roles.md).

### Give or revoke a user role

You can assign or revoke a user's role. From the **ODC Portal**, select **Users & Access**> **Users**. A table displays all existing users. You can: 

* Sort the list by users, status, and last login date
* Manage the user's role by selecting the user
* Add a new user by clicking **Invite user**

When you assign or revoke a role to an authenticated user, it can take up to a minute for the change to become active.

## Add new users to your organization

You can add new users to your organization and apps through the ODC Portal.

From the **ODC Portal**, select **Users & Access**> **Users**, and then click the **Invite Users** button on the top right. A form displays to enter the user's email and select their access. Then based on your choices, different options become available.

* If you choose **Organization** role, then you select a role. Note that the list of roles is the list of roles you create.
* If you choose **end user**, you can assign roles related to a specific app or all apps, and all stages or a specific stage. You can choose more than one app at a time.

## Activate, deactivate, or delete users

To **activate** a user, you must first invite the user. Once a user accepts the invitation, you see them as active in the list of users.

To **deactivate** a user, from the **Actions** menu, select **Deactivate**. A confirmation message displays, click **Yes, deactivate user.** The user now displays as deactivated.

To **delete** a user, from the **Actions** menu, select **Delete user**. A confirmation message displays, click **Yes, delete user.** The user is deleted and their name is removed from the list of users.

## Passwords for users

New users must set up their own passwords. The password must be at least 12 characters long and contain at least:

* One lowercase letter
* One numeric digit
* One special character from this set: ! \ # $ % & ' ( ) * + , - . / : ; < = > ? @ [
* One upper-case letter

### Manage user passwords

Only users can manage their passwords. Users can update their passwords from the **ODC Portal** > **User dropdown** > **Update password**.

Users can also update a forgotten password  from the Login page, by clicking **Forgot password**.

<div class="info" markdown="1">

Admins don't have permission to change or reset a password.

</div>
