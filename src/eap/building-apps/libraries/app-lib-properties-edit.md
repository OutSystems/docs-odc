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

# Edit app and library properties

This article demonstrates how you can edit the app and library properties (i.e. the  metadata) in ODC.
<iframe src="https://player.vimeo.com/video/1069574566" width="750" height="422" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">How to edit the app and library properties - Metadata</iframe>

The **Edit app properties** and **Edit library properties** dialog lets you configure your app and library components in ODC Studio. Using different tabs, you can edit **Details**, **Properties**, **Messages** and, **Extensibility** properties.

<div class="info" markdown="1">

After setting the properties, no save action is necessary. These changes save automatically.

</div>

## Access app and library properties

One way to access the dialog is to open your app and then click the **Edit app properties** or the **Edit library properties** icon.

![Image showing how to access edit properties icon](images/edit-app-icon-odcs.png "Access edit app properties icon")

## Edit app properties

### Details

On the **Details** tab, you can modify the following:

* Icon
* Primary color
* Name
* Description

![Image showing details tab properties](images/details-tab-odcs.png "Details tab properties")

### Properties

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

Refer to Edit app properties.

### Properties

On the **Properties** tab, you can modify the following:

Defaults

* Default Theme
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

### Extensibility

In the library dialog, the **Extensibility** tab includes the following:

* A JSON text editor that checks your syntax (1).
* A context pane with items you can reference by dragging or double-clicking (2).
* A details pane that lets you view the properties without closing the editor (3).

![Image showing extensibility tab](images/extensibility-tab-odcs.png "Extensibility in library dialog")
