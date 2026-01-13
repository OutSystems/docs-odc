---
tags: ui patterns, user interface design, data binding, widgets, employee management
summary: OutSystems Developer Cloud (ODC) includes a Dropdown Search UI Pattern for searchable option selection in applications.
locale: en-us
guid: 667dfcf6-b299-492b-8e93-655ad62ea91a
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A14668&t=ZwHw8hXeFhwYsO5V-1
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

# Dropdown Search

<div class="info" markdown="1">

Applies to the OutSystems UI framework only.

</div>

The Dropdown Search UI Pattern offers a choice of available options that the user can search.

**How to use the Dropdown Search UI Pattern**

In this example, we create a dropdown search for a list of employees. When the user selects an employee, a message displays the employee's  name and ID.

1. In ODC Studio, in the Toolbox, search for `Dropdown Search`.

    The Dropdown Search widget is displayed.

    ![Screenshot of the Dropdown Search widget in the ODC Studio Toolbox](images/dropdownsearch-widget-ss.png "Dropdown Search Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Dropdown Search widget into the Main Content area of your application's screen.

    ![Screenshot showing how to drag the Dropdown Search widget into the Main Content area of an application screen](images/dropdownsearch-drag-ss.png "Dragging the Dropdown Search Widget to the Screen")

1. Select and right-click your screen name, and select **Fetch Data from Database**.

    ![Screenshot of the context menu option to fetch data from the database for the Dropdown Search UI Pattern](images/dropdownsearch-fetch-ss.png "Fetching Data from Database for Dropdown Search")

1. To add a database entity, click the screen, and from the **Select Source** pop-up, select the relevant database entity and click **Select**.

    In this example, the **Sample_Employee** entity is selected.

    ![Screenshot of the Select Source pop-up for choosing a database entity for the Dropdown Search UI Pattern](images/dropdownsearch-source-ss.png "Selecting Database Entity for Dropdown Search")

    The **GetEmployees** aggregate is automatically created.

    ![Screenshot showing the automatic creation of the GetEmployees aggregate after selecting a database entity](images/dropdownsearch-aggregate-ss.png "GetEmployees Aggregate Creation")

1. Return to your screen by double-clicking the screen name. Select the Dropdown Search widget, and on the **Properties** tab, set the mandatory properties (**OptionsList**, **Value**, **Label**).

    ![Screenshot of the Properties tab where mandatory properties for the Dropdown Search widget are set](images/dropdownsearch-logic-ss.png "Setting Mandatory Properties for Dropdown Search Widget")

1. Staying on the **Properties** tab, from the OnChanged event **Handler** dropdown, select **New Client Action**.

    ![Screenshot of the Properties tab with the OnChanged event Handler dropdown to create a new client action for Dropdown Search](images/dropdownsearch-handler-ss.png "Creating a New Client Action for Dropdown Search")

1. Add the relevant logic to the client action.

    For this example:
    1. Add a **Message** to the client action.
    1. Add the following logic to the expression editor:

        `SelectedItem.Text + "(Employee ID: " + SelectedItem.Value + ")`

    1. Click **Close**.

        This displays the selected employee's name and their ID.

        ![Screenshot showing the addition of a message to the client action for displaying the selected employee's name and ID in Dropdown Search](images/dropdownsearch-message-ss.png "Adding Message Logic to Dropdown Search")

1. You can configure the Dropdown Search by selecting the pattern, and on the **Properties** tab, set the relevant optional properties. For more configurations, expand the OptionalConfigs property.

    ![Screenshot of the Properties tab for configuring optional properties of the Dropdown Search UI Pattern](images/dropdownsearch-properties-ss.png "Setting Optional Properties for Dropdown Search")

After following these steps and publishing the app, you can test the pattern in your app. The results from this example should look something like the following:

![Screenshot of the Dropdown Search UI Pattern in action displaying the result of a selected employee](images/dropdownsearch-result.png "Dropdown Search Pattern Result Display")

## Properties

| Property | Description |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| OptionsList (DropdownSearchOptionList): Mandatory | List of items to show in the dropdown. |
| SelectedOptions (DropdownSearchOption List): Optional | Defines preselected items in the dropdown list. |
| Prompt (Text): Optional | Text that is displayed when no items are selected and serves as an empty value. |
| OptionalConfigs.AllowMultipleSelection (Boolean): Optional | Set to True to allow the selection of multiple options. Default value is False. |
| OptionalConfigs.IsDisabled (Boolean): Optional | Set to True to disable the dropdown. |
| OptionalConfigs.NoResultsText (Text): Optional | Text that is displayed when there are no results to show. |
| OptionalConfigs.SearchPrompt (Text): Optional | Prompt text displayed in the search input box. |
| OptionalConfigs.NoOptionsText (Text): Optional | Set the message that is displayed in the Dropdown list when there are no options available.<br/><br/>The default message is: **There are no options to show.** |
| OptionalConfigs.SanitizeDropdownValues (Boolean): Optional | Set true to assure the values inputted in the dropdown will be sanitized or false if you want to explicitly allow custom code to run.<br/>By setting it to true it will replace HTML tags from option's text (value and label) to prevent potential injected code execution.<br/>This option is not enabled by default to avoid performance issues.<br/><br/>**Note:** When using OutSystems UI prior to version 2.23.0 and do not explicitly need to use HTML, ensure that the client action ``SetVirtualSelectConfigs`` is executed in the ``Initialized`` event handler of the Dropdown Search block, with ``enableSecureText = Entities.BooleanTypes.True`` to prevent potential injected code execution. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |
