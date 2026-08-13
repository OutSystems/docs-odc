---
summary: ODC data mashup lets you combine OutSystems entities with external data sources in aggregates or SQL nodes for richer queries and analysis.
tags:
  - Aggregates
  - Data
  - Entities
  - External Databases
  - SQL
locale: en-us
guid: 49e82c30-f818-4e76-9961-1ccae5852e4e
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=6663-458
platform-version: odc
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
coverage-type:
  - understand
isautopublish: true
---

# Combine data from different sources using data mashup

When you integrate your app with external data sources using [OutSystems Data Fabric](../../../integration-with-systems/external-databases/intro.md), you can use **data mashup** in an [aggregate](aggregate.md) or [SQL node](sql/use-sql.md) to fetch combined data from multiple sources. For example, you can mash up your OutSystems [entities](../modeling/entity.md) with an external data source, or mash up two distinct external data sources.

Some benefits of data mashup are:

* Simplified process: You can drag and drop data from different sources, creating custom logic to combine data. This helps you save time and effort.
* Improved data analysis: You can leverage data from various databases to gain deeper insights and make better business decisions.
* Increased flexibility: You get greater flexibility in data analysis and reporting.

![Screenshot showing an integration with external sources and an aggregate using data mashup to combine data from the external entities.](images/data-mashup-odcs.png "Aggregate using data mashup from external entities")

To better understand queries in data mashup, refer to [Writing better queries in data mashup](queries.md).

## Related resources

* [Data mashup transactions](transactions-data-mashup.md)

* [Troubleshooting aggregates that use data mashup](data-mashup-errors.md)

* [Integrate with External Databases (ODC)](https://learn.outsystems.com/training/journeys/integrate-external-databases-odc-2644) online course
