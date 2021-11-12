---
summary: Introduction to user and life cycle management.  
tags: user-management; authentication; lifecycle-management
---

# Manage Users

OutSystems users are given permissions so that they can perform tasks such as to create and manage users and to monitor and troubleshoot applications.

Currently all users have the same permissions enabling you to access and use all the available functionality. This means you can perform tasks that are usually restricted to only those with the proper permissions. For example, you can add users to your organization.

## Authentication

OutSystems knows who you are through your identity. Identities are unique and enable us to identify a user in OutSystems.  We can identify users in environments, apps, and tools. In addition, by using your identity, you no longer need to re-authenticate while using the same account.

Users are associated with an organization account. When users authenticate, their credentials are verified. The OutSystems identity service authenticates users against the Organization account to which they are associated. Once authenticated, users continue on their journey.

### Benefits

he following are some benefits of using the OutSystems identity service:

* Information is stored in a centralized location
* More secure because it manages all background identity
* One user - one identity - one login streamlining the log in process
* Onboarding new users is easier:
    * Send the user an email with login information
    * Users enter their personal information including their name, their email, and a password
  