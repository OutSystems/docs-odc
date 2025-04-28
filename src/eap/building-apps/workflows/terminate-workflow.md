---
summary: Learn how to terminate a workflow
tags: workflow termination, mobile apps, reactive web apps, workflow management, automatic activities
locale: en-us
guid: 79d2da47-7cb8-48eb-bc23-04f62fd67c86
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
coverage-type:
  - understand
audience:
  - full stack developers
  - mobile developers
outsystems-tools:
  - none
---
# Terminate a workflow

When implementing your workflow, you can use a **Terminate** node to stop the workflow execution. 

When a **Terminate** node is reached in a workflow:

1. Any ongoing activities (except automatic activities) are interrupted and their status changes to **Terminated**.

1. Any ongoing automatic activities are executed. Once finished, their status changes to either **Completed** or **Error**.

1. The workflow instance status changes to **Done**.

## Related resources

* [Troubleshooting workflows](troubleshooting-workflows.md)

* [Deploy workflows](../../deploying-apps/deploy-apps.md)

* [End a workflow](end-workflow.md)
