---
guid: 2eebb3da-895b-4503-9bea-36ed9904018e
locale: en-us
summary: Learn how ODC Studio previews File attribute values in Edit Data, Advanced SQL test queries, and the debugger.
figma: https://www.figma.com/design/tBZkZppoX8yflqZ57AJrtt/File-Data-Preview?node-id=8389-2&p=f&t=d0UgNlZxOOnCJWEh-0
coverage-type:
  - understand
topic:
  - edit-data-service-studio
  - file-storage
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - Developer
  - Front-end developer
tags:
  - Aggregates
  - Data
  - Debugging
  - Entities
  - SQL
  - Testing
outsystems-tools:
  - odc studio
helpids:
isautopublish: true
---

# Preview file data in ODC Studio

When an entity or Aggregate has a **File** attribute, ODC Studio previews the file's metadata instead of its content. Understanding this preview format helps you interpret **File** values while you inspect data, test queries, or debug your app.

## Preview file values in Edit Data

When you open **Edit Data** for an entity with a **File** attribute, ODC Studio shows the attribute's metadata instead of its content, formatted as `MIMEType`. For example, a PNG image previews as `image/png (4107463 bytes)`. To learn how to open **Edit Data**, refer to [Edit data in ODC Studio](../edit-data.md).

Unlike **BinaryData** cells, which let you upload a file directly, **File** cells are read-only in Edit Data. The **Upload** and **Delete** actions are disabled for **File** attributes. To add or replace a **File** attribute's content, use your app's logic instead, for example, an **Upload** widget or a server action.

![Screenshot showing a read-only File cell with disabled Upload and Delete actions in the ODC Studio Edit Data grid](images/file-preview-edit-data-odcs.png "Read-only File Cell in Edit Data")

## Preview file values in Advanced SQL test queries

When you test an **Advanced SQL** query that returns a **File** column, ODC Studio previews the column using the same `MIMEType` format as Edit Data.

![Screenshot showing a File column preview in an Advanced SQL test query in ODC Studio](images/file-preview-advanced-sql-odcs.png "File Column Preview in Advanced SQL Test Query")

## Preview file values while debugging

When you debug an action with a **File** variable, the variable inspector shows the value in the same format, mirroring how it displays **BinaryData** variables as `Binary`. For example, a **File** variable displays as `image/png (4107463 bytes)`.

![Screenshot showing a File variable value in the ODC Studio debugger variable inspector](images/file-preview-debugger-odcs.png "File Variable Preview in the Debugger")

## File in the data type picker

In the data type picker for entity attributes, ODC Studio groups **File** together with **BinaryData** under a **File Storage** category, separate from the basic data types.

![Screenshot showing the File data type grouped with BinaryData in the ODC Studio data type picker](images/file-preview-type-picker-odcs.png "File and BinaryData in the Data Type Picker")

## Next steps

After understanding how ODC Studio previews **File** values, you can explore related tasks:

* [The File data type](binaries-native-cloud.md): learn when to use **File** instead of **BinaryData**.
* [File lifecycle](file-reference-lifecycle.md): learn how a **File** reference behaves in entities and aggregates, and how ODC manages it over time.
* [Edit data in ODC Studio](../edit-data.md): learn how to add, delete, and modify entity records, including **BinaryData** attributes.
