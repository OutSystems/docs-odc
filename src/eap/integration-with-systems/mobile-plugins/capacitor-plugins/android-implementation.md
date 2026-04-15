---
guid: 4e24c9ec-1d93-42e6-9655-4609a585b73e
locale: en-us
summary: Implement Capacitor plugins on Android using Kotlin/Java for OutSystems Developer Cloud (ODC), including code examples for barcode scanner and configuring dependencies.
figma:
coverage-type:
  - apply
  - understand
topic:
app_type: mobile apps
platform-version: odc
audience:
  - mobile developers
tags: capacitor plugins, android native implementation, kotlin, java, android project, barcode scanner plugin
outsystems-tools:
  - none
helpids:
---
# Android native implementation

This article covers the Android native implementation for Capacitor plugins in ODC mobile apps. It is intended for mobile plugin developers who want to implement Android-specific functionality when [building Capacitor plugins](build-capacitor-plugin.md) from scratch.

For detailed information about how to build the Android layer of your Capacitor plugin, refer to the [Capacitor Android Plugin Guide](https://capacitorjs.com/docs/plugins/android).

## Prerequisites

To implement Android native functionality for your Capacitor plugin, ensure you have:

* Node.js (version 16 or later) and npm installed
* Basic knowledge of TypeScript/JavaScript for the web layer
* Native Android development experience:  Kotlin, Java
* Understanding of Capacitor plugin development

## Implement the Android plugin

The `android` directory contains the Android native code as an Android project with its own `build.gradle` and `AndroidManifest.xml` files. This directory includes the Android "bridge" - Kotlin or Java source files where plugin methods are implemented.

For the [Barcode Plugin](https://github.com/ionic-team/capacitor-barcode-scanner/tree/main/plugin), the main file is `OSBarcodePlugin.kt` with the `scanBarcode` method. Plugin methods called from the web layer are marked with the `@PluginMethod` annotation and receive a `PluginCall` parameter.

```kotlin
   @PluginMethod
    fun scanBarcode(call: PluginCall) {
        val hint = call.getInt("hint")
        val scanInstructions = call.getString("scanInstructions")
   // omitting other fields

        val parameters = OSBARCScanParameters(
                scanInstructions = scanInstructions,
                ... // omitting other fields
        )

        val scanIntent = Intent(activity, OSBARCScannerActivity::class.java)
                .putExtra("SCAN_PARAMETERS", parameters)

        startActivityForResult(call, scanIntent, "handleScanResult")
    }
```

For detailed information about troubleshooting, refer to [Troubleshooting Android issues](https://capacitorjs.com/docs/android/troubleshooting).

## Next steps

After building the Android native implementation, follow these steps:

1. [Develop the TypeScript interface layer](setup-and-implementation.md#develop-the-typescript-interface-layer-typescript-layer)
  
1. [Publish the plugin](https://capacitorjs.com/docs/plugins/workflow#publishing)
  
1. [Integrate the plugin into an ODC app](integrate-plugin-in-app.md)

## Related resources

Explore these resources from the official Capacitor documentation to learn more about plugin development:

* [Capacitor Android Plugin Guide](https://capacitorjs.com/docs/plugins/android)

* [Plugin tutorial](https://capacitorjs.com/docs/plugins/tutorial/introduction)
