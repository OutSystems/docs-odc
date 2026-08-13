---
summary: OS-CTXS-40401 occurs when the OutSystems Developer Cloud (ODC) Context Service can't find a resource that matches the request. Verify the identifier and retry.
tags:
  - Agentic
  - AI
  - Troubleshooting
guid: c39d9ba8-a237-4ca0-b25b-1c8000600798
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

# OS-CTXS-40401

## Error message

```
Resource not found.
```

## Cause

The Context Service couldn't find a resource that matches the request. Common reasons are a stale or incorrect identifier, a resource that lives in a different environment, or a resource that no longer exists.

## Impact

The Context Service returned no data for the request.

## Recommended action

Verify the resource identifier in your prompt. Confirm the resource exists in the environment you're targeting. If the identifier is correct and the resource exists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-CTXS-40401).
