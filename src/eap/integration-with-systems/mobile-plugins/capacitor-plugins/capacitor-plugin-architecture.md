---
guid: eadeb06d-11aa-4d20-a6e0-5b9f60d5c746
locale: en-us
summary: Capacitor plugin architecture in OutSystems Developer Cloud (ODC) uses three layers (web, Android, iOS) bridged by the Capacitor runtime.
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=10065-2
coverage-type:
  - understand
content-type:
  - conceptual
topic:
app_type: mobile apps
platform-version: odc
audience:
  - Developer
  - Tech lead
tags:
  - Android
  - Architecture
  - Capacitor
  - JavaScript
  - Mobile app
  - Native App
  - Plugins
outsystems-tools:
  - odc studio
helpids:
isautopublish: true
---

# Capacitor plugin architecture

This article explains how Capacitor plugins are structured and how the Capacitor bridge routes calls between the JavaScript layer and native device code.

Understanding the plugin architecture helps you make informed decisions when building custom plugins, integrating community plugins, or troubleshooting plugin behavior in ODC mobile apps.

## Plugin layers {#plugin-layers}

A Capacitor plugin is organized into three layers. Each layer handles a distinct responsibility, and together they enable your ODC mobile app to access native device capabilities.

The three layers map directly to the plugin repository structure:

* **Web layer (`src` directory)**: The `src` directory has the plugin's web layer and is the entry point of the plugin. It defines the plugin functions that are called from the mobile library. For detailed information, refer to [Set up Capacitor plugin project and implement web layer](setup-and-implementation.md).

* **Android layer (`android` directory)**: The `android` directory has the plugin's Android native code, in the form of an Android project, with its own `build.gradle` and `AndroidManifest.xml` files. For detailed information, refer to [Android native implementation](android-implementation.md).

* **iOS layer (`ios` directory)**: The `ios` directory has the plugin's iOS native code, in the form of an Xcode project, with its own `Info.plist` configuration file. For detailed information, refer to [iOS native implementation](ios-implementation.md).

Each layer is independently maintained. When you need to change platform-specific behavior, you modify only the relevant layer without affecting the others.

## The Capacitor bridge {#capacitor-bridge}

The Capacitor bridge is the runtime that connects the JavaScript layer to native platform code. It handles serialization, routing, and the return of results back to JavaScript.

When you build a mobile app with MABS 12 or later using the Capacitor runtime, all referenced Capacitor plugins are automatically bundled and registered. The bridge makes them available globally through `window.CapacitorPlugins` at runtime.

Your ODC mobile library accesses a plugin through a JavaScript node using the following pattern:

```javascript
window.CapacitorPlugins.PLUGIN_NAME.methodName(params)
```

The bridge resolves `PLUGIN_NAME` to the correct native implementation for the current platform (Android or iOS) and executes the corresponding native code.

## Communication flow {#communication-flow}

The following steps describe how a plugin call travels from your ODC app to native device code and back.

1. A screen or action in your ODC app calls a public client action from a mobile library.
1. The client action in the mobile library executes the JavaScript node.
1. The JavaScript node in turn calls the plugin method using `window.CapacitorPlugins`.
1. The Capacitor bridge receives the call and routes it to the appropriate platform implementation.
1. Native code runs on the device (Android or iOS).
1. The result is returned from the native code through the bridge to the JavaScript layer.
1. The JavaScript node assigns the result to the client action output parameters.
1. The client action returns the result to the caller in your ODC app.

The bridge handles all serialization between JavaScript types and native types, so your mobile library only needs to work with JavaScript values.

The following sequence diagram shows the plugin call from the ODC app to native device code and back.

![Sequence diagram showing an ODC app calling a client action in a mobile library, executing a JavaScript node that invokes window.CapacitorPlugins.METHOD, which the Capacitor bridge routes to native code and returns the result back through JavaScript and the library to the app.](images/app-plugin-native-code-diag.png "Sequence diagram of ODC app calling a Capacitor plugin through the bridge")

## Related resources {#related-resources}

To build and integrate plugins, refer to:

* [Build a Capacitor plugin from scratch](build-capacitor-plugin.md)
* [Integrate Capacitor plugin into a mobile app](integrate-plugin-in-app.md)

To work with existing Cordova plugins alongside Capacitor, refer to:

* [Implement a dual-stack plugin](dual-stack-plugin.md)
* [Adapt a Cordova plugin for compatibility with Capacitor](../migrate-cordova-plugin.md)
