---
summary: The Enterprise Context Graph indexes your tenant's apps, data, and dependencies as the knowledge layer agents read before they act.
tags:
  - Agentic development
  - Context search
  - Enterprise Context Graph
guid: 88381752-3878-49a1-8f2d-46c231f54a5a
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - portal
  - odc studio
  - mentor web
  - mentor studio
  - claude code
coverage-type:
  - understand
content-type:
  - conceptual
audience:
  - Developer
  - Architect
  - Tech lead
topic:
  - creating-apps
isautopublish: true
---

# Enterprise Context Graph

The Enterprise Context Graph is a structured, queryable representation of your tenant's full application estate. It is the knowledge layer agents read before they act, so changes build on the current state of the estate. Mentor reads this graph internally when it generates and modifies apps. From an MCP host, the agent reads the same graph through context lookups instead of downloading the app model.

## Indexed objects

The graph indexes the building blocks of your apps across the tenant.

* Entities, actions, screens, and structures.
* Roles and themes.
* AI model connections and AI agents.

From an MCP host, the agent reads these through typed context lookups, one per object kind. For the lookup tools, refer to [Tool reference](outsystems-mcp/tool-reference.md).

## App-scoped and tenant-wide queries

You query the graph for a single app or across the whole tenant.

* An app-scoped query returns the app's own objects by default. You can include the objects it inherits from referenced libraries, and each inherited result names the library that provides it.
* A tenant-wide query returns objects across all apps you can see.

## Reads from an indexed cache

Context reads are served from an indexed cache, not by downloading the app model. This keeps queries fast and avoids moving the model across the network.

## Freshness after a change

The index can lag a publish. Right after you publish a change, a query can return the previous view for a short time. When you need the current state immediately after a change, confirm it against the app rather than relying on the index alone.

## Canonical identifiers

The graph is a high-fidelity index, not a substitute for the model. Confirm a result against its canonical identifier, the asset key, because names can be edited and can collide. Treat the index as the fast way to locate things, and the canonical identifier as the reference you act on.

To find apps across the tenant, query one app step by step, and map its dependencies and dependents, refer to [Inspect apps and their dependencies](outsystems-mcp/introspect-app.md).
