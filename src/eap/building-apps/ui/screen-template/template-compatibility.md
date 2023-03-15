---
summary: You need a Screen Template compatible with your Theme to display the final page properly.
tags:
locale: en-us
guid: 9d153217-df3d-488c-ad5c-22cdc196942d
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Theme compatibility in Screen Templates

<a id="helpid-30171"></a>

When working with Screen Templates you may see the following warning message: **The Themes are not compatible. The final Screen may look different than the preview. To use this Screen Template, you need an app with a Theme based on (app name)\(theme name).** This means that your app and Screen Template are not compatible, which may cause the final page not to display correctly.

* Select a compatible Screen Template. The Screen Templates that come with ODC Studio are compatible with the built-in Application Templates.
* [Create your Screen Templates](<../creating-screens/create-screen-scratch.md>) and use your (custom) Theme as the base.

If the Screen Template was compatible with your app, but now it's not:
 
* Revert the changes you did to the app Theme. 
* Check if you set the correct Theme in the **Default Theme** property field of your app or UI Flow.

![Theme Compatibility warning](images/template-layout-theme-mismatch-odcs.png)
