---
summary: Learn to create and reuse UI blocks across apps with OutSystems Developer Cloud (ODC) for efficient development.
tags: ui development, component reusability
locale: en-us
guid: a62501dc-9ec8-41f6-add8-50b3e3934b8b
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A8810&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
---

# Create and Reuse Screen Blocks

You can reuse blocks within the same app or, if you want to reuse blocks across your apps, create public blocks in a library. With Blocks, you can have part of the UI in one place, so changes to the Blocks are automatically visible in all Screens that use it.

Here are notes about reusing Block across **different apps**:

* Blocks must be public.
* You can reuse Blocks in Web Apps and Mobile Apps. 

## Using Blocks

1. In a UI Flow inside a library, add a Block.
1. Implement the user interface and logic in the new Block.
1. Set the Block as public if you want to reuse it across apps.
1. Drag it the Block to the Screen where you want to use it. If you want to use the Block in another App, you first need to reference the Block.

## Example

Here is an example, with two sample apps, of how you can reuse a Block from library in a Mobile App.

**Create a public Block in a library:**

1. Create a new library.
1. In the library, go to **Interface** > **UI Flows** > right-click **Add UI Flow** > select **Add Block**. Name the Block **MyBlock**.
1. Set the **Public** property of Block to **Yes**.
1. Add some content to the Block. In our example we dragged a Text Widget and entered sample text "Hello from My Reactive App!".

    ![Screenshot of the source Web App with a public Block named MyBlock containing the text 'Hello from My Reactive App!'](images/block-reuse-source-app.png "Source App with Public Block")

1. Publish and release the library.

**Reuse the Block in MyPhoneApp:**

1. Create a new Mobile App.
1. Add a Screen to the app.
1. Open **Manage Dependencies** (CTRL+Q) and search producers for our library. Select the library.
1. In left pane navigate to **UI Flows** > **Main Flow** > select **MyBlock**. Click **Apply** to confirm and close.

    ![Dialog window showing the Manage Dependencies interface with MyBlock selected from the MyReactiveApp for reuse in a Mobile App](images/block-reuse-manage-dependencies.png "Block in Manage Dependencies Dialog")

1. In the Mobile App, navigate to **Interface** > **MyReactiveApp** (name of our example library) > **MainFlow2** > **MyBlock**.
1. Drag MyBlock to the Screen. You should see "Hello from My Reactive App!" in the preview.

    ![Preview of the Mobile App interface showing the reused MyBlock with the text 'Hello from My Reactive App!' on the screen](images/block-reuse-target-app.png "Source Block in Target App Preview")

1. Publish the app.

