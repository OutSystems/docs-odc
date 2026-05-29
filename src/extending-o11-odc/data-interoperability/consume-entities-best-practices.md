---
guid: d741a43a-8bcd-47e0-a9d5-d7a3da2cf8ea
locale: en-us
summary: Learn the development best practices for consuming O11 entities in ODC apps.
figma: https://www.figma.com/design/epaiN2jasbbKgJA0iSYfZn/Extending-with-ODC?node-id=2711-37
coverage-type:
  - understand
topic:
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - Developer
  - Front-end developer
tags: entities,data interoperability
outsystems-tools:
  - odc studio
helpids:
isautopublish: true
---

# Best practices for consuming O11 entities in ODC apps

This page describes development behaviors and best practices to consider when [consuming O11 entities in ODC apps](consume-entities.md).

## Writing SQL queries

When writing SQL queries for these entities, you must use a **syntax based on ANSI-92**. For more information, refer to [how to use ANSI-92 syntax in SQL nodes](../../eap/building-apps/data/fetch-data/sql/ansi-92-syntax.md).

## Working with O11 static entities {#o11-static-entities}

OutSystems is working to enable the consumption of O11 static entities as ODC static entities, which is a [limitation](data-interop.md#temporary-limitations) for now.

Currently, when you expose a static entity from an O11 app, it becomes a regular, read-only external entity in ODC. The "static" nature and its records are not available at design time in ODC Studio.

<div class="info" markdown="1">

**Auto-number** record identifiers (IDs) for an O11 static entity are not guaranteed to be the same across your different O11 environments. For these cases, avoid writing logic in ODC that compares with a specific hard-coded ID from an O11 static entity, as this can lead to unexpected behavior in different stages.

</div>

## Transactions

Similarly to other [external data source integrations](../../eap/building-apps/data/fetch-data/transaction-external-entities.md), ODC creates an independent transaction on the O11 database for each O11 entity action.

When combining O11 entities with other external data sources in your ODC app, be aware of the [transaction behavior in data mashup scenarios](../../eap/building-apps/data/fetch-data/transactions-data-mashup.md), especially when performing write operations before querying the combined data.

<div class="info" markdown="1">

[Data mashup with O11 Oracle entities](#oracle-mashup) is currently not supported.

</div>

If you require transactional consistency across multiple O11 records - for example, creating an Order and the Order Lines together - create a wrapper REST API in O11 that handles the transaction internally. Then, use [logic interoperability](../logic-interoperability/logic-interop.md) to consume that O11 logic in your ODC app.

## Performance

The scalability of your ODC apps that consume O11 data depends on the performance and capacity of the underlying O11 database. At the same time, high volumes of requests from ODC - such as those from high-traffic B2C apps or AI agents - can increase the load on your O11 database, potentially affecting the performance of your O11 applications.

To ensure stability across both platforms:

* **Design your O11 data model for performance:** Ensure proper indexing and normalization to handle queries efficiently. Refer to the [O11 data model best practices](https://success.outsystems.com/documentation/11/onboarding_developers/outsystems_platform_best_practices/#data-model) for more details.

* **Write efficient queries in your ODC apps:** Optimize data fetching by selecting only necessary columns and limiting result sets. Avoid executing SQL queries inside logic loops, as this generates database communication overhead. For more details, refer to the best practices for [fetching and displaying data](../../eap/building-apps/ui/creating-screens/best-practices-fetch-display-data.md) and [querying data using SQL](../../eap/building-apps/data/fetch-data/sql/use-sql.md). When combining O11 entities with other external data sources in your ODC app, follow the [best practices for data mashup queries](../../eap/building-apps/data/fetch-data/queries.md).

    <div class="info" markdown="1">

    [Data mashup with O11 Oracle entities](#oracle-mashup) is currently not supported.

    </div>

* **Test your apps:** Conduct load testing to verify that your O11 database can handle the additional concurrent load from ODC apps without degradation. Refer to [Testing apps](../../eap/testing-apps/testing-apps.md) for further details.

* **Monitor performance:** Use [ODC Analytics](../../eap/monitor-and-troubleshoot/app-health.md) to track the performance of your ODC app. Since the data resides in O11, use [O11 monitoring tools](https://www.outsystems.com/tk/redirect?g=636a2bea-478d-4703-aaf8-e2f8ee514f2c) to detect potential issues or bottlenecks.

## Consuming O11 Oracle entities in ODC apps

This section describes ODC behavior when you consume O11 Oracle entities in an app, and some known issues that you need to consider.

### Handling empty text

Due to [Oracle DBMS's representation of empty strings](https://www.outsystems.com/tk/redirect?g=9ae75fbb-3c7b-4307-9b9a-9e18bcb16017), when using an Oracle database, OutSystems 11 writes a single space character (`" "`) to represent an empty text value, instead of an empty string (`""`). This behavior applies to **Text**, **PhoneNumber**, and **Email** data types.

When consuming O11 Oracle entities in ODC apps, **Data Fabric follows the same O11 behavior** for read and write operations, adding a single space character (`" "`) to represent an empty text value.

However, ODC may behave differently from O11 in some empty text handling situations. The following behaviors apply when using the built-in functions `Trim()`, `ToLower()`, `ToUpper()`, `Substr()`, `Index()`, and the `+` (concatenation) operator:

* ODC maintains a **consistent behavior across aggregates and SQL nodes** for comparisons with an empty string (`""`) or the indicated functions and operator. This contrasts with O11, where **SQL nodes** don't include the single space character (`" "`) to match aggregates behavior.

* When using the indicated functions or operator on **entity attributes that return empty text**, ODC replaces the result with a single space character (`" "`). This ensures that expressions evaluate as `True` for string-to-string equality. Consequently, some expressions that evaluate as `False` in O11, evaluate as `True` in ODC, for example:

    * `Trim("") = Trim("")`
    * `Trim(" ") = Trim("")`
    * `ToLower("") = ToLower(" ")`

### Known issues

There are currently some known issues that you need to account for in your ODC apps when consuming O11 Oracle entities.

#### Redundant empty filters in aggregates

In aggregates, when filtering by an empty string and a single space at the same time on the same literal column, no records are returned, even though these filters are equivalent. For example:

* `MyO11Entity.TextAttribute = ""` and `MyO11Entity.TextAttribute = " "`

#### Displayed default values

When creating new records in runtime, the default values for **Email** and **Phone** types are being shown with quotation marks in the UI.

![ODC app showing default values with quotation marks](images/consume-best-practices-default-values-diag.png "ODC app showing default values with quotation marks")

#### Data mashup not supported {#oracle-mashup}

Using [data mashup](../../eap/building-apps/data/fetch-data/data-mash.md) to combine O11 Oracle entities with other external systems isn't currently supported in ODC apps.

Although basic queries might occasionally work, the system may not reliably handle complex queries in this setup.
