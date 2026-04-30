---
summary: OS-AISA-42902 occurs in OutSystems Developer Cloud (ODC) Mentor when the tenant exceeds the per-minute rate limit on the AI Provider service. Wait and retry.
tags:
  - AI
  - Mentor
  - Mentor Studio
  - Troubleshooting
guid: 14abb427-1dd9-45a6-a906-7fa061e55363
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - mentor studio
coverage-type:
  - unblock
isautopublish: true
---

# OS-AISA-42902

## Error message

```
Too many requests per minute for this tenant.
```

## Cause

The organization exceeded the maximum number of requests per minute allowed for the AI Provider service.

## Impact

Mentor can't process requests until the per-minute rate limit resets.

## Recommended action

Wait a few minutes before sending another request. If multiple team members use Mentor at the same time, coordinate usage to stay within the rate limit.
