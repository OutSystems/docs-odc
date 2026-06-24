---
summary: The coding agents behind Mentor interpret intent, plan work, and apply changes to the OutSystems Model while you stay in control of every change.
tags:
  - Agentic
  - AI
  - Architecture
  - Mentor
  - Mentor Studio
  - Mentor Web
guid: 67d3526b-8f47-4d4e-8f60-64d26ab357f6
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

Mentor builds and modifies OutSystems apps through conversation. Behind that conversation are coding agents that interpret your intent, plan the work, and apply changes to your app. This page explains what the agents are, the loop they follow, and how you stay in control of every change. The same agents power Mentor across ODC, including Mentor Web for creating apps in ODC Portal and Mentor Studio for modifying apps in ODC Studio.

## The agents behind Mentor

Agentic development uses coding agents that work together behind a single conversation. You talk to one assistant, and the agents coordinate the work. Each agent handles a different kind of work.

* **Building and modifying your app.** One agent works on the OutSystems Model rather than raw code, reading the current structure, planning the changes, and applying them. It leads the conversation from your first prompt through to the applied result.
* **Planning the app structure.** When you create a new app or request a major structural change, a planning agent scopes the work into a blueprint of entities, screens, roles, and the rest of the app structure. The conversation then builds from that blueprint.

For most requests you interact with one assistant. Direct edits, such as adding an attribute to an entity, are applied without a separate planning step. A new app or a major structural change produces a blueprint first, so you review the shape of the app before it's built. For the blueprint in Mentor Web, refer to [Blueprint](mentor-web/blueprint.md).

## How the agents work

The coding agents follow the same loop for every request: gather context, plan, act, and verify. Understanding this loop explains why explicit prompts produce better results and where you step in to guide the outcome.

1. **Gather context.** The agents read the OutSystems Model of the asset you're working on, along with a structured view of its logic, data model, dependencies, and integrations. This view is part of the Enterprise Context Graph, which also includes the public elements that other apps expose in your tenant. For the components involved, refer to [Architecture](architecture.md).
1. **Plan.** The agents interpret your intent and decide how to proceed. For a risky or hard-to-reverse change, Mentor presents a plan and waits for your approval. For a low-consequence, recoverable change, it proceeds directly.
1. **Act.** The agents apply the changes to the app model, working one asset at a time and reporting progress as each task completes.
1. **Verify.** You review what changed, and the OutSystems compiler enforces the same standards applied to every OutSystems app when the app is published.

## The model the agents work on

The coding agents work on the OutSystems Model, the high-level representation of an app's structure, data, logic, and UI. They don't generate raw code.

To understand your app, the agents query the model and render the underlying code for the parts that matter to a request, such as a single action or an entity and its attributes. To change your app, they modify the app model, and the OutSystems compiler translates that model into deployable code when you publish. This is the same model that ODC Studio works with, so apps built or modified through agentic development are standard OutSystems apps. For how the model, the agents, and the compiler fit together, refer to [Architecture](architecture.md).

## The context the agents use

The coding agents work with the context of the asset you have open and its relationships to the rest of your tenant. This context grounds their interpretation of your prompts and lets them reuse what already exists.

* **The open asset.** The agents read the structure, logic, data model, dependencies, and integrations of the asset you're working on.
* **Referenced assets.** The agents recognize the public elements that other apps expose, such as entities and actions, so they reuse existing assets instead of recreating them. For background, refer to [Reuse elements across apps](../app-architecture/reuse-elements.md).
* **Tenant context.** A populated development environment improves results, because the agents reference existing entities, actions, and patterns when they generate new elements.

A clear, explicit prompt combined with relevant context produces more accurate results than a vague description. For prompting strategies, refer to [Effective prompts for Mentor](effective-prompts.md).

## Planning and your control

You stay in control of every change. The coding agents propose work and apply it only after you decide to proceed, and you review the result before you continue.

* **Plan when it matters.** Mentor presents a plan for changes that carry risk, span multiple elements, or are hard to reverse. It applies a simple, recoverable change directly. For how to read and act on a plan in Mentor Studio, refer to [Review and accept the plan](mentor-studio/how-it-works.md#review-and-accept-the-plan).
* **Clarify at decision points.** The agents infer reasonable defaults rather than over-asking, and they state the assumptions they make. They ask a clarifying question when a wrong guess would cause significant rework or change the architecture.
* **Review and accept.** You accept the proposed changes, reject them, or refine your request through a follow-up prompt. Nothing is applied to your app until you accept.
* **Review the result.** After the agents apply changes, you compare your app before and after to confirm the outcome. For the comparison view, refer to [Review changes](mentor-studio/how-it-works.md#review-changes).

## How output quality is maintained

Apps created or modified through agentic development meet the same standards as apps built by hand. Quality is enforced at the platform level and measured continuously.

* **Same standards as hand-built apps.** Because the agents work on the OutSystems Model, the compiler applies the same security, performance, and architecture standards regardless of how the model was created. AI-generated apps receive the same enforcement, including role-based access, data encryption, and input validation, as any other OutSystems app.
* **Continuous evaluation.** OutSystems evaluates the coding agents against benchmarks for the quality and accuracy of their output, the reliability of their results, and their efficiency. These benchmarks track improvements across releases.

For how agentic development secures and handles your data, refer to [Security and data privacy](intro.md#security-and-data-privacy).

## What the coding agents can and can't do

The coding agents handle common app patterns and have constraints. Understanding these constraints helps you set realistic expectations and plan your development approach.

The agents generate data models, screens with standard UI patterns, roles and entity-level authorization, and basic logic and navigation. They explain existing code and suggest fixes. Complex business logic, external system integrations, custom CSS or JavaScript, mobile apps, and performance optimization require manual development in ODC Studio. For the full list, refer to [Known limitations](ai-limitations.md).

## Related resources

The coding agents support Mentor across the development lifecycle. The following resources cover the architecture, the workflows, and the prompting techniques that work with the agents.

* For the components that underpin agentic development, including the OutSystems Model and the Enterprise Context Graph, refer to [Architecture](architecture.md).
* For creating apps with the agents in Mentor Web, refer to [How AI app generation works](mentor-web/how-it-works.md).
* For modifying apps with the agents in Mentor Studio, refer to [AI development in Mentor Studio](mentor-studio/how-it-works.md).
* For the conceptual shift to prompt-based development, refer to [Thinking with AI](thinking-with-ai.md).
* For prompting strategies that apply across all Mentor tools, refer to [Effective prompts for Mentor](effective-prompts.md).
