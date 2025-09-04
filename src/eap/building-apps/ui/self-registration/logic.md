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

Once you [create a screen for users to sign in](screen.md), you can add logic to your screen. Logic enables you to validate your user's input and set up actions if the information is true or false.

If this is the first time you are creating the logic for self-registration, then follow all the procedures. If you are making updates to your existing app, jump to the task you want to do.
  
To create logic to register users, follow these procedures. To make it easier, The procedure is divided into sections.

## Setting up the Server action

1. From the **Interface** tab, select the **Common** > **Signup**, and then on the canvas, click the **Signup** button to display the Properties panel.

    ![Interface of the Signup screen in OutSystems showing the Toolbox, canvas, and logic areas](images/signup-screen-odcs.png "Signup Screen Interface")

    <div class="info" markdown="1">

    This screenshot shows the parts of the screen you use often. The Toolbox is on the left, the canvas is in the middle, and the logic is on the right. Depending upon what you select, what you see changes.

    </div>

1. From the **Properties** panel, click the dropdown for the on-click event and select **New Client Action**. The **SignUpOnClick** action flow displays on the canvas.

    ![OutSystems canvas displaying the initial setup of the SignUpOnClick action flow](images/starting-signup-flow-odcs.png "Initializing Signup Flow")

1. From the Toolbox, drag the **Assign** widget onto the **True** branch and place it below the **Assign** element. The Assignments panel displays.
1. In the **Assignments** panel, add the **IsExecuting** variable and set it to `True`.
1. From the Toolbox drag a **Run Server Action** widget to the canvas and place it below the **IsExecuting** assign element to display a select action pop-up.
1. From the **Select Action** pop-up, click the **New Server Action** button to display the canvas and the Properties panel.
1. In the **Server Action** Properties panel, in the name field enter `DoSignup`. The DoSignup function handles the user registration and validation inside the SignUpOnClick function.

## Configuring the Server action

After setting up the DoSignup action, you need to configure the Server action. In the Server action, you define what you want to happen next.

1. From the **Logic** tab, select **Server action**, and rename **Action1** to **DoSignup**.

1. From the **Logic** tab, select **Server action**, right-click, and select **Add Public element** to display a pop-up.

    ![OutSystems Logic tab with the Add Public Element pop-up searching for StartUserRegistration](images/add-public-element-odcs.png "Adding a Public Element")

    <div class="info" markdown="1">

    You can search for the action by pressing **Ctrl+Q** to display a Search bar.

    </div>

1. In the search bar pop-up, search for **StartUserRegistration**, then select it from the dropdown and click **Add**. ODC displays the **StartUserRegistration** action below system actions in the Logic tab.
1. From the Toolbox, drag the **Run Server Action** widget to the canvas and place it between the Start and End elements to display a pop-up. In the search pop up, enter **StartUserRegistration** Server action and then click **Select.**
  
    ![OutSystems interface showing the expansion of user input parameters for the StartUserRegistration action](images/expand-user-input-parameter-odcs.png "Expanding User Input Parameters")

1. From the **Logic** tab, right-click the **DoSignup** Server action and select **add input parameter**. Set the Name to `User` and the data type to `User`. In the **DoSignup** canvas, click **StartUserRegistration** action to display properties. Click  **+** to expand the user input and enter `name` as User.Name and `email` as User.Email.

    ![OutSystems DoSignup Server action interface with three output parameters added](images/output-paraments-signup-odcs.png "Output Parameters Configuration")

1. From the **Server Action**, right-click the **DoSignup** Server action and select **Add Output** parameter. Enter the following output parameters:
    * IsSuccess with data type `Boolean`.
    * ErrorMessage with data type `Text`.
    * VerificationCode with data type `Text`.

    ![OutSystems canvas with Assign widget setting output variables for StartUserRegistration](images/star-user-registration-variables-output-odcs.png "Setting Output Variables for User Registration")

1. On the **DoSignup** canvas, drag an **Assign** widget and place it after the **StartUserRegistration** action. Under the Assignments panel, assign, set the following:
    * IsSuccess as `StartUserRegistration.UserRegistrationResult.Success`.
    * VerificationCode as `StartUserRegistration.UserRegistrationResult.VerificationCode`.

    ![OutSystems SignUpOnClick client action properties panel showing the configuration of DoSignup input parameters](images/signup-dosignup-input-parameters-odcs.png "Configuring DoSignup Input Parameters")

1. From the canvas, click the **DoSignup** action to display the Properties panel, and set the following properties:

    * **Id** as `NullIdentifier()`
    * **Name** as `Name`
    * **Email** as `UserEmail`

## Validate the input

As a best practice, OutSystems recommends that you validate the information you are requesting users to input. This helps to ensure you are getting the information you expect from users.

You can check that the data entry fields only allow user data that complies with the app’s terms such as emails, names, and usernames.

### Checking for invalid emails

1. From the Toolbox, drag an **If** widget after the IsSuccess assign element.
1. In the Properties panel of the widget, set the Label as IsInvalidEmail? and the Condition as StartUserRegistration.UserRegistrationResult.StartUserRegistrationFailureReason.InvalidEmail
1. From the Toolbox, drag an **Assign** widget into the True branch.
1. Under the **Assignments** tab, assign a variable ErrorMessage as `Invalid Email`.

### Checking for invalid names

1. From the Toolbox, drag an **If** widget into the False branch.
1. In the Properties panel of the widget, set the Label as IsInvalidName? and the Condition as StartUserRegistration.UserRegistrationResult.StartUserRegistrationFailureReason.InvalidName
1. From the Toolbox, drag an **Assign** widget into the True branch.
1. Under the **Assignments** tab, assign a variable ErrorMessage as `Invalid Name`.

### Checking for a unique username

1. From the Toolbox, drag an **If** widget into the False branch.
1. In the Properties panel of the widget, set the Label as UsernameAlreadyExists? And the Condition as StartUserRegistration.UserRegistrationResult.StartUserRegistrationFailureReason.UserAlreadyRegistered
1. From the Toolbox, drag an **Assign** widget into the True branch.
1. Under the **Assignments** tab, assign a variable ErrorMessage as `User already exists. Try to recover your password`.

Verify the validation logic of the DoSignup action looks like the following screen shot.

![OutSystems DoSignup action flow depicting the validation logic for user registration](images/start-user-registration-validations-odcs.png "User Registration Validation Logic")

As a final validation, you can configure the flow to send an email to the user with the users name. Follow the steps below:

1. From the Toolbox, drag an **If** widget into the False branch. In the properties panel of the widget, set the Label as `IsUserRegistered?` and the Condition as `StartUserRegistration.UserRegistrationResult.Success`.

1. In the True branch, from the Toolbox, drag a **Send Email** widget. In the properties panel of the widget, set Name to `UserRegistration` and To as `User.Email`. In the Email setting, select the **New Email** option from the dropdown.

You can now [create an email to send the verification code.](email.md)

