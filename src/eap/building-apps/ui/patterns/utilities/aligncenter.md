---
tags: ui design, user experience
summary: Explore how to horizontally or vertically center content using the Align Center UI Pattern in OutSystems Developer Cloud (ODC).
locale: en-us
guid: 0902827b-4339-4965-b8c3-94a2a7825594
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A20614&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
  - apply
---

# Align Center

You can use Align Center UI Pattern to center content horizontally or vertically on the screen.

![Illustration of Align Center UI Pattern in use](images/aligncenter-1.png "Align Center UI Pattern")

**How to use the Align Center UI Pattern**

This example shows you how to center align a user's name and initials.

1. In ODC Studio, in the Toolbox, search for `Align Center`.

    The Align Center widget is displayed.

    ![Screenshot showing the Align Center widget in the ODC Studio Toolbox](images/aligncenter-2-ss.png "Align Center Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Align Center widget into the Main Content area of your application's screen.

    ![Screenshot of dragging the Align Center widget into the Main Content area](images/aligncenter-3-ss.png "Dragging Align Center Widget")

    By default, the Align Center widget contains a Content placeholder.

1. From the Toolbox, drag the User Avatar pattern into Content placeholder.

    ![Screenshot of User Avatar pattern being dragged into Align Center's Content placeholder](images/aligncenter-9-ss.png "User Avatar in Content Placeholder")

1. On the **Properties** tab, in the **Name** property, enter a name. In this example, we enter `Scott Richie`.

    ![Screenshot of the Properties tab with the Name property set to 'Scott Richie'](images/aligncenter-4-ss.png "Setting Name Property")

1. Add any other relevant content to the Content placeholder. In this example we add some text (Scott Richie) and an image.

    ![Screenshot showing additional content added to the Content placeholder](images/aligncenter-5-ss.png "Adding Content to Placeholder")

1. On the Align Center **Properties** tab, you can set the content's orientation (either vertical or horizontal).

    ![Screenshot of the Align Center Properties tab with content orientation options](images/aligncenter-6-ss.png "Content Orientation Setting")

After following these steps and publishing the app, you can test the pattern in your app.

**Without Align Center UI Pattern**

![Screenshot showing the app interface without the Align Center UI Pattern](images/aligncenter-7-ss.png "Without Align Center UI Pattern")

**With Align Center UI Pattern**

![Screenshot showing the app interface with the Align Center UI Pattern applied](images/aligncenter-8-ss.png "With Align Center UI Pattern")

## Properties

| Property                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IsHorizontal (Boolean): Optional | If True, content is displayed horizontally. This is the default. If False, the content is displayed vertically.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ExtendedClass (Text): Optional   | <p>Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.</p> <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
