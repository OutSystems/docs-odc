---
guid: b91101ba-b2f2-480f-aa7c-a60fc17948d1
locale: en-us
summary: Compare workflow versions in OutSystems Developer Cloud (ODC), using revision history and publish workflows to track changes, resolve conflicts, and maintain accuracy.
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=9929-10
coverage-type:
  - apply
topic:
app_type: reactive web apps
platform-version: odc
audience:
  - Developer
tags:
  - Workflows
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---
# Compare workflow versions

In a real-world application, you are most likely ending up with multiple versions of a workflow as you and your make changes and improvements over time. Having the capacity to compare different versions of a workflow is crucial for maintaining the integrity of your application and ensuring that you can track changes effectively.

ODC lets you compare different versions of a workflow side by side. Use this to identify changes, understand how your workflow evolved, and confirm you're working with the correct version. You can do this comparison in three ways:

* **In the revision history**. Here you can compare any previous revision with your current work or the latest published version.
* **When opening a workflow**. Whenever you have unpublished changes that aren't based on the latest published revision, you can compare both versions before choosing which one to continue with.
* **When publishing a workflow**. If another user published a newer revision since you started editing, you can compare your changes with the new revision before publishing.

## Compare in the revision history

As long as your workflow has more than one revision, you can compare a previous revision with your current working state directly from the revision history panel. To do this:

1. Open the workflow in the Workflow Editor.

1. Open the revision history panel, by clicking **Ctrl + H** or by clicking the Open revisions history, available in the top right corner of the editor, under **More options**.

1. Select a previous revision from the revisions list.

1. Depending on your current working state, you see one of the following options:

    * **Compare with autosaved.** Available when you have unpublished changes. Compares the selected revision with your current unsaved work.
    * **Compare with the latest.** Available when you have no unpublished changes. Compares the selected revision with the latest published revision.

    **Note:** The latest published revision doesn't show a compare option because there is nothing newer to compare it with.

    ![Workflow Editor showing the Revision history panel with a revision’s context menu open, highlighting the Compare with autosaved option.](images/compare-revision-history-pl.png "Revision history panel with compare option")

1. Click the **Compare with ...** option. The comparison view opens.

    ![Comparison view displaying two versions of a workflow side by side with change badges and Keep local work and Restore this revision buttons above each canvas.](images/compare-view-pl.png "Side-by-side workflow comparison view")

