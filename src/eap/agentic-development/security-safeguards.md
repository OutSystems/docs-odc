---
summary: "Mentor coding agents in OutSystems Developer Cloud (ODC) apply layered safeguards: data isolation, safe output, user approvals, and access governance."
tags:
  - AI
  - Agentic
  - Logging
  - Mentor
  - Mentor Studio
  - Mentor Web
  - Security
guid: 8ec0312c-41cd-4c37-8059-50d385cad7ef
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
  - Tech lead
  - Platform administrator
  - Developer
topic:
  - creating-apps
isautopublish: true
---

# Security and safeguards

Mentor's coding agents read and change your apps. OutSystems applies safeguards across that interaction: data privacy and isolation, prompt logging, guardrails and content filtering, output safety, human oversight, and access governance.

## Data privacy and isolation

OutSystems processes the data you send to Mentor under enterprise agreements and platform controls that enforce privacy and isolation.

* **Model training.** Enterprise agreements with the AI providers prohibit training third-party AI models on your prompts and requirement documents.
* **Tenant isolation and encryption.** OutSystems encrypts your data in transit and at rest with tenant-specific keys, and processes it in isolation from other tenants.
* **Mentor reads your app's model.** Mentor reads the OutSystems Model, including your app's structure, logic, and UI, at design time. Mentor sends text in your app, such as static values, to the model as context, so avoid putting personal and sensitive data in prompts and app content.

For where OutSystems processes this data, refer to [Data platform](../manage-platform-app-lifecycle/platform-architecture/intro.md#data-platform).

<div class="warning" markdown="1">

Don't include personally identifiable information (PII) such as real names, email addresses, phone numbers, or government IDs in prompts or requirement documents. Use placeholder or fictional data instead.

</div>

## Prompt logging

OutSystems logs the prompts you submit to Mentor for internal purposes: to audit agentic development activity and improve the service.

* **Scope.** Prompt logging applies at the tenant level and is on by default. The tenant setting governs every portfolio and stage.
* **Logged data.** Mentor records each prompt you submit, in every product surface where you use Mentor, such as Mentor Studio. Each record includes the prompt text, a timestamp, the source surface, and the affected asset when the prompt changes one. For what to avoid in your prompts, refer to [Data privacy and isolation](#data-privacy-and-isolation).
* **Access.** OutSystems may access prompt logs internally for auditing and service improvement.

Prompt logs persist for auditing even when the Mentor interface discards your conversation. For example, if you close your browser during a Mentor Web session, Mentor discards the conversation and blueprint, and the prompts you submitted remain logged.

## Guardrails and content filtering

Guardrails screen the prompts you submit to Mentor and the responses Mentor returns. Content filtering implements those guardrails, at the AI provider level and at the OutSystems level.

* **Provider guardrails.** The AI models Mentor runs on, hosted by providers such as AWS Bedrock, apply built-in content filters that screen for violations of the providers' safety policies.
* **OutSystems guardrails.** Mentor adds filtering of its own. For example, Mentor scopes its responses to your app, withholds internal implementation details, and masks personal data it identifies in your prompts. Masking depends on successful identification, so avoid putting personal data in your prompts.

<div class="info" markdown="1">

For the guardrails that inspect the prompts and AI model responses of the AI agents you build and run in your apps, refer to [Agent guardrails](../building-apps/build-ai-powered-apps/guardrails.md).

</div>

## Output safety

Mentor's output takes the form of model changes and meets platform standards.

* **Model-based changes.** Mentor turns your prompts into changes to the OutSystems Model, expressed as standard OutSystems Markup Language (OML).
* **Same standards as hand-built apps.** OutSystems Developer Cloud (ODC) enforces the same security, performance, and architecture standards regardless of how the model was created, including role-based access, encryption, and input validation.

For how the model and the compiler fit together, refer to [Architecture](architecture.md).

## Human oversight and control

You decide what Mentor applies. For a complex change, such as one that spans several entities, screens, and logic, Mentor proposes a plan and applies it only after you accept it. For a single-action change, Mentor applies the change directly. You review proposed changes before Mentor applies them, and compare your app before and after. You accept the change, discard it, or refine it with a follow-up prompt. For how planning and review work, refer to [Planning and your control](coding-agents.md#planning-and-your-control) and [Review and accept the plan](mentor-studio/how-it-works.md#review-and-accept-the-plan).

## Access and governance

Agentic development inherits your existing ODC governance. Access follows your ODC roles and permissions, and apps created or modified through agentic development follow the same governance, deployment, and review processes as any other ODC app. For how administrators govern who can use Mentor and how agentic development fits the software development lifecycle (SDLC), refer to [Agentic development in the SDLC](sdlc.md).

## Compliance

OutSystems operates Mentor under its enterprise security and compliance framework. For certifications, attestations, AI providers, and data residency, visit the [OutSystems Trust Center](https://security.outsystems.com/).

## Continuous testing and improvement

OutSystems tests the coding agents continuously, including independent security reviews, to match current security best practices. Feedback you give on responses, together with anonymized usage patterns, informs improvements to the coding agents.

## Related resources

The safeguards described here extend platform-wide security and the broader agentic development docs. The following resources add detail.

* For a summary of data handling in agentic development, refer to [Security and data privacy](intro.md#security-and-data-privacy).
* For the data platform features that log Mentor prompts, refer to [Features that send data to the data platform](../manage-platform-app-lifecycle/platform-architecture/intro.md#data-platform-features).
* For how the coding agents work, refer to [Coding agents](coding-agents.md).
* For the architecture behind agentic development, refer to [Architecture](architecture.md).
* For safeguards on the AI agents you build and run, refer to [Agent guardrails](../building-apps/build-ai-powered-apps/guardrails.md).
* For platform-wide security, refer to [Security of OutSystems Developer Cloud](../security/security.md).
* For certifications and policies, visit the [OutSystems Trust Center](https://security.outsystems.com/).
