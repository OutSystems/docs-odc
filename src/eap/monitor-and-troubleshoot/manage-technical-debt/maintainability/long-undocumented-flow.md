---
summary: An action with a high node count is hard to maintain, especially if it has no comments to explain the logic.
tags: maintenance, flow logic, comments, troubleshooting, node count
guid: 34e826d1-c93f-488e-8e42-524502cc0617
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3522-58&t=fro20soaPpjjIXwf-1
coverage-type:
  - evaluate
audience:
  - mobile developers
  - frontend developers
  - tech leads
outsystems-tools:
  - none
---
# Long undocumented flow

Action with a long and undocumented flow.

## Impact

A client action with more than 20 nodes or an action with more than 40 nodes is hard to maintain, especially if it has no comments to explain the logic.

## Why is this happening?

A client action within a flow contains more than 20 nodes or any action that surpasses 40 nodes. This high node count makes the flow difficult to understand and maintain, especially in the absence of comments that explain the underlying logic.

![A complex flow diagram with multiple nodes and no comments.](images/odcs-undocumented-flow.png "Undocumented Flow")

## How to fix

Break flow logic into smaller and potentially reusable actions and/or place comments to explain portions of your flow.

![A flow diagram with multiple nodes and a comment added to explain part of the logic.](images/odcs-comment-flow.png "Flow with Comments")

**Note**: Explore the **Extract to Action** feature.

To select the **Extract to Action** feature:

1. Right-click on the selected portion of the flow.

1. Select **Extract to Action**.

![Context menu showing the 'Extract to Action' option highlighted in a flow diagram.](images/odcs-extract-to-action.png "Extract to Action Feature")

