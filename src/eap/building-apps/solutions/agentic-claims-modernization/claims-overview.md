---
summary: OutSystems Developer Cloud (ODC) claims solution maps AI agents, ACORD-aligned data, and mobile submission for auto collision workflows.
tags:
  - AI
  - Agentic
  - Data Integrity
  - Data Model
  - Mobile app
locale: en-us
guid: 01c59f38-3736-4194-9c02-b108d78284f5
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/qNvoQig5kGad2lkuAU7c0W/banking-solution?node-id=41-103
audience:
  - Architect
  - Tech lead
outsystems-tools:
  - forge
content-type:
  - conceptual
coverage-type:
  - understand
  - evaluate
topic:
  - agentic-claims-modernization-overview
isautopublish: true
---

# Agentic First Notice of Loss: solution overview

Agentic First Notice of Loss (FNOL) is a property and casualty insurance solution for auto claims intake. Policyholders file and track a claim from a mobile app. Four governed AI agents guide the intake, analyze the evidence, write the claim summary, and answer policy questions on a shared, ACORD-aligned claims core. The solution sits in front of your claim management system and grounds its agents in your policies and coverages. The claim reaches your system structured and complete, and every coverage, liability, and payout decision stays with your organization.

![ODC Portal page of the Agentic First Notice of Loss solution with the Components tab selected. The tab lists 14 components: Mobile Insurance, the Claims Conversation Agent, the Claims Document and Evidence Agent, the Claims Damage Report Agent, the Claims Policy and Fraud Agent, Claims Services, Insurance Sync Services, Solutions Common Services, Solutions Common Patterns, Solutions Location Library, and the Claims Management, Vehicle Data, Roadside Assistance, and Car Rental integration wrappers.](images/claims-components-pl.png)

The ACORD-aligned data model supports any type of loss, but the business rules and the Claims Conversation Agent exercise only vehicle collision claims. You can extend the solution for other types of loss.

## What the solution includes {#what-the-solution-includes}

Each group of components has the following role in the solution:

* **End-user app**: Lets policyholders start a claim and follow its progress from a mobile app.
* **AI agents**: Guide the policyholder through the claim, analyze photos and documents, and write the claim summary. They use AI models that you configure in your tenant. For more information, refer to [AI agents in the First Notice of Loss solution](claims-agents.md).
* **Core services**: Keep the claim data in an ACORD-aligned data model and apply the business rules.
* **Integration wrappers**: Connect the solution to your claim management system and to the external provider systems that support a claim, such as roadside assistance, car rental, and vehicle data, through a fixed interface. Most return sample data until you connect your own systems.

## Governance of AI agents {#governance-of-ai-agents}

The solution keeps claim decisions with people and limits what the AI agents do. Governance works in the following ways:

* **Grounded in the claim**: With every response, the conversation agent works from the claim data and the rule for the current status of the claim. It doesn't determine coverage, fault, or fraud.
* **Safety first**: The conversation agent checks for safety before it collects the incident details. A safety override pauses the flow on any sign of injury or danger.
* **Evaluated before production**: The Claims Policy and Fraud Agent and the Claims Document and Evidence Agent ship with evaluation datasets that you run in ODC agent evaluations.
* **Evidence without verdicts**: The evidence agent describes each photo and document and makes no claim decision. The solution records integrity concerns as observations and flags them for the adjuster, without blocking or notifying the policyholder.
* **Proposals, not decisions**: Agents propose, and only the solution's core services update the claim. The Claims Policy and Fraud Agent has read-only access to coverages and returns recommendations only.
* **Recorded state and audit**: The solution keeps an audit log of business operations, an immutable history of status changes, and a stamp on each record that shows who created and updated it. Where an AI agent makes a change, the record can identify the agent.

## Claim flow {#claim-flow}

The policyholder starts a claim in Mobile Insurance, from a chat or a crash alert. The Claims Conversation Agent checks for safety first, collects the incident details, offers assistance services, and asks for photos and documents. The policyholder then reviews the claim summary and submits the claim. The following diagram shows the main steps and who performs them:

![Diagram of the claim flow in six steps, with lanes for the policyholder and the solution. The policyholder starts a claim in Mobile Insurance. The solution collects the incident details and requests evidence. The policyholder provides the details, photos, and documents. The solution analyzes the evidence and writes a summary. The policyholder reviews the summary and submits the claim. The claim is then pending adjuster review.](images/claims-process-diag.png)

The solution covers the claim up to its submission. The adjuster then decides the outcome and closes the claim outside the solution. The [Claim flow in the First Notice of Loss solution](claims-flow-and-status.md) page describes the phases and steps.

## Next steps {#next-steps}

To install and set up the Agentic First Notice of Loss solution, learn how it's built, refer to the following pages:

* [Agentic First Notice of Loss (ODC) on Forge](https://www.outsystems.com/forge/component-overview/25993/agentic-first-notice-of-loss-odc)
* [Get started with the First Notice of Loss solution](claims-get-started.md)
* [Architecture of the First Notice of Loss solution](claims-solution-architecture.md)
* [AI agents in the First Notice of Loss solution](claims-agents.md)
* [Claim flow in the First Notice of Loss solution](claims-flow-and-status.md)
