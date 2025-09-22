---
guid: 24d5a0ea-68c8-4851-b7de-e0908c122862
locale: en-us
summary: Integrate AI capabilities in your apps using AI models or agents in OutSystems Developer Cloud (ODC) to build intelligent, autonomous applications.
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=7782-132&p=f&t=KL8VHzLPQQ7E5ZHx-0
coverage-type:
  - understand
  - evaluate
topic:
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - full stack developers
  - tech leads
  - backend developers
tags: ai models,ai agents,integration,automation,odc studio
outsystems-tools:
  - odc studio
helpids: 30646, 30647, 30649, 30650
---

# Agentic apps in ODC

<div class="info" markdown="1">

AI agent creation is available through the Early Access Program. Click here to [apply for the Early Access Program](https://www.outsystems.com/low-code-platform/agentic-ai-workbench/eap-agent-workbench/).

</div>

In ODC Studio, you can integrate AI capabilities into your apps either by calling AI models directly or by orchestrating them through AI agents. Choose the approach that matches how dynamic and autonomous the required behavior must be.

An **agentic app** uses one or more AI agents to perform tasks, automate workflows, or handle complex multi‑step interactions. Unlike traditional apps that rely on direct user input for each step, agentic apps can act autonomously or semi‑autonomously—making decisions, invoking external tools, and coordinating logic. These apps consume the capabilities exposed by AI agents.

## AI models

In ODC, an AI model is a pre-trained algorithm or deployed machine learning service that provides a specific capability (for example, summarization, extraction, or generation). Call these models directly from your app logic using the `Call<AIModelName>` server action. For more information, see [AI models and search services in ODC](ai-models.md).

## Use AI agents

AI agents in ODC run without a user interface. They orchestrate AI models, business data, and external tools to add autonomy and decision-making. An agent app consumes AI model capabilities via a `Call<AIModelName>` server action and exposes its logic through a `Call<AgentName>` service action to any consuming app. For more information, see [Build AI-powered apps](intro.md).

![ODC Studio interface showing options to create a Web app, Mobile app, or Agent.](images/agent-app-odcs.png "ODC Studio App Creation Options")

### Understand the relationship

An AI model provides a focused capability. An AI agent is the orchestrator that combines models, application logic, data sources, and external tools to achieve a larger goal.

## AI agent fundamentals

Key AI fundamentals help ensure AI models within an agent operate effectively and align with your app's goals: **grounding**, **system prompts**, and **state persistence**.

### Grounding { #grounding }

Grounding means providing an AI model with relevant, factual, real-world context and data specific to the task. AI models are powerful but generic. Without grounding, their responses might be abstract, irrelevant, or incorrect for your use case.

* **Why it matters for agents:** Agents often use dynamic, business-specific information. Grounding ensures the AI model operates within your app's data and rules. For example, if an agent processes customer orders, grounding involves providing details like current inventory, customer history, or product specifications.
* **How it works in ODC agents:** In ODC, the `GetGroundingData` action (part of the AgentTask logic) retrieves and prepares this contextual information. Sources can include internal aggregates, search services (RAG), or external tools. This data becomes part of the input to the AI model, allowing it to make more informed and accurate decisions or generate more relevant outputs. For more information, see [Creating an AI agent in ODC Studio](create-agent.md).
* **Benefits:** Grounding improves the accuracy, relevance, and reliability of the AI model's outputs. It prevents the AI from providing generic responses by tethering its understanding to your app's reality.

### System prompts { #system-prompts }

System prompts (also called system instructions or system messages) are instructions or a persona given to an AI model at the start of a conversation or task. They define the AI's role, behavior, constraints, and overall objective. Unlike user prompts, which are dynamic, the system prompt sets the foundational guidelines for the AI's responses.

* **Why it matters for agents:** Within an agent, a system prompt guides the AI model's reasoning and output generation to align with the agent's purpose. For example, if an agent acts as a "customer support specialist," the system prompt instructs the AI to be helpful and only provide information from approved sources.
* **How it works in ODC agents:** The `BuildMessages` action in an ODC agent's logic constructs the full prompt for the AI model, injecting the system prompt. It sets the stage before adding user input or task-related data. When the agent can call external tools, clarify in the system prompt when the AI should request a tool invocation. For more information, see [Creating an AI agent in ODC Studio](create-agent.md).
* **Benefits:** System prompts control the AI's tone, style, and scope. They ensure the AI model consistently performs its role as intended by the agent's design, preventing it from deviating into unintended behaviors or topics. This helps maintain control and predictability over the agent's actions.

### State persistence { #state-persistence }

State persistence is the ability of an AI agent to retain and recall information from past interactions, decisions, or observations. Unlike single-shot AI model calls, which are stateless, memory allows an agent to build a continuous understanding of a situation, user, or ongoing process.

* **Why it matters for agents:** For an agent to perform complex, multi-step tasks or engage in extended interactions, it must remember what has occurred. Without memory, each interaction is isolated, leading to repetitive questions, incoherent responses, or an inability to complete processes that span multiple steps or sessions. Memory enables personalization, context retention, and learning over time.
* **How it works in ODC agents:** In ODC, the `StoreMemory` action, a key part of the AgentTask logic, serves this purpose. This action lets developers explicitly save relevant data, such as previous user queries, AI model outputs, intermediate decisions, or system states, that the agent might need to recall in future interactions or steps. You can then retrieve and integrate this stored memory into subsequent prompts or decision-making. For more information, see [Creating an AI agent in ODC Studio](create-agent.md).
* **Benefits:** Memory enhances the agent's intelligence and utility by enabling it to:
  * Maintain conversational context across multiple turns.
  * Learn from past interactions to improve future performance.
  * Execute multi-stage workflows without losing track of progress.
  * Provide personalized experiences based on historical data.

By applying grounding, system prompts, and state persistence, you can use AI models within agents to create reliable and intelligent automation solutions.

### External tools

Agents can call external tools to retrieve data or perform operations in other systems. In ODC, external tools come from either:

* **Custom MCP servers** – you host or configure a service that implements the Model Context Protocol (open standard).  
* **Prebuilt connectors** – curated integrations for popular APIs that are not MCP implementations (for example, SerpAPI for search enrichment).

External tools let agents perform actions such as credit checks, document verification, search result enrichment, or accessing third‑party databases—without embedding that integration logic directly into your app.

See the [External tools overview](tools/intro.md) to choose an approach, learn how to set up a [custom MCP server](tools/mcp-connectors.md), or browse [prebuilt connectors](tools/prebuilt-connectors.md).

## Next steps

To learn how to create an AI agent in ODC Studio, see [Create an AI agent in ODC Studio](create-agent.md). For related topics:

* [Build AI-powered apps](intro.md)
* [External tools overview](tools/intro.md)
* [Prebuilt connectors](tools/prebuilt-connectors.md)
* [Custom MCP servers](tools/mcp-connectors.md)
