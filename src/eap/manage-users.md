---
summary: Introduction to user and life cycle management.  
tags: user-management; authentication; lifecycle-management
---

# Manage Users

OutSystems users are given permissions to perform tasks like creating and managing users, creating apps, and monitoring or troubleshooting applications.

Currently all users have the same permissions enabling access and use of all the available functionality. This means you can perform tasks that are usually restricted to only those with the proper permissions. For example, like adding users to your organization.

## Authentication

Authentication is the process of identifying and validating users who want access to OutSystems tool and apps. OutSystems uses keycloacks, a tool that allows single sign-on with identity and access management. Keycloacks verify that users have access to the apps and files they requesting by checking the database to verify what a particular user can access and maintain.

Users are associated with and authenticated against their organization account. When users authenticate, their credentials are verified. Once authenticated, users continue on their journey and if they switch apps, they don't need to re-authenticate.

## Benefits

The following are some benefits of using the OutSystems identity service:

* Information is stored in a centralized location
* Apps are more secure because the identify service  manages all background identity
* One user - one identity - one login streamlining the login process
* Onboarding new users is easier:
    * Users receive an email with login information
    * Users enter their personal information including their name, their email, and a password
  