---
tags: 
summary: Learn how to implement the Card Item UI Pattern in OutSystems Developer Cloud (ODC) to enhance mobile app interfaces.
locale: en-us
guid: 0e53449a-f4be-400e-9736-d7d44cc30e7c
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A10572&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Card Item

You can use the Card Item UI Pattern to list items with multiple content types, such as image or icon (to the left), a title and description, and an action to the right.

![Example of a Card Item layout in a mobile app interface](images/carditem-1.png "Card Item Example")

**How to use the Card UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Card Item`.

    The Card Item widget is displayed.

    ![Screenshot showing the Card Item widget in the ODC Studio Toolbox](images/carditem-2-ss.png "Card Item widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Card widget into the Main Content area of your application's screen.

    In this example, we drag the widget into the Card widget that's already in the Main Content area of the screen. You can add as many Card Item widgets as required (we add 4). 

    ![Process of dragging the Card Item widget into the Main Content area of an application screen](images/carditem-3-ss.png "Dragging Card Item widget into Main Content Area")

    By default, the Card Item widget contains a Left, Title, Content, and Right placeholder.

1. Add your content to each of the placeholders.

    In this example, we add an icon to the Left placeholder, text to the Title and Content placeholders, and a phone icon to the Right placeholder.

    ![Example of adding an icon and text to the placeholders of a Card Item widget](images/carditem-4-ss.png "Adding Content to Card Item Widget Placeholders")

1. On the **Properties** tab, you can customize the Card Item's look and feel by setting any of the (optional) properties.

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<p>Examples</p><ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. |
