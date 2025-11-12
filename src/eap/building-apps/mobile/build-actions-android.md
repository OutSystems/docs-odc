---
guid: e694bb62-9815-4b62-9ed6-7ce9c35653a5
locale: en-us
summary: This articles provides reference information for Android Build Actions in mobile apps, including all available properties, actions, and configuration options.
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
tags: Mobile,Android,Build Actions,Extensibility,Configuration
outsystems-tools:
  - odc studio
  - odc portal
helpids: 
---

# Android build actions

This article provides reference documentation for all Android build actions available in mobile app development. [Build Actions](build-actions.md) allow you to customize and configure Android mobile apps beyond the standard low-code capabilities such as modifying Android Manifest file, inserting new Gradle snippets.

## appName

**Type**:

```TypeScript
string
```

**Description**: Updates the app display name, by changing the label attribute in the AndroidManifest.xml file, or setting the strings resource value when a resource value is referenced in the manifest.

**Conditional**: No

```json
{
    "platforms": {
        "android": {
            "appName": "OutSystems App Name"
        }
    }
}
```

## manifest

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
      merge: string; // xml string to merge
    }
  | {
      file: string;
      target: string;
      inject: string; // xml string to inject
    }
  | {
      file: string;
      target: string;
      deleteAttributes: Array<string>;
    }
  | {
      file: string;
      delete: string; // xpath
    }
>
```

**Description**: Applies modifications against Android Manifest XML files.

* `attrs`: Updates the attributes to the target XML element.
* `merge`: Merges the given XML tree.
* `inject`: Injects the given XML tree.
* `deleteAttributes`: Deletes the given attributes.
* `delete`: Deletes nodes selected targeted with provided xpath.

**Conditional**: Yes

```json
{
    "platforms": {
        "android": {
            "manifest": [
                {
                    "file": "AndroidManifest.xml",
                    "target": "manifest/application",
                    "attrs": {
                        "android:name": "com.ionicframework.intune.IntuneApplication"
                    }
                },
                {
                    "file": "AndroidManifest.xml",
                    "target": "manifest",
                    "merge": "<queries>\n    <package android:name=\"com.azure.authenticator\" />\n</queries>\n"
                },
                {
                    "file": "AndroidManifest.xml",
                    "target": "manifest",
                    "inject": "<sample-tag>\n    <package android:name=\"com.azure.authenticator\" />\n</sample-tag>\n"
                },
                {
                    "file": "AndroidManifest.xml",
                    "target": "manifest/application/application",
                    "deleteAttributes": ["android:name", "another:attribute"]
                },
                {
                    "file": "AndroidManifest.xml",
                    "delete": "//intent-filter"
                }
            ]
        }
    }
}
```

## gradle

**Type**:

```TypeScript
Array<
  | {
      file: string;
      target: object;
      insert: string;
    }
  | {
      file: string;
      target: object;
      insert: Array<object>;
      insertType: 'variable' | 'method' | undefined; // 'method' is default
    }
  | {
      file: string;
      target: object;
      replace: object;
    }
>;
```

**Description**: Applies modifications to Gradle files.

**Insert**:

* Inserts new Gradle snippets.
* Accepts either a raw string of Groovy-based Gradle, or an object.
* When inserting an object, this operation takes an `insertType` of either `method` (default) or `variable` which will create either a method call (`methodName methodArg`) or an assignment (`variable = value`).
**Replace**: Replaces existing Gradle configurations.

**Conditional**: Yes

```json
{
    "platforms": {
        "android": {
            "gradle": [
                {
                    "file": "build.gradle",
                    "target": {
                        "buildscript": null
                    },
                    "insert": [
                        {
                            "classpath": "'org.javassist:javassist:3.27.0-GA'"
                        }
                    ]
                },
                {
                    "file": "build.gradle",
                    "target": {
                        "allprojects": {
                            "repositories": null
                        }
                    },
                    "insert": [
                        {
                            "maven": [
                                {
                                    "url": "https://example.com"
                                },
                                {
                                    "name": "Duo-SDK-Feed"
                                }
                            ]
                        }
                    ]
                },
                {
                    "file": "variables.gradle",
                    "target": {
                        "ext": null
                    },
                    "insertType": "variable",
                    "insert": [
                        {
                            "firebaseMessagingVersion": "20.0.6"
                        }
                    ]
                },
                {
                    "file": "app/build.gradle",
                    "target": null,
                    "insert": "apply plugin: 'com.microsoft.intune.mam'\nintunemam {\n  includeExternalLibraries = [\"androidx.*\", \"com.getcapacitor.*\"]\n}\n"
                },
                {
                    "file": "app/build.gradle",
                    "target": {
                        "android": {
                            "buildTypes": {
                                "release": {
                                    "minifyEnabled": null
                                }
                            }
                        }
                    },
                    "replace": {
                        "minifyEnabled": true
                    }
                },
                {
                    "file": "app/build.gradle",
                    "target": {
                        "android": {
                            "buildTypes": {
                                "implementation": null
                            }
                        }
                    },
                    "replace": {
                        "implementation": "'test-implementation'"
                    }
                }
            ]
        }
    }
}
```

## res

**Type**:

```TypeScript
Array<
  | {
      path: string;
      file: string;
      text: string;
    }
  | {
      path: string;
      file: string;
      source: string;
    }
