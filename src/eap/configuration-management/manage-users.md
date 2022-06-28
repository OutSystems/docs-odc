---
summary: An overview of IT users and end-user roles in Project Neo.  
tags: user-management; authentication; lifecycle-management
locale: en-us
guid: 9e0fb9b7-d2b0-419f-a5d8-5b5ed730da5e
app_type: mobile apps, reactive web apps
---

# User management

<div class="info" markdown="1">

Project Neo documentation is under construction. It's frequently updated and expanded.

</div>

User management is about setting up users so that they can develop, create, modify or access your apps. A key part of user management is ensuring the access a user has to the app adheres to security rules.

Before you begin, it's important that you understand these terms:

* **User**. A person who belongs to an organization and has access to the OutSystems platform and/or its assets. For example, organization (IT) user or end (app) user. 
* **IT user** or **organization user**. A technical user of OutSystems tools, such as an administrator or a developer, that belongs to an organization. The IT users have permissions for tasks such as creating and managing users and apps, monitoring or troubleshooting apps. Developers are commonly IT users in an organization.
* **End user** or **app user**. A person who uses the apps made with OutSystems tools. Their level of access to the app depends on the tasks they need to complete.
* **Role** or **end-user role**. A set of permissions designed and applied to a user to control access to an app and within an app.

<div class="warning" markdown="1">

Currently in Project Neo Early all **IT users** have admin permissions.

</div>

The **Project Neo Portal** is the central place to manage users. In Portal you can:

* Invite a new user
* Search for a user
* Turn on or off organization permissions
* Assign and revoke end-user roles

![User management](images/manage-users-diag.png "User management")

The following features aren't currently available:

* Change password
* Deactivate user
* Delete user

## Add new users to your organization

<div class="info" markdown="1">

You send an email invitation to invite users to be part of your organization and then you can assign roles to them. To save time, you can add roles to users as part of the invitation.

</div>

From the Portal, select **Users & Access** > **Users** > then click **Invite users**. The user receives an invitation email to join the organization. New users must set up their password. The password must be at least 12 characters long, and contain at least:

* One upper case letter
* One lower case letter
* One numeric digit
* One special character from this set: `!` `\` `#` `$` `%` `&` `'` `(` `)` `*` `+` `,` `-` `.` `/` `:` `;` `<` `=` `>` `?` `@` `[`

## Give or revoke admin permissions

You can assign or revoke OutSystems admin permissions. From the Portal, select **Users & Access** > **Users**.

* For an existing user - search for a user, and from the **Organization permissions** section, toggle **OutSystems administrator**.  
* For a new user - click **Invite user** and select  **OutSystems administrator**.

IT users with the OutSystems administrator permission can:

* Access a list of available apps
* Assign users to roles such as organization or end-user roles
* Create and change apps
* Deploy apps across stages
* [Configure apps](./configuration-management.md)
* View application logs
* View and manage all other IT and end users