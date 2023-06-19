---
summary: Flip Content prioritizes information display, keeping the interface uncluttered.
tags: 
locale: en-us
guid: d87a061c-83e2-4b7f-b820-4e7f70267a38
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A10847&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Flip Content

You can use the Flip Content UI Pattern to display information that when, for example, is clicked, flips and displays different information.

![](<images/flipcontent-example.gif?width=500>)

**How to use the Flip content UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Flip Content`.

    The Flip Content widget is displayed.

    ![Flip Content widget](<images/flipcontent-widget-ss.png>)

1. From the Toolbox, drag the Flip Content widget into the Main Content area of your application's screen.

    ![Drag widget to screen](<images/flipcontent-dragwidget-ss.png>)

    By default, the Flip Content widget contains **CardFront** and **CardBack** placeholders.

1. Add the required content for the front and back placeholders inside the Flip Content widget.

    In this example, we add images by dragging the Image widget into the **CardFront** and **CardBack** placeholders and from the **Image** dropdown, selecting an image from the sample OutSystems UI images.

    ![Add content to widget](<images/flipcontent-addimage-ss.png>)

1. On the **Properties** tab, you can customize the Flip Content's look and feel by setting any of the (optional) properties.

    ![Properties](<images/flipcontent-properties-ss.png>)

## Properties
| Property                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| StartsFlipped (Boolean): Optional | If True, the CardFront content is displayed first before flipping. If False, the CardBack content is displayed first before flipping. This is the default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| FlipOnClick (Boolean): Optional   | If True, the flip event is triggered when the Flip Content card (front or back) is clicked. This is the default. If False, you can define the action that triggers the flip event.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ExtendedClass (Text): Optional    | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
