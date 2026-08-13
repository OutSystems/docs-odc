---
summary: OS-CTXS-40301 occurs in the OutSystems Developer Cloud (ODC) Context Service when the authenticated user lacks the permissions required for the request.
tags:
  - Authorization
  - Troubleshooting
guid: 14ceed8e-185b-4024-99fb-063d84513893
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
audience:
  - Developer
  - Platform administrator
outsystems-tools:
  - none
coverage-type:
  - unblock
isautopublish: true
---

# OS-CTXS-40301

## Error message

```
Caller lacks permission.
```

## Cause

The authenticated account doesn't have the permissions required to perform the requested operation on the Context Service.

## Impact

The request didn't proceed and no data was returned.

## Recommended action

Ask your OutSystems administrator to grant your account the permissions required to query the Context Service for the targeted resources. If you already hold those permissions, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-CTXS-40301).
