---
summary: OS-AISA-50002 occurs in OutSystems Developer Cloud (ODC) when the AI Provider service powering Mentor has a temporary problem. Wait and retry.
tags:
  - AI
  - Mentor
  - Mentor Studio
  - Troubleshooting
guid: 34a13e9b-8bee-4478-a2f1-bdc3e50798c3
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

# OS-AISA-50002

## Error message

```
Problem with the AI Provider service, please try again in a few minutes. If the issue persists please open a support ticket.
```

## Cause

The AI Provider service that powers Mentor experienced a temporary problem.

## Impact

Mentor can't process requests until the service recovers.

## Recommended action

Wait a few minutes and try again. If the error persists, try a different prompt. If the problem continues, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-AISA-50002).
