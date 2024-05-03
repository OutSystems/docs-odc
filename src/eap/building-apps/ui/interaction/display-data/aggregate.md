---
summary: Aggregates allow you to fetch data using an optimized query, tailored to your usage.
tags:
helpids: 17203
locale: en-us
guid: 0d8335b7-df99-40f3-8a9d-df0e5bd5ca18
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A7877&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---
# Aggregate

Aggregates allow you to fetch data using an optimized query, tailored to your usage. Aggregates automatically absorb changes in the data model and can load the local database's data from the server. They support combining several entities and advanced filtering, and bring only the attributes that are used on the screen or action. Attributes also abstract the underlying model for the developer, allowing attribute renaming and changes to the data type.  

In OutSystems Developer Cloud (ODC), you can now mash up data from different entities and distinct data sources in an aggregate. This allows you to join data from different sources to provide a unified view of all the data. ODC Studio pulls data from different sources and performs the operations in-memory to perform the data mash to provide the desired results. 

Some benefits of data mashup are:
* Simplified process: You can now directly drag and drop data from different sources rather than creating custom logic to combine different data. This helps you save time and effort. 
* Improved Data Analysis: you can now leverage data from various databases to gain deeper insights and make better business decisions.
* Increased Flexibility: you get greater flexibility in data analysis and reporting.

In Mobile and Web Apps, Aggregates can be client-side or server-side:

* Client-side Aggregates run in the client logic. You can use them to get data for your widgets when a Screen or a Block loads.
* Server-side Aggregates run in the server logic. You can use them in the logic flows.

## How to create an aggregate

You can create Aggregates in Screens, Blocks, or Action flows. 

### Create an Aggregate in a Screen or Block

To load data on a Screen or Block, right-click the Screen or Block and select **Fetch data from Database**.  
An empty Aggregate opens and ODC Studio displays a message on the empty Aggregate that you need to add an Entity.

![Screenshot of ODC Studio with an option to create a new Aggregate by right-clicking a Screen or Block](images/aggregate-create-ss.png "Create new Aggregate")

There are cases when you always need to fetch all records from the database, for example, to populate drop-down box lists. If you fetch all records using a Screen Aggregate, set the **Max. Records** higher than the maximum number of records you expect to fetch. Keep in mind that large amounts of data may slow down the user interface and degrade the responsiveness of the app.

### Create an Aggregate in an Action

To add an Aggregate to an Action, drag an **Aggregate** from the toolbox to the flow. 

![Screenshot showing how to add an Aggregate to an Action by dragging it from the toolbox to the flow in ODC Studio](images/aggregate-server-side-ss.png "Add Aggregate to an Action")

There are cases when you always need to fetch all records from the database, for example, to populate drop-down box lists. If you fetch all records using a Data Action, leave the **Max. Records** field empty. In Data Actions, the **Max. Records** value is optional. If you don't provide a value, the Data Action fetches all records from the database. 

## How to add a data source to an Aggregate

1. With the Aggregate open, navigate to **Data** > **Entities** > **Database**.

1. Drag one of the Entities to the Aggregate window.  
ODC Studio populates the Aggregate with columns that correspond to the attributes of the Entity. Note that, for example, if your Entity is called **MyEntity**, the Aggregate is automatically called **GetMyEntity**.

    ![Screenshot of ODC Studio displaying columns from a database entity added to an Aggregate](images/database-columns-aggregate-ss.png "Columns from database in Aggregate")

## How to add more data sources to an Aggregate

To add more data sources to your Aggregate, follow these steps:

1. With the Aggregate open, in the **Sources** tab, click **Add source**.

    ![Screenshot illustrating the process of adding a new data source to an Aggregate in ODC Studio](images/add-source-ss.png "Add a source to an Aggregate")

1. Click the source you want to add and then click **Select**.

    ![Screenshot of the source selection interface in ODC Studio for adding to an Aggregate](images/select-source-ss.png "Select source to add to the Aggregate")

1. Select the join type between your sources.  

    For more information, see [supported join types](supported-join-types.md).

    ![Screenshot showing the interface for selecting the join type between multiple sources in an Aggregate in ODC Studio](images/select-join-ss.png "Select join type between sources")

## Properties

| Name | Description | Mandatory | Default value | Observations |
|------|-------------|-----------|--------------|-------------|
| Name | Identifies an element in the scope where it is defined, like a screen, action, or app. | Yes |   |   |
| Description | Text that documents the element. |   |   | Useful for documentation purpose. The maximum size of this property is 2000 characters. |
| Timeout ("Server Request Timeout" for Screen Aggregates) | Maximum time in seconds to wait for the Aggregate to return data before triggering a Communication Exception. Overrides the [default timeout defined at the app level](../../../../getting-started/system-requirements.md#server-request-timeout). |   |   | Property doesn't exist for client-side Aggregates. There is a [maximum value](../../../../getting-started/system-requirements.md#server-request-timeout). |
| Max. Records | Maximum number of records read from the database. |   |   |  |
| Cache in Minutes | Maximum time content or results are stored in memory. When undefined, nothing is cached. |   |   | Property not available in client actions. |
| Start Index | Index of the first List item to iterate. Can be an expression. |   |   | The expression used in this property (if present) is evaluated before the web screen preparation. |
| Fetch |   | Yes | At start |   |

### Events

| Name | Description | Mandatory | Default value | Observations |
|------|-------------|-----------|--------------|-------------|
| On After Fetch | Action executed after the Aggregate fetches data from the data source. |   |   |   |

## Runtime Properties

| Name | Description | Read Only | Type | Observations |
|------|-------------|----------|-------|--------------|
| List | Collection of records returned by the performed query. |  | Record List |  |
| Count | Number of records returned by the Count query. |  | Long Integer |  |
| IsDataFetched | True when data has been fetched from the database and is ready to be used. | Yes | Boolean |  |
| HasFetchError | True when there is an error during data fetch due to a server error or communication timeout. | Yes | Boolean |  |
