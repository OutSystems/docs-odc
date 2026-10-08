---
summary: OutSystems Developer Cloud (ODC) enables data editing directly within ODC Studio, facilitating real-time app testing and stakeholder demonstrations.
tags:
  - Data
  - Data Model
  - Entities
  - Testing
locale: en-us
guid: 7d4d3bb7-5419-482d-8feb-747de019a7a0
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=4035%3A137&mode=design&t=3vXcogcuIh9sw9aQ-1
platform-version: odc
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
  - mentor studio
coverage-type:
  - apply
  - unblock
topic:
  - edit-entity-data
isautopublish: true
---

# Edit data in ODC Studio

After you create [entities to persist data](../data/modeling/entity-create.md), you can edit your app's data without leaving ODC Studio.

![Screenshot of ODC Studio interface showing data editing features](images/edit-data-odcs.png "Editing Data in ODC Studio Interface")

In ODC Studio, you can edit entity data in the development stage. The [entities](../data/modeling/entity.md) must meet the following criteria:

* Entities must have an identifier attribute.

* Entities must be from the server side only. This does not include static, local or external entities.

    * Static entities are entities that have hard coded values and don’t change dynamically as server entities.
    * Local entities are local storage entities available in mobile apps only.
    * External entities can be added through a connection from an external database, for example, Salesforce, SAP, and SQL Server. These entities are read-only.

Adding, removing, and changing entity records during app development, allows you to:

* Test your app with real and meaningful data to ensure your app works correctly once it reaches production.

* Prepare your demos with valid data to show your stakeholders real use cases and enable them to give you meaningful feedback.

In ODC, you can use sample data to create screen instances. To learn more about using sample data, see [sample data](../ui/screen-template/sample-data.md)

## Add records with Mentor Studio

Add records by describing them in Mentor Studio. Mentor Studio generates bootstrap logic that creates the records, and publishing the app runs that logic and creates the records in the database. The entity must meet the same criteria as for manual editing.

In your prompt, name the entity, the attribute values, and the number of records. Use fictional values, because prompts must not include personally identifiable information. For example, "Add three records to the Place entity with fictional names, addresses, and phone numbers."

