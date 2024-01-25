---
summary: ODC provides pre-built screens and blocks for common authentication functionalities.
tags:
locale: en-us
guid: 49853077-9937-4865-8183-3f1f9ff224c2
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---
# Custom authentication flows

Most apps share certain common authentication functionalities that let end-users login, change password, recover password, or edit profile information. In OutSystems Developer Cloud (ODC), these functionalities come in pre-built screens that you can use and edit. These are available in the **UI Flows** > **Common** folder in the **Interface** tab in ODC Studio.

Screen name | Description
---|---
ChangePassword | Screen where users can change their current password.
InvalidPermissions | Screen where users will be redirected when they have invalid permissions.
Login | Screen where users login.
RecoverPasswordRequest | Screen where users can request a new password.
RecoverPasswordReset | Screen where users can set a new password for this app. Users should be redirected here from a password recovery request.
UserProfile | Screen where the users can see and edit the user profile.

For example, you may want to create a branded login screen by editing the pre-built Login screen.

Each screen is built on top of one or more system actions. You can find more information about these authentication and user system actions in the [reference documentation](../../reference/intro.md#system-actions).

## Blocks 
There are also pre-built blocks available to use and edit. You can use the them in pre-built screens or in screens you create. Like the pre-built screens, these are also available in the **UI Flows** > **Common** folder in the **Interface** tab in ODC Studio.

Block name | Description
---|---
UserInfo | Displays the currently logged in user and allows to log out. If no user is logged in, it links to the login screen.
PasswordPolicy | Block that verifies and informs the user on the status of the password's validation.
