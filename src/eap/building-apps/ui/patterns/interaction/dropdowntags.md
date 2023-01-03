---
tags: runtime-mobileandreactiveweb;
summary: The Dropdown Tags UI Pattern offers multiple choice options to the user when using a dropdown search.
locale: en-us
guid: 91934a88-de31-437d-be9c-e2ca182835bb
app_type: mobile apps, reactive web apps
---

# Dropdown Tags

The Dropdown Tags UI Pattern offers multiple choice options to the user when when using a dropdown search.

**How to use the Dropdown Tags UI Pattern**

In this example, we create a dropdown tags search for a list of employees and a message that displays the number of selected items.

1. In ODC Studio, in the Toolbox, search for `Dropdown Tags`.

    The Dropdown Tags widget is displayed.

    ![Dropdown Tag widget](<images/dropdowntags-widget-ss.png>)

1. From the Toolbox, drag the Dropdown Search widget into the Main Content area of your application's screen.

    ![Drag widget to screen](<images/dropdowntags-drag-ss.png>)

1. Select and right-click your screen name, and select **Fetch Data from Database**.

1. To add a database entity, click the screen, and from the **Select Source** pop-up, select the relevant database entity and click **Select**.

    In this example, the **Sample_Employee** entity is selected. 

    ![Select database entity](<images/dropdowntags-source-ss.png>)

    The **GetEmployees** aggregate is automatically created.

    ![Aggregate automatically created](<images/dropdowntags-aggregate-ss.png>)

1. Return to your screen by double-clicking the screen name, select the **Dropdown Tags** widget, and on the **Properties** tab, set the mandatory properties (**ItemList**, **Value**, **Text**).

    ![Set mandatory properties](<images/dropdowntags-mandprops-ss.png>)

1. Staying on the **Properties** tab, from the **Handler** dropdown, select **New Client Action**.

    ![Create new client action](<images/dropdowntags-handler-ss.png>)

1. Add the relevant logic to the client action. 

    In this example:
    
    1. Add a Message to the client action.
    1. Add the following logic to the expression editor:

        `CurrentList.Length`

    1. Click **Close**. 
    
        This displays the number of selected items selected.

        ![Add logic](<images/dropdowntags-message-ss.png>)

1. You can configure the Dropdown Tags by selecting the pattern, and on the **Properties** tab, set the relevant optional properties. For more configurations, expand the **OptionalConfigs** property.

    ![Set properties](<images/dropdowntags-properties-ss.png>)

After following these steps and publishing the app, you can test the pattern in your app. The result of this example should look something like the following:

![Dropdown Tag result](<images/dropdowntags-result.png>)

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
