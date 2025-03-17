---
summary: Explore the supported join types in OutSystems Developer Cloud (ODC) for combining data from multiple entities.
tags: database operations, entity relationships, data aggregation, query optimization, data modeling
locale: en-us
guid: edee2ac8-5d4c-4423-9e26-cce4b0f45f4c
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A8518&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - understand
topic:
  - joins
---

# Supported join types

Usually your data is not stored in a single Entity. So, when performing queries on the data, you need to combine the records that is stored in multiple Entities. This is also known as joining records from multiple Entities.

To do this, just drag the entities into your aggregate. They are automatically joined together, but you can always customize how they are combined in the **Sources** tab. There are four ways to join records from two entities:

* Only fetch records that have a match in both entities.
* Fetch all rows from the first entity, even if there are no matches on the second entity.
* Fetch rows from both entities.
* For each record in the first entity, match it with a record from the second entity.

In the examples below we will combine the following two entities:

![Screenshot of two original database tables before joining](images/originaltables.png "Original Tables")

## Only fetch records with a match

To only retrieve Issues that have an Engineer assigned, use **Only With**.

![Example of 'Only With' join showing matched records between Issues and Engineers](images/onlywith-example.png "Only With Join Example")

Notice how Issues that have no Engineer assigned yet are not returned.

## Fetch all records from an entity, even if they don’t have a match

To retrieve all Issues regardless of whether they have an Engineer assigned to them, use **With or Without**.

In this join type the order of the Entities in the join condition makes a difference in the returned rows. The idea is to retrieve all records from the first entity, and combine the rows of the second entity to them. So if you swap the order of the Entities, you will get a different result.

![Illustration of 'With or Without' join difference with order of entities affecting the result](images/withorwithout-difference.png "With or Without Join Difference")

Notice that for the Issues that have no Engineer assigned, the columns with the Engineer information contain the default values.

## Fetch rows from both entities

To fetch all Issues and all Engineers, even if there is no match between them, use **With**.

![Example of 'With' join fetching all records from Issues and Engineers regardless of matches](images/with-example.png "With Join Example")

Notice that for Issues without an engineer assigned, the columns with the engineer information contain the default values.

For engineers that don’t have an issue assigned to them, the issue information contains the default values.

This option is specially useful for exporting data into third-party systems.

## Combine all records, ignore relationship

To combine each record from an entity with all records of a second entity (for example: to create a list that pairs each team with every adversary team), just make sure that there is no Join defined in the Sources tab.

To pair each team with their adversaries, add the Team entity twice to your aggregate.

![Example of a cross join pairing each team with every adversary team](images/crossjoin-example.png "Cross Join Example")

Then filter the aggregate to ensure that a team is not paired up with itself.
