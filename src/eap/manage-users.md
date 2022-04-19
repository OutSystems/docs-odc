---
summary: Introduction to user and life cycle management.  
tags: user-management; authentication; lifecycle-management
locale: en-us
guid: 9e0fb9b7-d2b0-419f-a5d8-5b5ed730da5e
app_type: mobile apps, reactive web apps
---

# Manage users

<div class="info" markdown="1">

Project Neo documentation is under construction. It's frequently updated and expanded. Leave your feedback and help us build the most useful content.

</div>

This article provides an overview of how users set their names and passwords, and how authentication works in OutSystems.

## Authentication

Authentication is the process of identifying and validating users who want access to OutSystems tools and apps.

Users are associated with and authenticated against the organization to which they're a member. When users provide username and password, their credentials are verified. Once authenticated, users can switch apps without needing reauthentication. In Project Neo, user management and authentication is ensured by the Identity Service.

OutSystems Identity Service:

* Stores information in a secure, centralized location
* Manages all background identity for accessing apps

Additionally, Identity Service facilitates onboarding by enabling new users to:

* Receive an email with login instructions
* Enter their personal information including their name, email, and a password
* Manage profiles
  
![User management](images/manage-users-diag.png "User management")

OutSystems users are given permissions to perform tasks such as creating and managing users, creating apps, and monitoring or troubleshooting applications.

<div class="warning" markdown="1">

Currently in the Project Neo Early Access Program, all users have the same permissions for enabling access and use of all the available functionalities. This means that all users can perform tasks that are usually restricted to a subset of admin users.

</div>

## IT users

Once logged in, IT users can:

* Access a list of available apps
* Create and change apps
* Deploy apps across stages
* [Configure apps](./configuration-management.md)
* View application logs
* View and manage all other IT users


## Deactivating users

For security purposes or if a user is on an extended leave, you might want to deactivate their account. When you deactivate a user, their permissions are suspended and they can't log into Service Studio or Portal.

To deactivate a user, check the options available from **Portal** > **Users & Access**.

## Password requirements

The password must be at least 12 characters long. Additionally, the password must contain at least:

* One upper case letter
* One lower case letter
* One numeric digit
* One special character from this set: `!` `\` `#` `$` `%` `&` `'` `(` `)` `*` `+` `,` `-` `.` `/` `:` `;` `<` `=` `>` `?` `@` `[`
