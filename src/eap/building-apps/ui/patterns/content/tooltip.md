---
tags: ui design, user experience
summary: Explore how to dynamically display tooltips in your applications using OutSystems Developer Cloud (ODC).
locale: en-us
guid: 33a42743-0e9c-44c6-b67d-363ec53dc01a
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A11799&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
content-type:
  - reference
  - procedure
---

# Tooltip

You can use the Tooltip UI Pattern to dynamically display informative text when a user hovers over, clicks, or taps an on-screen element.

![Screenshot of an example tooltip in action](images/tooltip-example.png "Example Tooltip")

**How to use the Tooltip UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Tooltip`.
  
    The Tooltip widget is displayed.

    ![Tooltip widget displayed in the ODC Studio Toolbox](images/tooltip-widget-ss.png "Tooltip Widget in ODC Studio")

1. From the Toolbox, drag the Tooltip widget into the Main Content area of your application's screen.

    ![Dragging the Tooltip widget into the Main Content area of an application screen](images/tooltip-drag-ss.png "Dragging Tooltip Widget to Screen")

    By default, the Tooltip widget contains Content and Tooltip placeholders.

1. Add your content to the placeholders. 
    
    In this example, we add a **Save** button to the Content placeholder and enter the tooltip text ``Save your details`` in the Tooltip placeholder.

    ![Adding a Save button to the Content placeholder and entering tooltip text](images/tooltip-content-ss.png "Adding Content to Tooltip Widget")
    
1. Select the **Save** button and add the relevant **On Click** event.

    ![Selecting the Save button to add an On Click event in the application](images/tooltip-onclick-ss.png "Adding OnClick Event to Save Button")

1. On the **Properties** tab, from the **Position** dropdown, select where you want the tooltip to appear. In this example we want the tooltip to appear on top of the **Save** button. You can also change the look and feel of the Tooltip by setting the (optional) properties.

    ![Setting optional properties for the Tooltip, including position and appearance](images/tooltip-properties-ss.png "Setting Optional Properties for Tooltip Widget")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Properties                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Position (Position Identifier): Optional | Set the tooltip's position, for example, top, right, or left.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| StartsOpen (Boolean): Optional           | If True, the tooltip is visible when the page is first loaded (without the need for the initial trigger). If False, the tooltip is not visible. This is the default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Trigger (TriggerIdentifier): Optional    | Set how the tooltip is triggered. By default, the tooltip is triggered by hovering over the element.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ExtendedClass (Text): Optional           | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the _myclass_ style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
