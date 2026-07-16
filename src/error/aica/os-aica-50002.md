---
summary: OS-AICA-50002 occurs in OutSystems Developer Cloud (ODC) Mentor Web when the AI Provider service returns a temporary error. Wait and retry.
tags:
  - Agentic
  - AI
  - Mentor
  - Mentor Web
  - Troubleshooting
guid: 8aa7aded-facf-4203-ab07-7346be996992
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - mentor web
coverage-type:
  - unblock
isautopublish: true
---

# OS-AICA-50002

## Error message

```
There was a problem with the AI provider service.
```

## Cause

The AI provider service that powers Mentor Web returned a low-level error.

## Impact

Mentor Web can't complete the current request.

## Recommended action

Wait a few minutes and try again. If the error persists, try a different prompt. If the problem continues, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-AICA-50002).
