---
summary: OutSystems Developer Cloud (ODC) provides server actions to perform various operations on human activity in run time.
tags: workflows, server actions, human activity, runtime operations, low-code apis
locale: en-us
guid: dc9f69f7-605a-4865-96dd-c70140f80a89
app_type: mobile apps, reactive web apps
platform-version: odc
content-type:
  - reference
figma:
audience:
  - backend developers
  - full stack developers
outsystems-tools:
  - odc studio
---
# Workflows

ODC provides server actions (low-code APIs) to modify the workflows at runtime.

## Actions

### HumanActivityAssign

_Server action_

<div class="info" markdown="1">

You must add the server action as a [public element](../../building-apps/libraries/use-public-elements.md) in the ODC app before using it.

</div>

You can assign or modify the UserId to whom the human activity is assigned at runtime. You can access this server action in the ODC Studio under **Logic > System > Server actions**.

**Use case:**
In a loan approval workflow, a loan application is initially assigned to a loan officer for review. If the loan officer is unavailable, the application can be reassigned to another officer using the **HumanActivityAssign** API. This ensures the workflow progresses without delays.

The API uses the ActivityInstanceId to identify the human activity of a workflow instance to which we want to assign the user.

For detailed information about using human activity in workflows, refer to [Using human activity](../../building-apps/workflows/add-human-activity.md)

_Inputs_

**ActivityInstanceId**
:   Type: ActivityInstance Entity. Mandatory.
    Identifier of the workflow instance. This value can be retrieved from the ActivityInstance entity

**UserId**
:   Type:  Mandatory.
    Identifier of the user to whom the activity is to be assigned.

### HumanActivityOpen

_Server action_

<div class="info" markdown="1">

You must add the server action as a [public element](../../building-apps/libraries/use-public-elements.md) in the ODC app before using it.

</div>

With this API, you can open a human activity at runtime. The human activity is assigned to the user who opens it, and the activity status changes to Open. This API is mainly used for reporting purposes to identify the time and effort involved in completing the human activity. You can access this server action in the ODC Studio under **Logic > System > Server actions**.

**Use case:**
In a loan approval workflow, a senior manager can use this API to open a human activity for reviewing loan application documents. This allows them to track the time and effort required for the review process and identify areas for workflow optimization.

The API uses the ActivityInstanceId to identify the human activity of a workflow instance.

For detailed information about using human activity in workflows, refer to [Using human activity](../../building-apps/workflows/add-human-activity.md)

_Inputs_

**ActivityInstanceId**
:   Type: ActivityInstance Entity. Mandatory.
    Identifier of the workflow instance. This value can be retrieved from the ActivityInstance entity

### HumanActivityRelease

_Server action_

<div class="info" markdown="1">

You must add the server action as a [public element](../../building-apps/libraries/use-public-elements.md) in the ODC app before using it.

</div>

You can release a human activity from a user currently carrying it using a low-code API implemented as a server action. The human activity is then available to be assigned to a different user, and the status of the activity changes to **Waiting**. You can access this server action in the ODC Studio under **Logic > System > Server actions**.

**Use case:**
In a loan approval workflow, a loan officer is assigned to review the loan application documents. If the loan officer realizes they cannot complete the task due to missing information or conflicting priorities, the HumanActivityRelease API can be used to release the task. This makes the human activity available for reassignment to another loan officer, ensuring the workflow continues without delays.

The API uses the ActivityInstanceId to identify the human activity of a workflow instance.

For detailed information about using human activity in workflows, refer to [Using human activity](../../building-apps/workflows/add-human-activity.md)

_Inputs_

**ActivityInstanceId**
:   Type: ActivityInstance Entity. Mandatory.
    Identifier of the workflow instance. This value can be retrieved from the ActivityInstance entity

### ProcessTerminate

_Server action_

<div class="info" markdown="1">

You must add the server action as a [public element](../../building-apps/libraries/use-public-elements.md) in the ODC app before using it.

</div>

You can terminate the execution of an active process using this low-code API implemented as a server action.  This server action can be accessed in the ODC Studio under **Logic > System > Server actions**.

The API uses the ProcessInstanceId to identify the process to be terminated.

_Inputs_

**ProcessInstanceId**
:   Type: ProcessInstance Entity. Mandatory.
    Identifier of the process instance. This value can be retrieved from the ProcessInstance entity.
