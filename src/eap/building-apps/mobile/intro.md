---
summary: OutSystems Developer Cloud (ODC) enables rapid development of mobile apps, including native apps, PWAs, and mobile backends.
tags: mobile app development, native apps, progressive web apps, mobile backend
locale: en-us
guid: 8e81892f-5deb-4b08-b3d7-e12459619f76
app_type: mobile apps
platform-version: odc
figma:
audience:
  - mobile developers
outsystems-tools:
  - none
coverage-type:
  - none
helpids: 30625
---

# Mobile apps

OutSystems Developer Cloud (ODC) enables you to create powerful, cross-platform mobile apps using low-code development. These apps leverage native device capabilities, providing seamless user experiences across both iOS and Android platforms.

ODC enables you to develop the following mobile assets:

* A mobile app: These are apps that users install on their phones, have access to the device sensors, can work offline, and have a UX designed for a native experience.
  
* A Progressive Web App (PWA): These are apps that users can access from their mobile browsers without installation.
  
* Mobile backend: Use OutSystems as the backend for your native mobile app, without using the traditional programming tools.

## Capacitor native runtime support in mobile apps

Starting from [MABS 12](mabs-overview.md), you can build mobile apps using both Apache Cordova and [Capacitor](https://capacitorjs.com/) runtimes. Capacitor is a modern cross-platform native runtime that allows you to build native mobile apps for iOS and Android using web technologies like HTML, CSS, and JavaScript.

Capacitor provides a flexible and scalable solution for integrating native features and plugins, enabling you to customize and extend mobile app functionality efficiently. You also have access to a highly active developer community with a growing library of [plugins](https://capacitorjs.com/docs/plugins) ready to use.

While creating your mobile package using MABS 12, you can [select the native runtime](creating-mobile-package.md) that best suits your app's requirements.

With MABS 12, you can:

* Build mobile apps using the modern Capacitor cross-platform native runtime.

* Continue using the Cordova framework for existing apps while preparing for a gradual transition to Capacitor.

## Getting started with mobile app development

If you're building a new mobile app with ODC, use Capacitor as your native runtime. Capacitor is the modern, recommended option for new mobile app projects.

**For new developers**: When building mobile apps in ODC Studio, you use low-code to design screens, add logic, and configure properties without writing native code.

To customize your mobile app, you must use [universal extensibility configurations](extensibility-configurations.md) and to manage configuration values across different deployment stages, you must use [extensibility settings](configuring-mobile-apps.md#define-extensibility-settings) .

You only need to consider the runtime choice when:

* Selecting plugins
* Building mobile packages

### Choosing plugins for your mobile app

When you need to access device features such as the camera, GPS, or barcode scanner, install plugins from [Forge](https://www.outsystems.com/forge/). OutSystems-supported plugins display compatibility information on their Forge pages.

To ensure compatibility with your app:

1. Search for the plugin you need in Forge
1. Check the plugin details page for framework compatibility.
1. Install plugins that support Capacitor for new mobile apps

All [OutSystems supported mobile plugins](../../integration-with-systems/mobile-plugins/os-supported-plugins.md) work with both Capacitor and Cordova.

### Generating mobile packages

From the ODC portal, use MABS 12 to generate your native iOS/Android mobile package. For detailed information, refer to [Create mobile app package](creating-mobile-package.md).

### Changes from Cordova to Capacitor apps {#cordova-capacitor-changes}

The transition from an OutSystems Cordova app to a Capacitor app brings several significant updates focusing on adopting the Capacitor cross-platform native runtime and modernizing the build process and extensibility.

| Feature | Cordova app | Capacitor app |
| -------------------------------- | -------------------------------------------------- | ------------------------------------------------- |
| **Mobile cross-platform native runtime** | Apache Cordova | Capacitor |
| **Device feature access** | Uses Cordova plugins | Uses Capacitor plugins |
| **Extensibility** | [Cordova-based extensibility](legacy-extensibility-configuration.md) and universal extensibility from MABS 12 | Only [Universal extensibility](extensibility-configurations.md) from MABS 12 with auto-complete and syntactical validation |
| **Mobile configuration** | Standard configurations | [Mobile configuration](configuring-mobile-apps.md) tab with Capacitor-specific settings |
| **Native project customization** | Limited via config files | [Build actions](build-actions.md) to customize native mobile projects |

For detailed information about migrating your Cordova apps to Capacitor, refer to [Migrating Cordova apps to Capacitor](migrate-cordova-to-capacitor.md).

## Related resources

* [Capacitor and Cordova support in MABS 12](mabs-overview.md)

* [Universal extensibility configurations JSON schema](extensibility-configurations.md)

* [Migrating Cordova apps to Capacitor](migrate-cordova-to-capacitor.md)
