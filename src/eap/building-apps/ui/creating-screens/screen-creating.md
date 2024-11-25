---
summary: Learn how to create and manage app screens using various methods in OutSystems Developer Cloud (ODC), ensuring consistency and efficiency in design.
tags: ui design, screen templates, scaffolding, ui flows
locale: en-us
guid: 4afcc536-cf53-4130-9d7a-15887083d629
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - odc studio
content-type:
  - conceptual
---

# Creating screens

This article describes the process you follow to create a screen. When you build an app, you want all your screens to have the same look and feel. When users are familiar with the screen design, they work more efficiently.

You can create a screen using any of the following methods:

* From a screen template based on a use case
* From an empty screen template that comes with a basic layout
* Using scaffolding (accelerators) to add an entity to a screen

<iframe src="https://player.vimeo.com/video/1022161042" width="750" height="422" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Demo demonstrating how to create a screen.</iframe>

When a screen is open in the main window (menu block), you can:

* Modify the elements by adding new elements or removing some elements
* Modify styles to match your corporate styles
* Change the layout by moving elements to different locations on the screen
* Edit the data sources the screen uses to show and edit data

A UI flow is a way to logically group screens. You can build a screen from the default MainFlow and add it to a specific flow. Or, you can select the flow and then create the screen.

You can use existing screen templates to create your screens. Screen templates have predefined layouts, widgets, components, styles, and logic. Some OutSystems screen templates also come with sample data. Using a screen template improves reuse and supports consistency.

Scaffolding is an accelerator that creates two screens when you drag an entity onto a UI flow. One screen is an overview, and the other is a detailed screen to edit entity records. Both screens have some built-in functionality like pagination and sorting.

When you create a new app, the app includes some default UI flows in ODC (OutSystems Developer Cloud) Studio > **Interface** > **UI flows**:

* **Common** - contains UI and logic the app reuses in screens and blocks. For example, menus, information about the signed-in user, and the sign-in logic.
* **Layouts** - contain blocks that define the design of the screens.
* **MainFlow** - is the default UI flow where you can start adding screens in your app. This UI flow is empty in a new app.

<div class="info" markdown="1">

If you don't see **MainFlow**, a different flow may be the default.

</div>

Periodically during development, it's important to save your work. When you click 1-Click Publish, OutSystems saves and builds your app in the development stage. You can access your app from a web browser by clicking the screen and selecting **Open in Browser**. You can continue making changes in ODC Studio, publish your app, and then refresh the page to see your updates.
