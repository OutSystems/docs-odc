---
summary: A workflow-oriented index of the tools the agent in your MCP host uses with OutSystems, grouped by task and cross-linked to the relevant concepts and tutorials.
tags: tool reference, mcp tools, mcp host, agentic development
guid: a76b6c8f-15b1-4080-a049-4c297ef8c92c
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - claude code
coverage-type:
  - remember
content-type:
  - reference
audience:
  - Developer
topic:
  - creating-apps
isautopublish: true
---

# Tool reference

This page groups the tools that the agent in your MCP host uses with OutSystems MCP by the workflow they support. For each tool's parameters and behavior, refer to the tool list in your MCP host and the OutSystems skill.

## Tool catalog and service sets {#how-to-read-this-reference}

The OutSystems MCP server publishes the authoritative tool catalog, and your MCP host shows it in its tool list. This page groups that catalog into the three service sets, Context, Mentor, and Platform, so you know which tool to use, and in what order. For more information about the service sets in the platform architecture, refer to [OutSystems MCP request architecture](architecture.md).

* The live tool list is the source of truth for names. The exact set and the tool names change between releases and vary by tenant, so read the tool list in your MCP host before you rely on a specific name.
* This page covers the remote MCP surface only.

## Operations that change tenant state

The OutSystems tool descriptions instruct the agent to restate the operation and wait for your confirmation before it publishes, deploys, or rolls back. Reads, searches, and edits within a Mentor session run immediately. For more information about how confirmation works and why you confirm against a canonical identifier, refer to [Governance in OutSystems MCP](governance.md#confirming-state-changing-operations).

## Context Services

Use these read-only tools to query your application estate before you change anything.

* **App lookups:** List the tenant's assets, read one app's details, list an app's references to other modules and libraries, and read an app's revision history.
* **Context lookups:** Typed reads over the Enterprise Context Graph, one per object kind, for entities, actions, screens, structures, roles, themes, connections, and AI agents. A cross-type search spans object kinds in one query.

For more information about how the graph is built and its freshness limits, refer to [Enterprise Context Graph](../context-graph.md). For the app introspection workflow, refer to [Inspect apps and their dependencies](introspect-app.md).

## Mentor Services

Use these tools to create an app or delegate a change to Mentor, which edits the app model on the server inside a session.

* Start a session on an app, or create a new app from a template or from an existing app within a session.
* Send a prompt to run an edit turn, poll the run until it finishes, and cancel a turn.
* Publish the session's edits, and close the session when the work is done.

Mentor runs as a session that holds the loaded app model. A session holds one app and runs one turn at a time. For more information about delegation and sessions, refer to [Delegation to Mentor](mentor-delegation.md).

## Platform Services

Use these tools to publish, deploy, manage, and monitor assets. These operations run under the same role permissions as ODC Portal.

* **Publish:** Track a publish's status and read its build messages. A publish starts from a Mentor session. For more information, refer to [Delegation to Mentor](mentor-delegation.md).
* **Deploy:** Promote a build across stages, roll back, list deployments, and read a deployment's status and messages. Run a deployment-impact analysis and track it.
* **External libraries:** Upload, publish, and delete a .NET library, inspect its contents, read its status and logs, and download its source.
* **Environments:** List your tenant's stages and their keys, and read one stage's details and its deployed apps.
* **Observability:** Read an app's runtime logs and traces, read health metrics for one or more apps, and read one stage's health rollup. Health reads require the stage key, which the tools call `env_key`.

For the full publish and deploy workflow, refer to [Evolve an existing app](evolve-app.md). For external libraries, refer to [Extend an app with custom C# code](extend-with-csharp.md). For monitoring in ODC Portal, refer to [Monitoring and troubleshooting apps](../../monitor-and-troubleshoot/monitor-apps.md).
