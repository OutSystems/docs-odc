---
summary: Utilize Extensibility Configurations in OutSystems Developer Cloud (ODC) for advanced mobile app customization.
tags: extensibility configurations, json configuration, mobile build service, mobile apps customization
locale: en-us
guid: 941e56cf-aacf-43bf-9d1c-f131565036e6
app_type: mobile apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3101%3A2600&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - apply
  - remember
topic:
  - customize-mobile-apps
---

# Advanced configurations for mobile app

ODC provides ways to configure your mobile app's native shell. Most preferences can be configured using the extensibility, which receives [the configuration JSON](extensibility-configurations-json-schema.md). Some of these preferences you can found in the **Mobile** tab to change the most used preferences in the UI.

For control and configuring options not exposed in the **Mobile** tab, you can edit the Extensibility Configurations. This page details how to modify the JSON structure to achieve these customizations.

Some of the functionalities you can change with Extensibility Configurations include:

* Defining portrait or landscape orientation
* Setting up a splash screen
* Defining a minimum mobile platform version
* Adding mobile plugins
* Changing deep link behavior
* Configuring domains
* Customizing the status bar
* Modifying the app icon

## Managing configurations across stages

Define default Extensibility Configurations in ODC Studio. You can then override these defaults in the ODC Portal for deployment stages (for example, development or production) to apply environment settings. Portal configurations take precedence over Studio defaults during deployment to that stage.

## Extensibility Configurations editor

In ODC Studio, open your mobile app, and under **Edit app properties** go to **Extensibility**. Double-click the field to open the editor.

![Screenshot of the Extensibility Configurations editor in OutSystems Developer Cloud Studio with areas A, B, and C highlighted](images/extensibility-configurations-editor-odcs.png "Extensibility Configurations Editor in ODC Studio")

The editor consists of the following:

* JSON text editor that checks your syntax **(A)**.
* Context pane with items you can reference by dragging or double-clicking **(B)**.
* Details pane that lets you view the properties without closing the editor **(C)**.

## Referencing the values in the ODC Studio

In ODC Studio, go to **Data** > **Settings** and create the values you need in your app. Then, in the Extensibility Configurations editor, reference the value from the scope pane. You can also reference images you add to your app. 

## Changing the settings in the ODC Portal

Once you publish your app, go to **ODC Portal** > **(your app)** > **Configuration** > **Settings**. Select the setting you want to edit, change the value, and apply the change.

<div class="info" markdown="1">

Changing the values of Setting in ODC Portal doesn't trigger automatic generation of a new mobile package. See [Create mobile app package](creating-mobile-package.md) for more information on how to create a package for iOS or Android. 

</div>

## Sample use cases

Here are some use cases of the JSON and how you can change behavior of your mobile app.

###  Lock the screen orientation

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
                "value": $settings.MobileAppSetting1
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
                "url": $settings.MyRepoXWithToken
            }
        (...)
        }

1. Mark it as a secret and set its value with your secret, for example `"https://[TOKEN]@github.com/OutSystems/cordova-plugin-camera.git#v1"`

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
