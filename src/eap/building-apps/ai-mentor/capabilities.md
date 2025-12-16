---
summary: Learn what Mentor can generate and recognize, including data models, authorization rules, dashboards, and UI layouts with AI-powered suggestions.
tags: app generation, data integration, entity management, authorization, dashboard creation
guid: bd40bfc1-f77a-4604-80de-17f457d45603
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - portal
  - ai mentor
coverage-type:
  - understand
audience:
  - frontend developers
  - backend developers
  - full stack developers
  - ui designers
topic:
  - creating-apps
---

# Capabilities and patterns

This page describes the components and patterns that Mentor App Generator and Mentor App Editor can create and modify. Mentor App Generator builds initial apps from prompts or requirement documents. Mentor App Editor provides tools to refine existing apps through prompts or AI-powered suggestions.

The capabilities described here apply to web apps in OutSystems Developer Cloud (ODC). Mentor automatically handles data binding, screen generation, authorization rules, and UI patterns based on the data model and user input.

## Mentor App Generator

Mentor App Generator converts natural language prompts or requirement documents into functional apps. During generation, the tool analyzes your input to identify entities, relationships, user roles, and UI requirements. It then applies design patterns and generates screens, data models, and authorization rules automatically.

The following table lists capabilities available during app generation.

| Area | Capability | Description |
| ------ | ------------ | ------------- |
| **Data and entities** | Data integration | Integrates with Data Fabric and public entities with read/write support |
| | Data manipulation | Edit entities before generation by adding, changing, or removing suggested entities and attributes |
| | Static entity detection | Detects static entities and related records and displays them as tags in the UI for status or task management use cases |
| | Data management | Download existing data or upload new data to replace sample data |
| | Field-level validation | Generates client-side validation rules including mandatory fields, past/future date checks, value range enforcement (numeric, text length, phone number format), and email validation |
| **Security** | Predefined roles | Analyzes your app context and suggests a set of roles that you can modify before generation |
| | Authorization rules | Supports entity-level authorization controlling which entities can be read or edited by available roles. Also supports logged-in user permissions, such as viewing or editing their own records or records associated with their team or department |
| **Screen generation** | Screen pattern selection | Selects patterns based on entity attribute count and relationships (for example, popup for entities with 5 or fewer non-ID attributes, table for entities with more attributes). Supports Tab patterns for organizing related content |
| | Context-aware screen layouts | Generates layouts based on data context (for example, list with map view for entities containing addresses, card layout for personal attributes) |
| | Theme application | Applies public themes when specified in the prompt or requirement document. Supports custom themes based on specific guidelines or uses the default OutSystems UI |
| | UI styling | Suggests styling elements such as primary color and icon based on app context |
| | AI-suggested icons | Suggests and applies Font Awesome icons for each menu item and the app logo |
| **Dashboards** | Dashboard generation | Generates dashboards with column layouts (2 to 6 equal columns or asymmetric 2:1 or 3:1 ratios), counters and charts with aggregation functions (Count, Sum, Average, Minimum, Maximum), date and status filters, chart types (Bar, Column, Line, Pie, Donut, Area), and lists (maximum 5 records) |

## Mentor App Editor

Mentor App Editor provides tools and AI-powered suggestions to refine and evolve generated apps. The following table lists capabilities available through prompts or AI suggestions.

| Capability | Operations | Automatic updates |
| ------------ | ------------ | ------------------- |
| **Entity management** | Add, replace, or delete local entities; add or delete external entity references from Data Fabric or public entities; convert external entities to local entities; add static entities for enumerations | References update automatically |
| **Attribute management** | Add, replace, delete, or change the data type of entity attributes | Screens and bindings update automatically |
| **Screen management** | Add, rename, or delete screens; add or remove attributes from screens; change screen permissions | Adding a screen creates the corresponding menu item |
| **Screen patterns** | Add map view to lists; add master-detail or popup layouts | Respects entity constraints (for example, entities with more than 5 attributes cannot use popup pattern) |
| **Role & authorization** | Add or delete user roles; configure entity-level authorization rules; adjust logged-in user permissions | Access rules update automatically |
| **Static entity records** | Add or delete records in static entities with automatic cleanup of dependent elements | Deleting a record removes counters from screens that reference the deleted value, and validates affected workflows |
| **App actions** | Undo or redo the last action; publish app; preview app | Undo and redo apply to the most recent change |

<div class="info" markdown="1">

**About stateflows:** In Mentor, a stateflow models an entity's lifecycle. It defines statuses (for example, `Draft`, `Submitted`, `Approved`) and the allowed transitions between them. Each transition can specify conditions, such as which roles can perform it and which attributes must be provided. At runtime, records can move only along the defined transitions.

</div>

### Additional capabilities

Mentor offers the following additional capabilities.

* **AI-powered suggestions**: Analyzes apps and suggests additions or modifications to entities, attributes, security roles, and static entity enumerations. Supports many-to-many structures and both local and external entities
* **WYSIWYG refinement**: Provides immediate preview of screens and data models with automatic validation. Converts patterns when entity structure changes and applied suggestions appear with sample data
* **App customization**: Supports customizing app name and icon

## Limitations

The following limitations apply to the current release.

* **Screen layout patterns**: Changing a screen's layout pattern (for example, from table to card list) requires replacing the screen
* **Filters and search**: Filter controls, sorting, and search inputs require manual configuration in ODC Studio

## Related

* [Prompting guide](prompts.md)
* [Using requirement documents](requirements-doc.md)
* [Mentor and the software development lifecycle](sdlc.md)
