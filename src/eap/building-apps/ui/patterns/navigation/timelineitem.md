---
tags: ui patterns, timeline implementation
summary: OutSystems Developer Cloud (ODC) features the Timeline Item UI Pattern for displaying events in chronological order.
locale: en-us
guid: e420ff2a-afcd-4ca6-9d65-9e42ee8d5213
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A18218&t=ZwHw8hXeFhwYsO5V-1
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
---

# Timeline Item

You can use the Timeline Item UI Pattern to show related events in a chronological order, such as a user's upcoming, current, and past activities.

![Screenshot of the initial state of Timeline Item UI Pattern in ODC Studio](images/timelineitem-1-ss.png "Initial Timeline Item UI Pattern")

**How to use the Timeline Item UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Timeline Item`.

    The Timeline Item widget is displayed.

    ![Display of the Timeline Item widget within the ODC Studio Toolbox](images/timelineitem-2-ss.png "Timeline Item Widget in Toolbox")

1. From the Toolbox, drag the Timeline widget onto your application's screen.

    ![Process of dragging the Timeline widget onto the application screen in ODC Studio](images/timelineitem-3-ss.png "Dragging Timeline Widget to Screen")

    By default, the Timeline Item widget contains Left, Icon, Title, Content, and Right placeholders. You can add as many Timeline Item widgets as required.

    In this example we add two more Timeline Item widgets.

1. Set the required content in each of the placeholders.

    In this example we add some icons and text.

    ![Example of adding icons and text to Timeline Item placeholders in ODC Studio](images/timelineitem-4-ss.png "Configuring Timeline Item Placeholders")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

### Timeline Item

| Property                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IsActive (Boolean): Optional       | If True, the item is set to active. If False, the item is inactive. This is the default.<br/><br/>**NOTE**: This property is deprecated. It renders an element as being active in mobile applications based on the OutSystems UI Base Theme prior to version 2.4.0. It has no effect in applications created after OutSystems UI version 2.4.0.                                                                                                                                                                                                                                                                                                |
| Color (Color Identifier): Optional | Icon background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - The icon background color is the color you chose when creating the app (default value).</li><li>_Entities.Color.Red_ - The icon background color is red.</li></ul></p>                                                                                                                                                                                                                                                                                               |
| ExtendedClass (Text): Optional     | <p>Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.</p> <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