1. Review the differences between the two versions. See [Understanding the comparison view](#understanding-the-comparison-view).

1. Choose one of the available actions:

    * **Keep local work**. This closes the comparison view and returns you to editing your current version.
    * **Restore this revision**. This restores the selected revision, replacing your current working state.

## Compare revisions when opening a workflow

When you open a workflow with unpublished changes not based on the latest published revision, the editor shows a dialog. For example, a colleague published a new revision while you had unsaved work. The dialog asks you to choose which version to use. To do this:

1. Open the workflow from the ODC Portal. If that version as unpublished changes that aren't based on the latest published revision, the _Recover unpublished work?_ pops up. This pop up shows your autosaved version and the latest published revision.

1. Click Compare revisions to open the comparison view.

    ![Recover unpublished work dialog listing an unpublished workflow revision and the latest revision, with the Compare revisions button highlighted.](images/recover-unpublished-work-pl.png "Recover unpublished work dialog")

1. Review the differences between your autosaved version (left) and the latest published revision (right).

1. You must choose one of the following actions before you can continue, since you can't dismiss this dialog:
    * Click **Keep local work** above the left canvas to continue editing your autosaved version.
    * Click **Restore this revision** above the right canvas to open the latest published revision (this discards your unsaved changes).

    ![Side-by-side comparison view showing an autosaved workflow on the left and the latest published revision on the right, with Keep local work and Restore this revision buttons highlighted.](images/compare-revisions-unpublished-pl.png "Compare autosaved and latest revisions")

**Note:** This dialog only appears when both conditions are true: you have unpublished changes, and those changes build on an older revision (not the latest published one). If your unpublished changes already build on the latest published revision, the workflow opens normally.

## Compare revisions when publishing

When you try to publish a workflow and another user published a newer revision since you started editing, the publish dialog includes a Compare both versions option.
This lets you review the differences before deciding how to proceed. This happens when:

1. You click **Publish** in the Workflow Editor.

1. If a ODC detects a publish conflict, a pop up appears with the following options:

    * **Cancel**. Closes the dialog and returns you to editing your current version.
    * **Override with my version**. Publishes your current work, replacing the latest published revision.
    * **Compare both versions**. Opens the comparison view.

    ![Publish and replace latest revision dialog explaining that another revision was published and offering Cancel, Override with my version, and Compare both versions options.](images/compare-publish-pl.png "Publish conflict compare dialog")

1. If you clicked Compare both versions, review the differences between your version (left) and the latest published revision (right). See [Understanding the comparison view](#understanding-the-comparison-view).

1. Then choose one of the following actions:

    * **Publish your work**. Publishes your version and returns you to the editor.
    * **Restore revision**. Discards your changes and restores the latest published revision.

    ![Side-by-side comparison view used during publishing, showing the current workflow version on the left and the latest published revision on the right with Publish your work and Restore this revision buttons.](images/compare-revisions-publish-pl.png "Compare revisions before publishing")

**Note:** This option only appears when your working session builds on an older revision than the latest published one.

## Understanding the comparison view

The comparison view shows two workflow canvases side by side:

* Left canvas. Always shows the newer or current version (your autosaved work or latest published revision, depending on the entry point).
* Right canvas. The latest published in case you are comparing to your autosaved or your selected revision.

The left canvas displays the local version (unsaved data) and the reference revision, which can be the latest published revision or an older restored one.

While the right canvas header displays the revision label, publication date, and the name of the person who published it.

If workflow metadata (title, icon, or description) differs between versions, the header highlights those differences.

### Color coding

Color coding highlights changes on nodes, connectors, and property values:

|Color|Meaning|
|--|--|
|Green|Added|
|Red|In Conflict|
|Blue|Modified/Deleted|

![Workflow comparison view illustrating nodes and connectors highlighted in green, red, and blue to indicate added, conflicting, and modified or deleted elements.](images/revisions-color-coding-pl.png "Color coding of workflow changes")

### Inspecting property-level changes

If you click in any highlighted node and see detailed property-level differences:

* For **modified nodes**, the properties pane opens and it  highlights the changed properties.
* For **added nodes**, the properties pane opens only on the side where the node exists.
* For **deleted nodes**, the properties pane opens only on the side where the node still appears.

In the example below, the start node appears in blue because it changed between revisions. When you click the node, the properties panel opens and highlights the changed properties in green.

In this case, the modifications added a description and an Instance label, even though the node already existed in the previous revision.

![Comparison view where a Start node is highlighted as modified and its properties panel shows added description and instance label fields highlighted as changes.](images/changes-details-modified-pl.png "Property changes for a modified node")

In the case below, the Human Activity “Analyse_Expense” is in red because there is a conflict since the Destination Screen and Close on Event are different in both revisions.

The same happens to the header, since the icon, name, and description of the workflow are different as well.

![Comparison view showing a Human Activity node and workflow header highlighted in red to indicate conflicts in destination screen, close on event, icon, name, and description between revisions.](images/changes-details-deleted-pl.png "Conflicting human activity and header changes")

In this next example, the Automatic Activity “Expense_Process” appears in green on the left side because it’s an added node. When you open the properties panel, all properties appear in green because the activity only exists in the left canvas.

![Comparison view where an Automatic Activity node appears only on the left canvas in green, and its properties panel shows all properties highlighted as added.](images/changes-details-added-pl.png "Added automatic activity node details")

When you delete a node, the comparison view highlights its connector in blue. The deleted node itself disappears from the canvas.

In the example below, the Parallel Activity after “Analyse_Expense” no longer exists on the left canvas. Its connector appears in blue to mark the deletion. On the right canvas, the activity and its connector remain unchanged.

![Comparison view showing a Parallel Activity missing from the left canvas while its connector is highlighted in blue, with the node still present on the right canvas to indicate deletion.](images/changes-details-deleted-node-pl.png "Deleted node indicated by connector change")

### Navigation

Both canvases are read-only. You can't edit, add, or delete nodes while in the comparison view.

Both canvases synchronize pan and zoom. When you scroll or zoom on one side, the other side moves in sync, making it easier to compare corresponding parts of the workflow.
