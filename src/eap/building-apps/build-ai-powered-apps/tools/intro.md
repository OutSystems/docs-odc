---
guid: 7a5bb4dd-9d82-48ef-9162-8f8a34d2d697
summary: Overview of MCP tools and prebuilt connectors.
locale: en-us
figma:
tags: integration, full stack development, tech leads, backend integration, cloud development
app_type: mobile apps,reactive web apps
platform-version: odc
coverage-type:
  - understand
  - apply
topic:
  - integration
audience:
  - full stack developers
  - tech leads
  - backend developers
outsystems-tools:
  - odc portal
  - odc studio
---

# Tools and connectors

External tools extend OutSystems Developer Cloud (ODC) apps and AI agents with remote capabilities such as search, validation, or enrichment. A tool is a callable capability surfaced in ODC Studio as a server action. ODC supports two sources:

* **Custom MCP servers**: Open protocol endpoints. The platform can discover capabilities, prefill connection details, and let you import selected tools (server actions).
* **Prebuilt connectors**: Curated integrations for popular APIs (for example, SerpAPI) with a guided flow (create connection, authenticate, import tools).

<div class="info" markdown="1">

Agentic app creation is available through the Early Access Program. [Apply for the Early Access Program](https://www.outsystems.com/low-code-platform/agentic-ai-workbench/eap-agent-workbench/).

</div>

Both paths produce server actions you can call in app logic or expose to agents (for example, in the `Call Agent` element). Choose a custom MCP server when you need open, portable definitions or plan to reuse across environments. Choose a prebuilt connector for faster setup and reduced protocol overhead.

Decision summary:

* Use a custom MCP server when you need extensibility, portability, or custom enterprise capabilities.
* Use a prebuilt connector when you need a supported integration quickly with minimal configuration.

## Next steps

* [Custom MCP servers](mcp-connectors.md)
* [Prebuilt connectors](prebuilt-connectors.md)
* [Unsupported structures](unsupported-structures.md)
* [Build AI-powered apps overview](../intro.md)
