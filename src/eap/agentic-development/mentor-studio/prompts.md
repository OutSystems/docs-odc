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

Use these prompts to create or modify server actions, client actions, service actions, aggregates, events, Timers, variables, and parameters, and to send emails.

### Prompt progression

* Basic: Create a server action that validates an email format.
* Detailed: Create a Server Action named `ValidateOrderTotal` that takes `OrderId` as input, retrieves all `OrderItem` records for that order, calculates the sum of `Quantity * UnitPrice`, and returns the `TotalAmount`. Include error handling for cases where the order doesn't exist.

### Aggregate prompts

Use these prompts as starting points to filter, sort, and join the data that an aggregate returns. Replace the element names with the names in your app.

* **Filter an aggregate:** In the `GetEmployees` aggregate, add a filter so that it returns only the employees whose `City` is London.
* **Sort an aggregate:** In the `GetEmployees` aggregate, sort the results by `FirstName` in ascending order.
* **Add a dynamic sort:** In the `GetOrders` aggregate, add a dynamic sort that uses a Text variable named `SortBy`. Users can sort by `Order.OrderDate`.
* **Return distinct values:** Create an aggregate that returns the distinct values of the `City` attribute of the `Employee` entity.
* **Add a calculated attribute:** In the `GetProducts` aggregate, count `Product.Id` for each group of `Category.Id` and `Category.Label`. Add a calculated attribute named `DropdownLabel` that shows the label followed by the count in parentheses.
* **Join an external entity:** In the `GetOrdersWithCustomers` aggregate, add the external `Customer` entity as a source with a With or Without join to `Order` on `CustomerId`.

### Email prompts

Use these prompts as starting points to send an email and attach files to it from a server action. Replace the element names with the names in your app.

* **Send an email:** Create a server action named `SendRegistrationConfirmation` that sends the `RegistrationConfirmation` email. Add an input parameter named `Recipient` of type Text for the To field. For each input parameter of the email, add an input parameter with the same name and data type, and pass it to the email.
* **Attach a file:** In the `SendOrderConfirmation` server action, attach the PDF resource `sample_pdf` to the Send Email node with the file name `sample.pdf` and the media type `application/pdf`.
* **Attach a list of files:** In the `SendProductCatalog` server action, fetch five records of the `Sample_ProductImage` entity and attach them to the Send Email node. Use `FileName` as the file name and `FileContent` as the content.

### Event prompts

Use these prompts as starting points to create events, handle them, and trigger them from database changes. Replace the element names with the names in your app.

* **Create an event:** Create a public event named `OnPurchaseStarted` with an input parameter `ProductId` of type Product Identifier. Trigger it at the end of the `PlacePurchase` server action, and handle it in this app with a new server action named `UpdateStock`.
* **Handle an event from another app:** Handle the public `OnPurchaseStarted` event from the `Storefront` app with a new server action named `CheckFraud`, and log any exception with the All Exceptions handler.
* **Add a database event:** Add an `OnUpdate` database event to the `Payment` entity that triggers the `PaymentUpdated` event with the `Payment` identifier as its input parameter, and handle `PaymentUpdated` with a new server action named `NotifyAccountOwner`.

### Server action prompts

Use these prompts as starting points for server actions that wrap entity actions or convert data between records and Excel. Replace the element names with the names in your app.

* **Wrap entity actions:** Create server actions that wrap the Create, Update, and Delete entity actions of the `Product` entity. Validate the mandatory attributes before saving, and set `CreatedOn` and `CreatedBy` when a record is created.
* **Export to Excel:** Create a server action named `ExportEmployeeToExcel` with a Binary Data output parameter named `ExcelContent`. Fetch the `Employee` entity with an aggregate, convert `GetEmployees.List` with Record List to Excel, and assign the result to `ExcelContent`. Exclude the `Employee.Address` attribute from the export.
* **Import from Excel:** In the `ImportEmployees` server action, use Excel to Record List to read the uploaded file with the `Employee` entity as the record definition. Call `CreateOrUpdateSomeEmployees` with the resulting list as the source list.

### Timer prompts

Use this prompt as a starting point to schedule a server action with a Timer. Replace the element names with the names in your app.

* **Create a Timer:** Create a Timer named `ArchiveOldOrders` that runs a new server action named `ArchiveOrders` every day at 2:00 AM, with a timeout of 30 minutes. In `ArchiveOrders`, set `IsArchived` to True for the `Order` records that are older than 365 days.

### Variable and parameter prompts

Use these prompts as starting points to create variables and parameters, and to bind them to widgets and logic. Replace the element names with the names in your app.

* **Create a local variable:** Create a Text local variable named `SearchKeyword` on the `Employees` screen. Bind it to the Search input, and filter the `Employee` aggregate by `FirstName` using the variable.
* **Create a client variable:** Create a client variable named `SearchKeyword` of type Text. Bind it to the Search input on the `Employees` screen, and filter the `Employee` aggregate by `FirstName` using the variable.
* **Add parameters:** In the `GetWeatherData` client action, add an output parameter `WeatherInfo` and the mandatory Text input parameters `City` and `Country`. Assign `WeatherInfo` the `Data` output of `API_GetWeatherData`.

## UI

Use these prompts to create or modify screens, web blocks, and layouts.

### Prompt progression

* Basic: Create a screen to list all Customer records.
* Detailed: Create a screen named `OrderDashboard` that displays a summary of orders by status. Include a table showing `OrderId`, `CustomerName`, `OrderDate`, and `Status`. Add a filter dropdown for `Status` and sort by `OrderDate` descending.

### UI prompts by task

Use this prompt as a starting point for an email template. Replace the element names with the names in your app.

* **Create an Email:** Create an Email named `WelcomeEmail` with the subject `Welcome`. Add a mandatory input parameter named `Handle` of type Text. Add a Text widget and an Expression widget that displays `"Hello, " + Handle + "!"`.

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

These prompt examples are starting points that you can adjust based on your app's structure and complexity. The following resources cover general strategies, the full range of Mentor Studio capabilities, and how to continue past conversations.

* For prompting strategies that apply across all Mentor tools, including entity-first thinking and decomposition, refer to [Effective prompts for Mentor](../effective-prompts.md).
* For the full list of elements that Mentor Studio supports, including logic, UI, and data, refer to [Capabilities and patterns for Mentor Studio](capabilities.md).
* For how Mentor Studio processes requests and integrates changes with existing apps, refer to [AI development in Mentor Studio](how-it-works.md).
* For how to find, search, and resume your past Mentor Studio conversations, refer to [Find and resume past conversations in Mentor Studio](conversation-history.md).
* For UI pattern prompts and app generation examples in Mentor Web, refer to [Prompts for Mentor Web](../mentor-web/prompts.md).
