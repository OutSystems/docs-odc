---
summary: OS-CTXS-40001 occurs when a request to the OutSystems Developer Cloud (ODC) Context Service, made for the agent in an MCP host, doesn't match the API contract.
tags:
  - Agentic
  - Troubleshooting
guid: 85b2344d-4186-42ae-9846-4d63a0fccdae
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

# OS-CTXS-40001

## Error message

```
Request does not follow agreed upon contract.
```

## Cause

The Context Service received a request that doesn't match its request contract. Your MCP host is the AI application you work in, such as Claude Code, Cursor, or AWS Kiro. The OutSystems MCP server sends these requests when the agent in your MCP host calls a context tool. The most common reason is a mismatch between the version of the OutSystems plugin or Power in your MCP host and the Context Service API.

## Impact

The Context Service rejected the request without processing it.

## Recommended action

Update the OutSystems integration in your MCP host and retry. In Claude Code, Claude Desktop, and the Cursor app, update the OutSystems plugin. In AWS Kiro, update the OutSystems Power, the package you install from the Kiro Powers panel. In the Cursor CLI and GitHub Copilot, replace the saved OutSystems skill file with the current version. If the error continues, report it to the provider of the tooling that calls the Context Service, with the request details. If the problem persists, create a case with [OutSystems Support](https://www.outsystems.com/support/portal/open-support-case?ErrorCode=OS-CTXS-40001).
