---
tags: user interaction, mobile app development
summary: Learn how to implement swipe gestures to manipulate data in your app using the Swipe Events UI pattern in OutSystems Developer Cloud (ODC).
locale: en-us
guid: b8415514-3f04-45f1-a26c-0ef4049b4487
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A21622&t=ZwHw8hXeFhwYsO5V-1
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

# Swipe Events

<div class="info" markdown="1">

Applies to the OutSystems UI framework only.

</div>

You can use the Swipe Events UI Pattern to enable swiping on a specific widget.

## How to use the Swipe Events UI Pattern

The following example shows how you can use the Swipe Events UI pattern to increase (swipe right) and decrease (swipe left) a number.

1. In ODC Studio, in the Toolbox, search for  `Swipe Events`.

    The Swipe Events widget is displayed.

    ![Screenshot of the Swipe Events widget in the ODC Studio Toolbox](images/swipeevents-1-ss.png "Swipe Events Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Swipe Events widget into the Main Content area of your application's screen.

    ![Dragging the Swipe Events widget into the main content area of the application screen](images/swipeevents-2-ss.png "Dragging Swipe Events Widget into Main Content Area")

1. Add a local variable by right-clicking on your screen name and selecting **Add Local Variable**.

    ![Adding a new local variable by right-clicking on the screen name in ODC Studio](images/swipeevents-3-ss.png "Adding a Local Variable in ODC Studio")

1. Enter a name, a data type, and a default value for the new variable. In this example, we enter `Number`, `Integer`, and `0` repsectively.

    ![Entering details for a new local variable with name 'Number', type 'Integer', and default value '0'](images/swipeevents-4-ss.png "New Local Variable Details")

1. Drag the new variable into the Main Content area of your application's screen.

    ![Dragging the new variable into the main content area of the application screen](images/swipeevents-5-ss.png "Placing New Variable on Application Screen")

1. From the Toolbox, drag the Container widget into the Main Content area of your application's screen and on the **Properties** tab, enter a name. In this example we enter `SwipeContainer`. We also add the text `Swipe left or right` inside the Container widget.

    ![Container widget named 'SwipeContainer' with text 'Swipe left or right' added to the main content area](images/swipeevents-6-ss.png "Adding Container Widget with Swipe Instructions")

1. From the **Widget Tree**, select the Swipe Events widget, and on the **Properties** tab, from the **WidgetId** drop-down, select the Id of the container you just created. In this example, we select **SwipeContainer.Id**.

    ![Selecting SwipeContainer.Id from the WidgetId drop-down in the properties of the Swipe Events widget](images/swipeevents-7-ss.png "Linking Swipe Events Widget to Container")

1. To set the action for when the user swipes left, remaining on the **Properties** tab, from the **SwipeLeft Handler** drop-down, select **New Client Action**.

    ![Choosing 'New Client Action' from the SwipeLeft Handler drop-down in the Swipe Events widget properties](images/swipeevents-8-ss.png "Setting Swipe Left Action in Properties")

1. Assign the relevant logic you want the swipe left action to perform. In this example, we want the number to decrease by 1 every time the user swipes left. To do this, we drag an Assign onto the client action, set the **Variable** to **Number**, and enter ``Number - 1`` for the **Value**.

    ![Assigning logic to decrease the number variable by 1 on swipe left action in the client action flow](images/swipeevents-9-ss.png "Configuring Swipe Left Logic")

1. Repeat steps 8 and 9 for the **SwipeRightHandler** and so that the number increases when the user swipes right, enter `Number + 1`.

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| **Property** | **Description** |
| --- | --- |
| WidgetId (Text): Mandatory | Element that's swipeable. |
