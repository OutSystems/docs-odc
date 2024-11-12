---
summary: Filtering workflow activities to build interactive UI components
tags: 
outsystems_tools: 
guid: b7af3484-4044-4e5c-a1f7-680c5a8edce5
locale: en-us
app_type: mobile apps, reactive web apps
content_type: 
audience: 
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=6274-150
---

# Build UI components using workflow entities

By using aggregates to filter workflow activities, you can, for example, build responsive dashboards and tailored task boxes, which contribute to a more streamlined and productive app experience. For example, in a loan approval app, an aggregate could group all loan applications exceeding a certain amount, allowing a financial manager's dashboard to show only those that need their approval.

Before you can create an aggregate that filters activities in a specific workflow, you need to do the following:

* Add the necessary **system entities** to your ODC app as public elements.

    ![Screenshot showing adding public elements in ODC Studio](images/workflow-public-elements-odcs.png "Add public elements to your ODC app")

* Copy the **ProcessDefinitionKey** - In the Workflow editor, click the ellipsis and select **Copy process definition key**. The process definition key identifies the specific workflow.

    ![Screenshot showing how to copy the process definition key in the ODC Portal](images/process-def-key-pl.png "Copy the process definition key in ODC Portal")

* Copy the **ActivityDefinitionId** - In the Workflow editor, go to a specific activity, click the ellipsis, and select **Copy activity definition key**. The activity definition key identifies the specific activity in a workflow.
    
    ![Screenshot showing how to copy the activity definition key in the ODC Portal](images/activity-def-key-pl.png "Copy the process definition key in ODC Portal")

The following is an example of how you can create an aggregate that filters a specific workflow process by a specific human activity.

1. Create the **GetHumanActivityInstances** aggregate using the **ActivityInstance**, **ActivityDefinition**, and **ProcessDefinition** entities.

    ![Screenshot showing the GetHumanActivityInstances aggregate in ODC Studio](images/workflows-aggregate-odcs.png "GetHumanActivityInstances aggregate in ODC Studio")

1. Set the aggregate filter to the following:

    * **ActivityDefinition.Key** = the activity definition key of a specific human activity in the workflow

    * **ProcessDefinition.Key** = the definition process key of the workflow

    This returns all human activities with that key in that specific workflow. 
     
    ![Screenshot showing the GetHumanActivityInstances aggregate in ODC Studio](images/workflows-agg-filter-odcs.png "GetHumanActivityInstances aggregate in ODC Studio")
