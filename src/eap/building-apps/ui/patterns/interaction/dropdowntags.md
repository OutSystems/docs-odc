---
tags: ui patterns, data binding, user interaction
summary: OutSystems Developer Cloud (ODC) features the Dropdown Tags UI Pattern, enabling users to select multiple options from a dropdown list.
locale: en-us
guid: 91934a88-de31-437d-be9c-e2ca182835bb
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A15084&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
content-type:
  - procedure
  - reference
---

# Dropdown Tags

The Dropdown Tags UI Pattern offers multiple choice options to the user when when using a dropdown search.

**How to use the Dropdown Tags UI Pattern**

In this example, we create a dropdown tags search for a list of employees and a message that displays the number of selected items.

1. In ODC Studio, in the Toolbox, search for `Dropdown Tags`.

    The Dropdown Tags widget is displayed.

    ![Screenshot of the Dropdown Tags widget in ODC Studio toolbox](images/dropdowntags-widget-ss.png "Dropdown Tags Widget in ODC Studio")

1. From the Toolbox, drag the Dropdown Search widget into the Main Content area of your application's screen.

    ![Dragging the Dropdown Search widget into the Main Content area of an application screen](images/dropdowntags-drag-ss.png "Dragging Widget to Screen")

1. Select and right-click your screen name, and select **Fetch Data from Database**.

1. To add a database entity, click the screen, and from the **Select Source** pop-up, select the relevant database entity and click **Select**.

    In this example, the **Sample_Employee** entity is selected. 

    ![Select Source pop-up with Sample_Employee entity selected for Dropdown Tags data source](images/dropdowntags-source-ss.png "Selecting Database Entity")

    The **GetEmployees** aggregate is automatically created.

    ![GetEmployees aggregate automatically created after selecting database entity for Dropdown Tags](images/dropdowntags-aggregate-ss.png "Aggregate Automatically Created")

1. Return to your screen by double-clicking the screen name, select the **Dropdown Tags** widget, and on the **Properties** tab, set the mandatory properties (**ItemList**, **Value**, **Text**).

    ![Properties tab showing mandatory properties set for the Dropdown Tags widget](images/dropdowntags-mandprops-ss.png "Setting Mandatory Properties")

1. Staying on the **Properties** tab, from the **Handler** dropdown, select **New Client Action**.

    ![Dropdown Tags Properties tab with Handler dropdown showing New Client Action selection](images/dropdowntags-handler-ss.png "Creating New Client Action")

1. Add the relevant logic to the client action. 

    In this example:
    
    1. Add a Message to the client action.
    1. Add the following logic to the expression editor:

        `CurrentList.Length`

    1. Click **Close**. 
    
        This displays the number of selected items selected.

        ![Adding a message and logic to the client action in Dropdown Tags configuration](images/dropdowntags-message-ss.png "Adding Logic to Client Action")

1. You can configure the Dropdown Tags by selecting the pattern, and on the **Properties** tab, set the relevant optional properties. For more configurations, expand the **OptionalConfigs** property.

    ![Dropdown Tags Properties tab with OptionalConfigs property expanded for additional configurations](images/dropdowntags-properties-ss.png "Setting Optional Properties")

After following these steps and publishing the app, you can test the pattern in your app. The result of this example should look something like the following:

![Final result of the Dropdown Tags UI Pattern in a published app](images/dropdowntags-result.png "Dropdown Tags Result")

## Properties

| Property                                            | Description                                               |
|-----------------------------------------------------|-----------------------------------------------------------|
| OptionsList (DropdownTagsOption List): Mandatory    | List of items to show in the dropdown.                    |
| SelectedOptions (DropdownTagsOption List): Optional | Defines preselected items in the dropdown list.           |
| Prompt (Text): Optional                             | Text that is displayed when no items are selected.        |
| OptionalConfigs.IsDisabled (Boolean): Optional      | Set as True to disable the Dropdown.                      |
| OptionalConfigs.NoResultsText (Text): Optional      | Text that is displayed when there are no results to show. |
| OptionalConfigs.SearchPrompt (Text): Optional       | Prompt text displayed in the search input box.            |
| OptionalConfigs.NoOptionsText (Text): Optional      | Set the message that is displayed in the Dropdown list when there are no options available.<br/><br/>The default message is: **There are no options to show.** |
|ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>_Blank_ - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |
