---
guid: 4af631fd-a285-4f52-84eb-3b3e2a6d5f00
summary: Integrate popular external services using prebuilt connectors in OutSystems Developer Cloud (ODC) with guided setup, validation, and simplified authentication.
locale: en-us
figma:
tags: integration, api connectors, prebuilt connectors, authentication, outsystems developer cloud
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

# Prebuilt connectors

Prebuilt connectors integrate external services without requiring you to host a custom MCP server. Each connector provides guided setup, authentication, and validation. After you create a connection and import selected tools (server actions), they are available in any app or agent.

<div class="info" markdown="1">

Agentic app creation is available through the Early Access Program. [Apply for the Early Access Program](https://www.outsystems.com/low-code-platform/agentic-ai-workbench/eap-agent-workbench/).

</div>

## Available connectors

The list below shows currently supported prebuilt connectors. Additional connectors may be added.

| Service | Description | Notes |
| --- | --- | --- |
| **SerpAPI** | Access structured search engine results (web, news, shopping) for retrieval, enrichment, or grounding. | Requires a SerpAPI account and API key. |

## Create a connection

In ODC Portal, go to **Integrate > Connections** and create a connection. Select a connector (for example, SerpAPI). Provide required authentication (API key). Test and save the connection.

### Import tools

Select **Import** and choose only the tools (server actions) you need. Optionally rename them. Imported tools appear in ODC Studio as server actions.

## Use tools in apps and agents

Add the imported tools as dependencies in ODC Studio. Invoke them in server logic or in an agent’s **Call Agent Core** element. Map required inputs (such as query text) and implement error handling—for example, invalid or expired key, empty results, or rate limit exceeded.

## Related topics

* [External tools overview](intro.md)
* [Custom MCP servers](../tools/mcp-connectors.md)
* [Unsupported structures](unsupported-structures.md)