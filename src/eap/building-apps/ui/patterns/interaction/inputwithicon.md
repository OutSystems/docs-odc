---
tags: 
summary: Input with Icon allows the end-user to input data with the help of a hint.
locale: en-us
guid: 74216051-2083-436f-b118-102696b9c182
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A15522&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Input with Icon

You can use the Input with Icon UI Pattern to allow the end-user input data with the help of a hint in the form of an icon.

The Input with Icon UI Pattern includes an icon and placeholder text that supports the user when entering data. Is assists the user's comprehension by providing an example of the type of input required.  

![Screenshot of the Input with Icon UI Pattern in a mobile app interface](images/inputwithicon-8-ss.png "Input with Icon UI Pattern")

**How to use the Input with Icon**

1. In ODC Studio, in the Toolbox, search for `Input with Icon`.

    The Input with Icon widget is displayed.

    ![Image showing the Input with Icon widget in the ODC Studio Toolbox](images/inputwithicon-1-ss.png "Input with Icon Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Input with Icon widget into the Main Content area of your application's screen.

    ![Dragging the Input with Icon widget into the Main Content area of an application screen](images/inputwithicon-2-ss.png "Dragging Input with Icon Widget")

    By default, the Input with Icon widget contains Icon and Input widgets.

1. Select the Input widget, and on the **Properties** tab, from the **Variable** drop-down, select **New Local Variable**.

    ![Selecting the Input widget to set properties in the ODC Studio](images/inputwithicon-3-ss.png "Selecting Input Widget")

1. Enter a name for variable. In this example we enter `Username` and set the **Data Type** property to Text.

    ![Creating a new local variable named 'Username' for the Input widget](images/inputwithicon-4-ss.png "Creating New Local Variable")

    This variable can be reused throughout your app.

1. Select the Input widget again, and on the **Properties** tab, in the **Prompt** property, enter the text you want displayed in the input box that describes the expected value. In this example, we enter `Username`.

    ![Setting the Prompt property of the Input widget to 'Username'](images/inputwithicon-5-ss.png "Setting Prompt Property")

1. To change the icon, select the Icon widget, and from the **Icon** drop-down, select the icon you want to display in the input box. In this example, we select the user icon.

    ![Selecting a user icon for the Input with Icon widget](images/inputwithicon-6-ss.png "Selecting Icon for Input")

1. You can change the Input with Icon's look and feel by setting the (optional) properties on the **Property** tab.

    ![Customizing the look and feel of the Input with Icon widget via properties](images/inputwithicon-7-ss.png "Customizing Input with Icon Appearance")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AlignIconRight (Boolean): Optional | If True, the icon is displayed on the right of the input box. If False, the icon is displayed on the left of the input box. This is the default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ExtendedClass (Text): Optional     | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |
