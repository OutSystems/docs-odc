---
summary: OutSystems Developer Cloud (ODC) offers user management actions for identity providers, including password resets and user profile updates.
tags: user management, password policy, account security, identity providers, authentication
locale: en-us
guid: 0889c9fd-98dc-489d-a8ed-bea68946f0ac
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

# User system actions

User actions for built-in and/or external identity providers.

## Actions

### ChangePassword

_Client action_

Allows a logged-in user to change their password. Changing passwords for users with access to the ODC Portal is not supported through this system action, even if the user also has application roles. For more information about passwords, check [Passwords](https://success.outsystems.com/documentation/outsystems_developer_cloud/user_management/passwords/).

_Inputs_

**Username**
:   Type: Text. Mandatory.
    Identification of the user changing the password.
    
**NewPassword**
:   Type: Text. Mandatory.
    Identification of the user changing the password.

**OldPassword**
:   Type: Text. Mandatory.
    Old user password.

_Outputs_

**ChangePasswordResult**
:   Type: [ChangePasswordResult](#changepasswordresult)
    Result of the password change action. Returns boolean values for the complexity policy failed if unsuccessful.

### FinishResetPassword

_Client action_

Finalizes the reset password operation, using a verification code that can be received by email. The client action throws an exception if the built-in identity provider is disabled for the current app.

_Inputs_

**Email**
:   Type: Email. Mandatory.
    Email of the user.

**VerificationCode**
:   Type: Text. Mandatory.
    Verification code for the password change operation.

**NewPassword**
:   Type: Text. Mandatory.
    New password defined by the user.

_Outputs_

**FinishResetPasswordResult**
:   Type: [FinishResetPasswordResult](#finishpasswordresetresult)
    Result of the reset password action. Returns the failure reason if unsuccessful.

### FinishUserRegistration

_Client action_

<div class="info" markdown="1">

Due to a temporary technical limitation, add this action from the public elements. Navigate to the **Add public elements** icon on the toolbar of ODC Studio or use the **Ctrl+Q** shortcut. Search for the action, select it, and click **Add**.

</div>

Activates the user’s password in the built-in identity provider and logs the user in.<br/>Call the action StartUserRegistration to register the user and obtain a temporary password.

_Inputs_

**Email**
:   Type: Text. Mandatory.
    Identification of the user completing the registration.

**Password**
:   Type: Text. Mandatory.
    Password defined by the user registering.

**VerificationCode**
:   Type: Text. Mandatory.
    Temporary password defined by the identity provider.

_Outputs_

**RegistrationResult**
:   Type: [FinishUserRegistrationResult](#finishuserregistrationresult)  
    Result of the user registration action. Returns a user identifier if the user was successfully registered. Returns a failure reason if unsuccessful.
    
### FinishUpdateEmail

_Client action_

Finalizes the update email operation, using a verification code.

_Inputs_

**VerificationCode**
:   Type: Text. Mandatory.
    Verification code for the email change operation.

_Outputs_

**FinishUpdateEmailResult**
:   Type: [FinishUpdateEmailResult](#finishupdateemailresult)  
    Result of the the action. If true, the action was successful.

*FinishUpdateEmailFailureReason**
:   Type: [FinishUpdateEmailFailureReason](#finishupdateemailfailurereason)  
    Contains the reason for failure if the action is not successful.

### GetPasswordComplexityPolicy

_Client action_

Gets the configured password policy for the built-in identity provider. Used to enable client-side validation in a user registration flow. The client action throws an exception if the built-in identity provider is disabled for the current app.

_Outputs_

**PasswordComplexityPolicy**
:   Type: [PasswordComplexityPolicy](#passwordcomplexitypolicy)  
    Result of the password policy action. Returns boolean values for the password complexity criteria.

### GetUserProfile
_Client action_

Returns logged-in user's information from the identity provider and updates the [User entity](#user-1) with that information.

_Outputs_

**UserInfo**
:   Type: [UserInfo](#userinfo)  
    User information.

### IsExternalUser

_Client action_

Function that validates if the logged-in user is from an external identity provider. Intended for use cases where we need to filter operations only available for users from the built-in identity provider.

_Outputs_

**IsExternalUser**
:   Type: Boolean.
    True if the logged user is an external user.

### StartResetPassword

_Server action_

Triggers the reset password operation, returning a verification code that sends by email to the user. Use the FinishResetPassword action, which receives a verification code as an input, to complete the password reset operation. The server action throws an exception if the built-in identity provider is disabled for the current app.

Resetting passwords for members with access to ODC Portal isn't supported through this system action, even if the member also has application roles. If this action is called with a ODC Portal member e-mail no verification code is returned. Members must always reset their password using the **Forgot password?** link in ODC Portal. ODC temporarily locks users out after repeated failed passsword reset attempts. The lockout duration increases with each additional failed attempt, starting at just a few seconds and reaching a maximum of approximately 5 minutes.

_Inputs_

**Email**
:   Type: Text. Mandatory.
    Email of the user.

_Outputs_

**StartResetPasswordResult**
:   Type: [StartResetPasswordResult](#startpasswordresetresult)
    Result of the action. Returns the verification code if successful.

### StartUpdateEmail

_Server action_

Triggers the update email operation for users who don't have access to the ODC Portal, returning a verification code that can be sent by email to the user. ODC temporarily locks users out after repeated failed attempts to update their email. The lockout duration increases with each additional failed attempt, starting at just a few seconds and reaching a maximum of approximately 5 minutes.

_Inputs_

**Email**
:   Type: Text. Mandatory.
    User's new email.

<div class="info" markdown="1">

The user's email cannot be removed from their profile. 

</div>

_Outputs_

**StartUpdateEmailResult**
:   Type: [StartUpdateEmailResult](#startupdateemailresult)
    Verification code created by the identity provider. **FinishUpdateEmail** is used to verify the email defined by the user.

**StartUpdateEmailFailureReasom**
:   Type: [StartUpdateEmailFailureReason](#startupdateemailfailurereason)
    Contains the reason for failure if the action isn't successful.
    
### StartUserRegistration

_Server action_

<div class="info" markdown="1">

Due to a temporary technical limitation, you must add this action from the public elements. Navigate to the **Add public elements** icon on the toolbar of ODC Studio or use the **Ctrl+Q** shortcut. Search for the action, select it, and click **Add**.

</div>

Registers the user in the built-in identity provider by creating the user as active. Call the action **FinishUserRegistration** to change the user's temporary password. The server action throws an exception if the built-in identity provider is disabled for the current app. ODC temporarily locks users out after repeated failed attempts to complete their registration. The lockout duration increases with each additional failed attempt, starting at just a few seconds and reaching a maximum of approximately 5 minutes.
 
_Inputs_

**User**
:   Type: [UserInfo](#userinfo). Mandatory.
    User information used to create a new user.

_Outputs_

**StartUserRegistrationResult**
:   Type: [StartUserRegistrationResult](#startuserregistrationresult)  
    Result of the user registration action.

### UpdateUserProfile

_Server action_

Allows a logged-in user to edit profile information. User can't change user email using this action. The server action throws an exception if the built-in identity provider is disabled for the current app.

_Inputs_

**User**
:   Type: [UserUpdateInfo](#UserUpdateInfo). Mandatory.
    New user information used to update the user.

_Outputs_

**UpdateUserResult**
:   Type: [UpdateUserResult](#UpdateUserResult)  
    Result of the update user action. Returns the failure reason if unsuccessful.

### ValidatePasswordComplexity

_Client action_

Validates a user's password with the password complexity policy. The client action throws an exception if the built-in identity provider is disabled for the current app.

_Inputs_

**Password**
:   Type: Text. Mandatory.
    Password sent by the user.

_Outputs_

**PasswordValidationResult**
:   Type: [PasswordValidationResult](#PasswordValidationResult)  
    Result of the password validation action. Returns boolean values for the password validity and complexity criteria.

## Structures

### ChangePasswordResult

*Attributes*

Success
:   Type: Boolean

ChangePasswordFailureReason
:   Type: ChangePasswordFailureReason

### FinishPasswordResetResult

*Attributes*

Success
:   Type: Boolean

FinishResetPasswordFailureReason
:   Type: FinishResetPasswordFailureReason

### FinishUserRegistrationResult

*Attributes*

Success
:   Type: Boolean

UserId
:   Type: User Identifier

FinishUserRegistrationFailureReason
:   Type: FinishUserRegistrationFailureReason

### PasswordComplexityPolicy

*Attributes*

MinimumLength
:   Type: Integer

UpperCaseLetterRequired
:   Type: Boolean

LowerCaseLetterRequired
:   Type: Boolean

NumberRequired
:   Type: Boolean

SpecialCharacterRequired
:   Type: Boolean

### PasswordValidationResult

*Attributes*

IsValid
:   Type: Boolean

MissingLowerCaseLetter
:   Type: Boolean

MissingMinimumLength
:   Type: Boolean

MissingUpperCaseLetter
:   Type: Boolean

MissingNumber
:   Type: Boolean

MissingSpecialCharacter
:   Type: Boolean

### StartResetPasswordResult

*Attributes*

Success
:   Type: Boolean

VerificationCode
:   Type: Text

### StartUpdateEmailResult

*Attributes*

Success
:   Type: Boolean

VerificationCode
:   Type: Text

### StartUpdateEmailFailureReason

*Attributes*

InvalidEmail
:   Type: Boolean

### FinishUpdateEmailResult

*Attributes*

Success
:   Type: Boolean

### FinishUpdateEmailFailureReason

*Attributes*

InvalidVerificationCode
:   Type: Boolean

### FinishResetPasswordFailureReason

*Attributes*

PasswordComplexityPolicyFailed
:   Type: Boolean

InvalidVerificationCode
:   Type: Boolean

InvalidEmail
:   Type: Boolean

### UserInfo

*Attributes*

Name
:   Type: Text

Email
:   Type: Text

PhotoURL
:   Type: Text

### StartUserRegistrationResult

*Attributes*

Success
:   Type: Boolean

StartUserRegistrationFailureReason
:   Type: StartUserRegistrationFailureReason
     * InvalidEmail
     * InvalidName
     * UserAlreadyRegistered

VerificationCode
:   Type: Text

    <div class="info" markdown="1">

    The Verification Code is valid for 15 minutes. This is a fixed value.

    </div>

UserId
:   Type: User Identifier

### UserUpdateInfo

*Attributes*

Name
:   Type: Text

PhotoURL
:   Type: Text

### UpdateUserResult

*Attributes*

Success
:   Type: Boolean

UserPhotoURL
:   Type: Text

UpdateUserFailureReason
:   Type: UpdateUserFailureReason

## Entities

### User

The end-user of the apps.

*Attributes*

Id
:   Type: Text

Name
:   Type: Text

Email
:   Type: Email

PhotoUrl
:   Type: Text
