---
summary: OutSystems Developer Cloud (ODC) bootstrap from Excel loads data into an existing entity and handles blank numeric cells.
tags: client-side aggregates, server-side aggregates, data management
locale: en-us
guid: e2c6960b-b589-475a-b0e4-4792bba6a6be
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
  - mentor studio
coverage-type:
  - apply
  - evaluate
topic:
  - bootstrap-excel-blanks
  - bootstrap-test-data-excel
isautopublish: true
---

# Bootstrap an Entity Using an Excel File

You can import data from an Excel file to load data to an entity. This is useful when you are developing and testing your application. This way, you can quickly have your data up and running in the application while developing it.

The bootstrap loads data into an existing entity. If the entity doesn't exist yet, describe it to Mentor Studio, validate the result with your spreadsheet, and then bootstrap the data in ODC Studio.

<div class="info" markdown="1">

If you're using Google Sheets, download your document as an .xlsx file (File > Download > Microsoft Excel), and then bootstrap the data.
</div>

## Create the entity with Mentor Studio

Create the entity by describing it in Mentor Studio, and validate that its names match the Excel sheet and column headers before you bootstrap the data.

In your prompt, name the entity after the sheet, and list one attribute for each column header with its data type. For example, "Create a Place entity with the attributes Name (Text), Address (Text), PhoneNumber (Phone Number), Latitude (Decimal), and Longitude (Decimal)."

For more prompt examples, refer to the data section of [Prompts for Mentor Studio](../../../agentic-development/mentor-studio/prompts.md#data).

For the requirements and the steps to prompt Mentor Studio and review the change, refer to [Modify an app with AI in ODC Studio](../../../agentic-development/mentor-studio/modify-app.md) and [Review and accept the plan](../../../agentic-development/mentor-studio/how-it-works.md#accept-plan). To create the entity manually, refer to [Create an Entity to Persist Data](entity-create.md).

### Validate the entity

The bootstrap maps the sheet to the entity by name. In the **Data** tab of ODC Studio, check the following:

* The entity has the same name as the Excel sheet.
* The entity has one attribute for each column header, and each attribute has the same name as its header.
* The data type of each attribute fits the values in its column. For numeric columns that contain blank cells, refer to the note in [Validate the Excel file](#validate-the-excel-file).

After the entity passes these checks, continue with [Validate the Excel file](#validate-the-excel-file) and [Bootstrap the data](#bootstrap-the-data).

## Validate the Excel file

1. Open the Excel file, check that the Excel sheet has the name of the Entity and the column headers have the names of the entity attributes.

1. Close the Excel file. The bootstrap can't read the Excel file if it's open.

<div class="info" markdown="1">

If you have blank cells in your spreadsheet and are getting import errors because it cannot interpret blank cells as numeric, either integer or decimal. You have two choices:

* Change the spreadsheet. Change blank cells defined as numeric fields to 0.

* Change the import process. Define the numeric fields as Text. Then, use a [Data Type Conversion](../data-types.md#data-type-conversions) function such as **TextToDecimal** to convert the text to Decimal or Integer.

</div>

## Bootstrap the data

The bootstrap action runs in ODC Studio. To bootstrap data from the first sheet of an Excel file to an existing entity, follow these steps:

1. In ODC Studio, go to the Data tab, right-click on the entity and in the Advanced menu, choose 'Create Action to Bootstrap data from an Excel...'.

1. Select the Excel file, check the mappings to see if they're correct and click on **Proceed**.
    ODC Studio creates:

    * An action with the bootstrap logic named "Bootstrap&lt;entityname&gt;" in the Server Actions folder in the Logic tab.

    * A structure with the content of the Excel file named "Excel_&lt;filename&gt;" in the Structures folder in the Data tab.

    * A resource with the Excel file in the Resources folder in the Data tab.

    * A timer to execute the action at publish time named "Bootstrap&lt;entityname&gt;" in the Timers folder in the Events tab.

1. Publish to bootstrap the data.

When you publish the app, it executes the action to bootstrap the data. If the entity already has data, the action with the bootstrap logic is **not** executed.
