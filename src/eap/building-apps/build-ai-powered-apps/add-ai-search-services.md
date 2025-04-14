---
guid: 8a85a3e3-87e6-490f-b302-adce099b9821
locale: en-us
summary: Add AI search services and custom search options with best practices for RAG using OutSystems Developer Cloud (ODC) platform.
figma:
coverage-type:
  - apply
  - understand
topic:
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - infrastructure managers
  - platform administrators
  - tech leads
tags: ai search services, custom search service, rag best practices, odc portal
outsystems-tools:
  - odc portal
helpids:
---

# Adding search services

This document explains adding search services like Azure AI Search, Amazon Kendra, or custom connections with your ODC environment to power **Retrieval Augmented Generation (RAG)** for generative AI search experiences. This integration lets your AI models to access and ground their responses in your organization's specific knowledge base. This guide is intended for developers familiar with the basic concepts of ODC and who want to enhance their AI apps with external knowledge.

## Prerequisites

Before adding a configured connection to your search service provider:

* Ensure the search service is set up, deployed, and accessible on its respective platform (Azure or AWS).
* Obtain the necessary access credentials and details required by the specific provider. 
* Ensure you have the necessary permissions within the ODC Portal to create and manage connections.

## Add a search service

Refer to [Create connections to external data sources](../../integration-with-systems/external-databases/create-connection-external-data.md#create-a-new-connection) to add your search service in the ODC Portal.

## Custom search service

Beyond native support for Azure AI Search and Amazon Kendra, ODC allows you to connect to other search services, such as those from different providers or your private search service. This is achieved using the **Custom AI search** option. To use this option, you must provide an intermediary web service that bridges ODC and your target LLM. This service must implement the OutSystems API contract.

When building your connector service, you implement a supported authentication scheme and ensure its endpoint is accessible to ODC, potentially using a private gateway for non-public endpoints. The connector must process requests and format responses, including handling standard parameters like messages and temperature, according to the OutSystems API contract details. Your service should also return standard HTTP status codes for errors. Once your connector service is deployed and accessible, you add it to the ODC Portal by selecting **Custom AI search** as the provider type during the **Select a provider** process and entering your connector's URL and authentication details.

For more information, download and inspect the [Swagger file](resources/swagger-custom-connection.json). Note that property names should use camelCase.

## Key considerations for RAG content preparation

Before integrating a search service, ensure your content is prepared for optimal RAG performance. This preparation impacts retrieval quality and relevance, influencing the accuracy of LLM-generated answers. Consider these guidelines:

* **Supported file formats**: Utilize Markdown, plain text, and PDF files as source documents for your knowledge base. Implement OCR to make images within PDFs searchable, ensuring efficient retrieval.
* **Maximum file size**: Adhere to a maximum file size of 16 MB per document to prevent processing bottlenecks.
* **Prioritize smaller files**: Use files that are smaller, in both size and content length where possible, to enhance retrieval speed and precision.
* **Chunking strategies**: Employ chunking strategies to divide large documents into manageable segments, aiming for 2-3 pages per chunk. This is vital for RAG, letting the model retrieve relevant sections instead of processing an entire document.
* **Token limits**: Avoid large files or chunks, as the retrieved context could exceed the token limits of language models and RAG could fail.
* **Relevance and contextual density**: Ensure that smaller chunks contain dense and focused contextual information so LLM can answer accurately based on the retrieved content.
