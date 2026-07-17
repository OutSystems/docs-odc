---
summary: Coding agents in OutSystems Developer Cloud (ODC) Mentor interpret intent, plan work, and apply changes to the OutSystems Model with you in control.
tags:
  - Agentic
  - AI
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

# Coding agents

Mentor builds and modifies OutSystems assets through conversation. Assets include reactive web apps and libraries. Behind that conversation are coding agents that interpret your intent, plan the work, and apply changes. This page explains what the agents are, how they work, and how you stay in control. You use Mentor in two places: Mentor Web to create apps in ODC Portal, and Mentor Studio to modify assets in ODC Studio.

## The agents behind Mentor

Agentic development uses coding agents that work together behind a single conversation. You talk to one assistant, and the agents coordinate the work. Each agent handles a different kind of work.

* **Building and modifying your asset.** One agent works on the OutSystems Model rather than raw code, reading the current structure, planning the changes, and applying them. It leads the conversation from your first prompt through to the applied result.
* **Planning the app structure.** When you create a new app in Mentor Web, one agent first scopes the work into a blueprint of entities, screens, roles, and the rest of the app structure. You review the blueprint, then other agents build from it.

For most requests you interact with one assistant. Direct edits, such as adding an attribute to an entity, are applied without a separate planning step. In Mentor Web, creating a new app produces a blueprint first, so you review the shape of the app before it's built. For the blueprint, refer to [Blueprint](mentor-web/blueprint.md).

## How the agents work

The coding agents work through a loop of four steps: gather context, plan, act, and verify. They follow these steps for most requests. For a simple change, they sometimes skip explicit context-gathering or planning. Knowing this loop helps you write better prompts and see where to guide the outcome.

1. **Gather context.** The agents read the OutSystems Model of the asset you're working on. They also read its logic, data model, dependencies, and integrations. This is part of the Enterprise Context Graph, which includes public elements from other assets in your tenant. For the components involved, refer to [Architecture](architecture.md).
1. **Plan.** The agents interpret your intent and decide how to proceed. For a complex change, Mentor proposes a plan for you to review before it does the work. For a straightforward change, it proceeds directly.
1. **Act.** The agents apply the changes to the model and show you what changed.
1. **Verify.** You review what changed, and the OutSystems compiler enforces the same standards applied to every OutSystems asset when it's published.

## The model the agents work on

The coding agents work on the OutSystems Model, the high-level representation of an asset's structure and behavior. They work with model elements rather than raw code, apart from elements that hold code by nature, such as CSS or JavaScript.

To understand your asset, the agents query the model. They render the underlying code for the parts that matter to a request, such as a single action or an entity and its attributes. To change your asset, they modify the model. The OutSystems compiler turns that model into deployable code when you publish. ODC Studio works with the same model, so assets built or modified through agentic development are standard OutSystems assets. For how the model, the agents, and the compiler fit together, refer to [Architecture](architecture.md).

## The context the agents use

The coding agents work with the context of the asset you have open and its relationships to the rest of your tenant. This context grounds their interpretation of your prompts and lets them reuse what already exists.

* **The open asset.** The agents read the structure, logic, data model, dependencies, and integrations of the asset you're working on.
* **Referenced assets.** The agents recognize the public elements that other assets expose, such as entities and actions, so they reuse existing assets instead of recreating them. For background, refer to [Reuse elements across apps](../app-architecture/reuse-elements.md).
* **Tenant context.** A populated development environment improves results, because the agents reference existing entities, actions, and patterns when they generate new elements.

A clear, explicit prompt combined with relevant context produces more accurate results than a vague description. For prompting strategies, refer to [Effective prompts for Mentor](effective-prompts.md).

## Planning and your control

You stay in control of every change. Mentor asks you to accept a structural proposal before it builds, applies smaller changes directly, and lets you review the result before you continue.

* **Plan when it matters.** Mentor proposes a plan for complex changes, such as those that span multiple elements. It applies a simple, self-contained change directly. For how to read and act on a plan in Mentor Studio, refer to [Review and accept the plan](mentor-studio/how-it-works.md#review-and-accept-the-plan).
* **Clarify at decision points.** The agents use reasonable defaults and state their assumptions. They ask a clarifying question only when a wrong guess would cause significant rework or change the architecture.
* **Review and accept.** For structural changes, Mentor proposes a blueprint (Mentor Web) or a plan (Mentor Studio). You accept, reject, or refine before Mentor builds. Mentor applies smaller changes without a separate step. You review the result afterward.
* **Review the result.** After the agents apply changes, you compare your asset before and after to confirm the outcome. For the comparison view, refer to [Review changes](mentor-studio/how-it-works.md#review-changes).

## How output quality is maintained

Assets created or modified through agentic development meet the same standards as assets built by hand. Quality is enforced at the platform level and measured continuously.

* **Same platform standards as hand-built assets.** Because the agents work on the OutSystems Model, the platform applies the same security, performance, and architecture standards for every asset. AI-built assets run with the same rules as any other OutSystems asset, including data encryption and input validation. Review the roles and permissions the agents set to confirm they match your intent.
* **Continuous evaluation.** OutSystems evaluates the coding agents using benchmarks for the quality and accuracy of their output, the reliability of their results, and their efficiency. These benchmarks track improvements across releases.

For the safeguards that protect agentic development, including data privacy, guardrails, and governance, refer to [Security and safeguards](security-safeguards.md).

## What the coding agents can and can't do

The coding agents handle common app patterns, and their reach depends on which tool you use. Understanding this helps you set realistic expectations and plan your development approach.

The agents generate data models, screens with standard UI patterns, roles and entity-level authorization, and basic logic and navigation. When you work on an existing asset, they also explain elements and suggest fixes. For the patterns each tool supports, refer to [Capabilities and patterns for Mentor Web](mentor-web/capabilities.md) and [Capabilities and patterns for Mentor Studio](mentor-studio/capabilities.md).

Mentor Web focuses on common app patterns. Mentor Studio works in the full development environment and handles more complexity. When a task goes beyond what the agents can do, you finish it in ODC Studio. These limits expand as agentic development matures. For which tool fits your work, refer to [When to use each tool](intro.md#when-to-use-each-tool). For current constraints, refer to [Known limitations](ai-limitations.md).

## Related resources

The coding agents support Mentor across the development lifecycle. The following resources cover the architecture, the workflows, and the prompting techniques that work with the agents.

* For the components that underpin agentic development, including the OutSystems Model and the Enterprise Context Graph, refer to [Architecture](architecture.md).
* For creating apps with the agents in Mentor Web, refer to [How AI app generation works](mentor-web/how-it-works.md).
* For modifying assets with the agents in Mentor Studio, refer to [AI development in Mentor Studio](mentor-studio/how-it-works.md).
* For the conceptual shift to prompt-based development, refer to [Thinking with AI](thinking-with-ai.md).
* For prompting strategies that apply across all Mentor tools, refer to [Effective prompts for Mentor](effective-prompts.md).
