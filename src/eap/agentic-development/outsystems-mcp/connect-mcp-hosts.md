---
summary: Connect your MCP host to the OutSystems MCP server, with setup for Claude Code, AWS Kiro, Cursor, GitHub Copilot, and Claude Desktop.
tags:
  - Agentic
  - AI
  - Authentication
  - OAuth
  - Plugins
  - Settings
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
  - Platform administrator
topic:
  - creating-apps
isautopublish: true
---

# Connect MCP hosts to OutSystems MCP

This page shows you how to connect your MCP host, the AI application you work in, to the OutSystems MCP server. It covers Claude Code, Cursor, AWS Kiro, GitHub Copilot, and Claude Desktop, and the settings any other MCP host needs. Each MCP host also loads the OutSystems skill, the instructions that tell the agent how to use the OutSystems tools. The install steps differ per MCP host, and each MCP host has its own section on this page. After you connect, refer to [Get started with OutSystems MCP](get-started.md) to authenticate and run a first request. For the terms this page uses, such as MCP host, OutSystems skill, OutSystems plugin, and OutSystems Power, refer to [Agentic development terminology](../agentic-development-terminology.md).

<div class="info" markdown="1">

The steps on this page assume that you're comfortable with command-line tools and configuration files. To have an AI tool such as Claude Code or AWS Kiro set up OutSystems MCP with you instead, refer to [Use the guided setup file](get-started.md#guided-setup).

</div>

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

    Put the URL under the top-level `mcpServers`. Kiro rewrites the `powers` block, including `powers.mcpServers`, on every Power update, which drops a URL stored there.

1. Ask Kiro Chat for an OutSystems request. Kiro opens the browser for OAuth on the first tool call, and you complete the sign-in there. Kiro runs the sign-in flow itself.

## Connect Cursor

Cursor is a validated MCP host. You connect it from the Cursor IDE or the Cursor CLI. Both paths read the same `mcp.json` file and open your default browser for sign-in. The CLI path works on every plan, including individual accounts. Cursor loads the OutSystems skill from `AGENTS.md` in your workspace root.

### Add the server and the skill

Add the OutSystems MCP server to the Cursor configuration, then install the OutSystems skill. The IDE and CLI paths both use these steps.

1. Add the server to the global config `~/.cursor/mcp.json`, or the project config `.cursor/mcp.json`. Cursor merges both files, and the project entry takes priority when the same server name appears in both. Read the file first, keep your other entries, then add this under the top-level `mcpServers` object:

        {
          "mcpServers": {
            "outsystems": {
              "url": "https://TENANT_HOSTNAME/mcp"
            }
          }
        }

    Use `mcpServers` as the key and omit `type`. Cursor reads the transport from the URL. An entry copied from another MCP host's configuration file uses that host's keys, and Cursor skips it silently.

