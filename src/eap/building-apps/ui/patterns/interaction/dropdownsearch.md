---
tags:
summary: The Dropdown Search UI Pattern offers a choice of available options that the user can search.
locale: en-us
guid: 667dfcf6-b299-492b-8e93-655ad62ea91a
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A14668&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Dropdown Search

The Dropdown Search UI Pattern offers a choice of available options that the user can search. 

**How to use the Dropdown Search UI Pattern**

In this example, we create a dropdown search for a list of employees. When the user selects an employee, a message displays the employee's  name and ID.

1. In ODC Studio, in the Toolbox, search for `Dropdown Search`.

    The Dropdown Search widget is displayed.

    ![Dropdown Search widget](<images/dropdownsearch-widget-ss.png>)

1. From the Toolbox, drag the Dropdown Search widget into the Main Content area of your application's screen.

    ![Drag the widget to the screen](<images/dropdownsearch-drag-ss.png>)

1. Select and right-click your screen name, and select **Fetch Data from Database**.

    ![Fetch data from database](<images/dropdownsearch-fetch-ss.png>)

1. To add a database entity, click the screen, and from the **Select Source** pop-up, select the relevant database entity and click **Select**.

    In this example, the **Sample_Employee** entity is selected. 

    ![Select database entity](<images/dropdownsearch-source-ss.png>)

    The **GetEmployees** aggregate is automatically created.

    ![The GetEmployees aggregates is automatically created](<images/dropdownsearch-aggregate-ss.png>)

1. Return to your screen by double-clicking the screen name. Select the Dropdown Search widget, and on the **Properties** tab, set the mandatory properties (**OptionsList**, **Value**, **Label**).

    ![Set the mandatory properties](<images/dropdownsearch-logic-ss.png>)

1. Staying on the **Properties** tab, from the OnChanged event **Handler** dropdown, select **New Client Action**.

    ![Create a new client action](<images/dropdownsearch-handler-ss.png>)

1. Add the relevant logic to the client action. 

    For this example:
    1. Add a **Message** to the client action.
    1. Add the following logic to the expression editor:

        `SelectedItem.Text + "(Employee ID: " + SelectedItem.Value + ")`

    1. Click **Close**. 
    
        This displays the selected employee's name and their ID.

        ![Add message logic](<images/dropdownsearch-message-ss.png>)

1. You can configure the Dropdown Search by selecting the pattern, and on the **Properties** tab, set the relevant optional properties. For more configurations, expand the OptionalConfigs property.

    ![Set optional properties](<images/dropdownsearch-properties-ss.png>)

After following these steps and publishing the app, you can test the pattern in your app. The results from this example should look something like the following:

![Dropdown result](<images/dropdownsearch-result.png>)

## Properties

| Property                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OptionsList (DropdownSearchOptionList): Mandatory          | List of items to show in the dropdown.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| SelectedOptions (DropdownSearchOption List): Optional      | Defines preselected items in the dropdown list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Prompt (Text): Optional                                    | Text that is displayed when no items are selected and serves as an empty value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| OptionalConfigs.AllowMultipleSelection (Boolean): Optional | Set to True to allow the selection of multiple options. Default value is False.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| OptionalConfigs.IsDisabled (Boolean): Optional             | Set to True to disable the dropdown.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| OptionalConfigs.NoResultsText (Text): Optional             | Text that is displayed when there are no results to show.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| OptionalConfigs.SearchPrompt (Text): Optional              | Prompt text displayed in the search input box.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| OptionalConfigs.NoOptionsText (Text): Optional | Set the message that is displayed in the Dropdown list when there are no options available.<br/><br/>The default message is: **There are no options to show.** |
| ExtendedClass (Text): Optional                             | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |
