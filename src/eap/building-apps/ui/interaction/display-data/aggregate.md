---
kinds: ServiceStudio.Model.Nodes+DataSet+Kind, ServiceStudio.Model.NRNodes+WebScreenDataSet+Kind
helpids: 17203
locale: en-us
guid: 0d8335b7-df99-40f3-8a9d-df0e5bd5ca18
app_type: mobile apps, reactive web apps
---

# Aggregate

Aggregates allow you to fetch data using an optimized query, tailored to your usage. Aggregates automatically absorb changes in the data model and can load the local database's data from the server. They support combining several entities and advanced filtering, and bring only the attributes that are used on the screen or action. Attributes also abstract the underlying model for the developer, allowing attribute renaming and changes to the data type.  

In Mobile and Web Apps, Aggregates can be client-side or server-side:

* Client-side Aggregates run in the client logic. You can use them to get data for your widgets when a Screen or a Block loads.
* Server-side Aggregates run in the server logic. You can use them in the logic flows.

## How to create an aggregate

You can create Aggregates in Screens, Blocks, or Action flows. 

### Create an Aggregate in a Screen or Block

To load data on a Screen or Block, right-click the Screen or Block and select **Fetch data from Database**.  
An empty Aggregate opens and ODC Studio displays a message on the empty Aggregate that you need to add an Entity.

![Create new Aggregate](images/aggregate-create-ss.png)

There are cases when you always need to fetch all records from the database, for example, to populate drop-down box lists. If you fetch all records using a Screen Aggregate, set the **Max. Records** higher than the maximum number of records you expect to fetch. Keep in mind that large amounts of data may slow down the user interface and degrade the responsiveness of the app.

### Create an Aggregate in an Action

To add an Aggregate to an Action, drag an **Aggregate** from the toolbox to the flow. 

![Add Aggregate to an Action](images/aggregate-server-side-ss.png)

There are cases when you always need to fetch all records from the database, for example, to populate drop-down box lists. If you fetch all records using a Data Action, leave the **Max. Records** field empty. In Data Actions, the **Max. Records** value is optional. If you don't provide a value, the Data Action fetches all records from the database. 

## How to add a data source to an Aggregate

1. With the Aggregate open, navigate to **Data** > **Entities** > **Database**.

1. Drag one of the Entities to the Aggregate window.  
ODC Studio populates the Aggregate with columns that correspond to the attributes of the Entity. Note that, for example, if your Entity is called **MyEntity**, the Aggregate is automatically called **GetMyEntity**.

    ![Columns from database in Aggregate](images/database-columns-aggregate-ss.png)

## How to add more data sources to an Aggregate

To add more data sources to your Aggregate, follow these steps:

1. With the Aggregate open, in the **Sources** tab, click **Add source**.

    ![Add a source to an Aggregate.](images/add-source-ss.png)

1. Click the source you want to add and then click **Select**.

    ![Select source to add to the Aggregate.](images/select-source-ss.png)

1. Select the join type between your sources.  

For more information, see [supported join types](supported-join-types.md).

    ![Select join type between sources.](images/select-join-ss.png)

## Properties

| Name | Description | Mandatory | Default value | Observations |
|------|-------------|-----------|--------------|-------------|
| Name | Identifies an element in the scope where it is defined, like a screen, action, or app. | Yes |   |   |
| Description | Text that documents the element. |   |   | Useful for documentation purpose. The maximum size of this property is 2000 characters. |
| Timeout ("Server Request Timeout" for Screen Aggregates) | Maximum time in seconds to wait for the Aggregate to return data before triggering a Communication Exception. Overrides the [default timeout defined at the app level](../../../../getting-started/system-requirements.html#server-request-timeout). |   |   | Property doesn't exist for client-side Aggregates. There is a [maximum value](../../../../getting-started/system-requirements.html#server-request-timeout). |
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
