---
summary: Introduction to user and life cycle management.  
tags: user-management; permissions; consoles; authentication; lifecycle-management
---

# Manage Users

OutSystems users are given permissions so that they can perform tasks such as to create and manage users and to monitor and troubleshoot applications.

For the public EAP (Early Access Program) all users have the same permissions enabling you to access and use all the available functionality. This means you can perform tasks that are usually restricted to only those with the proper permissions.
This document describes some of the improvements OutSystems made to improve your users journey.

## Consoles

For the public EAP all users have access to all the consoles. Users access the different consoles through links on the side navigation bar. The data and functionality you see is for all your applications and environments,  You can now manage and monitor users, apps, and environments in one location. For this EAP, you have access to only the User Management and Monitoring consoles.  

### Monitoring console

 The Monitoring Console provides a unified experience where you can monitor the health of all your applications. And then, from the same console you can identify any unexpected behaviors before they become issues that impact the performance of your systems or apps.

The goal of the Monitoring console is to reduce the effort it takes for you to:

* Detect app problems such as performance and unavailability.
* Understand what’s causing the anomaly in your application such as a configuration problem.

Using the Monitoring console makes it easier and quicker for you to locate and fix the issues. You can use the Monitoring Console during all stages of development to monitor and troubleshoot applications. You can also access capabilities to check for application governance, user management, and performance.

For the EAP release, the following log files  are available:

* **General Log** - shows the timestamp, app name, app key, message, and source
* **Error Log** - shows the timestamp, app name, app key, message, source, and error key
* **Integration Log** - shows the timestamp, app name, app key, type, source, action, endpoint, duration, log key/ID, and the error key/ID

A detail button to the right of each log entry, provides additional information.

## Permission model

Although not yet available, OutSystems new permissions model is easy to learn and use, and it comes with enhanced security features. For each stage, you define the following for users:

* what they can and can’t do in the applications
* What apps they can see and what access rights a user has
* What features they can access
* What tools they can use

It is important to note that, for each stage, you can define different permissions.

The permission model enables you to:

* Create complex structures quickly
* Define and use your own permission models

## Authentication

<divclass="info" markdown="1">
During EAP, only IT User accounts are being used.
</div>

OutSystems knows who you are through your identity. Identities are unique and enable us to identify a user in OutSystems.  We can identify users in environments, apps,and tools.  In addition, by using your identity, you no longer need to re-authenticate while using the same account.

Users are associated with an organization account. When users authenticate, their credentials are verified.  The OutSystems identity service authenticates users to the Organization account to which they are associated. Once authenticated, users continue on their journey.

### Benefits

he following are some benefits of using the OutSystems identity service:

* Information is stored in a centralized location
* More secure because it manages all background identify
* Single sign-on (SSO) works on different stages
* One user - one identity - one login
  * You can be an IT user on one system and an end user on another.
* Onboarding new users is easier
  * Send the user an email  with login information
  * Users enter their personal information including their name, their email, and a password
  * Users are able to access all the systems in different environments (stages) and different apps in different stages
  
In a later release, you will be able to configure 3rd party identity providers.
