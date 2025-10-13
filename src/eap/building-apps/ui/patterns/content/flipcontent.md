---
summary: OutSystems Developer Cloud (ODC) features the Flip Content UI Pattern for interactive content display in applications.
tags: ui design, user experience, custom widgets, application development, interactive content
locale: en-us
guid: d87a061c-83e2-4b7f-b820-4e7f70267a38
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A10847&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
  - remember
topic:
  - add-widget-ui-pattern
---

# Flip Content

You can use the Flip Content UI Pattern to display information that when, for example, is clicked, flips and displays different information.

<iframe src="https://player.vimeo.com/video/973090281" width="750" height="296" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Video showing how the Flip Content UI pattern in action, showing the front and back content flipping.</iframe>

**How to use the Flip content UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Flip Content`.

    The Flip Content widget is displayed.

    ![Screenshot of the Flip Content widget in ODC Studio's Toolbox](images/flipcontent-widget-ss.png "Flip Content Widget in ODC Studio")

1. From the Toolbox, drag the Flip Content widget into the Main Content area of your application's screen.

    ![Screenshot showing the process of dragging the Flip Content widget into the Main Content area](images/flipcontent-dragwidget-ss.png "Dragging Flip Content Widget to Screen")

    By default, the Flip Content widget contains **CardFront** and **CardBack** placeholders.

1. Add the required content for the front and back placeholders inside the Flip Content widget.

    In this example, we add images by dragging the Image widget into the **CardFront** and **CardBack** placeholders and from the **Image** dropdown, selecting an image from the sample OutSystems UI images.

    ![Screenshot demonstrating how to add images to the CardFront and CardBack placeholders in the Flip Content widget](images/flipcontent-addimage-ss.png "Adding Content to Flip Content Widget")

1. On the **Properties** tab, you can customize the Flip Content's look and feel by setting any of the (optional) properties.

    ![Screenshot of the Properties tab for customizing the Flip Content's appearance](images/flipcontent-properties-ss.png "Flip Content Properties")

## Properties

| Property                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| StartsFlipped (Boolean): Optional | If True, the CardFront content is displayed first before flipping. If False, the CardBack content is displayed first before flipping. This is the default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| FlipOnClick (Boolean): Optional   | If True, the flip event is triggered when the Flip Content card (front or back) is clicked. This is the default. If False, you can define the action that triggers the flip event.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ExtendedClass (Text): Optional    | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
