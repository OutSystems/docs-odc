---
summary: Learn about managing and inviting users to your organization in OutSystems Developer Cloud (ODC).
tags: user-management; authentication; lifecycle-management; permissions; custom roles
locale: en-us
guid: 9e0fb9b7-d2b0-419f-a5d8-5b5ed730da5e
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/KpEoUxciqaFLGLlZxo7Hiu/User-management?type=design&node-id=2449%3A32709&t=qXDLlqyCzAMXQgr0-1
platform-version: odc
---

# User management

User management in OutSystems Developer Cloud (ODC) is about setting up and providing access to a person who uses ODC. You assign **roles** to people, such as administrator, developer, architect, or end-user. A key part of user management is ensuring that users have the correct access to organization resources and apps in accordance with your access rules.

In this document, the term organization refers to the ODC account your company manages. All users are part of an organization. To use ODC, all users have roles with different permissions.

Users also known as Members have organization roles and can access the ODC Portal and use ODC Studio to build, manage, and deploy apps. Users with end-user roles only have access to your apps.

You can create groups of end-users. All end-users in the group have access to the same roles and apps. For example, you might create a group of end-users from the marketing team who need different access than a group of end-users from the finance team.

ODC enables you to use groups to accelerate giving users roles and access to apps. You can only add end-users to groups. Your ODC admin creates the group and adds end-users to the group. You associate groups and apps to roles. You can also invite users to a group which gives them access to all apps associated with the group.

Roles and permissions work together to define what members and end-users can do in ODC. You can create only one user for each email address. An individual can have different roles and types of access.

When you assign a role to a user, that user is automatically granted the permissions selected for that role. ODC has different permissions such as global, stage, or app to be more granular. This granularity helps to further limit access.

You define permissions based on tasks you want to allow a user to perform. You then grant permissions to the roles and assign users to the roles. You can apply permissions to a specific app.

When you define permissions, you should define them at the lowest level. Only give users access to what they must be able to do to complete a particular task. For example, you might want a user to be able to view all apps but only be able to make changes to a single app.

A single permission can belong to multiple roles. Some **permissions inherit other permissions** automatically. For example, if you grant a role in the Development stage, such as the **Change Application** permission, that role automatically gets the **Debug and Deploy Application** permission. So, the person now has three permissions.

The ODC Portal is the place to manage users, and you can:

* Invite a new user and also invite the user to a group
* Assign, revoke, or changes roles for all users
* View and manage all users that have organization and end-user roles
* Create a group
* Add or remove users from the group
* Add or remove roles associated with a group
* View all existing groups and users in a group
* View all roles and apps associated with the group


![User management](images/manage-users-in-portal-diag.png "User management")
