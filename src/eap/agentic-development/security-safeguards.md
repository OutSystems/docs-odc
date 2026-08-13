---
summary: "Mentor coding agents in OutSystems Developer Cloud (ODC) apply layered safeguards: data isolation, safe output, user approvals, and access governance."
tags:
  - Agentic
  - AI
  - Mentor
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

Mentor's coding agents read and change your apps, so OutSystems applies safeguards across that interaction: how your data is handled, how output is kept safe and standards-compliant, how you stay in control, and how access is governed. This page covers the safeguards OutSystems applies to Mentor's coding agents. Guardrails is a separate, opt-in capability you configure for the AI agents you build and run inside your apps. For those, refer to [Guardrails](../building-apps/build-ai-powered-apps/guardrails.md).

## Data privacy and isolation

OutSystems handles the data you send to Mentor under enterprise agreements and platform controls that keep it private and isolated.

* **No training on your data.** Prompts and requirement documents aren't used to train third-party AI models. Enterprise agreements with the AI providers prohibit it.
* **Tenant isolation and encryption.** OutSystems encrypts your data in transit and at rest with tenant-specific keys, and processes it in isolation from other tenants.
* **Mentor works on your app's model.** Mentor reads the OutSystems Model, including your app's structure, logic, and UI, at design time. Text in your app, such as static values, goes to the model as context, so keep personal and sensitive data out of prompts and app content.

For where data is processed, refer to [Data Platform](../manage-platform-app-lifecycle/platform-architecture/intro.md#data-platform).

<div class="warning" markdown="1">

Don't include personally identifiable information (PII) such as real names, email addresses, phone numbers, or government IDs in prompts or requirement documents. Use placeholder or fictional data instead.

</div>

## Content filtering

Mentor relies on the safety features of the AI models it uses. The models, hosted by providers such as AWS Bedrock, apply built-in content filters that screen for content that violates the providers' safety policies. Mentor also keeps its responses focused on your app and doesn't expose internal implementation details. Mentor doesn't add separate detection or masking of personal data, so keep personal data out of your prompts.

To enforce your own guardrails on the AI agents you build and run, use the opt-in guardrails capability. Refer to [Guardrails](../building-apps/build-ai-powered-apps/guardrails.md).

## Output safety

The way Mentor generates apps limits the risk in its output.

* **Model, not raw code.** Mentor turns your prompts into changes to the OutSystems Model, expressed as standard OutSystems Markup Language (OML), rather than hand-written code.
* **Same standards as hand-built apps.** OutSystems Developer Cloud (ODC) enforces the same security, performance, and architecture standards regardless of how the model was created, including role-based access, encryption, and input validation.

For how the model and the compiler fit together, refer to [Architecture](architecture.md).

## Human oversight and control

You decide what Mentor applies. For a complex change, such as one that spans several entities, screens, and logic, Mentor proposes a plan and applies it only after you accept it. For a straightforward change, such as adding a single action, it applies the change directly. Proposed changes are transparent: you review them before Mentor applies them and compare your app before and after. You accept the change, reject it, or refine it with a follow-up prompt. For how planning and review work, refer to [Planning and your control](coding-agents.md#planning-and-your-control) and [Review and accept the plan](mentor-studio/how-it-works.md#review-and-accept-the-plan).

## Access and governance

Agentic development inherits your existing ODC governance rather than adding a separate model. Access follows your ODC roles and permissions, and apps created or modified through agentic development follow the same governance, deployment, and review processes as any other ODC app. For how administrators govern who can use Mentor and how agentic development fits the software development lifecycle (SDLC), refer to [Agentic development in the SDLC](sdlc.md).

## Compliance

OutSystems operates Mentor under its enterprise security and compliance framework. For certifications, attestations, AI providers, and data residency, visit the [OutSystems Trust Center](https://security.outsystems.com/).

## Continuous testing and improvement

OutSystems tests the coding agents continuously, including independent security reviews, to keep pace with evolving best practices. Feedback you give on responses, together with anonymized usage patterns, informs improvements that benefit all users.

## Related resources

The safeguards described here build on platform-wide security and the broader agentic development docs. The following resources add detail on each.

* For a summary of data handling in agentic development, refer to [Security and data privacy](intro.md#security-and-data-privacy).
* For how the coding agents work, refer to [Coding agents](coding-agents.md).
* For the architecture behind agentic development, refer to [Architecture](architecture.md).
* For safeguards on the AI agents you build and run, refer to [Guardrails](../building-apps/build-ai-powered-apps/guardrails.md).
* For platform-wide security, refer to [Security of OutSystems Developer Cloud](../security/security.md).
* For certifications and policies, visit the [OutSystems Trust Center](https://security.outsystems.com/).
