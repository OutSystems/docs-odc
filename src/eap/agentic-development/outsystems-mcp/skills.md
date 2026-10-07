---
summary: The OutSystems skills that your MCP host loads for the agent, which skills are Beta Features, and how to send feedback on them.
tags: outsystems mcp, skills, beta, mcp host, agentic development
guid: f9a69471-9433-464a-9d88-111b28d26071
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - claude code
coverage-type:
  - remember
content-type:
  - reference
audience:
  - Developer
topic:
  - creating-apps
isautopublish: true
---

# OutSystems skills

This page lists the OutSystems skills that your MCP host loads for the agent, and identifies the skills that are Beta Features. An OutSystems skill is a set of instructions that tells the agent how to use the OutSystems tools for a task. OutSystems packages each skill in the Agent Skills format, as a `SKILL.md` file. For related terms, refer to [Agentic development terminology](../agentic-development-terminology.md). For the tools that the skills call, refer to [Tool reference](tool-reference.md).

## Core skill

The core skill, `outsystems`, covers the OutSystems MCP workflows: searching your tenant, editing apps through Mentor, publishing, deploying, and managing external libraries. It also tells the agent when to confirm an operation before it runs. Depending on your MCP host, the OutSystems plugin, the OutSystems Power, or a skill file you save in your workspace delivers the core skill. To install and update it, refer to [Connect MCP hosts to OutSystems MCP](connect-mcp-hosts.md).

## Beta skills

Some OutSystems skills are Beta Features. OutSystems provides Beta Features to collect customer feedback on non-final capabilities. A Beta Feature can change significantly, including through breaking changes, or OutSystems can discontinue it. For the terms that apply, refer to the [OutSystems Beta Features Agreement](https://www.outsystems.com/legal/beta-features-agreement).

The following OutSystems skills are Beta Features:

* `outsystems-app-architecture`
* `outsystems-custom-code`
* `outsystems-dependency-impact`
* `outsystems-design-to-app`
* `outsystems-spec-driven-build`
* `outsystems-tenant-architecture`

## Give feedback on Beta skills

You send feedback on a Beta skill through the OutSystems MCP feedback tool, the channel the OutSystems team uses for OutSystems MCP feedback. Use one of the following ways from your MCP host:

* In Claude Code, type `/outsystems-feedback` for a guided form, or `/outsystems-feedback MESSAGE` to submit directly. Replace `MESSAGE` with your feedback.
* In any MCP host, ask the agent in plain language, for example "send feedback about the OutSystems skill you just used".

Name the skill in your message, so the report identifies which skill it concerns. For more information about how the agent prepares your feedback before it submits it, refer to [Give feedback](connect-mcp-hosts.md#give-feedback).
