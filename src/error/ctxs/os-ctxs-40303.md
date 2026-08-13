---
summary: OS-CTXS-40303 occurs when an agent harness queries the OutSystems Developer Cloud (ODC) Context Service for resources in a different tenant than its credentials.
tags:
  - Agentic
  - AI
  - Authentication
  - Multi-Tenant
  - Troubleshooting
guid: d1baef33-b93e-4395-842a-fbd350e0ae70
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

# OS-CTXS-40303

## Error message

```
Caller tenant does not match request tenant.
```

## Cause

The tenant in the authentication token doesn't match the tenant scope of the request. This happens when the agent harness is authenticated to one tenant but the request targets resources owned by a different tenant.

## Impact

The Context Service rejected the request without processing it.

## Recommended action

Verify that your agent harness is signed in to the same tenant that owns the resources you're querying. Sign in to the correct tenant and retry the request.
