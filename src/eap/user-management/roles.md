---
helpids: 30493
summary: OutSystems Developer Cloud (ODC) features organization and end-user roles to manage access and permissions within its development environment.
locale: en-us
guid: 766ab743-31f2-4f58-ad91-a4cd0db8ab93
app_type: mobile apps, reactive web apps
figma:
platform-version: odc
---

# Roles

ODC has organization roles and end-user roles which you can use to limit access. Organization roles are for Organization members who perform work as developers or admins.

* Organization roles are for users that need access to both the ODC Portal and ODC Studio. You can assign built-in or custom roles at the organization or app levels.

<div class="info" markdown="1">

It's currently only possible to assign a maximum of 10 app scope roles to each user.

</div>

* End-user roles are for those users that access apps you create in ODC.

## Organization roles

An organization role groups a set of permissions that you can assign to members in your organization. You can apply these permissions to a stage, but you don't need to apply all permissions to a stage.

To see the organization roles:

1. From **ODC Portal** select **Users & access** > **Organization roles**.
1. Select a role to see the table of permissions.
1. Hover the mouse pointer over the permission in the table to display more information.

An organization role groups permissions in the following sections:

* App management
* Configurations
* Deployment management
* Forge
* Monitoring
* Stage
* User management

<div class="info" markdown="1">

If you assign an organization role to a user who currently has only end-user role(s), the user will transition to the **Invited** status and receive an email to complete the organization onboarding. The user's end-user access is not impacted.

</div>

### Built-in organization roles

ODC comes with two built-in organization roles: **Administrators** and **Developers**. Both roles can invite new users, but Developers can only grant access to applications (end-user roles) and only for the Development stage.

You can view these roles and assign them to users, but you can't **delete or modify** them. You can **duplicate** these roles. When you duplicate a built-in role, you make a copy of that role. ODC adds the word **copy** to the end of the current name (Developer-copy). You can't use the same name as the existing built-in role. You should give your new role a descriptive name, such as **Developer-cloud**. Once you duplicate (copy) the role, you can make any modifications you want to the role.

### Custom organization roles

A custom organization role is any role that you create. You can create a new role, or you can duplicate an existing role and then make changes. At a minimum, you must give the role a new name and at least one permission. As soon as you add a role name and one permission, the **Create** button is available.

From the **Create role** screen, within each section, such as **Deployment Management** > **Deploy apps** select the stage such as Development or QA for which you want to enable the permission. You can always come back to this screen to adjust the permissions.

## Organization access with app scope

Organization access is required for users to access the ODC Portal and to the ODC Studio to build apps.

To define what users are able to do, ODC uses Organization scope and App scope. Organization scope provides broad access, while App scope pertains to a particular app. As users begin working you might want to limit their access and then provide them with more access as needed. For example, for the Organization scope you might give an Organization member the Developer role or a custom role that you defined. Then if the Developer needs access to an app, they request additional access for a specific app.

Using Apps scope you can give developers Admin access to the specific App so they can complete their work.

Using different roles with different permissions and different access enables you to provide additional access to apps. Using App scope streamlines and enhances access while ensuring people have access to what they need and don’t have access to everything.

You can change the Organization scope role, using the scope dropdown. The default roles for the Organization scope is No role, Administrator, or Developer. You can also create custom roles for your Organization scope.

In the App scope section, you can Manage roles. You can add or delete App scope roles. This enables you to select the app and the role you want to give to an Organization member.

## End-user roles

End-user roles are specific to apps. You create end-user roles in ODC Studio while you develop an app. After you publish the app, you use the ODC Portal to assign the end-user role to users. Go to **Users & access** > **Users**. Search for the user, and in the user page below End-user roles, select **Manage roles**.

For more information about app dev development and end-user roles, see: [Secure your app with end-user roles](secure-app-with-roles.md).

## End-user groups

To accelerate the onboarding of users, ODC enables you to create groups of users. Using groups enables you to grant users roles in bulk. Before you can add users to groups, users must be part of your ODC organization.

Manage the groups from the ODC **Portal** > **Users & access** > **End-user groups**. When adding a new group, enter a group name. The group name is required, all other fields are optional.

You can add roles to a group before or after you add users to a group. Users in the group get all end-user roles associated with that group. Users can belong to multiple groups. You can create a new group in a different stage, with the same name or a different name, and use the same or similar roles.

You must select a stage to which the group belongs. Once you select a stage for the group and save it, you can't change the stage. The organization group members can only access the end-user roles and apps in the selected stage.

A person with **Manage end-user groups** permission can add users to a group, select users from a list of existing users and add them to the group. Once you save the group, it's available immediately. Adding or removing roles also takes effect immediately.

## Add new users or end-user groups to your organization

You can add new users to your organization and apps through the ODC Portal.

From the **ODC Portal**, select **Users & access** and then select either **Users** or **End-user groups**.

Clicking **Users**, displays a screen that shows a list of users. To invite a new user, from the top right click the **Invite user** button. A form displays to enter the user's email address and to select their access. Based on your choices, different options are available.

* If you choose **Organization access**, you can select an organization and an app. If you select an organization, then you can choose a specific role or no role. When you search for or select a group, you can also choose a stage.
* If you choose **End-user access** you also have access to add **End-user groups**. You can add the user to a group, assign roles related to a specific app or all apps, and a specific stage or all stages. You can choose more than one app at a time. A group can only have roles from the same stage. For example, if your group is in the Development stage you can't add roles from the Production stage.

<div class="info" markdown="1">

When a user signs into an app, their user profile information is synchronized to the [User entity](../reference/system-actions/user.md#user-1) of that app.

</div>

 Clicking **End-user groups**, displays a screen that shows the groups available. To create a new group, from the top right, click the **Create group** button. A dropdown arrow lets you choose the stage in which you want to create the group. Then enter a group name and a description. At the same time you can select one or more apps.

## Activate, deactivate, or delete users

Manage the users in the **ODC Portal** > **Users**.

To **activate** a user, you must first invite the user. Once a user accepts the invitation, you see them as active in the list of users.

To **deactivate** a user, from the Actions menu, select **Deactivate**. A confirmation message displays, click **Yes, deactivate user.** The user now displays as deactivated.

To **delete** a user, from the Actions menu, select **Delete user**. A confirmation message displays, click **Yes, delete user.** The user is deleted and their name is removed from the list of users.

## Give or revoke a user role

You can assign or revoke a user's role. This applies to individual roles and group roles.

From the **ODC Portal**, select **Users & access**> **Users**. A table displays all existing users. You can:

* Sort the list by users, status, and last login date
* Manage the user's role by selecting the user
* Add a new user by clicking **Invite user**

<div class="info" markdown="1">

Logged-in users needs to log out and log back in for changes in their assigned roles or role permissions to become effective.

</div>
