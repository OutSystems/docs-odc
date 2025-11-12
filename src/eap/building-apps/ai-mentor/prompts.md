---
summary: Use concise prompts to request specific UI patterns and layouts that Mentor can generate or refine.
tags: ui patterns, components, prompts, mentor, reactive web apps
guid: 4719a8d7-dea6-491c-879c-47c57e88f6c1
locale: en-us
app_type: reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=8087-2&p=f&t=rgnVMRZqI2WrC6iK-0
outsystems-tools:
  - portal
coverage-type:
  - understand
  - apply 
audience:
  - frontend developers
  - backend developers
  - full stack developers
  - ui designers
---

# Prompts cookbook

Use this cookbook to compose clear prompts for layouts and UI patterns Mentor can generate or refine. It complements "About Mentor App Generator and Editor" by focusing on UI expression: turning layout intent, entity structure, static values, roles, and refinement steps into model updates. Mentor interprets pattern keywords (table, card list, master detail, map), associates them with the entities and attributes you mention, and updates screens without raw code. Favor incremental refinement prompts over broad restatements.

## Using this cookbook effectively

This guide helps you achieve three key outcomes:

* **Pick an appropriate pattern** - Use the Pattern selection quick guide to match your data and use case.
* **Combine layout intent with entities, roles, and actions** - Structure prompts with specific details rather than vague descriptions.
* **Iterate with refinement prompts** - Add or adjust features incrementally instead of regenerating from scratch.

Pattern names are recognized flexibly. You can say "card list" or "cards list". Focus on intent and data.

## Pattern selection quick guide

Use this table to choose a UI pattern based on your dataset shape, visual emphasis, and refinement needs.

| Pattern | Use for | Avoid when | Common refinements |
|---------|---------|------------|--------------------|
| Dashboard | High-level KPIs, metrics summary, and data visualization at a glance | Detailed record editing or browsing individual items | Add counter with aggregation function, add chart type |
| Table | Dense tabular comparison; many columns | Highly visual summaries; mobile card-first | Add calculated column |
| Card list | Visual scanning of records with key attributes | Need wide column comparison | Add tags, actions on each card |
| Card gallery | Image-centric content (products, media) | Text-heavy data | Add category filter, lazy load |
| Master detail | Fast browse and inspect a record | Very small datasets | Add tabs, related lists |
| Card list with detail (sidebar) | Keep list visible while editing | Screen space is limited | Add inline edit for key field |
| Card list with map | Geo context alongside list | No location data | Add clustering, status tags |

## How to structure prompts

Include the following when relevant:

* Entity or dataset name
* Fields to show (prioritize key ones)
* Actions or permissions
* Layout/pattern keyword
* Optional: tabs, status tags, map usage, theme

Avoid vague phrases like "make it nicer". Be explicit about the change.

## Lists and tabular patterns

These patterns organize multiple records for browsing, comparison, or selection. Choose based on data density and visual emphasis needs.

### Table

![Table](images/sample-table.png "Table layout with sortable columns")

Use when you need to compare many records across consistent attributes.  
Avoid when you need visual emphasis or a card metaphor.

**Prompt progression**

Start with basic prompts and add details for better results:

* Basic: List `Product` records in a table.
* Better: List `Product` records in a table with columns: `Name`, `SKU`, `Stock`, `Price`.

### Card list

![Card list](images/sample-card-list.png "Card list showing items as cards")

Use when you need to display records as visual blocks with a few key fields.

**Prompt progression**

* Basic: Show `Employee` records as a card list.
* Better: Show `Employee` records as a card list with `Name`, `Department`, `Role`, and a colored tag for `Status`.

### Card gallery

![Card gallery](images/sample-card-gallery.png "Card gallery with image focus")

Use when you have image or media-heavy datasets.

**Prompt progression**

* Basic: Show `Product` records as a card gallery with image and `Name`.
* Better: Show `Product` records as a gallery with image, `Name`, a category tag, and `Price`.

## Dashboard patterns

![Dashboard](images/sample-dashboard.png "Dashboard with counters and charts")

Use dashboards to display high-level KPIs, metrics, and data summaries for quick insights. Dashboards combine multiple visual elements to provide at-a-glance understanding of key business data.

