---
summary: OutSystems Developer Cloud (ODC) simplifies data fetching and display from databases using Aggregates and widgets.
tags: data integration, entity management, client-side logic
locale: en-us
guid: 9072a3d9-8993-4b6a-98b7-2f623bcd78bc
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A7751&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
---

# Fetch and display data from the database in OutSystems

You often need to fetch data from a database to, for example, show it on the screen. An efficient way to fetch data from databases in OutSystems is to use an Aggregate.

This document guides you through two steps:

1. Getting data. You first need to load some data from your database. The example uses Entities from OutSystems sample data, but you can use your Entities as well. 
1. Showing data. Once your app has data, you can show all records or just some. The example uses the List widget, but you can add a Table or some other widget.

## Fetch data from a database

Here is how you can fetch data in your app by using an aggregate. Aggregates are a handy way to get data, and they don't require knowledge of databases. As this is a simple app, you can reference the data directly from the main app.

<div class="info" markdown="1">

This is an example of getting data with an aggregate to a screen. Both Aggregate and Screen run in the **client**. For more information about creating aggregates in the **server** logic, refer to [Server-side Aggregates](../../data/fetch-data/aggregate.md).

</div>

1. Add a Screen to your app. Go to **Interface** > **UI Flows**, right-click **MainFlow** and select **Add Screen**. In the **New Screen** window select **Empty** (1), enter **Home** as the Screen name (2), then click **CREATE SCREEN** (3). ODC Studio adds an empty Screen to your app.

    ![Screenshot of the New Screen window in ODC Studio with steps to create an empty screen named Home](images/new-screen-ss.png "Creating a New Screen in ODC Studio")

1. Add data sources to your app by referencing some Entities in the **Public Elements** window (**Ctrl+Q**). Once you reference Entities, they're available in ODC Studio under **Data** > **Entities** > **Database**.

    ![Screenshot showing how to reference Entities in ODC Studio under the Data section](images/database-entities-ss.png "Database Entities in ODC Studio")

    <div class="info" markdown="1">

    Instead of referencing existing Entities, you can [importing data from Excel](../../data/modeling/excel-bootstrap.md) and create new Entities.

    </div>

1. Publish the app by clicking the **1-Click Publish button**. This step is optional, but it lets the app show the data preview later.  

1. It's time to load some data to the Screen. Go to **Interface** > **UI Flows** > **Main Flow**, and then right-click your **Home** Screen. Select **Fetch Data from Database**. A new Aggregate edit screen opens, and there's a notice that you need some data.

    ![Screenshot of an empty Aggregate edit screen in ODC Studio indicating the need to add data](images/fetch-data-aggregate-open-ss.png "Starting an Aggregate in ODC Studio")

1. With the Aggregate still open, navigate to **Data** > **Entities** > **Database** > **OutSystemsSampleDataDB**. Drag the **Sample_Employee** Entity to the Aggregate window. If you're using your data instead of OutSystems sample data, then drag some other Entity. ODC Studio shows the data preview in columns, and uses the Entity name to name the Aggregate.
   
    ![Screenshot of an Aggregate in ODC Studio showing a data preview with the Sample_Employee Entity](images/fetch-data-aggregate-with-entity-ss.png "Aggregate with Sample Employee Entity")

    <div class="info" markdown="1">

    If you don't see a preview, but warnings instead, go ahead and publish your app to update the references and refresh the preview.

    </div>

1. Go back to **Interface** > **UI Flows** > **Main Flow** > **Home** and notice the **GetEmployees** Aggregate in the Screen. Expand the Aggregate to see the Entities, and then expand the Entities to list the Attributes. There's also a warning that you're not using the data anywhere. Follow the instructions on [how to show the data in an app](#showing-data) to prevent the warning. 

    ![Screenshot of the Home Screen in ODC Studio displaying the GetEmployees Aggregate with Entity Attributes](images/fetch-data-aggregate-in-screen-ss.png "Aggregate Displayed in Home Screen")

For more information, refer to the [best practices for fetching and displaying data](../../ui/creating-screens/best-practices-fetch-display-data.md).

## Show data in a widget

Once you fetch data from the database, use one of many OutSystems widgets to show the data to the users. Continuing from the previous section, in this example you create a list with the employee last names.

1. Open your **Home** Screen for editing. To do that, double-click **Home** in  **Interface** > **UI Flows** > **Main Flow**.

1. In the search bar, search for the **List** widget and drag the widget to the Screen. ODC Studio now shows an empty List widget.

    ![Screenshot showing an empty List widget added to the Home Screen in ODC Studio](images/fetch-data-new-widget-ss.png "Adding a List Widget to the Screen")

1. Click the List widget to select it, and go to the properties. In the **Source** field select **GetEmployees.List**. With this you're telling the app which data source to use with this widget.

    ![Screenshot of a List widget's properties with the Source field set to GetEmployees.List in ODC Studio](images/fetch-data-widget-with-data-source-ss.png "Configuring the Source Property of a Widget")

    <div class="info" markdown="1">

    The **Sample_Employees** Entity comes from the OutSystems sample data. See the [fetching data](#fetch-data-from-a-database) section for more information.

    </div>

1. With your List widget connected to a data source, add some Attributes to show data in the List. Expand the Entity to see the Attributes, under **Interface** > **UI Flows** > **Main Flow** > **Home** > **GetEmployees** > **Sample_Employee**. Drag an Attribute, for example, **LastName** to the List widget. This tells the widget to list all last names that are in the database.

    ![Screenshot illustrating the process of dragging the LastName Attribute from the Sample_Employee Entity to the List widget](images/fetch-data-drag-attribute-ss.png "Dragging an Entity Attribute to a List Widget")

1. Publish your app and load it in the browser. There's a list widget listing the last names of the employees.

    ![Browser view of the app running with a list widget listing employee last names](images/fetch-data-browser.png "App Displaying Employee Last Names")

## Related resources

* [Building Screens with Data](https://learn.outsystems.com/training/journeys/building-screens-with-data-637) online course
