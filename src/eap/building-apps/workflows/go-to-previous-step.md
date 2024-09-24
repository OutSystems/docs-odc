---
summary: Learn how to  go to a previous step in your workflow
tags:
locale: en-us
guid: 0f6e0ee0-427a-4ed6-b1f9-506cf094363c
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# Go to a previous step

When implementing your workflow, the **Go to a previous step** node allows you to return to a previous node in the workflow. This node mitigates the risk of infinite loops by restricting connections to previous nodes within the workflow, excluding the start node. The **Go to previous step** is only available when the next node is the **End** node, and there must be at least one **Decision** node preceding it.

For example, the workflows can return to a previous activity in a bank transaction. If the bank employee finds invalid user documents while approving the loan, they send them back for Document review validation.

![Screenshot of the ODC Portal with Go to previous step for banking example](images/go-to-previous-step-workflow-pl.png "ODC Portal Banking example")
