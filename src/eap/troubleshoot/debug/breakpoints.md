---
summary: Breakpoints in ODC Studio allow for suspending execution of threads for debugging.
tags:
locale: en-us
guid: 2f4fd5a1-65ad-48ef-83b6-69bbfa851f53
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---
# Breakpoints

A **breakpoint** in ODC Studio marks an element where the execution of a [thread](threads.md) is going to be suspended for debugging. 

Breakpoints can be added to all of the following elements (except for Comment elements):

* Elements of an action flow

It's not possible to set a breakpoint in a given line inside a JavaScript element, only in the element itself.

The execution is also suspended on exceptions when the option "Break On All Exceptions" is set, even when no breakpoints are defined in the app. When an exception occurs, the execution will be stopped at the element that raised the exception. If an Exception Handler is defined, the execution will stop before the handler is executed.

While it is a common practice to add breakpoints before running an app, you may add or remove breakpoints anytime during a debug session.

Breakpoints are stored in your user settings. They will be available in ODC Studio, even between restarts, as long as you keep working in the same computer.


## Add or Remove a Breakpoint

To add or remove a breakpoint in an element:

1. Right-click on that element.
1. Select the "Add Breakpoint" or "Remove Breakpoint" option in the pop-up menu. 

Or:

1. Click on that element to select it and press `F8`. This shortcut toggles between add/remove breakpoint. 

The element where the breakpoint was set will show a small red circle.

You can remove all breakpoints at once by selecting the "Remove All Breakpoints" option in the Debugger menu or in the context menu displayed by right-clicking anywhere in the Breakpoints Tab area.


## Disable a Breakpoint

To temporarily disable a breakpoint without removing it, do the following:

1. Right-click on that element.
1. Select the "Disable Breakpoint" option in the pop-up menu. 

Or:

1. Click on that element to select it and press `Ctrl+F8`. This shortcut toggles between enable/disable breakpoint. 

The element where the breakpoint was disabled will show a hollowed red circle.

Follow the same procedure to re-enable a breakpoint, selecting the "Enable Breakpoint" option.

You can also disable all breakpoints at once by selecting the "Disable All Breakpoints" option in the Debugger menu or in the context menu displayed by right-clicking anywhere in the Breakpoints Tab area.
