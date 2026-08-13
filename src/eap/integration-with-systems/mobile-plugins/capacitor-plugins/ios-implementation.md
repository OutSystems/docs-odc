---
guid: df9453d8-437e-41fe-b32c-57f9fcde7d24
locale: en-us
summary: iOS native implementation for Capacitor plugins in OutSystems Developer Cloud (ODC) covers Swift code, SPM support, and Apple privacy manifests.
figma:
coverage-type:
  - apply
  - understand
topic:
app_type: mobile apps
platform-version: odc
audience:
  - Developer
tags:
  - Capacitor
  - iOS
  - Mobile app
  - Native App
  - Plugins
outsystems-tools:
  - none
helpids:
isautopublish: true
---
# iOS native implementation

This article explains how to implement iOS native support for Capacitor plugins in mobile apps. It is intended for mobile plugin developers who want to implement iOS-specific functionality when [building Capacitor plugins](build-capacitor-plugin.md) from scratch. For an overview of the plugin structure, refer to [Capacitor plugin architecture](capacitor-plugin-architecture.md).

For detailed information about how to build the iOS layer of your Capacitor plugin, refer to [Capacitor iOS Plugin Guide](https://capacitorjs.com/docs/plugins/ios).

## Prerequisites

Before implementing the iOS native functionality for your Capacitor plugin, ensure that you have:

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

## Add SPM support

Swift Package Manager (SPM) is replacing CocoaPods as the dependency management toolchain for iOS Capacitor builds. All plugins must include a `Package.swift` file to be compatible with the SPM build toolchain.

<div class="warning" markdown="1">

CocoaPods-only plugins are not compatible with SPM-based builds. Plugins that lack a `Package.swift` file cause build failures when the app uses the SPM toolchain.

</div>

### Create the `Package.swift` file

The Capacitor [plugin generator](https://capacitorjs.com/docs/plugins/creating-plugins#plugin-generator) scaffolds a `Package.swift` file automatically. If your plugin was created without one, add a `Package.swift` file to the root of your plugin project, alongside the `.podspec` file.

The `Package.swift` file must:

* Declare your plugin as a library target
* List any native dependencies your plugin requires
* Set the source path to `ios/Sources/PLUGIN_NAME`

Replace `PLUGIN_NAME` with the name of your plugin.

For detailed information about the Swift package format, refer to [PackageDescription](https://developer.apple.com/documentation/packagedescription) in the Apple developer documentation.

### Migrate existing plugins

If your plugin currently relies on a `.podspec` file only, add a `Package.swift` file alongside it. Maintain both files during the transition period so that your plugin remains compatible with both CocoaPods and SPM toolchains.

## Configure Apple privacy manifests

Apple requires all apps to provide a `PrivacyInfo.xcprivacy` file. If your plugin accesses specific APIs that impact user privacy, you must bundle this manifest within your plugin so that it is automatically included in the app's privacy report.

For a full list of APIs that require a recorded reason and the specific data types that Apple tracks, refer to [Privacy manifest files](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files) in the Apple developer documentation.

### Create the privacy manifest

To ensure compatibility with swift package manager (SPM) support and to follow standard iOS development practices, place your manifest inside the `Sources` directory of your plugin.

1. Navigate to your plugin's ios/ folder.

1. Create the file in the path -  `ios/Sources/{PLUGIN_NAME}/PrivacyInfo.xcprivacy` where PLUGIN_NAME is the name of your plugin.

1. In the privacy file, declare your `NSPrivacyAccessedAPITypes`, `NSPrivacyCollectedDataTypes`, and `NSPrivacyTracking` as required by your plugin's functionality.

### Update the `.podspec` file

To ensure the manifest is correctly discovered by Xcode without conflicting with the main app's own manifest, you must bundle it using `resource_bundles`. This namespaces the file within a unique bundle during the build process.

Update your plugin's `.podspec` file to include the privacy manifest as a resource bundle. Verify that the file path in the configuration matches the exact location where you created the `PrivacyInfo.xcprivacy` file in the previous step:

```ruby
Pod::Spec.new do |s|
  s.name = 'YOUR_PLUGIN_NAME'
  # ... other configuration ...

  # Bundles the privacy manifest into a dedicated resource bundle
  s.resource_bundles = {
    'YOUR_PLUGIN_NAME_Privacy' => ['ios/Sources/YourPluginName/PrivacyInfo.xcprivacy']
  }
end
```

Do not add the manifest to `s.resources`. Using `s.resources` places the file in the main app bundle's root. This causes a collision and potential file overwrite if the app developer or another plugin also provides a `PrivacyInfo.xcprivacy` file.

### Update the `Package.swift` file

If your plugin includes a `Package.swift` file, declare the privacy manifest as a resource in your package target. This ensures the manifest is bundled correctly when the app builds with the SPM toolchain.

```swift
.target(
    name: "YourPluginName",
    dependencies: [],
    path: "Sources/YourPluginName",
    resources: [
        .process("PrivacyInfo.xcprivacy")
    ]
)
```

## Next steps

After building the iOS native implementation, follow these steps:

1. [Develop the TypeScript interface layer](setup-and-implementation.md#develop-the-typescript-interface-layer-typescript-layer)

1. [Publish the plugin](https://capacitorjs.com/docs/plugins/workflow#publishing)
  
1. [Integrate the plugin into an ODC app](integrate-plugin-in-app.md)

## Related resources

For detailed information about plugin structure, refer to [Capacitor plugin architecture](capacitor-plugin-architecture.md).

For more details, explore these resources from the official Capacitor documentation:

* [iOS Plugin Guide](https://capacitorjs.com/docs/plugins/ios)

* [Plugin tutorial](https://capacitorjs.com/docs/plugins/tutorial/introduction)
