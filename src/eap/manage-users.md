---
summary: Introduction to user and life cycle management.  
tags: user-management; authentication; lifecycle-management
---

# Manage Users

OutSystems users are given permissions so that they can perform tasks such as to create and manage users and to monitor and troubleshoot applications.

Currently all users have the same permissions enabling access and use of all the available functionality. This means you can perform tasks that are usually restricted to only those with the proper permissions. For example, adding users to your organization.

## Authentication

Authentication is the process of identifying and validating users who want to access OutSystems. To secure your apps OutSystems uses keyCloacks. Keycloaks are a tool that makes securing your applications easier and provides the correct access to a user.  We can identify users in environments, apps, and tools.

Users are associated with and authenticated against their organization account. When users authenticate, their credentials are verified. UOnce authenticated, users continue on their journey and if they switch apps, they don't need to re-authenticate.

### Benefits

The following are some benefits of using the OutSystems identity service:

* Information is stored in a centralized location
* More secure because it manages all background identity
* One user - one identity - one login streamlining the log in process
* Onboarding new users is easier:
    * Send the user an email with login information
    * Users enter their personal information including their name, their email, and a password
  