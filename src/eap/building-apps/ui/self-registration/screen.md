---
summary: Create a screen for users to self-register.
tags:
locale: en-us
guid: cd42bc12-6d0b-4da8-95f5-1e704fc0bfff
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Create a screen for users to self-register 

To enable users to self-register to access your app, you can provide end users with a screen. At the very least, end users must provide their name and email address.
  
To create a self-registration flow, open ODC studio and follow the steps below:

1. From the **Interface** tab, click **UI Flows** > Common folder then copy and paste the Login screen into the same folder. This creates a copy of Login screen named Login2.

    ![Copy login screen](images/copy-login-screen-odcs.png)

1. From the Common folder, click the **Login2** screen to display the form settings

1. On the form, change the name and title field to `Signup`, and for the description enter `screen where users sign up`.

1. From the **Interface** tab, click the **Widget Tree** > **Content** > **Container**, then rename LoginForm to `SignUpForm`.

    ![Sign-up screen structure](images/page-structure-odcs.png)

1. From the canvas, click the email label and input the fields container on the screen, then do the following:
    1. Copy and paste the specified container into the same folder.
    1. Set the Style Classes property of the new container to `margin-bottom-base`.

    ![Sign-up screen rename local variables](images/rename-local-variable-odcs.png)

1. From the **Elements** tab, click the **Sign-up screen** > **Under Variable** > **Add Local Variable** and name the new variable as `Name`, and the Data Type as `Text`.

1. From the **Widget Tree**, delete the container with the label password and input field in the Widget tree for the Signup screen.  

1. From the **Elements** tab, delete the client actions OnTogglePasswordVisibility and LoginOnClick, and the local variables IsPasswordVisible and Password.

1. In the **Signup** canvas, click **Login** button and change the text from Log in to `Sign-up` .

1. From the Toolbox, drag a button onto the canvas and place it after the Sign-up button and then name the button `Cancel`.

1. In the Properties panel for the cancel button, select `Common\\Login` from the dropdown for the On Click event.

1. In the Properties panel for the cancel button under the **Style classes** property, replace the class btn btn-primary with `btn margin-top-base` and change the value for IsFormDefault to No. Then, set the Width property to set Fill in under Styles > Layout.

    ![Sign-up delete useless code from Login screen.](images/delete-useless-code-odcs.png)

You can now [create logic to register a user.](logic.md)
