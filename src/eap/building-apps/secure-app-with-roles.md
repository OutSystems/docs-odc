---
summary: An overview of IT users and end-user roles in Project Neo.  
tags: user-management; authentication; lifecycle-management
locale: en-us
guid: BDA3A144-0EB0-4C04-953F-9DED85A477FE
app_type: mobile apps, reactive web apps
---

# Secure your app with end-user roles

<div class="info" markdown="1">

Project Neo documentation is under construction. It's frequently updated and expanded.

</div>

When you create a role, and assign it to a user, you can control access to screens, data and functionalities of your app. You can manage user roles from Service Studio and from the Project Neo Portal. In Service Studio, you design logic to control access.

When setting up roles for end-users, consider the following: 

* What do the end-users need to accomplish?
* What screens do they need to be able to access?
* What tasks do you want them to be able to do?
* What information can end users see and what needs to remain inaccessible?
 
## How to use roles

This is an overview of how to use roles:

1. In Service Studio, create end-user roles.
2. In Portal, assign end-user roles to users.
3. In Service Studio, use end-user roles to control access to the parts of the app. You can also grant and revoke a role to any user programmatically.

![How you can use roles](images/how-to-use-roles-diag.png "How you can use roles")

### Create end-user roles

Create roles in Service Studio, during design time. Go to the **Logic** tab > **Roles** > right-click the **Roles** folder > select **Add Role**. When Service Studio creates a role, it also creates a set of related actions you can use to manage roles during runtime.

### Assign roles to users through Portal

To assign roles to users, from Portal select **Users & Access** > **Users**. Search for a user and then from user properties, select **Manage permissions**. Then, set the permissions for the user for one or more **Apps** or **Stages**.

You can also assign roles at the same time you invite new users to your organization.

### Manage roles in app runtime

After you create a role, Service Studio also creates the following actions to let you manage the roles during the app runtime, in the app logic. These actions let you programmatically check, grant, or revoke a role.

| Action             | Example           | Description                                             |
| :------------------ | :----------------- | :------------------------------------------------------- |
| CheckROLENAMERole* | CheckManagerRole  | Returns True if the current user has the ROLENAME role. |
| GrantROLENAMERole  | GrantManagerRole  | Grants ROLENAME to the user with the UserId.            |
| RevokeROLENAMERole | RevokeManagerRole | Revokes ROLENAME from the user with the UserId.          |

**Notes**

(*) Available for both client and server logic. The light icon denotes the client-side version.

## Control access in your app with end-user roles

After you assign roles to your end-users, you can:

* Allow or block access to a screen
* Restrict access to data
* Restrict logic flows

![Control access in your app](images/control-access-in-your-app-end-user-roles-diag.png "Control access in your app")

<div class="warning" markdown="1">

Currently, users need to sign out and sign back in for the changes in role permission to become effective.

</div>

### Restrict access to a screen

To allow only users with a certain role to access a screen, you need to [create some roles first](#create-end-user-roles). You can then allow only registered users to access screens in the app.

1. Select the screen for which you want to edit the access.
1. From the screen properties, select **Authorization** > **Accessible by** and from the list select **Authenticated users**. The list of roles now shows in the **Authorization** section.
1. Select the roles users need to have to access the screen.

### Restrict logic flows

In Service Studio, in the logic of actions, use **CheckROLENAMERole()** function in the If element. You can do that by adding the If element to the logic flow, and then editing the **Condition** field.

For example, if you enter `CheckManagerRole()` in the **Condition** field of the If element, the logic of the true branch runs only if the current user has a Manager role.

### Restrict access to data

Use **CheckROLENAMERole()** function in expressions to verify that the user of the app has a role.

For example, you can create a filter in an aggregate with the expression `CheckAdminsRole() = True`. This aggregate now returns data only if the signed-in user has an Admin role.
