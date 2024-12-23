---
helpids: 30503
summary: OutSystems Developer Cloud (ODC) integrates AI models from Azure OpenAI and Amazon Bedrock to enhance AI Agent Builder capabilities.
tags: ai integration, azure openai, amazon bedrock, ai high availability, large-language-model integration
locale: en-us
guid: 81dc39d3-cb37-4757-88fe-eec0fbfc80ea
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - platform administrators
  - full stack developers
outsystems-tools:
  - ai agent builder
coverage-type:
  - apply
  - understand
---

# Configure your AI models

The AI Agent Builder uses AI models from [Azure OpenAI](https://azure.microsoft.com/en-in/products/ai-services/openai-service) and [Amazon Bedrock](https://aws.amazon.com/bedrock/). You can also integrate any Large-Language-Model (LLM) model of your preference to create agents and build generative AI applications. However, you must build a custom integration for the LLM you want to use.

This section contains information intended for administrators and dev-ops engineers with a good working knowledge of configuring AI services.

To configure your AI models and use them in the AI Agent Builder you must: 

1. Set up your AI service in [Azure](configure-aws-model.md) or [AWS](configure-aws-model.md), depending on the model you choose.

1. Get your registration keys and endpoint access for your model from the console.

1. Add your access keys and end-point access information to the AI Agent Builder.

1. [Create your agents](../create-agent.md) in the AI Agent Builder. 

## High availability of AI agents

High availability for an AI agent involves designing and implementing measures to ensure that the AI system remains operational despite any outages. OutSystems supports high availability for its AI agents by allowing you to configure multiple deployments or resources for an AI model and distribute the load between them. This approach ensures that the  system is accessible with minimal downtime, preventing failures due to outages at the upstream provider (AWS or Azure) or exceeding the tokens-per-minute (TPM)  limits.

## Related resources

* [Set up Azure OpenAI Service](configure-azure-model.md)

* [Add Azure OpenAI model to AI Agent Builder app](add-azure-model-to-aibuilder.md)

* [Set up Amazon Bedrock foundation AI models](configure-aws-model.md)

* [Add Amazon Bedrock AI model in the AI Agent Builder app](add-aws-model-to-aibuilder.md)

* [Configure AI model API contract](aiab-custom-model-api-contract.md)
