---
summary: OS-CTXS-40001 occurs when an agent harness sends a request to the OutSystems Developer Cloud (ODC) Context Service that doesn't match the API contract.
tags:
  - Agentic
  - AI
  - Troubleshooting
guid: 85b2344d-4186-42ae-9846-4d63a0fccdae
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
audience:
  - Developer
outsystems-tools:
  - none
coverage-type:
  - unblock
isautopublish: true
---

# OS-CTXS-40001

## Error message

```
Request does not follow agreed upon contract.
```

## Cause

The agent harness sent a request that doesn't match the Context Service request contract. The most common reason is a mismatch between the version of the OutSystems plugin or Power running in the agent harness and the Context Service API.

## Impact

The Context Service rejected the request without processing it.

## Recommended action

Update the OutSystems integration in your agent harness and retry. If the error continues, report it to the provider of your agent harness tooling with the request details. If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-CTXS-40001).
