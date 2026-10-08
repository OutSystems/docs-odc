---
summary: CRUD wrappers in OutSystems Developer Cloud (ODC) use Mentor Studio and the ODC Studio accelerator for validations, auditing, and non-AutoNumber IDs.
tags:
  - Best Practices
  - Data
  - Data Integrity
  - Data Model
  - Entities
  - Logic
guid: 27f0d3e2-f584-46a1-bb5a-adc6fe821a3d
topic:
  - crud-wrapper-accelerator
  - crud-wrapper-auditing
  - non-autonumber-crud-ids
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=6699-48
outsystems-tools:
  - odc studio
  - mentor studio
audience:
  - Developer
coverage-type:
  - understand
  - apply
  - evaluate
isautopublish: true
---

# Understanding CRUD operations in ODC

CRUD operations—Create, Read, Update, and Delete—are basic actions that let you work with data in applications. They’re a foundation of application development, making them critical for organizing, storing, and updating information. In OutSystems, CRUD operations are central because they help developers create and manage apps quickly and efficiently.

OutSystems provides tools that simplify CRUD operations, saving time while ensuring consistency and scalability. These tools allow developers to design systems that grow as needed and maintain high standards for functionality. A key feature of these tools is CRUD wrappers. CRUD wrappers let developers add rules, validations, and custom logic to CRUD actions to ensure the application behaves as expected. While manually creating CRUD wrappers can take time, OutSystems Studio’s accelerator feature lets developers create them faster and more easily.

## Create CRUD wrappers with Mentor Studio

Create the wrapper server actions by describing the entity and the actions you need in Mentor Studio, and validate the wrappers and their validations before you publish.

In your prompt, name the entity, the actions you need, and the validations and audit attributes to include. For example, "Create server actions that wrap the Create, Update, and Delete entity actions of the Product entity. Validate the mandatory attributes before saving, and set CreatedOn and CreatedBy when a record is created."

