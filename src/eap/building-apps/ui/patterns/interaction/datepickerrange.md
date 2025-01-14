---
tags: date handling, ui components
summary: Learn how to implement a Date Picker Range in OutSystems Developer Cloud (ODC) using the flatpickr library for selecting date ranges.
locale: en-us
guid: 940d5a36-2677-40c7-a073-974104ff7704
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A14106&t=ZwHw8hXeFhwYsO5V-1
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

# Date Picker Range

You can use the Date Picker Range UI Pattern to allow users select a range date using a calendar. The Date Picker Range Pattern is based on the [flatpickr library](https://flatpickr.js.org/). For more advanced options, you can refer to this library.

In this example, the user selects a range of dates from the calendar. The dates are saved in a variable and then displayed in an input widget.

1. In ODC Studio, in the Toolbox, search for `Date Picker Range`.

    The Date Picker Range widget is displayed.

    ![Screenshot of the Date Picker Range widget in ODC Studio Toolbox](images/datepickerrange-widget-ss.png "Date Picker Range Widget")

1. From the Toolbox, drag the Date Picker Range widget into the Main Content area of your application's screen.

    By default, the Date Picker Range contains an **Input** widget (type Text).

    ![Dragging the Date Picker Range widget into the Main Content area of an application screen](images/datepickerrange-drag-ss.png "Dragging Date Picker Range Widget")

1. Create a variable by selecting the **Input** widget, and on the **Properties** tab, select **New Local Variable** from the **Variable** dropdown.

    This variable stores any value entered into or received by the Input widget.

    ![Creating a new local variable for the Input widget in the Properties tab](images/datepickerrange-inputvar-ss.png "Creating a New Variable")

1. Enter a name for the variable (in this example **DateVar**) and select **Date** as the **Data Type**.

    ![Entering a name for the variable and selecting Date as the Data Type](images/datepickerrange-datevar-ss.png "Naming the Variable and Setting Data Type")

1. Right-click your main screen and add 2 local variables (one to store the start date and one to store the end date selected by the user).

    This variable stores the date selected by the user.

    ![Adding two local variables to store the start and end dates selected by the user](images/datepickerrange-addvar-ss.png "Adding Local Variables")

1. Enter a name for the variables (in this example **PickedStartDate** and **PickedEndDate**) and select **Date** as the **Data Type**.

    ![Entering names for the start and end date variables and setting Date as the Data Type](images/datepickerrange-pickedstart-pickedend-ss.png "Naming Start and End Date Variables")
   

1. To create an **OnSelect** event for the Date Picker Range, on the **Properties** tab, from the **Handler** dropdown, select New **Client Action**.

    ![Creating an onSelect event for the Date Picker Range in the Properties tab](images/datepickerrange-handler-ss.png "Creating onSelect Event")

1. To access the date range selected by the user, create an **Assign** and set the **PickedStartDate** to **Start Date** and **PickedEndDate** to **EndDate**.

    ![Assigning the PickedStartDate and PickedEndDate variables to the selected date range](images/datepickerrange-assign-ss.png "Assigning Variable Values")

1. You can configure the Date Picker Range by selecting the pattern, and on the **Properties** tab, set the relevant optional properties. For more configurations, expand the **OptionalConfigs** property.

    ![Configuring the Date Picker Range properties in the Properties tab](images/datepickerrange-properties-ss.png "Setting Properties for Date Picker widget Range")

After following these steps and publishing the app, you can test the pattern in your app.

**Result**

![Final result showing the Date Picker Range pattern in action within an application](images/datepickerrange-result.png "Date Picker pattern Range Result")

## Properties

| Properties                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DateFormat (Text): Optional                                           | Set the input date format. If empty, the date format will be the same as the server format. When using formats with time, make sure to set the **TimeFormat** property. The following are some examples:<ul><li>"DD/MM/YYYY" - 15/05/2022 </li> <li>"MM/DD/YYYY" - 05/15/2022</li><li>"DD MMM YYYY" - 15 May 2022</li><li>"DD-MMM-YYYY" - 15-May-2022</li><li>"DD.MMM.YYYY" - 15.May.2022</li><li>"MMM DDD, YYYY" - May Sun, 2022</li><li>"MMM DDD, YY" - May Sun, 22</li></ul>                                                                                                                                                       |
| ShowTodayButton (Boolean): Optional                                   | If True, the **Today** button is displayed below the Date Picker Range.  This button allows users to pick the date of the current day. If False, the **Today** Button is not displayed. The default value is False.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| OptionalConfigs.InitialStartDate (Date): Optional                     | The preselected start date for the Date Picker Range. If not set, no start date or end date is preselected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| OptionalConfigs.InitialEndDate (Date): Optional                       | The preselected end date for the Date Picker Range. If not set, no start date or end date is preselected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| OptionalConfigs.MinDate (DateTime): Optional                          | All days before this date are disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| OptionalConfigs.MaxDate (DateTime): Optional                          | All days before this date are disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| OptionalConfigs.FirstWeekDay (DatePickerWeekDay Identifier): Optional | Defines which week day is displayed first.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ExtendedClass (Text): Optional                                        | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <br/><br/>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |
