---
tags: user interface, animation, tutorials for beginners
summary: Explore how to animate user input labels using the Animated Label UI Pattern in OutSystems Developer Cloud (ODC).
locale: en-us
guid: 996f45dd-32e8-4480-aa55-a0e81d07d7e6
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A12991&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
  - remember
---

# Animated Label

You can use the Animated Label UI Pattern to animate a label when there is a user input.

 ![Screenshot of an example of the Animated Label in action](images/animatedlabel-example-ss.png "Animated Label Example")

**How to use the Animated Label UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Animated Label`.

    The Animated Label widget is displayed.

    ![Screenshot showing the Animated Label widget in the ODC Studio Toolbox](images/animatedlabel-widget-ss.png "Animated Label Widget in Toolbox")

1. From the Toolbox, drag the Animated Label widget into the Main Content area of your application's screen.

    ![Screenshot demonstrating how to drag the Animated Label widget into the Main Content area](images/animatedlabel-dragwidget-ss.png "Dragging Animated Label Widget")

    By default, the Animated Label widget contains Label and Input placeholders. The Input placeholder contains a variable of type Text. You can use this variable throughout your app.

1. Enter the relevant text in the Label placeholder. In this example, we enter `Name`.

    ![Screenshot showing the Label placeholder with the text 'Name' entered in the Animated Label widget](images/animatedlabel-labelname-ss.png "Setting Label Placeholder Text")

1. Enter a name and select a type for the Input variable.

    In this example, we enter the name User_Input and select UserInput as the variable type.

    ![Screenshot of the Animated Label widget where the Input variable name 'User_Input' and type 'UserInput' are being set](images/animatedlabel-variable-type-ss.png "Defining Input Variable for Animated Label Widget")

1. On the **Properties** tab, you can change the look and feel of the Animated Label by setting the (optional) properties.

    ![Screenshot of the Properties tab for the Animated Label widget with options to customize its appearance](images/animatedlabel-properties-ss.png "Animated Label widget Properties")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |
