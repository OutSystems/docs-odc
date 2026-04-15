---
guid: 5d10b0f6-098b-4275-b7e2-8acf88e9f016
locale: en-us
summary: This use cases guides you how to create a single user and assign a role to it using ODC User and Access management REST APIs.
figma:
coverage-type:
  - apply
topic:
  - role-assignment
  - creating-users
  - create-app-role
  - app-roles
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - backend developers
  - full stack developers
  - mobile developers
tags: rest apis, user management, role assignment, automation, access control
outsystems-tools:
  - odc studio
helpids:
---
# Creating a single user and assigning a role

This use case outlines the steps to programmatically create a [new user](../../../../user-management/intro.md) and then assign a specific application role to that user in ODC Studio using ODC REST APIs. This is useful for automating user provisioning and access control.

## Prerequisites

Before using the APIs to create a user and assign a role, ensure that you have:

* [Generated access token](../authentication/get-access-token.md) with the necessary permissions.  

* The name of the application role to be assigned to the user.

## Create a single user and assign a role

To create a single user and assign a role to the user using ODC REST API, follow these steps:

1. To create a new user, use:

   `POST /users`

      Pass the user’s email address. Optionally, provide the user's name, photo URL, and active status. Additionally, indicate if you want to add the user to the built-in provider in the request body.  

      On successful execution of the API, a new user is created, and the API response contains the newly created **user's key (UUID)**. This key is used in the subsequent steps.  

1. To get the application role key for a specific role, use:

   `GET  /application-roles`

      And filter by `nameContains` to get the application role key for a specified role name.

      This application role key, along with the user key, is used in the next step to grant an application role to the user.

1. To grant an application role to the user, use:  

   `POST /users/{key}/application-roles/{roleKey}`

      Pass the user key and the application role key obtained from the previous steps.

    On successful execution of the API,  the specified application role is assigned to the newly created user, and the user's access permissions now include those granted by the assigned role.

## Related resources

* [User and Access Management API reference](../../identity-v1.md)

* [User management in ODC](../../../../user-management/intro.md)
