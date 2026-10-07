---
summary: OS-CTXS-40303 occurs when an ODC Context Service query uses credentials for one tenant but targets resources in another tenant.
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
topic:
  - context-service-errors
isautopublish: true
---

# OS-CTXS-40303

## Error message

```
Caller tenant does not match request tenant.
```

## Cause

The tenant in the authentication token doesn't match the tenant scope of the request. Your MCP host is the AI application you work in, such as Claude Code, Cursor, or AWS Kiro. This error happens when your MCP host is signed in to one tenant but the request targets resources owned by a different tenant.

## Impact

The Context Service rejected the request without processing it.

## Recommended action

Verify that your MCP host is signed in to the same tenant that owns the resources you're querying. Sign in to the correct tenant and retry the request.
