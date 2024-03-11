---
summary: This article explains the setup process for Azure OpenAI Service and its integration with AI Agent Builder.
tags:
locale: en-us
guid: e577bb40-f2ee-468a-8ebe-ccad45fe2705
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---
# Set up Azure OpenAI Service

The [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/) provides access to OpenAI’s models, such as GPT-4, GPT-4 Turbo with vision, and GPT-3.5 Turbo, which you can customize to your specific needs for a variety of use cases. 

This article explains how to configure and deploy Azure OpenAI service and retrieve the OpenAI registration keys and endpoint. It is intended for administrators and DevOps engineers with good working knowledge of configuring AI services in Azure OpenAI.

Once you have the registration keys and the endpoint, you can configure the OpenAI models in the AI Agent Builder. 

## Prerequisites

Before you setup the Azure OpenAI Service, ensure that you have:

* An active Azure account subscription. You can [sign up](https://azure.microsoft.com/en-us/free/) for an Azure account if you don’t already have one.
* Access to the AI Agent Builder app.

## Configure and deploy Azure OpenAI service.

To configure and deploy the Azure OpenAI service, follow these steps:

1. Log into the Azure portal and sign in with your subscription username and password.

1. Search for **OpenAI** in the portal and select the OpenAI service.

1. Create a new OpenAI resource. 

For more information, refer to [Create and Deploy an Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal). 

Once the deployment is complete, you can retrieve the two OpenAI registration keys and the endpoint. For more information, refer to [Retrieve key and endpoint](https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart?tabs=command-line%2Cpython&pivots=programming-language-python). 

You can use the keys and the endpoint in the AI Agent Builder app to interact with the OpenAI model.

## 	Next steps

[Add Azure OpenAI model in AI Agent Builder app](./add-azure-model-to-aibuilder.md)
[Create agent](../create-agent.md)
