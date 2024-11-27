---
summary: The number of records fetched from the database is not set in Aggregate.
tags:
guid: c3b5a66a-e289-4032-a76c-0343832f8925
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3525-223&node-type=CANVAS&t=4GWqMD3OdwPTBIl5-0
content-type:
  - troubleshooting
  - reference
---

# Unlimited records in Aggregate

The number of records fetched from the database isn't set in Aggregate.

## Impact

More records are fetched from the database than are used by the application, resulting in useless I/O and memory consumption.

## Why is this happening?

The issue occurs because Aggregates fetch all records by default, leading to unnecessary data retrieval and potential performance problems.

![The Max. Records property of an Aggregate is not set.](images/odcs-max-records-aggregate.png "Max. Records property not set")

## How to fix

Set the **Max. Records** parameter of the Aggregate to the required amount of records.

For more information, refer to [best practices for fetching and displaying data](../../../building-apps/ui/creating-screens/best-practices-fetch-display-data.md#max-records).
