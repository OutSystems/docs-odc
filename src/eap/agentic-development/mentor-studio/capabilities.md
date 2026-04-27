---
summary: Mentor Studio generates and modifies server actions, client actions, screens, entities, aggregates, and provides code analysis for existing apps.
tags: agentic development, code generation, server actions, client actions, aggregates
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
  - Front-end developer
  - Developer
topic:
  - creating-apps
isautopublish: true
---

# Capabilities and patterns for Mentor Studio

Mentor Studio modifies existing apps through conversation. You describe goals in natural language, and Mentor generates or modifies logic, screens, data structures, and other elements within the app. Changes integrate with existing elements and follow OutSystems patterns for security, architecture, and code quality.

This page describes the elements Mentor Studio generates and the types of tasks it supports. For capabilities available when creating new apps, refer to [Capabilities and patterns for Mentor Web](../mentor-web/capabilities.md).

## Element generation

Mentor Studio generates and modifies elements across several categories. Each element type follows OutSystems conventions, and generated code integrates with the existing app model.

### Logic

Mentor generates and modifies logic elements that implement business rules, data operations, and processing workflows. The following logic elements are supported:

* **Server actions**. Creates or modifies server-side logic for data processing, business rules, and backend operations.
* **Client actions**. Creates or modifies client-side logic for UI interactions, form handling, and screen behavior.
* **Service actions**. Creates or modifies actions exposed as services for cross-app communication.
* **Aggregates**. Creates or modifies data queries with filtering, sorting, grouping, and joins.
* **SQL nodes**. Creates or modifies custom SQL queries for advanced data retrieval that goes beyond aggregate capabilities.

### UI

Mentor generates and modifies UI elements that define app screens and reusable visual components. The following UI elements are supported:

* **Screens**. Creates or modifies screens with layouts, data bindings, and navigation.
* **Web blocks**. Creates or modifies reusable UI components that encapsulate layout and logic.
* **Emails**. Creates or modifies email templates with dynamic content and formatting.

### Data

Mentor generates and modifies data elements that define the app's data model. The following data elements are supported:

* **Entities**. Creates or modifies database tables with attributes and data types.
* **Attributes**. Adds, changes, or removes fields within entities, including data type changes.
* **Relationships**. Creates or modifies foreign key relationships and reference attributes between entities.

### Other elements

Mentor generates and modifies additional elements that support background processing and event-based communication.

* **Timers**. Creates or modifies scheduled background tasks for recurring operations.
* **Events**. Creates or modifies events for asynchronous communication between apps.

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

Mentor Studio can generate and modify logic, UI, data, and other elements within any web app. It handles tasks ranging from creating a single server action to coordinating changes across multiple elements in a single conversation.

For constraints that apply to Mentor Studio, refer to [Known limitations](../ai-limitations.md). For a breakdown of what Mentor handles and what requires manual development, refer to [When to use each tool](../intro.md#when-to-use-each-tool).
