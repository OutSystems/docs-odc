---
summary: Learn password management and recovery protocols for OutSystems Developer Cloud (ODC), including creation, changes, and lockout procedures.
locale: en-us
guid: 41b86768-295e-4aeb-98ed-9a0f6db4cfd2
app_type: mobile apps, reactive web apps
figma:
platform-version: odc
tags: password management, security protocols, authentication, user management, account lockout
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - odc portal
coverage-type:
  - remember
---

# Passwords

New users must set up their own passwords. The password must be at least 12 characters long and contain at least:

* One numeric digit
* One character from this set: !, \, #, $, %, &, ', (, ), *, +, ,, -, ., /, :, ;, <, =, >, ?, @, [
* One upper-case letter

<div class="info" markdown="1">

Only users can manage their passwords. Admins don't have permission to change or recover other users' passwords.

</div>

Organization members with an organization role, such as Developer or Administrator, can change their password using the **ODC Portal** > **User dropdown** > **Change password**, or recover their password by clicking **Forgot password?** on the ODC Portal login page.

If you're not receiving the password reset email, please check your spam folder and any filters. The emails are sent from `noreply@outsystems.dev`.

To enable your apps' end users to change and recover their passwords, you must provide them with authentication functionalities. You can build these functionalities in your app using ODC pre-built user screens. For more information, see [Custom authentication flows](../building-apps/ui/custom-auth.md).

ODC temporarily locks users out after five consecutive failed sign-in or password change attempts. The lockout duration increases with each additional failed attempt, starting at just a few seconds and reaching a maximum of approximately 15 minutes. After the lockout period passes, your user information returns to the initial state.

## Password reset

ODC provides pre-built screens that allow end users to request a new password (RecoverPasswordRequest) and set a new password (RecoverPasswordReset) for their app. For detailed information, refer to [Custom authentication flows](../building-apps/ui/custom-auth.md).

The password reset in ODC is authenticated via a verification code received in an email. 

Here’s the high-level overview of the password reset mechanism in ODC:

1. To receive the verification code, the end-user enters the email address in **RecoverPasswordRequest** screen.

1. The **RecoverPasswordRequest** screen invokes the system server action **StartResetPassword,** which sends the verification code to the end user's email address.

1. The user receives the verification code and a link to the **RecoverPasswordReset** page in the email. 

1. The user opens the  **RecoverPasswordReset** page and enters the new secure password. 

1. The **RecoverPasswordReset** page invokes the system client action **FinishResetPassword**, and sets the email, verification code, and new password for the end user in the Identity server. 
