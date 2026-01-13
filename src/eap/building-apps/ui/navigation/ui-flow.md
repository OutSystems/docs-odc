---
summary: OutSystems Developer Cloud (ODC) features UI Flows that organize Screens and Blocks within the Interface tab for app development.
tags: ui design, application development
locale: en-us
guid: f7e6d4a4-7d1e-4593-9975-b8e160df3780
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3101%3A10564&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - odc studio
coverage-type:
  - understand
  - apply
topic:
  - ui-elements-screen-blocks
---

# UI flows

<div class="info" markdown="1">

Applies to the OutSystems UI framework only.

</div>

The **UI Fflow** is an element that groups screens and blocks. All instances of a UI flow in an app are under the **UI Flows** in the **Interface** tab.

![Screenshot of default UI Flows in ODC Studio Interface tab](images/ui-flows-odcs.png "UI Flows in ODC Studio")

When you create a new app, the app already has some default UI flows in **Interface** > **UI Flows**:

* **Common**. Contains UI and logic the app reuses in screens and blocks. For example, menus, info about the signed-in user, the sign in logic.

* **Layouts**. Contains Blocks that define the layout of the screens.

* **MainFlow**. The default UI flow where you can start adding screens in your app. This UI flow is empty in a new app.

<div class="warning" markdown="1">

Be careful when editing the default content of **Common** and **Layouts** UI flows, as you may affect all screens in your app.

</div>

## Adding a new UI flow

To add a new UI flow, do the following in ODC Studio:

1. Go to the **Interface** tab and right-click on the **UI FLows** folder.

1. From the help menu, select **Add new UI Flow**.

    ![Help menu in ODC Studio showing the option to Add new UI Flow](images/ui-flow-add-new-odcs.png "Adding a New UI Flow")

## Creating UI flow without styles

Follow these steps in ODC Studio to create a UI flow without CSS styles:

1. Create your theme without styles.

1. [Add a new UI Flow](#adding-a-new-ui-flow) to your app.

1. Set the UI flow to use your theme without styles. See [Setting the Theme of UI Flow](#setting-the-theme-of-ui-flow) for instructions.

1. Optionally, add a screen under the UI flow and verify if has no styles.

    ![Example of a Screen with a blank Theme in ODC Studio](images/screen-blank-theme-odcs.png "UI Flow with Blank Theme")

## Setting the theme of UI flow

All elements you add to a UI flow use the default theme of the app. You can change the theme by editing the **Theme** property of the **UI Flow**. To change the theme of a UI flow, do the following in ODC Studio:

1. Go to the **Interface** tab.

1. Select the UI flow for which you want to change the theme.

    <div class="info" markdown="1">

    All apps with UI from the default app templates use **MainFlow** as the default UI flow for screens. This is a convention more than a requirement.

    </div>

1. In the UI flow properties, select a theme from the **Theme** list.

    ![UI Flow properties in ODC Studio with Theme list expanded](images/ui-flow-default-theme-odcs.png "Setting the Theme of a UI Flow")

1. Optionally, create a screen under the UI flow to verify the screen uses the UI flow's theme.

## Setting the default Screen

**Default Screen** is the index page in Web apps, or the home screen in Mobile apps. There can be only one Default Screen in the app, and it's marked with the house icon.

![UI Flows in ODC Studio highlighting the Default Screen with a house icon](images/ui-flows-home-screen-odcs.png "Default Screen in UI Flows")

To set a screen as default, do the following in ODC Studio:

1. Navigate to the Screen you want to set as default.
1. Right-click on the Screen and in the help menu select **Mark as Default Screen**.

## UI Flow editor

When you double-click on a UI flow, the UI flow editor opens. Use the editor to:

* See the relationship between Screens
* Drag elements from the tool box that UI Flow supports

Even though you can draw connectors in **UI Flow**, these connections are only visual. You must define the interaction between screens.

### Using toolbox

To create a screen or block, drag the element from the toolbox to the UI flow editor. The available elements on the toolbox depend on the type of app you're creating.

![Toolbox in UI Flow editor of ODC Studio with various elements to drag into the UI Flow](images/ui-flow-toolbox-odcs.png "UI Flow Toolbox")

### Scaffolding screens

Drag **Entities** to the UI flow editor to start the accelerators (scaffolding). For example, if you drag an entity to a UI flow editor, you automatically scaffold two screens with working logic, one for listing the items, one for editing them.

![UI Flow editor in ODC Studio showing the process of scaffolding Screens by dragging Entities](images/scaffolding-screens-odcs.png "Scaffolding Screens")
