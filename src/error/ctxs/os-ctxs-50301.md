---
summary: OS-CTXS-50301 occurs when the OutSystems Developer Cloud (ODC) Context Service isn't ready to handle requests. Wait a few minutes and retry.
tags:
  - Troubleshooting
guid: 65b7efe5-b51d-4610-9ccc-b5de92c162e7
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

# OS-CTXS-50301

## Error message

```
Service is not ready to handle requests.
```

## Cause

The Context Service isn't ready to handle requests. Common reasons are startup, scaling, or a temporary outage.

## Impact

No requests complete until the service returns to a ready state.

## Recommended action

Wait a few minutes and try again. If the issue continues, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-CTXS-50301).
