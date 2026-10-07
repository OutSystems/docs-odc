---
summary: Connect your MCP host to the OutSystems MCP server, with setup for Claude Code, AWS Kiro, Cursor, GitHub Copilot, and Claude Desktop.
tags: install, setup, mcp, mcp host, claude code, kiro, cursor, copilot
guid: c4722355-e921-4c57-a127-dcd7991a6615
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - claude code
coverage-type:
  - apply
content-type:
  - procedure
audience:
  - Developer
topic:
  - creating-apps
isautopublish: true
---

# Connect MCP hosts to OutSystems MCP

This page shows you how to connect your MCP host, the AI application you work in, to the OutSystems MCP server. It covers Claude Code, Cursor, AWS Kiro, GitHub Copilot, and Claude Desktop, and the settings any other MCP host needs. Each MCP host also loads the OutSystems skill, the instructions that tell the agent how to use the OutSystems tools. The install steps differ per MCP host, and each MCP host has its own section on this page. After you connect, refer to [Get started with OutSystems MCP](get-started.md) to authenticate and run a first request. For the terms this page uses, such as MCP host, OutSystems skill, OutSystems plugin, and OutSystems Power, refer to [Agentic development terminology](../agentic-development-terminology.md).

## Prerequisites

You need the following for any MCP host:

