---
summary: A flow with more than 50 nodes, or with 20 to 50 nodes and no comments, is hard to understand and maintain.
tags:
  - Logic
  - Modular Programming
  - Refactoring
  - Technical Debt
guid: 34e826d1-c93f-488e-8e42-524502cc0617
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3522-58&t=fro20soaPpjjIXwf-1
coverage-type:
  - unblock
topic:
  - simplify-long-flows
audience:
  - Developer
  - Front-end developer
  - Tech lead
outsystems-tools:
  - none
isautopublish: true
---
# Long undocumented flow

Action with a very long flow, or a long flow without comments.

## Impact

A long flow is hard to understand and maintain. It's harder still when no comments explain the logic.

## Why is this happening?

The flow has too many nodes. This happens in one of the following cases:

* **Very long flow**: The flow has more than 50 nodes, even if it has comments.

* **Medium flow without comments**: The flow has 20 to 50 nodes and no comments.

The node count excludes comments. The same rule applies to every action type and to screen actions.

![A complex flow diagram with multiple nodes and no comments.](images/odcs-undocumented-flow.png "Undocumented Flow")

## How to fix

Break the flow logic into smaller, reusable actions. For a medium flow, adding comments that explain portions of the logic also resolves the finding. For a very long flow, comments don't resolve the finding, so split the flow.

![A flow diagram with multiple nodes and a comment added to explain part of the logic.](images/odcs-comment-flow.png "Flow with Comments")

**Note**: Explore the **Extract to Action** feature.

To select the **Extract to Action** feature:

1. Right-click on the selected portion of the flow.

1. Select **Extract to Action**.

![Context menu showing the 'Extract to Action' option highlighted in a flow diagram.](images/odcs-extract-to-action.png "Extract to Action Feature")
