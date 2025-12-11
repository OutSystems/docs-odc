---
summary: Use requirement documents to provide a blueprint for apps with data models, roles, and screen requirements.
tags: requirement documents, ai mentor, app generation, best practices, documentation
guid: da1fc397-5aff-4513-b531-df5f58c29af0
locale: en-us
app_type: reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=8327-67&p=f&t=Wym62fkSpj2wy7Rs-0
outsystems-tools:
  - portal
  - ai mentor
coverage-type:
  - apply
audience:
  - frontend developers
  - backend developers
  - full stack developers
  - ui designers
topic:
  - creating-apps
---

# Use requirement documents

While short prompts are good for generating simple apps and making quick changes, a requirement document acts as a blueprint for more complex apps. This "scaffold and refine" workflow lets you provide Mentor with a structured foundation that you can then iterate on using Mentor App Editor and prompts.

Use a well-structured document to define a detailed data model, establish specific roles and permissions, and lay out your screen requirements from the start.

![Best practices for requirement documents: formats, structure, settings, integrations, focus, relevance](images/requirement-best-practices-ams.png "Best Practices for Requirement Documents")

## Supported formats and limits

You can upload requirement documents in the following formats:

* `.txt`
* `.docx`
* `.pdf`

The maximum file size is 5 MB.

## Structure your requirement document

Structure your requirement document so Mentor has the context required to generate accurate data models, screens, and business logic. Use consistent sections to explain the app purpose, user roles, data relationships, and interface expectations. Review the sample documents later in this guide to see the structure in practice.

### Follow recommended document structure

Use the following table as a checklist when preparing your requirement document. Each row summarizes what to include and whether the section is optional.

| Section | Required | What to include | Example details |
| --- | --- | --- | --- |
| App overview | Yes | Purpose of the app, high-level goals, key users | 1-2 paragraph description of the business problem and desired outcome |
| General app settings | Optional | Theme, branding, localization, accessibility requirements | `"Use the 'Mentor' theme available in the ODC tenant."` |
| Data model | Yes | Entities with data types, relationships, static entities and records | List entities such as `Employee`, `OnboardingStep`; specify relationships (One-to-Many, Many-to-Many) and static lookups |
| Roles and permissions | Yes | Roles, entity-level access, row-level rules, special permissions | Define access by role (Full/Edit/View) and note any ownership-based restrictions |
| Main features and screens | Yes | Screen list, layouts, dashboard expectations, UX notes | Identify screen patterns (table, master detail) and required charts or counters |
| External integrations | Optional | External data sources, system dependencies, integration direction | `"Customer data is sourced from Salesforce."` |

### Specify data types for attributes

When defining entity attributes, include a data type so Mentor generates the correct fields and validations. Use the table below to match each attribute to the appropriate type.

| Data type | Typical use |
| --- | --- |
| Identifier | Primary keys, foreign keys, bridging entities |
| Text | Names, descriptions, addresses, free-form notes |
| Boolean | True/false flags such as `IsActive` or `RequiresApproval` |
| DateTime / Date | Timestamps, scheduled dates, deadlines, birth dates |
| Currency | Monetary values, subscription fees, total amounts |
| Integer | Quantities, counts, ranking positions |
| Email | Business or personal email addresses |
| Phone Number | Mobile, landline, or contact center numbers |
| User Identifier | References to OutSystems users or identities |

Here is an example of an entity definition with attributes and their data types:

```
Entity: Product
- Id: An Identifier that serves as the Primary Key
- Name: Text, the product name
- Price: Currency, the current price
- StockQuantity: An Integer representing current stock
- IsActive: Boolean, whether the product is available
```

### Examples of well-structured content

Use these examples as patterns when drafting each portion of your requirement document. They demonstrate how to translate business intent into precise statements Mentor can interpret.

#### Entity definition with relationships

Describe entities by listing their attributes with data types and by explaining how entities connect.

```
Entity: Order
This entity is stored locally.
Attributes include:
- Id: An Identifier that serves as the Primary Key
- OrderNumber: Text, an auto-generated unique identifier
- OrderDate: DateTime, timestamp of when the order was placed
- CustomerId: An Identifier that is a Foreign Key to the Customer entity
- StatusId: An Identifier that is a Foreign Key to the OrderStatus static entity

Entity Relationships:
- A Customer can have many Orders (One-to-Many)
- An Order can have many OrderItems (One-to-Many)
```

#### Static entity with records

Static entities define lookup values. List the purpose and enumerated records.

```
Entity Name: OrderStatus
Purpose: Defines the possible states of an order throughout its lifecycle
Records: Pending, Confirmed, Processing, Shipped, Delivered, Cancelled
```

#### Role with permissions

Document roles by specifying entity-level access and any special considerations.

```
Role: Sales Rep
- Order: Edit Access
- OrderItem: Edit Access
- Customer: View Access
- Product: View Access
```

#### Dashboard specification

When requesting dashboards, state the elements and aggregation types Mentor should generate.

```
Dashboard should consist of:
- Total Active Orders as a counter
- Pending Orders as a counter
- Orders by Status as a Donut Chart
- Revenue by Month as a Vertical Bar Chart
```

## Include and avoid

Include the following types of content in your requirement document and avoid content that Mentor can't process.

### Include in your requirement document

* **Detailed entity definitions**: Specify data types (Text, Identifier, Boolean, DateTime, Currency, etc.) and field purposes
* **Explicit relationships**: State how entities connect (One-to-Many, Many-to-Many)
* **Functional requirements**: Describe what the app should do and how users interact with it
* **Specific UI layouts**: Indicate preferred screen types (gallery, card list, master-detail, table, map view)
* **Dashboard specifications**: List specific charts and counters to include
* **Business logic and workflows**: Define rules and processes
* **Access control details**: Specify entity-level and row-level permissions

### Avoid in your requirement document

* **Implementation code**: Don't include code snippets or technical implementation instructions
* **Screenshots or embedded images**: They aren't processed by Mentor
* **Complex tables**: Use simple lists and clear text instead
* **Ambiguous language**: Be specific rather than using vague terms like "user-friendly" or "intuitive"

## Sample requirement documents

The following sample documents demonstrate requirement structures for different types of apps. Use these as templates to create your own requirement documents.

* [Employee Onboarding Requirements Document](resources/employee-onboarding-requirements.docx): HR app example covering employee data management, onboarding workflows, and role-based access for HR teams and managers
* [Order Management System Requirements Document](resources/order-management-system-requirements.docx): E-commerce example including order processing, customer management, product catalog integration, and multi-role permissions
* [IT Service Management Requirements Document](resources/it-service-management-requirements.docx): Help desk example covering ticket management, comment systems, role-based access, and status tracking workflows

## Related

* [Prompting guide](prompts.md)
