---
summary: Some parts of logic never run due to hard-coded True/False conditions
tags: hard-coded conditions, dead code, feature flags, logic best practices, troubleshooting
guid: 2ba9682e-9253-4df7-9c9f-a7dc5f391cd9
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3523-166&node-type=CANVAS&t=fro20soaPpjjIXwf-0
coverage-type:
  - unblock
audience:
  - mobile developers
  - full stack developers
  - test engineers
outsystems-tools:
  - none
---
# Hard-coded statements

## Impact

Some parts of your logic never run due to hard-coded True/False conditions. This can result in dead code, forgotten feature flags, or incorrect/unexpected behavior in your actions. Unreachable logic can also take the team's time to test, maintain, and document code that's never used.

## Why is this happening?

The code uses hard-coded True/False conditions, causing certain branches of the logic to be permanently bypassed and never executed

![Flowchart showing a condition that is always true, causing the false branch to never execute.](images/odcs-unreachable-logic.png "Flowchart with Unreachable Logic")

In this example, the flow has a condition that's always **True**. The **False** branch never executes because the condition doesn't allow it to be reached.

## How to fix

Revise the affected True/False conditions and consider removing/changing the unreachable logic.

For more information, refer to the [logic best practice for avoiding hard-coded values](../../../building-apps/logic/best-practices-logic.md#hard-coded-values).
