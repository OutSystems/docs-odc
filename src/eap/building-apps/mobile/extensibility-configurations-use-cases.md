---
guid: 83738400-1f27-4729-9e11-c630d38ea933
locale: en-us
summary: This article explains the different app and library use cases of extensibility configurations JSON schema.
figma: 
coverage-type:
  - apply
  - understand
topic: 
app_type: mobile apps
platform-version: odc
audience:
  - mobile developers
tags: Mobile,Extensibility
outsystems-tools:
  - odc studio
helpids: 
---
# Using universal extensibility configurations JSON schema

Extensibility configurations allows you to customize and enhance mobile app functionality beyond the default settings available in the **Mobile** tab. By leveraging JSON-based configurations, you can define runtime behaviors, modify build-time settings, and integrate advanced features tailored to specific app requirements.

For detailed information about configuring and managing mobile and extensibility settings, refer to [Configuring mobile apps](configuring-mobile-apps.md).

With extensibility configurations, you can:

* Customize app properties such as orientation, splash screens, and status bars.
* Integrate and configure mobile plugins for extended functionality.
* Define permissions and deep link behaviors.
* Apply advanced build actions using JSON files.

## App configuration use cases

The [App extensibility configuration reference](extensibility-configurations/extensibility-app-reference.md) describes a JSON schema for customizing mobile apps. It's broken down into two main sections:

`appConfigurations` for customizing runtime behaviors

`buildConfigurations` for modifying build-time settings.

Here are some of the use cases that can be customized with application extensibility configuration file:

### Set app orientation

Set the orientation of the app's user interface to `portrait`, `landscape`, or `all`.

```json
{
  "appConfigurations": {
    "orientation": "portrait"
  }
}
```

### Add resources to the build

Copy resources, such as configuration files, from a source to a target location within the generated mobile project.

```json
{
  "buildConfigurations": {
    "resources": {
      "ios": [
        {
          "source": "$extensibilitySettings.GoogleServiceInfoPlist",
          "target": "GoogleService-Info.plist"
        }
      ],
      "android": [
        {
          "source": "$extensibilitySettings.GoogleServicesJsonBinary",
          "target": "android/app/src/main/res/google-services.json"
        }
      ]
    }
  }
}
```

### Customize the splash screen image

Customize the splash screen to display a specific image, with different configurations for Android and iOS.

```json
{
  "buildConfigurations": {
    "splashscreens": {
      "android": {
        "logo": "$images.MyAppLogoFromAnotherDepartment"
      },
      "ios": {
        "logo": "appIcon"
      }
    }
  }
}
```

### Advance customization using build actions

Enables advanced customization of the native mobile project using JSON files. This is the modern replacement for Cordova hooks. The JSON file defines a series of actions to be performed on the project.

```json
{
  "buildConfigurations": {
    "buildAction": {
      "config": "$resources.buildAction.json",
      "parameters": {
        "parameter1": "parameterValue1",
        "parameter2": "parameterValue2"
      }
    }
  }
}
```

### Customize deeplink behavior

In Capacitor, the default behavior for deeplinks is to navigate to the specified URL. To customize this behavior, you must define the `window.handleOpenURL` function. When this function is defined, the function is executed with the deeplink URL as its argument, instead of performing the default navigation.

```
window.handleOpenURL = function (url) {
    // Your custom logic here
}
```

To apply this change for the users you must [publish and generate a new mobile application](creating-mobile-package.md) and distribute it.

## Plugin configuration use cases {plugin-use-cases}

The [Library extensibility configuration reference](extensibility-configurations/extensibility-lib-reference.md) describes a JSON schema for mobile libraries that wrap Cordova plugins, Capacitor plugins, or both.

`pluginConfigurations` for customizing plugin runtime behaviors

`buildConfigurations` for customizing plugin build-time settings

Here are some of the use cases that can be customized with library (plugin) extensibility configuration file:

### Specify cordova plugin source

Specify the source from which a Cordova plugin is fetched for installation. This is typically an npm package specifier.

```json
{
  "buildConfigurations": {
    "cordova": {
      "source": {
        "npm": "cordova-plugin-camera"
      }
    }
  }
}
```

### Specify both Capacitor and Cordova plugin sources

For dual-stack plugins, specify both Capacitor and Cordova plugin sources. The appropriate plugin is used based on the runtime selected for the mobile app.

```json
{
  "buildConfigurations": {
    "cordova": {
      "source": {
        "npm": "cordova-plugin-camera"
      }
    },
    "capacitor": {
      "source": {
        "npm": "@capacitor/camera"
      }
    }
  }
}
```

### Customize cordova plugin preferences

Set Cordova preferences for a plugin. Configuration values can be static or a reference to a Setting, and you can set them globally or override them per platform.

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
          "SomePreference": "SomeAndroidValue"
        }
      }
    }
  }
}
```

### Customize capacitor plugin configurations

Provide configuration values for a Capacitor plugin, which can be set globally or per platform. You can configure multiple plugins simultaneously.

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
            "resizeOnFullScreen": "true"
          }
        }
      }
    }
  }
}
```

### Declare plugin permissions

Declare Android permissions or iOS usage descriptions that the plugin requires. You can also provide a default description for an iOS usage description key.

```json
{
  "pluginConfigurations": {
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

### Define variables for plugin installation

Define variables required for installation within the buildConfigurations for a Cordova plugin. Variable values can be static or a reference to a Setting.

```json
{
  "buildConfigurations": {
    "cordova": {
      "source": {
        "npm": "<npm plugin identifier>",
        "variables": {
          "stringVar": "varValue",
          "integerVar": 1,
          "numberVar": 8.9,
          "boolvar": true,
          "placeholderVar": "$extensibilitySettings.SomeSetting"
        }
      }
    }
  }
}
```

### Add build-time resources

Copy resources from a specified source to a target location within the mobile project. The source can be a reference to a setting or an OutSystems application image.

```json
{
  "buildConfigurations": {
    "resources": {
      "ios": [
        {
          "source": "$extensibilitySettings.GoogleServiceInfoPlist",
          "target": "GoogleService-Info.plist"
        }
      ],
      "android": [
        {
          "source": "$extensibilitySettings.GoogleServicesJsonBinary",
          "target": "android/app/src/main/res/google-services.json"
        }
      ]
    }
  }
}
```

### Define build actions with a json file

Use build actions to customize mobile projects with a JSON file. Define a config that references the JSON file and pass parameters to it.

```json
{
  "buildConfigurations": {
    "buildAction": {
      "config": "$resources.buildAction.json",
      "parameters": {
        "parameter1": "parameterValue1",
        "parameter2": "parameterValue2"
      }
    }
  }
}
```

## Related resources

For more information about app and library extensibility configurations:

* [App extensibility configuration JSON schema](extensibility-configurations/extensibility-app-reference.md)

* [Library (plugin) extensibility configuration JSON schema](extensibility-configurations/extensibility-lib-reference.md)

* [Extensibility settings](configuring-mobile-apps.md#configure-extensibility-settings)
