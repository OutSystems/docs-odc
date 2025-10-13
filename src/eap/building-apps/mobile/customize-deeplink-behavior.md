---
summary: OutSystems Developer Cloud (ODC) allows customization of deeplink behavior in mobile apps using the `DeepLinksHandlerType` preference.
tags: mobile app development, cordova plugins, deep linking, extensibility configurations, application distribution
locale: en-us
guid: 7ead36ce-4ee4-48e7-b8f8-3575d373f17b
app_type: mobile apps
platform-version: odc
figma:
audience:
  - mobile developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
---

# Customize Deeplink Behavior

Prior to MABS 9, all deeplinks handled by a mobile app caused a reload of the page. In MABS 9 this behavior was changed, and deeplinks triggered a screen navigation.

## Customizing the behavior

You can customize the deeplink behavior using the `DeepLinksHandlerType` preference in the [extensibility configurations](extensibility-configurations-json-schema.md). The preference can have 4 different values:

* `default`: performs a screen navigation to the URL _(the default behavior)_
* `event`: fires an event to the `OSDeepLinksHandlerChannel` _(does not navigate)_
* `function`: calls the `handleOpenURL` function _(does not navigate)_
* `legacy`: loads the URL in the webview directly, which performs a page reload _(the behavior from MABS 8 and earlier)_

Example using `function`:

```
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

## Distribution

To make this change available for the users, [publish and generate a new mobile application](<./creating-mobile-package.md>) and distribute it.
