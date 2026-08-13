---
summary: Reference for OutSystems Developer Cloud (ODC) agent connection errors (OS-ABRS) that surface when you test or run a connection to an MCP server or an external agent (A2A).
tags:
  - AI
  - Agentic
  - MCP
  - Troubleshooting
guid: a21b483d-d8d4-4857-962c-75b6b1c0bdaa
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
audience:
  - Developer
  - Tech lead
outsystems-tools:
  - odc portal
coverage-type:
  - remember
  - unblock
isautopublish: true
---

# AI agent connection errors

The OS-ABRS error family covers failures in the ODC service that runs connections between AI agents and external capabilities. Those connections include Model Context Protocol (MCP) servers and agent-to-agent (A2A) endpoints. The errors surface in ODC Portal under **Integrate** > **Connections**, most often when you select **Test connection**.

In the error code, the `CONN` segment identifies a connection error. The numeric suffix maps to a specific failure, ranging from invalid input on your side to an unexpected failure inside the service.

For the features these errors apply to, refer to [Use MCP servers](../../eap/building-apps/build-ai-powered-apps/tools/mcp-connectors.md) and [Adding external agents in the ODC Portal using A2A](../../eap/building-apps/build-ai-powered-apps/agent-2-agent/using-agent-2-agent.md).

## Using the error code

Use the error code to locate the matching page. Each page documents the error message, the cause, the impact on the operation, and the recommended action. When the action is to contact OutSystems Support, include the exact error code.
