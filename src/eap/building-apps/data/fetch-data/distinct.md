---
summary: Learn how to retrieve distinct values from a database using OutSystems Developer Cloud (ODC) by grouping entity attributes in aggregates.
tags: database operations, data aggregation, entity management, data retrieval, aggregates
locale: en-us
guid: b72114bf-98ec-4f22-89b6-e162569612a1
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A8282&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
content-type:
  - procedure
---

# Get distinct values from the database

Database tables may have columns containing repeated values. There are situations when you only want to get the distinct values, instead of all the data including the repetitions. To obtain distinct values of entity attributes, you can use an aggregate with grouped columns.

To get distinct values of an entity attribute:

1. In an aggregate in the action flow, add the entity.

1. Right-click on the attribute for which you want to obtain distinct values, and choose to group by the attribute.

![Screenshot showing how to group by a single attribute in an aggregate to get distinct values](images/distinct.png "Grouping by a Single Attribute")

The aggregate only outputs the attribute values that are grouped.

To get distinct values using multiple entity attributes, select all the required attributes and choose to `Group by selected attributes`.

![Screenshot demonstrating grouping by multiple attributes in an aggregate for distinct values](images/distinct-2.png "Grouping by Multiple Attributes")
