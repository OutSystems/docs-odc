---
tags: widget implementation, ui design, date handling, form inputs, flatpickr library
summary: Explore the Date Picker UI Pattern in OutSystems Developer Cloud (ODC) for selecting dates using a calendar interface.
locale: en-us
guid: 87d21dac-8006-44b5-8e43-919e93a4e462
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A13767&t=ZwHw8hXeFhwYsO5V-1
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
topic:
  - add-widget-ui-pattern
---

# Date Picker

You can use the Date Picker UI Pattern to allow users to select a single date using a calendar. The Date Picker Pattern is based on the [flatpickr library](https://flatpickr.js.org/). For more advanced options, you can refer to this library.

In this example, the user selects a date from the calendar, the date is saved in a variable and then displayed in an input widget.

1. In ODC Studio, in the Toolbox, search for `Date Picker`.

    The Date Picker widget is displayed.

    ![Screenshot of the Date Picker widget in ODC Studio Toolbox](images/datepicker-widget-ss.png "Date Picker Widget")

1. From the Toolbox, drag the Date Picker widget into the Main Content area of your application's screen.

    By default, the Date Picker contains an **Input** widget (type Text).

    ![Dragging the Date Picker widget into the Main Content area on the screen](images/datepicker-drag-ss.png "Dragging Date Picker Widget")

1. Create a variable by selecting the **Input** widget, and on the **Properties** tab, select **New Local Variable** from the **Variable** dropdown.

    This variable stores any value entered into or received by the Input widget.

    ![Creating a new variable for the Input widget in the Properties tab](images/datepicker-var-ss.png "Creating a New Variable")

1. Enter a name for the variable (in this example **DateTimeVar**) and select **Date Time** as the **Data Type**. This variable is used to store the date that you selected.

    ![Entering a name for the new variable and selecting Date Time as the data type](images/datepicker-varname-ss.png "Naming the Variable")

1. To create an **OnSelect** event for the Date Picker, on the **Properties** tab, from the **Handler** dropdown, select New **Client Action**.

    ![Creating an onSelect event for the Date Picker in the Properties tab](images/datepicker-clientaction-ss.png "Creating onSelect Event")

1. To access the date selected by the user, create an **Assign** and set the **DatePicked** to **SelectedDateTime**.

    ![Adding an assign to set the DatePicked variable to the SelectedDateTime](images/datepicker-assign-ss.png "Assigning Variable Value")

1. You can configure the Datepicker by selecting the pattern, and on the **Properties** tab, set the relevant optional properties. For more configurations, expand the **OptionalConfigs** property.

    ![Configuring the Date Picker properties in the Properties tab](images/datepicker-properties-ss.png "Setting Date Picker Widget Properties")

After following these steps and publishing the app, you can test the pattern in your app.

**Result**

![Final result showing the Date Picker pattern in action within the app](images/datepicker-result.png "Date Picker pattern Result")

## Properties

| Properties                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DateFormat (Text): Optional                                           | Set the input date format. If empty, the date format will be the same as the server format. When using formats with time, make sure to set the **TimeFormat** property. The following are some examples:<ul><li>"DD/MM/YYYY" - 15/05/2022 </li> <li>"MM/DD/YYYY" - 05/15/2022</li><li>"DD MMM YYYY" - 15 May 2022</li><li>"DD-MMM-YYYY" - 15-May-2022</li><li>"DD.MMM.YYYY" - 15.May.2022</li><li>"MMM DDD, YYYY" - May Sun, 2022</li><li>"MMM DDD, YY" - May Sun, 22</li></ul>                                                                                                                                                       |
| ShowTodayButton (Boolean): Optional                                   | If True, the **Today** button is displayed below the Date Picker.  This button allows users to pick the date of the current day. If False, the **Today** Button is not displayed. The default value is False.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| TimeFormat (DatePickerTimeFormat Identifier): Optional                | Select the time format (12 or 24 hours). By default, no time is shown.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| OptionalConfigs.InitialDate (Date Time): Optional                     | The initial selected date for the Date Picker. If not set, no initial date is selected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| OptionalConfigs.MinDate (DateTime): Optional                          | All days before this date are disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| OptionalConfigs.MaxDate (DateTime): Optional                          | All days after this date are disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| OptionalConfigs.FirstWeekDay (DatePickerWeekDay Identifier): Optional | Defines which week day is displayed first.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ExtendedClass (Text): Optional                                        | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <br/><br/>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |
