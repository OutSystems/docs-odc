---
guid: 3e9cca36-951b-4500-9ad3-8a930b13848e
locale: en-us
summary: This documents provides reference information for iOS build actions explaining the different settings and properties of the JSON file.
figma: 
coverage-type:
  - remember
  - understand
topic:
  - customize-mobile-apps
app_type: mobile apps
platform-version: odc
audience:
  - mobile developers
tags: Mobile,native mobile configuration,extensibility configuration
outsystems-tools:
  - odc studio
  - odc portal
helpids: 
---

# iOS build actions

This article provides reference documentation for all iOS build actions available in mobile app development. [Build actions](build-actions.md) allow you to customize and configure iOS mobile apps beyond the standard low-code capabilities such as updating and modifying **Info.plist** file and setting specific build settings.

## Targets and builds

Build actions for iOS support different targets and builds. These are optional and specified as parent keys in the JSON. The following build actions example omits targets and builds, but they are always valid.

```json
{
    "platforms": {
        "ios": {
            "productName": "Every build and target gets this value!",
            "builds": {
                "Debug": { "displayName": "Debug App" },
                "Release": { "displayName": "Prod App" }
            },
            "targets": {
                "App": /* Operations for the App target (the default for Capacitor apps) */,
                "My App Clip": {
                    "builds": { "Debug": /* Operations for the My App Clip target and Debug build */,
                    "Release": /* Operations for the My App Clip target and Release build */ }
                }
            }
        }
    }
}
```

## Actions

### displayName

**Type**:

```TypeScript
string
```

**Description**: Updates the app display name, which appears on a device when installed.

**Conditional**: No

```json
{
    "platforms": {
        "ios": {
            "displayName": "OutSystems App Name"
        }
    }
}
```

### productName

**Type**:

```TypeScript
string
```

**Description**: Updates the product name, which appears in the App Store and on a device when installed.

**Conditional**: No

```json
{
    "platforms": {
        "ios": {
            "productName": "OutSystems App Name"
        }
    }
}
```

### buildSettings

**Type**:

```TypeScript
Record<string, string>
```

**Description**: Sets build settings.

**Conditional**: Yes

```json
{
    "platforms": {
        "ios": {
            "buildSettings": {
                "ENABLE_BITCODE": false,
                "SWIFT_VERSION": "5.0"
            }
        }
    }
}
```

### buildPhases

**Type**:

```TypeScript
Array<{
  comment: string;
  shellPath: string;
  shellScript: string;
  inputPaths?: Array<string>;
  outputPaths?: Array<string>;
  replace?: boolean;
}>;
```

**Description**: Sets build phases scripts to run. By default, values should be merge unless replace is set to `true` to overwrite the entire target object with a given comment.

**Conditional**: Yes

```json
{
    "platforms": {
        "ios": {
            "buildPhases": [
                {
                    "replace": true,
                    "comment": "Crashlytics",
                    "shellPath": "/bin/sh",
                    "shellScript": "\"${PODS_ROOT}/FirebaseCrashlytics/run\"",
                    "inputPaths": [
                        "\"$(BUILT_PRODUCTS_DIR)/$(INFOPLIST_PATH)\""
                    ]
                }
            ]
        }
    }
}
```

### plist

**Type**:

```TypeScript
Array<{
  file?: string;
  replace?: boolean;
  entries: Array<any>;
}>;
```

**Description**: Updates the **Info.plist** file for the specified target and build, or default target and all builds when not specified. Or updates a given plist file if provided.

By default, values should be merged unless replace is set to `true` to overwrite the entire target object.

**Conditional**: Yes

```json
{
    "platforms": {
        "ios": {
            "plist": [
                {
                    "replace": true,
                    "file": "GoogleService-Info.plist",
                    "entries": [{ "Key": "Value" }]
                },
                {
                    "replace": false,
                    "entries": [
                        {
                            "CFBundleURLTypes": [
                                {
                                    "CFBundleURLSchemes": [
                                        "AdditionalBundleURLScheme"
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }
}
```

### xcprivacy

**Type**:

```TypeScript
Array<{
  replace?: boolean;
  entries: Array<any>;
}>;
```

**Description**: Updates the PrivacyInfo.xcprivacy file for the specified target and build, or default target and all builds of not specified.

By default, values are merged unless replace is set to `true` to overwrite the entire target object.

**Conditional**: Yes

```json
{
    "platforms": {
        "ios": {
            "xcprivacy": [
                {
                    "replace": true,
                    "entries": [{ "NSPrivacyTracking": [] }]
                },
                {
                    "replace": false,
                    "entries": [
                        {
                            "NSPrivacyAccessedAPITypes": {
                                "NSPrivacyAccessedAPIType": "NSPrivacyAccessedAPICategoryUserDefaults",
                                "NSPrivacyAccessedAPITypeReasons": ["CA92.1"]
                            }
                        }
                    ]
                }
            ]
        }
    }
}
```

### entitlements

**Type**:

```TypeScript
Array<{
  entries: Array<Record<string, boolean | string | string[]>>;
  replace?: boolean;
}>;
```

**Description**: Updates the .entitlements file for the specified target and build, or the default target and all builds if not specified.

By default, values are merged unless replace is set to `true` to overwrite the entire target object.

**Conditional**: Yes

```json
{
    "platforms": {
        "ios": {
            "entitlements": {
                "replace": true,
                "entries": [
                    {
                        "keychain-access-groups": [
                            "$BUNDLE_ID",
                            "com.microsoft.intune.mam",
                            "com.microsoft.adalcache"
                        ]
                    },
                    { "something-else": true }
                ]
            }
        }
    }
}
```

### frameworks

**Type**:

```TypeScript
Array<{
  name: string;
  customFramework?: boolean;
  link?: boolean;
  embed?: boolean;
}>;
```

