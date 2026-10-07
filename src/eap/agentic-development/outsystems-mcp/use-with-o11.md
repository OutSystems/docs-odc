---
summary: Keep OutSystems MCP requests on ODC when your MCP host also connects to O11. Recognize the ODC server, name the platform, and enter the right tenant hostname.
tags: outsystems mcp, o11, mcp host, agentic development, tenant hostname
guid: 01d0c5b1-af47-4fa7-bcd3-dc8a833fc63b
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - claude code
coverage-type:
  - understand
  - apply
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

# Use OutSystems MCP in ODC alongside O11

Your MCP host can connect to the OutSystems MCP server for OutSystems Developer Cloud (ODC) and to the Service Studio MCP server for OutSystems 11 (O11). With both connections, the agent has tools for both platforms. This page covers the ODC side: how to recognize the OutSystems MCP server, how to word requests so that they reach it, and which tenant hostname to enter.

For the O11 side, refer to [OutSystems MCP](https://www.outsystems.com/tk/redirect?g=716a959b-9b36-4098-9e85-182bba489d8c) in the O11 documentation.

## Prerequisites

Before you work with both platforms from one MCP host, make sure the following are in place:

* The OutSystems MCP server is connected in your MCP host, and the OutSystems skill is installed. Refer to [Get started with OutSystems MCP](get-started.md).
* The Service Studio MCP server for O11 is connected in the same MCP host. Refer to [Get started with OutSystems MCP](https://www.outsystems.com/tk/redirect?g=9fefed39-c894-483b-b625-0c88caf81f51) in the O11 documentation.

## The OutSystems MCP server for ODC

The following facts identify the ODC side, so that you recognize which tools and prompts belong to it:

* **Name in your MCP host:** The server appears as `outsystems`. In Claude Code, the plugin registers it as `plugin:outsystems:outsystems`.
* **Where it runs:** OutSystems hosts the server for your tenant, at `https://TENANT_HOSTNAME/mcp`. You don't start it.
* **What it works on:** The apps in your ODC tenant.
* **How a change reaches the app:** The agent delegates the edit to Mentor, and then runs the publish and deploy steps. Refer to [Delegation to Mentor](mentor-delegation.md).
* **Sign-in and confirmation:** You sign in through your browser, and your ODC roles apply to every request. Before a publish, deploy, or rollback, the agent is instructed to restate the operation and wait for your confirmation. Refer to [Governance in OutSystems MCP](governance.md).

## Name the platform in your requests

A request such as "Add a DueDate attribute to the Task entity" doesn't state which platform it targets. State that the request is for ODC, and name the app. For example:

* "In ODC, add a DueDate attribute to the Task entity of the Expenses app."
* "Which environments do I have in my ODC tenant?"

For a first request that confirms the connection, refer to [Verify the connection](get-started.md#verify-the-connection).

## Enter your ODC tenant hostname

OutSystems MCP in ODC needs the hostname of your ODC tenant, for example `mycompany.outsystems.dev`. If you also work in O11, the OutSystems URL you use every day can belong to an O11 environment. An O11 environment hostname isn't an ODC tenant, and the connection fails with it.

Use the host of your ODC Portal URL as the tenant hostname. Use the bare hostname, without `https://` or a path.

## Approval and sign-in prompts

With both servers connected, you see two kinds of prompts. A sign-in in your browser belongs to OutSystems MCP in ODC. The approval prompt in Service Studio belongs to OutSystems MCP in O11. For more information, refer to [OutSystems MCP](https://www.outsystems.com/tk/redirect?g=716a959b-9b36-4098-9e85-182bba489d8c) in the O11 documentation.

## Instruction files

Some setup paths save the OutSystems skill to a shared instruction file that the OutSystems skill for O11 also uses. The following setup paths use a shared instruction file:

* **Cursor CLI:** `AGENTS.md` in your workspace root.
* **GitHub Copilot in VS Code:** `.github/copilot-instructions.md` in your workspace.

Before you save the OutSystems skill for ODC, check whether the file already exists. If the file exists, keep its content and add the OutSystems skill for ODC to the end of the file. For the steps for your MCP host, refer to [Connect MCP hosts to OutSystems MCP](connect-mcp-hosts.md).

## Give feedback

The feedback tool of the OutSystems MCP server sends feedback about OutSystems MCP in ODC. For the ways to send feedback from your MCP host, refer to [Give feedback](connect-mcp-hosts.md#give-feedback).

## Next steps

Continue with the page that fits your task:

* To connect your MCP host and run a first request, refer to [Get started with OutSystems MCP](get-started.md).
* To understand how the agent and Mentor divide the work, refer to [Delegation to Mentor](mentor-delegation.md).
* For the terms that differ between the platforms, refer to [Agentic development terminology](../agentic-development-terminology.md).
