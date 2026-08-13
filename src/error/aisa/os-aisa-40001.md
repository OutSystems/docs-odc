---
summary: OS-AISA-40001 in OutSystems Developer Cloud (ODC) Mentor occurs when the AI context limit is reached. Start a new conversation to continue.
tags:
  - AI
  - Mentor
  - Mentor Studio
  - Troubleshooting
guid: cb54ee6d-2e3c-4513-b254-2e8ddd7a7133
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

# OS-AISA-40001

## Error message

```
The maximum length for this conversation was reached. You can start a new conversation, but current progress will be lost.
```

## Cause

The conversation with Mentor exceeded the maximum context length supported by the underlying AI model. Working with large applications or long conversations increases the chance of reaching this limit.

## Impact

Mentor can't process additional prompts in the current conversation.

## Recommended action

Start a new conversation. To avoid reaching the context limit, break complex requests into smaller, focused prompts and start new conversations between unrelated tasks.