1. Install the OutSystems skill. Save the [Cursor skill file](https://raw.githubusercontent.com/OutSystems/outsystems-mcp/refs/heads/main/cursor/skills/outsystems/SKILL.md) to `AGENTS.md` in your workspace root, which Cursor loads for the agent. Cursor loads `.mdc` files with rule frontmatter from `.cursor/rules/`, so a plain Markdown copy saved there is ignored.

### Sign in from the Cursor IDE

Cursor starts the sign-in when it loads the server entry. To sign in and confirm the connection:

1. Save `mcp.json`. Cursor opens your default browser.
1. Complete the sign-in in the browser.
1. In Cursor, open the **MCPs** tab and select `outsystems`. Confirm that **Local** shows **Connected** under **Environments**.
1. Confirm the connection by asking `list 10 of my outsystems apps` in Cursor chat.

### Sign in from the Cursor CLI

The Cursor CLI provides the `agent` command. To install it, approve the server, and sign in:

1. Install the Cursor CLI. On macOS, Linux, and WSL, run the following command:

        curl https://cursor.com/install -fsS | bash

    On Windows, run the following command in PowerShell:

        irm 'https://cursor.com/install?win32=true' | iex

    For more information, refer to the [Cursor CLI installation](https://cursor.com/docs/cli/installation) page.

1. Run the following commands in a terminal. The last command opens your default browser to sign in:

        agent mcp list
        agent mcp enable outsystems
        agent mcp login outsystems

    The `login` command requires an approved server, and an unapproved server fails with `has not been approved`. Run `agent mcp enable outsystems` when `agent mcp list` shows `outsystems` as needing approval.

1. Confirm the connection by running the following command in the terminal:

        agent "list 10 of my outsystems apps"

### Install the plugin for a team

Team and Enterprise plans install the Cursor app plugin from a Team Marketplace. A team administrator imports the `OutSystems/outsystems-mcp` repository under **Plugins** > **Team Marketplaces** in the Cursor dashboard. Marketplace plugins require a Team or Enterprise plan, so free and individual plans use the steps in the previous sections. For the plugin path, refer to the [Cursor plugin setup](https://github.com/OutSystems/outsystems-mcp/blob/main/cursor/README.md).

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

Claude Desktop connects through the `mcp-remote` local proxy, which completes the OAuth flow with an OutSystems tenant.

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

Other MCP hosts connect to the same endpoint with a generic setup. The OutSystems MCP server is a standard MCP endpoint over the Streamable HTTP transport with OAuth and Dynamic Client Registration, so MCP hosts that support this transport connect to it. The MCP hosts listed on this page are the ones OutSystems validates.

1. Register `outsystems` as an MCP server in your MCP host, pointing at `https://TENANT_HOSTNAME/mcp` over the Streamable HTTP transport. Leave the callback port unset, so the host picks one automatically.
1. Add the OutSystems skill to the host's agent instructions from the [root skill file](https://raw.githubusercontent.com/OutSystems/outsystems-mcp/main/SKILL.md).
1. Start the MCP host's sign-in for the server, then complete the OAuth flow in the browser.

## Update the OutSystems skill

OutSystems updates the OutSystems MCP server on the tenant side. You update the OutSystems skill in your MCP host, which the plugin, the Power, or the saved skill file delivers.

* **Claude Code:** Run the following commands in this order, then restart Claude Code:

        claude plugin marketplace update outsystems
        claude plugin update outsystems@outsystems

    The first command refreshes Claude Code's copy of the OutSystems marketplace. The second command compares your installed plugin with that copy and installs the newer version. Run on its own, the second command compares with the old copy and reports that you already have the latest version.

* **Claude Desktop:** Uninstall the OutSystems plugin, reinstall it from the same marketplace, and restart Claude Desktop.
* **AWS Kiro:** Update the OutSystems Power from the Powers panel. To reinstall the latest version, uninstall the Power and import it again from the same URL.
* **Cursor CLI and GitHub Copilot:** The saved skill file keeps the version you installed. Download the current [Cursor skill file](https://raw.githubusercontent.com/OutSystems/outsystems-mcp/refs/heads/main/cursor/skills/outsystems/SKILL.md) or [Copilot skill file](https://raw.githubusercontent.com/OutSystems/outsystems-mcp/refs/heads/main/copilot/skill.md) again, and replace the saved copy.
* **Cursor app:** A team administrator refreshes the `OutSystems/outsystems-mcp` import under **Plugins** > **Team Marketplaces** in the Cursor dashboard.

### Upgrade an earlier Claude Code setup

Before plugin version 0.20.0, the setup registered the server with `claude mcp add`, and that entry takes precedence over the server the plugin registers. When `claude mcp list` shows an `outsystems` entry, move to the plugin's server, which appears as `plugin:outsystems:outsystems`:

1. Set your tenant on the plugin:

        claude plugin install outsystems@outsystems --config tenant_hostname=TENANT_HOSTNAME

1. Remove the earlier entry:

        claude mcp remove outsystems -s user

1. Restart Claude Code, and sign in again on your next OutSystems request.

The OutSystems tools then use the `mcp__plugin_outsystems_outsystems__` prefix. Update any Claude Code permission rules or hooks that name the earlier `mcp__outsystems__` tools.

## Give feedback

The feedback tool of the OutSystems MCP server sends feedback about OutSystems MCP. For the ways to send feedback from your MCP host, refer to [Give feedback on OutSystems MCP](give-feedback.md).

## Next steps

The following pages cover authentication and your first workflow.

* To authenticate and run a first request, refer to [Get started with OutSystems MCP](get-started.md).
* To understand what you can do once connected, refer to [OutSystems MCP](outsystems-mcp-overview.md).
* To send feedback about OutSystems MCP, refer to [Give feedback on OutSystems MCP](give-feedback.md).
