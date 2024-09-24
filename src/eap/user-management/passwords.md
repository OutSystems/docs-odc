---
summary: Learn password management and recovery protocols for OutSystems Developer Cloud (ODC), including creation, changes, and lockout procedures.
locale: en-us
guid: 41b86768-295e-4aeb-98ed-9a0f6db4cfd2
app_type: mobile apps, reactive web apps
figma:
platform-version: odc
---

# Passwords

New users must set up their own passwords. The password must be at least 12 characters long and contain at least:

* One numeric digit
* One character from this set: !, \, #, $, %, &, ', (, ), *, +, ,, -, ., /, :, ;, <, =, >, ?, @, [
* One upper-case letter

Only users can manage their passwords. Users can change their password using the **ODC Portal** > **User dropdown** > **Change password**.

Organization members with an organization role such as Developer or Admin can also recover their forgotten password from the Portal login page by clicking **Forgot password**.

If you're not receiving the password reset email, please check your spam folder and any filters. The emails are sent from `noreply@outsystems.dev`.

<div class="info" markdown="1">

Admins don't have permission to change or recover other users' passwords.

</div>

You can use pre-built user screens in your app to enable end-users to change and recover their password. For more information, see [Custom authentication flows](../building-apps/ui/custom-auth.md). If organization users (Organization members) working in an app need to recover their password, they must use the ODC Portal.

ODC temporarily locks users out after five consecutive failed sign-in or password change attempts. The lockout duration increases with each additional failed attempt, starting at just a few seconds and reaching a maximum of approximately 15 minutes. After the lockout period passes, your user information returns to the initial state.
