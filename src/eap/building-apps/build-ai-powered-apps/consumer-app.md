---
guid: 8f9e2d45-a1c7-4b62-9854-12e7f9b8c3a6
locale: en-us
summary: Learn how to build consumer apps that interact with AI agents, managing user sessions and processing user input through the agent workflow.
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=7613-159&p=f&t=JTOV8cE34sR9mPPz-0
coverage-type:
  - apply
topic:
  - road-to-automation
  - integration-patterns
  - creating-apps
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - mobile developers
  - full stack developers
  - tech leads
tags: consumer apps,ai agents,session management,user input,agent integration
outsystems-tools:
  - odc studio
helpids: 
---

# Consumer apps for AI agents

<div class="info" markdown="1">

Native ODC agent apps are only available to Early Access Program (EAP) customers.

</div>

Consumer apps are the user-facing applications that interact with AI agents to provide intelligent experiences to end users. These apps manage user sessions, process user input, and orchestrate communication with AI agents to deliver contextual, conversation-driven functionality.

When building consumer apps that interact with AI agents, you must provide two essential parameters: **UserInput** and **SessionId**. The UserInput contains the user's message, query, or request that the agent processes. The SessionId [maintains conversation context across multiple interactions](agentic-apps.md#state-persistence), ensuring the agent can reference previous exchanges and provide contextually relevant responses. Generate a unique SessionId using the `GenerateGuid` server action in ODC Studio, though you can use any method that produces a unique identifier.

## High-level process overview

A consumer app handles user interactions through a simple workflow that leverages [state persistence](agentic-apps.md#state-persistence):

1. **Session setup**: Generate a unique SessionId using `GenerateGuid`
1. **User interaction**: Capture UserInput from the UI components  
1. **Agent call**: Invoke the agent's service action with UserInput and SessionId
1. **Response handling**: Process and display the Response output parameter from the service action
1. **Session continuity**: Persist the SessionId for subsequent interactions

The following screenshot shows a consumer app's logic flow. The sample logic generates a unique session identifier using the built-in `GenerateGuid` server action. This action creates a globally unique identifier (GUID) that serves as the SessionId for maintaining conversation context, though any unique identifier generation method works. Add the `GenerateGuid` action to your logic by dragging it from the toolbox or typing its name in the action flow.

![Consumer app workflow diagram showing the interaction between user input, session management, and AI agent communication](images/consumer-app-ai-odcs.png "Consumer App Workflow")

<div class="info" markdown="1">

This example shows multiple server action calls from client actions for demonstration purposes. In production apps, minimize server action calls from client actions by consolidating logic into fewer server-side operations to improve performance and user experience.

</div>

On the agent app side, the service action receives UserInput and SessionId as input parameters and processes the request. The agent uses the SessionId to retrieve conversation context and track interaction history, while the UserInput contains the specific message or query to process. The agent then orchestrates the necessary actions—such as retrieving grounding data, building messages for the AI model, and generating a contextually relevant response—before returning the result through the Response output parameter to the consumer app.

![Agent app workflow](images/agent-app-logic-odcs.png "Agent app sample logic")
