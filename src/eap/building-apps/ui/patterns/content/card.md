---
tags: ui design patterns, cards ui pattern
summary: Explore how to effectively utilize the Cards UI Pattern in OutSystems Developer Cloud (ODC) to organize and display information.
locale: en-us
guid: 594f6cef-f632-40c4-9ffc-2204252e6dd2
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A10485&t=ZwHw8hXeFhwYsO5V-1
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
---

# Card

<div class="info" markdown="1">

Applies to the OutSystems UI framework only.

</div>

You can use the Cards UI Pattern to group small pieces of information and highlight them on the screen. The information is grouped into a small block that is easily noticeable on-screen.

![Example of a Card UI Pattern in use](images/card-1.png "Card UI Pattern Example")

**How to use the Card UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Card`.

    The Card widget is displayed.

    ![Screenshot showing the Card widget in the ODC Studio Toolbox](images/card-2-ss.png "Card Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Card widget into the Main Content area of your application's screen.

    ![Screenshot of dragging the Card widget into the Main Content area in ODC Studio](images/card-3-ss.png "Dragging Card Widget into Main Content Area")

1. Add your content to the placeholder. In this example we add some text.

    ![Screenshot showing text being added to the Card widget placeholder in ODC Studio](images/card-4-ss.png "Adding Content to Card Placeholder")

1. On the **Properties** tab, you can customize the Card's look and feel by setting any of the (optional) properties.

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property | Description |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UsePadding (Boolean): Optional | If set to True, padding is applied to the content area. This is the default value. If set to False, the content area has no padding. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<p>Examples</p><ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. |