For more prompt examples, refer to [Prompts for Mentor Studio](../../agentic-development/mentor-studio/prompts.md#data).

For the requirements and the steps to prompt Mentor Studio and review the change, refer to [Modify an app with AI in ODC Studio](../../agentic-development/mentor-studio/modify-app.md) and [Review and accept the plan](../../agentic-development/mentor-studio/how-it-works.md#accept-plan).

### Validate the bootstrap logic

The platform guarantees that the model is valid, and you decide whether the logic creates the data you need for your test or demo. Mentor Studio adds the records through logic that calls the Create action of the entity, for example in an existing bootstrap server action. In the **Logic** tab of ODC Studio, check the following:

* The logic creates one record for each record you described, in the entity you intended.
* Each record sets every mandatory attribute, with a value that fits the data type of the attribute.
* Foreign key values point to existing records.
* The values are fictional and contain no personally identifiable information.

### Validate the data

After you publish the app, check the records that the bootstrap logic created. In the **Data** tab of ODC Studio, right-click the entity, select **View or Edit Data**, and check the following:

* The entity contains the records you described.
* Mandatory cells are filled. A red outline marks a mandatory cell without a value.
* Foreign key values point to existing records. By design, ODC Studio doesn't validate foreign keys to referenced entities.

If a record is wrong, correct the cell manually. Also correct the bootstrap logic, so that later runs of the logic create the values you need.

## Edit data manually in ODC Studio

To edit the data yourself, use the data grid that ODC Studio provides for each entity.

<div class="info" markdown="1">

By design, foreign keys to referenced entities are not validated so care must be taken when setting the foreign key values manually. OutSystems recommend you use the suggested values from the dropdown list.

Additionally, foreign key cells for the User entity don't show values or suggestions in ODC Studio. The workaround for this is to open the User entity inside the (System) database folder, find the relevant ID and copy it.

</div>

**Prerequisites**

You must have the App management **Change** permission for the app

![Image displaying the change permission settings for app management in ODC Studio](images/edit-data-change-permission-odcs.png "App Management Change Permission in ODC Studio")

Learn how to [add a record or row](#add-a-record-or-row), [delete a record or row](#delete-a-record-or-row), and [modify a record's attribute](#modify-a-records-attribute) in ODC Studio.

### Add a record or row

To add a record or row, follow these steps:

1. In the app where the entity exists, go to the **Data** tab, and right-click the entity to **View or Edit Data**.

    ![Screenshot showing the option to view or edit data for an entity in ODC Studio](images/edit-data-view-edit-odcs.png "View or Edit Data Option in ODC Studio")

    **Note**: Even though it seems like you're editing data in a spreadsheet, you're actually preparing changes to data in a relational database. Rows represent entity records, and cells represent attributes.

1. Click **Add row**.

    ![Image showing mandatory fields highlighted with red outlines in ODC Studio data editing interface](images/edit-data-mandatory-fields-odcs.png "Mandatory Fields Highlighted in ODC Studio")

    **Note:** If any cell has a red outline, it means that those fields are mandatory and you must fill them in. To understand each issue, hover over the highlighted cell.

1. You can make more than one change to the entity at a time. Once you've finished your changes, click [Apply](#apply-changes).

    ![Screenshot illustrating the process of adding a new row to an entity in ODC Studio](images/edit-data-add-row-odcs.png "Adding a New Row in ODC Studio")

## Delete a record or row

To delete a record or row, follow these steps:

1. In the app where the entity exists, go to the **Data** tab, and right-click the entity to **View or Edit Data**.

    ![Screenshot showing the option to view or edit data for an entity in ODC Studio](images/edit-data-view-edit-odcs.png "View or Edit Data Option in ODC Studio")

1. Right-click the row you want to delete, and select **Delete row**.

    ![Screenshot showing how to delete a row from an entity in ODC Studio](images/edit-data-delete-row-odcs.png "Deleting a Row in ODC Studio")

1. You can delete more than one row at a time. Once you've  finished your changes, click **Apply**.

    ![Image displaying the Apply button to confirm row deletion in ODC Studio](images/edit-data-delete-row-apply-odcs.png "Applying Row Deletion in ODC Studio")

## Modify a record's attribute

To modify a record's attribute or cell, follow these steps:

1. In the app where the entity exists, go to the **Data** tab, and double-click the entity to **View or Edit Data**.

    ![Screenshot showing the option to view or edit data for an entity in ODC Studio](images/edit-data-view-edit-odcs.png "View or Edit Data Option in ODC Studio")

1. Double-click inside the cell you want to change.

1. Depending on the data type of the cell, set the data in one of the following ways:

    * For a **Text** or **Phone** cell, enter a text string, for example, text or +1 555 565 3730.
    * For an **Email** cell, enter a text string with at least two characters separated by a @, for example, <fran.wilson@example.com>.
    * For an **Integer** or a **Long Integer** cell, enter an integer, for example, 10.
    * For a **Decimal** or a **Currency** cell, enter a decimal, for example, 10.8.
    * For a **Date** cell, enter a date using the YYYY-MM-DD format, for example, 1988-08-28.
    * For a **Time** cell, enter a time using the HH:MM:SS format, for example, 23:59:59.
    * For a **Date Time** cell, enter a time using the YYYY-MM-DD HH:MM:SS format, for example, 1988-08-28 23:59:59.
    * For a **Boolean** cell, select either True or False.
    * For a **Binary** cell, select and upload a file.
    * For an entity identifier cell, select a value from the dropdown.
    * For a static entity identifier cell, select a value from the dropdown.

1. You can make more than one change at a time. Once you've finished your changes, click **Apply**.

## Apply changes

Once you've finished your changes, confirm that you want to change the data by clicking **Apply**.

**Note**: You can’t apply your changes if a cell has errors.

After applying your changes to the database, one of the following messages is displayed:

* If all changes are successful, a success message displays.

    ![Success message displayed after applying data changes successfully in ODC Studio](images/edit-data-changes-success-odcs.png "Successful Data Changes in ODC Studio")

* If some changes fail, an error message displays and the problem cells are highlighted. To understand the cause of the errors, hover over the cell. Additionally, you can generate a text file with all of the errors by clicking **view error report**.

    ![Error message displayed after failing to apply data changes in ODC Studio](images/edit-data-changes-failed-odcs.png "Failed Data Changes in ODC Studio")

## Discard changes

You can permanently discard changes in one of the following ways:

* To discard changes to a specific row, right-click the row and select **Discard this change**.

    ![Option to discard specific changes in ODC Studio highlighted in the interface](images/edit-data-discard-odcs.png "Discarding Changes in ODC Studio")

* To discard all of your changes, click **Discard** and then confirm that want to permanently discard your changes.

    ![Button to discard all changes in ODC Studio with a confirmation dialog](images/edit-data-discard-all-changes-odcs.png "Discarding All Changes in ODC Studio")

## Related resources

The following resource describes what the platform guarantees and what you check in a Mentor Studio proposal.

* For what the platform guarantees and what you validate, refer to [Platform guarantees and AI interpretation](../../agentic-development/odc-ai-and-platform.md).
