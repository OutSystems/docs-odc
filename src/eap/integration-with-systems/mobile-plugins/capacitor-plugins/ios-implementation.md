---
guid: df9453d8-437e-41fe-b32c-57f9fcde7d24
locale: en-us
summary: This article describes how to build iOS native implementation for a Capacitor plugin using Barcode scanner example.
figma:
coverage-type:
  - apply
  - understand
topic:
app_type: mobile apps
platform-version: odc
audience:
  - mobile developers
tags: capacitor framework,Plugins,swift language
outsystems-tools:
  - none
helpids:
---
# iOS native implementation

This article explains how to implement iOS native support for Capacitor plugins in mobile apps. It is intended for mobile plugin developers who want to implement iOS-specific functionality when [building Capacitor plugins](build-capacitor-plugin.md) from scratch.

For detailed information about how to build the iOS layer of your Capacitor plugin, refer to [Capacitor iOS Plugin Guide](https://capacitorjs.com/docs/plugins/ios).

## Prerequisites

To implement iOS native functionality for your Capacitor plugin, ensure you have:

* Node.js (version 16 or later) and npm installed
* Basic knowledge of TypeScript/JavaScript for the web layer
* Native iOS development experience: Xcode, Swift, or Objective-C knowledge
* Understanding of Capacitor plugin development

## Implement the iOS plugin

The `ios` directory contains the native iOS code as an Xcode project with its own `Info.plist` configuration file. This directory includes the iOS Swift or Objective-C source files where plugin methods are implemented.

For the [Barcode Plugin](https://github.com/ionic-team/capacitor-barcode-scanner/tree/main/plugin), the main file is `CapacitorBarcodeScannerPlugin.swift`. The `scanBarcode` function is called from the web layer and receives a `CAPPluginCall` parameter.

Here's a code snippet of the scanBarcode function on iOS, in Swift:

```swift
@objc func scanBarcode(_ call: CAPPluginCall) {
        ... // omitted code

        Task {
            do {
                let scannedBarcode = try await manager.scanBarcode(with: scanArguments.scanInstructions, scanArguments.scanButtonText, scanArguments.cameraDirection, and: scanArguments.scanOrientation)
                call.resolve(["ScanResult": scannedBarcode])
            } catch OSBARCManagerError.cameraAccessDenied {
                call.sendError(with: OSBarcodeError.cameraAccessDenied)
            } catch OSBARCManagerError.scanningCancelled {
                call.sendError(with: OSBarcodeError.scanningCancelled)
            } catch {
                call.sendError(with: OSBarcodeError.scanningError)
            }
        }
    }
```

## Configure iOS permissions and dependencies

If your plugin has functionality on iOS that requires permissions from the end user, then you must implement the permissions pattern. For detailed information, refer to [Permissions](https://capacitorjs.com/docs/plugins/ios#permissions).

## Next steps

After building the iOS native implementation, follow these steps:

1. [Develop the TypeScript interface layer](setup-and-implementation.md#develop-the-typescript-interface-layer-typescript-layer)

1. [Publish the plugin](https://capacitorjs.com/docs/plugins/workflow#publishing)
  
1. [Integrate the plugin into an ODC app](integrate-plugin-in-app.md)

## Related resources

For more details, explore these resources from the official Capacitor documentation:

* [iOS Plugin Guide](https://capacitorjs.com/docs/plugins/ios)

* [Plugin tutorial](https://capacitorjs.com/docs/plugins/tutorial/introduction)
