---
summary: Learn how to migrate your existing Cordova mobile apps to Capacitor in OutSystems Developer Cloud (ODC).
tags: mobile app migration, cordova to capacitor, capacitor migration, mobile runtime
locale: en-us
guid: fe0b5001-64c7-4d69-9a57-e98bac12cbbb
app_type: mobile apps
platform-version: odc
figma:
audience:
  - mobile developers
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - apply
  - understand
helpids:
---

# Migrating Cordova apps to Capacitor

With MABS 12, you can migrate your existing Cordova mobile apps to the modern Capacitor cross-platform native runtime. This migration enables you to leverage Capacitor's flexible plugin integration, active developer community while maintaining your app's core functionality.

Existing mobile apps using Cordova don't require immediate action. Apart from those introduced by new SDKs, there are no breaking changes for existing Cordova apps.

## Required changes

* **Migrate extensibility schema**: Update your Cordova-based extensibility schema to the [universal extensibility schema](extensibility-configurations.md). For detailed information, refer to [Migrate Cordova-based schema to the universal schema](migrate-cordova-schema.md).

* **Identify plugin compatibility**: For apps with plugins, check for plugin incompatibilities and if needed [adapt your existing Cordova plugins](../../integration-with-systems/mobile-plugins/migrate-cordova-plugin.md) to work with Capacitor apps. All [Outsystems-supported plugins](../../integration-with-systems/mobile-plugins/os-supported-plugins.md) in Forge work with both Cordova and Capacitor.

* **Build with MABS 12**: From the ODC Portal, [create your mobile app package](creating-mobile-package.md) using MABS 12 and select Capacitor as the runtime.

## Optional changes depending on your app

* **Use extensibility settings**: If your app or plugins use ODC Settings, reconfigure them to use [extensibility settings](configuring-mobile-apps.md#configure-extensibility-settings-configure-extensibility-settings).

* **Use build actions:** If your app uses Cordova hooks and requires native project customizations, such as modifying Info.plist or build.gradle files, then use [build actions](build-actions.md).

 The transition from Cordova to Capacitor doesn't impact the end-user experience.

## Related resources

For more information, refer to the following:

* [Capacitor and Cordova support in MABS 12](mabs-overview.md)

* [Universal extensibility configurations JSON schema](extensibility-configurations.md)

* [Migrate Cordova-based schema to the universal schema](migrate-cordova-schema.md)

* [Adapt Cordova plugin for compatibility with Capacitor](../../integration-with-systems/mobile-plugins/migrate-cordova-plugin.md)

* [Build actions](build-actions.md)
