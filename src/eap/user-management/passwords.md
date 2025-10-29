---
summary: Learn password management and recovery protocols for OutSystems Developer Cloud (ODC), including creation, changes, and lockout procedures.
locale: en-us
guid: 41b86768-295e-4aeb-98ed-9a0f6db4cfd2
app_type: mobile apps,reactive web apps
figma: 
platform-version: odc
tags: password management,security protocols,authentication,user management,account lockout
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - odc portal
coverage-type:
  - remember
  - unblock
  - understand
  - evaluate
  - apply
topic:
  - passwords
  - lockout
helpids: 
---

# Passwords

New users must set up their own passwords. Passwords must be at least 12 characters long and include at least:

* One numeric digit
* One upper-case letter
* One special character from this set: `! \ # $ % & ' ( ) * + , - . / : ; < = > ? @ [`

<div class="info" markdown="1">

Only users can manage their own passwords. Admins can't change or recover passwords on behalf of other users.

</div>

## Lockout policy

ODC temporarily locks users out after five consecutive failed sign-in or password change attempts. The lockout duration increases with each additional failed attempt, starting at just a few seconds and reaching a maximum of approximately 5 minutes. After the lockout period passes, your user information returns to the initial state.

## Password reset for members (IT-users) { #password-reset-members }

[Members](intro.md#members-it-users) can recover their password by clicking **Forgot password?** in the ODC Portal login page.

## Password reset for end-users

<div class="info" markdown="1">

Members that are also end-users must recover their password by following the instruction in [Password reset for members (IT-users)](#password-reset-members). Following the instructions in this section won't work for members that also have application roles.

</div>

To allow your app’s [end-users](intro.md#end-users) to change or recover their password, you need to implement [custom authentication flows](../building-apps/ui/custom-auth.md) in your app. You can do this using the following ODC’s pre-built user screens:

* **RecoverPasswordRequest**, for requesting a password reset
* **RecoverPasswordReset**, for setting a new password

In these screens ODC implements a flow to authenticate password resets with a verification code sent by email. Here’s how the process works:

1. To receive the verification code, end-users enter their email on the **RecoverPasswordRequest** screen.
1. The **RecoverPasswordRequest** screen calls the [**StartResetPassword**](../reference/system-actions/user.md#startresetpassword) system server action, which sends a verification code to the user’s email.
1. End-users receive the verification code and a link to the **RecoverPasswordReset** page in the email.
1. On the **RecoverPasswordReset** screen, end-users enter their new password.
1. The **RecoverPasswordReset** screen then calls the **FinishResetPassword** system client action, which applies the email, verification code, and new password to update the user’s credentials in the Identity Server.

## Email configuration and troubleshooting

To ensure the password reset process works as expected, make sure you configure your ODC tenant to send emails. To do this, verify the email settings in the **Emails** page of the ODC Portal, under the **Configure** section. For step-by-step instructions, refer to [Configure emails](../manage-platform-app-lifecycle/configure-emails.md).

If users aren’t receiving the password reset email, ask them to check their spam folder or email filters. Password reset messages come from `noreply@outsystems.dev`.

## Related resources

* [User management](intro.md)
