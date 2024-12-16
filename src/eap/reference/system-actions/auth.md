---
summary: Explore authentication actions for built-in and external identity providers in OutSystems Developer Cloud (ODC).
tags: authentication, identity providers, user management, security, login
locale: en-us
guid: af4a6d9d-0af3-434b-b3b9-daf8d49ad6f7
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - remember
---

# Authentication system actions

Authentication actions for built-in and/or external identity providers.

## Actions

### Login
_Client action_

Performs a login in to the built-in identity provider using a username and password. By default, a user is logged in for 12 hours until a logout is performed. This default cannot be changed. User profile information is synchronized to the [User entity](user.md#user-1) before this action is finished. Throws an exception if the built-in identity provider is disabled for the current app.

_Inputs_

**Username**
:   Type: Text. Mandatory
    Name of the user logging in.

**Password**
:   Type: Text. Mandatory.
    Password of the user logging in.

_Outputs_

**UserLoginResult**
:   Type: Structure.
    Result of the user login action. Returns a user identifier if the user was successfully logged in. Returns a failure reason if unsuccessful.

### GetExternalLoginURL
_Client action_

<div class="info" markdown="1">

You must first add this action due to a temporary technical limitation. Navigate to the **Add public elements** icon on the top toolbar of ODC Studio or use the **Ctrl+Q** shortcut. Search for the action, select it, and click **Add**.

</div>

Returns the URL to which the user should be redirected in order to login in an external provider.

_Inputs_

**ReturnToURL**
:   Type: Text.
    URL called after the authentication process. The provider will redirect users to this URL after a successful login.

**IdentityProvider**
:   Type: Text.
    Identity provider where the user will log in. Defined as the provider name in ODC Portal.

_Outputs_

**ExternalLoginURL**
:   Type: Text.  
    The redirect to redirect the user to for the login.

<div class="info" markdown="1">

You can learn about how to use this action in your apps [here](../../manage-platform-app-lifecycle/external-idps/apps.md).

</div>

### Logout
_Client action_

Logs out the user from the built-in identity provider.

### GetExternalLogoutURL
_Client action_

<div class="info" markdown="1">

You must first add this action due to a temporary technical limitation. Navigate to the **Add public elements** icon on the top toolbar of ODC Studio or use the **Ctrl+Q** shortcut. Search for the action, select it, and click **Add**.

</div>

Returns the URL where the user can log out of an external identity provider, if one is configured, or "" otherwise.

CallbackURL is the URL that the user will be redirected to after a successful logout.
If an IdentityProvider is configured for the current app and the user is currently logged in, the provider's logout URL is returned. Use a RedirectToURL node in your flow, after the action, to redirect the user to this URL to complete the logout. 

Throws an exception if no external identity provider is configured for the current app or if the user is not currently logged in with an external provider.

_Inputs_

**CallbackURL**
:   Type: Text.
    URL called after the logout process. The provider will redirect users to this URL after a successful logout.

_Outputs_

**ExternalLogoutURL**
:   Type: Text.
    Value of the URL where the user can log out of an external provider, if one is configured, or "" otherwise. Use a RedirectToURL node in your flow, after the action, to redirect the user to this URL.

## Structures

### UserLoginResult

*Attributes*

RetryAfterSeconds
:   Type: Integer

Success
:   Type: Boolean

UserId
:   Type: User Identifier

UserLoginFailureReason
:   Type: UserLoginFailureReason
