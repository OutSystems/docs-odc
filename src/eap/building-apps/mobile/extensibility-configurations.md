---
summary: Utilize Extensibility Configurations in OutSystems Developer Cloud (ODC) for advanced mobile app customization.
tags: extensibility configurations, json configuration, mobile build service, mobile apps customization
locale: en-us
guid: 941e56cf-aacf-43bf-9d1c-f131565036e6
app_type: mobile apps
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=8221-2
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - apply
  - remember
topic:
  - customize-mobile-apps
helpids: 30664
---

# Universal extensibility configurations JSON schema

With the introduction of the modern [Capacitor](https://capacitorjs.com/docs) framework the extensibility configurations support both Capacitor and Cordova frameworks and are managed through two distinct JSON files.

* [App extensibility configurations JSON file](extensibility-configurations/extensibility-app-reference.md)

* [Library extensibility configurations JSON file](extensibility-configurations/extensibility-lib-reference.md)

OutSystems recommends adopting the universal schema because of the following benefits:

* Provides better modularity and maintainability by separating app and library configurations

* Enables structured and repeatable modifications/customizations using [build actions](build-actions.md) that are available within the app and library extensibility schema.

* Supports auto-complete and synctactical validation for preferences and values.

This screenshot illustrates auto-complete support for JSON while configuring your apps through **Extensibility**.

![Screenshot showing auto-complete support for JSON configuration in OutSystems Developer Cloud.](images/extensibility-auto-complete-odcs-pl.png "Auto-complete Support for JSON Configuration")

The [Cordova-based extensibility configuration schema](legacy-extensibility-configuration.md) doesn't have separate app and library contexts and doesn't support build actions.

<div class="warning" markdown="1">

The support for the Cordova-based schema will be deprecated soon. If the app includes both Cordova-based and universal schema, the Cordova-based schema is ignored.

</div>

However, If you're building apps with Apache Cordova framework using MABS versions older than 12, you can continue to use the [Cordova-based extensibility configurations  JSON schema](legacy-extensibility-configuration.md).

If you attempt to use the Cordova-based schema with the Capacitor apps an error is thrown. For detailed information, refer to [Troubleshooting errors](extensibility-configurations/troubleshooting-errors.md).

## App extensibility configurations JSON schema

[App configuration](extensibility-configurations/extensibility-app-reference.md)is defined at the mobile app level. You use it to customize the final mobile app package, setting properties like the display name, orientation, app-wide permissions, and splash screen. This is the primary configuration you edit when building your app.

For detailed information about app configurations use cases, refer to [Using extensibility configuration JSON schema](extensibility-configurations-use-cases.md).

## Library extensibility configurations JSON schema

[Library (or plugin) configuration](extensibility-configurations/extensibility-lib-reference.md) is defined within a library module. You use it to define the native plugin that the library wraps. In library configuration, you can specify the plugin source, such as npm, its required variables, and the specific permissions the plugin needs to function. You edit this configuration file when creating or wrapping a mobile plugin.

For detailed information about library configurations use cases, refer to [Using extensibility configuration JSON schema](extensibility-configurations-use-cases.md).

## Related resources

For more information about configuring your app using universal extensibility configurations:

* [App extensibility configuration JSON schema](extensibility-configurations/extensibility-app-reference.md)

* [Library (plugin) extensibility configuration JSON schema](extensibility-configurations/extensibility-lib-reference.md)

* [Using extensibility configurations](extensibility-configurations-use-cases.md)
