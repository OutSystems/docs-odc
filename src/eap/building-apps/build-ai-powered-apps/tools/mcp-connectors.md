---
guid: 7a08a9ca-8a6e-4f48-9079-8f840ce01a7b
summary: Integrate MCP servers with AI agents in OutSystems Developer Cloud (ODC) to extend agent capabilities with external tools and enterprise services.
locale: en-us
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=8018-13&p=f&t=7IONekw0zMyvK9bL-0
tags: mcp servers,ai agents,external tools,enterprise integration
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

# Use MCP servers

Use Model Context Protocol (MCP) servers to extend AI agents in OutSystems Developer Cloud (ODC) with external systems. Tools exposed by an MCP server become server actions that agents can call. ODC Portal accelerates setup by discovering connection details from the server URL.

MCP standardizes how agents call external capabilities. LLMs can't reach real-time or protected enterprise data on their own; bespoke integrations create inconsistency and maintenance overhead. MCP defines a common contract (purpose, inputs, outputs) so an agent can call any compliant tool without custom glue.

With this shared protocol you add capabilities once and reuse them across apps and agents. Imported MCP tools (server actions) can support scenarios like credit scoring, document verification, or compliance validation.

Key benefits:

* **Enterprise integration**: Connect agents to business systems and services.
* **Standardized protocol**: Use consistent authentication and communication patterns.
* **Real-time operations**: Access current data and perform live operations.
* **Secure access**: Maintain controlled, authenticated access to external resources.

## Terminology

In the MCP domain, a capability is a "tool". When you import an MCP tool through a connection in ODC Portal, it appears in ODC Studio as a server action. In an agent configuration you select those server actions as tools. In this document:

* MCP tool or tool: the capability exposed by the MCP server.
* Server action: the OutSystems artifact created from an imported MCP tool.

## Transport types

MCP servers communicate using one of two transport protocols. The transport type determines how ODC Portal exchanges messages with the server—either through discrete HTTP calls or a persistent event stream.

| Transport type | URL suffix | Description |
| --- | --- | --- |
| Streamable HTTP | `/mcp` | Standard HTTP request/response. Each tool call is a separate request. |
| SSE (Server-Sent Events) | `/sse` | Persistent connection that streams responses in real time. |

Select the transport type that matches your server's endpoint suffix.

## Authentication methods

MCP servers may require authentication to protect access to tools and data. ODC supports several authentication methods depending on how the server validates requests.

* **User login (OAuth)**: Delegates authentication to an identity provider. The user completes an OAuth flow, and ODC Portal uses the resulting token. When you enter the server URL, ODC Portal attempts to discover remaining fields automatically. If discovery fails, manually provide the token URL, client ID, client secret, authorization URL, refresh token URL, resource URI, and scopes.

* **System to system (OAuth)**: Uses client credentials to authenticate without user interaction. Provide the server token URL, client ID, client secret, and scopes.

* **API key**: Sends a static key with each request. Provide the key value and select the key location (authorization header or custom header).

* **No auth**: The server allows unauthenticated access. No additional configuration required.

## Use MCP capabilities

Custom MCP servers let you connect to any system that supports the protocol. At a high level: create a connection in ODC Portal, import selected tools, then reference them in ODC Studio and agent configurations.

### Create a connection

In ODC Portal you can create a connection to an MCP server.

### Configure a connection

In ODC Portal, go to **Integrate** > **Connections** > **Create connection** > **MCP server**.

Select a [transport type](#transport-types) based on your server endpoint, then choose an [authentication method](#authentication-methods) and provide the required credentials. Select **Test connection** to verify authentication and confirm the MCP server returns available tools.

<div class="info" markdown="1">

If your MCP server is on a private network:

* Enable the **Private Gateway** toggle.
* Enter the port configured in your Cloud Connector.
* For **System to system** authentication, also enter the port for the server token URL. Use the same port in both fields if both services share a port.

</div>

### Import tools

Select **Import** in the connection list to bring tools (server actions) into ODC. Select only the tools you need. Optionally rename them. They then appear in ODC Studio as server actions.

![ODC Portal interface showing the selection of actions from an MCP example connection.](images/mcp-import-actions-pl.png "Importing MCP tools in Portal")

### Add dependencies

In ODC Studio, open the agentic app and add the MCP tools (server actions) as dependencies. They keep the names assigned during import.

You can add MCP tools as dependencies in any ODC app.

### Use tools in an agent

In the **Call Agent** element, add tools (server actions), configure parameters, map values, and handle errors.

## Sample use cases

Examples of how MCP servers connect AI agents to external systems:

| Area | Use Cases |
| --- | --- |
| **Financial services** | Connect to credit bureaus for real-time score retrieval, access compliance databases for anti-money laundering (AML) checks, and integrate with employment verification services. |
| **Customer onboarding** | Integrate with government databases for identity confirmation (KYC), connect to screening services for fraud prevention, access risk scoring platforms, and automate account creation through core system APIs. |
| **Supply chain** | Validate suppliers by connecting to business registry databases, monitor compliance with regulatory databases, track inventory with third-party logistics systems, and verify product quality with certification databases. |
| **HR automation** | Integrate with screening services for background checks, connect to professional certification databases to assess skills, and access regulatory databases to verify employment eligibility. |

## Related resources

For more information about AI agents and ODC capabilities:

* [Create an AI agent in ODC Studio](../create-agent.md)
* [Agentic apps in ODC](../agentic-apps.md)
* [Consumer app](../consumer-app.md)

For external resources:

* [Model Context Protocol specification](https://modelcontextprotocol.io/)
