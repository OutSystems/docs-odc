---
summary: This article guides on integrating Amazon Bedrock AI models into the AI Agent Builder app using OutSystems Developer Cloud (ODC).
tags:
locale: en-us
guid: e871f14b-e322-4cfc-a1b8-bc361fba8dc5
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---
# Add Amazon Bedrock AI model to the AI Agent Builder

To use Amazon Bedrock AI models, you must add the Bedrock AI models to the AI Agent Builder. To ensure high availability of the agent and distribute the load, you can add one or more Bedrock resources of the same model as endpoints and prioritize them for use.

OutSystems recommends that each model resource you add in the AI Agent Builder as an endpoint corresponds to the same AI model and version. For example, if you use the Anthropic Claude Haiku model, all resources created in AWS accounts should only be for Anthropic Claude Haiku model.

<div class="info" markdown="1">

You must create multiple accounts in AWS with separate credentials to create multiple resources for a model.

</div>

This article explains how to add the Amazon Bedrock AI model to AI Agent Builder. It is intended for administrators and DevOps engineers who are responsible for setting up the AI Agent Builder.

## Prerequisites

Before you add an Amazon Bedrock AI model in the AI Agent Builder, ensure that you:

* [Set up Amazon Bedrock foundation models](configure-aws-model.md).

* Obtain the secret key and access key from the AWS console.

* Gain access to the AI Agent Builder app with the **Configurator** role assigned in the ODC portal.

## Add Amazon Bedrock AI model

To add the Amazon Bedrock model to the AI Agent Builder, follow these steps:

1. Log into the AI Agent Builder app.

<div class="info" markdown="1">

The first time you log into the AI Agent Builder, OutSystems recommends to add a model. You can follow the instructions provided in the pop-up message. To add additional models, follow these steps:

</div>

2. Go to the Configurations tab. A list of all configured AI models and data sources is displayed.

1. Click **Add AI model** and select **Amazon Bedrock**. The Add AI model page displays.

1. Enter the following details:

    * **Name** - An identifiable name for the AI model.

    * **ID** -  Identifier for the AI model, Auto-filled with the **Name** field without blank spaces. You can also edit the field.

    * **Description** - (Optional) Description of the AI model.

1. Click **Add endpoint** to enter the model resource details.

1. Enter the following details for the endpoint: 

   * **Name**- An identifiable name for the AI model.

   * **Endpoint URL**- Amazon Bedrock Service endpoint retrieved from the AWS console. 

   * **Access key**- The authentication key required to access the endpoint.

   * **Secret key**- The secret key of the authentication credential.

   * **Status**- (Optional) The current state of the endpoint. 

   * **Priority**- The priority level of the endpoint determines the order in which the agent utilizes them. The priority 1 endpoint is used first. If it experiences an outage, the priority 2 endpoint takes over to prevent downtime. This process continues with priority 3, and so on, ensuring continuous operation

    For more information about managing access keys, refer to [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).

<div class="info" markdown="1">

The first endpoint you add is always assigned the first priority.  

</div>

7. Click **Add endpoint** to add the endpoint.

1. (Optional) To add more endpoint, click **Add endpoint** in the Model details page and enter the details for the endpoint..

<div class="info" markdown="1">

 Ensure that all endpoints you add belong to the same model and version.

 </div>

Once you have added all the endpoints, a list of all endpoints is displayed under **Model endpoints** in the Model details page. To adjust the priority level order, click the edit icon, navigate to the **Priority** dropdown, and choose the priority level.

9. Click **Add AI model**.

Once you've added the model, you are redirected to the **Configurations** page. A confirmation message confirms that the AI model has been added successfully. You can also view the newly added model on the **Configurations** page. If adding the model fails, an error message is displayed.

You can **edit** the fields of the model and **delete** the model from the AI Agent Builder app if you no longer need the AI model or have changed providers. 

## Next steps

* [Create agent](../create-agent.md)

* [Configure data source](../configure-data-source/configure-aws-data-source.md)
