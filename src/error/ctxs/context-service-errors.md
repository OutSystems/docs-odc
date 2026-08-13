---
summary: Reference for OutSystems Developer Cloud (ODC) Context Service errors (OS-CTXS) returned to agent harnesses that query the Enterprise Context Graph.
tags:
  - AI
  - Agentic
  - Troubleshooting
guid: fb418a18-5113-473a-b3c7-e5bf0457e5f0
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
audience:
  - Developer
outsystems-tools:
  - none
coverage-type:
  - remember
  - unblock
isautopublish: true
---

# Context Service errors

The Context Service powers tenant-wide discovery and semantic search across the Enterprise Context Graph. It backs the tools that external agent harnesses use to find apps, entities, and integrations across an ODC tenant. Errors in the `OS-CTXS` family surface through your agent harness when one of those requests fails.

Several codes in this family signal failures inside the Context Service or its upstream dependencies that you can't resolve directly. The reference exists so you can match the code to a cause, take the corrective action when one is available, and include the exact code when you contact OutSystems Support.

## Error sources

The error codes group into two categories based on where the failure occurs.

* **Caller-side errors.** The request the agent harness sent is incorrect or out of scope. The pages list what to verify or who to contact.
* **Server-side and upstream errors.** The Context Service or one of its dependencies returned a failure. The pages explain what the failure means and direct you to OutSystems Support.

## Using the error code

Use the error code to locate the matching page. Each page documents the cause, the impact on the in-flight request, and the recommended action. The action might be yours, an administrator's, the provider of your agent harness tooling, or OutSystems Support.
