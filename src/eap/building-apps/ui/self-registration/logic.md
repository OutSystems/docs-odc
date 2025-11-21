---
summary: Learn how to set up user registration logic in OutSystems Developer Cloud (ODC) by configuring server actions and validating user inputs.
tags: user registration, user input validation
locale: en-us
guid: bf31e755-d3d7-49b2-9591-fd0d197db633
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A22075&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
topic:
  - self-registration
---

# Create logic to register a user

This article explains how to create the logic for the self-registration flow in ODC. You'll validate user input and configure server actions. You must complete each section in order.

<div class="info" markdown="1">

You can save time by installing the [User Self Registration Flow](https://www.outsystems.com/forge/component-overview/17017/user-self-registration-flow-odc) asset from the **Forge** in the ODC Portal, which already implements the flow described in this article.

</div>

## Prerequisites

Before you begin, [create the Sign up screen](screen.md).

## Create the Signup client action

The goal of the **SignUpOnClick** client action is to handle the user's request from the Sign up screen to sign up. To create the **SignUpOnClick** client action in ODC Studio, follow these steps:

1. Go to the **Interface** > **Elements** tab, expand **UI Flows** > **Common**, and open the **SignUp** screen.

    ![Interface of the Signup screen in OutSystems showing the Toolbox, canvas, and logic areas](images/signup-screen-odcs.png "Signup Screen Interface")

1. On the canvas, select the **Signup** button, and from the **On Click** event dropdown, select **New Client Action**.

    The **SignUpOnClick** action flow opens on the canvas.

    ![OutSystems canvas displaying the initial setup of the SignUpOnClick action flow](images/starting-signup-flow-odcs.png "Initializing Signup Flow")

1. Add an **Assign** element to the **True** branch after the **SignUpForm.Valid** if node, and assign the **IsExecuting** variable to `True`.
1. Add a **Run Server Action** after the **IsExecuting** assign, and in the dialog, choose **New Server Action**. Name it `DoSignup`.
1. Add an **Assign** element to the **True** branch after the **DoSignup** server action, and assign the **IsExecuting** variable to `False`.

    ![Provisional setup of the SignUpOnClick action flow in OutSystems](images/signuponclick-provisional-odcs.png "SignUpOnClick Provisional Setup")

## Add the beginning logic to the DoSignup server action

Add the beginning logic to the **DoSignup** server action:

1. Double-click the **DoSignup** server action.

1. Add the **StartUserRegistration** [public element](../../libraries/use-public-elements.md) after the **Start** node.

1. Right-click the **DoSignup** server action and select **Add Input Parameter**. Set the name to **User** and the **Data Type** to `UserInfo`.

1. On the canvas, select **StartUserRegistration**, and set **User** to `User`.

    ![OutSystems interface showing the expansion of user input parameters for the StartUserRegistration action](images/expand-user-input-parameter-odcs.png "Expanding User Input Parameters")

1. Right-click **DoSignup** and select **Add Output** parameter. Add:
    * **IsSuccess** with data type `Boolean`
    * **ErrorMessage** with data type `Text`

    ![OutSystems DoSignup Server action interface with three output parameters added](images/output-paraments-signup-odcs.png "Output Parameters Configuration")

1. On the **DoSignup** canvas, drag an **Assign** after **StartUserRegistration** and set:
    * **IsSuccess** to `StartUserRegistration.UserRegistrationResult.Success`

    ![OutSystems canvas with Assign widget setting output variables for StartUserRegistration](images/star-user-registration-variables-output-odcs.png "Setting Output Variables for User Registration")

1. Back in **SignUpOnClick** action logic, select the **DoSignup** run server action, and then click **+** to expand User.

    ![OutSystems SignUpOnClick client action properties panel showing the configuration of DoSignup input parameters](images/signup-dosignup-expand-input-parameters-odcs.png "Configuring DoSignup Input Parameters")

1. Set the following **Attribute Values**:

    * **Name** to `Name`
    * **Email** to `UserEmail`

    ![OutSystems SignUpOnClick client action properties panel showing the configuration of DoSignup input parameters](images/signup-do-signup-input-parameters-odcs.png "Configuring DoSignup Input Parameters")

## Validate the user input

To ensure you collect valid user data (email, name, and username), you must add validations to the flow.

### Check email format

To validate the email format, follow these steps:

1. On the **DoSignup** server action logic, drag an **If** after the **IsSuccess** assign.
1. Set the **If** node's **Label** to `IsInvalidEmail?` and **Condition** to `StartUserRegistration.UserRegistrationResult.StartUserRegistrationFailureReason.InvalidEmail`.
1. In the **True** branch, add an **Assign** and set `ErrorMessage` to `"Invalid Email"`.

### Check name format

To validate the name format, follow these steps:

1. On the **DoSignup** server action logic, in the **False** branch, add an **If** element.
1. Set the **If** node's **Label** to `IsInvalidName?` and **Condition** to `StartUserRegistration.UserRegistrationResult.StartUserRegistrationFailureReason.InvalidName`.
1. In the **True** branch, add an **Assign** element and set the `ErrorMessage` variable to `"Invalid Name"`.

### Check if the user already exists

To check if the user already exists, follow these steps:

1. On the **DoSignup** server action logic, in the **False** branch of the last **If**, add an **If** element.
1. Set the **If** node's **Label** to `UserAlreadyExists?` and **Condition** to `StartUserRegistration.UserRegistrationResult.StartUserRegistrationFailureReason.UserAlreadyRegistered`.
1. In the **True** branch, add an **Assign** and set `ErrorMessage` to `"User already exists. Try to recover your password"`.

    ![OutSystems DoSignup action flow depicting the validation logic for user registration](images/start-user-registration-validations-odcs.png "User Registration Validation Logic")

## Send a registration email

To send an email on successful registration, follow these steps:

1. On the **DoSignup** server action logic, in the **False** branch of the last **If**, add another **If** element.
1. Set the **If** node's **Label** to `Success?` and **Condition** to `StartUserRegistration.UserRegistrationResult.Success`.
1. In the **True** branch, add a **Send Email** widget. Set **Name** to `UserRegistration`, **To** to `User.Email`, and from the **Email** dropdown, select **New Email**.

![OutSystems DoSignup action flow showing the complete logic](images/do-sign-up-logic-odcs.png "DoSignup Logic")

## Next step

The next step of the self-registration flow is to [create the email to send the verification code](email.md).
