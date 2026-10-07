---
summary: Agentic development in OutSystems Developer Cloud (ODC) uses AI to create and modify apps through Mentor Studio, OutSystems MCP, and Mentor Web.
tags:
  - OutSystems MCP
  - Agentic
  - Agentic Systems Engineering
  - AI
  - Development lifecycle
  - Mentor
  - Mentor Studio
  - Mentor Web
  - Security
guid: 7681329f-0fe1-47ea-9d99-911eddfac02b
locale: en-us
app_type: reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=9254-46
outsystems-tools:
  - portal
  - odc studio
  - mentor web
  - mentor studio
  - claude code
coverage-type:
  - understand
  - evaluate
audience:
  - Developer
  - Architect
  - Tech lead
topic:
  - creating-apps
isautopublish: true
---

# Agentic development

With agentic development, you describe an app in natural language, and OutSystems builds and updates it for you. You work through one of three paths: Mentor Studio in ODC Studio, your own MCP host through OutSystems MCP, or Mentor Web in OutSystems Developer Cloud (ODC) Portal. Every path produces the same OutSystems app model, and the platform compiles and governs it the same way.

<div class="info" markdown="1">

For a video walkthrough of agentic development concepts and tools, take the [Agentic development](https://www.outsystems.com/tk/redirect?g=eb9a16f2-f6b9-4903-9be8-122a0188f113) online course.

</div>

## Development paths

Choose the path that matches where you work and what you want to accomplish. If you already build with AI and are new to OutSystems, start with OutSystems MCP. The following table compares the three paths.

| Path | What you do | Where you work | Choose it when | Start here |
| ---- | ----------- | -------------- | -------------- | ---------- |
| [Mentor Studio](mentor-studio/how-it-works.md) | Modify existing apps | ODC Studio | You build in ODC Studio and want AI to change the app you have open. | [Modify an app with AI](mentor-studio/modify-app.md) |
| [OutSystems MCP](outsystems-mcp/outsystems-mcp-overview.md) | Build, evolve, and deploy apps | Your MCP host, such as Claude Code or Cursor | You work in an AI tool, or you combine OutSystems with other tools, such as Jira or Figma, in one workflow. | [Get started with OutSystems MCP](outsystems-mcp/get-started.md) |
| [Mentor Web](mentor-web/how-it-works.md) | Create new apps from requirements | ODC Portal | You start a new app from a prompt or a requirements document. | [Create an app with AI](mentor-web/create-app.md) |

## Platform foundation

Agentic development is the app development capability within OutSystems Agentic Systems Engineering, the approach to building governed, enterprise-ready agentic systems. Every path builds on the same platform, so the same guarantees hold whichever one you use. The compiler applies the same security, performance, and architecture standards to the app model, whether AI or a developer built it. The same governance policies and roles apply to every path.

For what the platform guarantees and what you review, refer to [Platform guarantees and AI interpretation](odc-ai-and-platform.md). For the components behind agentic development, refer to [Architecture](architecture.md). For data safeguards and compliance, refer to [Security and safeguards](security-safeguards.md). For lifecycle fit and access control, refer to [Agentic development in the SDLC](sdlc.md).

## Working effectively with AI

Clear, specific requests produce more accurate results. The AI interprets your instructions and applies patterns it supports, so it builds from what you state explicitly. To learn how Mentor works, refer to [Mentor](coding-agents.md). For the mindset and prompting technique, refer to [Thinking with AI](thinking-with-ai.md) and [Effective prompts for Mentor](effective-prompts.md).

## Agentic development and AI-powered apps

Agentic development and AI-powered apps use AI for different purposes. Agentic development applies AI while you build the app. An AI-powered app applies AI while it runs, to serve its users. This section covers agentic development. To build apps that call AI models at runtime, refer to [Build AI-powered apps](../building-apps/build-ai-powered-apps/intro.md).

## Limitations and scope

Agentic development uses generative AI, so its output varies and each path has boundaries. Generative AI produces non-deterministic output, so you review each result before you rely on it. For current constraints, refer to [Known limitations](ai-limitations.md). For what OutSystems MCP covers and where its scope stops, refer to [OutSystems MCP](outsystems-mcp/outsystems-mcp-overview.md).

## Terminology

The agentic development pages use a shared set of terms across the three paths, such as Mentor, OutSystems Model, MCP host, and agent. For their definitions, refer to [Agentic development terminology](agentic-development-terminology.md).
