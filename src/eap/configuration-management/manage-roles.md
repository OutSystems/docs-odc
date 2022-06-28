---
summary: An overview of IT users and end-user roles in Project Neo.  
tags: user-management; authentication; lifecycle-management
locale: en-us
guid: BDA3A144-0EB0-4C04-953F-9DED85A477FE
app_type: mobile apps, reactive web apps
---

# Manage roles

<div class="info" markdown="1">

Project Neo documentation is under construction. It's frequently updated and expanded.

</div>

A role defines a set of tasks that someone can perform. When you create a role, and assign it to a user, you control access to screens and operations of your app. You manage user roles from Service Studio and from the Project Neo Portal. 
 
**How to use roles:**

1. In Service Studio, create end-user roles.
2. In the Portal, assign end-user roles to users.
3. In Service Studio, use end-user roles to control access.

![How you can use roles](images/use-roles-diag.png "How you can use roles")

<div class="info" markdown="1">

Functions to add and revoke user roles are currently available only in the Portal.

</div>

## Create end-user roles

You can create roles in Service Studio, during design time. From the **Logic** tab select **Roles**, then right-click the **Roles** folder, and select **Add Role**.

When setting up roles for end users, consider the following: 

* What do the end users need to accomplish?
* What screens do they need to be able to access?
* What tasks do you want them to be able to do?
* What information can end users see and what needs to remain inaccessible?

### Assign roles to users

To assign roles to users, from the Portal select **Users & Access** > **Users**. Search for a user and then from user properties, click **Manage permissions**.  Then, set the permissions for the user by one or more **Apps** or **Stages**.

You can also assign roles at the same time you invite new users to your organization.

<div class="warning" markdown="1">

Currently, users need to sign out and sign back in for the changes in role permission to become effective.

</div>

## Control access in your app with end-user roles

After you assign roles to your end-users, you can:

* Allow or block access to a screen
* Restrict access to data
* Restrict logic flows

![Control access in your app](images/control-access-in-your-app-diag.png "Control access in your app")

<div class="warning" markdown="1">

Currently, users need to sign out and sign back in for the changes in role permission to become effective.

</div>

### Restrict access to a screen

To allow only users with a certain role to access a screen, you need to [create some roles first](#create-end-user-roles).

1. Select the screen for which you want to edit the access.
1. From the screen properties, select **Authorization** > **Accessible by** and from the list select **Authenticated users**. The list of roles now shows in the **Authorization** section.
1. Select the roles users need to have to access the screen.

### Restrict logic flows

In the logic of server actions, use **CheckROLENAMERole()** function in the condition of the If element of the flow. The function **CheckROLENAMERole()** is available in the server actions only.

#### Restrict access to data

Use **CheckROLENAMERole()** function in expressions to verify that the user of the app has a role. For example, you can create a filter in an aggregate with the expression `CheckAdminsRole() = True`. The aggregate now returns data if the signed-in user has an "Admin" role.
