---
summary: Connect unattended AI agents to OutSystems MCP in ODC with an API client. A token script keeps long agent runs going without a browser sign-in.
tags:
  - Agentic
  - AI
  - Authentication
  - Authorization
  - OAuth
  - Security
guid: 6c6f27f7-39fb-4c39-8d8b-066abd0fe553
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

# Connect unattended agents to OutSystems MCP with an API client

Some AI agents run without a person present, such as in a scheduled job or a continuous integration (CI) pipeline. To connect these agents to OutSystems MCP, authenticate them with an ODC API client. A browser sign-in expires, and a long agent run stops until someone signs in again. With an API client, a token script gets an access token from the client credentials. When the token expires, the script gets a new one.

Use an API client only for agents that run on their own. OutSystems MCP runs every operation of the agent as the API client, with the permissions of the API client. For agents that you start and follow, keep the browser sign-in, so their operations run under your identity. For more information, refer to [Get started with OutSystems MCP](get-started.md).

This page covers Claude Code.

<div class="info" markdown="1">

To connect another MCP host with an API client, refer to the documentation of the MCP host. The MCP host must send an `Authorization` header with each request or support the OAuth client credentials flow. Also check whether the MCP host requests a new token when the token expires. If the MCP host doesn't, restart it with a new token within 12 hours. To get a token, run the token script from [Configure Claude Code for agent runs](#configure-claude-code). The script prints the `Authorization` header as JSON.

</div>

## Prerequisites

You need the following before you start:

* An API client for each agent pipeline, with its client ID and client secret. For more information, refer to [Configure API access using an API client](../../reference/apis/public-rest-apis/authentication/create-api-client.md).
* The permissions that the agent's work requires, granted to the API client. An API client needs the same permissions that a member needs for the same operation. If the agent uses Mentor, grant the API client the **Mentor** > **Use** permission.
* Claude Code 2.1.238 or later, with the OutSystems plugin installed. Earlier versions of Claude Code don't run the token script again when a token expires. For the plugin installation, refer to [Install the OutSystems plugin](get-started.md#install-the-outsystems-plugin).
* Your ODC tenant hostname, the host part of your ODC Portal URL, for example `mycompany.outsystems.dev`.
* `curl` on macOS and Linux, or PowerShell 7 on Windows.

## Configure Claude Code for agent runs {#configure-claude-code}

Create a configuration file that only agent runs use. Your own Claude Code sessions keep the browser sign-in, because the configuration file applies only to the runs that you start with it. Claude Desktop doesn't accept command-line options, so these steps use the Claude Code command-line tool.

1. Download the token script for your operating system, and save it in a folder outside your code repositories:

    * [odc-mcp-token.sh](resources/odc-mcp-token.sh) for macOS and Linux. Make the file executable with `chmod +x odc-mcp-token.sh`.
    * [odc-mcp-token.ps1](resources/odc-mcp-token.ps1) for Windows.

    The script requests an access token with the API client credentials and prints it as an `Authorization` header. The script stores nothing on disk.

1. Store the client secret where the token script reads it. Use one of the following options:

    * **macOS keychain:** Run `security add-generic-password -s odc-mcp -a CLIENT_ID -w`, and enter the client secret at the prompt.
    * **Linux secret service:** Run `secret-tool store --label odc-mcp service odc-mcp account CLIENT_ID`, and enter the client secret at the prompt.
    * **Windows Credential Manager:** Add a generic credential with the name `odc-mcp:CLIENT_ID` and the client secret as the password. The script reads the credential through the CredentialManager PowerShell module. To install the module, run `Install-Module CredentialManager -Scope CurrentUser`.
    * **Secret file:** Save the client secret as the only content of a file that only your user account can read. In the next step, add `ODC_CLIENT_SECRET_FILE=` followed by the full path of the file to the `headersHelper` command. On Windows, set `ODC_CLIENT_SECRET_FILE` as a user environment variable.

    Replace `CLIENT_ID` with the client ID of the API client.

1. In the folder where you start agent runs, create a file named `agent-mcp.json` with the following content:

        {
          "mcpServers": {
            "outsystems": {
              "type": "http",
              "url": "https://TENANT_HOSTNAME/mcp",
              "headersHelper": "ODC_TENANT=TENANT_HOSTNAME ODC_CLIENT_ID=CLIENT_ID SCRIPT_PATH"
            }
          }
        }

    Replace the following:

    * `TENANT_HOSTNAME`: your ODC tenant hostname, without `https://` or a path.
    * `CLIENT_ID`: the client ID of the API client.
    * `SCRIPT_PATH`: the full path of `odc-mcp-token.sh`.

    On Windows, set `ODC_TENANT` and `ODC_CLIENT_ID` as user environment variables, and set `headersHelper` to `pwsh -NoProfile -File SCRIPT_PATH`, with the full path of `odc-mcp-token.ps1`.

    The file holds no secret. Keep the server name `outsystems`.

1. Start the agent run with the configuration file:

        claude -p --mcp-config agent-mcp.json --strict-mcp-config "PROMPT"

    Replace `PROMPT` with the task for the agent. The `-p` option runs Claude Code without an interactive session. The `--strict-mcp-config` option makes Claude Code use only the MCP servers in `agent-mcp.json`. If the agent needs other MCP servers, add them to the same file.

1. Confirm that the agent runs as the API client. Run the command from the previous step with the following prompt as `PROMPT`:

    * "Check the OutSystems authentication status."

    The response shows the user name `service-account-` followed by the client ID.

An access token is valid for 12 hours, and the API client receives no refresh token. Claude Code runs the token script when it connects to OutSystems MCP. When OutSystems MCP rejects an expired token, Claude Code runs the script again and retries the call, so the agent run continues.

## Limits for unattended agents

Mentor isolates sessions per API client, not per agent.

<div class="warning" markdown="1">

Agents that use the same API client can read, prompt, and close each other's Mentor sessions when they have the session ID. Agents that use different API clients can't access each other's sessions. To keep agent runs apart, use one API client for each agent pipeline, and keep session IDs out of shared logs and shared agent memory. For more information about Mentor sessions, refer to [Delegation to Mentor](mentor-delegation.md).

</div>

The following limits also apply to agents that authenticate with an API client:

* **Asset scope:** You can't limit the Asset management permissions of an API client to individual apps, as you can with an app-scope role for a member. Grant the API client only the permissions that the agent's work needs.
* **Attribution:** OutSystems MCP attributes every change that the agent makes to the API client, not to the person who started the agent run.
