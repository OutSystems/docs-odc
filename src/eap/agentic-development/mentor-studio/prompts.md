---
summary: Mentor Studio prompt examples for OutSystems Developer Cloud (ODC) apps, covering logic, UI, data, debugging, refactoring, and task decomposition.
tags:
  - AI
  - Data
  - Logic
  - Mentor
  - Mentor Studio
  - Technical Debt
  - UI
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
  - Front-end developer
  - Developer
isautopublish: true
---

# Prompts for Mentor Studio

This cookbook provides prompt examples for modifying apps with Mentor Studio. Examples progress from basic (single-task prompts) to detailed (prompts with specific context and multiple aspects). For general prompting strategies that apply across all Mentor tools, refer to [Effective prompts for Mentor](../effective-prompts.md).

## Before you start

Mentor reads the element you select and the view you have open in ODC Studio. Select an element, then refer to it directly, such as "modify this action." To act on a different element, name it in your prompt instead, such as "modify the ValidateEmail action." After you add a public element through **Add public elements**, reference it by name the same way. Mentor also finds and adds a public element when you reference one it locates in the tenant.

## Logic

Use these prompts to create or modify server actions, client actions, service actions, and aggregates.

### Prompt progression

* Basic: Create a server action that validates an email format.
* Detailed: Create a Server Action named `ValidateOrderTotal` that takes `OrderId` as input, retrieves all `OrderItem` records for that order, calculates the sum of `Quantity * UnitPrice`, and returns the `TotalAmount`. Include error handling for cases where the order doesn't exist.

### Logic prompts by task

Use these prompts as starting points for aggregates, server actions, and client variables. Replace the element names with the names in your app.

* **Filter an aggregate:** In the `GetEmployees` aggregate, add a filter so that it returns only the employees whose `City` is London.
* **Sort an aggregate:** In the `GetEmployees` aggregate, sort the results by `FirstName` in ascending order.
* **Add a dynamic sort:** In the `GetOrders` aggregate, add a dynamic sort that uses a Text variable named `SortBy`. Users can sort by `Order.OrderDate`.
* **Return distinct values:** Create an aggregate that returns the distinct values of the `City` attribute of the `Employee` entity.
* **Add a calculated attribute:** In the `GetProducts` aggregate, count `Product.Id` for each group of `Category.Id` and `Category.Label`. Add a calculated attribute named `DropdownLabel` that shows the label followed by the count in parentheses.
* **Join an external entity:** In the `GetOrdersWithCustomers` aggregate, add the external `Customer` entity as a source with a With or Without join to `Order` on `CustomerId`.
* **Wrap entity actions:** Create server actions that wrap the Create, Update, and Delete entity actions of the `Product` entity. Validate the mandatory attributes before saving, and set `CreatedOn` and `CreatedBy` when a record is created.
* **Create a client variable:** Create a client variable named `SearchKeyword` of type Text. Bind it to the Search input on the `Employees` screen, and filter the `Employee` aggregate by `FirstName` using the variable.

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

### Data prompts by task

Use these prompts as starting points for specific data modeling tasks. Use fictional values in prompts, because prompts must not include personally identifiable information.

* **Create an entity:** Create a `Place` entity with a mandatory `Name` attribute of type Text with 100 characters, a mandatory `Address` attribute of type Text with 200 characters, an optional `PhoneNumber` attribute of type Phone Number, and optional `Latitude` and `Longitude` attributes of type Decimal.
* **Create a static entity:** Create a `Status` static entity with a `TextDescription` attribute of type Text. Add the records `Booked`, `CheckedIn`, `CheckedOut`, and `Canceled`, and give each a description.
* **Create a one-to-one relationship:** Create a `Profile` entity that extends the `User` entity in a one-to-one relationship. Use the `User` identifier as the `Profile` identifier, and add the attributes `Twitter` (Text), `Facebook` (Text), and `Photo` (Binary Data).
* **Create a many-to-many relationship:** Create a `Review` entity as a junction between the `User` and `Place` entities in a many-to-many relationship. Add the attributes `Classification` (Integer), `Comments` (Text), and `SubmittedOn` (Date).
* **Add records:** Add three records to the `Place` entity with fictional names, addresses, and phone numbers.

## Reuse public elements

Use these prompts to reuse public elements that other apps expose in the tenant. Add the element through **Add public elements** first, or let Mentor find and add it for you.

### Prompt progression

* Basic: Use the public `CallAgent01_Intake` action to call the intake agent from a new `ProcessIntake` screen.
* Detailed: List the public elements available in this tenant, then add the `CallAgent01_Intake` action from the `LoanOrigination` app and call it from a new `ProcessIntake` screen that captures applicant documents.

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
* With a selection: Select the logic flow, then ask "Explain this."

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
