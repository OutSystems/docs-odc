---
summary: OS-AISA-40005 occurs in OutSystems Developer Cloud (ODC) when Mentor can't retrieve the application state at the start of a conversation. Try the request again.
tags:
  - Mentor
  - Mentor Studio
  - Troubleshooting
guid: 7d848247-a59c-40f6-a388-b484ff49a869
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

# OS-AISA-40005

## Error message

```
Problem retrieving application state. If the issue persists please open a support ticket.
```

## Cause

Mentor couldn't retrieve the current state of the application. This is an app-dependent issue that occurs when loading the application at the start of a conversation.

## Impact

Mentor can't process the request because it doesn't have access to the app's current state.

## Recommended action

Try the request again. If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-AISA-40005).
