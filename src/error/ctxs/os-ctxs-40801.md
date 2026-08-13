---
summary: OS-CTXS-40801 occurs when a search in the OutSystems Developer Cloud (ODC) Context Service doesn't return in time. Wait a few seconds and retry.
tags:
  - Agentic
  - AI
  - Troubleshooting
guid: 1814655d-c528-428c-a352-42f909a6ed39
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

# OS-CTXS-40801

## Error message

```
Search not ready after all attempts.
```

## Cause

The Context Service search backend didn't respond within the retry budget. This can happen on the first query after an idle period while the search backend warms up.

## Impact

The search request returned no results.

## Recommended action

Wait a few seconds and send the same request again. If the issue continues after several minutes, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-CTXS-40801).
