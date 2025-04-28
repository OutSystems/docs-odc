---
summary: Build AI-powered mobile and reactive web apps using OutSystems Developer Cloud (ODC).
tags: ai-powered apps, mobile apps, reactive web apps
guid: f217cece-7042-4055-811a-948ed6244007
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - odc portal
  - forge
coverage-type:
  - understand
audience:
  - mobile developers
  - frontend developers
---

# Build AI-powered apps

Automate business processes, enhance productivity, and enable new user experience patterns by integrating AI into your business using OutSystems Developer Cloud (ODC). ODC provides a platform that combines low-code development with AI integration features, simplifying the creation of AI-enhanced solutions. Incorporating AI into your ODC apps and workflows enables capabilities such as:

* Respond dynamically to changing conditions in real time.  
* Generate personalized and relevant content on demand.  
* Inject AI-driven insights and decision-making into business workflows.  
* Facilitate interactions through natural language.

ODC offers built-in tools to help you incorporate these AI functionalities. The platform enables you to use large language models (LLMs). You can connect these models with your organizational data through integrated search services, a process known as retrieval-augmented generation (RAG). You can also configure AI-driven behaviors and manage the overall process. This lets you add intelligence to your app logic and user interfaces.

## Choosing your Al tool

ODC provides access to AI models in the ODC Portal and the [AI Agent Builder via Forge](../use-ai/intro.md). Both enhance apps with AI capabilities but differ in their range of functions and ideal use cases. Understanding these differences helps you select the appropriate tool for your needs.

<div class="info" markdown="1">

OutSystems recommends using AI models in Portal whenever they fit your use cases. This article guides you in evaluating your use cases to help you decide when to use AI models in Portal.

</div>

### Al models

AI models are available in the ODC Portal. They are best suited for integrating AI capabilities into **pre-defined processes** or app logic. In this approach, your app orchestrates the steps, fetches any necessary data, which can be real-time data, and passes it as context to the model. The model then performs tasks like analysis or generation based on the provided context, supporting a relatively **limited or pre-defined set of requests**.

Use cases suited for this approach include: 

* Analyzing historical sales data or survey results **provided as context** to identify trends and insights.
* Generating articles, brainstorming ideas, or creating marketing content based on **provided context**.  
* Providing personalized recommendations using historical user data **supplied by the app**.  
* Summarizing key points from real-time meeting transcripts **provided by the app**.  
* Answering user queries based on product documentation **and** current user status information **fetched by the app and passed as context**.

### Al Agent Builder

The Al Agent Builder, available to install via [Forge](https://www.outsystems.com/forge/list), offers extended capabilities, including real-time data access and agent-based automation for complex tasks.

Use cases include:

* Providing real-time updates, such as current weather forecasts or stock market trends, retrieved via [external calls](../../integration-with-systems/intro.md).  
* Automating booking processes that require interaction with external [APIs](../../integration-with-systems/consume_rest/intro.md), like scheduling flights and hotel reservations.
* Enabling chatbots to handle complete transactions, such as processing orders and managing refunds, involving multiple steps and [external system calls](../../integration-with-systems/intro.md).

Both Al models in the ODC Portal and the Al Agent Builder enable you to:

* Make Al integration more accessible, allowing the developers to implement many common Al tasks independently.
* Reduce costs associated with upskilling teams specifically for complex Al integrations.
* Control how your organization uses Al to help ensure security and compliance.

Al Agent Builder additionally enables you to:

* Inspire teams to innovate and increase automation by demonstrating how quickly Al agents can be integrated.
* Create reusable agents that you can apply across multiple use cases.
* Build user interfaces (Uls) that connect directly to Al-powered widgets and the logic within your app.

## Capability comparison

The following table compares which tool offers the specific Al needed for your use case.

| Capability or Use Case | AI models in the ODC Portal | AI Agent Builder |
| :---- | :---- | :---- |
| AI-driven text generation | Yes | Yes |
| Static data analysis | Yes | Yes |
| Autonomous multi-system data fetching during execution | No | Yes |
| Simple pre-defined workflows or tasks | Yes | Yes |
| Multi-step complex/dynamic workflows (agent-driven) | No | Yes |
| Transactional interactions | No | Yes |
| Autonomous decision-making (external actions) | No | Yes |
| Content generation from the provided context | Yes | Yes |
| Classification/analysis of static datasets | Yes | Yes |

ODC facilitates the development and management of intelligent apps. This document details AI integration features. ODC also provides a dedicated **app analytics dashboard** for monitoring the performance, usage, and errors of your deployed apps. This dashboard offers key metrics such as **health score, top apps by usage, request volume and rate, error counts and rates, and response times**. For detailed insights into user engagement, feature utilization, performance trends across different geographies and browsers, and specific element and AI model metrics, refer to the [Monitor app analytics in the ODC Portal](../../monitor-and-troubleshoot/app-health.md).

## Next steps

* [AI models and search services in ODC](ai-models.md)
* [Adding AI models](add-ai-models.md)
* [Adding search services](add-ai-search-services.md)
* [Integrating AI models and search services](integrate-ai-models-logic-rag.md)
