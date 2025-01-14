---
summary: OutSystems Developer Cloud (ODC) accelerates CRUD operations with CRUD wrappers, enabling efficient data handling and faster development.
tags: crud operations, data handling, outsystems, application development, crud wrappers
guid: 27f0d3e2-f584-46a1-bb5a-adc6fe821a3d
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=6699-48
outsystems-tools:
    - odc studio
content-type:
    - conceptual
    - best practice
audience:
    - full stack developers
    - backend developers
---

# Understanding CRUD operations in ODC

CRUD operations—Create, Read, Update, and Delete—are basic actions that let you work with data in applications. They’re a foundation of application development, making them critical for organizing, storing, and updating information. In OutSystems, CRUD operations are central because they help developers create and manage apps quickly and efficiently.

OutSystems provides tools that simplify CRUD operations, saving time while ensuring consistency and scalability. These tools allow developers to design systems that grow as needed and maintain high standards for functionality. A key feature of these tools is CRUD wrappers. CRUD wrappers let developers add rules, validations, and custom logic to CRUD actions to ensure the application behaves as expected. While manually creating CRUD wrappers can take time, OutSystems Studio’s accelerator feature lets developers create them faster and more easily.


## Core concepts of CRUD wrappers in OutSystems

CRUD wrappers are actions that group together the default CRUD entity actions, such as creating or updating a record. They provide a way to add extra checks and rules to these actions, making development more efficient and promoting code reusability. With CRUD wrappers, developers can:

* Verify the validity of data before saving it, ensuring high data quality.
* Apply business rules, such as marking records as inactive rather than deleting them, to preserve data history.
* Centralize error handling and change tracking, making applications easier to maintain and debug.

While CRUD wrappers are extremely useful, they can be tedious to create manually, especially in applications with many entities or complex requirements.

### ODC Studio accelerator 

ODC Studio offers an accelerator feature designed to simplify CRUD wrapper creation for entities created in ODC Studio. The accelerator automates repetitive tasks like adding validations and parameters, streamlining the initial setup process. 

The accelerator creates four server action wrappers, which are visible in the Logic tab under a folder with the same name as the entity:

* `<Entity>Create`
* `<Entity>CreateOrUpdate`
* `<Entity>Delete`
* `<Entity>Update`

These server actions encapsulate the entity actions and include validations to ensure mandatory attributes are filled in. The accelerator only supports entities created in ODC Studio and does not handle external entities. They also create the necessary input and output parameters. If the entity is public, additional service actions are created to encapsulate the server actions mentioned earlier. These service actions allow external access to the functionality. Conversely, if the entity is not public, only the server actions are created, and they remain internal to the application. However, it’s important to note that the accelerator simplifies the initial creation of CRUD wrappers but doesn’t automatically adjust to changes in the data model, like adding or removing attributes or modifying their properties.


To use the accelerator, right-click an entity in ODC Studio and choose the option **Create Entity Action Wrappers**.

![ODC Studio interface showing the option to create entity action wrappers for the Products entity.](images/crud-wrappers-create-odcs.png "Create Entity Actions Wrappers Option")

![ODC Studio interface displaying server actions for the Products entity, including create, create or update, delete, and update actions.](images/crud-wrappers-actions-odcs.png "Server Actions for Products Entity")

## Best practices

Even with the accelerator, it’s important to follow best practices to ensure robust and efficient applications:

* **Plan your data model**: Organize your data model carefully to keep your app efficient and easy to scale. Define relationships between entities clearly to reduce errors and optimize performance. Use isolated entities for large or complex data.
* **Consider the use of soft deletes**: Instead of permanently deleting records, mark them as inactive. This approach helps preserve a record’s history for audits or restoration purposes.
* **Monitor performance**: Regularly evaluate the performance of CRUD operations. Optimize aggregates and queries, and use indexes where needed to keep your application responsive as data grows.&#x20;
* **Add custom checks**: Include validations specific to your app’s requirements. These checks enforce business rules and enhance data accuracy. For example:
    * check that a date field contains a valid future date before saving a record
    * add role validations
    * add logic to update related tables, for example, updating the stock when an order is fulfilled
    * write into auditing tables

