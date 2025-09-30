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

Use this cookbook to compose clear prompts for layouts and UI patterns Mentor can generate or refine. It complements the concepts in "About Mentor App Generator and Editor" by focusing on UI expression: turning layout intent, entity structure, static values (tags), roles, and refinement steps into safe model updates. Mentor interprets pattern keywords (table, card list, master detail, map), associates them with the entities and attributes you mention, and updates screens without raw code. Favor incremental refinement prompts over broad restatements.

Goals

* Pick an appropriate pattern.
* Combine layout intent with entities, roles, and actions.
* Iterate with refinement prompts instead of regenerating from scratch.

Pattern names are recognized flexibly. You can say "card list" or "cards list". Focus on intent and data.

## Pattern selection quick guide

Use this table to choose a UI pattern based on your dataset shape, visual emphasis, and refinement needs.

| Pattern | Use for | Avoid when | Common refinements |
|---------|---------|------------|--------------------|
| Table | Dense tabular comparison; many columns | Highly visual summaries; mobile card-first | Add calculated column |
| Card list | Visual scanning of records with key attributes | Need wide column comparison | Add tags, actions on each card |
| Card gallery | Image-centric content (products, media) | Text-heavy data | Add category filter, lazy load |
| Master detail | Fast browse + inspect a record | Very small datasets | Add tabs, related lists |
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

### Table

![Table](images/sample-table.png "Table layout with sortable columns")

When to use: Compare many records across consistent attributes.  
Avoid when: You need visual emphasis or a card metaphor.

Prompt progression

* Basic: List `Product` records in a table.
* Better: List `Product` records in a table with columns: `Name`, `SKU`, `Stock`, `Price`.

### Card list

![Card list](images/sample-card-list.png "Card list showing items as cards")

Use when each record benefits from a visual block with a few key fields.

Prompt progression

* Basic: Show `Employee` records as a card list.
* Better: Show `Employee` records as a card list with `Name`, `Department`, `Role`, and a colored tag for `Status`.

### Card gallery

![Card gallery](images/sample-card-gallery.png "Card gallery with image focus")

Use for image or media-heavy datasets.

Prompt progression

* Basic: Show `Product` records as a card gallery with image and `Name`.
* Better: Show `Product` records as a gallery with image, `Name`, a category tag, and `Price`.

## Master detail and in-place detail patterns

### Master detail

![Master detail](images/sample-master-detail-screen.png "Master detail layout")

Prompt progression

* Basic: Use a master detail layout for `Customer` records.
* Better: Master detail for `Customer` records with list on the left (`Name`, `Segment`) and right panel tabs: Profile, Orders, Notes.

### Card list with detail in sidebar

![Card list with detail on sidebar](images/sample-card-list-with-detail-on-sidebar.png "Card list with side detail panel")

Use when detail editing is frequent and the list context must remain.

Prompt progression

* Basic: Card list with detail in a sidebar for `Project` records.
* Better: Card list (`Name`, `Owner`, `Status` tag). Selecting a card opens a sidebar with `Description` and `DueDate`.


## Spatial patterns

### Card list with map

![Card list with map](images/sample-card-list-with-map.png "Card list with map context")

Use when location supports decision making.

Prompt progression

* Basic: Card list with map for `FieldWorkOrder` records.
* Better: Card list with map for `WorkOrder` records (`Title`, `AssignedUser`, `Status` tag, `Address`). Map uses markers at `Address`.

## Multi-pattern scenarios

### Asset tracking scenario

Initial prompt: Create an Asset Tracking app with a dashboard (total assets, assets needing maintenance), a card list with map for `Asset` records, and a side menu (Dashboard, Assets, Maintenance).

### Customer management scenario

Initial prompt: Create a master detail layout for `Customer` records with tabs Profile, Orders, Tickets. Include a dashboard with total customers and open tickets.

## Refinement strategies

If the pattern choice was wrong, request a replacement: Change the current layout to a master detail layout for `Customer` records.

Current limitation: Mentor suggestions support add operations only (no rename or change). Rephrase changes as additions where possible. Filters, sorting controls, and search inputs are not generated from prompts at this time. The navigation layout (horizontal vs side) applies globally.

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

* For more information about natural language prompts, refer to [About Mentor App Generator and Editor](intro.md).
* For more information about requirement documents, refer to [About Mentor App Generator and Editor](intro.md).
