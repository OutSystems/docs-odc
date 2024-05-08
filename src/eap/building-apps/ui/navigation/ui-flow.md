---
summary: OutSystems Developer Cloud (ODC) features UI Flows that organize Screens and Blocks within the Interface tab for app development.
tags:
locale: en-us
guid: f7e6d4a4-7d1e-4593-9975-b8e160df3780
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3101%3A10564&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---
# UI Flows

**UI Flow** is an element that groups Screens and Blocks. All instances of UI Flow in an app are under the **UI Flows** in the **Interface** tab.

![Screenshot of default UI Flows in ODC Studio Interface tab](images/ui-flows-odcs.png "UI Flows in ODC Studio")

When you create a new app, the app already has some default UI Flows in **Interface** > **UI Flows**:

* **Common**. Contains UI and logic the app reuses in Screens and Blocks. For example, menus, info about the signed-in user, the sign in logic. 
* **Layouts**. Contains Blocks that define the layout of the Screens.
* **MainFlow**. The default UI Flow where you can start adding Screens in your app. This UI Flow is empty in a new app. 

<div class="warning" markdown="1">

Be careful when editing the default content of **Common** and **Layouts** UI Flows, as you may affect all Screens in your app.

</div>

## Adding a new UI Flow

To add a new UI Flow, do the following in ODC Studio:

1. Go to the **Interface** tab and right-click on the **UI FLows** folder.
   
1. From the help menu, select **Add new UI Flow**.
    
    ![Help menu in ODC Studio showing the option to Add new UI Flow](images/ui-flow-add-new-odcs.png "Adding a New UI Flow")

## Creating UI Flow without styles

Follow these steps in ODC Studio to create a UI Flow without CSS styles:

1. Create your Theme without styles.

2. [Add a new UI Flow](#adding-a-new-ui-flow) to your app.

3. Set the UI Flow to use your Theme without styles. See [Setting the Theme of UI Flow](#setting-the-theme-of-ui-flow) for instructions.

4. Optionally, add a Screen under the UI Flow and verify if has no styles.

    ![Example of a Screen with a blank Theme in ODC Studio](images/screen-blank-theme-odcs.png "UI Flow with Blank Theme")

## Setting the Theme of UI Flow

All elements you add to a UI Flow use the default Theme of the app. You can change the Theme by editing the **Theme** property of the **UI Flow**. To change the Theme of a UI Flow, do the following in ODC Studio:

1. Go to the **Interface** tab.

2. Select the UI Flow for which you want to change the Theme.

    <div class="info" markdown="1">

    All apps with UI from the default app templates use **MainFlow** as the default UI Flow for Screens. This is a convention more than a requirement. 

    </div>

3. In the UI Flow properties, select a Theme from the **Theme** list.

    ![UI Flow properties in ODC Studio with Theme list expanded](images/ui-flow-default-theme-odcs.png "Setting the Theme of a UI Flow") 

4. Optionally, create a Screen under the UI Flow to verify the Screen uses the UI Flow's Theme. 

## Setting the default Screen

**Default Screen** is the index page in Web Apps, or the home screen in Mobile Apps. There can be only one Default Screen in the app, and it's marked with the house icon.

![UI Flows in ODC Studio highlighting the Default Screen with a house icon](images/ui-flows-home-screen-odcs.png "Default Screen in UI Flows")

To set a Screen as default, do the following in ODC Studio: 

1. Navigate to the Screen you want to set as default.
2. Right-click on the Screen and in the help menu select **Mark as Default Screen**.

## UI Flow editor

When you double-click on a UI Flow, the UI Flow editor opens. Use the editor to:

* See the relationship between Screens
* Drag elements from the tool box that UI Flow supports

Even though you can draw connectors in **UI Flow**, these connections are only visual — you must define the interaction between Screens.

### Using toolbox

To create a Screen or Block, drag the element from the toolbox to the UI Flow editor. The available elements on the toolbox depend on the type of app you're creating.

![Toolbox in UI Flow editor of ODC Studio with various elements to drag into the UI Flow](images/ui-flow-toolbox-odcs.png "UI Flow Toolbox")

### Scaffolding Screens

Drag **Entities** to the UI Flow editor to start the accelerators (scaffolding). For example, if you drag an Entity to a UI Flow editor, you automatically scaffold two Screens with working logic, one for listing the items, one for editing them.

![UI Flow editor in ODC Studio showing the process of scaffolding Screens by dragging Entities](images/scaffolding-screens-odcs.png "Scaffolding Screens")
