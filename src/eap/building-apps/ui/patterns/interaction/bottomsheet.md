---
tags: 
summary: 
locale: en-us
guid: b45a2a54-8dbe-44f4-8a96-63e5e26d5ae0
app_type: mobile apps
platform-version: odc
---

# Bottom Sheet

<div class="info" markdown="1">

Applies to Mobile Apps only.

</div>

You can use the Bottom Sheet Pattern to display additional information. This additional information is displayed at the bottom of the screen and supports the user's understanding of the main content.

**How to use the Bottom Sheet UI Pattern**

In this example, we create a button that opens and closes the Bottom Sheet widget.

1. In ODC Studio, in the Toolbox, search for `Bottom Sheet`.

    The Bottom Sheet widget is displayed.

    ![Search for the Bottom Sheet widget](<images/bottomsheet-widget-ss.png>)

1. From the Toolbox, drag the Bottom Sheet widget into the Main Content area of your application's screen and on the **Properties** tab, in the **Name** field, enter a name for the Bottom Sheet widget.

    ![Search for the Bottom Sheet widget](<images/bottomsheet-dragwidget-ss.png>)

    By default, the Bottom Sheet widget contains a **TopBar** and a **Content** placeholder.

    ![The Bottom Sheet widget placeholder](<images/bottomsheet-placeholder-ss.png>)

1. Add the relevant content to the TopBar and Content placeholders. 

    ![Add content to Bottom Sheet placeholders](<images/bottomsheet-content-ss.png>)

    In this example, we add text, an icon, and a button to close the widget.

1. To close the bottom sheet, select the **Close** button, and on the **Properties** tab, from the **On Click** dropdown, select **New Client Action**.  

    ![New client action for close button](<images/bottomsheet-onclick-ss.png>)

1. Drag a **Run Client Action** to the client action, add from the **Select Action** popup, navigate to the **BottomSheetClose** action and click **Select**.

    ![Add BottomSheetClose action](<images/bottomsheet-close-ss.png>)

1. On the **Properties** tab, set the **WidgetId** to **BottomSheet.Id**.

    ![Set the widgetId](<images/bottomsheet-id-ss.png>)

1. In this example we create a button to open the Bottom sheet by dragging the **Button** widget just below the **Bottom Sheet** widget and on the **Properties** tab, in the **Text** field, enter the text you want to appear on the button.

    ![Add an Open button](<images/bottomsheet-openbutton-ss.png>)

1. Select the button, and on the **Properties** tab, from the **On Click** dropdown, select **New Client Action**.

1. Drag a **Run Client Action** to the client action, add from the **Select Action** popup, navigate to the **BottomSheetOpen** action and click **Select**.

    ![Add BottomSheetOpen action](<images/bottomsheet-openaction-ss.png>)

1. On the **Properties** tab, set the **WidgetId** to **BottomSheet.Id**.

1. You can customize the Bottom Sheet by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties.

    ![Set relevant properties](<images/bottomsheet-properties-ss.png>)

After following these steps and publishing the app, you can test the pattern in your app. 

![Set relevant properties](<images/bottomsheet-resultapp.png>)

## Properties

| Property                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shape (Shape Identifier): Optional | Set the Bottom Sheet shape. The predefined options are SoftRounded, Rounded, and Sharp. For example, Entities.Shape.Rounded inherits the rounded style. This is the default shape.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ShowHandler (Boolean): Optional    | Set to True to display a handler above the Bottom Sheet. The default value is True.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ExtendedClass (Text): Optional     | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <br/>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |
