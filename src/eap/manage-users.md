---
summary: Introduction to user and life cycle management.  
tags: user-management; authentication; lifecycle-management
---

# Manage users

<div class="info" markdown="1">

Project Neo documentation is under construction. It's frequently updated and expanded. Leave your feedback and help us build the most useful content.

</div>

This article provides an overview of how users set their names and passwords, and how authentication works in OutSystems.

OutSystems identity service:

* Stores information in a centralized location
* Manages all background identity for accessing apps
* Makes the login process more effective

Additionally, identity service facilitates onboarding by enabling new users to:

* Receive an email with login instructions
* Enter their personal information including their name, email, and a password
* Manage profiles
  
![OutSystems Identity Service](images/manage-users-identy-service.png)

OutSystems users are given permissions to perform tasks such as creating and managing users, creating apps, and monitoring or troubleshooting applications.

<div class="warning" markdown="1">

Currently in the Project Neo Early Access Program, all users have the same permissions for enabling access and use of all the available functionalities. This means that all users can perform tasks that are usually restricted to a subset of admin users.

</div>

## Organization (Technical) user

Once an Organization user logs into the portal, they can:

* Access all developer or administrative users
* Invite other users (via email) to complete their profile
* Sign into the portal and see a list of available apps
* Access a list of available apps

<div class="info" markdown="1">

You can't change a username if that username is an email address.

</div>

## Deactivating users

For security purposes or if a user is on an extended leave, you might want to deactivate their account. When you deactivate a user, Project Neo blocks them from signing in to the portal and suspends their permissions.

To deactivate a user, check the options available from **Portal** > **Users & Access**.

## Password requirements

The password must be at least 10 characters long. Additionally, the password must contain at least:

* One upper case letter
* One lower case letter
* One numeric digit
* One special character from this set ("!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", ")

## Authentication

Authentication is the process of identifying and validating users who want access to OutSystems tools and apps. OutSystems uses Keycloak, an open source identity and access management solution, to authenticate users.

Users are associated with and authenticated against the organization to which they're a member. When users provide username and password, their credentials are verified. Once authenticated, users can switch apps without needing reauthentication.
