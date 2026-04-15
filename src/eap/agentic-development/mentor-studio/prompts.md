---
summary: Prompt examples for modifying apps with Mentor Studio, organized by logic, UI, data, and code analysis tasks.
tags: prompts, agentic development
guid: a69ed2b1-c692-4f80-801c-0acafacccdfa
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - odc studio
  - mentor studio
coverage-type:
  - apply
audience:
  - frontend developers
  - backend developers
  - full stack developers
isautopublish: true
---

# Prompts for Mentor Studio

This cookbook provides prompt examples for modifying apps with Mentor Studio. Examples progress from basic (single-task prompts) to detailed (prompts with specific context and multiple aspects). For general prompting strategies that apply across all Mentor tools, refer to [Effective prompts for Mentor](../effective-prompts.md).

## Before you start

Mentor doesn't detect the current screen or selection, so reference elements by name in every prompt. For example, "modify the ValidateEmail action" instead of "modify this action." For general prompting strategies, refer to [Effective prompts for Mentor](../effective-prompts.md).

## Logic

Use these prompts to create or modify server actions, client actions, service actions, and aggregates.

### Prompt progression

* Basic: Create a server action that validates an email format.
* Detailed: Create a Server Action named `ValidateOrderTotal` that takes `OrderId` as input, retrieves all `OrderItem` records for that order, calculates the sum of `Quantity * UnitPrice`, and returns the `TotalAmount`. Include error handling for cases where the order doesn't exist.

## UI

Use these prompts to create or modify screens, web blocks, and layouts.

### Prompt progression

* Basic: Create a screen to list all Customer records.
* Detailed: Create a screen named `OrderDashboard` that displays a summary of orders by status. Include a table showing `OrderId`, `CustomerName`, `OrderDate`, and `Status`. Add a filter dropdown for `Status` and sort by `OrderDate` descending.

## Data

Use these prompts to create or modify entities, attributes, and relationships.

### Prompt progression

* Basic: Add a `Priority` attribute to the `Task` entity.
* Detailed: Create a `Comment` entity linked to the `Ticket` entity with attributes `CommentText` (Text), `CreatedBy` (User reference), and `CreatedDate` (DateTime). Set up a one-to-many relationship where each Ticket can have multiple Comments.

## Add documentation

Use these prompts to generate descriptions for elements and add comments that explain code.

### Prompt progression

* Basic: Write a short description for a Client Action named `CalculateDiscount` that takes `BasePrice` and `CustomerTier` as inputs and returns the `FinalPrice`.
* Detailed: On the `ProcessRefund` Service Action, explain the input parameters, the logic flow (including the aggregate filters used), and the specific exception handling strategy. Also, describe the impact analysis for other apps in the same ODC tenant that consume this service.

## Explain code

Use these prompts to understand unfamiliar logic or get an overview of app structure.

### Prompt progression

* Basic: Explain what the `GetOrdersByStatus` Aggregate is doing, specifically the 'Only With' join between `Order` and `ShippingStatus`.
* Detailed: Provide a high-level explanation of what the OrderManagement application does. What are the main flows?

## Fix errors and warnings

Use these prompts to resolve TrueChange errors and warnings.

### Prompt progression

* Basic: I'm getting a 'Data Type Mismatch' warning when assigning a Text variable to an Identifier attribute. How do I properly use **TextToIdentifier**?
* Detailed: I have a 'Cyclic Dependency' warning between two ODC Libraries. Suggest a refactoring strategy to move the shared Structures or Service Actions into a 'Core' library to resolve the cycle while maintaining ODC best practices for modularity.

## Find and fix bugs

Use these prompts to identify inconsistencies or unexpected behavior.

### Prompt progression

* Basic: The 'Save' button is enabled even when the Form is invalid. Review the SaveOrder logic and tell me where the `Form.Valid` check is missing.
* Detailed: Users are reporting that the 'Total Amount' on the screen doesn't update when a line item is deleted. Review the UpdateOrderTotal Client Action logic and the 'On Parameters Changed' event of the Block to identify why the state isn't refreshing correctly in the ODC Reactive UI.

## Manage technical debt

Use these prompts to identify areas that need improvement and refactor complex logic.

### Prompt progression

* Basic: Identify redundant logic in the CalculateShipping Action where the same Aggregate is being called twice unnecessarily.
* Detailed: The ProcessOrder Server Action has over 20 nodes and multiple nested 'If' statements. Break this down into smaller, reusable Actions. Focus on separating the 'Data Retrieval' logic from the 'Business Validation' and 'Data Persistence' steps to improve maintainability.

## Break down complex tasks

Use these prompts to decompose large requirements into smaller implementation steps.

### Prompt progression

* Basic: List the steps needed to implement a 'Forgot Password' flow.
* Detailed: I need to build a 'Real-time Inventory Dashboard' that consumes data from an external API and displays it in ODC. Break this down into tasks: external logic integration, Data Action setup, caching strategy for performance, and the UI Block structure for the charts.

## Related resources

These prompt examples are starting points that you can adjust based on your app's structure and complexity. The following resources cover general strategies and the full range of Mentor Studio capabilities.

* For prompting strategies that apply across all Mentor tools, including entity-first thinking and decomposition, refer to [Effective prompts for Mentor](../effective-prompts.md).
* For the full list of elements that Mentor Studio supports, including logic, UI, and data, refer to [Capabilities and patterns for Mentor Studio](capabilities.md).
* For how Mentor Studio processes requests and integrates changes with existing apps, refer to [AI development in Mentor Studio](how-it-works.md).
* For UI pattern prompts and app generation examples in Mentor Web, refer to [Prompts for Mentor Web](../mentor-web/prompts.md).
