---
tags: 
summary: Displays the current progress of a task using circular or semi-circular progress indicators.
locale: en-us
guid: 58229e1f-1b30-4d29-8c94-d709d5428012
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A19985&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Progress Circle

You can use the Progress Circle UI Pattern to show the current progress of an operation flow. The progress is incremented in fractions of the circular badge.

![Screenshot of an example progress circle showing current operation flow progress](images/progresscircle-example-ss.png "Example Progress Circle")

**How to use the Progress Circle UI Pattern**

In this example, we create a button that increments the progress circle each time it's clicked and displays the progress as a fraction.

1. In ODC Studio, in the Toolbox, search for `Progress Circle`.

    The Progress Circle widget is displayed.

    ![Screenshot of the Progress Circle widget in ODC Studio Toolbox](images/progresscircle-widget-ss.png "Progress Circle Widget")

1. From the Toolbox, drag the Progress Circle widget into the Main Content area of your application's screen.

    ![Screenshot illustrating how to drag the Progress Circle widget into the Main Content area](images/progresscircle-dragwidget-ss.png "Drag Widget to Screen")

1. Right-click your screen name, select **Add Local Variable**, and enter a name. for example, `Count`.

    ![Screenshot showing the process of adding a local variable in ODC Studio](images/progresscircle-variable-ss.png "Add Local Variable")

1. Select the Progress Circle widget, and on the **Properties** tab, in the **Progress** property, enter the **Count** variable. 

    ![Screenshot demonstrating how to add progress logic to the Progress Circle widget properties](images/progresscircle-logic-ss.png "Add Progress Logic")

1. Select the **Expression** widget inside the Progress Circle, and on the **Properties** tab, in the **Value** property, enter the relevant logic for the progress. In this example, enter the local variable **Count**. 

    ![Screenshot showing the Expression widget inside the Progress Circle with the Properties tab open](images/progresscircle-expression-ss.png "Add Expression Logic")

1. From the Toolbox, drag the **Separator** widget into the Progress Circle.

    ![Screenshot of adding the Separator widget into the Progress Circle](images/progresscircle-separator-ss.png "Add Separator Widget")

1. From the Toolbox, drag an **Expression** widget under the **Separator** widget and enter the relevant logic for the denominator. In this example, enter ``"100"``.

    ![Screenshot showing the addition of an Expression widget for the denominator under the Separator widget](images/progresscircle-denominator-ss.png "Add Expression Widget for Denominator")

1. From the Toolbox, drag the Button widget into the Main Content area of your application's screen. 

    In this example, we call the button **Increment** and set the **On Click** event to a  **New Client Action** that assigns the **Count** variable to `Count + 1`.

    ![Screenshot of adding an Increment button to the Main Content area of the application's screen](images/progresscircle-button-ss.png "Add a Button to the Screen")

    ![Screenshot showing the logic for the On Click event of the Increment button](images/progresscircle-assign-ss.png "Set On Click Action Logic")

1. Select the Progress Circle widget, and on the **Properties** tab, you can change the Progress Circle's look and feel by setting the (optional) properties, for example, the color settings.

    ![Screenshot of the Progress Circle widget properties tab with options to change its appearance](images/progresscircle-properties-ss.png "Set Optional Properties")

After following these steps and publishing the app, you can test the pattern in your app. The result of this example should look something like the following:

![Screenshot of the published app showing the result of the implemented Progress Circle UI Pattern](images/progresscircle-result-ss.png "Published App Result")

## Properties

| Property                      | Description                                                                                             |
|-------------------------------|---------------------------------------------------------------------------------------------------------|
| Progress (Integer): Mandatory | Progress percentage. Usually a number between 0 and 100. You can also use functions or local variables. |
|ProgressColor (Color Identifier): Optional | The color that fills the circle, as progress goes up, using the OutSystems UI Color palette.
|TrailColor (Text): Optional | The color of the empty part of the progress circle, using the OutSystems UI Color palette.  |
|Thickness (Integer): Optional | The thickness of the circle that marks the progress. |
|OptionalConfigs.Shape (Shape Identifier): Optional  | Set the progress circle shape.|
|OptionalConfigs.AnimateInitialProgress (Boolean): Optional  | If True, the progress from zero to the progress value is animated. This is the default.|
|ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <br/>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |
