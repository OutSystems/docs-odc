---
summary: You can import data from an Excel file to load data to an entity.
tags:
locale: en-us
guid: e2c6960b-b589-475a-b0e4-4792bba6a6be
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---
# Bootstrap an Entity Using an Excel File

You can import data from an Excel file to load data to an entity. This is useful when you are developing and testing your application. This way, you can quickly have your data up and running in the application while developing it.

<div class="info" markdown="1">

If you're using Google Sheets, download your document as an .xlsx file (File > Download > Microsoft Excel), and then bootstrap the data. 
</div>

## Validate the Excel file

1. Open the Excel file, check that the Excel sheet has the name of the Entity and the column headers have the names of the entity attributes.

1. Close the Excel file. The bootstrap can't read the Excel file if it's open.

<div class="info" markdown="1">
    
If you have blank cells in your spreadsheet and are getting import errors because it cannot interpret blank cells as numeric, either integer or decimal. You have two choices:

* Change the spreadsheet. Change blank cells defined as numeric fields to 0.

* Change the import process. Define the numeric fields as Text. Then, use a [Data Type Conversion](../data-types.md#data-type-conversions) function such as **TextToDecimal** to convert the text to Decimal or Integer.

</div>

## Bootstrap the data

To bootstrap data from the first sheet of an Excel file to an existing entity, follow these steps:

1. In ODC Studio, go to the Data tab, right-click on the entity and in the Advanced menu, choose 'Create Action to Bootstrap data from an Excel...'. 

1. Select the Excel file, check the mappings to see if they're correct and click on **Proceed**.
    ODC Studio creates:

    * An action with the bootstrap logic named "Bootstrap&lt;entityname&gt;" in the Server Actions folder in the Logic tab.

    * A structure with the content of the Excel file named "Excel_&lt;filename&gt;" in the Structures folder in the Data tab.

    * A resource with the Excel file in the Resources folder in the Data tab.

    * A timer to execute the action at publish time named "Bootstrap&lt;entityname&gt;" in the Timers folder in the Processes tab.

1. Publish to bootstrap the data.

When you publish the app, it executes the action to bootstrap the data. If the entity already has data, the action with the bootstrap logic is **not** executed.
