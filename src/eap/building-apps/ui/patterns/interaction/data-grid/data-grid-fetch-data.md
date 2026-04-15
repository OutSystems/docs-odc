---
tags: data grid, odc, data fetching, grid configuration, outsystems
summary: Learn to fetch and display data in the OutSystems Data Grid (ODC) for reactive web apps, including configuration and customization properties.
guid: f7f7cc5c-680f-47c3-ba1f-d4346729745a
locale: en-us
app_type: reactive web apps
platform-version: odc
content-type:
  - tutorial
  - procedure
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=6245-11
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
  - forge
---
# Fetch data for OutSystems Data Grid

<div class="info" markdown="1">

Applies to the OutSystems UI framework only.

</div>

**Prerequisites**

* Install the ODC Data Grid component from Forge.
  
* In ODC Studio, add the necessary Data Grid public elements to your app.

## Fetch data from a database

This example fetches data from a database and displays it in the grid. (This example does not define any column structure.)

<!-- Add the Grid block to a screen and learn about it's placeholders -->
### 1. Add the Grid widget to the screen

1. In ODC Studio, in the toolbox, search for the Grid widget and drag it into the **MainContent** area of your app's screen.

    ![Screenshot showing the process of dragging the Grid block into the MainContent area in ODC Studio.](images/grid-widget-odcs.png "Adding Grid Block to MainContent")

    The Grid widget is added to the screen.

    ![Screenshot displaying the Grid widget added to the screen in ODC Studio.](images/grid-widget-drag-odcs.png "Grid Widget Added to Screen")

    By default, the Grid widget contains the following placeholders:

    * ContextMenu
    * Loading (displayed while data is being fetched from the server)
    * NoResults (displayed when no results are returned)
    * GridColumns
    * ServerSideInformation (adds no functionality, only provides guidance for server-side pagination)

    ![Screenshot displaying the default placeholders within the Grid widget, including ContextMenu, Loading, NoResults, GridColumns, and ServerSideInformation.](images/grid-placeholders-odcs.png "Default Grid Widget Placeholders")

    You can change the content of these placeholders as required.

<!--Create a data action to fetch data to display in the Grid, serialize data as JSON-->
### 2. Create a data action to fetch the data

1. On the **Interface** tab, right-click your screen and select **Fetch Data from Other Sources**.

    ![Screenshot showing the creation of a Data Action to fetch data for the grid.](images/grid-fetch-data-odcs.png "Creating a Data Action")

1. Enter a name for the action's output parameter (for example, Products) and ensure the **Data Type** is **Text**.

    This output parameter is used to receive the data fetched from the database.

    ![Screenshot of the output parameter settings for a Data Action with the Data Type set to Text.](images/grid-output-par-odcs.png "Setting Output Parameter for Data Action")

1. To build the logic for the **GetAllProducts** data action, double-click it. The data action flow is displayed. Switch to the **Data** tab and drag the data source entity onto the flow.

    ![Screenshot showing the process of dragging a data source entity onto the flow in ODC Studio.](images/grid-drag-entity-odcs.png "Dragging Data Source Entity")

    An aggregate (in this example, GetProducts) is automatically created.

1. The Grid block receives data in JSON format. Therefore, after the aggregate, you must serialize its results. To do this, from the **Toolbox**, drag the **JSONSerialize** onto the flow and place it between the **GetProducts** aggregate and the **End** node.

1. Set the **Data** property to the aggregate result, `GetProducts.List`. The list of the aggregate results is passed to the **JSONSerialize**.

    ![Screenshot showing the aggregate result in the data action flow in ODC Studio.](images/grid-aggregate-result-odcs.png "Aggregate Result")

1. Next, assign the resulting JSON to the `Products` output parameter by dragging an **Assign** onto the flow after **JSONSerialize** and assigning the `JSONSerialize.JSON` to `Products`. The `Products`output of the `GetAllProducts` data action is what is used by the Grid widget on the screen.

    ![Screenshot showing the process of assigning JSONSerialize.JSON to the Products output parameter in the data action flow.](images/grid-set-assign-odcs.png "Assigning JSON to Output Parameter")

   <!--Bind the results of the data action to the Grid data property-->

### 3. Bind the data action's results to the Grid data property

1. Return to the main screen and select **Structures\Grid** to display its properties.

1. On the **Properties** tab, set the **Data** to the output of the Data action, in this example, `GetAllProducts.Products`.

1. Bind the Grid's **IsDataFetched** property to the Data Action property **IsDataFetched**.

    ![Screenshot showing the process of setting the Grid's Data property to the output of the Data action in ODC Studio.](images/grid-data-prop-odcs.png "Binding Grid Data Property")

<!--Add Column blocks for each attribute to display in the Grid, learn the type of block to use-->
### 4. Display the data

1. Populate the **Structures\Grid** block with all the columns you want to display in the grid. The columns are added to the **GridColumnsPlaceholder**.

1. Drag the relevant Column type to the **GridColumnsPlaceholder**.

After following these steps and publishing the module, you can test the component in your app. The result is a screen with a Grid widget that can display data from an aggregate.

![Screenshot of the final result showing data displayed in the OutSystems Data Grid component.](images/grid-result-odcs.png "Data Grid Component Result")

## Next steps

* [Edit data in OutSystems Data Grid](data-grid-edit.md)
* [Save changes in OutSystems Data Grid](data-grid-save.md)

## Grid block properties

The following table lists all the properties of the Grid block, its data types, and their description.

| **Properties** | **Description** |
| --- | --- |
| Data (Text): Mandatory | The data displayed in the Grid. |
| IsDataFetched (Boolean): Mandatory | Defines what is displayed while data is loading. |
| GridHeight (Integer): Optional | Sets the Grid's height in pixels. Default height is 400 pixels. |
| HasGroupPanel (Boolean): Optional | Enables the group panel to allow dragging columns and apply the grouping by the fields corresponding to the dragged columns. Default value is True. |
| AllowColumnEdit (Boolean): Optional | Allows columns to be edited. Default value is False. |
| AllowColumnReorder (Boolean): Optional | Allows columns to be reordered. Default value is True. |
| AllowColumnResize (Boolean): Optional | Allows column width to be resized. Default value is True. |
| AllowColumnSort (Boolean): Optional | Allows sorting data by column. Default value is True. |
| KeyBinding (Text): Optional | Set the primary key field of the data. Expected format: 'Entity.Attribute'. <br/>Use this field when doing server-side validations. <br/> Don't refresh the grid after adding lines. Combine with UpdateAddedLineKey and GetRowNumberByKey actions. |
| RowHeight (Integer): Optional | Sets the row height in pixels. Default height is 48 pixels. |
| RowsPerPage (Integer): Optional | Sets the number of rows displayed per page. Default value is 50. |
| ShowAggregateValues (Boolean): Optional | Set to True to display a line below the grid with the column values aggregated (sum, min, max, etc.). <br/>By default, the parameter is set to False. <br/>To define the aggregation function of a given numeric (Number or Currency) column, use the SetColumnAggregate client action. |
| SanitizeInputValues (Boolean): Optional | Set True to assure the values inputed in the grid will be sanitized or False if you want to explicitly allow custom code to run. |
| ServerSidePagination (Boolean): Optional | Set to True if you want to enable server-side pagination. Default value is False. |
| RowHeader (RowHeader Identifier): Optional | Defines what is shown on the first column of the grid. Default value is ``Entities.RowHeader.RowNumber``. |
