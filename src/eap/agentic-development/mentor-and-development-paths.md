---
summary: Mentor paths in OutSystems Developer Cloud (ODC) compare Mentor Studio, Mentor Web, and OutSystems MCP, with shared models and review steps.
tags:
  - Agentic
  - AI
  - Mentor
  - Mentor Studio
  - Mentor Web
guid: 7acaf5bd-f584-46e5-98d5-aa1b11c43e36
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - portal
  - odc studio
  - mentor web
  - mentor studio
  - claude code
coverage-type:
  - understand
content-type:
  - conceptual
audience:
  - Developer
  - Architect
  - Tech lead
topic:
  - creating-apps
isautopublish: true
---

# Mentor and the development paths

Mentor is the OutSystems AI that builds and modifies OutSystems assets through conversation. You reach Mentor through one of the development paths: Mentor Studio in ODC Studio, Mentor Web in ODC Portal, or OutSystems MCP from your MCP host. If a page describes a path other than the one you use, this page explains which parts of the description still apply to the way you work.

Each path is a different way to reach the same Mentor. The path decides where you work and who sends your request to Mentor. Mentor does the same work in every path, and every path produces the same OutSystems Model.

## What Mentor does

Mentor turns a natural-language request into changes to an OutSystems asset. It combines general-purpose large language models with OutSystems-specific knowledge to map your request to OutSystems development patterns, such as entities, relationships, roles, and UI patterns.

For most requests, Mentor reads the context it needs, plans the change, and applies it to the OutSystems Model. You then review the result, and the OutSystems compiler applies the platform standards when you publish. Mentor works with model elements, except elements that contain code, such as CSS or JavaScript.

For more information about how Mentor works, refer to [Mentor](coding-agents.md).

## What every path shares

The following parts are the same whichever path you use:

* **The OutSystems Model:** Mentor changes the same OutSystems Model that ODC Studio and ODC Portal work on. Assets that Mentor creates or changes are standard OutSystems assets, and the OutSystems compiler turns the model into deployable code when you publish.
* **Platform standards and governance:** The compiler applies the same security, performance, and architecture standards to the app model, whichever path produced it. The same governance policies and roles apply to every path.
* **Tenant context:** Mentor reads the [Enterprise Context Graph](context-graph.md), an index of your tenant's apps, entities, actions, screens, and dependencies. Mentor uses it to reuse the public elements that other apps expose.
* **Probabilistic interpretation:** Mentor's interpretation of a request is probabilistic, so the same prompt can produce different results on repeated runs. You review what Mentor produces in every path.

For what the platform guarantees and what you review, refer to [Platform guarantees and AI interpretation](odc-ai-and-platform.md).

## How the paths differ

The paths differ in where you work, who sends prompts to Mentor, and what Mentor works on. The following table compares them. For more information about choosing a path, refer to [Development paths](intro.md#development-paths).

| Path | Where you work | Who sends prompts to Mentor | What Mentor works on |
| ---- | -------------- | --------------------------- | -------------------- |
| Mentor Studio | The Mentor panel in ODC Studio | You | The asset you have open, such as a web app, a library, or an agentic app |
| Mentor Web | ODC Portal | You | A new app, from a prompt or a requirements document |
| OutSystems MCP | Your MCP host, such as Claude Code or Cursor | The agent in your MCP host | An app that a Mentor session loads, such as an existing app or one that the agent creates from a template |

### Request flow in Mentor Studio

In Mentor Studio, you describe a change in the Mentor panel in ODC Studio. Mentor reads the element you select and the view you have open as context, and it changes the asset you have open. Each app keeps its own conversation.

For a complex request, Mentor proposes a plan before it applies the changes. You proceed with the plan, review the changes first, or discard it. Mentor applies simpler changes directly. After Mentor applies a change, the **Review changes** dialog compares your app before and after.

For more information, refer to [AI development in Mentor Studio](mentor-studio/how-it-works.md).

### Request flow in Mentor Web

In Mentor Web, you describe a new app in ODC Portal, as a prompt or a requirements document. Mentor interprets the input and shows a blueprint of the proposed entities, roles, and screens. You review the blueprint and refine it through prompts before Mentor generates anything.

After you approve the blueprint, Mentor generates the app and publishes it to the development stage. You refine the generated app with prompts in the editor, or you continue in ODC Studio when the app needs capabilities beyond Mentor Web.

For more information, refer to [AI app generation in Mentor Web](mentor-web/how-it-works.md).

### Request flow in OutSystems MCP

With OutSystems MCP, you describe the outcome you want to the agent in your MCP host. The agent reads your tenant's context, delegates app changes to Mentor, and runs the publish and deploy steps.

Mentor runs in a server-side Mentor session that holds one loaded app model. Mentor edits the model in the session and returns the result to the agent. The model stays on the server, and the agent inspects the app through context lookups. The edits become part of the app when the agent publishes them.

The OutSystems tool descriptions instruct the agent to restate publish, deploy, and rollback operations and wait for your confirmation. The agent in your MCP host is separate from Mentor's own agents. For each meaning of the word agent, refer to [Context-dependent terms](agentic-development-terminology.md#context-dependent-terms).

For more information, refer to [OutSystems MCP](outsystems-mcp/outsystems-mcp-overview.md) and [Delegation to Mentor](outsystems-mcp/mentor-delegation.md).

## Switching between paths

Every path works on the same OutSystems Model, so you can continue an app in a different path. Apps built through agentic development are standard OutSystems apps, and you can switch between prompts and manual development in ODC Studio at any time.

The following examples show how you continue an app across paths:

* An app that Mentor Web generates opens in ODC Studio, where you continue with Mentor Studio or manual development.
* A new Mentor session in OutSystems MCP loads the app's most recent revision, so it includes changes that others published from ODC Studio.

If someone publishes a newer revision after your session loads the app, Mentor reconciles the two revisions on the next publish. Mentor merges changes that don't overlap. When changes overlap, the agent reports the newer revision and asks you how to proceed. For more information, refer to [Concurrent changes to an app](outsystems-mcp/mentor-delegation.md#concurrent-changes-to-an-app).

## How the docs name Mentor

The docs use the name Mentor in a consistent way, so you can tell whether a statement applies to your path. The following list shows the naming patterns.

* **Mentor:** The name alone refers to the AI. On a page that covers every path, a statement about Mentor holds for every path. For example, "Mentor generates a data model, screens, and logic from a natural-language description" applies in every path. On a page about one path, such as a Mentor Studio page, the statement describes Mentor in that path.
* **Mentor Studio, Mentor Web, or OutSystems MCP:** A path name marks a statement that holds for that path only. For example, "You can also describe a data change to Mentor Studio in ODC Studio" applies to Mentor Studio.
* **Interface labels:** Labels appear as the product shows them, such as the **Mentor** icon in the ODC Studio toolbar.
* **Other capabilities:** Some capabilities name Mentor as the engine behind them, such as code quality analysis. For more information, refer to [Manage technical debt in ODC](../monitor-and-troubleshoot/manage-technical-debt/managing-tech-debt.md).

## Related resources

The following pages cover the paths and Mentor in more depth:

* [Agentic development](intro.md)
* [Mentor](coding-agents.md)
* [Delegation to Mentor](outsystems-mcp/mentor-delegation.md)
* [Agentic development terminology](agentic-development-terminology.md)
