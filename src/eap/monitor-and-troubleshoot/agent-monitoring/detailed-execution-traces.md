---
guid: ca21828f-de73-42dc-acef-d48acda045cd
locale: en-us
summary: ODC detailed execution traces record agent prompts, responses, and tool calls per execution; enable per agent in the ODC Portal Configuration tab.
figma:
coverage-type:
  - understand
  - apply
topic:
  - agent monitoring
app_type: reactive web apps
platform-version: odc
audience:
  - Tech lead
  - Developer
tags:
  - Agentic
  - AI
  - Debugging
  - Logging
  - Monitoring
  - Quality Assurance
  - Troubleshooting
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---

# Enable detailed execution traces for an agent

Detailed execution traces capture what an agent was actually prompted with, what it responded, and which tools it called, per execution, per stage. This gives you the evidence needed to diagnose an unexpected response without having to reproduce the issue in a development environment.

Nothing is captured until you configure the traces for an agent.

Also, **note that agent traces are only available through the Analytics console.** You can't reach agent traces through the traces screen.

## Before you begin

* Review [what's captured](#what-gets-captured) before enabling, since this feature stores prompt and response content that may include data your users entered.
* You need to activate the **Show detailed execution data** for every agent that you desire to have monitoring and to view traces afterward.

## Enable monitoring for the agent

To have the detailed execution data, each agent needs to be individually enabled.

1. Go to the agent in the ODC Portal.
1. Go to the **Configuration** tab.
1. Under **Monitoring and Troubleshooting**, turn on **Show Detailed Execution Data**.

From this point forward, every execution of this agent is captured and available in the Analytics console. Turning this off stops new captures; it doesn't delete traces already recorded.

## What gets captured

For each production execution, the platform records:

| Field | Granularity | Notes |
| --- | --- | --- |
| Agent prompt | Per CallAgent node | Includes any grounding data injected before the agent call |
| Agent response | Per CallAgent node | |
| Tool selection | Per CallAgent node | Tool name only, parameters aren't captured |
| Input tokens / output tokens | Per CallAgent node | Shown as separate values |

## Retention

* Trace records are retained for **30 days** and permanently deleted after that.
* There is no configurable retention period.

## Next steps

Once enabled, see [view a production trace](view-a-production-trace.md) to browse and inspect individual executions.
Also, understand [quality signals](quality-signals.md) to see what is relevant to monitor in your agent's answer relevance and safety.
