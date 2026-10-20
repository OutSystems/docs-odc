---
summary: OutSystems Developer Cloud (ODC) merge in ODC Studio helps you compare app revisions side by side and resolve conflicting textual and visual changes.
locale: en-us
guid: ac454655-5a7f-47fb-8797-584d44f89894
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=4002%3A173&mode=design&t=upO9mxr7in19rYkC-1
tags:
  - 1-Click Publish
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
coverage-type:
  - apply
  - unblock
content-type:
  - conceptual
  - procedure
isautopublish: true
---

# Merge the work

In an environment where many developers work on the same app, you often need to incorporate other people's changes. OutSystems Developer Cloud (ODC) Studio automatically merges differences if no conflicts exist.
If ODC detects conflicting changes when you select **1-Click Publish**, you must resolve them before publishing the app.

ODC Studio's merge capabilities are designed with OutSystems visual language, so that you can review changes for both visual and textual elements.

To resolve conflicts, refer to [Compare and merge example](merge-example.md). For an overview of how merge works in a team, refer to [The merge feature and team collaboration](concepts.md).

## Conflicting revision detected

If ODC Studio detects changes and can't automatically merge and publish your app, ODC Studio displays the **Conflicting revision detected** window. The following list describes the most relevant buttons and their actions.

* Override with this revision
:   Overrides the published revision of the app with your local revision. All changes in the current published revision are lost.

* Compare revisions
:   Opens the **Compare and Merge** window to preview the changes between revisions. You then edit the local revision and publish it.

![Screenshot of the 'Conflicting revision detected' window in OutSystems Developer Cloud Studio](images/modified-version-detected-odcs.png "Conflicting Revision Detected in ODC Studio")

## Compare revisions window

To open the **Compare revisions** window, select **Compare revisions** in the **Conflicting revision detected** window. The **Compare revisions** window displays the local and published revisions side by side, enabling you to select and incorporate textual and visual elements. Elements with conflicting changes are labeled **Conflict (Modified)** or **Conflict (Deleted)**. Double-click an element to navigate to the details screen.

## Edit the textual elements

During the merge, you edit textual elements such as CSS, JavaScript, and property values within elements in a conflict state. The textual elements are read-only if they aren't in a conflict state. When you double-click a textual element, two tabs display the different revisions of the element.<br/>

**Merged revision (# of conflicts)** tab in a conflict state, with the editable text and comparison:

* **Your revision** pane – displays the textual element in the local revision of the app during a merge, which you can edit.
* **The other revision** pane – displays the textual element in the published revision of the app, which you cannot edit.

Select **Done and back** to save the resolved conflict and go back to the compare screen.

**Merged revision (# of conflicts)** tab not in a conflict state, with the comparison:

* **Your revision** pane: displays the textual element in the local revision of the app. You can't edit it.
* **The other revision** pane: displays the textual element in the server revision of the app. You can't edit it.

Select **Back** to go back to the compare screen.

### Resolve conflicts in the textual elements

Select the changes you want to publish to the server. From the **Merged revision (# of conflicts)** tab,

* To accept the changes from the published revision, select the red arrow in **The other revision** pane.
* To accept the changes from the local revision, select the check box in **Merged revision** pane.
* To change the resulting local revision, edit the text in **Merged revision** pane.

### Highlight all differences

By default, the pane for editing the changes highlights only the lines with conflicts. To highlight all the changes, select the **Highlight all differences** check box.

### Color reference

The highlights in different colors help identify the differences between the revisions. To see a tooltip description, hover over the highlight.

Following are the color descriptions.

| Color | Name | Meaning |
| --- | --- | --- |
| ![Color reference indicating a gray highlight for a deleted line in the merge comparison](images/color-modifed-deleted.png "Color Reference for Deleted Line") | Gray | Deleted line |
| ![Color reference indicating a green highlight for an inserted line in the merge comparison](images/color-modifed-added.png "Color Reference for Inserted Line") | Green | Inserted line |
| ![Color reference indicating a light blue highlight for an unchanged line with no conflicts in the merge comparison](images/color-modifed-light.png "Color Reference for Unchanged Line") | Light blue | The modified line with no changes and conflicts, no changes in this revision |
| ![Color reference indicating a red highlight for a line modified in both versions with conflicts in the merge comparison](images/color-modifed-conflict.png "Color Reference for Conflicted Line") | Red | Modified in both versions with conflicts |

## Recover previous merge

ODC saves the merge changes and actions automatically. When the **Recover Previous Merge** window appears, select **Yes** to continue working on changes without losing the previous edits. Selecting **No** deletes the saved merge edits, and you must start the edits from scratch.

![Screenshot of the 'Recover Previous Merge' dialog in OutSystems Developer Cloud Studio](images/recover-previous-merge-dialog-odcs.png "Recover Previous Merge Dialog in ODC Studio")
