---
tags: 
summary: Progress Bar displays the progress of a task by incrementing values in a bar.
locale: en-us
guid: 9365cf5d-fdea-45fa-9e39-19089259a83b
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Progress Bar

You can use the Progress Bar to display percentage values by incrementing values in a bar and to show the current progress of a task flow.

![Example of Progress Bar Pattern](<images/progressbar-example-ss.png>)

**How to use the Progress Bar UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Progress Bar`.

    The Progress Bar widget is displayed.

    ![Progress Bar widget](<images/progressbar-widget-ss.png>)

1. From the Toolbox, drag the Progress Bar widget into the Main Content area of your application's screen.

    ![Drag widget to screen](<images/progressbar-dragwidget-ss.png>)

1. Add the text you want to appear as the Progress Bar title. 

    In this example, we add `Ongoing tasks`.

    ![Add title to Progress Bar](<images/progressbar-text-ss.png>)

1. Right-click your screen name, select **Add Local Variable**, and enter a name. In this example, we enter `Count`.

    ![Add local variable](<images/progressbar-var-ss.png>)

1. Select the Progress Bar widget, and on the **Properties** tab, in the Progress property, enter the relevant logic for the progress percentage.

    In this example, we enter the following logic which sets the progress percentage to 4%:

    ``Count / 25 * 100``

1. From the Toolbox, drag the **Button** widget into the Main Content area of your application's screen. In this example, call the button **Increment** and set the **On Click** property to a **New Client Action** that assigns the **Count** variable to ``Count + 1``.

    ![Add a button](<images/progressbar-button-ss.png>)

    ![Set the assign](<images/progressbar-assign-ss.png>)

1. You can configure the Progress Bar by selecting the pattern, and on the **Properties** tab, set the relevant optional properties. For more configurations, expand the **OptionalConfigs** property.

    ![Set optional properties](<images/progressbar-prop-ss.png>)

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
