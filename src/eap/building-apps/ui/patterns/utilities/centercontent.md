---
tags: runtime-mobileandreactiveweb;  
summary: Use the Center Content pattern to align the content to the center of its container.
locale: en-us
guid: a4890513-8edb-4155-8075-a2e68740e6f0
app_type: mobile apps, reactive web apps
---

# Center Content

You can use the Center Content UI Pattern to vertically align content to the center of its container.

![](<images/centercontent-1.png>)

**How to use the Center Content UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Center Content`.

    The Center Content widget is displayed.

    ![](<images/centercontent-2-ss.png>)

1. From the Toolbox, drag the Center Content widget into the Main Content area of your application's screen.

    ![](<images/centercontent-3-ss.png>)

    By default, the Center Content widget contains Top, Center, and Bottom placeholders.

1. Add the relevant content to each of the placeholders. In this example we add some images and text.

    ![](<images/centercontent-4-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtendedClass (Text): Optional | <p>Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.</p> <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
