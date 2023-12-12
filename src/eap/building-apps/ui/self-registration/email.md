---
summary: Create email for users to start self-registration.
tags:
locale: en-us
guid: 8e30d486-dbf3-457c-87f8-4cd9e65b0156
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A22069&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---
# Create email to send verification code

<div class="info" markdown="1">

Before you begin creating your email, make sure you have an [email provider configured](../../../configuration-management/configure-emails.md).

</div>

This article describes creating an email to send to the person registering to use your app. First, you start an email with a verification code that the person must enter on the form. To make this task easier and quicker, OutSystems provides you with a sample email. To create your email, copy the email and then make the following updates.

## Creating the email

Follow these steps to create your own email.

![Screenshot of the base email template in OutSystems](images/email-screen-odcs.png "Base Email Screen")

1. From the **Interface** tab, click **UI Flows**. Then from the Emails copy and paste the **ResetPassword** email into the same folder. This creates a copy of the Reset password in the emails folder named ResetPassword2.
1. In the **Elements** tab, select Emails, and rename the email **ResetPassword2** to `UserRegistration`.
1. From **Emails**, click **UserRegistration**, then modify the **Subject** in the properties panel, for example, `Welcome to Your Sample App`.
1. On the canvas, click on the text above the unique verification code. Then in properties, replace the text.

    <div class="info" markdown="1">

    You're receiving this e-mail because you requested a password reset for your user account. To set a new password, use the button below or insert the following verification code in the reset password page.
    
    </div>

    New note text:

    <div class="info" markdown="1">

    Thank you for joining us. We’re glad to have you on board. You're receiving this e-mail because you registered in our _Your Name_ Portal. You now have a verification code.
    
    </div>

1. On the canvas, click on the text below the unique verification code. Then in Properties, replace the text.
    
    <div class="info" markdown="1">

    This verification code expires in 1 hour.

    </div>
    
    New note text:

    <div class="info" markdown="1">

    This verification code expires in 15 minutes.

    </div>

    ![Image showing the container to be deleted in the email template](images/delete-password-container.png "Delete Password Container")

1. Click on the **Widget** tree, and remove the following containers:
   1. Click on the **ResetPassword** parent container, to select and delete the container shown in the previous image.
   1. Click on the **Instruction** container, to select and delete the container.

    ![Screenshot of the final email template after modifications](images/final_result-odcs.png "Email Final Result")

## Updating the actions

Before updating the actions, delete the input parameter **CustomerEmail** by expanding the **UserRegistration** element in the **Elements** tab, then follow the steps below.

1. From the **Logic** tab, click **server actions** > **DoSignup** action to display logic on canvas.

    ![Diagram showing how to set user registration email properties in OutSystems](images/user-registration-variables-odcs.png "User Registration Variables")

1. From the canvas, click **UserRegistration** element to display Properties panel. Set the following properties:

    1. **CustomerName** to `user.Name`
    1. **VerificationCode** to `StartUserRegistration.UserRegistrationResult.VerificationCode`
    1. **ApplicationName** as `GetAppName()`

1. From the **Interface tab**, click  the **SignUp screen** > **SignUpOnClick** action to display **SignUpOnClick** on the canvas.
 
    ![Flowchart detailing the SignUpOnClick client action input parameters in OutSystems](images/signup-dosignup-input-parameters-odcs.png "SignUp OnClick Client Action")

1. From the canvas, click the **DoSignup** action to display the Properties panel, and confirm the following properties:

      1. **Id** as `NullIdentifier()`
      1. **Name** as `Name`
      1. **Email** as `UserEmail`

## Completing the DoSignUp flow

1. From the Toolbox, drag an **Assign** widget and place it below **DoSignup** action in the True branch.

1. In the **Assignments** pane, set the assign variable **IsExecuting** to `False`.

1. From the Toolbox, drag an **If** widget, and place it below the previously added **Assign widget**.

1. In the **If** widget, set the **Condition** as `DoSignup.IsSuccess`.

1. From the Toolbox, drag a **Message** widget into the True branch. Set the **Type** as `Info` and paste the following text.

    `Check your email to copy the verification code.`

1. From the Toolbox, drag an **End** element to the bottom of the True branch to complete the flow.

1. From the Toolbox, drag a **Message** widget into the False branch. Set the **Type** as `Error`, and paste the following text in the message.

    `DoSignup.ErrorMessage`

1. From the **Message** widget, go to the Properties panel, and set the **ApplicationName** as `GetAppName()`.

You can now [create a form to validate the verification code.](create-validation-form.md)

