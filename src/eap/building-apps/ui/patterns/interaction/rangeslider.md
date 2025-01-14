---
tags: ui components, integration techniques
summary: OutSystems Developer Cloud (ODC) supports the Range Slider UI Pattern, enabling users to select values within a defined range.
locale: en-us
guid: 3004b9a7-ba25-42d8-8430-703d2be50470
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A16464&t=ZwHw8hXeFhwYsO5V-1
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
---

# Range Slider

You can use the Range Slider UI Pattern to allow users select a single value between two range values. This pattern enables the adjustment of content within a predetermined range. Moving the slider along the track increases or decreases the value.  

![Overview of the Range Slider UI Pattern in a mobile app interface](images/rangeslider-overview.png "Range Slider Overview")

<div class="info" markdown="1">

The Range Slider Pattern is based on the [noUiSlider library](https://refreshless.com/nouislider/) (v15.5.1). For more information about the Range Slider’s behaviors and extensibility methods, see the provider’s documentation.

</div>

## How to use the Range Slider UI Pattern

In this example, we create a Range Slider that allows the user select the number of months it will take them to pay back a loan.

1. In ODC Studio, in the Toolbox, search for `Range Slider`.

    The Range Slider widget is displayed.

    ![Screenshot of the Range Slider widget in the ODC Studio Toolbox](images/rangeslider-widget-ss.png "Range Slider Widget in Toolbox")

1. From the Toolbox, drag the Range Slider widget into the Main Content area of your application's screen.

    ![Dragging the Range Slider widget into the Main Content area of an application screen](images/rangeslider-dragwidget-ss.png "Dragging Range Slider Widget")

1. On the **Properties** tab, enter the mandatory minimum, maximum, and starting values. 
    
    In this example, we add static values.

    ![Entering mandatory minimum, maximum, and starting values for the Range Slider in the Properties tab](images/rangeslider-prop-vals-ss.png "Adding Mandatory Values to Range Slider")

1. To create an OnChange event, on the **Properties** tab, from the **Handler** drop-down, select **New Client Action**.

    ![Creating an OnChange client action for the Range Slider in the Properties tab](images/rangeslider-clientaction-ss.png "Creating Client Action for Range Slider")

    By default, the **Value** input parameter is created.  

    ![Automatically created Value input parameter for the Range Slider client action](images/rangeslider-value-input-ss.png "Value Input Parameter Creation")

1. From the Toolbox, drag the **Container** widget into the Main Content area of your application's screen, and add your content to the Container placeholder.

    In this example we add some text and an expression.

    ![Adding text and an expression to a Container widget on the application screen](images/rangeslider-container-ss.png "Adding Content to Container")

1. To create a variable for the expression, right-click your screen name, select **Add Local Variable**, and on the **Properties** tab, enter a name and data type (in this example, we use **Decimal**).

    ![Creating a local variable of type Decimal for the Range Slider expression](images/rangeslider-locvar-ss.png "Creating a Local Variable")

1. To bind the new variable to the expression, double-click the expression widget, and in the **Expression Value** editor, select the variable you just have created, and click **Close**.

    ![Binding a local variable to the expression widget for the Range Slider](images/rangeslider-expression-ss.png "Binding Variable to Expression")

1. So that the **Value** parameter reads the range slider selection, double-click your client action, and from the Toolbox, add the **Assign** action to the client action. Set the Assign **Variable** to the local variable you created, and the Assign **Value** to the automatically generated input parameter (Value).

    ![Setting the Assign action variables and values in the client action for the Range Slider](images/rangeslider-assign-ss.png "Setting Assign Variables and Values")

1.  You can configure the Range Slider by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties, for example, the size. For more configurations, expand the **OptionalConfigs** property.

    ![Configuring optional properties of the Range Slider on the Properties tab](images/rangeslider-properties-ss.png "Configuring Range Slider Properties")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MinValue (Decimal): Mandatory                         | Slider's minimum value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MaxValue (Decimal): Mandatory                         | Slider's maximum value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| StartingValue (Decimal): Mandatory                    | Value selected by default when the page is rendered. Must be between min and max values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Orientation (Orientation Identifier): Optional        | Sets the Range Slider direction. Default value is horizontal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Size (Text): Optional                                 | Sets the Range Slider size. If horizontal, the size is the width. Otherwise (vertical), the size is the height.  Accepts any kind of unit (px, %, vw). Default value is 100%.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ExtendedClass (Text): Optional                        | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
| OptionalConfigs.ShowFloatingLabel (Boolean): Optional | Set to True to add a floating label above the handler. Default value is False.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| OptionalConfigs.Step (Decimal): Optional              | Slider moves in increments of steps. If the step is set to 10, the slider increases or decreases in units of 10, for example, 0 to 10, to 20, to 30, and so on.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| OptionalConfigs.ShowTickMarks (Boolean): Optional     | Set to True to display tick marks below the slider. Default value is False. To generate the tick marks, you must set the TickMarksInterval to True.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| OptionalConfigs.TickMarksInterval (Integer): Optional | Range interval after which a tick mark is displayed (when ShowTickMarks is set to True). For example, if TickMarksInterval = 5, a tick mark is shown for each 5 steps. The value cannot be less than 0 (library restraint).                                                                                                                                                                                                                                                                                                                                                                                                             |
| OptionalConfigs.IsDisabled (Boolean): Optional        | Set as True to disable the Range Slider. Default value is False.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

