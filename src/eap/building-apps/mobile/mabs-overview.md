---
summary: This article provides an overview of MABS and specifics of MABS12.
tags: mabs, hybrid mobile apps, capacitor, cordova, outsystems
locale: en-us
guid: 6b8e1729-3b16-4945-bf72-c22628e71421  
app_type: mobile apps
platform-version: odc
figma:
audience:
  - mobile developers
outsystems-tools:
  - odc portal
coverage-type:
  - understand
  - remember
---
# Capacitor and Cordova support in MABS

Mobile App Build Service (MABS) is an OutSystems cloud service that generates native mobile app packages for iOS and Android from an ODC mobile app.

MABS supports different versions. Each is designed to be compatible with specific Android and iOS versions while supporting new mobile technology stacks. For detailed information about the list of supported MABS versions, refer to [Mobile Apps Build Service Versions](https://success.outsystems.com/Support/Release_Notes/Mobile_Apps_Build_Service_Versions).

MABS versions earlier than 12.0 use Apache Cordova as its underlying hybrid framework.

## Dual stack support in MABS 12

MABS 12 supports building both **Cordova apps** and [**Capacitor apps**](https://capacitorjs.com/). From ODC Portal, while building the mobile package, you can [select the mobile framework](creating-mobile-package.md) Cordova or Capacitor. The default framework for MABS 12 is Capacitor.

Here are some recommendations for building mobile apps using MABS 12:

* **For new apps:** To leverage the modern framework and its capabilities, use the Capacitor stack from the beginning and adapt or create any necessary plugins to work with it. For detailed information about what's changing from Cordova to Capacitor apps, refer to [Changes from Cordova to Capacitor apps](intro.md#changes-from-cordova-to-capacitor-apps-cordova-capacitor-changes).
  
For detailed information about using plugins in Capacitor apps, refer to [Using plugins in Capacitor apps](../../integration-with-systems/mobile-plugins/intro.md#using-plugins-in-capacitor-apps-use-plugins-capacitor-apps).
  
* **For existing Cordova apps with a tight deadline:** Continue with the Cordova stack and prepare for transition to Capacitor.
  
* **For existing Cordova apps in a regular maintenance or improvement cycle:** Try the Capacitor stack, identify any plugin incompatibilities, and gradually work on the migration. For detailed information about how to adapt Cordovoa plugins, refer to [Adapt Cordova plugin for compatibility with Capacitor](../../integration-with-systems/mobile-plugins/migrate-cordova-plugin.md).

## Related resources

Here are some related resources regarding extensibility configurations and plugins:

### Extensibility configuration resources

* [Universal extensibility configuration JSON schema](extensibility-configurations.md)
  
* [Using extensibility configuration JSON schema](extensibility-configurations-use-cases.md)

### Plugin resources

* [Building a Capacitor plugin from scratch](../../integration-with-systems/mobile-plugins/capacitor-plugins/build-capacitor-plugin.md)

* [Adapt Cordova plugin for comptability with Capacitor](../../integration-with-systems/mobile-plugins/migrate-cordova-plugin.md)
