---
summary: This article guides on integrating the Azure OpenAI model into the AI Agent Builder app within the OutSystems Developer Cloud (ODC) platform.
tags:
locale: en-us
guid: db6b7e45-96d2-4f0b-9723-b5a59c57fe60
app_type: mobile apps, reactive web apps
platform-version: odc
figma: 
---
# Add Azure OpenAI model to AI Agent Builder app

To use Azure OpenAI models for your agent, you must add the Azure OpenAI models to the AI Agent Builder. To ensure high-availability of your agent and distribute the load, you can add one or more deployments of the same model as endpoints and prioritize them.

OutSystems recommends that each model deployment you add in the AI Agent Builder as an endpoint corresponds to the same AI model and version. For example, if you use the GPT-4o model, all deployments created in Azure should only be for GPT-4o.

This article explains how to add Azure OpenAI model to AI Agent Builder. It is intended for administrators and DevOps engineers who are responsible for setting up the AI Agent Builder.

<div class="info" markdown="1">

You need only a single Azure subscription to handle multiple deployments of a model. This means you can create and manage multiple deployments for a model within the same account. This provides greater flexibility than Amazon Bedrock, where multiple AWS accounts are required.

</div>

## Prerequisites

Before you add an Azure OpenAI model to the AI Agent Builder app, ensure that you:

* Configure and deploy [Azure OpenAI service](configure-azure-model.md).

* Obtain the following from the Azure portal:
    
    * OpenAI registration keys.

    * Endpoint URL

    * Deployment name

* Gain access to the AI Agent Builder app with **Configurator** role in ODC portal.

## Add Azure OpenAI model

To add the Azure OpenAI model, follow these steps:

1. Log into the AI Agent Builder app.

<div class="info" markdown="1">

The first time you log into the AI Agent Builder, OutSystems recommends to add a model. You can follow the instructions provided in the pop-up message. To add additional models, follow these steps:

</div>

2. Go to the **Configurations** tab. A list of all your configured AI models and data sources display.

1. Click **Add AI model** and choose the provider **Azure Open AI**.

1. Enter the following details:

    * **Name** - An identifiable name for the AI model.

    * **ID** -  Identifier for the AI model, Auto-filled with the **Name** field without blank spaces. You can also edit the field.

    * **Description** - (Optional) Description of the AI model.

1. Click **Add endpoint** The Add Endpoint pop-up page displays.

1. Enter the following details for the endpoint you want to add. 

   * **Name**- An identifiable name for the AI model.

   * **Endpoint URL**- Azure OpenAI service endpoint URL retrieved from the Azure portal.

   * **Deployment name**-  Azure OpenAI service deployment name retrieved from the Azure portal.

    * **API key**-  Azure OpenAI API key retrieved from the Azure portal.

   * **Status**- (Optional) The current state of the AI model. 

   * **Priority**- The priority level of the endpoint determines the order in which the agent utilizes them. A priority 1 endpoint is used first. If it experiences an outage, the priority 2 endpoint takes over to prevent downtime. This process continues with priority 3, and so on, ensuring continuous operation.
    The first endpoint you add is always assigned the first **priority**.

1. Click **Add endpoint** to add the endpoint.

1. (Optional) To add more endpoint, click **Add endpoint** in the Model details page and enter the details for the endpoint..

<div class="info" markdown="1">

 Ensure that all endpoints you add belong to the same model and version.

 </div>

Once you have added all the endpoints, a list of all endpoints is displayed under **Model endpoints** in the Model details page. To adjust the priority level order, click the edit icon, navigate to the **Priority** dropdown, and choose the priority level.

9. Click **Add AI model**.

Once you've added the model, you are redirected to the **Configurations** page. A confirmation message is displayed confirming that the AI model has been added successfully. You can also view the newly added model on the **Configurations** page. If adding the model fails, an error message is displayed.

You can **edit** the fields of the model and **delete** the model from the AI Agent Builder app in case you no longer need the AI model or have changed providers.

## Next steps

* [Create agent](../create-agent.md)

* [Configure data source](../configure-data-source/add-azure-data-source-to-aibuilder.md)
