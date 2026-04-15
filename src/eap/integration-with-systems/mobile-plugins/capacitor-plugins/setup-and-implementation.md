---
guid: 40b21bde-218b-4ae4-b86c-e2970b835391
locale: en-us
summary: This article explains how to scaffold a Capacitor plugin project and define the interface layer.
figma:
coverage-type:
  - apply
  - understand
topic:
app_type: mobile apps
platform-version: odc
audience:
  - mobile developers
tags: Plugins,capacitor framework,typescript
outsystems-tools:
  - none
helpids:
---
# Set up Capacitor plugin project and define the interface layer

This article covers the initial setup and web layer implementation that serves as the entry point for your plugin's functionality. It is intended for mobile plugin developers who want to [build Capacitor plugin](build-capacitor-plugin.md) from scratch.

Before implementing platform-specific code, you must first design your plugin's API using TypeScript. This API defines the methods and data structures that will be consistent across all platforms. For detailed information about designing the interface, refer to [Designing the Plugin API](https://capacitorjs.com/docs/plugins/tutorial/designing-the-plugin-api).

## Create the plugin project

Ensure that you use the latest Node LTS version and npm 6+.

Use the Capacitor [plugin generator](https://capacitorjs.com/docs/plugins/creating-plugins#plugin-generator) to scaffold your plugin project.

It sets up the complete plugin structure, which includes:

* TypeScript definition files for defining your JavaScript interface
* An iOS directory with Swift plugin code and a `Package.swift` configuration file
* An Android directory containing Java plugin classes and Gradle build files
* A pre-configured `package.json` file with essential dependencies

For information about different files, explore the [Barcode plugin](https://github.com/ionic-team/capacitor-barcode-scanner/tree/main/plugin) repository that has three main directories `src`, `android`, and `ios`.

## Develop the TypeScript interface layer {#typescript-layer}

The TypeScript interface layer defines your plugin's API and serves as the bridge between your app and the native implementations. This layer consists of two key components: defining the plugin interface and registering the plugin.

### Define the plugin interface

Define the method's signature in the exported TypeScript interface for your plugin in `src/definitions.ts`.

In the example, `scanBarcode` method is added which takes `scanInstructions`, `cameraDirection`, `scanOrientation`, `scanButton`, `scanText`, `hint`, `scanningLibrary` as input and generates a string as output.

```typescript
export interface CapacitorBarcodeScanner {
  /**
   * Scan a barcode or QR code
   */
  scanBarcode(options: ScanBarcodeOptions): Promise<ScanBarcodeResult>;
}

export interface ScanBarcodeOptions {
  scanInstructions?: string;
  cameraDirection?: string;
  scanOrientation?: string;
  scanButton?: boolean;
  scanText?: string;
  hint?: number;
  android?: {
    scanningLibrary?: string;
  };
}

export interface ScanBarcodeResult {
  ScanResult: string;
}
```

### Register the plugin

Update the `src/index.ts` file to register the plugin and export it for use in your apps. To register, using the `registerPlugin()` module exported from `@capacitor/core`.

For a complete example, refer to the [index.ts](https://github.com/ionic-team/capacitor-barcode-scanner/blob/main/plugin/src/index.ts) file in the barcode scanner plugin repository.

## Next steps

Build the native implementations for each platform:

* [Android native implementation](android-implementation.md)
  
* [iOS native implementation](ios-implementation.md)

## Related resources

Explore these resources from the official Capacitor documentation to learn more about plugin development:

* [Plugin development workflow](https://capacitorjs.com/docs/plugins/workflow)
  
* [Designing the Plugin API](https://capacitorjs.com/docs/plugins/tutorial/designing-the-plugin-api)
  
* [Plugin tutorial](https://capacitorjs.com/docs/plugins/tutorial/introduction)
