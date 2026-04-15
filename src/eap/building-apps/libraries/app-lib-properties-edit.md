---
summary: Learn how to configure app and library components in OutSystems Developer Cloud (ODC) using the Edit properties dialog in ODC Studio.
tags: ui configuration, cloud development
locale: en-us
guid: 5923266e-a350-4775-a6ea-8c6882b8755c
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=4751%3A743&mode=design&t=lk9vABF8xFbGr0cY-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
---

# Edit app, library, and mobile library properties

This article demonstrates how you can edit the app, library, and mobile library properties, that is, the metadata in ODC.
<iframe src="https://player.vimeo.com/video/1069574566" width="750" height="422" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">How to edit the app and library properties - Metadata</iframe>

Depending on what you want to edit, the **Edit app properties**, **Edit library properties**, and **Edit mobile library properties** dialog box allows you to configure your app, library, and mobile library properties in ODC Studio. Using different tabs, you can edit **Details**, **Properties**, **Messages** and, **Extensibility** properties.

<div class="info" markdown="1">

After setting the properties, no save action is necessary. These changes save automatically.

</div>

## Access app, library, and mobile library properties

To edit the properties, follow these steps:

1. Go to ODC Studio.
1. Depending on what you to edit, click the app, or library, or mobile library.
   The edit properties dialog box is displayed.

![Image showing how to access edit properties icon](images/edit-app-icon-odcs.png "Access edit app properties icon")

## Edit app properties

### Details

On the **Details** tab, you can modify the following:

* Icon
* Primary color
* Name
* Description

![Image showing details tab properties](images/details-tab-odcs.png "Details tab properties")

### Properties {edit-app}

On the **Properties** tab, you can modify the following:

Defaults

* Default Theme
* Default Screen
* Splash Screen
* Global Exception Handler
* Default Transition
* Server Request Timeout

Required Scripts

* Add Required Script

### Messages

On the **Messages** tab, you can modify the following:

Validation Messages

* Mandatory Input
* Invalid Integer
* Invalid Decimal
* Invalid Currency
* Invalid Date
* Invalid Time
* Invalid DateTime
* Invalid Text
* Invalid Phone
* Invalid Email

**Upgrade Messages**:

* Upgrade Complete
* Upgrade Failed
* Upgrade Failed on Resources
* Upgrade Failed on Data Model
* Upgrade Required
* Upgrade Required with Data Loss

## Edit library properties

### Details

Refer to [Edit app](#properties-edit-app) properties.

### Properties {library-properties}

On the **Properties** tab, you can modify the following:

Defaults

* Default Theme
* Global Exception Handler
* Default Transition
* Server Request Timeout

Required Scripts

* Add Required Script

### Messages {library-messages}

On the **Messages** tab, you can modify the following:

Validation Messages

* Mandatory Input
* Invalid Integer
* Invalid Decimal
* Invalid Currency
* Invalid Date
* Invalid Time
* Invalid DateTime
* Invalid Text
* Invalid Phone
* Invalid Email

To configure extensibility, you must use only mobile libraries.

## Edit mobile library properties

### Details

Refer to [Edit app](#properties-edit-app) properties.

### Properties

Refer to [Library properties](#properties-library-properties).

### Messages

Refer to [Library messages](#messages-library-messages).

### Extensibility

For detailed information about configuring extensibility, refer to [Configure extensibility configurations](../../building-apps/mobile/configuring-mobile-apps.md#configure-extensibility-configurations-configure-extensibility).
