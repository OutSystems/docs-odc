---
summary: OS-CTXS-50302 occurs when the OutSystems Developer Cloud (ODC) Context Service can't reach an upstream service it needs to authorize requests. Wait and retry.
tags:
  - Authorization
  - Troubleshooting
guid: 8eb1ef8a-104a-4fe3-a7d8-fd030ec4eb2d
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

# OS-CTXS-50302

## Error message

```
Claims Agent Service is not reachable.
```

## Cause

The Context Service can't reach an upstream service it relies on to authorize each request. The dependency is temporarily unreachable.

## Impact

The Context Service can't authorize requests until the dependency becomes reachable.

## Recommended action

Wait a few minutes and try again. If the issue continues, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-CTXS-50302).
