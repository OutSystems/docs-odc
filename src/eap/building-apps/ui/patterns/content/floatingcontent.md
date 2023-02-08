---
tags: runtime-mobileandreactiveweb;  
summary: Floating Content displays a panel that floats over content (like a map or an image), docked to a screen corner or direction.
locale: en-us
guid: 12a78364-ee4e-4528-a0f7-239c9b0e31f9
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Floating Content

You can use the Floating Content UI Pattern to display content on top of other screen elements, such as a map with navigation instructions.

![](<images/floatingcontent-1-ss.png>)

**How to use the Floating Content UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Floating Content`.

    The Floating Content widget is displayed.

    ![](<images/floatingcontent-2-ss.png>)

1. From the Toolbox, drag the Floating Content widget into the Main Content area of your application's screen.

    In this example, the Main Content area of already contains an image of a map. 

    ![](<images/floatingcontent-3-ss.png?width=800>)

    By default, the Floating Content widget contains a Content placeholder.

1. Add the relevant content to the placeholder.

    In this example, we add a Search widget. 

    ![](<images/floatingcontent-4-ss.png?width=800>)

1. Select the Floating Content widget, and on the **Properties** tab, set the mandatory **Position** property. This defines where the widget is displayed. You can customize the Section's look and feel by setting any of the (optional) properties.

    ![](<images/floatingcontent-5-ss.png?width=800>)

After following these steps and publishing the app, you can test the pattern in your app. 

## Properties

### Floating Content

| **Property**                              | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Position (Position Identifier): Mandatory | The position the floating content is displayed on screen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| UseFullHeight (Boolean): Optional         | If True, the widget takes up the full height of the screen. If False, the widget doesn't take up the full height of the screen. This is the default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| UseFullWidth (Boolean): Optional          | If True, the widget takes up the full width of the screen. If False, the widget doesn't take up the full width of the screen. This is the default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| UseMargin (Boolean): Optional             | If True, a margin is applied to the widget. This is the default. If False, there is no margin applied to the widget.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ExtendedClass (Text): Optional            | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |
