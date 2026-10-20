---
summary: How OutSystems governs OutSystems MCP operations from your MCP host, covering per-request identity and permissions, confirmation before state changes, and data residency.
tags: governance, security, outsystems mcp, mcp host, agentic development
guid: 21776eb4-8b22-4ab7-9936-62a3d64b9337
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - claude code
coverage-type:
  - understand
  - evaluate
content-type:
  - conceptual
audience:
  - Architect
  - Tech lead
  - Platform administrator
topic:
  - creating-apps
isautopublish: true
---

# Governance in OutSystems MCP

With OutSystems MCP, every operation runs under the same governance as operations from ODC Portal or ODC Studio. The same policies and roles apply. This page separates what OutSystems enforces on every request from what the agent is instructed to do. It also covers where your data goes. For more information about the platform guarantee that the same governance applies to every request origin, refer to [Platform guarantees and AI interpretation](../odc-ai-and-platform.md#platform-guarantees). For more information about who can use Mentor and how access is granted, refer to [Agentic development in the SDLC](../sdlc.md).

## Identity and access

Every operation runs under your own identity. You sign in to your tenant as your ODC user, each tool call carries your OAuth bearer token, and OutSystems authorizes the operation against that user's roles. An operation requires the same role permissions as the equivalent action in ODC Portal. If you lack the permission, the operation fails the same way it fails in ODC Portal. OutSystems enforces these checks on every tool call, whichever agent or MCP host sends it.

## Confirmation of state-changing operations {#confirming-state-changing-operations}

Confirmation before a change is an instruction that the agent follows. OutSystems enforces your roles on the operation itself, and the confirmation step depends on the agent and your MCP host. The instructions come from the following sources:

* **OutSystems tool descriptions:** The descriptions of the publish, deploy, and rollback tools instruct the agent to restate the operation and wait for your confirmation. Every agent connected to the OutSystems MCP server receives these descriptions.
* **OutSystems skill:** The skill extends the confirmation to creating an app and to uploading, publishing, or deleting an external library. It also sets the order of operations, such as publishing a data model before building screens. The agent receives these instructions only when your MCP host loads the OutSystems skill. For installation steps, refer to [Connect MCP hosts to OutSystems MCP](connect-mcp-hosts.md).
* **MCP host permission settings:** Your MCP host can ask you to approve a tool call before it runs, whatever the agent's instructions say.

Install the OutSystems skill with the OutSystems MCP server, so the agent receives the full set of instructions. To require a confirmation that doesn't depend on the agent, set your MCP host to ask you before it runs the OutSystems tools that change your tenant.

Inspecting an app, searching the context graph, and editing within a Mentor session run immediately. A deployment-impact analysis leaves your apps unchanged, and your MCP host or the agent can still ask you to confirm before the analysis starts. A general "go ahead" earlier in a session applies only to that point in the conversation. Confirm each new operation against its canonical identifier, which is an asset key, a stage key, or an operation key. Names are editable and can collide.

## Data residency

The OutSystems MCP server, the Enterprise Context Graph, and the lifecycle operations run on OutSystems infrastructure and apply your tenant's access controls. The large language model (LLM) that the agent runs on receives only the context the agent sends it while it processes your prompts. In a security review, treat the context the agent sends to its LLM as the data that leaves OutSystems.
