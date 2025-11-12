---
summary: Learn how to customize mobile apps using the JSON schema for Extensibility Configurations in OutSystems Developer Cloud (ODC).
tags: json configuration, plugin management, app customization, mobile development, configuration schema
locale: en-us
guid: ecb98e61-f07f-4204-a899-9fd1d5460fbf
app_type: mobile apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=8030-23
audience:
  - mobile developers
outsystems-tools:
  - odc studio
coverage-type:
  - understand
  - remember
helpids: 30680
---

# Extensibility configurations JSON schema

<div class="info" markdown="1">

Applies only to mobile apps.

</div>

**Extensibility Configurations** are JSON-based settings used to customize mobile app builds. The extensibility configurations allow you to customize the mobile app's native preferences using a JSON string. You can configure your extensibility from **App** > **Edit app properties** > **Extensibility**.

![Screenshot of the Extensibility tab in the Edit app properties window showing JSON configurations for permissions, orientation, and target device.](images/edit-app-extensibility-odcs.png "Editing App Extensibility Configurations in ODC")

Some of these properties can be configured visually via the mobile app properties. For detailed information, refer to [Configuring mobile apps](configuring-mobile-apps.md).

<div class="info" markdown="1">

Extensibility configurations may be processed by OutSystems for service improvement and troubleshooting purposes. You are fully responsible for ensuring these configurations never contain, or allow OutSystems to access, any personal, confidential, or sensitive information. If a configuration must include sensitive details, you must use the ODC's secret settings to prevent sensitive data from being collected or accessed by OutSystems.

</div>

## Why are extensibility configurations needed?

Extensibility configurations are essential for customizing mobile apps and managing plugins to meet specific requirements. For detailed information about different use cases, refer to [Using extensibility configurations](extensibility-configurations-use-cases.md).

Here are some ways in which you can use the extensibility configurations:

### Customize mobile app properties

You can customize mobile app properties, such as display name, orientation, permissions, and splash screens, to meet specific requirements via the [app extensibility configurations JSON file](extensibility-configurations/extensibility-app-reference.md).

### Manage plugins

Define and manage native plugins, specifying their source, required variables, and permissions via [library extensibility configurations JSON file](extensibility-configurations/extensibility-lib-reference.md).

Within the app and library extensibility configurations, you can perform native project modifications via the [build actions](build-actions.md). Build Actions use JSON files to define a sequence of customizations to be applied to the mobile project during the build process. With build actions you can modify **Info.plist** or **build.gradle** files in a structured and repeatable way.

Build actions is the modern replacement for Cordova hooks and is available in both the app and library configuration. You can use build actions only for Capacitor apps.

### Build plugins that support dual framework

Support plugins that wrap Cordova, Capacitor, or both. This allows library creators to build a single wrapper that can be used in either a Cordova project or in a modern Capacitor project, facilitating a smoother transition.

### Configure and manage build time settings

You can configure and manage build time settings for your mobile app using **Extensibility settings**. You can declare these settings for your mobile app in ODC Studio and from ODC Portal, you can define and manage these settings for different deployment stages. For detailed information, refer to [Configuring mobile apps](configuring-mobile-apps.md).

## Related resources

For more information about configuring your app using universal extensibility configurations:

* [Universal extensibility configurations JSON schema](extensibility-configurations.md)

* [Using extensibility configurations](extensibility-configurations-use-cases.md)

For more information about configuring your app using Cordova-based extensibility configurations:

* [Cordova-based extensibility configurations JSON schema](legacy-extensibility-configuration.md)

* [Cordova-based extensibility configurations use cases](cordova-extensibility-configurations-use-cases.md)
