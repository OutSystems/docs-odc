---
summary: Learn how to end a workflow
tags: workflow management, process design, user interface flows, app development, service studio usage
locale: en-us
guid: 4bf7d64b-4197-4769-86e4-50a69f579ead
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - understand
---

# End a workflow

You can continue adding steps to your workflow until you reach the **End** node. Once the workflow reaches the End node, the workflow execution stops.

If your workflow includes one or more [conditional start](add-conditional-start.md) flows, the workflow is completed when the **End** node is reached in both the main workflow and all conditional start flows. The workflow instance status then changes to **Done**. This means the main workflow will not finish until every conditional start flow has been completed.

If your workflow has no conditional start flows, the workflow is completed when the **End** node is reached, at which point all activities are complete, and the workflow instance status changes to **Done.**

## Related resources

* [Troubleshooting workflows](troubleshooting-workflows.md)

* [Deploy workflows](../../deploying-apps/deploy-apps.md)

* [Terminate a workflow](terminate-workflow.md)
