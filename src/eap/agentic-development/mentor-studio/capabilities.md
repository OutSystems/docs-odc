---
summary: Mentor Studio in OutSystems Developer Cloud (ODC) generates server actions, screens, entities, aggregates, and analyzes existing app code.
tags:
  - Agentic
  - Aggregates
  - AI
  - Entities
  - Logic
  - Mentor Studio
  - Screens
guid: 5abbc7b0-dedb-49ec-9af5-41e3220bb071
locale: en-us
app_type: reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=9424-6
outsystems-tools:
  - odc studio
  - mentor studio
coverage-type:
  - remember
  - understand
audience:
  - Developer
topic:
  - creating-apps
isautopublish: true
---

# Capabilities and patterns for Mentor Studio

Mentor Studio modifies existing apps through conversation. You describe goals in natural language, and Mentor generates or modifies elements within the open asset. Changes integrate with existing elements and follow OutSystems patterns for security, architecture, and code quality.

This page describes what Mentor Studio edits and the types of tasks it supports. For capabilities available when creating new apps, refer to [Capabilities and patterns for Mentor Web](../mentor-web/capabilities.md).

## Element coverage

Mentor Studio edits the elements the open asset supports. Each asset type has its own architecture, which determines what's available in a Mentor conversation. Refer to the asset documentation for the complete element list:

* [Apps](../../app-architecture/intro.md) covers web apps.
* [Libraries](../../building-apps/libraries/libraries.md) covers general-purpose and mobile libraries (beta).
* [Agentic apps in ODC](../../building-apps/build-ai-powered-apps/agentic-apps.md) covers agentic apps (beta). Mentor Studio edits agents in Agent Workbench, the ODC capability for building and managing agents.

Generated code follows OutSystems conventions and integrates with the existing app model. Build mobile apps manually in ODC Studio.

<div class="info" markdown="1">

To edit libraries and agentic apps, open **ODC Studio** > **Settings** and select **Enable Mentor for Agentic apps and Libraries** under **Beta**.

</div>

## Code analysis

Mentor Studio analyzes existing code and provides insights beyond generating new elements. Code analysis helps you understand unfamiliar logic, identify areas for improvement, and plan implementation approaches.

* **Explain existing code**. Describe what a specific action, aggregate, or screen does in plain language.
* **Suggest implementation approaches**. Recommend how to implement a requirement based on the existing app structure.
* **Identify technical debt**. Highlight areas that benefit from refactoring, such as duplicated logic or overly complex actions.
* **Review for bugs**. Check actions for inconsistencies, missing error handling, or unexpected behavior.

## Use cases

Mentor Studio supports a range of development tasks. The following table describes common use cases with example prompts.

| Use case | Description | Example prompt |
| -------- | ----------- | -------------- |
| Add features | Create entities, screens, or logic for a requirement | "Create a Comment entity linked to the Ticket entity with a list screen." |
| Add documentation | Generate descriptions for elements and add comments to explain code | "Add descriptions to all server actions in the OrderManagement app." |
| Explain code | Understand unfamiliar logic or get an overview of app structure | "Explain what the GetActiveOrders aggregate does." |
| Fix errors and warnings | Resolve TrueChange errors and warnings | "Fix the errors in the CreateOrder action." |
| Find and fix bugs | Identify inconsistencies or unexpected behavior | "Check the ProcessPayment action for potential bugs." |
| Modernize legacy code | Redesign UI patterns or refactor outdated logic | "Update the CustomerList screen to use the card layout." |
| Manage technical debt | Identify areas that need improvement | "What technical debt exists in the OrderManagement app?" |
| Break down complex tasks | Decompose large requirements into smaller steps | "Break down adding user authentication into tasks." |

## Scope

Mentor Studio edits web apps, libraries, and agentic apps. It handles tasks ranging from creating a single server action to coordinating changes across multiple elements in a single conversation. The available elements depend on the asset type.

For constraints that apply to Mentor Studio, refer to [Known limitations](../ai-limitations.md). For a breakdown of what Mentor handles and what requires manual development, refer to [When to use each tool](../intro.md#when-to-use-each-tool).
