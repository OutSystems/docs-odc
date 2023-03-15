---
tags: 
summary: Submenu is used to create a menu contained within another menu.
locale: en-us
guid: 643d37e9-efa8-48a3-87ba-f409a1f04efa
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Submenu

You can use the Submenu UI Pattern to create a menu that is contained within another menu.

![Example submenu](<images/submenu-example-ss.png>)

**How to use the Submenu UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Submenu`.

    The Submenu widget is displayed.

    ![Submenu widget](<images/submenu-widget-ss.png>)

1. From the Toolbox, drag the Submenu widget into the Main Content area of your application's screen.

    ![Drag widget to screen](<images/submenu-dragwidget-ss.png>)

    By default, the Submenu widget contains a Menu placeholder and an Items placeholder that contains a link. You can add as many Items placeholders as required. In this example we add 3 more.

1. Add the relevant content to the Menu and Items placeholders.

    In this example, we add text to the Menu placeholder, and set the links in the Items placeholders to navigate to different pages in the app.

    ![Add content](<images/submenu-additems-ss.png>)

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
