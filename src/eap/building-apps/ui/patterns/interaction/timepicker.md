---
tags: ui pattern implementation, time picker configuration
summary: Explore how to implement and configure the Time Picker UI Pattern in OutSystems Developer Cloud (ODC) for user time input.
locale: en-us
guid: 510393e6-a590-4ceb-a143-eefdac104240
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A17949&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
content-type:
  - reference
  - procedure
---

# Time Picker

You can use the Time Picker UI Pattern to allow users input a time of day in either a 24-hour or AM/PM format. The Time Picker Pattern is based on the [flatpickr library](https://flatpickr.js.org/) For more advanced options, you can refer to this library.

## How to use the Time Picker UI Pattern

1. In ODC Studio, in the Toolbox, search for `Time Picker`.
    
    The Time Picker widget is displayed.

    ![Screenshot of the Time Picker widget in the ODC Studio Toolbox](images/timepicker-widget-ss.png "Time Picker Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Time Picker widget into the Main Content area of your application's screen.

    ![Dragging the Time Picker widget into the Main Content area of an application screen](images/timepicker-widget-drag-ss.png "Dragging Time Picker Widget to Screen")

    By default, the Time Picker contains an **Input** widget (type Text).

1. Create a variable by selecting the **Input** widget, and, on the **Properties** tab, select **New Local Variable** from the **Variable** dropdown.

    ![Creating a new local variable for the Time Picker in the Properties tab](images/timepicker-local-variable-ss.png "Creating a Local Variable for Time Picker")

    This variable stores any value entered into or received by the input widget.

1. Enter a name for the variable (in this example **TimeVar**) and select **Time** as the **Data Type**.

    ![Entering a name for the Time Picker variable and selecting Time as the Data Type](images/timepicker-timevar-ss.png "Naming the Time Variable")

1. Right-click your main screen and add another local variable.

    ![Adding a new local variable in the main screen of the application](images/timepicker-new-loc-var-ss.png "Adding a New Local Variable")

    This variable stores the time selected by the user.

1. Enter a name for the variable (in this example **TimePicked**) and select **Time** as the **Data Type**.

    ![Entering a name for the Time Picked variable and selecting Time as the Data Type](images/timepicker-timepicked-ss.png "Naming the Time Picked Variable")

1. To create an **OnSelect** event for the Time Picker, select the widget and on the **Properties** tab, from the **Handler** dropdown, select **New Client Action**.

    ![Creating a new client action for the Time Picker widget in the Properties tab](images/timepicker-clientaction-ss.png "Creating a New Client Action for Time Picker")

1. To access the time selected by the user, create an **Assign** and set the **TimePicked** to **SelectedTime**.

    ![Creating an Assign to set the TimePicked variable to the SelectedTime](images/timepicker-assign-ss.png "Creating an Assign for Time Selection")

1. You can configure the Time Picker by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties. For more configurations, expand the **OptionalConfigs** property.

    ![Setting properties for the Time Picker pattern in the Properties tab](images/timepicker-properties-ss.png "Setting Properties for Time Picke Widget")

After following these steps and publishing the app, you can test the pattern in your app. 

![Final result showing the Time Picker pattern implemented in the application](images/timepicker-result-ss.png "Time Picker Result Pattern in App")
## Properties

| Property  | Description  | 
|---|---|
|  Is24Hours (Boolean): Optional | Set to **False** to display the time in an AM/PM format. By default, the time is displayed using a 24 hour format.  | 
|  InitialTime (Time): Optional | The initial time selected for the Time Picker. If not set, no initial time is displayed and the Time Picker starts at 12:00.  | 
| OptionalConfigs.MinTime (Time): Optional  |  Set the minimum time that can be selected. Time before the minimum time is disabled. | 
| OptionalConfigs.MaxTime (Time): Optional  | Set the maximum time that can be selected. Time after the maximum is disabled.  | 
| ExtendedClass (Text): Optional  | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |



