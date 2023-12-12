---
tags:
summary: Floating Actions is a UI pattern that displays an action that floats in the bottom right corner of the screen.
locale: en-us
guid: a246e3bb-4c75-4e3b-8a53-eb45a08996ae
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A15421&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---
# Floating Actions

You can use the Floating Actions UI Pattern to display an action that floats in the bottom right corner of the screen, providing access to a set of additional actions.

Use the Floating Action UI Pattern to show the primary action on a screen. You can choose actions such as create, share, explore, but it is advised to avoid actions such as delete, archive, or an alert. Exclude limited actions such as cut-and-paste text or actions that should be in a toolbar.

**How to use the Floating Actions UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Floating Actions`.

    The Floating Actions widget is displayed.

    ![Screenshot of the Floating Actions widget in the ODC Studio Toolbox](images/floatingactions-1-ss.png "Floating Actions Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Floating Actions widget into the Main Content area of your application's screen.

    ![Dragging the Floating Actions widget into the main content area of an application screen](images/floatingactions-2-ss.png "Dragging Floating Actions Widget into Main Content Area")

    By default, the Floating Actions widget contains a Button placeholder (with an icon) and an Items placeholder with 3 Floating Actions Item widgets (each containing a Label and Item placeholder). You can add or delete the Floating Actions Item widgets as required.

1. Add the relevant content to the placeholders.

    In this example, we add text to the Label placeholders and linked icons to the Item placeholders.  

    ![Adding text and icons to the placeholders in the Floating Actions widget](images/floatingactions-3-ss.png "Adding Content to Floating Actions Placeholders")

1. Select the Floating Actions widget, and on the **Properties** tab, set the relevant properties, for example, whether the actions are expanded and visible when the page loads.

    ![Setting properties of the Floating Actions widget in the Properties tab](images/floatingactions-4-ss.png "Setting Properties of Floating Actions Widget")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

### Floating Actions

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IsExpanded (Boolean): Optional | If True, the floating actions are expanded and immediately visible on screen. If False, the floating actions are not visible. This is the default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| IsHover (Boolean): Optional    | If True, the floating actions are triggered by hovering the mouse pointer over them. If False, the floating actions are not triggered by hovering the mouse pointer over them. This is the default.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |

### Floating Actions Item

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |
