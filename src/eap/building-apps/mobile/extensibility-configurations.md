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
---

# Advanced configurations for mobile app

Use Extensibility Configurations in the app properties to create a JSON with advanced configurations. Mobile Apps Build Service (MABS) in OutSystems Developer Cloud (ODC) uses the JSON as additional settings when creating your mobile package for iOS or Android. Extensibility Configurations lets you access options like defining a portrait or landscape orientation, splash screen, or a minimum mobile platform version.

You set the default values of Extensibility Configurations for Mobile Apps and Libraries in the ODC Studio. You can then change the values in the ODC Portal.

Here are some functionalities you can change with Extensibility Configurations:

* Add custom mobile plugins
* Change deep link behavior
* Configure the domains
* Customize the status bar 
* Modify the app icon
* Set up a splash screen

## Extensibility Configurations editor

In ODC Studio, open your mobile app, and under app properties go to **Advanced** > **Extensibility Configurations**. Double-click the field to open the editor.

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

The value is hard-coded and lock the screen to portrait.

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

1. Mark it as a secert and set its value with your secret, for example `"https://[TOKEN]@github.com/OutSystems/cordova-plugin-camera.git#v1"`

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
