---
summary: Authenticate Claude Code to OutSystems MCP and confirm the connection with a first tenant request.
tags: getting started, setup, claude code, oauth, mcp, mcp host
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

This page describes how to set up OutSystems MCP (also known as OutSystems Agent Experience) in Claude Code, your MCP host. The steps cover installing the OutSystems plugin, signing in, and running a first request. If you use another MCP host, such as Cursor or AWS Kiro, follow the steps for your host in [Connect MCP hosts to OutSystems MCP](connect-mcp-hosts.md) instead. For the MCP hosts OutSystems validates, refer to [Supported MCP hosts](outsystems-mcp-overview.md#supported-mcp-hosts).

## Prerequisites

You need the following before you start:

* Claude Code installed.
* Your OutSystems tenant hostname, the host part of your OutSystems URL, for example `mycompany.outsystems.dev`.
* A web browser on the same machine as Claude Code. The sign-in redirect goes to a local loopback address.
* A tenant with OutSystems MCP enabled for your organization, and your user able to sign in to it.
* The ODC role permissions for the work you plan to do. The following permissions are examples for common workflows:
    * **Asset management** > **Create** to create an app.
    * **Asset management** > **Change** to change an app and publish it.
    * **Release management** > **Deploy assets** to deploy an app to another stage.
    * **Monitoring** > **Access asset logs and traces** to read an app's logs and traces.

For the full list of permissions, refer to [ODC permissions](../../user-management/roles.md#permissions-registry).

## Install the OutSystems plugin

The OutSystems plugin registers the OutSystems MCP server in Claude Code and delivers the OutSystems skill. Install it once for your tenant.

1. Add the OutSystems marketplace:

        claude plugin marketplace add OutSystems/outsystems-mcp

1. Install the plugin with your tenant hostname:

        claude plugin install outsystems@outsystems --config tenant_hostname=TENANT_HOSTNAME

    Replace `TENANT_HOSTNAME` with your tenant hostname. Use the bare hostname, without `https://` or a path.

1. Confirm the plugin registered the server:

        claude mcp list

    The output lists `plugin:outsystems:outsystems` with the URL `https://TENANT_HOSTNAME/mcp`.

1. Restart Claude Code so it loads the server.

## Sign in

Claude Code signs you in through the browser the first time you call an OutSystems tool, using a built-in authenticate tool that runs the flow automatically.

1. Open Claude Code in a working folder by running `claude`.
1. Ask the agent an OutSystems request, for example:

    * "Which environments do I have in OutSystems?"

1. The agent returns an authorization URL. Open it in your browser, sign in, and approve access.
1. Confirm what happens next based on where Claude Code runs:
    * On your local machine, where the browser reaches the loopback address, the OutSystems tools load and the request continues. Tell the agent once you approve.
    * On a remote machine, such as an SSH session or a container, the redirect page fails to load even though sign-in already succeeded. Copy the full URL from the browser's address bar and paste it back to the agent, which completes the flow with it.

If Claude Code shows an MCP setup warning before you authenticate, continue with the first request. The connection completes after you authorize in the browser.

Depending on your Claude Code permission settings, Claude Code asks you to allow each OutSystems tool before the agent first runs it. Allow the tool, and the request continues.

If the sign-in doesn't start, or a request fails with an authentication error, run `/mcp` in Claude Code, select the `outsystems` server that comes from the plugin, and choose **Authenticate**.

Your sign-in persists across requests. When it expires, the agent prompts you to authenticate again and retries the request.

## Verify the connection

Confirm the connection by asking for something only your tenant answers.

1. Ask the agent:

    * "Which environments do I have in OutSystems?"

1. Confirm the response lists your tenant's stages, such as Development.

This request lists stages rather than apps, so it returns results on a tenant that has no apps. To list the apps in your tenant, ask the agent:

* "List the apps in my OutSystems tenant."

If a call returns a `tenant_not_allowed` rejection, your sign-in succeeded, but your tenant needs OutSystems MCP enabled. The rejection comes from a server-side check, so reinstalling the plugin leaves the result unchanged. Ask your organization to enable OutSystems MCP.

## Next steps

With the connection working, build a first app, then read the delegation model before you run other workflows, because the delegation model determines how the tools behave.

* To build a first app from a sample prompt file, refer to [Build your first app](build-first-app.md).
* To understand how the agent and Mentor divide the work, refer to [Delegation to Mentor](mentor-delegation.md).
* To see example prompts for evolving an app end to end, refer to [Evolve an existing app](evolve-app.md).