**Description**: Adds core frameworks to the iOS project.

**Conditional**: Yes

```json
{
    "platforms": {
        "ios": {
            "frameworks": ["AudioToolbox.framework", "CoreServices.framework"]
        }
    }
}
```

### json

**Type**:

```TypeScript
Array<
  | {
      file: string;
      set: object;
    }
  | {
      file: string;
      merge: object;
    }
>;

```

**Description**: Modifies the content of JSON files. It requires a file relative to the root of the iOS project.

The operation supports two modes:

* `set`: Overrides the element (and clobber any children).
* `merge`: Merges the values.

**Conditional**: Yes

```json
{
    "platforms": {
        "ios": {
            "json": [
                {
                    "file": "google-services.json",
                    "set": {
                        "project_info": {
                            "project_id": "MY_ID"
                        }
                    }
                },
                {
                    "file": "google-services.json",
                    "merge": {
                        "data": {
                            "field": "MY_FIELD"
                        }
                    }
                }
            ]
        }
    }
}
```

### xml

**Type**:

```TypeScript
Array<
  | {
      file: string;
      target: string;
      attrs: Record<string, string>;
    }
  | {
      file: string;
      target: string;
      merge: string;
    }
  | {
      file: string;
      target: string;
      inject: string;
    }
  | {
      file: string;
      target: string;
      deleteAttributes: Array<string>;
    }
  | {
      file: string;
      target: string;
      replace: string;
    }
  | {
      file: string;
      delete: string;
    }
>;
```

**Description**: Applies modifications to the specified XML file.

* `attrs`: Updates the attributes of the given target node.
* `merge`: Merges the given XML tree supplied to merge with the given target. Merge expects a matching root node to be supplied. The merge algorithm merges any nodes that match with at least all of the supplied node's attributes, or appends any new children not found in the target node.
* `inject`: Injects the given XML tree supplied to inject inside of the given target.
* `delete`: Deletes nodes specified by delete in XPath format.
* `deleteAttributes`: Deletes the given attributes in deleteAttributes inside of the given target.

**Conditional**: Yes

```json
{
    "platforms": {
        "ios": {
            "xml": [
                {
                    "file": "app/file.xml",
                    "target": "entries/field",
                    "merge": "<field>\n  <string>Value</string>\n</field>\n"
                }
            ]
        }
    }
}
```

### copy

**Type**:

```TypeScript
Array<{
  src: string;
  dest: string;
}>;
```

**Description**: Copies files, directories, or URLs relative to the root of the iOS project.

**Conditional**: Yes

```json
{
    "platforms": {
        "ios": {
            "copy": [
                {
                    "src": "../firebase/GoogleService-Info.plist",
                    "dest": "App/GoogleService-Info.plist"
                },
                {
                    "src": "old/path/of/directory",
                    "dest": "new/path/of/directory"
                },
                {
                    "src": "https://example.com/file.png",
                    "dest": "new/path/of/file.png"
                }
            ]
        }
    }
}
```

### strings

**Type**:

```TypeScript
Array<
  | {
      file: string;
      set: Record<string, string>;
    }
  | {
      file: string;
      setFromJson: string;
    }
>;
```

**Description**: Updates `.strings` files to add/update localization/translation strings.

It allows the direct definition of objects into the file using the `set` key, or to load values from a JSON file using the `setFromJson` key.

**Conditional**: Yes

```json
{
    "platforms": {
        "ios": {
            "strings": [
                {
                    "file": "App/Localizable.strings",
                    "set": {
                        "Insert Element": "Insert Element"
                    }
                },
                {
                    "file": "App/Localizable.strings",
                    "setFromJson": "lang/en.json"
                }
            ]
        }
    }
}
```

### xcconfig

**Type**:

```TypeScript
Array<{
  file: string;
  set: Record<string, string>;
}>
```

**Description**: Updates `.xcconfig` files to add/update build configurations.

**Conditional**: Yes

```json
{
    "platforms": {
        "ios": {
            "xcconfig": [
                {
                    "file": "App/Config.xcconfig",
                    "set": {
                        "PRODUCT_NAME": "$NAME"
                    }
                }
            ]
        }
    }
}
```

### code

**Type**:

```TypeScript
Array<
  | {
      source: string;
      compilerFlags?: string;
    }
  | {
      file: string;
      target: string;
      replace: string;
    }
  | {
      file: string;
      patchFile: string;
    }
>
```

**Description**: Adds source code files to the project or applies patches to source files.

Adds a given source file and adds it to the project with `compilerFlags` if needed. It also allows direct replacement on files by setting a target and the replace text, or from patch files using the `patchFile` key.

iOS also has the code action, but the type of the object is slightly different.

**Conditional**: Yes

```json
{
    "platforms": {
        "ios": {
            "code": [
                {
                    "source": "files/CustomBridge.swift"
                },
                {
                    "source": "files/FooBarLib.a",
                    "compilerFlags": "-fno-objc-arc"
                },
                {
                    "file": "App/AppDelegate.swift",
                    "target": "/import Capacitor/",
                    "replace": "import Capacitor\nimport WatchConnectivity\n"
                },
                {
                    "file": "App/AppDelegate.swift",
                    "patchFile": "patches/ChangeAppDelegate.patch"
                }
            ]
        }
    }
}
```

### tar

**Type**:

```TypeScript
Array<{
  src: string;
  dest: string;
  command: 'c' | 'r' | 'u' | 'x';
}>;
```

**Description**: Adds tar support to build actions.

**Conditional**: Yes

```json
{
    "platforms": {
        "ios": {
            "tar": [
                {
                    "source": "files/FooBar.tar",
                    "targetDir": "files/FooBar",
                    "action": "x"
                }
            ]
        }
    }
}
```
