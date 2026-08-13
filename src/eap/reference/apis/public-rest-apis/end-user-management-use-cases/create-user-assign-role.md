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
  - Developer
tags: rest apis, user management, role assignment, automation, access control
outsystems-tools:
  - odc studio
helpids:
isautopublish: true
---
# Create a user and assign a role using REST APIs

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

      <div class="info" markdown="1">

      If you create the user using the API and want the user to set a password and finish the registration process, use the reset password flow. Call [**StartResetPassword**](../../../system-actions/user.md#startresetpassword) to send the verification code email, then call [**FinishResetPassword**](../../../system-actions/user.md#finishresetpassword) with the verification code and the new password.

      For more information about resetting passwords, refer to [Passwords](../../../../user-management/passwords.md).

      </div>

1. If you have multiple apps with similar role names, get the `assetKey` (the key of your app):

   `GET /assets`

      Filter by `nameContains` to find your app.

      On successful execution of the API, the response contains the **asset key (UUID)** of each app in the `key` field. Use the asset key that matches your app.

      For details, refer to the [Asset Repository API reference](../../asset-v1.md).

1. To get the application role key for a specific role, use:

   `GET /application-roles`

      And filter by `nameContains` to get the application role key for a specified role name.

      If you have multiple apps with similar role names, also filter by `assetKey` (the key of your app).

      This application role key, along with the user key, is used in the next step to grant an application role to the user.

1. To grant an application role to the user, use:  

   `POST /users/{key}/application-roles/{roleKey}`

      Pass the user key and the application role key obtained from the previous steps.

    On successful execution of the API,  the specified application role is assigned to the newly created user, and the user's access permissions now include those granted by the assigned role.

## Related resources

* [User and Access Management API reference](../../identity-v1.md)

* [User management in ODC](../../../../user-management/intro.md)
