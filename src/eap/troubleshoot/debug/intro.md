---
summary: Learn how to find and troubleshoot errors in your apps by using the debugger.
tags: 
locale: en-us
guid: bd64bfb4-afcf-4eb8-b87a-1923fd19524c
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Debugging apps

Debug your app in ODC Studio by pausing at [breakpoints](<breakpoints.md>), specific points in an app, and then running the logic step-by-step. This lets you find any issues in your logic design.

The [Debugger tab](<debugger-ui-reference.md>) shows variables and runtime values. It also shows the current debugging context: [thread](<threads.md>) event name, UI flow, screen and action, when applicable. Use the debugger commands available in the Debugger Toolbar and in the Debugger menu.

When debugging an action in your library, ensure that the app is using the most recent version, as there may be multiple versions of the library; otherwise, a warning occurs. Stepping into a Service Action from a consumer app isn't supported.

![The Debugger window](images/debugger-intro-ss.png?width=800)

## How to debug your app

To debug your app, do the following in ODC Studio:

1. Click the 1-Click Publish button to save the latest changes in the app before debugging. 

1. Set one or more [breakpoints](<breakpoints.md>) in the app you're debugging.

1. If you're debugging a **mobile app distributed as a PWA**, select **Emulate using Google Chrome** in **Debugger** > **Debug Setup**. 

1. Start debugger by clicking the **Start Debugging** button in the [Debugger tab](<debugger-ui-reference.md>). When you're debugging mobile apps using the Google Chrome target, ODC Studio opens a dedicated Chrome browser instance for debugging only.

1. Do some tasks in the app, up to a point when the execution runs into a breakpoint and suspends.

1. When you switch to the ODC Studio window, the flow containing the element with the breakpoint shows on the canvas. ODC Studio selects the element with the breakpoint and marks is with the ![debug icon](images/overlay-active-request.png) debug icon.

1. The execution context shows in the **Threads** tab of the **Debugger** tab, marked with the ![current thread](images/overlay-active-request.png) current thread icon, showing the current execution stack of the app elements. The **Debugger** tab also shows additional information you can explore.

1. After analyzing the runtime values at that execution point, you can continue running the app by:

    * Selecting one of the commands available for advancing the execution of the application logic: ![continue icon](images/toolbar-button-continue.png) **Continue**, ![step over icon](images/toolbar-button-step-over.png) **Step Over**, ![step into button](images/toolbar-button-step-into.png) **Step Into** or ![step out button](images/toolbar-button-step-out.png) **Step Out**. The execution point advances according to the command you run.

    * Right-clicking an element on the canvas (or in the app tree) and selecting the **Continue To Here** option in the context menu. The execution continues until it reaches that element on the canvas.

## Working with dates and times

When debugging an app and checking the values of the Date Time data type, keep in mind the following:

* During debugging, ODC Studio shows UTC date and time in the debugger.
* In the client UI, the date and time are in the timezone of the client.
* On the server, the date and time are in the timezone of the server.
