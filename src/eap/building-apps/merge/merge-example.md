---
summary: "ODC merge conflict resolution: resolve CSS and action assign element conflicts when two developers edit the same ODC app simultaneously."
locale: en-us
guid: 04cfd0b0-ab60-454e-a770-6a8d19f9974f
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=4002%3A633&mode=design&t=lSXYmGomrMjw4KTt-1
tags:
  - CSS
  - Logic
  - Screens
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
coverage-type:
  - apply
content-type:
  - procedure
isautopublish: true
---

# Compare and merge example with conflicts

In this example, you're trying to publish an app, but a **Modified revision detected** window appears. You and your fellow developer edited the app simultaneously. You select **Compare revisions** > **Merge and publish**, but there are conflicting changes between the local and the published revisions of the app.

Due to conflicts, you can't automatically integrate your changes. ODC displays two options: **Overwrite with this revision** and **Compare revisions**. You select **Compare revisions** to compare your revision with the other revision.

![Popup window showing 'Modified revision detected' indicating conflicts in the app](images/conflicts-detected-odcs.png "Conflicts Detected in ODC")

After analyzing the **Compare and Merge** window, you find that:

* You both edited the CSS on the "ClientList" screen. You must resolve the conflicting changes.
* You both edited the "Section" Assign on the "SaveOnClick" action. You need to resolve the conflicting changes.
* The other developer added a new screen called "Report." There are no conflicts to resolve here.

Follow these steps to resolve the conflicts.

1. Double-click the **Style Sheet (pending text conflict)** element in the **ClientList** screen. The **Compare and Merge - Style Sheet** window opens. The number in the **Merged revision (1 conflict)** tab indicates the number of conflicts.

    ![Compare and Merge window highlighting conflicts in the Style Sheet of the 'ClientList' screen](images/conflicts-text-odcs.png "Conflicts in Style Sheet")

1. Select the checkbox next to the text in **Merged revision** to add the CSS code of the revision. **Merged revision (1 conflict)** changes to  **Merged revision (0 conflicts)**. You can edit the code by typing in the **Merged revision** pane.

    ![Merged revision pane with an orange arrow pointing to the checkbox to resolve the CSS code conflict](images/conflicts-text-orange-arrow-odcs.png "CSS Conflict Checkbox")

1. Select **Done and back** in the lower right corner of the screen to return to the **Compare and Merge** section.

    ![Compare and Merge section with the 'Done and back' button in the lower right corner](images/merge-example-compare-odcs.png "Compare and Merge Done and Back")

1. Double-click **SaveOnClick** to open the **Compare and Merge - SaveOnClick** window. The `Section` assign element has conflicting values.

    ![Compare and Merge - SaveOnClick window showing conflicting 'Section' assign values](images/visual-element-changes-odcs.png "SaveOnClick Section Assign Conflicts")

1. Select the value viewer labeled by the three dots (`...`) next to the **Assignments** value to open the **Compare and Merge - Value** window.

1. To select the value from your revision of the app, click the check box in the  **Merged revision (1 conflict)** pane. **Merged revision (1 conflict)** changes to **Merged revision (0 conflicts)**.

    ![Checkbox selected in the Merged revision pane indicating a resolved conflict in the app](images/text-changes-checkbox-odcs.png "Resolved Conflict Checkbox")

1. Select **Done and back** in the lower right corner to return to the **Compare and Merge - SaveOnClick** section.

1. Select **Back** in the lower right corner to return to the main **Compare and Merge** window. If there are no conflicts (no elements highlighted in red), you publish the app.

1. Select **Merge and Publish** to publish it. To update the local app and publish later, select **Merge** at this step.

    ![Final screen showing the 'Merge and Publish' button indicating the merge process is complete](images/merge-complete-odcs.png "Merge Complete")
