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

When you create a role and assign it to a user, you can control access to screens, data, and functionalities of your app. You can manage user roles from ODC (OutSystems Developer Cloud) Studio and from the ODC Portal. In ODC Studio, you design logic to control access.

When setting up roles for end-users, consider the following:

* What do the end-users need to accomplish?
* What screens do they need to access?
* What tasks do you want them to be able to do?
* What information can end-users see, and what needs to remain inaccessible?

## How to use roles

This is an overview of how to use roles:

1. In ODC Studio, create end-user roles.
1. In the ODC Portal, assign end-user roles to users.
1. In ODC Studio, use end-user roles to control access to the parts of the app. You can also grant and revoke a role to any user programmatically.

![Diagram illustrating the process of using roles in OutSystems Developer Cloud](images/overview-how-to-use-roles-diag.png "How you can use roles")

You can also use the ODC [User management REST APIs](../reference/apis/identity-v1.md) for programmatically managing the user and access related operations. For detailed information about how to use these APIs, refer to [Getting started](../reference/apis/public-rest-apis/getting-started.md).

### Create end-user roles { #create-end-user-roles }

To create roles in ODC Studio during design, follow these steps:

1. Go to the **Logic** tab > **Roles** > right-click the **Roles** folder > select **Add Role**.

1. Enter **Name**, **Description**.

1. Select **Yes** from **Public** drop-down to set the role as Public. The default value is No.

When ODC Studio creates a role, it also creates a set of related actions you can use to [manage roles](#manage-roles-in-app-runtime) during runtime.

### Assign end-user roles to users

After you publish an app that has end-user roles, the end-user roles are available in ODC Portal. For more details on how to assign end-user roles, refer to [Grant or revoke roles to end-users](grant-and-revoke-user-roles.md#grant-roles-to-end-users).

### Use end-user roles to control access in app runtime

After you create an end-user role, ODC Studio also creates the following actions that enable you to manage the end-user roles in the app logic. These actions let you programmatically check, grant, or revoke a role. The actions apply to the currently logged-in user if the UserId parameter is not specified.

|                        |                                      |                   |                                                         |
| ---------------------- | ------------------------------------ | ----------------- | ------------------------------------------------------- |
| **Action**             | **Client-side or Server-side logic** | **Example**       | **Description**                                         |
| CheckROLENAMERole (\*) | Client-side logic                    | CheckManagerRole  | Returns True if the current user has the ROLENAME role. |
| CheckROLENAMERole      | Server-side logic                    | CheckManagerRole  | Returns True if the current user has the ROLENAME role. |
| GrantROLENAMERole      | Server-side logic                    | GrantManagerRole  | Grants ROLENAME to the user with the UserId.            |
| RevokeROLENAMERole     | Server-side logic                    | RevokeManagerRole | Revokes ROLENAME from the user with the UserId.         |

**Note:** (*) The light icon denotes the client-side version.

## Control access in your app with end-user roles { #control-access-in-your-app-with-end-user-roles }

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

### Restrict access to a screen

To allow only users with a certain role to access a screen, you need to [create some roles first](#create-end-user-roles). You can then allow only registered users to access screens in the app, which is a [best practice to protect your screens](../building-apps/ui/creating-screens/best-practices-screens.md#roles).

1. Select the screen for which you want to edit the access.

1. From the screen properties, select **Authorization** > **Accessible by** and from the list select **Authenticated users**. The list of roles from all apps under the Organization where the roles are set as public shows in the **Authorization** section.

1. Select at least one user role from the list to give access to the screen.

### Restrict logic flows

In ODC Studio, in the logic of actions, use **CheckROLENAMERole()** function in the If element. You can do that by adding the If element to the logic flow, and then editing the **Condition** field.

For example, if you enter `CheckManagerRole()` in the **Condition** field of the If element, the logic of the true branch runs only if the current user has a Manager role.

<div class="info" markdown="1">

Always validate user permissions on server-side logic. This is a [best practice](../building-apps/logic/best-practices-logic.md) to protect against malicious users attempting to access or modify unauthorized data.

</div>

### Restrict access to data

Use **CheckROLENAMERole()** function in expressions to verify that the user of the app has a role.

For example, you can create a filter in an aggregate with the expression `CheckAdminsRole() = True`. This aggregate now returns data only if the signed-in user has the Admin role, which is a [best practice to protect sensitive data](../building-apps/ui/creating-screens/best-practices-fetch-display-data.md#restrict-access).

## Related resources

* [Best practices for user governance](best-practices-user-management.md)

* [Create, activate, deactivate, and delete users](create-deactivate-and-delete-users.md)

* [Best practices for logic](../building-apps/logic/best-practices-logic.md)

* [Role-based Security](https://learn.outsystems.com/training/journeys/role-based-security-575) online course
