---
guid: 1b618c3e-ffcf-480b-a0a7-74a9d567aec5
locale: en-us
summary: OutSystems Developer Cloud (ODC) agent quality signals explain answer relevance and safety scoring to help you assess and improve agent performance.
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
  - Agentic
  - AI
  - Monitoring
  - Performance
  - Quality Assurance
  - Security
  - Troubleshooting
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---

# Quality signals

When you have the detailed execution traces enabled, you can evaluate your agents using two judges. Answer relevance and Safety. These two quality metrics are important for assessing your agent performance, beyond just consumption and performance metrics or errors. This article explains what each one measures and how to act on a low score.

## Answer relevance

**What it measures:** whether the agent's response actually addresses what the user asked.

**Inputs:** the agent prompt and agent response for each CallAgent node.

**When to use it:** applicable to all conversational agents.

**What a low score means:** the agent is drifting toward generic or off-topic responses. To investigate:

* Review the system prompt and the agent's goal definition
* Check whether a recent prompt or model change correlates with the drop
* Look at which specific input patterns are driving low scores

## Safety

**What it measures:** whether harmful, toxic, biased, or otherwise unsafe content is appearing on either side of the agent.

* **Unsafe input:** jailbreak attempts, harmful user requests, or prompt-injection patterns reaching the agent
* **Unsafe output:** harmful content in the agent's response

**Inputs:** the agent prompt and agent response for each CallAgent node.

**When to use it:** recommended for all production agents, and especially important if you rely on custom Guardrails. the Safety score doesn't replace Guardrails, but it tells you whether your Guardrails policy is actually catching what it should in real traffic.

**What a low score means:** content is crossing safety thresholds. To investigate:

* Determine whether the failure is on the input side (a harmful or adversarial prompt reaching the agent) or the output side (the agent producing unsafe content)
* Check whether your configured Guardrails should have caught the offending pattern
* If you own the Guardrails policy, consider whether categories or thresholds need to be extended or tuned based on what you're seeing in real traffic

## How scoring works

* Both judges run automatically, there's no option to select or configure them.
* Every trace produced is scored, 100% coverage, no sampling.
* Scoring evaluates recorded trace data only. It doesn't execute your Service Action or make any new agent calls.
