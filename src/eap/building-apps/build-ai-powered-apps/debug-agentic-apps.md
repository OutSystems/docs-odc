---
guid: ed88ebbf-ca57-4d12-aa89-436c27d72c2d
locale: en-us
summary: Debug end-to-end flows that call AI agents by running separate debugging sessions for your consumer app and agentic app in ODC Studio.
tags: agentic apps,debugging,breakpoints,odc studio
platform-version: odc
app_type: mobile apps,reactive web apps
audience:
  - full stack developers
  - tech leads
outsystems-tools:
  - odc studio
coverage-type:
  - apply
figma: 
topic:
helpids: 
---

# Debug agentic apps

To debug an agentic app end to end, trace the execution from the consumer app event that starts the interaction to the agent logic that saves results back to the consumer app.

For end-to-end testing and debugging, triggering the agent through a workflow is the recommended approach. If your solution doesn’t use workflows, trace the execution from the consumer app’s **Run Server Action** that calls the agent.

<div class="info" markdown="1">

Agentic apps and consumer apps run in separate debugging sessions. Stepping into the agent service action from a consumer app isn't supported.

</div>

## Prerequisites

* You work in the Development stage.
* You published the latest version of both apps.
* You understand how to debug apps in ODC Studio. For more information, refer to [Debugging apps](../../debugging-apps/intro.md).
* Your consumer app triggers the workflow that calls the agentic app (recommended) or calls the agent from a **Run Server Action**.

## Debug an end-to-end flow that calls an agent

To debug your agentic app, follow these steps:

1. In ODC Studio, open the consumer app.
1. In the **Debugger** tab, select a debugging target and select **Start debugging**.
1. In ODC Studio, open the agentic app.
1. Add breakpoints as needed.
1. In the agentic app, select **Start debugging**.

    You may receive the following notification, which you can ignore:

    ```text
    There was an error loading the application for client-side debugging.
    The debugging session will be server-side only.
    ```

1. In the browser where the debugging session is running, trigger the agent call from the consumer app:

    1. Perform the user action or system event that triggers the agent call:

        * If your solution uses workflows (recommended), perform the action or event that starts the workflow.
        * If your solution doesn’t use workflows, perform the action that runs the **Run Server Action** that calls the agent.

    1. Complete any required steps that provide inputs to the agent call (for example, upload documents).
    1. If the trigger is automatic, wait for the agent call to run.

1. In ODC Studio, return to the agentic app and review the debugging output for the agent run.

    * Confirm the service action receives the expected input values.
    * Review the agent response text and any calculated decisions.
    * Check for errors on the node that saves results back to the consumer app.

1. Stop debugging in both apps.

## Related resources

* For more information about debugger controls and runtime inspection, refer to [Debugger tab reference](../../debugging-apps/debugger-ui-reference.md).
* For more information about setting breakpoints, refer to [Breakpoints](../../debugging-apps/breakpoints.md).
* For more information about validating behavior without debugging, refer to [Test agentic apps](testing.md).
