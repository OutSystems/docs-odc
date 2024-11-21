---
summary: 
tags: 
guid: e9f56ae4-aea1-411e-8ddd-6391e0b51fcc
locale: en-us
app_type: reactive web apps
platform-version: odc
figma: 
---

# Workflow nodes

You can implement a workflow in the workflow editor using the following nodes:

* [Start](start-workflow.md)

* [Automatic activity](add-automatic-activity.md)

* [Human activity](add-human-activity.md)

* [Decision](add-decisions.md)

* [Go to a previous step](go-to-previous-step.md)

* [End](end-workflow.md)

## Statuses of workflow nodes

At any given time, based on the progress of the activity, the workflow node can be in one of the following statuses:

- **Running** - The activity is currently being executed, such as when a service action is retrieving data.

- **Waiting** - The activity is on hold, awaiting further action. For instance, the **HumanActivityNode** can be on stand-by for manual intervention or the **AutomaticActivityNode** can be waiting for a scheduled event.

- **Completed** -  The activity has finished, allowing the workflow to proceed to the next step.

- **Terminated** - The activity and the entire workflow is terminated following the successful execution of the **ProcessTerminate** API or any other unexpected terminate activity.

- **Error** - The activity encounters an issue, which can happen due to:
  * An error in the service action that the activity calls.
  * Reaching the maximum number of retries without successful execution.
  * Temporary problems, such as a service action being unavailable.

- **Open** - The human activity has been opened by an end-user but has not yet proceeded to execution.

<div class="info" markdown="1">

The **Open** status applies only to human activity node.

</div>

## Related resources

* [Workflows in ODC](workflows-in-odc.md)
* [Using workflows](using-workflows.md)
* [Troubleshooting workflows](troubleshooting-workflows.md)

