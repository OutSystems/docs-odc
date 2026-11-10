---
summary: OutSystems builds agentic industry solutions for banking and insurance. Each one is a pre-built system of apps, AI agents, and services for a specific business problem.
tags:
  - Agentic
  - AI
  - Architecture
  - Modular Programming
  - Workflows
locale: en-us
guid: 77bed402-a8d1-4ebd-95c2-023d13e24861
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - Architect
  - Developer
  - Tech lead
outsystems-tools:
  - forge
content-type:
  - conceptual
coverage-type:
  - understand
  - evaluate
topic:
  - agentic-industry-solutions-overview
isautopublish: true
---

# Agentic industry solutions

Organizations in regulated industries want to optimize their systems and apply AI agents to operational processes. However, agents must follow the organization's policies, keep decisions auditable, work with existing systems, and leave decisions to a human. Building a governed agent system from scratch means designing the apps, agents, workflows, and audit trail yourself.

OutSystems offers agentic industry solutions so you don't have to build that system yourself. Each one is a pre-built system for a specific business problem. You adapt it to your own products and policies, and a human makes the final decision.

## What agentic industry solutions provide {#what-agentic-industry-solutions-provide}

Each solution provides the following:

* **Agents with human oversight**: Agents handle tasks such as document validation and fraud risk analysis. A human makes the final decision, such as the loan officer who validates a loan application.
* **Audit trail**: The audit trail records business operations, so you can review what changed and when.
* **Modular architecture**: The solution is built using components that you can deploy separately.
* **Integration with existing systems**: The solution works with the systems you already run, such as core banking or claim management systems, through integration wrappers.
* **Sample data**: Sample data and mock integrations let you test the journey after installation and setup, before you connect your own systems.

## How agentic industry solutions are built {#how-agentic-industry-solutions-are-built}

An agentic industry solution organizes its components in two ways: by responsibility, and by whether the components are custom or shared.

### Groups of components {#groups-of-components}

Each component belongs to one group, based on its responsibility:

* **Workflows**: Coordinate the steps of a process between people, apps, and agents in solutions that need orchestration.
* **End-user apps**: Serve as the access point for end users.
* **AI agents**: Assist with tasks in the process.
* **Core services**: Keep the data, the business rules, and the audit evidence.
* **Integration wrappers**: Abstract external providers behind a fixed interface. You map the API of your own connector to that interface, so changing providers doesn't affect the other components.

### Custom and shared components {#custom-and-shared-components}

Custom components are specific to an organization, and shared components are reused across organizations. Each component also has a level of specificity, from the most specific to the most generic. The following table describes each level.

| Level | Description | Dependencies |
| --- | --- | --- |
| Custom composition components | The most specific components. They can be tailored to each organization. | Can depend on any add-on, common industry, or cross-industry component. |
| Add-on components | Capabilities for a specific business area, such as lending or claims handling. | Can only depend on add-on, common industry, and cross-industry components. |
| Common industry components | Components shared across an industry, such as banking. | Can only depend on common industry and cross-industry components. |
| Cross-industry components | Components that stay industry-agnostic and reusable everywhere. | Can only depend on cross-industry components. |

Dependencies run only from specific to generic components, so shared components stay independent of custom ones.

## Available solutions {#available-solutions}

OutSystems has two agentic industry solutions, one for banking and one for insurance:

* **[Agentic Loan Applications](https://www.outsystems.com/forge/component-overview/25462/agentic-loan-applications-odc)**: Consumer lending for banking. Governed AI agents, a workflow, and apps guide a loan application from the customer request to the loan officer's decision.
* **[Agentic First Notice of Loss](https://www.outsystems.com/forge/component-overview/25993/agentic-first-notice-of-loss-odc)**: Property and casualty insurance for auto collision claims. Governed AI agents and a mobile app guide a policyholder from the first notice of loss to a submitted claim.
