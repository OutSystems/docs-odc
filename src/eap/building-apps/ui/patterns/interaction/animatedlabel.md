---
tags: 
summary: The Animated Label animates a label when there is user input.
locale: en-us
guid: 996f45dd-32e8-4480-aa55-a0e81d07d7e6
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A12991&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Animated Label

You can use the Animated Label UI Pattern to animate a label when there is a user input.

 ![](<images/animatedlabel-example-ss.png>)

**How to use the Animated Label UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Animated Label`.

    The Animated Label widget is displayed.

    ![](<images/animatedlabel-widget-ss.png>)

1. From the Toolbox, drag the Animated Label widget into the Main Content area of your application's screen.

    ![](<images/animatedlabel-dragwidget-ss.png>)

    By default, the Animated Label widget contains Label and Input placeholders. The Input placeholder contains a variable of type Text. You can use this variable throughout your app.

1. Enter the relevant text in the Label placeholder. In this example, we enter `Name`.

    ![](<images/animatedlabel-labelname-ss.png>)

1. Enter a name and select a type for the Input variable.

    In this example, we enter the name User_Input and select UserInput as the variable type.

    ![](<images/animatedlabel-variable-type-ss.png>)

1. On the **Properties** tab, you can change the look and feel of the Animated Label by setting the (optional) properties.

    ![](<images/animatedlabel-properties-ss.png>)

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |
