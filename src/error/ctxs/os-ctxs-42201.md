---
summary: OS-CTXS-42201 occurs when the OutSystems Developer Cloud (ODC) Context Service can't process the input in an otherwise valid request. Refine the input and retry.
tags:
  - Agentic
  - AI
  - Troubleshooting
guid: 3dd60932-eaae-4259-bdf4-4ba55a06a8ee
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
audience:
  - Developer
outsystems-tools:
  - none
coverage-type:
  - unblock
isautopublish: true
---

# OS-CTXS-42201

## Error message

```
Failed to process input data.
```

## Cause

The Context Service received a well-formed request but couldn't process the input it contained. Common reasons are malformed search input, unsupported query syntax, or input that exceeds size limits.

## Impact

The Context Service didn't process the request and returned no data.

## Recommended action

Refine the prompt or query you sent to the agent. Shorter, more specific queries are more likely to succeed. If the input looks valid, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-CTXS-42201).