For more prompt examples, refer to [Prompts for Mentor Studio](../../agentic-development/mentor-studio/prompts.md#logic).

For the requirements and the steps to prompt Mentor Studio and review the change, refer to [Modify an app with AI in ODC Studio](../../agentic-development/mentor-studio/modify-app.md) and [Review and accept the plan](../../agentic-development/mentor-studio/how-it-works.md#accept-plan).

### Validate the wrappers

The platform guarantees that the model is valid, and you decide whether the wrappers implement the rules your app needs. Compare the generated server actions with the output of the [ODC Studio accelerator](#odc-studio-accelerator), and check the following:

* The wrappers cover the operations you described. The accelerator creates `<Entity>Create`, `<Entity>CreateOrUpdate`, `<Entity>Delete`, and `<Entity>Update` in a folder named after the entity.
* Each wrapper calls the entity action it encapsulates.
* The validation covers the [mandatory attributes](#mandatory-attributes) that your rules require. The accelerator doesn't validate numeric, Boolean, and basic audit attributes.
* The audit attributes `CreatedOn`, `CreatedBy`, and `UpdatedOn` or `ModifiedOn`, and `UpdatedBy` or `ModifiedBy`, are assigned values. For more information, refer to [Enable auditing for data changes](#enable-auditing-for-data-changes).
* For an entity whose identifier isn't AutoNumber, the `Create` and `CreateOrUpdate` wrappers check that the identifier is set, and your logic provides a unique value. For more information, refer to [Handling identifiers that aren't AutoNumber](#handling-identifiers-that-arent-autonumber).
* If other apps write to the entity, service actions encapsulate the server actions. The wrappers can come back as server actions only, so name the service actions in your prompt when you need them.
* The wrappers match the current data model. Existing wrappers don't adjust when you add or remove attributes or change their properties, so update them when the data model changes.

## Core concepts of CRUD wrappers in OutSystems

CRUD wrappers are actions that group together the default CRUD entity actions, such as creating or updating a record. They provide a way to add extra checks and rules to these actions, making development more efficient and promoting code reusability. With CRUD wrappers, developers can:

![Diagram showing benefits of CRUD wrappers: Validate data integrity, Enforce data retention, Centralize error tracking.](images/crud-wrappers-benefits-diag.png "Benefits of CRUD Wrappers")

* Verify the validity of data before saving it, ensuring high data quality.
* Apply business rules, such as marking records as inactive rather than deleting them, to preserve data history.
* Centralize error handling and change tracking, making applications easier to maintain and debug.

While CRUD wrappers are extremely useful, they can be tedious to create manually, especially in applications with many entities or complex requirements.

### ODC Studio accelerator

You can also create the wrappers with the accelerator. ODC Studio offers an accelerator feature designed to simplify CRUD wrapper creation for entities created in ODC Studio. The accelerator automates repetitive tasks like adding validations and parameters, streamlining the initial setup process.

The accelerator creates four server action wrappers, which are visible in the Logic tab under a folder with the same name as the entity:

* `<Entity>Create`
* `<Entity>CreateOrUpdate`
* `<Entity>Delete`
* `<Entity>Update`

![Diagram showing the creation of CRUD wrappers for public and nonpublic entities in ODC Studio.](images/crud-wrappers-actions-diag.png "CRUD Wrappers Actions")

These server actions encapsulate the entity actions and include validations to ensure mandatory attributes are filled in. The accelerator only supports entities created in ODC Studio and does not handle external entities. They also create the necessary input and output parameters. If the entity is public, additional service actions are created to encapsulate the server actions mentioned earlier. These service actions allow external access to the functionality. Conversely, if the entity is not public, only the server actions are created, and they remain internal to the application. However, it’s important to note that the accelerator simplifies the initial creation of CRUD wrappers but doesn’t automatically adjust to changes in the data model, like adding or removing attributes or modifying their properties.

To use the accelerator, right-click an entity in ODC Studio and choose the option **Create Entity Action Wrappers**.

![ODC Studio interface showing the option to create entity action wrappers for the Products entity.](images/crud-wrappers-create-odcs.png "Create Entity Actions Wrappers Option")

### Mandatory attributes

The accelerator adds an If node to validate mandatory attributes of the following types: `Text`, `Email`, `Phone Number`, `Date`, `DateTime`, `Time`, `Binary`, other `Entity Identifiers`. It doesn't validate Numeric values (`Integer`, `Long Integer`, `Decimal`, `Currency`), `Booleans`, and basic audit attributes.

Basic audit attributes, even if they're mandatory, aren't validated in this node. Instead, they're assigned values in dedicated assignment nodes.

### Handling identifiers that aren't AutoNumber

OutSystems entities typically have an Id attribute as their primary key, configured as AutoNumber by default. This means the platform automatically generates a unique, sequential integer for each new record, simplifying data management.

However, you may want to disable AutoNumber in scenarios where you need manual control over record IDs. This includes cases like integrating with external systems that rely on predefined IDs or implementing a custom ID generation strategy. If you choose to disable AutoNumber, your application must have a mechanism to generate and assign unique Ids to maintain data integrity.

For entities where the ID attribute is not AutoNumber, the CRUD wrappers include specific logic. In the `Create` and `CreateOrUpdate` wrappers, a validation checks if the Identifier is set, since the platform won't automatically generate one. Therefore, you must ensure your logic provides a unique identifier, such as using the `GenerateGuid()` system action or another suitable method.

### Enable auditing for data changes

Entities can include attributes that automatically track when and by whom a record was created or modified. These auditing attributes provide valuable transparency and accountability for your data, enhancing data management and overall application reliability.

Benefits of auditing include:

* Traceability and accountability: Tracks data changes for auditing and troubleshooting.
* Data integrity: Provides a record of data modifications to identify and correct errors.
* Compliance and reporting: Helps meet regulatory requirements.
* Business insights: Analyze usage patterns for data-driven decisions.
* Debugging and issue resolution: Review change history to identify and resolve issues faster.

The generated CRUD wrappers provide basic auditing using these attributes:

* `CreatedOn`: The date and time when the record was initially created.
* `CreatedBy`: The user who created the record.
* `UpdatedOn` or `ModifiedOn`: The date and time when the record was last updated.
* `UpdatedBy` or `ModifiedBy`: The user who last updated the record.

When generating wrapper logic, ODC Studio identifies these basic auditing attributes by name and data type, and adds assignments to fill them in.

For a full audit trail, it's best practice to use a separate entity to store dates and users for each record change.

<div class="info" markdown="1">

For `CreateOrUpdate` wrappers on entities with non-AutoNumber Identifiers, the logic assumes a record is new if its Created audit attributes (`CreatedOn`, `CreatedBy`) are empty. Review and adjust this logic to fit your specific requirements.

</div>

## Best practices

Even with the accelerator, it's important to follow best practices to ensure robust and efficient apps:

* **Plan your data model**: Organize your data model carefully to keep your app efficient and easy to scale. Define relationships between entities clearly to reduce errors and optimize performance. Use isolated entities for large or complex data.
* **Consider the use of soft deletes**: Instead of permanently deleting records, mark them as inactive. This approach helps preserve a record’s history for audits or restoration purposes.
* **Monitor performance**: Regularly evaluate the performance of CRUD operations. Optimize aggregates and queries, and use indexes where needed to keep your application responsive as data grows.
* **Add custom checks**: Include validations specific to your app's requirements. These checks enforce business rules and enhance data accuracy. For example:
    * Check that a date field contains a valid future date before saving a record.
    * Add role validations.
    * Add logic to update related tables, for example, updating the stock when an order is fulfilled.
    * Write into auditing tables.

## Related resources

The following resource describes what the platform guarantees and what you check in a Mentor Studio proposal.

* For what the platform guarantees and what you validate, refer to [Platform guarantees and AI interpretation](../../agentic-development/odc-ai-and-platform.md).
