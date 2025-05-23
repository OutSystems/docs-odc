---
summary: Add AI models in OutSystems Developer Cloud (ODC) for mobile and reactive web apps.
tags: ai models, mobile apps, reactive web apps
guid: af45db6e-ac0f-4ab9-8e4a-4ba8fd559812
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=7348-589&p=f&t=Yqn50gOLIwN2Vqkb-0
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - understand
  - apply
audience:
  - mobile developers
  - frontend developers
topic:
---
# Adding AI models

ODC lets you connect your OutSystems apps to external large language models, often called LLMs, from various providers or use pre-configured ODC trial models for experimentation. This enables you to integrate AI capabilities directly into your app.

## Supported providers and ODC trial models

Using the [ODC API contract](ai-models.md#custom-model-connections), you can add connections to your provisioned models through **Custom connections**. This allows you to integrate with LLMs from various providers or your own private models that are not natively supported by ODC. For natively supported providers like Azure OpenAI and Amazon Bedrock, ODC offers specific integration methods that do not require implementing the generic ODC API contract. ODC currently supports Amazon Bedrock models that are compatible with the [Bedrock Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html).

Alternatively, for quick testing and exploration in the development stage, ODC provides ready-to-use trial models. These include GPT-4o via Azure OpenAI and Claude 3.7 Sonnet via Amazon Bedrock. These trial models allow only 100 calls per tenant and serve for initial evaluation before you set up your own configured connection.

## Prerequisites

Before adding a configured connection to your model provider, such as Azure OpenAI, Amazon Bedrock, or Custom:

* Set up, deploy, and ensure the external AI service is accessible on the provider's platform, such as Azure or AWS. Note that an administrator or DevOps team typically performs this external setup, which is not covered here.
* Obtain the necessary access credentials and details the specific provider requires, such as API keys, endpoint URLs, deployment names, model IDs, and access or secret keys. Refer to the [AI model parameters](#add-ai-models) section below for details.
* Ensure you have the required permissions within ODC to manage AI models. Note that managing AI models utilizes the same permissions as managing connections within the ODC Portal.

These prerequisites don't apply when adding an ODC trial model.

## Add AI models { #add-ai-models }

Follow these steps to add an AI model connection or an ODC trial model in the ODC Portal:

1. Navigate to the **INTEGRATE** > **AI models** section.

1. Click **Add AI model**. The **Add AI model** dialog opens.

1. Choose the type of model you want to add:
    * **Own configured model**: Select the provider, such as Amazon Bedrock, Azure OpenAI, or a custom connection.
    * **ODC trial model**: Select the desired trial model, for example, GPT or Claude Sonnet.
    
      ![Screenshot of the 'Add AI model' dialog in the ODC Portal showing options to select a provider or a trial model.](images/add-ai-model-pl.png "Add AI Model Dialog in ODC Portal")

1. Click **Confirm**.
    * **For your own configured model**, proceed to configure the connection details.
    * **For the ODC trial model**, ODC adds the trial model directly to your list, completing the setup.

1. On the model configuration page that appears, enter a unique 
**Name** and an optional **Description** for this AI model connection.

1. In the **Endpoints** section, click **+ Add** to open the **Add endpoint** dialog.
  ![Screenshot of the 'Add endpoint' button in the ODC Portal under the Configuration section.](images/add-endpoints-pl.png "Add Endpoint Button in ODC Portal")

1. Enter the required endpoint details for the provider you selected. Set the **Priority** for this endpoint. For details about the fields, refer to the [AI model parameters](#add-ai-models-add-ai-models-) section. Click **Save**.
  ![Screenshot of the 'Add endpoint' dialog in the ODC Portal showing fields for Access key, Secret key, and Priority.](images/set-priority-endpoint-configuration-pl.png "Set Priority in Endpoint Configuration")

1. Optionally, add more endpoints if you have them available for different stages, such as development and production. More endpoints also enable load balancing. Ensure all endpoints under one connection use the same underlying AI model and version.

1. Optionally, in the **Usage limit** section, set a daily token limit to control the model consumption.

1. If you added multiple endpoints, adjust their priority order on the main model configuration page using the edit icon next to each endpoint.

1. Click **Save** to confirm.

After you complete the steps, ODC redirects you to the main AI models page. You can now use the newly added model connection or ODC trial model within your apps in ODC Studio.

## AI model parameters { #ai-model-parameters }

Use the following parameters when configuring endpoints for Azure OpenAI, Amazon Bedrock models, and Custom AI models in the ODC Portal.

### Azure OpenAI parameters

Use the following parameters when configuring Azure OpenAI model endpoints.

| Parameter | Description | Notes |
| :---- | :---- | :---- |
| Deployment name | The name of your model deployment within the Azure OpenAI service. | Obtain from the Azure portal. |
| API key | The authentication key required to access the Azure OpenAI service. | Obtain from the Azure portal. Treat this securely. |
| URL | The endpoint URL for the Azure OpenAI service. | Obtain from the Azure portal. |
| Priority | Determines the order of endpoints, with one being the highest. Lower-priority endpoints act as fallbacks. | You can adjust priorities if multiple endpoints exist. |

### Amazon Bedrock parameters

Use these parameters when configuring Amazon Bedrock model endpoints.

| Parameter | Description | Notes |
| :---- | :---- | :---- |
| Name | User-defined, identifiable name for the endpoint instance. | Differentiates between multiple endpoints for the same Bedrock model connection. |
| Model ID | The unique identifier for the specific Amazon Bedrock foundation model or its Amazon Resource Name (ARN). | For example, anthropic.claude-3-sonnet-20240229-v1:0. Refer to [AWS documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) for model IDs. |
| Access key | The authentication access key ID for your AWS IAM user or role with permissions for Bedrock. | Obtain from the AWS console or security credentials. |
| Secret key | The secret access key associated with the Access key for AWS authentication. | Obtain from the AWS console or security credentials. Treat this securely. |
| URL | The Invoke URL for Amazon Bedrock. | Ensure the AWS region matches your model's region; the URL typically follows the format runtime.bedrock.\[aws-region\].amazonaws.com. |
| Priority | Determines the order of endpoints, with one being the highest. Lower-priority endpoints act as fallbacks. | ODC assigns Priority 1 to the first endpoint by default. You can adjust priorities if multiple endpoints exist. |

### Custom AI model parameters

Use these parameters when configuring custom connection AI models and their endpoints in the ODC Portal.

| Parameter   | Description | Notes |
| :---------- | :-------------------------------------- | :----------------------------------- |
| Name        | A unique, user-defined name for this specific AI model connection in ODC. Set on the main connection page.                      | Helps you identify this connection later (e.g., "My Custom Text Generator"). |
| Description | An optional description for the AI model connection. Set on the main connection page. | Useful for adding context about the connection purpose.                                                                                                                                          |
| Model ID    | The identifier for the specific custom model being used. | |
| URL         | The endpoint URL for the custom AI service or model API.| Enter the base URL provided by the custom model service.                                                                                                                                           |
| Priority    | Determines the order endpoints are used where one is the highest. Lower-priority endpoints act as fallbacks. | The first endpoint added will be assigned Priority 1 by default. You can adjust priorities if multiple endpoints exist.                                                                             |
| Headers     | A set of HTTP headers required by the custom API (authentication, content type, etc.).  | For the endpoint dialog to add necessary key-value pairs (for example, `Content-Type`, `Authorization`). These are specific to the API you are connecting to.                         |

## Next steps

[Integrating AI models and search services](integrate-ai-models-logic-rag.md)