Avoid when you need detailed record editing or browsing individual items.

### Supported patterns

* **Counters**: Highlight key metrics in a prominent visual format.
* **Charts**: Visualize data trends and distributions. Supported chart types include:
    * Vertical bar chart
    * Horizontal bar chart
    * Line chart
    * Pie chart
    * Donut chart
* **Lists**: Display top elements, most recent records, or latest items.

### Supported aggregation functions

Dashboards support the following aggregation functions on counters and charts:

* **Count**: Total number of records.
* **Sum**: Total of a numeric field across records.
* **Avg**: Average value of a numeric field.
* **Max**: Maximum value of a numeric field.
* **Min**: Minimum value of a numeric field.

**Prompt progression**

* Basic: Create a dashboard with total orders counter.
* Better: Create a dashboard with a counter for total orders (Count), a vertical bar chart for sales by month (Sum of `OrderValue`), and recent orders list.
* Advanced: Add a pie chart showing order distribution by category (Count of `Order` grouped by `Category`).

## Master detail and in-place detail patterns

These patterns let users browse a list and view or edit record details simultaneously. Choose based on screen space and editing frequency.

### Master detail

![Master detail](images/sample-master-detail-screen.png "Master detail layout")

Use when you need to browse records and view details without navigating away from the list.

**Prompt progression**

* Basic: Use a master detail layout for `Customer` records.
* Better: Master detail for `Customer` records with list on the left (`Name`, `Segment`) and right panel tabs: Profile, Orders, Notes.

### Card list with detail in sidebar

![Card list with detail on sidebar](images/sample-card-list-with-detail-on-sidebar.png "Card list with side detail panel")

Use when you need frequent detail editing and the list context must remain.

**Prompt progression**

* Basic: Card list with detail in a sidebar for `Project` records.
* Better: Card list (`Name`, `Owner`, `Status` tag). Selecting a card opens a sidebar with `Description` and `DueDate`.

## Spatial patterns

These patterns add location context to help users make geography-based decisions.

### Card list with map

![Card list with map](images/sample-card-list-with-map.png "Card list with map context")

Use when location information supports decision making.

**Prompt progression**

* Basic: Card list with map for `FieldWorkOrder` records.
* Better: Card list with map for `WorkOrder` records (`Title`, `AssignedUser`, `Status` tag, `Address`). Map uses markers at `Address`.

## Multi-pattern scenarios

Combine multiple patterns in a single prompt to create complete app experiences. These examples show common pattern combinations.

### Asset tracking scenario

Initial prompt: Create an Asset Tracking app with a dashboard (total assets, assets needing maintenance), a card list with map for `Asset` records, and side menu.

### Customer management scenario

Initial prompt: Create a master detail layout for `Customer` records with tabs Profile, Orders, Tickets. Include a dashboard with total customers and open tickets.

## Refinement strategies

Use these approaches to adjust patterns or add functionality without starting over.

If you chose the wrong pattern, request a replacement: Change the current layout to a master detail layout for `Customer` records.

Mentor suggestions support add operations. To modify existing elements, rephrase changes as additions. Note: Filters, sorting controls, and search inputs require manual configuration. The navigation layout (horizontal or side) applies to your entire app.

## Troubleshooting

Use these targeted fixes when the output doesn't match the prompt intent.

Issue: Pattern not applied.  
Action: Re-specify the entity, pattern, and key fields in one prompt.

Issue: Missing fields.  
Action: Add `FieldName` to the `Entity` list.

Issue: Wrong layout.  
Action: Change layout to `PreferredPattern` for `Entity`.

Issue: No map shown.  
Action: Confirm the entity has an address or location attribute and restate: Show map next to list using `Location`.

## Glossary

Quick reference for terms used in the prompt examples.

* Card list: List of records as uniform cards.
* Card gallery: Image-first variant of a card list.
* Master detail: Two-pane list plus selected record details.
* Sidebar (side panel): Persistent vertical navigation or detail area.
* Tag: Visual label for a static entity value (status, priority).

## Related

* Learn about [natural language prompts and requirement documents](intro.md).
