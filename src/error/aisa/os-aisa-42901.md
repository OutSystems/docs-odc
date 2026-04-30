---
summary: OS-AISA-42901 occurs in OutSystems Developer Cloud (ODC) Mentor when requests to the AI Provider service exceed the allowed rate. Wait and retry.
tags:
  - Agentic
  - AI
  - Mentor
  - Mentor Studio
  - Troubleshooting
guid: e2569b59-1a7f-49ed-bb84-ce9dc9cad9d3
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

# OS-AISA-42901

## Error message

```
Too many requests to LLM Gateway.
```

## Cause

The number of requests sent to the AI Provider service exceeded the allowed rate.

## Impact

Mentor can't process the request until the rate limit resets.

## Recommended action

Wait a few minutes before sending another request.
