---
summary: OutSystems Developer Cloud (ODC) supports the creation of one-to-many relationships between entities using foreign keys.
tags: database modeling, entity relationships, data management, referential integrity, data modeling
locale: en-us
guid: 6bde9ed9-7127-4f01-96ee-3add9ecda974
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3202%3A7447&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
  - understand
---

# Create a One-to-Many Relationship

When modeling data, it is sometimes necessary to create one-to-many relationships between entities. For instance, a `Place` (parent entity) can have many `Reviews` (child entity). This is typically implemented with a foreign key - the identifier of the parent record - in the child records.

To create a one-to-many relationship between two entities:

1. Select the entity with the child records (e.g. `Review`).
1. Add a new attribute that holds the identifier of the parent entity (e.g. identifier of the `Place` entity). This attribute will be the foreign key.

Having an identifier attribute pointing to another entity automatically creates a relationship. You can see the relationships between entities if you have them in the same Entity Diagram.

![Diagram illustrating a one-to-many relationship between Place and Review entities with a foreign key](images/one-to-many-relationship-1.png "One-to-Many Relationship Diagram")

When you create relationships between entities in your app, you must define the referential integrity you want to use when deleting records. 
