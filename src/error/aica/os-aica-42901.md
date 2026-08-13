---
summary: OS-AICA-42901 occurs in OutSystems Developer Cloud (ODC) Mentor Web when requests to the LLM Gateway exceed the allowed rate. Wait and retry.
tags:
  - Agentic
  - AI
  - Mentor
  - Mentor Web
  - Troubleshooting
guid: aa105e87-5322-40dd-a6b4-f7118b734c27
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

# OS-AICA-42901

## Error message

```
There were too many requests to the LLM Gateway.
```

## Cause

The number of requests sent to the LLM Gateway exceeded the defined rate limits, either for your tenant or due to global capacity constraints on the underlying AI provider.

## Impact

Mentor Web can't process the request until the rate limit resets.

## Recommended action

Wait a few minutes before sending another request. Large prompts consume more tokens and can reach the limit faster, so simplify the prompt if the error recurs.
