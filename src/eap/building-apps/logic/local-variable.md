---
helpids: 1013
summary: Explore managing Local Variables in OutSystems Developer Cloud (ODC) for data filtering.
locale: en-us
guid: 2e1a1542-5dc1-4269-987b-f2665ce37f07
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3213%3A21499&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
tags: data filtering, local variable management, data binding, aggregate filtering, widget properties
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
  - apply
---

# Local Variable

A Local Variable exists only in the scope of its parent element, for example, a Screen or an Action. A Local Variable can only be assigned and used locally inside that scope. Local variables are destroyed when execution leaves the scope of the parent element. The image below shows how to add a Local Variable inside a Screen.  

![Screenshot showing the process of adding a Local Variable inside a Screen](images/add-local-variable-ss.png "Adding a Local Variable in a Screen")

## How to use

This example shows how to use a Local Variable to keep the value of a Search widget. The value of the Local Variable is then used to filter an Aggregate.

1. Select the Input widget.

1. On the **Properties** tab, select the **Variable** dropdown and select **New Local Variable**.

    ![Screenshot of the Properties tab with the Variable dropdown expanded showing the option to create a New Local Variable](images/local-variable-ss.png "Creating a New Local Variable")

1. Enter a name for the variable, for example `SearchKeyword`. Make sure the **Data Type** is set to `Text`.

    ![Screenshot of naming the Local Variable 'SearchKeyword' with the Data Type set to Text](images/variable-searchkeyword-ss.png "Naming the Local Variable")

1. Double-click the aggregate on the Elements tree.

1. On the **Filter** tab, click **Add filter**.

1. Insert the filter condition.

    ```
    Employee.FirstName like "%" + SearchKeyword + "%"
    ```

1. To save the filter, click **Close**.

    ![Screenshot of an Aggregate with a filter condition using the 'SearchKeyword' Local Variable to filter results](images/filtered-aggregate-ss.png "Filtered Aggregate Using Local Variable")

After you follow these steps and publish your app, you can test the functionality of the filter in your browser. The text inserted in the Input of the Search widget is stored in the defined Local Variable and is then used to filter the aggregate. When you change to another screen or close your browser, the Local Variable is destroyed and the filter no longer applies.
