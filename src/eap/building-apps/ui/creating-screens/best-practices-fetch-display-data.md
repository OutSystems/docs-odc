---
summary: Learn the best practices for fetching and displaying data in OutSystems.
tags:
outsystems-tools:
guid: 65834d5d-b36c-47b0-afc5-43ae35b5bd7d
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=6412-1148
content-type:
  - best practice
---

# Best practices for fetching and displaying data

In OutSystems, you can [fetch data to populate screens](../interaction/fetch-display.md) using aggregates or data actions. Follow these best practices to manage and display data from different sources efficiently.

## Use aggregates to fetch data from database entities

[Aggregates](../../data/fetch-data/aggregate.md) allow you to fetch data using an optimized query tailored to your needs. 

### Recommendations

Use aggregates to fetch data from database entities. Favor using aggregates over SQL queries.

### Benefits

When fetching data from database entities, aggregates offer the following advantages:

* Aggregates are visually defined, making data retrieval more intuitive. They also allow you to preview their outputs in real time.

* Aggregates automatically absorb changes in the data model. 

* Aggregates support combining several entities and advanced filtering.

* Aggregates retrieve only the attributes that are used on the screen.

* Aggregates run asynchronously, allowing users to interact with the app while data loads.

For more information, refer to [Fetch and display data from the database in OutSystems](../interaction/fetch-display.md) and [Displaying Data on Screens](https://learn.outsystems.com/training/journeys/building-screens-with-data-637/displaying-data-on-screens/odc/109).

## Use data actions to fetch complex data from the database or to fetch external data

Data actions allow you to define custom server-side logic. The outputs of a data action can be used in screen widgets.

### Recommendations

Use data actions when:

* Fetching complex data from the database, which you cannot achieve using a single aggregate. 

* Fetching data from external sources (for example, REST APIs).

### Benefits

Data actions can call external REST APIs or execute advanced SQL queries, allowing you to retrieve complex data from the database, which you wouldn't be able to do using aggregates.

For more information, refer to [Displaying Data on Screens](https://learn.outsystems.com/training/journeys/building-screens-with-data-637/displaying-data-on-screens/odc/109).

## Keep the number of fetched records consistent with your needs { #max-records }

Usually, there's no need to display thousands of records on a single screen. For example, a list usually displays only a fixed set of records, then additional records are fetched with the use of pagination or infinite scroll mechanism. If you don't limit the maximum number of records read from the database, all the records that match the criteria will be unnecessarily fetched, increasing database load and response time.

### Recommendation

Keep the number of records fetched by your aggregates and SQL queries consistent with your needs:

* For aggregates, set the **Max. Records** property to match the amount of data you want to display. If you need the total count of records, use the **&lt;Aggregate&gt;.Count**, as it's not limited by the **Max. Records** value.

* For SQL queries, add an SQL clause to the SQL element statement to filter the results at the database level. For example, `SELECT <column_names> FROM <table_joins> LIMIT 10`.

    <div class="info" markdown="1">

    Setting the **Max. Records** property in SQL queries doesn't change its SQL statement. This limit is only applied at the app level to the results returned by the database. 

    </div>

    By limiting the results returned by the query, you no longer rely on the SQL query **.Count** property to get the correct count of records complying with the original query conditions and joins. If you need the total number of records, you must make a separate query to do that count.

### Benefits

Keeping the number of records fetched from the database consistent with your needs optimizes aggregates and SQL queries execution time and improves screen loading. This is especially useful when fetching table records or when an aggregate is used to fetch a single record.

## Don't show a blank screen while data is being fetched

Plan what your app will display to the user while data is being fetched. 

### Recommendations

To avoid showing a blank screen while data is being fetched:

* Fetch smaller data when initializing the app. This renders essential elements while larger data loads in the background. 

* Inform users that data is loading. For example, use loading spinners, progress bars, or skeleton screens. 

### Benefits

By following these recommendations, you avoid the perception of an unresponsive or broken app, improving user experience.

## Avoid fetching a large number of records

Displaying a large number of records all at once is slow and unnecessary, as the user may only need some records at a time. 

### Recommendations

When displaying a large number of records, follow these recommendations:

* Fetch data only on demand by setting the **Fetch** property of your screen aggregates to ```Only on Demand```. For more information, refer to [Fetching Data On Demand](https://learn.outsystems.com/training/journeys/programming-model-645/fetching-data-on-demand/odc/487).

* If you use the list widget, take a lazy loading approach by handling the **On Scroll Ending** event. This approach makes your app load data incrementally as users scroll. ​

* If you use the table widget, use the [pagination](../patterns/navigation/pagination.md) UI pattern to load only a certain number of records each time instead of loading an entire table at once.

### Benefits

Implementing these best practices helps reducing initial load times and server strain, while ensuring a smooth user experience. You can efficiently handle large datasets without overwhelming the user interface.

## Restrict access to sensitive data { #restrict-access }

When fetching sensitive data that depends on the user role or Id, it's not safe to rely on control information from client-side inputs, as it can be manipulated by malicious users.

### Recommendations

Filter your aggregates using the **CheckROLENAMERole()** function to [restrict access sensitive data](../../../user-management/secure-app-with-roles.md#restrict-access-to-data). You can also use the **GetUserId()** function for more restricted access.

![Screenshot showing an aggregate filtered by user role](images/best-practices-fetch-data-restrict-access-odcs.png "Filter your aggregates by user role")

You can reinforce this best practice by [validating user permissions also on the server-side logic](../../logic/best-practices-logic.md#validate-permissions-server-side).

### Benefits

Restricting access to your data brings an additional level of security to your app.