* An OutSystems tenant with OutSystems MCP enabled for your organization. Access is gated server-side, so confirm this with your administrator before you install. If a call later returns a `tenant_not_allowed` rejection, refer to [Verify the connection](get-started.md#verify-the-connection) for the cause and the resolution.
* Your OutSystems tenant hostname. Replace `TENANT_HOSTNAME` with the host part of your OutSystems URL, for example `mycompany.outsystems.dev`.
* A web browser on the same machine as your MCP host. The sign-in redirect goes to a local loopback address, so run the MCP host and the browser on one machine.

The OutSystems MCP server supports OAuth Dynamic Client Registration, so your MCP host registers its own OAuth client and gets a client ID and callback port automatically. Setting a fixed client ID or callback port makes two sessions contend for the same port, so only the first session signs in.

For the MCP hosts OutSystems validates, refer to [Supported MCP hosts](outsystems-mcp-overview.md#supported-mcp-hosts).

## Connect Claude Code

Claude Code is a validated MCP host. You connect it with the OutSystems plugin, which registers the OutSystems MCP server and delivers the OutSystems skill. To install the plugin, sign in, and run a first request in one path, follow [Get started with OutSystems MCP](get-started.md).

## Connect AWS Kiro

AWS Kiro is a validated MCP host. Install the OutSystems Power, set your tenant URL, and sign in on the first request. A Power is a package you install in Kiro from the Powers panel. The OutSystems Power delivers the OutSystems skill.

1. Open the Powers panel, select **Add Custom Power**, then **Import power from GitHub**. Paste the following URL and select **Install**:

        https://github.com/OutSystems/outsystems-mcp/tree/main/kiro/outsystems

1. Set your tenant URL in `~/.kiro/settings/mcp.json`. Read the file first, keep every other entry, then add this under the top-level `mcpServers` object:

        {
          "mcpServers": {
            "outsystems": {
              "type": "http",
              "url": "https://TENANT_HOSTNAME/mcp"
            }
          }
        }

    Put the URL under the top-level `mcpServers`, not under `powers.mcpServers`. Kiro rewrites the `powers` block on every Power update, which drops a URL stored there.

1. Ask Kiro Chat for an OutSystems request. Kiro opens the browser for OAuth on the first tool call, and you complete the sign-in there. Kiro runs the flow itself, so there's no authenticate tool to call.

## Connect Cursor

Cursor is a validated MCP host. The Cursor CLI path works on every plan, including individual accounts. Cursor loads the OutSystems skill from `AGENTS.md` in your workspace root.

1. Add the server to the global config `~/.cursor/mcp.json`, or the project config `.cursor/mcp.json`. Read the file first, keep your other entries, then add this under the top-level `mcpServers` object:

        {
          "mcpServers": {
            "outsystems": {
              "url": "https://TENANT_HOSTNAME/mcp"
            }
          }
        }

    Use `mcpServers` as the key, not `servers`, and omit `type`. Cursor reads the transport from the URL.

1. Install the OutSystems skill. Save the [Cursor skill file](https://raw.githubusercontent.com/OutSystems/outsystems-mcp/refs/heads/main/cursor/skills/outsystems/SKILL.md) to `AGENTS.md` in your workspace root, which Cursor loads for the agent.

1. Verify and sign in from a terminal:

        agent mcp list
        agent mcp enable outsystems
        agent mcp login outsystems

1. Confirm the connection by asking `list 10 of my outsystems apps`.

Team and Enterprise plans install the Cursor app plugin from a Team Marketplace. For that path, refer to the [Cursor plugin setup](https://github.com/OutSystems/outsystems-mcp/blob/main/cursor/README.md).

## Connect GitHub Copilot

GitHub Copilot connects to the OutSystems MCP server in agent mode across VS Code, the CLI, and Visual Studio. VS Code loads the OutSystems skill from `.github/copilot-instructions.md` in your workspace.

<div class="info" markdown="1">

On a Copilot Business or Enterprise plan, an administrator enables the **MCP servers in Copilot** policy before the server appears.

</div>

To connect in VS Code, add the server and the OutSystems skill, then start the server:

1. Add the server to the workspace file `.vscode/mcp.json`, or to your user configuration. Read the file first, keep existing entries, then add this under the top-level `servers` object:

        {
          "servers": {
            "outsystems": {
              "type": "http",
              "url": "https://TENANT_HOSTNAME/mcp"
            }
          }
        }

    Use `servers` as the key. VS Code registers its own client through Dynamic Client Registration, so omit `oauth.clientId`.

1. Install the OutSystems skill. Save the [Copilot skill file](https://raw.githubusercontent.com/OutSystems/outsystems-mcp/refs/heads/main/copilot/skill.md) to `.github/copilot-instructions.md` in your workspace.

1. Start the server from the MCP configuration. A browser opens for OAuth on the first connection.

To connect in the Copilot CLI, register the server and reload the config:

1. Register the server:

        copilot mcp add --transport http outsystems https://TENANT_HOSTNAME/mcp

1. In a running session, type `/mcp reload` to load the server, then make an OutSystems request to start the OAuth flow.

## Connect Claude Desktop

Claude Desktop connects through a local proxy. The native **Add custom connector** flow doesn't complete OAuth with an OutSystems tenant, so use the `mcp-remote` proxy.

1. Confirm Node.js with `npx` is available, then install the proxy:

        npm install -g mcp-remote

1. Add the server to the Claude Desktop configuration file. The file is at one of these paths:

    * macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
    * Windows: `%APPDATA%\Claude\claude_desktop_config.json`
    * Linux: `~/.config/Claude/claude_desktop_config.json`

    Read the file first, keep every other entry, then add the `outsystems` entry under `mcpServers`. Use the shape for your operating system.

    On macOS and Linux:

        {
          "mcpServers": {
            "outsystems": {
              "command": "npx",
              "args": ["mcp-remote", "https://TENANT_HOSTNAME/mcp"]
            }
          }
        }

    On Windows:

        {
          "mcpServers": {
            "outsystems": {
              "command": "cmd",
              "args": ["/c", "npx mcp-remote https://TENANT_HOSTNAME/mcp"]
            }
          }
        }

1. Restart Claude Desktop. The first OutSystems tool call opens a browser for OAuth.

<div class="info" markdown="1">

To get the OutSystems skill in Claude Desktop, install the plugin from the same marketplace as Claude Code. Plugins require a paid plan.

</div>

## Connect another MCP host

Other MCP hosts connect to the same endpoint without validated setup. The OutSystems MCP server is a standard MCP endpoint over the Streamable HTTP transport with OAuth and Dynamic Client Registration, so MCP hosts that support this transport connect to it. OutSystems validates only the MCP hosts listed on this page.

1. Register `outsystems` as an MCP server in your MCP host, pointing at `https://TENANT_HOSTNAME/mcp` over the Streamable HTTP transport. Leave the callback port unset, so the host picks one automatically.
1. Add the OutSystems skill to the host's agent instructions from the [root skill file](https://raw.githubusercontent.com/OutSystems/outsystems-mcp/main/SKILL.md).
1. Start the MCP host's sign-in for the server, then complete the OAuth flow in the browser.

## Update the OutSystems skill

OutSystems updates the OutSystems MCP server on the tenant side, so the server needs no action from you. You update the OutSystems skill in your MCP host, which the plugin, the Power, or the saved skill file delivers.

* **Claude Code:** Run the following commands in this order, then restart Claude Code:

        claude plugin marketplace update outsystems
        claude plugin update outsystems@outsystems

    The first command refreshes Claude Code's copy of the OutSystems marketplace. The second command compares your installed plugin with that copy and installs the newer version. Run on its own, the second command compares with the old copy and reports that you already have the latest version.

* **Claude Desktop:** Uninstall the OutSystems plugin, reinstall it from the same marketplace, and restart Claude Desktop.
* **AWS Kiro:** Update the OutSystems Power from the Powers panel. If the panel offers no update, uninstall the Power and import it again from the same URL.
* **Cursor CLI and GitHub Copilot:** The saved skill file keeps the version you installed. Download the current [Cursor skill file](https://raw.githubusercontent.com/OutSystems/outsystems-mcp/refs/heads/main/cursor/skills/outsystems/SKILL.md) or [Copilot skill file](https://raw.githubusercontent.com/OutSystems/outsystems-mcp/refs/heads/main/copilot/skill.md) again, and replace the saved copy.
* **Cursor app:** A team administrator refreshes the `OutSystems/outsystems-mcp` import under **Plugins** > **Team Marketplaces** in the Cursor dashboard.

### Upgrade an earlier Claude Code setup

Before plugin version 0.20.0, the setup registered the server with `claude mcp add`, and that entry takes precedence over the server the plugin registers. When `claude mcp list` shows an `outsystems` entry instead of `plugin:outsystems:outsystems`, move to the plugin's server:

1. Set your tenant on the plugin:

        claude plugin install outsystems@outsystems --config tenant_hostname=TENANT_HOSTNAME

1. Remove the earlier entry:

        claude mcp remove outsystems -s user

1. Restart Claude Code, and sign in again on your next OutSystems request.

The OutSystems tools then use the `mcp__plugin_outsystems_outsystems__` prefix. Update any Claude Code permission rules or hooks that name the earlier `mcp__outsystems__` tools.

## Give feedback

The OutSystems MCP server includes a feedback tool, and it's the channel the OutSystems team uses for OutSystems MCP feedback. Every way of sending feedback from your MCP host goes through this tool. Use one of the following ways:

* In Claude Code, type `/outsystems-feedback` for a guided form, or `/outsystems-feedback MESSAGE` to submit directly. Replace `MESSAGE` with your feedback. The command sends your feedback through the feedback tool.
* In any MCP host, ask the agent in plain language, for example "send a thumbs-up about the OutSystems agent".

Before it submits, the agent removes secrets and personal data from your message, then reports what it replaced.

The agent can also report its own observations about the OutSystems tools, such as a lookup that returned no results when the agent expected data. The agent asks for your agreement once in each conversation before it sends any. Each observation contains a fixed category and one sentence that the agent writes, without your messages, code, or app content. When a tool call fails unexpectedly, the agent can also offer, once in each session, to send a bug report with the failed call and its error code.

## Next steps

The following pages cover authentication and your first workflow.

* To authenticate and run a first request, refer to [Get started with OutSystems MCP](get-started.md).
* To understand what you can do once connected, refer to [OutSystems MCP](outsystems-mcp-overview.md).
