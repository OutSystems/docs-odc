---
summary: Definitions of the terms used across agentic development in ODC, including Mentor, OutSystems MCP, MCP host, agent, and the OutSystems skill.
tags:
  - OutSystems MCP
  - Agentic
  - Mentor
  - Mentor Studio
  - Mentor Web
  - MCP
  - Terminology
guid: 98283a24-a179-44a1-a706-435a15f8b838
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
  - remember
  - understand
content-type:
  - reference
audience:
  - Developer
  - Architect
  - Tech lead
topic:
  - creating-apps
isautopublish: true
---

# Agentic development terminology

This page defines the terms that the agentic development pages use across Mentor Studio, Mentor Web, and OutSystems MCP. Each definition states what the term names and links to the page that explains it in depth. Use this page to look up a term. It also explains terms whose meaning depends on the context, such as agent, which names both the agent in an MCP host and the AI agents you build into apps.

## Development paths

The following terms name agentic development and the three paths you use it through.

| Term | Definition |
| ---- | ---------- |
| Agentic development | The OutSystems Developer Cloud (ODC) capability that builds and changes apps from natural-language requests. You use it through Mentor Studio, Mentor Web, or OutSystems MCP. Every path produces the same OutSystems Model. Refer to [Agentic development](intro.md). |
| Agentic Systems Engineering | The OutSystems approach to building governed, enterprise-ready agentic systems. Agentic development is its app development capability. Refer to [Agentic development](intro.md#platform-foundation). |
| Mentor | The OutSystems AI that builds and modifies OutSystems assets through conversation. Mentor Studio, Mentor Web, and OutSystems MCP all send app changes to Mentor. Refer to [Mentor](coding-agents.md). |
| Mentor Studio | Mentor inside ODC Studio. You use Mentor Studio to change the asset you have open, such as a web app, a library, or an agentic app. Refer to [AI development in Mentor Studio](mentor-studio/how-it-works.md). |
| Mentor Web | Mentor inside ODC Portal. You use Mentor Web to create a new app from a prompt or a requirements document. Refer to [AI app generation in Mentor Web](mentor-web/how-it-works.md). |
| OutSystems MCP | The OutSystems capability that lets the agent in an MCP host, such as Claude Code or Cursor, build and manage OutSystems apps. OutSystems MCP has two parts: the OutSystems MCP server, which OutSystems hosts for your tenant, and the OutSystems skill, which your MCP host loads. The agent sends app changes to Mentor and runs publish and deploy operations. Refer to [OutSystems MCP](outsystems-mcp/outsystems-mcp-overview.md). |

## Mentor and the app model

The following terms name what Mentor reads, what it proposes, and where its work happens.

| Term | Definition |
| ---- | ---------- |
| Blueprint | The structure that Mentor Web proposes for a new app, including entities, screens, and roles, before it generates the app. You review and refine the blueprint, then Mentor Web builds from it. Refer to [Blueprint](mentor-web/blueprint.md). |
| Enterprise Context Graph | A structured, queryable index of your tenant's application estate, such as apps, entities, actions, screens, and their dependencies. Mentor reads the Enterprise Context Graph when it builds and changes apps, and the agent in an MCP host queries it through context lookups. Refer to [Enterprise Context Graph](context-graph.md). |
| Mentor session | When you work from an MCP host, the server-side session that holds one loaded app and runs one Mentor turn at a time. The agent in your MCP host starts a Mentor session, sends prompts to it, and publishes the changes from it. Refer to [Delegation to Mentor](outsystems-mcp/mentor-delegation.md). |
| OutSystems Model | The high-level representation of an asset's structure and behavior, also called the app model. Mentor, ODC Studio, and ODC Portal all work on the same OutSystems Model, and the OutSystems compiler turns it into deployable code when you publish. Refer to [Mentor](coding-agents.md#the-model-mentor-works-on). |
| Plan | The set of changes that Mentor Studio proposes for a complex request, before it applies them. You proceed with the plan, review the changes first, or discard it. Refer to [Review and accept the plan](mentor-studio/how-it-works.md#accept-plan). |

## MCP and OutSystems MCP

The following terms follow the Model Context Protocol (MCP) specification, which defines how AI applications connect to external tools. OutSystems MCP uses these terms for the parts that connect your AI application to OutSystems.

| Term | Definition |
| ---- | ---------- |
| Agent | When you work from an MCP host, the AI model that the MCP host runs and that directs its own tool use. The agent interprets your requests, calls OutSystems tools, and reports the results to you. Refer to [OutSystems MCP](outsystems-mcp/outsystems-mcp-overview.md). |
| MCP client | The component inside the MCP host that maintains a dedicated connection to one MCP server. The MCP host creates one MCP client for each MCP server it connects to. Refer to [OutSystems MCP request architecture](outsystems-mcp/architecture.md). |
| MCP host | The AI application you work in, such as Claude Code, Cursor, AWS Kiro, VS Code with GitHub Copilot, or Claude Desktop. The MCP host runs the agent, manages your session, applies its own permission and consent settings, and creates the MCP clients that connect to MCP servers. For the term harness, refer to [Context-dependent terms](#context-dependent-terms). Refer to [Connect MCP hosts to OutSystems MCP](outsystems-mcp/connect-mcp-hosts.md). |
| Model Context Protocol (MCP) | An open protocol that connects AI applications to external tools and data. MCP defines three roles: the MCP host, the MCP client, and the MCP server. Refer to the [MCP architecture overview](https://modelcontextprotocol.io/docs/learn/architecture). |
| OutSystems MCP server | The remote MCP server at your tenant's `/mcp` endpoint, reached over the Streamable HTTP transport. The OutSystems MCP server is the server part of OutSystems MCP. It exposes the OutSystems tools to the MCP client and runs each tool call against your tenant. Refer to [OutSystems MCP request architecture](outsystems-mcp/architecture.md). |
| OutSystems plugin | The package that delivers the OutSystems skill to Claude Code, Claude Desktop, and the Cursor app. In Claude Code, the OutSystems plugin also registers the OutSystems MCP server for your tenant. Refer to [Connect MCP hosts to OutSystems MCP](outsystems-mcp/connect-mcp-hosts.md). |
| OutSystems Power | The package that delivers the OutSystems skill to AWS Kiro. You install a Power from the Kiro Powers panel. Refer to [Connect MCP hosts to OutSystems MCP](outsystems-mcp/connect-mcp-hosts.md). |
| OutSystems skill | The instructions that tell the agent how to use the OutSystems tools, such as when to confirm an operation and how to sequence a Mentor session. OutSystems packages the skill in the Agent Skills format, as a `SKILL.md` file. Refer to [Connect MCP hosts to OutSystems MCP](outsystems-mcp/connect-mcp-hosts.md). |
| Tool | A function that an MCP server exposes for the agent to call, such as a context lookup, a Mentor prompt, or a deploy. The OutSystems MCP server groups its tools into Context Services, Mentor Services, and Platform Services. Refer to [Tool reference](outsystems-mcp/tool-reference.md). |
| Tool description | The text that an MCP server publishes with each tool to tell the agent what the tool does and how to use it. OutSystems tool descriptions instruct the agent to restate publish, deploy, and rollback operations and wait for your confirmation. Refer to [Governance in OutSystems MCP](outsystems-mcp/governance.md). |

## AI in the apps you build

The following terms name AI that runs inside your apps. This AI serves your app's users, while agentic development helps you build the app.

| Term | Definition |
| ---- | ---------- |
| Agent Workbench | The ODC capability for building and managing AI agents. Mentor Studio edits AI agents in Agent Workbench. Refer to [Capabilities and patterns for Mentor Studio](mentor-studio/capabilities.md#element-coverage). |
| Agentic app | An app that uses one or more AI agents to perform tasks, automate workflows, or handle multi-step interactions. Refer to [Agentic apps in ODC](../building-apps/build-ai-powered-apps/agentic-apps.md). |
| AI agent | An orchestrator inside an app that combines AI models, application logic, data sources, and external tools to reach a larger goal. AI agents in ODC run without a user interface. Refer to [Agentic apps in ODC](../building-apps/build-ai-powered-apps/agentic-apps.md#use-ai-agents). |
| AI model | A pre-trained algorithm or deployed machine learning service, such as a large language model, that provides a specific capability, such as summarization, extraction, or generation. An app calls an AI model through its `Call<AIModelName>` server action. Refer to [Agentic apps in ODC](../building-apps/build-ai-powered-apps/agentic-apps.md#ai-models). |
| AI-powered app | An app that applies AI while it runs, to serve its users, such as an app that calls an AI model or an AI agent. Refer to [Build AI-powered apps](../building-apps/build-ai-powered-apps/intro.md). |

## Context-dependent terms

Some terms mean different things depending on the context they appear in, such as working from an MCP host, the apps you build, or the wider AI industry. Each of the following entries names the contexts and the term these pages use in each one.

| Term | Definition |
| ---- | ---------- |
| Agent | When you work from an MCP host, the agent is the AI model in your MCP host that calls OutSystems tools. In the apps you build, an AI agent is an orchestrator that runs inside the app. On the Mentor page, Mentor's agents are the internal parts of Mentor that plan and build changes. Refer to the entries for Agent, AI agent, and Mentor on this page. |
| Environment | In O11, an environment is where you develop, test, or run apps, such as Development or Production. ODC uses a tenant instead, and your tenant has stages, such as Development and Production, that you deploy assets to. The OutSystems MCP server and the OutSystems skill use environment for a stage, for example in the **Environments** tools and the `env_key` parameter. These pages use tenant and stage for ODC. Refer to [Deploying assets](../deploying-apps/deploy-apps.md). |
| Harness | In AI engineering, an agent harness is the software around an AI model that runs its tool loop and manages its memory and context. MCP hosts such as Claude Code include their own agent harness. In some OutSystems tool descriptions and setup guides, harness means the MCP host. These pages use MCP host for the application you work in. Refer to the entry for MCP host on this page. |
| MCP | Model Context Protocol (MCP) is the open protocol that connects AI applications to external tools. OutSystems MCP is the OutSystems capability that connects the agent in your MCP host to your tenant. In the apps you build, an AI agent calls external MCP servers to use their tools. Refer to the entries for Model Context Protocol (MCP) and OutSystems MCP on this page, and to [Use MCP servers](../building-apps/build-ai-powered-apps/tools/mcp-connectors.md). |
| Model | In ODC, the OutSystems Model is the representation of an asset that Mentor and ODC Studio change. In AI, a model is a pre-trained model, such as a large language model, that an app, an AI agent, or the agent in an MCP host runs on. Refer to the entries for OutSystems Model and AI model on this page. |
