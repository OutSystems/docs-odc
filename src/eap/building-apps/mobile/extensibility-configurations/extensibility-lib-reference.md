---
guid: 50dda025-21a0-4063-a2e1-483761eb7797
locale: en-us
summary: This article provides detailed information about Library extensibility configuration schema.
figma:
coverage-type:
  - remember
topic:
app_type: mobile apps
platform-version: odc
audience:
  - mobile developers
tags: json configuration,Mobile,mobile app build service,mobile app extensibility,mobile apps
outsystems-tools:
  - none
helpids:
---
# Library (plugin) extensibility configuration JSON schema

<div class="info" markdown="1">

The schema may change with every new MABS version.

</div>

[pluginConfigurations](#pluginconfigurations)

[properties](#properties)

[cordova](#cordova)

[preferences](#preferences)

[capacitor](#capacitor)

[configurations](#configurations)

[permissions](#permissions)

[android](#android-android)

[ios](#ios-ios)

[buildConfigurations](#buildconfigurations)

[properties](#properties-properties-1)

[cordova](#cordova-cordova-1)

[source](#source)

[capacitor](#capacitor-capacitor-1)

[source](#source-source-1)

[resources](#resources)

[android](#android-android-1)

[ios](#ios-ios-1)

[buildAction](#buildaction)

[config](#config)

[parameters](#parameters)

The extensibility configuration for libraries allows the declaration of the associated Cordova plugins, Capacitor plugins, or both.

| Property | Type | Required |
| :---- | :---- | :---- |
| [pluginConfigurations](#pluginconfigurations) | `object` | Optional |
| [buildConfigurations](#buildconfigurations) | `object` | Optional |


**Example**

```json
{
  "pluginConfigurations": {
    ...
  },
  "buildConfigurations": {
    ...
  }
}

```

## pluginConfigurations 

The plugin specification.

`pluginConfigurations`

* Optional  
* Type: `object`

### properties 

| Property | Type | Required |
| :---- | :---- | :---- |
| [cordova](#cordova) | `object` | Required if `capacitor` is missing |
| [capacitor](#capacitor) | `object` | Required if `cordova` is missing |
| [permissions](#permissions) | `array of object` | Optional |

### cordova

An object with the required specification for a given Cordova plugin.

Example:

```json
{
  "pluginConfigurations": {
    "cordova": {
      "preferences": {
        "a": "b"
      }
    }
  }
}
```

`cordova`

* Optional  
* Type: `object`

**Properties**

| Property | Type | Required |
| :---- | :---- | :---- |
| [preferences](#preferences) | `string` | Required |


#### preferences 

A set of Cordova [preferences](https://cordova.apache.org/docs/en/11.x/config_ref/#preference) associated with the plugin. Configuration values can be static or a reference to a Setting. Additionally, configurations can be declared globally or per platform, with the platform-specific value taking precedence over the global one.

**Example**

```json
{
  "pluginConfigurations": {
    "cordova": {
      "preferences": {
        "SomePreference": "SomeValue",
        "SomeInteger": 1,
        "SomeNumber": 8.9,
        "SomeBool": true,
        "android": {
          "SomePreference": "SomeAndroidValue",
          "SomeInteger": 2,
          "SomeNumber": 7.6,
          "SomeBool": false
        },
        "ios": {
          "SomePreference": "SomeIosValue",
          "SomeInteger": 3,
          "SomeNumber": 4.5,
          "SomeBool": false
        }
      }
    }
  }
}

```

### capacitor 

An object with the required specification for a given Capacitor plugin.

`capacitor`

* Optional  
* Type: `object`

**Properties**

| Property | Type | Required |
| :---- | :---- | :---- |
| [configurations](#configurations) | `object` | Optional |

#### configurations 

An object with configuration values specified by plugin class name. Multiple configurations can be provided for multiple plugins simultaneously. This is useful in scenarios where a plugin depends on other plugins that require configurations on their own.

Configurations can be set globally or per platform under `android` or `ios` properties.

Example:

```json
{
  "pluginConfigurations": {
    "capacitor": {
      "configurations": {
        "Keyboard": {
          "ios": {
            "resize": "body"
          },
          "android": {
            "resizeOnFullScreen":"true"
          }
        },
        "AnotherPlugin": {
          "ios": {
            "Pref5Dynamic": "$settings.Pref5DynamicValue",
            "Pref6Static": "tangerine"
          },
          "android": {
            "Pref5Dynamic": "$settings.Pref5DynamicValue",
            "Pref6Static": "lemon"
          }
        }
      }
    }
  }
}
```

`configurations`

* Optional  
* Type: `object`

**Properties**

| Property | Type | Required |
| :---- | :---- | :---- |
| [`android`](#android-2) | `object` | Optional |
| `ios` | `object` | Optional |
| Additional properties | `object` | Optional |

#### android {#android-2}

Plugin configurations specific to Android. If a configuration with the same name exists globally (i.e. at the root of `configurations` object), the value from `android` takes precedence.

`android`

* Optional  
* Type: `object`

Properties:

| Property | Type | Required |
| :---- | :---- | :---- |
| Additional properties | `object` | Optional |

#### ios {#ios-2}

Plugin configurations specific to iOS. If a configuration with the same name exists globally (i.e. at the root of `configurations` object), the value from `ios` takes precedence.

`ios`

* Optional  
* Type: `object`

**Properties**

| Property | Type | Required |
| :---- | :---- | :---- |
| Additional properties | `object` | Optional |


### permissions 

Declares which Android permissions or iOS usage descriptions the plugin defines.

| ❗️ Permissions/usage description values set at the application level take precedence over the values defined on Libraries Extensibility Configuration. |
| :---- |

**Example**

```json
{
  "pluginConfigurations": {
    "permissions": {
      "ios": {
        "NSCameraUsageDescription": {
          "description": "This app wants to help you take a selfie."
        }
      },
      "android": ["android.permissions.CAMERA"]
    }
  }
}
```

`permissions`

* Optional  
* Type: `object`

| Property | Type | Required |
| :---- | :---- | :---- |
| [android](#android) | `array` of `string` | Optional |
| [ios](#ios) | `object` | Optional |

#### android {#android}

List of android permissions required by the plugin.

`android`

* Optional  
* Type: `array` of `string`

#### ios {#ios}

In iOS, to be able to access protected resources such as location information, bluetooth interface, or user's photos, the system asks for permissions on behalf of the application. Developers are expected to provide “usage descriptions” that are presented to the end users when prompting for permission to access the associated protected resources.

OutSystems Libraries can declare, via Extensibility Configuration, which protected resources the plugin might attempt to access, as such, the associated usage description keys can be declared, making it explicit that the plugin requires access to the associated protected resources. Additionally, the library might define a default value for the description that is expected to be used if, at the application level, no value has been provided for the usage description key.

Example

```json
{
  "version": "1",
  "plugin": {
    "capacitor": { ... },
    "permissions": {
      "ios": {
        "NSCameraUsageDescription": {},
        "NSCalendarsFullAccessUsageDescription": {
          "description": "Your time matters, let me manage it for you!"
        }
      },
      "android": ["android.permissions.CAMERA"]
    }
  }
}
```

In the above example, both usage description keys `NSCameraUsageDescription` and `NSCalendarsFullAccessUsageDescription` are declared as required by the plugin, however, only `NSCalendarsFullAccessUsageDescription` contains a default usage description message. When this plugin is in use in an application, if neither the application nor any other plugin in use by the application provides a value for `NSCameraUsageDescription`, the build fails because of a missing requirement.

`ios`

* Optional  
* Type: `object`

**Properties**

| Property | Type | Required |
| :---- | :---- | :---- |
| [Additional properties](#ios-additional-properties) | `object` | Optional |

#### ios additional properties 

Any property name is valid as long as the value follows the following schema

* Optional  
* Type: `object`

**Properties:**

| Property | Type | Required |
| :---- | :---- | :---- |
| description | `string` | Optional |

## buildConfigurations 

`buildConfigurations`

* Optional  
* Type: `object`

### properties {#properties-1}

| Property | Type | Required |  |
| :---- | :---- | :---- | :---- |
| [cordova](#cordova-1) | `object` | Required if `capacitor` is missing |  |
| [capacitor](#capacitor-1) | `object` | Required if `cordova` is missing |  |
| [resources](#resources) | `array of object` | Optional |  |
| [buildAction](#buildaction) | `object` | Optional | false |

Set of build time configurations allowing to configure the plugin sources and build time resources.

**Example**

```json
{
  "buildConfigurations": {
    "resources": {},
    "capacitor": {
      "source": {
        "npm": "<npm_package_name_specifier>"
      }
    },
    "cordova": {
      "source": {
        "npm": "<npm_package_name_specifier>",
        "variables": {
          "a": "b"
        }
      }
    }
  }
}
```

### cordova {#cordova-1}

An object with the required specification for a given Cordova plugin.

**Example**

```json
{
  "buildConfigurations": {
    "cordova": {
      "source": {
        "npm": "<npm_package_name_specificer>",
        "variables": {
          "stringVar": "varValue",
        }
      }
    }
  }
}
```

`cordova`

* Optional  
* Type: `object`

**Properties**

| Property | Type | Required |
| :---- | :---- | :---- |
| [source](#source) | `string` | Required |


#### source 

The source of the Cordova plugin, from where it is fetched for installation and, if needed, the Cordova plugin variables.

`source`

* Required  
* Type: `object`

**Properties**

| Property | Type | Required |
| :---- | :---- | :---- |
| [npm](#npm) | `string` | Required |
| [variables](#variables) | `object` | Optional |


#### npm 

A valid npm [package spec](https://docs.npmjs.com/cli/v10/using-npm/package-spec) from where to fetch the plugin.

`npm`

* Required  
* Type: `string`

#### variables 

An object with the plugin variables required for installation. Object key maps to variable name and associated value maps to variable value.

**Example**

```json
{
  "buildConfigurations": {
    "cordova": {
      "source": {
        "npm": "<npm_package_name_specificer>",
        "variables": {
          "stringVar": "varValue",
          "integerVar": 1,
          "numberVar": 8.9,
          "boolVar": true,
          "placeholderVar": "$settings.SomeSetting"
        }
      }
    }
  }
}
```

`variables`

Variable values can be a static value or a reference to a Setting.

* Optional  
* Type: `object`

**Properties**

| Property | Type | Required |
| :---- | :---- | :---- |
| Additional properties | `string` or `boolean` or `number` or `integer` | Optional |

### capacitor {#capacitor-1}

An object with the required specification for a given Capacitor plugin.

**Example**

```json
{
  "buildConfigurations": {
    "capacitor": {
      "source": {
        "npm": "<npm_package_name_specificer>"
      }
    }
  }
}
```

`capacitor`

* Optional  
* Type: `object`

Properties:

| Property | Type | Required |
| :---- | :---- | :---- |
| [source](#source-1) | `object` | Required |

#### source {#source-1}

The source of the capacitor plugin

`source`

* Required  
* Type: `object`

Properties:

| Property | Type | Required |
| :---- | :---- | :---- |
| [npm](#npm-1) | `string` | Required |

#### npm {#npm-1}

A valid npm [package spec](https://docs.npmjs.com/cli/v10/using-npm/package-spec) from where to fetch the plugin.

`npm`

* Required  
* Type: `string`

### resources 

Set of resources that can be copied from a specific source to a target location within the generated mobile project

**Example**

```json
{
  "buildConfigurations": {
    "resources": {
      "ios": [
        {
          "source": "$settings.GoogleServiceInfoPlist",
          "target": "GoogleService-Info.plist"
        }
      ],
      "android": [
        {
          "source": "$settings.GoogleServicesJsonBinary",
          "target": "android/app/src/main/res/google-services.json"
        }
      ]
    }
  }
}
```

`resources`

* Optional  
* Type: `object`

| Property | Type | Required |
| :---- | :---- | :---- |
| [android](#resource-item) | `array` of `object` | Optional |
| [ios](#resource-item) | `array` of `object` | Optional |

#### android {#android-1}

A list of resources to be added to the generated Android project.

`android`

* Optional  
* Type: `array` of [resource](#resource-item) items

#### ios {#ios-1}

A list of resources to be added to the generated iOS project.

`ios`

* Optional  
* Type: `array` of [resource](#resource-item) items

#### resource item {#resource-item}

**Properties**

| Property | Type | Required |
| :---- | :---- | :---- |
| source | `string` | Required |
| target | `string` | Required |

`source`

The source for the resource. One of:

* `string` representing a file path relative to the root folder of the generated project  
* Reference to a Setting that holds a `string` value representing a path relative to the root folder of the generated project. E.g. `$settings.SomeTextSetting`  
* Reference to a Binary Setting  
* Reference to an OutSystems application image via `$images`

`Target`

| ❗️For Android, the target location is relative to the android project located under `android/` For iOS, the target location is relative to the App folder inside `ios/App/App/` |
| :---- |

| Note that `resources` copying occurs before `cap sync` is executed. If a target location is affected by the result of `cap sync`, the resources might be missing |
| :---- |

The target location for the resource in the form of a file path

### buildAction

Build actions enable developers to customize their mobile projects. It is available for MABS 12 and uses YAML files to define which customization is to be done on the mobile project. The YAML definition for each build action can be found [here](https://docs.google.com/document/d/1wK1j6RBTUnq1d6OyUbPiNMkxM7c9gXwDfwpMwWxHzqg/edit?tab=t.0). 

To run multiple changes, you need to add all to the YAML file, and MABS will run each action following the order of the YAML file, top to bottom.

If you have build configurations defined at the plugin and app level, the plugin runs first.

| Property | Type | Required |
| :---- | :---- | :---- |
| config | `Object` | Required |
| parameters | `object` | Optional | 

**Example**

```json
{
  "buildConfigurations": {
    "buildAction": {
        "config": "$resources.buildAction.yaml",
        "parameters": {
"parameter1" : "parameterValue1",
"parameter2" : "parameterValue2"
}
    }
  }
}
```
#### config 

Reference to the resource uploaded on IDE, under resources. The file must have *Deploy Action* as *Deploy to Target Directory.*

| ❗️settings not supported |
| :---- |

* Required  
* Type: `object`

#### parameters

The parameters to pass values to the variables defined on the yaml. 

* Optional  
* Type: `object`

<div class="info" markdown="1">

Extensibility configurations may be processed by OutSystems for the purposes of service improvement and troubleshooting. These configurations should not include or permit access by OutSystems to personal data or confidential or sensitive information. Customers are responsible for ensuring that no personal data or confidential or sensitive information is accessible to OutSystems through any Extensibility configurations. Where such information is included in those configurations, customers should use secret settings to prevent personal data or confidential or sensitive information from being collected by OutSystems.

</div>