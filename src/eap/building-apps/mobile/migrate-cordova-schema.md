---
summary: Learn how to migrate existing Cordova-based schema to Universal extensibility configuration JSON schema.
tags: json configuration, app customization, mobile development, configuration schema
locale: en-us
guid: b148ff0f-fb1f-4151-89df-d554ca3d3aa9
app_type: mobile apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=8547-2
audience:
  - mobile developers
outsystems-tools:
  - odc studio
coverage-type:
  - understand
  - remember
helpids: 30735
---

# Migrate your Cordova-based schema to the universal schema

<div class="info" markdown="1">

OutSystems is progressively rolling out the automatic migration of Cordova-based schema to universal schema.

</div>

<div class="info" markdown="1">

This migration applies only to existing mobile apps or libraries that contain extensibility configurations using the Cordova-based schema.

</div>

With the introduction of the modern [Capacitor](https://capacitorjs.com/docs) framework, you can now use [universal extensibility configurations](extensibility-configurations.md) that support both Capacitor and Cordova frameworks.

OutSystems recommends that you migrate your existing Cordova-based schema to the universal schema for modern Capacitor support, enhanced development experience, and better  structure and maintainability of your configurations.

If your existing app or library contains Cordova-based extensibility configuration, a **TrueChange** warning appears when you load the asset. This indicates that the Cordova-based schema is being used.

![Screenshot of a TrueChange warning that indicates that a deprecated JSON schema has been detected.](images/deprecated-schema-warning-odcs.png "Deprecated JSON Schema Warning")

To migrate your schema, follow these steps:

1. Double-click the **TrueChange** warning to open the **Edit properties** dialog and click **Extensibility**.

1. Review the migration notice on the **Extensibility** tab:

    * If your configuration contains recognized Cordova-based properties, the **Preview update** button is displayed.

      ![Screenshot showing the notice that a new Universal schema is available, with a button labeled 'preview update'.](images/extensibility-configuration-preview-update-odcs.png "Universal Schema Preview Update Notice")

    * If your configuration contains only unrecognized properties,  a link to documentation is displayed instead of a preview option.

      ![Screenshot showing the notice that a new Universal schema is available, with a link to documentation about the new universal schema.](images/extensibility-configuration-universal-schema-notice-no-preview-odcs.png "Universal Schema Documentation Notice")

1. To preview your configuration in the universal schema format, click **Preview update**. The preview screen displays your existing Cordova-based configuration alongside the migrated universal schema configuration.

    ![Screenshot of the edit app properties window showing a schema migration preview from the Cordova-based schema to the universal schema.](images/extensibility-configuration-auto-migration-preview-odcs.png "Schema Migration Preview")

    <div class="info" markdown="1">

    If your configuration includes unsupported properties, the migration tool only migrates the recognized properties and leaves unrecognized properties in place within the new schema structure.

    ![Screenshot of the edit app properties window showing a schema migration preview from the Cordova-based schema to the universal schema, with unsupported properties being unmigrated.](images/extensibility-configuration-auto-migration-preview-unsupported-props-odcs.png "Schema Migration Preview with Unsupported Properties")

    </div>

1. Review the preview and do one of the following:

    * Click **Update schema** to apply the universal schema configuration to your app or library.
    * Click **Back** to return to the previous view without saving your changes.

## Roll back schema changes

To undo the schema migration, use the **Undo** functionality in ODC Studio.

![Screenshot demonstrating how to invoke the undo functionality of ODC.](images/ide-edit-undo-sample-odcs.png "Undo Schema Migration")

If you can't undo the changes, [revert to a previous version](../../deploying-apps/deploy-apps.md#versions-and-revisions) of your app.

If you encounter any issues while migrating your extensibility configuration, contact the [support team](https://success.outsystems.com/support/home/).

## Related resources

Explore these resources to learn more about the universal extensibility configuration JSON schema:

* [Universal extensibility configurations JSON schema](extensibility-configurations.md)

* [Using universal extensibility configurations](extensibility-configurations-use-cases.md)
