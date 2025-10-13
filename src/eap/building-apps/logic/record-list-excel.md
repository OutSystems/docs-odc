---
summary: Convert record lists to Excel files using OutSystems Developer Cloud (ODC) by defining the necessary server actions, parameters, and entities for efficient data export.
tags: record list, excel export, data conversion, mobile apps, reactive web apps
guid: 5f26092b-0d42-4e47-8203-1d25e5d775c7
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=6728-2
api-render: false 
outsystems-tools:
  - odc studio
coverage-type:
content-type:
audience:
  - frontend developers
  - full stack developers
---

# Record List to Excel

The **Record List to Excel** action converts a Record list to an Excel file. This article explains how you can use the Record List action to convert your data into an Excel file.

## Convert a Record List to Excel

The following example shows a scenario in which you export a list of employees from an Entity called **Employee** into an Excel spreadsheet.

1. In a Server Action, create an Output Parameter called **ExcelContent** with a **Binary Data** data type.

1. Drag an **Aggregate** node and add the **Employee** Entity as a source.

1. Drag the **Record List to Excel** Action and define the **Record List** parameter as **GetEmployees.List**.

1. Drag an **Assign** node and assign the output of **Record List to Exce**l to the **ExcelContent** Output Parameter.

    ![Screenshot of the Assign node in the ExportEmployeeToExcel action, showing the assignment of the RecordListToExcel output to the ExcelContent output parameter.](images/assign-odcs.png "Assign Node in ExportEmployeeToExcel Action")

1. (Optional) You can omit which information is exported into Excel. For example, you may want your employees' names but not their addresses. In the previous logic, you can untick the **Employee.Address** attribute to ensure it's not exported.

    ![Screenshot of the Record List to Excel action configuration, showing the selection of attributes to be included in the Excel export.](images/select-odcs.png "Record List to Excel Action Configuration")

## Properties

|Name|Description|Mandatory|Default value|Observations |
|---|---|---|---|---|
|Name|Identifies an element in the scope where it's defined, like a screen, action, or app/library.| Yes| RecordListToExcel1 | |
|Description| Text that documents the element.  | No | | Useful for documentation purposes. The maximum size of this property is 2000 characters. |
|Record List| Holds the list of records to be exported to an Excel file |Yes | | The required type for this property is **Record List**.  |

## Related resources

* [Excel to Record List](excel-record-list.md)
