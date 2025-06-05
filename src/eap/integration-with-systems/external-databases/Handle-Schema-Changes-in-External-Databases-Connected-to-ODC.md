---
helpids:
summary: Learn how to manage schema changes in external databases and avoid errors in ODC applications.
tags: database integration, data modeling, error handling, external entities, configuration management
guid: 
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: 
outsystems-tools:
  - odc studio
  - odc portal
content-type:
  - procedure
  - reference
audience:
  - platform administrators
  - full stack developers
  - backend developers
---

# Handle Schema Changes in External Databases Connected to ODC

Make this change to prevent runtime errors when modifying external database schemas in applications connected to OutSystems Developer Cloud (ODC).

Applications connected to external databases in ODC rely on consistent metadata across all environments. Schema changes—such as adding, removing, renaming columns, or changing data types—must follow a strict deployment order to avoid breaking the application with errors like `OS-BERT-60407` or `OS-DFQE-50201`.

To do this task, follow these steps:

## Add new columns/attributes to external database

Add new columns/attributes to enhance your schema safely without causing runtime issues.

1. Add the new column in the Dev database.
2. Open the External Database Configuration Console in ODC and apply the changes.
3. Update your application to use the new column and test it in Dev.
4. Before promoting to QA:
   - Ensure the column exists in the QA database.
   - Refresh metadata in the QA environment.
   - Deploy the updated app.
5. Repeat the same process for the Prod environment.

## Remove columns/attributes from external database

Remove columns/attributes safely to avoid breaking references in the deployed app.

1. Do not remove the column directly from the database or ODC Console configuration.
2. First, update the app to stop using the column in all logic and queries.
3. Deploy the updated version of the app to Dev, QA, and Prod.
4. Once the app no longer references the column:
   - Remove the column from all databases.
   - Remove the column from the External Database Configuration and apply it.

## Rename columns/attributes or change their data type

Change column names or types safely by using a replacement-and-migration strategy.

1. Do not rename or change types directly in the existing column.
2. Instead, add a new column with the new name or type.
3. Update the application logic to use the new column and stop using the old one.
4. Deploy the updated app to all environments.
5. After verifying the app is no longer dependent on the old column:
   - Remove the old column from the databases.
   - Remove it from the ODC Database Configuration and apply.

## Notes

- ODC does not support environment-specific external database configurations.
- Changes in the Console configuration are applied globally across Dev, QA, and Prod.
- Changing or removing a column that's still used in the app can lead to errors such as:
  - `OS-BERT-60407 - [500] Could not execute the specified command`
  - `OS-DFQE-50201 - Connection returned an error`
  - `Bad value for type long` (if metadata is mismatched)

Create schema changes carefully and always align database updates with app deployments to maintain stability across environments.
