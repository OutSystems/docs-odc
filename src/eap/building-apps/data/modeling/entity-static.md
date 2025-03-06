---
summary: Learn how to manage Static Entities in OutSystems Developer Cloud (ODC) for predefined data sets with global scope.
tags: data modeling, database design
locale: en-us
guid: 1093da45-38cc-47b6-aaa2-7123a1d2d964
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3202%3A7357&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
  - apply
---

# Static Entities

A **Static Entity** consists of a set of named values. Think of Static Entities as literal values stored in a database whose scope is always global. The **Records** folder of the Static Entity holds the data, and the Attributes define the structure of the data.

The only action available for the Static Entities is the **Get&lt;StaticEntity&gt;** action, because OutSystems manages the data persistence for you.

When modeling your data, keep in mind that Static Entities can only contain foreign keys of other Static Entities. For more information check out [Entity Relationships](relationship/relationships.md).

OutSystems recommends using [entities](entity.md) to store dynamically changing information. For example, in a finance app, the user's address could change.

## Create a Static Entity

To add a Static Entity to your app, do the following in ODC Studio:

1. Navigate to the **Data** tab, right-click on the **Entities** folder, and select **Add Static Entity to Database**.

    ![Screenshot of ODC Studio with the menu option to add a Static Entity to the database highlighted](images/add-static-entity-odcs.png "Adding a Static Entity in ODC Studio")

    Start typing to enter the name. Press **Enter** to confirm.

1. Each new Static Entity gets the [default set of Attributes](#default-attributes). To add a new Attribute, right-click on your Static Entity, and select **Add Entity Attribute**. Then, edit the Attribute name and data type.

1. Finally, add some data to your Static Entity. Right-click on the Static Entity, and select **Add Record**. Enter the properties of the Record.

## Default Attributes

ODC Studio creates the following Attributes automatically:

**Id**
:   Identifies a record and is always unique.

**Label**
:   Holds a value to display in an application.

**Order**
:   Defines the order for displaying the records to the end-user.

**Is_Active**
:   Defines whether a record is available during runtime. For example, the records with **Is_Active** set to false aren't used when scaffolding uses the Static Entity.


## Convert Static Entity to Entity

You can convert existing Static Entities to Entities. To convert a Static Entity to Entity, right-click on the Static Entity, navigate to the **Advanced** help menu and then select **Convert to Entity**. 

After converting a Static Entity to an Entity:

* The records from the Static Entity become available through database queries, via Aggregate or SQL Query 
* The **Records** folder is no longer available in ODC Studio

Note that it's also possible to convert an Entity to Static Entity.

## Example

Use Static Entities when you need a predefined, or constant, set of values. For example, in a hotel app, you probably need some reservation statuses: "booked", "checked in", "checked out", and "canceled". You also need the default descriptions for the statuses like "The guests have just left." for "checked out".

Your Static Entity Status may look like this:

![Example of a Static Entity structure in ODC Studio with different reservation statuses](images/static-entity-example-odcs.png "Static Entity Example in ODC Studio")

The Records folder of your Static Entity contains all statuses you have created. If you select "CheckedOut", the Properties Editor shows the following details:

![Details of a 'Checked Out' record in a Static Entity within ODC Studio showing Identifier, Label, and TextDescription fields](images/static-entity-record-example-odcs.png "Static Entity Record Details in ODC Studio")

The Identifier for the checked out status is `CheckedOut` and the Label is `"Checked-Out"`. The field TextDescription is the custom field and has the string value `"The guests have just left."`.

You can access the record for checked out status by referencing its Identifier, like this: `Entities.Status.CheckedOut`.
