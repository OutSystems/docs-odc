---
tags: 
summary: Use the Margin Container and easily add symmetrical padding around a container.
locale: en-us
guid: 7e38da14-e0fb-42d7-b677-5b18818c788f
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A21157&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Margin Container

You can use the Margin Container UI Pattern to add symmetrical padding around a container.

![Screenshot of the Margin Container UI Pattern in ODC Studio](images/margincontainer-1-ss.png "Margin Container UI Pattern")

**How to use the Margin Container UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Margin Container`.

    The Margin Container widget is displayed.

    ![Display of the Margin Container widget in the ODC Studio Toolbox](images/margincontainer-2-ss.png "Margin Container Widget in Toolbox")

1. From the Toolbox, drag the Margin Container widget into the Main Content area of your application's screen.

    ![Dragging the Margin Container widget into the Main Content area in ODC Studio](images/margincontainer-3-ss.png "Dragging Margin Container Widget")

    You can add as many Margin Container widgets as you want. In this example, we add 2.

1. Add the relevant content to the Margin Container placeholder.

    In this example we add an image widget to each of the placeholders and on the **Properties** tab, import an image using the **Image** dropdown.

    ![Adding an image widget to the Margin Container placeholders in ODC Studio](images/margincontainer-4-ss.png "Adding Content to Margin Container")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtendedClass (Text): Optional | <p>Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.</p> <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