>;
```

**Description**: Creates new resource files that will be stored under the `res` folder of the Android project structure.

**Conditional**: Yes

```json
{
    "platforms": {
        "android": {
            "res": [
                {
                    "path": "raw",
                    "file": "auth_config.json",
                    "text": "{\n  \"client_id\": \"$INTUNE_CLIENT_ID\",\n  \"authorization_user_agent\": \"DEFAULT\",\n  \"redirect_uri\": \"msauth://$PACKAGE_NAME/$HASH\",\n  \"broker_redirect_uri_registered\": true,\n  \"authorities\": [\n    {\n      \"type\": \"AAD\",\n      \"audience\": {\n        \"type\": \"AzureADMyOrg\",\n        \"tenant_id\": \"$INTUNE_TENANT_ID\"\n      }\n    }\n  ]\n}\n"
                },
                {
                    "path": "drawable",
                    "file": "icon.png",
                    "source": "../common/test/fixtures/icon.png"
                },
                {
                    "path": "drawable",
                    "file": "remote-icon.png",
                    "source": "https://www.outsystems.com/icon.png"
                }
            ]
        }
    }
}
```

## json

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

**Description**: Modifies the content of JSON files.

* **set**: Overrides the element.
* **merge**: Merges the values.

**Conditional**: Yes

```json
{
    "platforms": {
        "android": {
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

## xml

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
      merge: string; // xml string to merge
    }
  | {
      file: string;
      target: string;
      inject: string; // xml string to inject
    }
  | {
      file: string;
      target: string;
      deleteAttributes: Array<string>;
    }
  | {
      file: string;
      target: string;
      replace: string; // xml string to replace
    }
  | {
      file: string;
      delete: string; // xpath
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
        "android": {
            "xml": [
                {
                    "file": "app/file.xml",
                    "target": "entries/field",
                    "merge": "<field>\n  <string>Value</string>\n</field>\n"
                },
                {
                    "resFile": "values/strings.xml",
                    "target": "resources/string[@name=\"app_name\"]",
                    "replace": "<string name=\"app_name\">Awesome App</string>\n"
                }
            ]
        }
    }
}
```

## copy

**Type**:

```TypeScript
Array<{ src: string; dest: string; }>
```

**Description**: Copies files, directories, or URLs relative to the root of the Android project.

**Conditional**: Yes

```json
{
    "platforms": {
        "android": {
            "copy": [
                {
                    "src": "../firebase/google-services.json",
                    "dest": "app/google-services.json"
                },
                {
                    "src": "old/path/of/directory",
                    "dest": "new/path/of/directory"
                },
                {
                    "src": "https://www.outsystems.com/file.png",
                    "dest": "new/path/of/file.png"
                }
            ]
        }
    }
}
```

## code

**Type**:

```TypeScript
Array<
  | {
      source: string;
      targetDir: string;
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
>;
```

**Description**: Adds source code files to the project or applies patches to source files.

* **source**: Copies files from the specified source to the specified `targetDir`.
    * `targetDir` is required when using source on Android.

* **file**: Updates the specified file.
    * **replace**: Replaces the target with the provided string.
    * **patchFile**: Applies the provided patch file to the target file.

**Conditional**: Yes

```json
{
    "platforms": {
        "android": {
            "code": [
                {
                    "source": "files/FooBar.java",
                    "targetDir": "src/com/foo/bar"
                },
                {
                    "file": "MainActivity.java",
                    "target": "/import com.getcapacitor.BridgeActivity;/",
                    "replace": "import com.getcapacitor.BridgeActivity;\nimport com.cordova.plugin.splashscreenvideo.VideoDialogFragment;\n"
                },
                {
                    "file": "MainActivity.java",
                    "patchFile": "patches/MainActivity.patch"
                }
            ]
        }
    }
}
```

## tar

**Type**:

```TypeScript
Array<{ src: string; dest: string; command: 'c' | 'r' | 'u' | 'x'; }>
```

**Description**: Adds tar support to build actions.

**Conditional**: Yes

```json
{
    "platforms": {
        "android": {
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
