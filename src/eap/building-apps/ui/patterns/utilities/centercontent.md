---
tags: ui design, ui patterns
summary: OutSystems Developer Cloud (ODC) features the Center Content UI Pattern for vertically aligning content within an application's container.
locale: en-us
guid: a4890513-8edb-4155-8075-a2e68740e6f0
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A21058&t=ZwHw8hXeFhwYsO5V-1
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
topic:
  - add-widget-ui-pattern
---

# Center Content

<div class="info" markdown="1">

Applies to the OutSystems UI framework only.

</div>

You can use the Center Content UI Pattern to vertically align content to the center of its container.

![Illustration of the Center Content UI Pattern in use](images/centercontent-1.png "Center Content UI Pattern")

**How to use the Center Content UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Center Content`.

    The Center Content widget is displayed.

    ![Screenshot showing the Center Content widget in the ODC Studio Toolbox](images/centercontent-2-ss.png "Center Content Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Center Content widget into the Main Content area of your application's screen.

    ![Screenshot of dragging the Center Content widget into the Main Content area](images/centercontent-3-ss.png "Dragging Center Content Widget")

    By default, the Center Content widget contains Top, Center, and Bottom placeholders.

1. Add the relevant content to each of the placeholders. In this example we add some images and text.

    ![Screenshot of the Center Content widget with Top, Center, and Bottom placeholders filled with content](images/centercontent-4-ss.png "Center Content Widget with Placeholders")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ExtendedClass (Text): Optional | <p>Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.</p> <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
