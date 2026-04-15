---
summary: Multiple server Aggregates or multiple Server Action requests inside Client Actions.
tags: server requests, aggregates, client actions, latency reduction, best practices
guid: e23a842d-a31b-4cb8-850a-f6612d1f0c16
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3525-200&t=ZHJybqzEUX6B7aIU-1
coverage-type:
  - unblock
  - remember
audience:
  - frontend developers
  - full stack developers
  - backend developers
outsystems-tools:
  - odc studio
  - odc portal
---
# Multiple server requests (Aggregates or Actions) inside Client Actions

Multiple server Aggregates or multiple Server Action requests inside Client Actions.

## Impact

Each server request or server Aggregate is a different request, generating its overhead on establishing the connection and launching a server-side process. Multiple processes also generate different database transactions.

## Why is this happening?

Server-side logic breaks down into multiple separate Aggregates or Server Actions, each called individually within a Client Action. Each call results in a separate server request, leading to multiple round trips between the client and server, which can increase latency.

![A Client Action flow with multiple Run Server Action nodes.](images/odcs-multiple-server-requests.png "Multiple Server requests inside a Client Action")

## How to fix

Instead of sequencing a set of server requests or server Aggregates on your client-side code, compose all required server logic in a single Server Action. This reduces the number of server requests.

![A Client Action flow with a single Run Server Action node.](images/odcs-single-server-action.png "Single Server request inside a Client Action")

For more information, refer to the [logic best practice for avoiding multiple server calls in a client action flow](../../../building-apps/logic/best-practices-logic.md#multiple-server-calls).
