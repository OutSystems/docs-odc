---
summary: Learn to create a many-to-many relationship in OutSystems Developer Cloud (ODC) using a junction entity.
tags: database modeling, entity relationship
locale: en-us
guid: 4e158cbd-cb4d-4152-81f2-dae5e703e5ec
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3202%3A7449&t=ZwHw8hXeFhwYsO5V-1
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
topic:
  - data-relationships
---

# Create a Many-to-Many Relationship

A many-to-many relationship happens when one entity has a one-to-many relationship with another entity, and vice-versa. For example, an `Author` can write several `Books`, and a `Book` can be written by several` Authors`. This kind of relationship is also known as **N to M** relationship.

Resolve this kind of relationships by adding a third entity, called **junction entity**. It must have at least two foreign keys, one to each entity in the relationship. Other attributes can also be added if needed (see the example).

To create a many-to-many relationship, follow these steps:
    
1. [Create a relationship entity](../entity-create.md).
1. Add an attribute and set the data type to the identifier of the first entity.
1. Add another attribute and set the data type to the identifier of the second entity.

Check here our [online training videos ](https://learn.outsystems.com/training/journeys/modeling-data-relationships-642/many-to-many-relationship/odc/447) on this topic:

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/874762411?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Many-to-Many Relationship [en-US / 11]"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>


## Example

You have a mobile application called GoOut, where end-users can find and review places like restaurants, hotels, etc. An end-user can review many places and a place can have reviews from many end-users, i.e. a many-to-many relationship. We will call these two entities `Review` and `Place`. Besides the two foreign keys, a review has also other attributes: classification, comments, and submission date.

Let's create the `Review` entity:

1. In the Data tab, open the GoOutWebDataModel entity diagram.
1. Drag the User system entity and the `Place` entity to the diagram.
1. Right-click the diagram canvas and select 'Add Entity'.
1. Name the entity as `Review`.
1. Drag the `User.Id` attribute to the `Review`.
1. Drag the `Place.Id` attribute to the `Review`.
1. Add the remaining attributes:
    * `Classification`, Integer type
    * `Comments`, Text type
    * `SubmittedOn`, Date type

![Entity diagram showing the many-to-many relationship between User, Review, and Place entities in the GoOut application](images/many-to-many-relationship-1.png "Many-to-Many Relationship Entity Diagram")
