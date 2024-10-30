---
summary: Learn to write efficient queries in ODC using best practices for joins, filters, aggregates, and sorting.
tags: 
guid: eb941889-6a5e-4e81-a570-80321841e5c1
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=5399%3A383&mode=design&t=SWFFXJVfxBN7UhUU-1 
---

# Writing better queries in data mashup 

To better understand Joins in OutSystems, refer to the [Supported Join Types](supported-join-types.md) documentation. In OutSystems, joins are represented using the following terminology:

* Inner Join = Only With
* Left Join = With or Without
* Full Join = With

You can define a left join using the With or Without join type. You effectively create a right join by swapping the entities, moving the one on the right to the left.

![Diagram showing different types of database joins: Left Join, Right Join, Inner Join, and Full Outer Join.](images/different-joins.png "Different Types of Joins")

To write better queries, you need to understand the following joins:

* An equi-join matches rows from two tables based on the equality operator (=) applied to specified columns.
* A full equi-join, also known as a full outer join, returns all rows from both tables where the join condition is met.
* A partial equi-join resembles an equi-join, but not all rows are included in the result because there isn't a matching condition in both tables.
* A cross join is the same as an Only With Join with an always true condition.
* The outer side of a With or Without Join is the left side. For a right join, it would be the right side.
* A full equi-join compares attributes with "=" and "AND", for example:
    * `ON a.id = b.id`
    * `ON a.id = b.id AND a.int = b.int`
* A partial equi-join combines equi-join conditions with non-equi conditions using "AND", for example: 
    * `ON a.id = b.id AND (a.int > b.int OR a.int > 1)`
* A non-equi-join covers everything else, for example:
    * `ON a.id = b.id OR a.int = b.int`
    * `ON a.int > b.int`

## Best practices

* Only select attributes you intend to use for mashup.
* Avoid binary data attributes due to their impact on performance.
* Avoid full outer and cross joins.
* When using entities from the same database, join them first before joining entities from other databases, for example: 
    * `db1.a With or Without db1.b With or Without db2.c` - Not Recommended 
    * `(db1.a With or Without db1.b) With or Without db2.c` - Recommended 
* Ensure to index attributes used in filters and join conditions in the databases. 
* Use similar data types for attributes used in the join condition. For example, when joining on string attributes, ensure the allowed length is the same in both databases.
* Queries that work fine in ODC Studio data preview may fail in runtime due to exceeding the execution plan cost limit. This can happen because:
    * Test query limits the number of records, reducing plan cost.
    * Entities in QA or Production environments may have more records than those in the Development environment.
* In mashup queries, use With or Without instead of Only With.
* Use aggregate functions (e.g., avg, count, sum) carefully in queries that combine data from different sources or handle large volumes of data in respective entities.
* In a With or Without join, apply aggregate functions (e.g., avg, count, sum) to the left entity.

### Join conditions      

* Use a full or partial equi-join condition, for example:

    * `ON a.id = b.id` - Recommended 
    * `ON a.id = b.id AND a.id2 = b.id2` - Recommended 
    * `ON a.id = b.id AND a.date <> b.date` - Recommended 
    * `ON a.id = b.id OR a.id2 = b.id2` - Not Recommended 
    * `ON a.id > b.id` - Not Recommended 
* Avoid nullable attributes in the join condition for SQL Server and SAP entities.
* Do not write predicates with literals or dynamic parameters in the join condition; use a filter instead, for example:
    * `ON a.id = b.id AND a.id = 1` - Not Recommended 
    * `ON a.id = b.id WHERE a.id = 1` - Recommended 

### Filters

* Using predicates combined with "AND" is the best way to minimize fetching of unnecessary data, for example: 
    * `ON a.date = b.date WHERE a.date < '1990-01-01' ` -  Not Recommended 
    * `ON a.date = b.date WHERE a.date < '1990-01-01' AND b.date < '1990-01-01' ` - Recommended 
* Try to build complex filters using "AND" at the top level and keep filters for each entity in separate parts, for example: 
    * `ON a.col = b.col WHERE (a.col = 3 AND a.int < 3) OR (a.col = 3 AND b.int > 1)` - Not Recommended 
    * `ON a.col = b.col WHERE a.col = 3 AND b.col = 3 AND (a.int < 3 OR b.int > 1)` - Recommended 

### Aggregate functions and grouping
    
* Prefer to use Only With Joins with aggregate functions and/or grouping since this can often allow the aggregate to be split and pushed down to the databases.
* The `COUNT` function can be resource-intensive, depending on the number and volume of entities involved. The [Pagination UI](../../ui/patterns/navigation/pagination.md) pattern worsens this by executing an additional `COUNT` query to calculate and display the total number of records, which can cause performance issues. To mitigate these concerns, consider using other pagination patterns. [Forge](https://www.outsystems.com/forge/list?q=&t=&o=latest-submitted&tr=False&oss=False&c=%20&a=&v=odc&hd=False&tn=&scat=forge) offers more efficient alternatives.

### Sorting

* Sorting can significantly affect performance. If you anticipate many records, performing any required sorting in your app rather than in the aggregate is advisable.

## Supported use cases

### Joining a large entity to a large entity across two systems

* Limit the amount of data fetched using Max Records.
* Use a full or partial equi-join condition, for example:
    * `ON a.id = b.id` - Recommended 
    * `ON a.id = b.id AND a.id2 = b.id2` - Recommended 
    * `ON a.id = b.id AND a.date <> b.date` - Recommended 
    * `ON a.id = b.id OR a.id2 = b.id2` - Not Recommended 
    * `ON a.id > b.id` - Not Recommended 
* Avoid using string attributes when mashups with Salesforce / SAP.
* Don't sort by any attributes. Do any required sorting in your application logic.

When best practices are followed:

* The queries for both entities will sort records based on the equi-keys in the join condition in ascending order with nulls last.
* A merge join algorithm joins the records in the Data Fabric.
