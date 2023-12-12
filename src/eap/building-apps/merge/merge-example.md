---
summary: Resolve conflicts when merging app revisions
locale: en-us
guid: 04cfd0b0-ab60-454e-a770-6a8d19f9974f
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=4002%3A633&mode=design&t=lSXYmGomrMjw4KTt-1
---
# Compare and merge example with conflicts

In this example you are trying to publish an app, but a window **Modified revision detected** pops up. It seems that you and your fellow developer edited the app simultaneously. You select **Compare revisions** > **Merge and publish**, but there are conflicting changes between the local and the published versions of the app. 

Due to conflicts, you can't automatically integrate your changes. ODC displays two options, **Overwrite with this revision** and **Compare revisions**. You click **Compare revisions** to compare your revision with the other revision. 

![Popup window showing 'Modified revision detected' indicating conflicts in the app](images/conflicts-detected-odcs.png "Conflicts Detected in ODC")

After analyzing the **Compare and Merge** window, you find that:

* You both edited the CSS on the "ClientList" screen. You must resolve the conflicting changes.
* You both edited the "Section" Assign on the "ButtonOnClick" action. You need to resolve the conflicting changes.
* The other developer added a new screen called "Report." There are no conflicts to resolve here.

Follow these steps to resolve the conflicts.

1. Double-click the element **Style Sheet (pending text conflict)** in the **ClientList** screen. The **Compare and Merge - Style Sheet** opens. The number in the tab **Merged revision (1 conflict)** indicates the number of conflicts.

    ![Compare and Merge window highlighting conflicts in the Style Sheet of the 'ClientList' screen](images/conflicts-text-odcs.png "Conflicts in StyleSheet")

1. Select the checkbox next to the text in **Merged revision** to add the CSS code of the revision. **Merged revision (1 conflict)** changes to  **Merged revision (0 conflicts)**. You can edit the code by typing in the **Merged revision** pane.

    ![Merged revision pane with an orange arrow pointing to the checkbox to resolve the CSS code conflict](images/conflicts-text-orange-arrow-odcs.png "Edit Conflict Revision")

1. Click **Done and back** in the lower right corner of the screen to return to the **Compare and Merge** section.

    ![Compare and Merge section with the 'Done and back' button in the lower right corner](images/merge-example-compare-odcs.png "Merge Example")

1. Double-click **SaveOnClick** to open the **Compare and Merge - ButtonOnClick** window. You see that the `Section` assign element has conflicting values.

    ![Compare and Merge - ButtonOnClick window showing conflicting 'Section' assign values](images/visual-element-changes-odcs.png "Visual Element Changes")

1. Click on the value viewer labeled by the three dots (`...`) next to the **Assignments** value to open **Compare and Merge - Value** window.

1. To select the value from your revision of the app, click the check box in the  **Merged revision (1 conflict)** pane. **Merged revision (1 conflict)** changes to **Merged revision (0 conflicts)**.

    ![Checkbox selected in the Merged revision pane indicating a resolved conflict in the app](images/text-changes-checkbox-odcs.png "Resolved Conflicts")

1. Click **Done and back** in the lower right corner to return to the **Compare and Merge - ButtonOnClick** section.

1. Click **Back** in the lower right corner to return to the main **Compare and Merge** window. If there are no conflicts (no elements highlighted in red), you can publish the app.

1. Click **Merge and Publish** to publish it. If you want to update the local app and publish later, click **Merge** at this step.

    ![Final screen showing the 'Merge and Publish' button indicating the merge process is complete](images/merge-complete-odcs.png "Merge Complete")
