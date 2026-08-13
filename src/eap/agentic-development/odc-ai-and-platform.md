---
summary: In OutSystems Developer Cloud (ODC), the platform guarantees the model, compiler, and governance, while you validate what Mentor's AI interprets from your intent.
tags:
  - Agentic
  - AI
  - Development lifecycle
  - Mentor
  - Mentor Studio
  - Mentor Web
guid: be028f43-ee1e-4574-b777-eab1ffeaf97b
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
  - Developer
  - Front-end developer
topic:
  - creating-apps
isautopublish: true
---

# Platform guarantees and AI interpretation

This page describes how ODC and the AI divide the work when you build with Mentor, and what that division requires from you. ODC applies a fixed set of guarantees to every app it compiles, so its results are deterministic. The AI interprets your intent to propose a model, and interpretation is probabilistic, so you review and validate each proposal. This distinction tells you where the output is reliable and where your review is required. Mentor and manual development in ODC Studio produce the same OutSystems Model.

Your starting point depends on your background:

| Background | What you already know | What is new here |
| ---------- | --------------------- | ---------------- |
| Low-code | Entities, screens, aggregates, and logic | Mentor proposes these from your intent, and you validate the result |
| Writing code directly | How to specify a data model, query, screen, and authorization in code | The OutSystems Model as the abstraction you work through, compiled to a standard app |

## Platform guarantees

ODC provides these guarantees at the platform level. Every ODC app is enterprise-grade by default: it inherits the compiler, delivery pipeline, security, observability, governance, and scalable runtime, whether you build it by hand or through Mentor. ODC applies these standards to every app it compiles, so the results are deterministic.

* **One model.** Mentor works on the OutSystems Model, the high-level representation that every OutSystems app is built on. Assets built or modified through Mentor are standard OutSystems assets, with no separate AI code path. For how the model, the agents, and the compiler fit together, refer to [Architecture](architecture.md).
* **Compiler-enforced standards.** The OutSystems compiler turns the model into deployable code and applies the same security, performance, and architecture standards to Mentor output as to hand-built assets. For how the agents and the compiler interact, refer to [Coding agents](coding-agents.md).
* **Reviewable intent before it is applied.** For structural work, Mentor presents its intended work before it commits: the blueprint in Mentor Web, and proposed changes in Mentor Studio. You accept, reject, or refine first. For the blueprint, refer to [The blueprint](mentor-web/blueprint.md).
* **Governance parity.** From deployment, monitoring, and audit perspectives, an asset created through Mentor is indistinguishable from one built in ODC Studio. The same quality gates, reviews, and lifecycle processes apply. For lifecycle integration, refer to [Agentic development in the SDLC](sdlc.md).

## AI interpretation today

The AI's contribution behaves differently from the platform guarantees in two ways. It is probabilistic rather than deterministic, and it changes as agentic development matures. The word "today" marks the second point. Verify these behaviors against your current release rather than assuming they are fixed.

* **Interpretation is probabilistic.** The coding agents interpret your description and map it to OutSystems patterns; they don't apply a fixed rule. The same prompt can produce different results.
* **Coverage expands between releases.** The range of tasks the agents handle grows over time. A limit in the current release may not exist in the next one. Check the current constraints rather than assuming a fixed boundary. For current constraints, refer to [Known limitations](ai-limitations.md).
* **Output is a proposal.** A generated entity, screen, or logic flow reflects what the AI inferred from your prompt, and it compiles to a standard OutSystems asset. Compilation confirms the code is valid. You confirm that it matches your requirement.
* **The prompt is your input to interpretation.** Because the agents build from what you state, clear and explicit intent produces more accurate proposals. For prompting technique, refer to [Effective prompts for Mentor](effective-prompts.md).

## Review checks

In review, you apply your judgment to the AI's output. The platform guarantees the model is valid; you determine whether it is the correct model for the requirement. Every developer can judge whether a data model, screen, query, authorization boundary, logic flow, workflow, or AI feature is correct, whether you built it in a visual editor or wrote it in code. Your judgment validates Mentor's output. The following checks are examples, not a complete list. They run from the simplest structural elements to more complex logic, and each maps to a step in the describe, review, refine loop.

| What you know | What you check | Where in the workflow |
| ------------- | -------------- | --------------------- |
| What a well-formed entity, its attributes, and their data types look like | The blueprint's entities, attributes, and data types match the domain | Blueprint review in Mentor Web, before generation |
| How entities relate and the correct cardinality | The one-to-many and many-to-many relationships and foreign keys are correct | Blueprint review, before generation |
| Which screen pattern a requirement calls for | The generated screens use the intended pattern, such as a list with master detail or a dashboard | After generation, and when reviewing proposed changes |
| What an aggregate should return | The filters, sorts, and joins behind a screen or logic flow return the intended data | When reviewing generated or modified logic |
| How entity-level authorization and roles work | The roles and permissions match who should read or edit each entity | Blueprint review, and after any change to roles |
| How a business rule should behave in an action flow | The generated logic implements the rule, including edge cases and exception handling | When reviewing generated or modified logic in Mentor Studio |
| How a business process should flow through its activities, decisions, and states | The generated workflow's activities, decisions, and transitions match the process, and human activities route to the right roles | When reviewing a generated or modified workflow |
| What an AI feature should do and which data should ground it | The AI agent uses the intended model, prompt, and tools, grounds its answers in the right data, and applies guardrails to the output | When reviewing a generated AI agent or AI logic |

Your main tasks are to direct Mentor with well-formed intent and to validate its output using checks like these. For how oversight scales with the reach of a change, refer to [Match oversight to impact](thinking-with-ai.md#match-oversight-to-impact).

## Related resources

The tools and workflows in this section apply these platform guarantees and AI behaviors. The following resources cover them in detail.

* For the mindset and iteration cycle of prompt-based development, refer to [Thinking with AI](thinking-with-ai.md).
* For an overview of both Mentor tools and guidance on when to use each, refer to [Introduction to agentic development](intro.md).
* For what the coding agents are and how they work, refer to [Coding agents](coding-agents.md).
* For prompting strategies that improve how Mentor interprets your intent, refer to [Effective prompts for Mentor](effective-prompts.md).
