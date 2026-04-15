---
tags: mobile apps, user interface components, outsystems patterns
summary: Explore the Stacked Cards UI Pattern in OutSystems Developer Cloud (ODC) for creating swipeable, multi-directional event-triggering cards.
locale: en-us
guid: 30866b44-9a14-45a8-bbbd-ee11cc898d5f
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A17757&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
  - apply
topic:
  - add-widget-ui-pattern
---

# Stacked Cards

<div class="info" markdown="1">

Applies to the OutSystems UI framework only.

</div>

You can use Stacked Cards UI Pattern to add swipeable cards that can be dragged in multiple directions triggering events, such as deny, approve, and archive. This pattern is ideal when you want to individually scan multiple cards.

![Example of Stacked Cards UI Pattern in a mobile app interface](images/stackedcards-1.png "Stacked Cards UI Pattern")

## How to use the Stacked Cards Pattern

1. In ODC Studio, in the Toolbox, search for  `Stacked Cards`.

    The Stacked Cards widget is displayed.

    ![Screenshot showing the Stacked Cards widget in the ODC Studio Toolbox](images/stackedcards-2-ss.png "Stacked Cards Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Swipe Events widget into the Main Content area of your application's screen.

    ![Screenshot of dragging the Swipe Events widget into the Main Content area in ODC Studio](images/stackedcards-3-ss.png "Adding Swipe Events Widget")

    By default, the Stacked Cards widget contains a List, Overlay Top, Overlay Right, and Overlay Left placeholders.

1. Add content to the List placeholder. In this example, from the **Data** tab, we drag a list of Employees into the List placeholder.

    ![Screenshot showing the addition of a list of Employees to the List placeholder in Stacked Cards](images/stackedcards-4-ss.png "Adding Content to List Placeholder")

    The **GetEmployees** aggregate is automatically created.

    ![Screenshot of the GetEmployees aggregate being automatically created in ODC Studio](images/stackedcards-5-ss.png "Automatic Creation of GetEmployees Aggregate")

1. From the Toolbox, drag the Icon widget into the OverlayTop placeholder, and from the Pick an Icon editor, choose an icon. Click **Select**.

    ![Screenshot of adding an icon to the OverlayTop placeholder in the Stacked Cards pattern](images/stackedcards-6-ss.png "Adding Icon to OverlayTop Placeholder")

1. Repeat step 4 for the OverlayRight and OverlayLeft placeholders.

    ![Screenshot of icons added to OverlayRight and OverlayLeft placeholders in Stacked Cards](images/stackedcards-7-ss.png "Icons for OverlayRight and OverlayLeft Placeholders")

1. To create a swipe action for the OverlayLeft placeholder, select the pattern, and from the OnLeftSwipe **Handler** drop-down, select **New Client Action**.

    ![Screenshot of selecting a new client action for the OnLeftSwipe handler in Stacked Cards](images/stackedcards-8-ss.png "Creating Swipe Action for OverlayLeft")

1. From the Toolbox, drag a **Run Server Action** onto the client action, and from the **Select Action** editor, navigate to the action you want the swipe left action to perform. In this example, we use the **DeleteEmployee** action.

    ![Screenshot of dragging a Run Server Action onto the client action for swipe left in Stacked Cards](images/stackedcards-9-ss.png "Configuring Swipe Left Action")

1. From the **Id** drop-down, select the action Id. In this example, the Id is the currently selected employee. This means, that when the user swipes left, the currently selected user is deleted form the list of employees.

   ![Screenshot of selecting the action Id for the swipe left action in Stacked Cards](images/stackedcards-10-ss.png "Selecting Action ID for Swipe Left")

1. Repeat step 7 for the OverlayTop (swipe up) and OverLayRight (swipe right) placeholders.

1. From the **Properties** tab, you can change the Stacked Card's look and feel by setting the (optional) properties.

   ![Screenshot of the Properties tab where Stacked Card's look and feel can be changed](images/stackedcards-11-ss.png "Stacked Cards Pattern Properties Settings")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                                                   | Description                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| StackedOptions (StackedCardsPosition Identifier): Optional | Change stacked cards view from bottom, top, or none.  <p>Examples <ul><li>Entities.StackedCardsPosition.Bottom - The stacked cards are positioned on the bottom. This is the default. </li><li>Entities.StackedCardsPosition.Top - The stacked cards are positioned on top. </li></ul></p> |
| Rotate (Boolean): Optional                                 | If True, the rotation for each move on the stacked cards is activated. This is the default. If False, each move is not activated.                                                                                                                                                          |
| Items (Integer): Optional                                  | Number of visible elements when the StackedOptions property is set to bottom or top. <p>Examples <ul><li>Blank - 5 elements are visible. This is the default. </li><li>3 - 3 elements are visible. </li></ul></p>                                                                          |
| ElementsMargin                                             | Define the distance between each element when the StackedOptions property is set to bottom or top. <p>Examples <ul><li>Blank - 5 elements are visible. This is the default. </li><li>3 - 3 elements are visible. </li></ul></p>                                                            |
| UseOverlays (Boolean): Optional                            | If True, overlays for swipe elements are enabled. This is the default. If False, the overlays are disabled.                                                                                                                                                                                |
  
## Compatibility with other patterns

Avoid using the Stacked Cards Pattern inside patterns with swipe events / touch events, like [Tabs](../navigation/tabs.md) or [Carousel](carousel.md).
