---
guid: 30ca1648-f01f-4193-b2a5-1b0ebf351102
locale: en-us
summary: Develop AI agents in OutSystems Developer Cloud (ODC) using ODC Studio, configure their capabilities, and integrate them with your mobile and reactive web apps.
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?m=auto&node-id=7614-231&t=xAl8FSPFM1T6mRgI-1
coverage-type:
  - apply
topic:
  - road-to-automation
  - integration-patterns
  - outsystems-overview
  - creating-apps
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - full stack developers
tags: ai agent development,odc studio,outsystems ai,large language models,mobile apps
outsystems-tools:
  - odc studio
helpids: 
---

# Creating an AI agent in ODC Studio

<div class="info" markdown="1">

Native ODC agent apps are only available to Early Access Program (EAP) customers.

</div>

Use ODC Studio to define your AI agent's purpose, structure its capabilities, and develop the underlying logic that powers its actions. After creating the agent, you can reference its functionality in the consumer app.

## Prerequisites

Before creating an AI agent in ODC, ensure you have configured and set up an [AI model in the ODC Portal](add-ai-models.md). 

## High-level process for using AI agents in ODC 

Follow these steps to create, configure, and integrate AI agents into your OutSystems apps, enhancing their intelligence and interactivity.

![Diagram showing the high-level process for creating, configuring, and integrating AI agents in OutSystems Developer Cloud (ODC).](images/use-agents-diag.png "High-level process for using AI agents in ODC")

1. Create an AI agent app

You build your AI agent app in ODC Studio. To start your creation journey, you can either go directly to ODC Studio or begin from the ODC Portal. In the ODC Portal, click **Create** and select **Agent** to go to ODC Studio, where you can define and develop your agent's capabilities.

1. Choose an AI model 

Select the large language model (LLM) your agent uses for its core intelligence. Refer to [Adding AI Models](add-ai-models.md) for more information about connecting your OutSystems apps to LLMs.

1. Build the AI agent's core functionality

An `AgentTask` action encapsulates an AI agent's core functionality. This server action orchestrates the interaction with the AI model and handles data preparation and response processing. A typical `AgentTask` action wraps a sequence of server actions:

* `GetGroundingData`: Retrieves any necessary contextual or [grounding data](agentic-apps.md#grounding) the AI model needs to provide a relevant and accurate response. Grounding data provides the AI with specific, up-to-date, or proprietary information beyond its general training. Through this action, you implement custom logic to gather and prepare the exact context the AI model requires. The action gets this context from the app's data sources, such as AI search service, REST API, aggregate, or static text, to enrich your agent's knowledge and context.  
* `BuildMessages`: Constructs the prompt and conversation history (messages) that the AI model receives. It combines user input, historical conversation turns, and contextual or grounding data retrieved by the `GetGroundingData` action into a format the chosen AI model understands. An Assign node within this logic allows you to define the [system prompt](agentic-apps.md#system-prompts).  
* `Call<AIModelName>`: Transmits the formatted messages to the selected AI model and receives its response.  
* `StoreMemory`: Saves the conversation or generated information for future reference. This maintains context and enables multi-turn conversations or personalized interactions. For more information about state persistence, refer to [Agentic apps in ODC](agentic-apps.md#state-persistence).

The service action is what encapsulates the AI agent's core logic. Once published, your Service Action becomes available for other apps to reference and consume.

1. Reference agent service action in the consumer app

After publishing your AI agent app, to use it in another app, you must establish a dependency on its service action. This makes the AI agent's capabilities available within your consumer app's logic. This service action appears as `Call<AgentName>`. 

1. Add `Call<AgentName>` to logic

Integrate the AI agent's functionality into your consumer app. When calling the agent, ensure you pass parameters such as `SessionId`, to maintain conversational context, and `UserInput`, the user's query or instruction. 

## Next steps

For more information about how to consume a `Call<AgentName>` Service Action in your consumer app, refer to [Consuming an agent in an app](consumer-app.md).
