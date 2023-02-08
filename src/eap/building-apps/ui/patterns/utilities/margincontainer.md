---
tags: runtime-mobileandreactiveweb;  
summary: Use the Margin Container and easily add symmetrical padding around a container.
locale: en-us
guid: 7e38da14-e0fb-42d7-b677-5b18818c788f
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Margin Container

You can use the Margin Container UI Pattern to add symmetrical padding around a container.

![](<images/margincontainer-1-ss.png>)

**How to use the Margin Container UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Margin Container`.

    The Margin Container widget is displayed.

    ![](<images/margincontainer-2-ss.png>)

1. From the Toolbox, drag the Margin Container widget into the Main Content area of your application's screen.

    ![](<images/margincontainer-3-ss.png>)

    You can add as many Margin Container widgets as you want. In this example, we add 2.

1. Add the relevant content to the Margin Container placeholder.

    In this example we add an image widget to each of the placeholders and on the **Properties** tab, import an image using the **Image** dropdown.

    ![](<images/margincontainer-4-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtendedClass (Text): Optional | <p>Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.</p> <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
