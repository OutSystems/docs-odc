---
summary: Use watches to examine app elements while debugging threads in your app.
locale: en-us
guid: 244beb4f-2076-4bca-86f2-d166ca06e7a9
app_type: mobile apps, reactive web apps
---

# Watches

Watches allow you to examine app elements in ODC Studio while debugging your app. These elements are always displayed in the Watches Tab, regardless of being in or out of scope of the element being debugged. This behavior contrasts with the rest of the [scope tabs](<debugger-ui-reference.md#scope-tabs-area>), where the displayed content depends on the current scope.

Using watches you can inspect:

* Parameter values
* Variables
* Screen widgets


## Add a Watch

To watch an app element do the following:

1. Run the app in Debug mode.
1. Right-click the element to watch, either in the Scope tabs or in the app tree.
1. Select the "Add To Debug Watches" option in the pop-up menu. 

All watched app elements are alphabetically listed in the Watches Tab. 


## Remove a Watch

To remove a watch from an app element do the following:

1. Right-click on the watched element in the Watches Tab.
1. Select the option "Remove Watch" in the pop-up menu.


## Remove All Watches

To remove all watches do the following:

1. Right-click anywhere on the Watches Tab area.
1. Select the "Remove All Watches" option in the pop-up menu. 

Alternatively, select the "Remove All Watches" option available in the Debugger menu.

