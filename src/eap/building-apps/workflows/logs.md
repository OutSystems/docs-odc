---
summary: Introduction to ODC workflow logs.
tags: workflow logs, business process management, troubleshooting, process analysis, workflow monitoring
outsystems-tools:
  - odc portal
guid: 3c5d3179-bef9-43ca-9636-90c4d40aa61f
locale: en-us
app_type: mobile apps, reactive web apps
content-type:
  - conceptual
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?m=auto&node-id=6372-10&t=QL4wNRboofdp7zdI-1
audience:
  - business analysts
  - platform administrators
  - full stack developers
  - team lead
  - team manager
  - project managers
  - product owners
---
# Workflow logs

The ODC portal provides a centralized, detailed view of all activities within a workflow. Workflow logs allow business process owners (BPOs) and developers to analyze and troubleshoot workflows.

The following types of changes are logged automatically:

* When the process starts

* When a conditional start is initiated

* When the process ends

* Instance status transitions

* Activity status transitions

* When a human activity is opened

* When a human activity is released

* When a handled event closes a human activity or wait activity

* When a human activity is assigned to a user

* When a human activity is assigned to a role

* When a terminate instance operation is used

* When a retry operation is used

## Benefits of using logs

With workflow logs, you can:

* Access a chronological record of all significant changes in a workflow's execution. This allows you to track actions, identify who performed them, and understand when and where they occurred.

* Access information about a specific instance of a workflow or multiple workflow executions. This allows you to investigate anomalies, identify patterns, and respond to inquiries.

## Using workflow logs

Consider this example of a loan approval workflow. As a BPO, you are responsible for ensuring the workflow runs smoothly. The bank received a complaint from a client regarding a loan application that took an unusually long time to process. You must identify the cause of the delay to prevent similar issues in the future.

Note: To track the complaint, you must have the workflow instance number.

1. In ODC Portal, navigate to **Monitor** >  **Logs** > **Workflows**.

1. From the **Workflow** dropdown, select the workflow you want to examine.

    ![Dropdown menu in ODC Portal showing various workflow options with 'Loan Approval' selected.](images/select-workflow-pl.png "Workflow Selection Dropdown")

1. In the **Instance** field, enter the instance ID.

    ![Input field in ODC Portal for entering the Instance ID with an example ID entered.](images/instance-id-pl.png "Instance ID Input Field")

    **Note**: Enter the IDs of the workflows you want to analyze. To identify patterns across specific workflow instances, provide multiple IDs. For example, this can help determine if an instance is part of a recurring pattern rather than an isolated case.

    <div class="info" markdown="1">

    When you apply at least one Instance ID, the **Date/Time** filter automatically changes to **Last 30 days.** The maximum log retention period is 30 days.

    </div>

1. In the **Context** dropdown, filter by the context level, such as the instance level or the type of activity you want to investigate.

Applying these optional filters tailors the logs to better match your search.

The structure of a log includes:

* **Time**- The time the activity is performed.

* **Workflow**- The workflow in which the activity is performed.

* **Instance**- The unique identifier that represents a specific execution of the workflow process.

* **Context**- The context level where the operation occurred.

* **Message**- Provides a more granular look into the operation performed.

* **User**- The person who performs the operation.

![Log entries in ODC Portal showing details such as time, workflow, instance ID, activity, message, and user.](images/logs-pl.png "Workflow Logs")

## Troubleshooting instances

For more information about troubleshooting workflow instances, refer to [Troubleshooting workflows](troubleshooting-workflows.md).

## Related resources

* [Troubleshooting workflows](troubleshooting-workflows.md)

* [Deploy workflows](../../deploying-apps/deploy-apps.md)
