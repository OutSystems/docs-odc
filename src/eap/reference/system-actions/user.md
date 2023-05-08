---
summary: User actions for built-in and/or external identity providers.
tags: 
locale: en-us
guid: 0889c9fd-98dc-489d-a8ed-bea68946f0ac
app_type: mobile apps, reactive web apps
platform-version: odc
---
# User

User actions for built-in and/or external identity providers.

## Actions

### ChangePassword
_Client action_

Allows a logged-in user to change their password. Throws an exception if the built-in identity provider is disabled for the current app.

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

Finalizes the reset password operation, using a verification code that can be received by email. Throws an exception if the built-in identity provider is disabled for the current app.

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

Due to a temporary technical limitation, you must add this action from the public elements. Navigate to the **Add public elements** icon on the top toolbar of ODC Studio or use the **Ctrl+Q** shortcut. Search for the action, select it, and click **Add**.

</div>

Sets the user as active and their password in the built-in identity provider and logs the user in.<br/>Call the action StartUserRegistration to register the user and obtain a temporary password.

_Inputs_

**Email**
:   Type: Text. Mandatory.
    Identification of the user completing the registration.           

**Password**
:   Type: Text. Mandatory.
    Password defined by the user registering.           

**TemporaryPassword**
:   Type: Text. Mandatory.
    Temporary password defined by the identity provider.     

_Outputs_

**RegistrationResult**
:   Type: [FinishUserRegistrationResult](#finishuserregistrationresult)  
    Result of the user registration action. Returns a user identifier if the user was successfully registered. Returns a failure reason if unsuccessful.

### GetPasswordComplexityPolicy
_Client action_

Gets the configured password policy for the built-in identity provider. Used to enable client-side validation in a user registration flow. Throws an exception if the built-in identity provider is disabled for the current app.

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

**Email**
:   Type: Boolean.
    True if the logged user is an external user.

### ResetPassword
_Client action_

Allows a user to reset their password using a verification code received via email. Throws an exception if the built-in identity provider is disabled for the current app.

_Inputs_

**Email**
:   Type: Text. Mandatory.
    Email of the user.

**ResetToken**
:   Type: Text. Mandatory.
    Verification code for the password change operation.

**NewPassword**
:   Type: Text. Mandatory.
    New password defined by the user.

_Outputs_

**ResetPasswordResult**
:   Type: [ResetPasswordResult](#resetpasswordresult)  
    Result of the reset password action. Returns the failure reason if unsuccessful.

### SendResetPasswordEmail
_Client action_

Triggers the reset password flow, which sends an email to the user with a verification code used to reset the password. Throws an exception if the built-in identity provider is disabled for the current app.

_Inputs_

**Email**
:   Type: Text. Mandatory.
    User email that will receive a recovery link. If no user with such email is found, no email will be sent.

### StartResetPassword
_Server action_

Triggers the reset password operation, returning a verification code that can be sent by email to the user. Use the FinishResetPassword action, which receives a verification code as an input, to complete the password reset operation. Throws an exception if the built-in identity provider is disabled for the current app.

_Inputs_

**Email**
:   Type: Text. Mandatory.
    Email of the user.

_Outputs_

**StartResetPasswordResult**
:   Type: [StartResetPasswordResult](#startpasswordresetresult)
    Result of the action. Returns the verification code if successful.
    
### StartUserRegistration
_Server action_

<div class="info" markdown="1">

Due to a temporary technical limitation, you must add this action from the public elements. Navigate to the **Add public elements** icon on the top toolbar of ODC Studio or use the **Ctrl+Q** shortcut. Search for the action, select it, and click **Add**.

</div>

Registers the user in the built-in identity provider by creating the user as inactive and setting a temporary password. Synchronises the [User entity](#user-1) with the identity provider.<br/>Call the action FinishUserRegistration to activate the user and change the password.<br/>It throws an exception if the built-in identity provider is disabled for the current app.

_Inputs_

**User**
:   Type: [UserInfo](#userinfo). Mandatory.
    User information that will be used to create a new user. 

_Outputs_

**StartUserRegistrationResult**
:   Type: [StartUserRegistrationResult](#startuserregistrationresult)  
    Result of the user registration action. 

### UpdateUserProfile
_Server action_

Allows a logged-in user to edit profile information. The user email can't be changed using this action. Throws an exception if the built-in identity provider is disabled for the current app.

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

Validates a user's password against the password complexity policy. Throws an exception if the built-in identity provider is disabled for the current app.

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

### ResetPasswordResult

*Attributes*

Success
:   Type: Boolean

ResetPasswordFailureReason
:   Type: ResetPasswordFailureReason

### StartPasswordResetResult

*Attributes*

Success
:   Type: Boolean

VerificationCode
:   Type: Text

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

VerificationCode
:   Type: Text

UserId
:   Type: User Identifier

### UpdateUserInfo

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

The end user of the apps.

*Attributes*

Id
:   Type: Text

Name
:   Type: Text

Email
:   Type: Email

PhotoUrl
:   Type: Text
