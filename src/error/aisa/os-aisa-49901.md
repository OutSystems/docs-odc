---
summary: OS-AISA-49901 occurs in OutSystems Developer Cloud (ODC) when a Mentor conversation is cancelled mid-response. Start a new conversation to retry.
tags:
  - Mentor
  - Mentor Studio
  - Troubleshooting
guid: 725f0f49-5fa4-4558-a9ed-c41f7dd0db16
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

# OS-AISA-49901

## Error message

```
Conversation was cancelled.
```

## Cause

Mentor cancelled the conversation before finishing the request. This happens when you close the chat window or navigate away while Mentor is still responding.

## Impact

The current request wasn't processed. No changes were applied to the app.

## Recommended action

Start a new conversation and resend the request.
