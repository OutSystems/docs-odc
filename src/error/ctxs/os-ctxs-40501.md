---
summary: OS-CTXS-40501 occurs when an agent harness calls the OutSystems Developer Cloud (ODC) Context Service with an HTTP method the resource doesn't support.
tags:
  - Agentic
  - AI
  - REST
  - Troubleshooting
guid: cc085543-16a6-4adf-baa9-c282f5bbfb91
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

# OS-CTXS-40501

## Error message

```
Method is not supported for this resource.
```

## Cause

The agent harness called an HTTP method that the Context Service doesn't support on the requested resource.

## Impact

The Context Service rejected the request before processing it.

## Recommended action

Report the error to the provider of your agent harness tooling. The plugin or Power that integrates with OutSystems is calling the wrong method on the Context Service. If you authored the tooling, review the Context Service API reference and align the request to the supported method.
