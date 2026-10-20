---
summary: Excel to Record List in OutSystems Developer Cloud (ODC) imports Excel data in server actions, maps sheets, and validates mandatory values.
tags:
  - Data
  - Entities
  - Logic
guid: f597eb92-f243-48a3-abd8-fc2fffab2ff2
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=6717-13
api-render: false
outsystems-tools:
  - odc studio
  - mentor studio
coverage-type:
  - apply
  - evaluate
topic:
  - excel-to-record-list
content-type:
audience:
  - Developer
isautopublish: true
---

# Excel to Record List

The **Excel to Record List** action converts an Excel object to a Record List. This article explains how you can use the **Excel to Record List** action to load data from an Excel file and save it in your app at runtime.

The Excel To Record List is only available in Server Actions. In Reactive Web and Mobile apps, you must send the uploaded file to the server and then process it in a Server Action.

## Prerequisites {#prerequisites}

To use **Excel To Record List** action, you need an entity or structure that matches the content of the Excel (.xls, .xlsx or .xlsb) file you want to import. OutSystems matches the attribute labels of the entity or structure specified in the Record Definition property with column headings in the Excel file. Entity attributes without a corresponding column in the Excel file get the default value of their data type (for example, "" for a Text attribute).

## Import Excel data with Mentor Studio

Add the **Excel to Record List** action to a Server Action by describing the import in Mentor Studio, and validate the properties and the data flow before you publish.

In your prompt, include the following:

* The Server Action
* The entity or structure that defines the records
* The Excel file source
* The entity action that saves the records

For example, the following sentences form one prompt:

* "In the ImportEmployees Server Action, use the Excel to Record List action to read the uploaded file with the Employee entity as the Record Definition."
* "Call CreateOrUpdateSomeEmployees with the resulting list as the Source List."

### Validate the conversion

The platform guarantees that the model is valid, and you decide whether the import loads the data you expect. Check the following against the [Prerequisites](#prerequisites) and the [Properties](#properties) on this page:

* The action is in a Server Action, because **Excel to Record List** is only available there.
* The **Record Definition** is the entity or structure whose attribute labels match the column headings in the Excel file.
* The **File Content** is a Binary Data value that holds the Excel file.
* The **Sheet Name** is set when you import a specific sheet. Without a **Sheet Name**, the action imports the first sheet, unless the file has a sheet named 'Sheet1'.
* The **Source List** of the entity action is the output of **Excel to Record List**.
* The logic validates mandatory values, because **Excel to Record List** doesn't validate them. Attributes without a column get the default value of their data type.

## Import Excel data manually in ODC Studio

The following example shows a scenario in which you want to add or update the names and addresses of your current employees in an entity called Employee.

1. In a Server Action, add the **Excel to Record List** action to the logic.

1. Define the **Record Definition** property as the **Employee** entity.

1. Define the **File Content** property as the Excel file you are importing.

    ![Screenshot showing the ExcelToRecordList action in a Server Action with properties for Name, Description, Record Definition, File Content, and Sheet Name.](images/excel-record-odcs.png "Excel to Record List Action in Server Action")

1. (Optional) To import a specific sheet, you must specify the sheet name in the **Sheet Name** property. By default, OutSystems imports data from the first sheet.

1. Add the **CreateOrUpdateSomeEmployees** entity action and define its **Source List** as the **ExceltoRecordList**.

    ![Screenshot showing the CreateOrUpdateSomeEmployees action in a Server Action with the SourceList property set to ExcelToRecordList.](images/action-excel-record-odcs.png "Create or Update Employees Action")

1. (Optional) Add a Server Action to validate the imported data and ensure it complies with your business rules.

    **Note**:  Excel to Record doesn't validate if the Excel file data has mandatory values.

## Properties {#properties}

| Name | Description | Mandatory | Observations |
| --- | --- | --- | --- |
| Name | Identifies an element in the scope where it is defined, like a screen, action, or app/library. | Yes | |
| Description | Text that documents the element. | | Useful for documentation purposes. The maximum size of this property is 2000 characters. |
| Record Definition | Entity or structure that defines the structure of the data that you want to load. | Yes | The attribute labels must match the column header names in the imported Excel. |
| File Content | Holds the Excel file. | Yes | The expected data type is Binary Data. |
| Sheet Name | Name of the Excel sheet to import. By default, the first sheet is imported unless a sheet named 'Sheet1' exists in the file. | | The expected data type is Text. |

## Related resources

The following resources describe prompt examples, the steps to prompt Mentor Studio, the reverse conversion, and bootstrapping an entity from Excel.

* For more prompt examples, refer to [Prompts for Mentor Studio](../../agentic-development/mentor-studio/prompts.md#logic).
* For the requirements and the steps to prompt Mentor Studio and review the change, refer to [Modify an app with AI in ODC Studio](../../agentic-development/mentor-studio/modify-app.md) and [Review and accept the plan](../../agentic-development/mentor-studio/how-it-works.md#accept-plan).
* [Record List to Excel](record-list-excel.md)
* [Bootstrap an Entity Using an Excel File](../data/modeling/excel-bootstrap.md)
* For what the platform guarantees and what you validate, refer to [Platform guarantees and AI interpretation](../../agentic-development/odc-ai-and-platform.md).
