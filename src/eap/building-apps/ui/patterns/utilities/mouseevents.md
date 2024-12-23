---
tags: ui development, interface design
summary: Explore how to implement precise element selection using the Mouse Events UI Pattern in OutSystems Developer Cloud (ODC).
locale: en-us
guid: c9b283f3-79d1-4ac0-93a4-1f1a7a2c50e7
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A21331&t=ZwHw8hXeFhwYsO5V-1
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
---

# Mouse Events

You can use the Mouse Events UI Pattern when the user needs to select elements on the interface with high precision.

## How to Use the Mouse Events UI Pattern

The following example shows how you can use the Mouse Events UI pattern to display the distance the mouse is dragged left and right across the screen.

1. In ODC Studio, in the Toolbox, search for `Mouse Events`.

    The Mouse Events widget is displayed.

    ![Screenshot of the Mouse Events widget in the ODC Studio Toolbox](images/mouseevents-1-ss.png "Mouse Events Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Mouse Events widget into the Main Content area of your application's screen.

    ![Dragging the Mouse Events widget into the Main Content area of an application screen](images/mouseevents-2-ss.png "Dragging Mouse Events Widget to Main Content Area")

1. From the Toolbox, drag the Center Content widget into the Main Content area of your screen.
 
    ![Dragging the Center Content widget into the Main Content area of an application screen](images/mouseevents-3-ss.png "Center Content Widget in Main Content Area")

1. On the **Properties** tab, enter a name in the **Name** property. In this example, we enter `card`.

    ![Entering a name for the Mouse Events widget in the Properties tab](images/mouseevents-4-ss.png "Naming the Mouse Events Widget")

1. Add 2 local variables by right-clicking on your screen name and selecting **Add Local Variable**.

    In this example we call name them **Drag** and **Distance**. Both local variables are of data type text.

    ![Adding local variables named Drag and Distance to the application screen](images/mouseevents-5-ss.png "Adding Local Variables")

1. Add the relevant content to the Center Content widget placeholders. 

   In this example, we add text and 2 expressions to the Center placeholder, and text to the Bottom placeholder. 

   ![Adding text and expressions to the Center Content widget placeholders](images/mouseevents-6-ss.png "Content in Center Content Widget")

   Each of the expressions are set to the local variables respectively (**Drag** and **Distance**). 

   ![Setting expressions to local variables Drag and Distance in the Center Content widget](images/mouseevents-7-ss.png "Expressions Set to Local Variables")

1. Add a client action by right-clicking your screen name and selecting **Add Client Action**. 

1. Enter a name for the client action. In this example, we enter `MouseEventsMove`.

   ![Entering a name for the MouseEventsMove client action](images/mouseevents-8-ss.png "Creating MouseEventsMove Client Action")

1. Add 2 input parameters by right-clicking the client action and selecting **Add Input Parameter**.

    In this example, we add the **OffsetX** and **OffsetY** input parameters and set their data type to decimal.

    ![Adding OffsetX and OffsetY input parameters to the MouseEventsMove client action](images/mouseevents-9-ss.png "Adding Input Parameters to Client Action")

1. Add the relevant logic to the client action. In this example, we add the following:

    ![Adding logic to the MouseEventsMove client action](images/mouseevents-10-ss.png "Logic for MouseEventsMove Client Action")

1. Select the Mouse Events widget and set the **WidgetId**, **PreventDefaults**, and the **Handler** properties. 

    In this example, the **WidgetId** is set to **card.Id**, the **PreventDefaults** to **False**, **OfFsetX** to **OffsetX**, and **OffsetY** to **OffsetY**.

    ![Setting WidgetId, PreventDefaults, and Handler properties for the Mouse Events widget](images/mouseevents-11-ss.png "Configuring Mouse Events Widget Properties")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| **Property**                        | **Description**                                                                                                                                                      |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WidgetId (Text): Mandatory          | The element that responds to the mouse event you configure.                                                                                                          |
| PreventDefaults (Boolean): Optional | If True, events propagation to the screen and other widgets is stopped. This is the default. If False, event propagation to the screen and other widgets is enabled. |
