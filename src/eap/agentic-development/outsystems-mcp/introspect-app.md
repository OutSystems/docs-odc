---
summary: Find apps in your tenant, inspect an app's structure, and map its dependencies and dependents from your MCP host.
tags: introspect, app structure, mcp host, context graph, context search, dependencies, integration mapping, tutorial, agentic development
guid: bc0cf5c3-beff-44c5-919b-4de2dc7d1e11
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - claude code
coverage-type:
  - apply
content-type:
  - tutorial
audience:
  - Developer
  - Architect
topic:
  - creating-apps
isautopublish: true
---

# Inspect apps and their dependencies

This tutorial shows you how to use OutSystems MCP to find apps across your tenant from your MCP host and read one app's full structure. It also shows you how to map what the app depends on and what depends on it. Understanding an app before you change it helps you write accurate prompts and find problems before you deploy.

Most of these lookups read the Enterprise Context Graph. For more information about how the index works and its freshness limits, refer to [Enterprise Context Graph](../context-graph.md).

This tutorial uses these placeholders. Replace the following:

* `APP_NAME`: the app you inspect.
* `TARGET_STAGE`: the stage you plan to deploy the app to, for example QA.

## Prerequisites

You need the following before you start:

* An MCP host connected to your tenant. Refer to [Get started with OutSystems MCP](get-started.md).
* An app that has been published at least once, so the context graph has indexed it.

## Step 1: Find apps and elements in the tenant

Start with a tenant-wide search when you don't know which app holds what you need. The search spans every app you can see, and you can narrow it to one object type, such as entities or screens, or to one app.

For example, ask the agent:

* "Find the apps and elements in my tenant that handle orders."

The search reads the context graph, so an empty result means nothing in the index matches your terms. Try a different term, or the exact name of an element. Pick the app you want to inspect, and note its asset key.

## Step 2: Read the app details

Confirm the app exists and read its top-level details. The agent returns the app's name, type, asset key, and current revision number.

Ask the agent:

* "Show me the details of `APP_NAME`."

Confirm the asset key in the response. Use this key for all subsequent queries, because names can be edited and can collide across the tenant.

## Step 3: Query the data model

Query the app's entities to understand its data model. Scope the query to the app so it returns only entities related to this app.

Ask the agent:

* "List the entities owned by `APP_NAME`."

By default, when you scope a query to an app, the lookup returns only entities the app owns. Each entity result includes an `isReferenced` field. The value `false` means the app owns the entity. The value `true` means the entity is inherited from a referenced library, such as OutSystems UI or a Forge component, and the `producerAssetName` field names that library.

To include inherited entities alongside owned ones, ask explicitly.

Ask the agent:

* "List all entities in `APP_NAME`, including inherited ones."

The response includes inherited entities, each tagged with the name of the library that provides it. Group inherited entities by their providing library to understand which data the app uses from each library.

## Step 4: Query logic, UI, and security

The same query pattern from Step 3 applies to every object type the context graph indexes.

The following table lists the object types you can query and what each returns.

| Object type | Returns |
| --- | --- |
| Actions | Server and client actions |
| Screens | Screens |
| Structures | Data structures |
| Roles | Security roles |
| Themes | UI themes |
| Connections | AI model connections |
| AI agents | AI agents in the tenant, or the ones the app references |

Every object type supports the same app scope, owned-only filter, and paging as the entities in Step 3.

Ask the agent:

* "Describe the screens, actions, roles, and structures in `APP_NAME`."

The agent reports the results together.

## Step 5: Paginate large results

Context queries return a capped result set. The response reports the total count, whether more results exist, and where the next page starts.

When the response indicates that more results exist beyond the current page, ask for the next page.

Ask the agent:

* "List the next page of entities in `APP_NAME`."

The agent passes the paging position to the lookup. Continue paging until the response indicates no more results.

## Step 6: Map dependencies and dependents

Before you change the app, map what it depends on and what a deploy affects.

For dependencies, ask the agent:

* "What does `APP_NAME` depend on?"

The response lists the modules and libraries the app uses, read from the context graph. Each reference includes the name and key of the artifact that provides it. When the graph has no data for the app, the lookup returns the dependencies the app declares instead, and the response names the source it used. To list the AI model connections an app uses, query connections for the app, as in Step 4.

For dependents, ask the agent:

* "What would deploying `APP_NAME` to `TARGET_STAGE` affect?"

The agent runs a deployment-impact analysis in the background and polls until the analysis finishes. The analysis leaves your apps unchanged, and your MCP host can still ask you to confirm before it starts. The analysis covers the app's latest deployed revision, so the app must be deployed to at least one stage. The analysis includes only changes you've published. For the deploy workflow this analysis feeds into, refer to [Evolve an existing app](evolve-app.md).

## Verify the inspection

Confirm the inspection covers the app's full structure by asking the agent for a summary.

Ask the agent:

* "Summarize the structure of `APP_NAME`."

Confirm the summary covers entities, screens, actions, roles, and dependencies. If a lookup returned empty results, the index doesn't include the app's latest changes yet. For more information, refer to [Freshness after a change](../context-graph.md#freshness-after-a-change). When the graph has no data for the app, the dependency list from Step 6 falls back to the dependencies the app declares.

## Related tasks and index coverage

A few related tasks fall outside this tutorial:

* These queries return the object types the context graph indexes. For more information about what the index covers, refer to [Enterprise Context Graph](../context-graph.md).
* This tutorial reads apps. To change one, refer to [Evolve an existing app](evolve-app.md).
* ODC Portal shows app health across all stages in the tenant. Refer to [Monitoring and troubleshooting apps](../../monitor-and-troubleshoot/monitor-apps.md).

## Related

The following pages provide additional context for this workflow:

* [Enterprise Context Graph](../context-graph.md): how the index works and its freshness limits.
* [Evolve an existing app](evolve-app.md): change, publish, and deploy an app.
* [Tool reference](tool-reference.md): the context lookup tools, under Context Services.
