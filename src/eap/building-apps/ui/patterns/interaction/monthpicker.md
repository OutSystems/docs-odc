---
tags:
summary: OutSystems Developer Cloud (ODC) features a Month Picker UI Pattern that leverages the flatpickr library for user-friendly month selection in applications.
locale: en-us
guid: 7302634b-c545-4b3a-98d4-f41d0a7545a2
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A15863&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---
# Month Picker

You can use the Month Picker UI Pattern to allow users input a month of the year. The Month Picker Pattern is based on the [flatpickr library](https://flatpickr.js.org/) For more advanced options, you can refer to this library.

## How to use the Month Picker UI Pattern

1. In ODC Studio, in the Toolbox, search for `Month Picker`.
    
    The Month Picker widget is displayed.

    ![Screenshot of the Month Picker widget in ODC Studio](images/monthpicker-widget-ss.png "Month Picker Widget")

1. From the Toolbox, drag the Month Picker widget into the Main Content area of your application's screen.

    ![Dragging the Month Picker widget into the Main Content area of an application screen](images/monthpicker-dragwidget-ss.png "Drag Month Picker Widget to Screen")

    By default, the Month Picker contains an **Input** widget (type Text).

1. Create a local variable by selecting the Input widget, and, on the **Properties** tab, select **New Local Variable** from the **Variable** dropdown.

    This variable stores any value entered into or received by the input widget.

    ![Creating a new local variable for the Month Picker in the Properties tab](images/monthpicker-variable-ss.png "Create New Local Variable")

1. Enter a name for the variable (in this example **MonthVar**) and select **Text** as the **Data Type**.

    ![Naming the local variable as MonthVar and selecting Text as the Data Type](images/monthpicker-monthvar-ss.png "Name the Variable MonthVar")

1. Right-click your main screen and add another local variable.

    This variable stores the month selected by the user.

    ![Creating another local variable for storing the selected month](images/monthpicker-localvar-ss.png "Create Another Local Variable")

1. Enter a name for the variable (in this example **MonthPicked**) and select **MonthYear** as the **Data Type**.

    ![Naming the new local variable as MonthPicked and selecting MonthYear as the Data Type](images/monthpicker-monthpicked-ss.png "Name the New Variable MonthPicked")

1. To create an **OnSelect** event for the Month Picker, select the Month Picker widget, and on the **Properties** tab, from the **Handler** dropdown, select **New Client Action**.

    ![Creating a new client action for the OnSelect event of the Month Picker](images/monthpicker-client-action-ss.png "Create a Client Action")

1. To access the month selected by the user, create an **Assign** and set the **MonthPicked** to **SelectedMonth**.

    ![Adding an Assign to the client action to set the MonthPicked variable to the selected month](images/monthpicker-assign-ss.png "Add an Assign to the Client Action")

1. You can configure the Month Picker by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties.

    ![Setting optional properties for the Month Picker in the Properties tab](images/monthpicker-properties-ss.png "Set Relevant Properties")

After following these steps and publishing the app, you can test the pattern in your app.

![Final result showing the Month Picker implemented in an application](images/monthpicker-result.png "Month Picker Result")

<div class="info" markdown="1">

You can use the [FormatDateTime](../../../../reference/built-in-functions/format.md#formatdatetime) function to specify a format for the date and time. 

</div>  

## Properties

| Property  | Description  | 
|---|---|
|  DateFormat (Text): Optional | Set the input date format. If empty, the date is the same as the server format. | 
|  InitialMonth (MonthYear): Optional | The initial selected month and year for the Month Picker. If not set, no initial month is selected. | 
| MinMonth (MonthYear): Optional  |  Set the minimum month that can be selected. Any month before this is disabled and cannot be selected. | 
| MaxMonth (MonthYear): Optional  | Set the maximum month that can be selected. Any month after this is disabled and cannot be selected.  | 
| ExtendedClass (Text): Optional  | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |




