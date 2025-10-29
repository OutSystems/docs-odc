---
guid: 35892a80-96be-43bf-a89f-8d535b5b6f09
locale: en-us
summary: This article explains what are build action and how you can use build action to configure your mobile apps.
figma: 
coverage-type:
  - apply
  - understand
topic:
  - customize-mobile-apps
app_type: mobile apps
platform-version: odc
audience:
  - mobile developers
tags: Mobile,mobile app configuration,Extensibility
outsystems-tools:
  - odc studio
helpids: 
---

# Build actions

You can use build actions to perform native project modifications such as modifying **Android Manifest file**, **Info.plist** or **build.gradle** files in a structured and repeatable way. Build Actions use YAML-based configuration file and a set of predefined constructs to define and apply modifications to a mobile app during the build process. Build actions are integrated into the mobile app build process via [Extensibility](extensibility-configurations-json-schema.md).

You can configure your extensibility from **App** > **Edit app properties** > **Extensibility**.

Build actions are the modern replacement for Cordova hooks and is available in both the [app](extensibility-configurations/extensibility-app-reference.md) and [library](extensibility-configurations/extensibility-lib-reference.md) extensibility configuration.

<div class="info" markdown="1">

You can use build actions only for Capacitor apps.

</div>

The actions execute after the `cap sync` command during the build.

The build actions are platform specific. For detailed information about iOS build actions, refer to [iOS build actions](build-actions-iOS.md). For detailed information about Android build actions, refer to [Android build actions](build-actions-android.md).

## Use cases for build actions

Here are some of the platform-specific use cases for build actions:

### Android use cases

Here are some ways in which you can use build actions for customizing your Android app:

* Apply modifications to the **AndroidManifest.xml** file, such as updating attributes on the application node or injecting new XML elements.

* Insert new Gradle snippets, methods, or variables into files such as **build.gradle** to manage dependencies or apply plugins.

* Modify the content of existing JSON files such as **google-services.json** or other XML files.

### iOS use cases

Here are some ways in which you can use build actions for customizing your iOS app:

* Update the **Info.plist** file for the specified target and build. For example, to define custom URL schemes (CFBundleURLSchemes) or add other key-value entries.

* Set specific Xcode build settings, such as disabling Bitcode or specifying the Swift version.

* Modify the **.entitlements** file to configure app capabilities such as keychain access groups.

* Update the **PrivacyInfo.xcprivacy** file to comply with app store requirements.

## How build actions work

To use build actions in your app, follow these steps:

### Step 1: Create a YAML file
  
Define your build actions in a YAML file, for example, `buildAction.yaml file`. Define variables at the root level of your YAML file using the `variables` property. These variables can be strings, numbers, arrays, or objects, and can be referenced later in your build actions. You also must include a `platforms` property to define platform-specific operations. The allowed child keys are `android` and `ios`.

```yaml
variables:
  APP_NAME:
    type: string
  EXAMPLE_NUMBER:
    default: -1
    type: number

platforms:
  android:
    appName: $APP_NAME
  ios:
    displayName: $APP_NAME
```

### Step 2: Add the YAML file as a resource

In ODC Studio, add the YAML file as a resource. Set  **Deploy Action** to **Deploy to Target Directory**.

### Step 3: Configure Extensibility

Under **App > Edit app properties > Extensibility**, add the configuration to resolve variables defined within the YAML file. The `parameters` property is used to resolve the variables.

```yaml
{
  "version": "1",
  "buildConfigurations": 
  {
      "buildAction": 
      {
          "config": $resources.buildAction.yaml,
          "parameters": 
          {
              "APP_NAME": "Holiday tracker",
              "EXAMPLE_NUMBER": 5
          }
               
      }
  }
}
```

### Step 4: Build the app

Build the app in the ODC Portal. While building the package, ensure that you selected MABS 12 or greater.

## Conditional execution of build actions

Many build actions support conditional execution. This allows you to run an action only when a specified condition is met. The supported conditional expressions include:

**eq**: Evaluates to `true` if both arguments are equal.
Example: `eq('hello', 'hello')`

**ne**: Evaluates to `true` if both arguments are not equal.
Example: `ne('hello', 'goodbye')`

**ge**: Evaluates to `true` if the left argument is greater than or equal to the right. The arguments must be numeric.
Example: `ge(3,1)`

**le**: Evaluates to `true` if the left argument is less than or equal to the right. The arguments must be numeric.
Example: `le(1,3)`

**gt**: Evaluates to `true` if the left argument is greater than or equal to the right. The arguments must be numeric.
Example: `gt(3,1)`

**lt**: Evaluates to `true` if the left argument is less than or equal to the right. The arguments must be numeric.
Example: `lt(1,3)`

```yaml
variables:
  APPLY_PATH:
    default: 0
    type: number

platforms:
  ios:
    code:
      - file: App/AppDelegate.swift
        condition: ge($APPLY_PATH, 0) # greater-than or equal
        patchFile: patches/ChangeAppDelegate.patch
```

## Related resources

Here's the platform specific build actions reference files:

* [iOS build actions](build-actions-iOS.md)

* [Android build actions](build-actions-android.md)

Here's the detailed information about extensibility configuration JSON schema:

* [Extensibility configuration JSON schema](extensibility-configurations-json-schema.md)
  
* [App extensibility configuration JSON schema](extensibility-configurations/extensibility-app-reference.md)
  
* [Library extensibility configuration JSON schema](extensibility-configurations/extensibility-lib-reference.md)
