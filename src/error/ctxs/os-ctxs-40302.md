---
summary: OS-CTXS-40302 occurs when an upstream authorization check denies a request to the OutSystems Developer Cloud (ODC) Context Service. Contact Support.
tags:
  - Authorization
  - Troubleshooting
guid: 619ff696-e37a-47fd-b359-99b94efcdb31
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

# OS-CTXS-40302

## Error message

```
Claims Agent Service denied access.
```

## Cause

An upstream authorization check denied access for the current request. This is a service-level decision, not a user-level permission check.

## Impact

The Context Service rejected the request without processing it.

## Recommended action

Create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-CTXS-40302) and include the error code.
