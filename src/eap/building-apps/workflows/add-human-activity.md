---
summary: Learn how to add a human activity to your workflow
tags:
locale: en-us
guid: 9b6fcc2b-f38c-4225-b5a0-4989655f9545
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# Add human activity

When implementing your workflow, you can include tasks to be carried out by the end-user. This is accomplished by including a **HumanActivity** node in your workflow. 

In the workflow editor for **HumanActivityNode**:

* Specify a task and assign it to an end-user of your ODC app. You can change the user ID programmatically in ODC Studio using the [HumanActivityAssign](#programmatic-assign) API to assign a task to a different end-user. 

    **Note**: You must develop your own custom notifications using the **HumanActivityInstance** entity to remind users of pending tasks.

* Select the **Close on** event and set the conditions within the human activity. If the conditions are not set, all human activities listening for the **Close on** event will end on the event's occurrence.

After the human activity executes, its status remains Open, Running, or Waiting until the ODC app triggers the **Close on** event. In ODC Studio, you must build your own logic that triggers the **Close on** event to end the human activity. 

When the **Close on** event occurs, and conditions within the human activity are met, the human activity ends, and the workflow moves to the next step.

To include human activity in a workflow, follow these steps:

1. From the workflow editor, click the (+) icon between the two nodes and choose **Human activity**.

1. Enter the following details in the sidebar:

    a. **Add description**: (Optional) Brief description of the human activity task to be carried out.

    b. **Fetch more data**: (Optional) Select a service action from the ODC app. You can add multiple service actions from different apps. For example, you can select a service action, GetUserDocs, from the Loans app and a service action GetManagerName from the Directory app. If the service action has one or more input parameters, enter values for the mandatory input parameters to execute the service action. 

    c.**Assign to**: (Optional) Identifies who the activity is assigned to. You can select a User ID to assign the activity.  

    **Note:** You can change the User ID at runtime in ODC Studio using the **HumanActivityAssign** server action under **System**.

    d. **Destination screen:** (Optional) Select the public screen of your app where the user must perform the human activity. If applicable, you can enter input parameters in this screen to pass context from the workflow to your app.

    **Note:** The destination screen is stored as a relative URL in the URL attribute of the system entity **HumanActivityInstance**. After the workflow revision has been published, if the app name, screen name, or attributes of the destination screen are changed, the URL stored in the system entity becomes invalid. In such cases, you must create a new revision.

    e. **Display message**: (Optional) Click the text area to open the Expression Editor and edit the condition on the editor. You can add more data so that more information is available for use within the scope of the Expression editor.

    f. **Close on**: (Mandatory) Select the event and define the conditions within the human activity.  Once the event occurs and the conditions are met, **HumanActivityStatus** changes from Waiting or Running to Completed, and the workflow moves on to the next step. For example, in a human document review scenario, only when the event **LoanReview** occurs, and both conditions (DocsVerified=OK AND NumberDocsReviewed=NumberDocsSubmitted) are simultaneously true, will the human activity be closed, and the workflow moves on to the next step.

## Manually assign or re-assign human activity to a different user { #programmatic-assign }

You can modify the UserId to whom the human activity is assigned at runtime using low-code API implemented as a server action. This enables you to change the workflow from the ODC app at runtime. This server action can be accessed in the ODC Studio under the Logic > System > Server actions. 

The API uses the ActivityInstanceId to identify the workflow instance. This value is passed from the workflow editor in the ODC portal to Studio apps using service actions and screen input parameters.
 
**Name** |  **Description** |  **Input Parameters**| **Type** | Mandatory/Optional
---|---|---|---|---
 HumanActivityAssign| Assigns or re-assigns a human activity to a specific user of a particular workflow instance. |ActivityInstanceId - Identifier of the workflow instance. This value can be retrieved from the ActivityInstance entity. |EntityReference | Mandatory
 | | |UserId - Identifier of the user who the activity is to be assigned to. | |  Mandatory

