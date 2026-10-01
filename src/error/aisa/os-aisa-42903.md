---
summary: OS-AISA-42903 occurs in OutSystems Developer Cloud (ODC) when the organization reaches the daily usage limit for Mentor. Wait until the limit resets, or contact Support to confirm your limit.
tags:
  - Mentor
  - Troubleshooting
guid: a77505a8-44b6-45a2-9ada-b32758d2d367
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
audience:
  - Developer
outsystems-tools:
  - mentor studio
coverage-type:
  - unblock
isautopublish: true
---

# OS-AISA-42903

## Error message

```
Mentor is currently unavailable due to reached usage limits. Limit resets in <reset_time>.
```

## Cause

Your organization has reached the daily usage limit for Mentor. The limit is a daily quota that applies to the whole organization.

## Impact

Mentor is unavailable for all users in the organization until the limit resets.

## Recommended action

Wait until the reset time shown in the error message, and then try again.

To understand how the limit works:

* The limit applies to the organization as a whole, not to individual users.
* The quota resets once a day. The error message shows the time remaining until the reset.
* The error message doesn't display the numeric limit.
* To confirm the limit that applies to your organization, check your organization's plan details or contact your OutSystems account team.

If you keep seeing this error after the reset time has passed, contact OutSystems Support.
