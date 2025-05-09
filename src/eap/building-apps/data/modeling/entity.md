---
summary: OutSystems Developer Cloud (ODC) streamlines database modeling with entities, primary keys, and indexes for efficient data management.
tags: database modeling, entity management, data management, primary keys, indexes
locale: en-us
guid: 7bf1d47d-7310-4ec8-a5db-a41b983bdb5b
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - understand
topic:
  - indexes
---

# Entities

Entities are elements that allow you to persist information in the database and to implement your database model. You can think of them as database tables or views. 

An Entity is defined through Entity Attributes that store the information related to it. Examples of entity attributes are: Name, Address, Zip Code, City and so on.

You can convert an existing entity to a static entity right-click the entity and select **Convert to Static Entity** from the **Advanced** menu.

OutSystems recommends using [static entities](entity-static.md) for a constant set of values that do not change at runtime, such as enumerations. For example, in a finance app, the transaction type could be a deposit or withdrawal.

## Primary key

In OutSystems, a primary key is called Entity Identifier.

When an Entity is created, an attribute called Id is automatically added as Entity Identifier. By default, it is of data type Long Integer and its value is automatically calculated in sequence (an AutoNumber in OutSystems). This way, you don't have to implement any specific logic to uniquely identify each entity record. 

You can use other data types as Entity Identifiers or switch off the AutoNumber in an attribute. In these cases, you have to implement the logic to uniquely identify each entity record.

To set another attribute as Entity Identifier simply go to that attribute, right-click and set it as identifier.

<div class="info" markdown="1">

When designing the data model, choose the identifier attribute and its name carefully. After the first publish, you can’t change the identifier attribute or rename it.

</div>

In OutSystems, it is not possible to have composite keys because only one attribute can be the Entity Identifier. But you can use indexes to create alternate keys (see more below about indexes).

## Sequential attributes

Sequential attributes are useful for Entity Identifier attributes. It is an easy way to ensure that each record has a unique primary key. 

When creating new records in the database with Entity Actions, the platform automatically calculates a new sequential and unique value. 

There can be only one sequential attribute per Entity.

## Indexes

Like in relational databases, OutSystems provides indexes for faster access to data in the entity. If you usually search or sort by one or more attributes of the entity, you can create an index based on those attributes to make it faster.

Indexes can also be used to create alternate and composite keys. 

When creating an index there is always a relevant trade-off between fetching and inserting data as it may bring some overhead to the latter.

For more information, refer to the [best practices for indexing entities](../data-best-practices/intro.md#index-entities)

## Impacts when changing entities

When you create a new entity attribute, the platform automatically manages the update of all records stored in the database for you. The new attribute is added to the records and set with the default value for its data type.

When you set an entity attribute as mandatory it is automatically validated on the user interface by the platform. However, in the database, mandatory attributes are created allowing null values thus, at the database level there's no validation for mandatory attributes.

When you delete an entity or an entity attribute, the platform is permissive and lets you do it whether it is being used or not, but you must fix the elements where it is being used. In the database, the entity or entity attribute is not deleted by the platform.

## Choosing between entities and static entities

Use Entities and Static Entities based on the type of data you need to manage.

* Use Entities to store data that can change over time. Entities support Create, Read, Update, and Delete (CRUD) operations at runtime.
* Use Static Entities for constant, predefined data that doesn't change at runtime. Static Entities only support read operations and function as enums. To learn more, refer to [Static Entities](entity-static.md).

For example, in a finance app, you need to store user details. Since this data can change frequently, store it in an Entity. But to store the PaymentStatus field with predefined values like Pending, Completed, and Failed. You need to use Static Entity since they are constant.

### Convert an entity to a static entity

To convert an existing entity to a static entity right-click the entity and select **Convert to Static Entity** from the **Advanced** menu.


<div class="info" markdown="1">

To convert an existing static entity to an entity right-click the static entity and select **Convert to Entity** from the **Advanced** menu.

</div>

## Related resources

* [Modeling Data](https://learn.outsystems.com/training/journeys/modeling-data-643) online course

* [Data Model Integrity](https://learn.outsystems.com/training/journeys/data-model-integrity-638) online course
