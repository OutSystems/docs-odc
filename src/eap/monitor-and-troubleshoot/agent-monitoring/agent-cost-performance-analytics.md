---
guid: edea80d1-274e-463b-9c64-c6a88cd5ac08
locale: en-us
summary: 'ODC agent performance analytics: view token consumption, P90 latency, and cost data for each agent in the OutSystems Developer Cloud Analytics console.'
figma:
coverage-type:
  - understand
topic:
  - agent monitoring
app_type: reactive web apps
platform-version: odc
audience:
  - Tech lead
  - Developer
tags:
  - AI
  - Agentic
  - Monitoring
  - Performance
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---

# View agent performance data

The Analytics console shows you token consumption and response time for every agent in your tenant.

## Compare agents in the overview

The **Agent** overview page includes two additional sortable columns:

* **Tokens** — total tokens consumed by the agent in the selected time range
* **P90 response time** — 90th-percentile latency, consistent with the P90 already shown on the agent detail page

Sort by either column to quickly identify which agents are the most expensive or the slowest, without opening each one individually. The summary header at the top of the overview shows total tokens across all agents, the same way total requests is shown today.

## View token and latency data for an agent

1. Open the **Analytics console** in the ODC Portal.
1. Search for, or select directly from the list, the agent you want to inspect.
1. On the agent detail page, you'll find:
   * **Input tokens**, **output tokens**, and **total tokens** for the selected time range
   * A trend chart showing input and output tokens as separate series over time
   * The existing **Requests** and **Response time** charts, with the addition of a P90 line on the response time chart

Use the trend chart to spot days or periods where token consumption was unusually high, and investigate what changed (a prompt edit, a model change, a spike in usage).

## Distinguish agent elements from generic elements

In the element breakdown, **CallAgent nodes** are now visually distinguished from generic Service Action infrastructure elements. Use this to focus on agent-specific behavior when diagnosing a performance issue, rather than reviewing every element in the flow.

## Time range

The time range picker offers the same presets used elsewhere in the Analytics console, from **Last 15 minutes** to **Last 1 month**, plus a **Custom** option. The maximum window is one month, aligned with the 30-day retention period for this data.
