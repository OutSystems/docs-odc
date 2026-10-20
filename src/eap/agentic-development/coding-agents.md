---
summary: Mentor in OutSystems Developer Cloud (ODC) interprets your intent, plans the work, and applies changes to the OutSystems Model with you in control.
tags:
  - Agentic
  - AI
  - Architecture
  - Development lifecycle
  - Mentor
  - Mentor Studio
  - Mentor Web
guid: b2010a27-fe8b-44f8-b052-bb598f73c29d
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - portal
  - odc studio
  - mentor web
  - mentor studio
coverage-type:
  - understand
audience:
  - Architect
  - Developer
  - Tech lead
topic:
  - creating-apps
isautopublish: true
---

# Mentor

Mentor builds and modifies OutSystems assets through conversation. For the asset types Mentor builds, refer to the scope in [Capabilities and patterns for Mentor Studio](mentor-studio/capabilities.md#scope) and [Capabilities and patterns for Mentor Web](mentor-web/capabilities.md). Mentor interprets your intent, plans the work, and applies the changes. This page explains what Mentor is, how it works, and how you stay in control.

You use Mentor through three paths. Mentor Web creates apps in ODC Portal, and Mentor Studio modifies assets in ODC Studio. With OutSystems MCP, the agent in your MCP host, such as Claude Code or Cursor, delegates app changes to Mentor. For how that delegation works, refer to [Delegation to Mentor](outsystems-mcp/mentor-delegation.md).

## Mentor's agents

Mentor comprises several agents, each performing a different part of a request. You send prompts through a single conversation, and the agents coordinate internally. Mentor's agents are separate from the agent in an MCP host and from the AI agents you build into apps. For each meaning, refer to [Context-dependent terms](agentic-development-terminology.md#context-dependent-terms).

* **Building and modifying your asset.** One agent operates on the OutSystems Model, reading the current structure, planning the changes, and applying them. This agent processes the request from your first prompt to the applied result.
* **Planning the app structure.** When you create a new app in Mentor Web, one agent first generates a blueprint of entities, screens, roles, and the remaining app structure. You review the blueprint, then other agents build from it.

For most requests, you interact with Mentor through a single conversation. Direct edits, such as adding an attribute to an entity, are applied without a separate planning step. In Mentor Web, creating a new app produces a blueprint first, so you review the structure of the app before Mentor builds it. For the blueprint, refer to [Blueprint](mentor-web/blueprint.md).

## The working loop

Mentor processes a request in four steps: gather context, plan, act, and verify. It applies these steps to most requests. For a self-contained change, it sometimes skips explicit context-gathering or planning. Knowing these steps shows you where your prompt influences the outcome.

1. **Gather context.** Mentor reads the OutSystems Model of the asset you're working on. It also reads its logic, data model, dependencies, and integrations, using the Enterprise Context Graph, which indexes your tenant's estate, including public elements from other assets. For the graph, refer to [Enterprise Context Graph](context-graph.md). For the components involved, refer to [Architecture](architecture.md).
1. **Plan.** Mentor interprets your intent and selects an approach. For a complex change, Mentor proposes a plan for you to review before it does the work. For a straightforward change, it proceeds directly.
1. **Act.** Mentor applies the changes to the model and displays what changed.
1. **Verify.** You review what changed, and the OutSystems compiler enforces the same standards applied to every OutSystems asset when it's published. For the checks you apply when you review, refer to [Review checks](odc-ai-and-platform.md#review-checks).

## The model Mentor works on

Mentor works on the OutSystems Model, the high-level representation of an asset's structure and behavior. It works with model elements, except for elements that contain code, such as CSS or JavaScript.

To read your asset's structure, Mentor queries the model. It renders the underlying code for the parts a request affects, such as a single action or an entity and its attributes. To change your asset, it modifies the model. The OutSystems compiler turns that model into deployable code when you publish. ODC Studio works with the same model, so assets built or modified through agentic development are standard OutSystems assets. For how the model, Mentor, and the compiler fit together, refer to [Architecture](architecture.md).

## The context Mentor uses

Mentor uses the context of the asset you have open and its relationships to the rest of your tenant. Mentor applies this context to interpret your prompts and to reuse existing elements.

* **The open asset.** Mentor reads the structure, logic, data model, dependencies, and integrations of the asset you're working on.
* **Referenced assets.** Mentor reads the public elements that other assets expose, such as entities and actions, and reuses them. For background, refer to [Reuse elements across apps](../app-architecture/reuse-elements.md).
* **Tenant context.** A populated Development stage improves results, because Mentor references existing entities, actions, and patterns when it generates new elements.

A clear, explicit prompt combined with relevant context produces more accurate results than a vague description. For prompting strategies, refer to [Effective prompts for Mentor](effective-prompts.md).

## Your control over changes

You stay in control of every change. Mentor prompts you to accept a structural proposal before it builds, applies smaller changes directly, and returns the result for you to review before you continue.

* **Plan when it matters.** Mentor proposes a plan for complex changes, such as those that span multiple elements. It applies a simple, self-contained change directly. For how to read and act on a plan in Mentor Studio, refer to [Review and accept the plan](mentor-studio/how-it-works.md#accept-plan).
* **Clarify at decision points.** The agents use reasonable defaults and state their assumptions. They ask a clarifying question only when a wrong guess would cause significant rework or change the architecture.
* **Review and accept.** For structural changes, Mentor proposes a blueprint (Mentor Web) or a plan (Mentor Studio). For a blueprint, you refine it through follow-up prompts until it matches your intent. For a plan, you proceed, review the changes first, or discard it. Mentor applies smaller changes without a separate step. You review the result afterward.
* **Review the result.** After the agents apply changes, you compare your asset before and after to confirm the outcome. For the comparison view, refer to [Review changes](mentor-studio/how-it-works.md#review-changes).

## Output quality

Because Mentor works on the OutSystems Model, the platform applies the same standards to its output as to any OutSystems asset. Review the roles and permissions Mentor sets to confirm they match your intent. For what the platform guarantees regardless of origin, refer to [Platform guarantees and AI interpretation](odc-ai-and-platform.md).

OutSystems measures Mentor's quality continuously, using benchmarks for the accuracy of its output, the reliability of its results, and its efficiency. These benchmarks track improvements across releases.

For the safeguards that protect agentic development, including data privacy, guardrails, and governance, refer to [Security and safeguards](security-safeguards.md).

## Scope and limits

Mentor supports common app patterns, and the supported range depends on which tool you use. Knowing these limits helps you plan your development approach.

Mentor generates data models, screens with standard UI patterns, roles and entity-level authorization, and basic logic and navigation. When you work on an existing asset, it also explains elements and suggests fixes. For the patterns each tool supports, refer to [Capabilities and patterns for Mentor Web](mentor-web/capabilities.md) and [Capabilities and patterns for Mentor Studio](mentor-studio/capabilities.md).

Mentor Web supports common app patterns. Mentor Studio works in the full development environment and supports more complex changes. When a task exceeds what Mentor supports, you finish it in ODC Studio. These limits expand across releases. For the constraints, refer to [Known limitations](ai-limitations.md).

## Related resources

Mentor supports development across the lifecycle. The following resources cover the architecture, the workflows, and the prompting techniques that work with Mentor.

* For the components that underpin agentic development, including the OutSystems Model, refer to [Architecture](architecture.md). For the tenant index Mentor reads, refer to [Enterprise Context Graph](context-graph.md).
* For creating apps in Mentor Web, refer to [AI app generation in Mentor Web](mentor-web/how-it-works.md).
* For modifying assets in Mentor Studio, refer to [AI development in Mentor Studio](mentor-studio/how-it-works.md).
* For the conceptual shift to prompt-based development, refer to [Thinking with AI](thinking-with-ai.md).
* For prompting strategies that apply across all Mentor tools, refer to [Effective prompts for Mentor](effective-prompts.md).
