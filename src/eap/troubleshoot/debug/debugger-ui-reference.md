---
summary: The Debugger Tab in ODC Studio allows you to track threads being debugged and examine app elements and runtime values.
tags:
locale: en-us
guid: 81645496-3038-4765-9092-e2ab5a7f413b
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/8RLmb1pp1PYm5xqtrnq5O8/Debugging-apps?type=design&node-id=2901%3A73&t=sdGPdlxTkpCARchu-1
platform-version: odc
---
# Debugger reference

The Debugger Tab is in the lower pane of ODC Studio and allows you to track all threads being debugged and examine app elements and runtime values. This tab is automatically shown when the debugger is active and the execution flow hits a breakpoint.

![Overview of the Debugger User Interface in ODC Studio](images/debugger-ui-overview.png "Debugger UI Overview")

The Debugger Tab contains three main areas:

* The [Debugger Toolbar](#debugger-toolbar) **(1)**
* The [debugging context area](#debugging-context-area) **(2)**
* The [scope tabs area](#scope-tabs-area) **(3)**


## Debugger Toolbar { #debugger-toolbar }

It's located in the top right section of the Debugger Tab and provides you with a set of debugging commands to trace the execution of the thread being debugged. The toolbar buttons (except for the Break on All Exceptions button) are only available during a debug session.

The available buttons in the toolbar are the following:

![Image of the Debugger Toolbar with various debugging commands in ODC Studio](images/debugger-toolbar.png "Debugger Toolbar")

The table shows more information about each command.

Icon | Name | Shortcut | Description
:---:|------|:--------:|------------
![Icon of the Stop Debugging button in the Debugger Toolbar](images/toolbar-button-stop.png "Stop Debugging Button")     | Stop Debugging | | Stops the debugger and resumes the execution of all of the suspended threads.
![Icon of the Suspend Running Server Threads button in the Debugger Toolbar](images/toolbar-button-suspend.png "Suspend Running Server Threads Button")  | Suspend Running Server Threads | | Suspends the execution of all current server threads in OutSystems Developer Cloud (ODC).
![Icon of the Abort Running Server Threads button in the Debugger Toolbar](images/toolbar-abort-button.png "Abort Running Server Threads Button")    | Abort Running Server Threads | | Aborts the execution of the current server threads in ODC.
![Icon of the Continue button with the F9 shortcut in the Debugger Toolbar](images/toolbar-button-continue.png "Continue Button") | Continue | `F9` | Resumes the execution.
![Icon of the Step Over button with the F10 shortcut in the Debugger Toolbar](images/toolbar-button-step-over.png "Step Over Button")| Step Over | `F10` | Steps the execution trace to the next element in the same flow or, when in a web application, screen "level".
![Icon of the Step Into button with the F11 shortcut in the Debugger Toolbar](images/toolbar-button-step-into.png "Step Into Button")| Step Into | `F11` | Steps the execution trace to the first element "inside" elements like: <br/> &#8212; Execute Client Action (or Execute Server Action) elements which execute user-defined actions of the same app<br/> &#8212; User functions of the same app<br/> &#8212; Assignments of Assign elements<br/> Trying to step into any other element is the same as doing a ![Icon of the Step Over button with the F10 shortcut in the Debugger Toolbar](images/toolbar-button-step-over.png "Step Over Button") Step Over operation.
![Icon of the Step Out button with the Shift+F11 shortcut in the Debugger Toolbar](images/toolbar-button-step-out.png "Step Out Button") | Step Out | `Shift+F11` | Continues the execution trace to the next element in the outer "level" of the flow or screen, i.e. it "gets out" of the current flow or screen.
![Toggle icon of the Break On All Exceptions button in the Debugger Toolbar](images/toolbar-button-break-on-all-exceptions.png "Break On All Exceptions Button") | Break On All Exceptions | | When active, this toggle button forces the debugger to suspend the execution of threads whenever handled or unhandled exceptions occur.

## Debugging Context Area { #debugging-context-area }

Located on the left-hand side of the Debugger Tab, this area contains several tabs containing information about the debugger execution. 

You can double-click on elements listed in these tabs to show them on the canvas. However, if the app element being debugged does not belong to your app (e.g. an app reference, an action in a producer app, etc.), it cannot be visualized on the canvas, and will only be displayed in the Threads Tab with its name followed by its app name between brackets.

Threads Tab
:   This tab shows the current debugging context. It lists all the threads being debugged and their debugging context: app element (if applicable), event, UI flow, screen or block, and client/server action(s) that make up the call stack. The action executed last is listed at the bottom of each thread entry.

Breakpoints Tab
:   Lists all breakpoints defined in the app.

Users Tab
:   Lists all the other users that are also debugging server threads in your app. You may expand each user to see the list of threads being debugged by them.

### Unpublished Changes

If there are any unpublished changes to the app you're currently debugging, the modified app elements will have the following visual cues in the Threads Tab:

* ![Overlay icon indicating a missing element in the Threads Tab during debugging](images/overlay-missing-element.png "Missing Element Overlay") **Missing element**: the element is no longer present in the app but it still exists in the published version of the app. The missing element will still be debugged, but it will not have visual feedback on the canvas.

* ![Overlay icon indicating a modified element in the Threads Tab during debugging](images/overlay-modified-element.png "Modified Element Overlay") **Modified element**: the element is different from the one that was published. The element that is going to be debugged is the published one, not the modified one.

### Switching to Another Thread

The thread being debugged, i.e. the active thread, is identified by a ![Blue arrow icon indicating the active thread in the Threads Tab during debugging](images/overlay-active-request.png "Active Thread Indicator") blue arrow in this tab, as well as the app element being debugged on canvas. Every other thread that may also be suspended (but inactive, as they're not being debugged) is marked with a ![Grey arrow icon indicating an inactive thread in the Threads Tab during debugging](images/overlay-inactive-request.png "Inactive Thread Indicator") grey arrow, as well as their app element on the canvas (if visible).  

To switch to another thread, double-click on the thread you want to debug in the Threads Tab; ODC Studio updates the contents of the Debugger Tab with the debug information for that thread.

Learn more about threads in the [Threads](threads.md) topic.

## Scope Tabs Area { #scope-tabs-area }

Located on the right-hand side of the Debugger Tab, this area contains several **scope tabs** displaying app elements and runtime values for you to examine while the execution is suspended during a debug session.

All elements shown in scope tabs are listed in alphabetical order in the tabs. Some elements can be expanded to examine inner elements value, e.g., the `Name` in a `Customer` Record. Values presented in <span style="color: red;">red</span> are the ones that have changed since the last debug step. 

If a value of an element is too long to be displayed in the tab or if the value is of List data type, you can double-click on the element to open a window displaying its value.

Debug Setup Tab
:   Allows to set the entry point, the target for debugging (in mobile apps only) and start a new debug session. This tab is only visible when the debugger is not running. 

    Use the "Entry app:" combo box to select the entry point where the user interaction begins. This is useful when debugging producer apps.
    
    In **mobile apps** you must choose the target where you want to debug your app: emulate using Google Chrome browser on your PC or debug in an iOS/Android device connected to your PC. If you choose the Google Chrome browser target, ODC Studio will open a special Google Chrome instance where the user must perform user interactions with the app.
    
In Use Tab
:   Lists all elements from the scope tree relevant for immediate examination regarding the app element currently being debugged.

Locals Tab
:   Lists all elements in the local scope of the app element being debugged.

Widgets Tab
:   Lists all widgets in scope of the app element currently being debugged.

Client Tab
:   Only available for Mobile and Reactive web applications. Lists all client variables of the app.

Settings
:   Lists all settings properties of the app.

Watches Tab
:   Lists all variables explicitly marked as watched.

