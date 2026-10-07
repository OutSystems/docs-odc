---
summary: How custom C# code becomes a governed external library in OutSystems, and how you bring it in and integrate it into an app from your MCP host.
tags: external library, c#, extend, mcp host, agentic development
guid: c8c0c926-77d2-4286-a27d-14b1148393c0
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - claude code
  - mentor
coverage-type:
  - understand
  - apply
content-type:
  - conceptual
  - process
audience:
  - Developer
topic:
  - creating-apps
isautopublish: true
---

# Extend an app with custom C# code

When ODC's standard logic doesn't cover what you need, you extend an app with custom C# code packaged as an external library. With OutSystems MCP, you ask the agent in your MCP host to bring that library into your tenant and integrate it into an app. The platform validates, versions, and governs the library the same way as any other external library.

This page explains how the parts fit together and describes the process at a high level. Your MCP host lists the exact tool names. The External Libraries SDK documentation covers how to build the library.

## External libraries and OutSystems MCP

An external library is custom .NET code that OutSystems exposes as reusable server actions and structures. Apps consume it like any other library, without knowing the C# behind it.

The work runs in three places, and the agent coordinates the OutSystems part:

* You build and package the library with the External Libraries SDK, in your own IDE. You build the same library as for any ODC app. For more information, refer to [Extend your apps with custom code](../../building-apps/external-logic/intro.md) and the [SDK README](../../building-apps/external-logic/README.md).
* The agent brings the package into the tenant and integrates it into an app, through the OutSystems MCP server.
* The platform generates the library, holds it for review, publishes it as a tenant-level asset, and applies the same role permissions as any other operation.

## Library integration process

The first stage runs in your IDE, and the other stages run through the agent in your MCP host:

1. **Build and package.** Write the C# with the SDK, decorate it with the SDK attributes, and package it as described in the [SDK documentation](../../building-apps/external-logic/README.md). The result is a single package ready to upload.
1. **Bring it into the tenant.** Your agent uploads the package. By default, the platform generates the library and holds it in a review state until you publish it. An upload set to auto-publish publishes the library directly. Uploading and publishing both change tenant state. Publishing a library under an existing name creates a new revision of that library.
1. **Check the result.** Inspect the generated server actions and structures the library exposes, and read the validation messages if generation or publication fails.
1. **Integrate it into an app.** Ask Mentor to use the library's actions in the app you're changing, then publish and deploy the app as usual. For the build-and-ship flow, refer to [Evolve an existing app](evolve-app.md).

## Behavior and limitations

The following characteristics affect how long the process takes and when it needs a manual step:

* Generation and publication run as background operations and can take time. Your agent polls until each one reaches a terminal state.
* If generation or publication fails, the validation messages name the cause. Fix the C# and upload again.
* Mentor can fail to add the library reference to an app. If the agent can't add the dependency, add it to the app in ODC Studio, then continue from your MCP host.

## Related

The following pages support this workflow:

* [Extend your apps with custom code](../../building-apps/external-logic/intro.md) and the [SDK README](../../building-apps/external-logic/README.md): build and package the C# library.
* [Delegation to Mentor](mentor-delegation.md): how the integration step runs.
* [Tool reference](tool-reference.md): the external-library tools, under Platform Services.
* [Governance in OutSystems MCP](governance.md): the access controls that apply when you publish.
