---
summary: Learn the best practices for managing data in OutSystems.
tags: 
guid: 858e8c87-2c13-4803-b279-008726bb77ea
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: 
---

# Best practices for data management

The following are recommended best practices for data management that help you design efficient and scalable applications.

## Implement data purging and archiving strategies when dealing with a large volume of data { #data-purging-archiving }

When dealing with a large volume of application data, the high growth of data may lead to application performance deterioration over time.

### Recommendations

If you expect your application to handle a large volume of data, consider the implementation of [data purging](./data-purging.md) and [data archiving](./data-archiving.md) mechanisms:

* **Data purging:** Mechanism that permanently deletes inactive or obsolete records from the database. Consider it for entities with an evident high-growth rate, which can quickly achieve considerable volumes of data.

* **Data archiving:** Mechanism that stores data that's no longer relevant for daily operations in a separate location, while still retaining it for future reference or regulatory compliance, as it remains important to the organization.

The following criteria can help you determine if these mechanisms are necessary for your application:

* Forecast the growth of your data during the design phase, based on business knowledge and existing metrics. If you don’t have enough information, take a conservative approach and consider the high growth of the data.

* [Monitor the application performance](../../../monitor-and-troubleshoot/app-health.md) to identify long response times for specific requests involving entities that may be good candidates for archiving.

### Benefits

Implementing purging and archiving strategies improves **runtime performance** and prevents scenarios of application performance deterioration. Since the volume of active data is reduced, queries take less time to execute and the application reacts faster.
