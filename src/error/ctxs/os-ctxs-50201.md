---
summary: OS-CTXS-50201 occurs when the OutSystems Developer Cloud (ODC) Context Service gets an invalid response from an upstream dependency. Retry or contact Support.
tags:
  - Troubleshooting
guid: 8d986915-eb60-44dc-afc6-df8494642e7b
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

# OS-CTXS-50201

## Error message

```
Service received an invalid response from upstream server or database.
```

## Cause

The Context Service received an invalid response from one of its upstream dependencies.

## Impact

The request didn't complete.

## Recommended action

Wait a few seconds and send the same request again. If the issue continues, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-CTXS-50201).
