---
guid: f87890c8-0e38-443b-85be-38be20882571
locale: en-us
summary: This article describes some of the common use cases with JSON snippets for Cordova-based extensibility configuration JSON schema.
figma: 
coverage-type:
  - apply
  - understand
topic: 
app_type: mobile apps
platform-version: odc
audience:
  - mobile developers
  - tech leads
tags: Mobile,mobile app extensibility,extensibility configuration
outsystems-tools:
  - odc studio
helpids: 
---

# Cordova-based extensibility configurations use cases

<div class="info" markdown="1">

Applies only to Cordova-based apps.

</div>

Extensibility configurations allows you to customize and enhance mobile app functionality beyond the default settings available in the **Mobile** tab. By leveraging JSON-based configurations, you can define runtime behaviors, modify build-time settings, and integrate advanced features tailored to specific app requirements.

For detailed information about configuring and managing mobile and extensibility settings, refer to [Configuring mobile apps](configuring-mobile-apps.md).

With extensibility configurations, you can:

* Customize app properties such as orientation, splash screens, and status bars.
* Integrate and configure mobile plugins for extended functionality.
* Define permissions and deep link behaviors.
  
## Sample use cases

Here are some use cases of the JSON and how you can change behavior of your mobile app.

### Lock the screen orientation

The value is hard-coded and locks the screen to portrait.

    {
    (...)
        "preferences": {
            "global": [{
                "name": "orientation",
                "value": "portrait"
            }]
        }
    (...)
    }

### Define a custom variable

You can define a variable in  **Data** > **Settings** and reference it.

    {
    (...)
        "preferences": {
            "global": [{
                "name": "MySampleSetting",
                "value": $extensibilitySettings.MobileAppSetting1
            }]
        }
    (...)
    }

### Define a private git repository for a custom mobile plugin

You can use secrets to add private data to the JSON of a plugin or app.

For example, you may need to point to a private git repository accessed by a token. To do this:

1. Define, `MyRepoXWithToken`, for example, as the setting for the `url` of the plugin:
   

        {
        (...)
            "plugin": {
                "url": $extensibilitySettings.MyRepoXWithToken
            }
        (...)
        }

2. Mark it as a secret and set its value with your secret, for example `"https://[TOKEN]@github.com/OutSystems/cordova-plugin-camera.git#v1"`

You could also use a secret to use an API key on a preference on a plugin, for example.

### Reference an image

You can also reference images in the JSON file.
    
    {
    (...)
        "icons": {
            "android": [{
                "resource": $images.Logo,
                "density": "ldpi"
            }]
        }
    (...)
    }


### Customize deeplink behavior

You can customize the deeplink behavior using the `deeplinksHandler` under `appConfigurations` in the [App extensibility configuration JSON schema](extensibility-configurations/extensibility-app-reference.md). The preference can have  different values:

* `default`: performs a screen navigation to the URL the default behavior.
  
* `event`: fires an event to the `OSDeepLinksHandlerChannel` and does not navigate.
  
* `function`: calls the `handleOpenURL` function and does not navigate.

* `legacy`: loads the URL in the webview directly, which performs a page reload (the behavior from MABS 8 and earlier)

Example using `function`:

```json
{
    "preferences": {
        "global": [
            {
                "name": "DeepLinksHandlerType",
                "value": "function"
            }
        ]
    }
}
```

In order to use the `event` and `function` options, the specific handler must be defined in a script loaded by the app module.

Example for `event`:

```
var channel = cordova.require("cordova/channel");
if (channel) {
    channel.OSDeepLinksHandlerChannel.subscribe(function (url) {
        ...
    });
}
```

Example for `function`:
```
window.handleOpenURL = function (url) {
    ...
}
```
To make this change available for the users, [publish and generate a new mobile application](creating-mobile-package.md) and distribute it.

## Related resources

* [Extensibility configuration JSON schema](extensibility-configurations-json-schema.md)
  
* [Cordova-based extensibility configuration JSON schema](legacy-extensibility-configuration.md)


