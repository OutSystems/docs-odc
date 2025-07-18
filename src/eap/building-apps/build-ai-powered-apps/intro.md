---
summary: Build AI-powered mobile and reactive web apps using OutSystems Developer Cloud (ODC).
tags: ai-powered apps,mobile apps,reactive web apps
guid: f217cece-7042-4055-811a-948ed6244007
locale: en-us
app_type: mobile apps,reactive web apps
platform-version: odc
figma: 
topic:
  - machine-learning
  - chatbots
  - sentiment-analisys
  - outsystems-overview
  - creating-apps
outsystems-tools:
  - odc portal
  - forge
coverage-type:
  - understand
audience:
  - mobile developers
  - frontend developers
helpids: 
---

# Build AI-powered apps

<div class="info" markdown="1">

Native ODC agent apps are only available to Early Access Program (EAP) customers.

</div>

Automate business processes, enhance productivity, and enable new user experience patterns by integrating AI into your business using OutSystems Developer Cloud (ODC). ODC provides a platform that combines low-code development with AI integration features, simplifying the creation of AI-enhanced solutions. Incorporating AI into your ODC apps and workflows enables capabilities such as:

* Respond dynamically to changing conditions in real time.  
* Generate personalized and relevant content on demand.  
* Inject AI-driven insights and decision-making into business workflows.  
* Facilitate interactions through natural language.
* Orchestrate complex tasks and workflows autonomously.


ODC offers built-in tools to help you incorporate these AI functionalities. The platform enables you to use large language models (LLMs) through AI models and AI agents. You can connect these models with your organizational data through integrated search services, a process known as retrieval-augmented generation (RAG). You can also configure AI-driven behaviors and manage the overall process. This lets you add intelligence to your app logic and user interfaces.

## Choosing your AI tool

ODC provides access to AI models in the ODC Portal through native support for AI models and agents and the [AI Agent Builder via Forge](../use-ai/intro.md). Both enhance apps with AI capabilities but differ in their range of functions and ideal use cases. Understanding these differences helps you select the appropriate tool for your needs.

<div class="info" markdown="1">

OutSystems recommends using native support for AI models and agents whenever they fit your use cases. This article guides you in evaluating your use cases to help you decide when to use native support for AI models and agents versus the AI Agent Builder.

</div>

### AI models

AI models are available in the ODC Portal. They are best suited for integrating AI capabilities into **pre-defined processes** or app logic. In this approach, your app orchestrates the steps, fetches any necessary data, which can be real-time data, and passes it as context to the model. The model then performs tasks like analysis or generation based on the provided context, supporting a relatively **limited or pre-defined set of requests**.

Use cases suited for this approach include: 

* Analyzing historical sales data or survey results **provided as context** to identify trends and insights.
* Generating articles, brainstorming ideas, or creating marketing content based on **provided context**.  
* Providing personalized recommendations using historical user data **supplied by the app**.  
* Summarizing key points from real-time meeting transcripts **provided by the app**.  
* Answering user queries based on product documentation **and** current user status information **fetched by the app and passed as context**.

### AI agents 

AI agents handle more complex and autonomous tasks directly within your low-code environment. They can independently manage multi-step workflows, interact with various systems and data sources, and make decisions based on their defined objectives and the information they gather.

Use cases suited for AI agents include:

* Intelligent automation of customer service inquiries, autonomously accessing knowledge bases, processing information, and resolving issues.  
* Dynamic inventory monitoring and automated low-stock alerts.  
* Automated data aggregation and report generation from internal data sources.
* Automatic intake of supplier quotes by processing complex supplier quotes for clinical studies, extracting data, populating a budget workbook, comparing against rate sheets, and providing feedback/error reporting.  
* Accelerate equity research report creation in the financial industry by collecting and ingesting data from various sources, reducing report writing time.

### AI Agent Builder

The AI Agent Builder, available to install via [Forge](https://www.outsystems.com/forge/list), offers extended capabilities, including real-time data access and agent-based automation for complex tasks.

Use cases include:

* Providing real-time updates, such as current weather forecasts or stock market trends, retrieved via [external calls](../../integration-with-systems/intro.md).  
* Automating booking processes that require interaction with external [APIs](../../integration-with-systems/consume_rest/intro.md), like scheduling flights and hotel reservations.
* Enabling chatbots to handle complete transactions, such as processing orders and managing refunds, involving multiple steps and [external system calls](../../integration-with-systems/intro.md).

Both AI models in the ODC Portal and the AI Agent Builder enable you to:

* Make AI integration more accessible, allowing the developers to implement many common AI tasks independently.
* Reduce costs associated with upskilling teams specifically for complex AI integrations.
* Control how your organization uses AI to help ensure security and compliance.

AI Agent Builder additionally enables you to:

* Demonstrate how quickly AI agents can be integrated to inspire teams to innovate and increase automation.
* Create reusable agents that you can apply across multiple use cases.
* Build user interfaces (Uls) that connect directly to AI-powered widgets and the logic within your app.

## Capability comparison

The following table compares which tool offers the specific AI needed for your use case.

| Capability or Use Case | AI models in the ODC Portal | AI Agent Builder |
| :---- | :---- | :---- |
| AI-driven text generation | Yes | Yes |
| Static data analysis | Yes | Yes |
| Autonomous multi-system data fetching during execution | No | Yes |
| Simple pre-defined workflows or tasks | Yes | Yes |
| Multi-step complex/dynamic workflows (agent-driven) | Yes | Yes |
| Transactional interactions | No | Yes |
| Autonomous decision-making (external actions) | No | Yes |
| Content generation from the provided context | Yes | Yes |
| Classification/analysis of static datasets | Yes | Yes |

ODC facilitates the development and management of intelligent apps. This document details AI integration features. ODC also provides a dedicated **app analytics dashboard** to monitor the performance, usage, and errors of your deployed apps. This dashboard offers key metrics such as **health score, top apps by usage, request volume and rate, error counts and rates, and response times**. It provides a comprehensive overview of app performance. For detailed insights into user engagement, feature utilization, and performance trends across different geographies and browsers, refer to the [Monitor app analytics in the ODC Portal](../../monitor-and-troubleshoot/app-health.md). It also provides specific element and AI model metrics.

## Next steps

* [AI models and search services in ODC](ai-models.md)
* [Adding AI models](add-ai-models.md)
* [Adding search services](add-ai-search-services.md)
* [Integrating AI models and search services](integrate-ai-models-logic-rag.md)
* [Agentic apps in ODC](agentic-apps.md)
