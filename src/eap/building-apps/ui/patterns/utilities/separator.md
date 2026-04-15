---
tags: ui design, user experience, application development, visual organization, separation patterns
summary: Learn how to visually organize content in your applications using the Separator UI Pattern in OutSystems Developer Cloud (ODC).
locale: en-us
guid: 91b4bcb5-4ebd-4cf5-9dca-b64edaef2256
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A21611&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
  - remember
topic:
  - add-widget-ui-pattern
---

# Separator

<div class="info" markdown="1">

Applies to the OutSystems UI framework only.

</div>

You can use the Separator UI Pattern to separate content clearly and ease visual organization.

  ![Example of a Separator widget used in a mobile app interface](images/separator-example.png "Separator Widget Example")

**How to use the Separator UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Separator`.

    The Separator widget is displayed.

    ![Screenshot showing the Separator widget in the ODC Studio Toolbox](images/separator-widget-ss.png "Separator Widget in Toolbox")

1. From the Toolbox, drag the Separator widget into the Main Content area of your application's screen, where you want to separate content. In this example, we drag the widget in between 2 images.

    ![Process of dragging the Separator widget into the Main Content area of an application screen](images/separator-drag-ss.png "Dragging Separator Widget to Screen")

    By default, the pattern displays a horizontal line with the application’s primary color.

1. On the **Properties** tab, you can customize the Separator's look and feel by setting any of the optional properties, for example, the color and the amount of space separating the content.

    ![Screenshot of the Properties tab for customizing the Separator widget's appearance](images/separator-prop-ss.png "Separator Pattern Properties")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| **Property** | **Description** |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Color (Color Identifier): Optional | Set the color for the separator line. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - Displays a gray (Neutral4) line (default value).</li><li>_Entities.Color.Red_ - Displays a red line.</li></ul></p> |
| Space (Space Identifier): Optional | Set the space around the separator line. The predefined vales are: <p> <ul><li>None</li><li>Extra small</li><li>Small</li><li>Base</li><li>Medium</li><li>Large</li><li>Extra large</li><li>Extra extra large</li></ul></p><p>Examples <ul><li>_Blank_ - Displays a space of 16px (_Entities.Space.Base_) around the line separator. This is the default value.</li><li>_Entities.Space.Large_ - Displays a space of 32px around the line separator.</li></ul></p> |
| IsVertical (Boolean): Optional | If False, the separator line displays horizontally (default). If True, the separator line displays vertically. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass"- Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
