---
summary: Send feedback about OutSystems MCP, including the server, the tools, the skills, and delegation to Mentor, through the feedback tool of the OutSystems MCP server.
tags:
  - Agentic
  - Mentor
  - Security
guid: 67bafccc-6450-4ded-95a8-aa73ea13a700
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - claude code
coverage-type:
  - apply
content-type:
  - reference
audience:
  - Developer
topic:
  - creating-apps
isautopublish: true
---

# Give feedback on OutSystems MCP

This page describes how to send feedback about OutSystems MCP from your MCP host. The OutSystems team collects product feedback through the feedback tool of the OutSystems MCP server. Every way of sending OutSystems MCP feedback goes through this tool.

## Feedback scope for OutSystems MCP

The feedback tool of the OutSystems MCP server accepts feedback about any part of OutSystems MCP. The following parts are examples:

* The OutSystems MCP server and its authentication.
* The tools that the agent calls. For the tools, refer to [Tool reference](tool-reference.md).
* The OutSystems skills that your MCP host loads. For the skills, refer to [OutSystems skills](skills.md).
* Delegation of app changes to Mentor. For more information, refer to [Delegation to Mentor](mentor-delegation.md).

## Send OutSystems MCP feedback from your MCP host

To send feedback through the feedback tool of the OutSystems MCP server, use one of the following ways:

* In Claude Code, type `/outsystems-feedback` for a guided form, or `/outsystems-feedback MESSAGE` to submit directly. Replace `MESSAGE` with your feedback. The command sends your feedback through the feedback tool.
* In any MCP host, ask the agent in plain language, for example "send a thumbs-up about the OutSystems agent".

To help the OutSystems team act on your feedback, describe the action you took, the result you expected, and the result you got.

<div class="warning" markdown="1">

Don't include secrets, personally identifiable information (PII), code, or other sensitive data in your feedback. Use placeholder or fictional data instead of real names, email addresses, phone numbers, or other sensitive data. Redaction of your feedback depends on the AI model in your MCP host, so redaction isn't guaranteed. For more information, refer to [Redaction of secrets and personal data from feedback](#redaction-of-secrets-and-personal-data-from-feedback).

</div>

## Send feedback about an OutSystems skill

To send feedback about an OutSystems skill, including a skill that is a Beta Feature, name the skill in your message. The name identifies which skill the feedback concerns. For example, ask the agent to "send feedback about the `outsystems-custom-code` skill". For the skills that are Beta Features, refer to [Beta skills](skills.md#beta-skills).

## Redaction of secrets and personal data from feedback

The OutSystems skill instructs the agent to replace the following in your feedback with `[redacted]` before the agent submits it:

* Tokens, API keys, passwords, and client secrets.
* Personal data, such as email addresses, names, and phone numbers.
* Code snippets and OML.
* Full transcripts of multi-turn dialogue.

The agent then reports what it replaced.

The AI model in your MCP host applies these instructions. Redaction depends on the model identifying the data, so the agent can miss data in your message. Review your message before you send it.

## Agent-reported observations and bug reports

The agent can report its own observations about the OutSystems tools, such as a lookup that returned no results when the agent expected data. The agent asks for your agreement once in each conversation before the agent sends any observation. Each observation contains a fixed category and one sentence that the agent writes, without your messages, code, or app content.

When a tool call fails unexpectedly, the agent can also offer, once in each session, to send a bug report with the failed call and its error code.

## Next steps

The following pages cover the parts of OutSystems MCP that you can send feedback about.

* To see the OutSystems skills that your MCP host loads, refer to [OutSystems skills](skills.md).
* To see the tools that the agent calls, refer to [Tool reference](tool-reference.md).
* To connect an MCP host and run a first request, refer to [Get started with OutSystems MCP](get-started.md).
