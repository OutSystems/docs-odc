---
tags: ui design patterns, mobile app development, ui components, outsystems ui, user experience
summary: OutSystems Developer Cloud (ODC) enables the use of the Bottom Sheet UI pattern in mobile apps.
locale: en-us
guid: b45a2a54-8dbe-44f4-8a96-63e5e26d5ae0
app_type: mobile apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A13167&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - ui designers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
  - remember
topic:
  - add-widget-ui-pattern
---

# Bottom Sheet

<div class="info" markdown="1">

Applies to Mobile Apps only.

</div>

<div class="info" markdown="1">

Applies to the OutSystems UI framework only.

</div>

You can use the Bottom Sheet Pattern to display additional information. This additional information is displayed at the bottom of the screen and supports the user's understanding of the main content.

**How to use the Bottom Sheet UI Pattern**

In this example, we create a button that opens and closes the Bottom Sheet widget.

1. In ODC Studio, in the Toolbox, search for `Bottom Sheet`.

    The Bottom Sheet widget is displayed.

    ![Screenshot showing the search for the Bottom Sheet widget in ODC Studio Toolbox](images/bottomsheet-widget-ss.png "Bottom Sheet Widget Search")

1. From the Toolbox, drag the Bottom Sheet widget into the Main Content area of your application's screen and on the **Properties** tab, in the **Name** field, enter a name for the Bottom Sheet widget.

    ![Screenshot of dragging the Bottom Sheet widget into the Main Content area in ODC Studio](images/bottomsheet-dragwidget-ss.png "Dragging Bottom Sheet Widget")

    By default, the Bottom Sheet widget contains a **TopBar** and a **Content** placeholder.

    ![Screenshot of the Bottom Sheet widget with TopBar and Content placeholders in ODC Studio](images/bottomsheet-placeholder-ss.png "Bottom Sheet Widget Placeholder")

1. Add the relevant content to the TopBar and Content placeholders.

    ![Screenshot showing the addition of text, icon, and a close button to the Bottom Sheet widget placeholders](images/bottomsheet-content-ss.png "Adding Content to Bottom Sheet widget")

    In this example, we add text, an icon, and a button to close the widget.

1. To close the bottom sheet, select the **Close** button, and on the **Properties** tab, from the **On Click** dropdown, select **New Client Action**.  

    ![Screenshot of the Properties tab showing the selection of a New Client Action for the Close button](images/bottomsheet-onclick-ss.png "Bottom Sheet Close Button Action")

1. Drag a **Run Client Action** to the client action, add from the **Select Action** popup, navigate to the **BottomSheetClose** action and click **Select**.

    ![Screenshot depicting the process of adding a BottomSheetClose action in ODC Studio](images/bottomsheet-close-ss.png "Bottom Sheet Close Action")

1. On the **Properties** tab, set the **WidgetId** to **BottomSheet.Id**.

    ![Screenshot of the Properties tab with the WidgetId field set to BottomSheet.Id](images/bottomsheet-id-ss.png "Setting WidgetId for Bottom Sheet widget")

1. In this example we create a button to open the Bottom sheet by dragging the **Button** widget just below the **Bottom Sheet** widget and on the **Properties** tab, in the **Text** field, enter the text you want to appear on the button.

    ![Screenshot showing a new button added below the Bottom Sheet widget to open it](images/bottomsheet-openbutton-ss.png "Adding Open Button for Bottom Sheet widget")

1. Select the button, and on the **Properties** tab, from the **On Click** dropdown, select **New Client Action**.

1. Drag a **Run Client Action** to the client action, add from the **Select Action** popup, navigate to the **BottomSheetOpen** action and click **Select**.

    ![Screenshot illustrating the addition of a BottomSheetOpen action in ODC Studio](images/bottomsheet-openaction-ss.png "Bottom Sheet widget Open Action")

1. On the **Properties** tab, set the **WidgetId** to **BottomSheet.Id**.

1. You can customize the Bottom Sheet by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties.

    ![Screenshot of the Properties tab showing the customization options for the Bottom Sheet pattern](images/bottomsheet-properties-ss.png "Customizing Bottom Sheet widget Properties")

After following these steps and publishing the app, you can test the pattern in your app.

![Image of the Bottom Sheet pattern as it appears in the published mobile app](images/bottomsheet-resultapp.png "Bottom Sheet in Published App")

## Properties

| Property | Description |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Shape (Shape Identifier): Optional | Set the Bottom Sheet shape. The predefined options are SoftRounded, Rounded, and Sharp. For example, Entities.Shape.Rounded inherits the rounded style. This is the default shape. |
| ShowHandler (Boolean): Optional | Set to True to display a handler above the Bottom Sheet. The default value is True. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <br/>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |
