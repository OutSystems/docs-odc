---
guid: c4e2a953-4731-4af3-ae7e-c7e4da4aeafa
locale: en-us
summary: ODC agent execution trace view in the Analytics console shows prompt, response, and tool calls for each CallAgent node per execution.
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
  - AI
  - Agentic
  - Monitoring
  - Performance
  - Troubleshooting
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---

# View an agent trace

Detailed execution traces, see how to activate [here](detailed-execution-traces.md), for an agent allow you to inspect individual executions to see exactly what the agent was prompted with, what it responded, and which tools it called.

## Before you begin

Trace content for agents' relevance and safety are only reachable through the Analytics console. You can't reach this level of detail by searching traces directly elsewhere in ODC. General trace search shows execution metadata but not agent prompt/response content.

## View a trace

1. Open the **Analytics console** and navigate to the Agentic App and Service Action you want to inspect.
1. Scroll down to the request tables (Requests with Errors , Slowest Requests, Requests by relevance score, Requests by safety score).
1. Double-click on the desired event time stamp to open the trace view.

## What you'll see

For **each CallAgent node** in the execution:

* The **Agent prompt** sent to that node (including any grounding data injected beforehand)
* The **Agent response** produced by that node
* Any **tools** the node called (tool name only)

For the execution as a whole:

* **Duration**. The complete time from invocation to response
* **Input tokens** and **output tokens**, shown separately.

## Related

* [Enable detailed execution traces for an agent](detailed-execution-traces.md)
* [Quality signals](quality-signals.md)
