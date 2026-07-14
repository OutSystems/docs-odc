---
summary: "OutSystems Developer Cloud (ODC) agentic development: AI agents, the OutSystems Model, and the compiler form the Enterprise Context Graph."
tags:
  - Agentic
  - AI
  - Architecture
  - Mentor
  - Mentor Studio
  - Mentor Web
guid: d79811bf-4406-465e-b4b2-0351b967d20e
locale: en-us
app_type: reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=9332-117
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

# Architecture

Agentic development in OutSystems combines three components to turn natural language into app structures. This architecture applies to both Mentor Web and Mentor Studio. Together with tenant context, these components form the OutSystems Enterprise Context Graph. This graph gives AI agents the context they need to understand your apps, data, and dependencies.

* **AI agents** interpret natural language and map it to OutSystems development patterns.
* **OutSystems Model** (the app model, not an AI model) represents the app's structure, data, logic, and UI at a high level of abstraction.
* **OutSystems compiler** translates the app model into deployable code, enforcing security and performance standards.

Understanding how these components work together explains why explicit prompts produce better results than vague descriptions.

## AI agents

Agentic development uses AI agents that combine general-purpose Large Language Models with OutSystems-specific knowledge and instructions. These agents plan and carry out multi-step tasks across different parts of an app. They map natural language to OutSystems development patterns. When you write a prompt or upload a requirement document, the agents identify entities, relationships, roles, and UI patterns. In Mentor Web, this becomes a blueprint. In Mentor Studio, it becomes a set of proposed changes. You review both before changes are applied.

The agents know common app structures: entities and their relationships, user roles and permissions, screen layouts, and business logic patterns. When your input matches these patterns, agentic development generates structures that fit them. When input is unclear or uses unfamiliar terms, the agents interpret it as best they can based on context.

This is why explicit, structured prompts produce better results than vague descriptions. The agents work primarily from patterns they recognize, so they may not infer requirements you leave unstated.

## Tenant context

Mentor reads context from your development environment to produce more relevant results. This applies to new apps and to changes in existing apps. The context includes existing entities, public elements from other apps (such as actions and entities), Data Fabric connections, and app metadata. When you reference an element in a prompt, Mentor uses this context to generate elements that build on it.

Tenant context includes the public elements that other apps expose for reuse. Mentor references and reuses these public elements when generating or modifying an app, so you can build on existing assets without recreating them. For background on public elements and producer-consumer dependencies, refer to [Reuse elements across apps](../app-architecture/reuse-elements.md).

A populated development environment improves results. If your tenant has entities, actions, and established patterns, Mentor can reference them when generating new elements. For new tenants with little existing structure, Mentor relies more on the prompt and recognized patterns.

## OutSystems Model

The OutSystems Model is a structured representation of an app's data, logic, and UI. All OutSystems apps are built on this model, not just those built through agentic development. Whether you build in ODC Studio or use Mentor, you work with the same app model.

Agentic development creates and modifies the app model, not raw code. Working at this level keeps generated apps consistent and easy to maintain in ODC Studio.

The app model captures what to build, not how to build it. This brings three advantages:

**ODC standards.** The compiler enforces security, performance, and architecture rules when it turns the model into code. AI-generated apps follow the same standards as hand-built apps.

**Consistency.** The model ensures generated apps use OutSystems patterns correctly. Entity links, screen bindings, and authorization rules follow ODC conventions.

**Maintainability.** Because agents work at the model level, you can continue development in ODC Studio without dealing with AI-generated code quality issues.

## Compiler

The OutSystems compiler turns the app model into deployable code when you publish. It applies the same security, performance, and architecture rules whether you used agentic development or built the app by hand. All apps run with data encryption and input validation. The platform also enforces the roles and permissions the app defines, so review the access the agents configure to confirm it matches your intent.

## Generation flow (Mentor Web)

When you create a new app in Mentor Web, the request follows a set path from input to deployable code. Knowing this path helps you spot where to adjust when results don't match what you expected. You review a blueprint before generation begins.

![Portal generation flow showing developer input flowing through ODC Portal and AI Services to external LLM providers, with blueprint review before app generation](images/ai-app-gen-portal-architecture-diag.png "Mentor Web architecture")

The diagram shows the components involved in app generation. When you enter a prompt or upload a document, the request moves through these components and produces a deployable app. The blueprint review gives you a checkpoint before generation starts.

* **Input.** A prompt or requirement document describing the desired app.
* **Interpretation.** The AI agents analyze the input using [tenant context](#tenant-context), identifying entities, relationships, roles, UI patterns, and business logic.
* **Blueprint.** ODC produces a visual representation of the interpreted requirements for review.
* **App model generation.** After blueprint approval, ODC creates the app model.
* **Compilation.** When published, the compiler translates the app model into deployable code.

Refinement prompts repeat the interpretation and generation phases, applying changes incrementally to the existing app model.

## Modification flow (Mentor Studio)

Mentor Studio works differently from Mentor Web. Instead of building a new app, it reads the existing model and applies targeted changes.

![ODC Studio modification flow showing prompts flowing through AI Services with tenant context and agent processing to external LLM providers](images/ai-modify-app-prompts-ide-architecture-diag.png "Mentor Studio architecture")

The diagram shows the components for app modification. When you enter a prompt in the Mentor panel, the request moves through these components. Mentor Studio starts by reading the existing app to understand what is there.

* **Context analysis.** Mentor reads the current app model, including entities, screens, actions, and relationships.
* **Input.** A prompt expressing your intent: changes, explanations, code review, or implementation guidance.
* **Interpretation.** The AI agents analyze the prompt in the context of the existing app structure.
* **Proposed changes.** For complex requests, Mentor Studio presents the changes it plans to make and applies them after you accept. It applies simpler changes directly, and you review the result.
* **App update.** After approval, Mentor applies the changes to the app model.
* **Compilation.** When published, the compiler translates the updated app model into deployable code.

The key difference is context. Mentor Studio reads the existing app and generates changes that fit in. You can make targeted edits without rebuilding the whole app.

## How the tools work together

Both tools work with the same app model. Mentor Web creates new apps and supports iteration. Mentor Studio gives you the full development environment for changes of any complexity. You can switch between them as needed.

A typical workflow might be:

1. **Create in Mentor Web.** Generate a new app from requirements.
1. **Refine in Mentor Web.** Use the editor to iterate on the generated app.
1. **Extend in Mentor Studio.** Open the app in ODC Studio and use Mentor Studio to add features, fix issues, or extend logic.
1. **Manual development.** Use ODC Studio's visual tools for advanced development that requires capabilities beyond the supported patterns.

All tools share the same app model. Apps built through agentic development are standard OutSystems apps. You can switch between AI prompts and manual development at any time.

## Related resources

The architecture described here supports both Mentor Web and Mentor Studio. The following resources explain how each tool interacts with the app model and how agentic development fits into your development lifecycle.

* For how Mentor Web uses this architecture to generate new apps from requirements, refer to [How AI app generation works](mentor-web/how-it-works.md).
* For how Mentor Studio uses this architecture to modify existing apps through conversation, refer to [AI development in Mentor Studio](mentor-studio/how-it-works.md).
* For how agentic development integrates with testing, deployment, and governance, refer to [Agentic development in the SDLC](sdlc.md).
