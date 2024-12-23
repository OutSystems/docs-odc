---
tags: ui patterns, widget configuration
summary: OutSystems Developer Cloud (ODC) features a Progress Bar UI pattern for visually tracking task completion percentages.
locale: en-us
guid: 9365cf5d-fdea-45fa-9e39-19089259a83b
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A19941&t=ZwHw8hXeFhwYsO5V-1
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

# Progress Bar

You can use the Progress Bar to display percentage values by incrementing values in a bar and to show the current progress of a task flow.

![Screenshot showing an example of a Progress Bar pattern in use](images/progressbar-example-ss.png "Progress Bar Example")

**How to use the Progress Bar UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Progress Bar`.

    The Progress Bar widget is displayed.

    ![Screenshot of the Progress Bar widget in ODC Studio Toolbox](images/progressbar-widget-ss.png "Progress Bar Widget")

1. From the Toolbox, drag the Progress Bar widget into the Main Content area of your application's screen.

    ![Screenshot illustrating how to drag the Progress Bar widget into the Main Content area](images/progressbar-dragwidget-ss.png "Drag Progress Bar Widget")

1. Add the text you want to appear as the Progress Bar title. 

    In this example, we add `Ongoing tasks`.

    ![Screenshot showing where to add the title 'Ongoing tasks' to the Progress Bar](images/progressbar-text-ss.png "Add Title to Progress Bar")

1. Right-click your screen name, select **Add Local Variable**, and enter a name. In this example, we enter `Count`.

    ![Screenshot demonstrating how to add a local variable named 'Count' to the screen](images/progressbar-var-ss.png "Add Local Variable")

1. Select the Progress Bar widget, and on the **Properties** tab, in the Progress property, enter the relevant logic for the progress percentage.

    In this example, we enter the following logic which sets the progress percentage to 4%:

    ``Count / 25 * 100``

1. From the Toolbox, drag the **Button** widget into the Main Content area of your application's screen. In this example, call the button **Increment** and set the **On Click** property to a **New Client Action** that assigns the **Count** variable to ``Count + 1``.

    ![Screenshot showing the addition of an 'Increment' button to the application's screen](images/progressbar-button-ss.png "Add Increment Button")

    ![Screenshot depicting the assignment of the 'Count' variable to 'Count + 1' on button click](images/progressbar-assign-ss.png "Set Assign Action")

1. You can configure the Progress Bar by selecting the pattern, and on the **Properties** tab, set the relevant optional properties. For more configurations, expand the **OptionalConfigs** property.

    ![Screenshot showing how to set optional properties for the Progress Bar pattern](images/progressbar-prop-ss.png "Set Optional Properties for Progress Bar Pattern")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Progress (Integer): Mandatory                              | Progress percentage. Usually a number (integer) between 0 and 100. You can also use functions and local variables.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ProgressColor (Color Identifier): Optional                 | The background color of the progress bar. By default, the progress color is the primary color you chose when creating the app.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| TrailColor (Color Identifier): Optional                    | The color of the empty part of the bar. By default, the trail color is Neutral 4 (#DEE2E6).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Thickness (Integer): Optional                              | The height of the progress bar, in pixels, for example 20.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ExtendedClass (Text): Optional                             | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1" "myclass2"- Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
| OptionalConfigs.Shape (Shape Identifier): Optional         | Set the progress shape. The predefined options are SoftRounded, Rounded, and Sharp.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| OptionalConfigs.AnimateInitialProgress (Boolean): Optional | If True, the progress bar will show an animation going from zero to its initial progress.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
