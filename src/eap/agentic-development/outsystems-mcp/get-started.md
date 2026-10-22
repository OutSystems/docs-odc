---
summary: Set up OutSystems MCP in Claude Code with a guided file or manual steps, sign in, and confirm the connection with a first request.
tags:
  - Agentic
  - AI
  - Authentication
  - OAuth
  - Plugins
  - Troubleshooting
guid: 3d7c70ce-dbd2-47ee-a927-76b6009b0b84
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

# Get started with OutSystems MCP

This page shows you how to connect Claude Code, your MCP host, to OutSystems MCP from a terminal. You install the plugin, sign in, and run a first request.

To have an AI tool guide you instead, refer to [Use the guided setup file](#guided-setup). To use another MCP host, such as Cursor or AWS Kiro, refer to [Connect MCP hosts to OutSystems MCP](connect-mcp-hosts.md). For the MCP hosts that OutSystems validates, refer to [Supported MCP hosts](outsystems-mcp-overview.md#supported-mcp-hosts).

## Use the guided setup file {#guided-setup}

Give the guided setup file to your AI tool, and it sets up OutSystems MCP with you. It shows each step, runs the step, and asks for your confirmation before it continues. Setup changes nothing in your tenant.

1. Download the [guided setup file](resources/outsystems-mcp-setup.txt) and save it in an empty folder.
1. Open the empty folder in your AI tool.
1. Start a new session.
1. Ask your AI tool:

    * "Follow the instructions in @outsystems-mcp-setup.txt"

1. Answer the questions that your AI tool asks, and approve each step.

In Claude Code, the `@` reference attaches the file. In AWS Kiro, name the file in the prompt. In other AI tools, attach or name the file the way the tool does.

The guided setup file supports Claude Code in the **Code** tab of Claude Desktop and AWS Kiro. It also covers Cursor, GitHub Copilot, and the **Chat** tab of Claude Desktop. The **Code** tab requires a paid Claude plan.

## Prerequisites for the manual steps {#prerequisites}

You need the following before you start:

* The Claude Code command-line tool installed, so that the `claude` command runs in your terminal. To check, run `claude --version`. For more information about installing Claude Code, refer to the [Claude Code quickstart](https://code.claude.com/docs/en/quickstart).
* Your OutSystems tenant hostname, the host part of your OutSystems URL, for example `mycompany.outsystems.dev`.
* A web browser on the same machine as Claude Code. The sign-in redirect goes to a local loopback address.
* A tenant with OutSystems MCP enabled for your organization, and your user able to sign in to it.
* The ODC role permissions for the work you plan to do. The following permissions are examples for common workflows:
    * **Asset management** > **Create** to create an app.
    * **Asset management** > **Change** to change an app and publish it.
    * **Release management** > **Deploy assets** to deploy an app to another stage.
    * **Monitoring** > **Access asset logs and traces** to read an app's logs and traces.

A Personal Edition tenant has OutSystems MCP enabled and gives you these permissions. For the full list of permissions, refer to [ODC permissions](../../user-management/roles.md#permissions-registry).

## Install the OutSystems plugin

The OutSystems plugin registers the OutSystems MCP server in Claude Code and delivers the OutSystems skill. Install it once for your tenant.

<div class="info" markdown="1">

The manual steps on this page run in a terminal and assume that you're comfortable with command-line tools. To have an AI tool such as Claude Code or AWS Kiro set up OutSystems MCP with you instead, refer to [Use the guided setup file](#guided-setup).

</div>

1. Add the OutSystems marketplace:

        claude plugin marketplace add OutSystems/outsystems-mcp

1. Install the plugin with your tenant hostname:

        claude plugin install outsystems@outsystems --config tenant_hostname=TENANT_HOSTNAME

    Replace `TENANT_HOSTNAME` with your tenant hostname. Use the bare hostname, without `https://` or a path.

1. Confirm the plugin registered the server:

        claude mcp list

    The output lists `plugin:outsystems:outsystems` with the URL `https://TENANT_HOSTNAME/mcp` and the status `Needs authentication`, which clears after you sign in.

1. Restart Claude Code so it loads the server.

## Sign in

Claude Code signs you in through the browser the first time you call an OutSystems tool, using the plugin's authenticate tool.

1. Open Claude Code in a working folder by running `claude`.
1. Ask the agent an OutSystems request, for example:

    * "Which environments do I have in OutSystems?"

1. The agent returns an authorization URL. Open it in your browser, sign in, and approve access.
1. Confirm what happens next based on where Claude Code runs:
    * On your local machine, where the browser reaches the loopback address, the OutSystems tools load and the request continues. Tell the agent once you approve.
    * On a remote machine, such as an SSH session or a container, the redirect page fails to load even though sign-in already succeeded. Copy the full URL from the browser's address bar and paste it back to the agent, which completes the flow with it.

If Claude Code shows an MCP setup warning before you authenticate, continue with the first request. The connection completes after you authorize in the browser.

Depending on your Claude Code permission settings, Claude Code asks you to allow each OutSystems tool before the agent first runs it. Allow the tool, and the request continues.

Your sign-in persists across requests. When it expires, the agent prompts you to authenticate again and retries the request.

### Sign in with a command

If the sign-in doesn't start, or a request fails with an authentication error, start the sign-in yourself with one of the following options.

* **Terminal command:** Run the following command in a terminal. It opens your browser, and it reports when the sign-in completes:

        claude mcp login plugin:outsystems:outsystems

    On a remote machine, add the `--no-browser` option. The command prints the authorization URL. After you sign in, paste the redirect URL only at the command's prompt.

* **Slash command:** In a Claude Code session, run `/mcp`, select the `outsystems` server that comes from the plugin, and choose **Authenticate**.

If a running Claude Code session doesn't list the OutSystems tools after the sign-in, restart Claude Code. To clear the stored sign-in, run `claude mcp logout plugin:outsystems:outsystems`.

## Verify the connection

Confirm the connection by asking for something only your tenant answers.

1. Ask the agent:

    * "Which environments do I have in OutSystems?"

1. Confirm the response lists your tenant's stages, such as Development. A Personal Edition tenant lists one stage, Development.

This request lists stages rather than apps, so it returns results on a tenant that has no apps. To list the apps in your tenant, ask the agent:

* "List the apps in my OutSystems tenant."

If a call returns a `tenant_not_allowed` rejection, your sign-in succeeded, but your tenant needs OutSystems MCP enabled. The rejection comes from a server-side check, so reinstalling the plugin leaves the result unchanged. Ask your organization to enable OutSystems MCP.

## Next steps

With the connection working, build a first app, then read the delegation model before you run other workflows, because the delegation model determines how the tools behave.

* To build a first app from a sample prompt file, refer to [Build your first app](build-first-app.md).
* To understand how the agent and Mentor divide the work, refer to [Delegation to Mentor](mentor-delegation.md).
* To see example prompts for evolving an app end to end, refer to [Evolve an existing app](evolve-app.md).
* To send feedback about OutSystems MCP, refer to [Give feedback on OutSystems MCP](give-feedback.md).
