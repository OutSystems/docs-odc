---
tags: ui design, design systems, user experience, application development, outsystems
summary: Learn how to implement a submenu within an application using the Submenu UI Pattern in OutSystems Developer Cloud (ODC).
locale: en-us
guid: 643d37e9-efa8-48a3-87ba-f409a1f04efa
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A18027&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - odc studio
content-type:
  - procedure
  - reference
---

# Submenu

You can use the Submenu UI Pattern to create a menu that is contained within another menu.

![Screenshot of an example submenu pattern in a mobile app interface](images/submenu-example-ss.png "Example Submenu Pattern")

**How to use the Submenu UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Submenu`.

    The Submenu widget is displayed.

    ![Screenshot showing the Submenu widget in the ODC Studio Toolbox](images/submenu-widget-ss.png "Submenu Widget in Toolbox")

1. From the Toolbox, drag the Submenu widget into the Main Content area of your application's screen.

    ![Screenshot illustrating the process of dragging the Submenu widget into the Main Content area of an application screen](images/submenu-dragwidget-ss.png "Dragging Submenu Widget to Screen")

    By default, the Submenu widget contains a Menu placeholder and an Items placeholder that contains a link. You can add as many Items placeholders as required. In this example we add 3 more.

1. Add the relevant content to the Menu and Items placeholders.

    In this example, we add text to the Menu placeholder, and set the links in the Items placeholders to navigate to different pages in the app.

    ![Screenshot demonstrating how to add text and links to the Menu and Items placeholders in the Submenu widget](images/submenu-additems-ss.png "Adding Content to Submenu Widget")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
