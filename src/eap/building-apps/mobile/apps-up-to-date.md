---
summary: OutSystems Developer Cloud (ODC) facilitates seamless mobile app updates with automatic version detection and resource caching.
tags: mobile app deployment, app version management, resource caching
locale: en-us
guid: 1ca55d98-3586-4c1f-843d-227b1c858502
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
  - understand
---

# Keeping apps up to date for your users

<div class="info" markdown="1">

Applies only to mobile apps.

</div>

When you click the **1-Click Publish** button, the updates to the mobile app that you deploy to a production stage become available. The users can continue using the app as the app updates automatically. The mobile app detects the updates when the app connects to the server. Only mobile app packages generated from a stage receive the new developments and changes published in that same stage.

## Detecting a new app version

To be up to date with the version on the server, there are several instances when the app checks for a new version. These instances are:

* Opening of the app.
* Navigation between screens.
* Call to the server, for example, to execute a server action or a server aggregate.

When there's a new version on the server, the app updates itself and notifies the user with a feedback message.

## Seamless upgrades and attention-requiring upgrades

**Seamless upgrade.** After detecting that a new version is available, the app starts caching all the new resources in the background. Once the app caches the resources, the next navigation event triggers the update. This can be, for example, a screen transition. Once the app is fully updated and the destination screen loads, the app notifies the user about the update with a feedback message. If the update takes time, the app shows the splash screen before navigating to the destination screen. This is a seamless upgrade.

**Attention-requiring upgrade.** An attention-requiring upgrade may happen when the user is on a screen that's changed in the new app version. If the user does something in the app that requires interaction with the server, that interaction may fail due to the upgrade requirements. For example, tapping a button to save data calls a server action, but because that action now has a different signature, the action fails. The user then sees a message that a new app version is available and required to proceed. Clicking the message updates the app. After the update, the app loads the updated screen and shows the update confirmation message.

When there's a form widget on the screen, the message about the required update also informs the user that the information they entered in the Form will be lost, because the app needs to reload. The data saved in local storage and client variables remains unaffected.

## Situations when the update isn't possible in the device

There may be situations when the automatic update of the app isn't possible in the user device, even when there are no issues during the publishing step. Possible causes:

* Poor network connection to download the resources needed for the update.
* Local data model upgrade that the app can't update automatically.
  
In situations where the app can't update itself on the device of the user, the app rolls back to the most recent fully working version. There's also a message that the update wasn't possible and that the user should restart the app and then try updating the app again.

When the error happens while updating the local storage data model, possibly because the existing data is incompatible with the new data model, the message informs the user that they may need to reinstall the app if the problem persists. The reinstallation clears the current app data.

You can find the issue in the logs by looking for "Upgrade failed - rolling back to previous application version". The information in the log should help you discover the cause of the upgrade failure and implement a fix in a new version of the app.

## Situations when the user must install a new build { #required-new-build }

Some changes require installation of an updated app package on the user device. You need a new app build when you **change** one of the following:

* App name.
* App icon.
* Primary color of the app.
* External resource, including any configuration files of mobile plugins.
* Plugin or plugin configuration.
* Configurations for a mobile package.
* Extensibility Configurations property.

These changes may negatively affect the user experience in the outdated apps, but the issues are automatically fixed when the user upgrades to the latest app package. In the case of plugins, it's a good practice to include fallbacks in the apps to avoid crashing until the latest app version is on the device. 

When installing a new version of an Android app using the build type **Debug**, uninstall the previous version from the device before installing the new one. This guarantees the new features work correctly.
