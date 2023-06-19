---
tags: 
summary: Allow users to input a time of day in either a 24-hour or AM/PM format. 
locale: en-us
guid: 510393e6-a590-4ceb-a143-eefdac104240
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A17949&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Time Picker

You can use the Time Picker UI Pattern to allow users input a time of day in either a 24-hour or AM/PM format. The Time Picker Pattern is based on the [flatpickr library](https://flatpickr.js.org/) For more advanced options, you can refer to this library.

## How to use the Time Picker UI Pattern

1. In ODC Studio, in the Toolbox, search for `Time Picker`.
    
    The Time Picker widget is displayed.

    ![Time Picker widget](<images/timepicker-widget-ss.png>)

1. From the Toolbox, drag the Time Picker widget into the Main Content area of your application's screen.

    ![Drag Time Picker widget to screen](<images/timepicker-widget-drag-ss.png>)

    By default, the Time Picker contains an **Input** widget (type Text).

1. Create a variable by selecting the **Input** widget, and, on the **Properties** tab, select **New Local Variable** from the **Variable** dropdown.

    ![Create local variable](<images/timepicker-local-variable-ss.png>)

    This variable stores any value entered into or received by the input widget.

1. Enter a name for the variable (in this example **TimeVar**) and select **Time** as the **Data Type**.

    ![Enter variable name](<images/timepicker-timevar-ss.png>)

1. Right-click your main screen and add another local variable.

    ![Add a new local variable](<images/timepicker-new-loc-var-ss.png>)

    This variable stores the time selected by the user.

1. Enter a name for the variable (in this example **TimePicked**) and select **Time** as the **Data Type**.

    ![Enter a variable name](<images/timepicker-timepicked-ss.png>)

1. To create an **OnSelect** event for the Time Picker, select the widget and on the **Properties** tab, from the **Handler** dropdown, select **New Client Action**.

    ![Create a new client action](<images/timepicker-clientaction-ss.png>)

1. To access the time selected by the user, create an **Assign** and set the **TimePicked** to **SelectedTime**.

    ![Create an Assign](<images/timepicker-assign-ss.png>)

1. You can configure the Time Picker by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties. For more configurations, expand the **OptionalConfigs** property.

    ![Set the properties](<images/timepicker-properties-ss.png>)

After following these steps and publishing the app, you can test the pattern in your app. 

![Result](<images/timepicker-result-ss.png>)
## Properties

| Property  | Description  | 
|---|---|
|  Is24Hours (Boolean): Optional | Set to **False** to display the time in an AM/PM format. By default, the time is displayed using a 24 hour format.  | 
|  InitialTime (Time): Optional | The initial time selected for the Time Picker. If not set, no initial time is displayed and the Time Picker starts at 12:00.  | 
| OptionalConfigs.MinTime (Time): Optional  |  Set the minimum time that can be selected. Time before the minimum time is disabled. | 
| OptionalConfigs.MaxTime (Time): Optional  | Set the maximum time that can be selected. Time after the maximum is disabled.  | 
| ExtendedClass (Text): Optional  | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |



