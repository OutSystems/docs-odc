---
guid: a8b9c1d2-e3f4-5678-9abc-def012345678
locale: en-us
summary: Learn how to build custom Capacitor plugins from scratch for OutSystems Developer Cloud (ODC) mobile applications.
figma:
coverage-type:
  - understand
  - apply
  - unblock
topic:
app_type: mobile apps
platform-version: odc
audience:
  - mobile developers
tags: capacitor plugins, mobile development, native plugins, plugin development, outsystems plugins
outsystems-tools:
  - odc studio
  - odc portal
helpids:
---

# Building a Capacitor plugin from scratch

This article provides a comprehensive guide for building custom Capacitor plugins for ODC mobile apps. It's intended for mobile plugin developers with experience in Capacitor plugin development who need to create native functionality not available in existing plugins.

As you build your Capacitor plugin, consider the [Capacitor plugin abstraction patterns](https://capacitorjs.com/docs/plugins/tutorial/code-abstraction-patterns).

## When to build a Capacitor plugin from scratch

Before building a [custom plugin](https://capacitorjs.com/docs/plugins/creating-plugins), consider your options in this order:

1. **Check OutSystems Forge**: Search for existing Capacitor-supported plugins.

1. **Adapt existing Cordova plugins**: If you have custom Cordova plugins, consider [adapting the existing Cordova plugin](../migrate-cordova-plugin.md) to make it compatible with Capacitor.

1. **Use community Capacitor plugins**: Integrate existing [official or community plugins](https://capacitorjs.com/docs/plugins).

1. **Build from scratch**: When no existing solution meets your specific requirements.

## Prerequisites

Before starting to build your Capacitor plugin, ensure you have:

* Node.js (version 16 or later) and npm installed
* Basic TypeScript/JavaScript knowledge for the web layer
* Native development experience:
    * iOS: Xcode, Swift or Objective-C knowledge
    * Android: Android Studio, Java or Kotlin knowledge

## Capacitor plugin architecture

Capacitor plugins follow a multi-layer architecture that enables web-to-native communication. Throughout this article, the [Barcode Plugin](https://github.com/ionic-team/capacitor-barcode-scanner/tree/main/plugin) repository serves as an example to demonstrate the plugin development process.

The repository has three main directories: `src`, `android`, and `ios`.

### Plugin structure and communication flow

* **Web layer (`src` directory)**: The `src` directory has the plugin's web layer and is the entry point of the plugin. It defines the plugin functions that are called from the mobile library. For detailed information, refer to [Set up Capacitor plugin project and implement web layer](setup-and-implementation.md).

* **Android layer (`android` directory)**: The `android` directory has the plugin's Android native code, in the form of an Android project, with its own `build.gradle` and `AndroidManifest.xml` files. For detailed information, refer to [Android native implementation](android-implementation.md).

* **iOS layer (`ios` directory)**: The `ios` directory has the plugin's iOS native code, in the form of an Xcode project, with its own `Info.plist` configuration file. For detailed information, refer to [iOS native implementation](ios-implementation.md).

## Plugin development workflow

Here are the high-level steps involved in building a Capacitor plugin from scratch:

![Flow diagram showing the steps to build a Capacitor plugin from scratch: Plan and design, Set up development and implement web layer, Implement native functionality, Configure platform integration, Test plugin, Package and publish plugin, Create ODC wrapper library, Distribute ODC plugin library in Forge.](images/capacitor-plugin-flow-diag.png "Capacitor Plugin Development Workflow")

1. **Plan and design**: Define your plugin's API, methods, and data structures.

1. **Set up development environment and implement web layer**: For detailed information, refer to [Setting up development environment and web layer implementation](setup-and-implementation.md).

1. **Implement native functionality**: Build iOS (Swift/Objective-C) and Android (Kotlin/Java) implementations for the plugin. For detailed information, refer to [Android native implementation](android-implementation.md) or [iOS native implementation](ios-implementation.md).

1. **Test the plugin**: Create test apps and verify functionality across platforms.

1. **Package and publish**: Package your plugin using a supported module format (ES Modules, CommonJS, or UMD), then publish to npm. For detailed information, refer to [Publishing](https://capacitorjs.com/docs/plugins/workflow#publishing).

1. **Create an ODC wrapper library**: Build a mobile library that integrates the plugin with ODC apps. For detailed information, refer to [Integrate Capacitor plugin into ODC app](integrate-plugin-in-app.md).

1. **Deploy and distribute**: Make the plugin library available to ODC developers through OutSystems Forge.

## Related resources

Explore these resources as you build your plugin:

* [Set up Capacitor plugin project and implement web layer](setup-and-implementation.md)

* [Android native implementation](android-implementation.md)

* [iOS native implementation](ios-implementation.md)

Explore these resources from the Capacitor official documentation:

* [Plugin development workflow](https://capacitorjs.com/docs/plugins/workflow)
  
* [Plugin tutorial](https://capacitorjs.com/docs/plugins/tutorial/introduction)
