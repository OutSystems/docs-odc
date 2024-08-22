---
helpids: 30553
summary:  In this article you will learn how to add custom AI model to the AI Agent Builder app.
tags: 
guid: 2fdeaba8-6979-4a03-aa9c-50422431e38a
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?m=auto&node-id=5302-572&t=fjpPZauR2aOAen2p-1
---

# Add a custom AI model 

You can add a custom AI model to the AI Agent Builder to support any Large Language Model (LLM). A custom model allows you to fine-tune and tailor the model's behavior. This customization can enhance performance and improve accuracy. To integrate a custom AI model, ensure you:

- Build an AI model connector in compliance with the API contract established by OutSystems.
- Gain access to the AI Agent Builder app with the Configurator role assigned in the ODC portal.

You can[ integrate custom data sources](../use-ai/configure-data-source/add-custom-data-source.md) into AI Agent Builder to optimize your AI model.

## Add a custom AI Model

To add a custom AI model, follow these steps:

1. Log into the AI Agent Builder app.
1. Go to the **Configurations** tab to display a list of all configured AI models and data sources.
1. Click **Add AI Model**.
1. Select **Custom connection**, and click **Confirm**.
  ![Screenshot showing the AI Agent Builder app with a dialog box to choose an AI provider. Options include Azure OpenAI, Amazon Bedrock, and Custom connection.](images/add-custom-ai-model.png "Screenshot of adding a custom AI model in AI Agent Builder")
1. Enter the AI model details. To learn more about parameters, refer to [AI model parameters.](#ai-model-parameters)
1. Click **Add endpoint**.
1. Enter the endpoint details. To learn more about parameters, refer to [AI model parameters.](#ai-model-parameters)
1. Click **Add header**.
1. Enter the authentication headers required for your custom-built AI model connector. To learn more about parameters, refer to [AI model parameters.](#ai-model-parameters)

You can add more endpoints and adjust their priority level order. You can edit the fields of the model and delete the model from the AI Agent Builder app if you no longer need the AI model or have changed providers.

## Build an AI model connector

To build an AI model connector, follow these steps:

1. Build the AI model connector for your LLM service according to the OutSystems API contract.
  * Set up the endpoints to be accessible via HTTP(S). You can either make the endpoint publicly discoverable or use a Private Gateway. To learn more, refer to [Configure a private gateway](../../manage-platform-app-lifecycle/private-gateway.md).
  * Ensure that AI model endpoints are synchronous, as the AI Agent Builder does not support asynchronous requests (streaming).
  * Implement authentication schemes for your REST endpoints.
1. Authenticate and integrate your AI model connector with the AI Agent Builder.

# Reference

## AI model parameters

The following are the parameters to add a custom AI model,

| Parameter name| Description | Notes |
|--|----|--|
| Name(AI model)  | An identifiable name for the AI model. | |
| ID              | Identifier for the AI model, Auto-filled with the Name field without blank spaces. You can also edit the field. |  |
| Description     |  Description of the AI model. | Optional |
| Name (endpoint) | An identifiable name for the endpoint. |  |
| Endpoint URL    | URL of the custom-built AI model connector. | |
| Status          | The current state of the AI model.  | Optional |
| Priority        | The priority level of the endpoint determines the order in which the agent utilizes it. For example, A priority 1 endpoint is used first. If it experiences an outage, the priority 2 endpoint takes over to prevent downtime.  | The first endpoint you add is always assigned the first priority. |
| Name (header)   | The name of the header  | |
| Value           | The value of the header | |

## API contract

The API contract allows you to implement your logic and integrate it with AI Agent Builder. The API is a REST service available via the POST method. The property names must be in camelCase format.

The following tables detail the input and output parameters.


### HTTP Parameters

| Endpoint | Url to be called | Mandatory/Optional | Notes |
|--|----|-|---|
| HTTP Headers (List of key-value pairs) | Allows support sending HTTP headers required by service. For example, authentication headers `API-Key: xxxx` or `Access-Key: xxxx` <br/> `Access Secret: xxxx` | Optional  | You should define the Key, Value, and the number of headers. |


### Request parameters

| Name | JSON Type | Mandatory/Optional | Description  |
|--|---|--|----|
| messages | array of messages | Mandatory | List of chat messages. To learn more, refer to the [message](#message). |
| temperature | number | Optional | A float to pass upstream as generation temperature setting. |
| maxTokens   | number | Optional | The maximum number of tokens the model can generate. At this point, the generation is cut. |
| stop        | string | Optional | List of sequences that will trigger generation stop. |
| tools       | array of tools | Optional | Optional list of tools. To learn more, refer to the [tool](#tool). |
| extraBody   | string | Optional | Embed JSON strings into the upstream payload. This lets you pass parameters not supported by this service but supported by the upstream provider. |

For example, a sample request looks like:

```json
{
  "messages": [
    {
      "role": "",
      "content": "",
      "name": ""
    }
  ],
  "temperature": 0.1,
  "maxTokens": 1234,
  "stop": "",
  "tools": [
    {
      "type": "",
      "function": {
        "name": "",
        "description": "",
        "parameters": {
          "type": "",
          "properties": {
            "parameter1": {
              "type": "",
              "description": "",
              "enum": [
                ""
              ]
            },
            "parameter2": {
              "type": "",
              "description": "",
              "enum": [
                ""
              ]
            },
            "parameter3": {
              "type": "",
              "description": "",
              "enum": [
                ""
              ]
            },
            "parameter4": {
              "type": "",
              "description": "",
              "enum": [
                ""
              ]
            },
            "parameter5": {
              "type": "",
              "description": "",
              "enum": [
                ""
              ]
            },
            "parameter6": {
              "type": "",
              "description": "",
              "enum": [
                ""
              ]
            },
            "parameter7": {
              "type": "",
              "description": "",
              "enum": [
                ""
              ]
            },
            "parameter8": {
              "type": "",
              "description": "",
              "enum": [
                ""
              ]
            },
            "parameter9": {
              "type": "",
              "description": "",
              "enum": [
                ""
              ]
            },
            "parameter10": {
              "type": "",
              "description": "",
              "enum": [
                ""
              ]
            }
          },
          "required": [
            ""
          ]
        }
      }
    }
  ],
  "extraBody": ""
}

```

#### message

| Name    | JSON Type | Mandatory/Optional | Description |
| -- | --- | -- | ---- |
| role    | string "< user \| assistant \| function>" | Mandatory          | The role of the message's author.      |
| content | string                                    | Mandatory          | The message’s text content.            |
| name    | string                                    | Optional           | The name of the author of the message. |

#### tool

| Name | JSON Type | Mandatory/Optional | Description  |
| -- | --- | -- | ----- |
| type | string | Mandatory | The type of the tool. Currently, only [ request functions](#request-function) are supported. |
| function | function  | Mandatory | A list of functions the model may generate JSON inputs for. To learn more, refer to [request function](#request-function). |

#### request function

| Name        | JSON Type   | Mandatory/Optional | Description |
| -- | --- | -- | ---- |
| name        | string      | Mandatory          | The name of the function to be called. |
| description | string      | Optional           | A description of what the function does, used by the model to choose when and how to call the function. |
| parameters  | parameters  | Mandatory          | The parameters the function accepts. To learn more, refer to [parameters](#parameters). |

#### parameters

| Name       | JSON Type    | Mandatory/Optional | Description |
| -- | ---| -- | ---- |
| type       | string       | Mandatory          | The type of parameter. Currently, you can only send object as the value.|
| properties | priorities   | Mandatory          | The properties of the parameters. For more information, refer to [properties](#properties). |
| required   | string array | Optional           | The list of required parameters |

#### properties

| Name | JSON Type | Mandatory/Optional | Description |
| -- | ---| -- | ---- |
| parameter1  | parameter  | Optional | A function parameter. To learn more, refer to the [parameter](#parameter). |
| parameter2  | parameter  | Optional | A function parameter. To learn more, refer to the [parameter](#parameter). |
| parameter3  | parameter  | Optional | A function parameter. To learn more, refer to the [parameter](#parameter). |
| parameter4  | parameter  | Optional | A function parameter. To learn more, refer to the [parameter](#parameter). |
| parameter5  | parameter  | Optional | A function parameter. To learn more, refer to the [parameter](#parameter). |
| parameter6  | parameter  | Optional | A function parameter. To learn more, refer to the [parameter](#parameter). |
| parameter7  | parameter  | Optional | A function parameter. To learn more, refer to the [parameter](#parameter). |
| parameter8  | parameter  | Optional | A function parameter. To learn more, refer to the [parameter](#parameter). |
| parameter9  | parameter  | Optional | A function parameter. To learn more, refer to the [parameter](#parameter). |
| parameter10 | parameter  | Optional | A function parameter. To learn more, refer to the [parameter](#parameter). |


#### parameter

| Name        | JSON Type    | Mandatory/Optional | Description |
| -- | ---| -- | ---- |
| type        | string       | Mandatory          | The type of parameter. Currently, only string data type is supported. |
| description | string       | Mandatory          | Description of the parameter.                                         |
| enum        | string array | Optional           | The list of possible values for the parameter.                        |


### Response parameters

| Name      | JSON Type    | Mandatory/Optional | Description |
| -- | ---| -- | ---- |
| choices   | array of choice  | Mandatory | The contents of the message. To learn more, refer to the [choice](#choice).          |
| usage     | usage            | Optional  | Usage statistics for the model request. To learn more, refer to the [usage](#usage). |
| extraBody | string           | Optional  | Add more information to a JSON object. |
| error     | error            | Mandatory if the request fails. Optional otherwise. | The error details. To learn more, refer to the [error](#error) |

For example, a sample response looks like:

```json
{
  "choices": [
    {
      "content": "",
      "toolCalls": [
        {
          "id": "",
          "type": "",
          "function": {
            "name": "",
            "arguments": {
              "parameter1": "",
              "parameter2": "",
              "parameter3": "",
              "parameter4": "",
              "parameter5": "",
              "parameter6": "",
              "parameter7": "",
              "parameter8": "",
              "parameter9": "",
              "parameter10": ""
            }
          }
        }
      ]
    }
  ],
  "usage": {
    "completionTokens": 0.1,
    "promptTokens": 0.1,
    "totalTokens": 0.1
  },
  "extraBody": "",
  "error": {
    "message": "",
    "statusCode": 1234,
    "code": ""
  }
}

```

#### choice

| Name      | JSON Type    | Mandatory/Optional | Description |
| -- | ---| -- | ---- |
| content   | string    | Optional  | The contents of the message.   |
| toolCalls | toolCalls | Optional  | The tool calls generated by the model, such as function calls. For more information, refer to [toolCalls](#toolcalls). |

#### toolCalls

| Name      | JSON Type    | Mandatory/Optional | Description |
| -- | ---| -- | ---- |
| id       | string    | Mandatory | The ID of the tool call. |
| type     | string    | Mandatory | The type of the tool call, in this case function. |
| function | function  | Mandatory | The function that the model called. To learn more, refer to the [function](#response-function). |


#### response function

| Name      | JSON Type    | Mandatory/Optional | Description |
| -- | ---| -- | ---- |
| name      | string     | Mandatory | The name of the function to call. |
| arguments | arguments  | Mandatory | The arguments to call the function with, as generated by the model. To learn more, refer to [arguments](#arguments). |


#### arguments

| Name        | JSON Type | Mandatory/Optional | Description                  |
| -- | ---| -- | ---- |
| parameter1  | string    | Optional           | The value for the parameter. |
| parameter2  | string    | Optional           | The value for the parameter. |
| parameter3  | string    | Optional           | The value for the parameter. |
| parameter4  | string    | Optional           | The value for the parameter. |
| parameter5  | string    | Optional           | The value for the parameter. |
| parameter6  | string    | Optional           | The value for the parameter. |
| parameter7  | string    | Optional           | The value for the parameter. |
| parameter8  | string    | Optional           | The value for the parameter. |
| parameter9  | string    | Optional           | The value for the parameter. |
| parameter10 | string    | Optional           | The value for the parameter. |


#### usage

| Name             | JSON Type | Mandatory/Optional | Description |
| -- | ---| -- | ---- |
| completionTokens | number    | Mandatory          | Number of tokens in the generated completion.                     |
| promptTokens     | number    | Mandatory          | Number of tokens in the prompt.                                   |
| totalTokens      | number    | Mandatory          | Total number of tokens used in the request (prompt + completion). |


#### error

| Name             | JSON Type | Mandatory/Optional | Description |
| -- | ---| -- | ---- |
| statusCode | number    | Mandatory | The HTTP status code that corresponds to the error raised. |
| code       | string    | Mandatory | The code that identifies the type of error. For more information, refer to [Errors](#errors). |
| message    | string    | Mandatory | The error message. |


To ensure proper error handling and data recording, send both the code and statusCode. Refer to the [Errors ](#errors)table below for the expected values for each parameter and the corresponding error type. Any additional errors are recorded as Other errors in AI Agent Builder analytics.

## Errors

Errors are returned with a message and a HTTP Status code.

| Name             | JSON Type | Mandatory/Optional | Description |
| -- | ---| -- | ---- |
| Content filter triggered | 400  | content\_filter           | The response was filtered due to the prompt triggering the custom AI model content management policy. |
| Token limit exceeded     | 400  | context\_length\_exceeded | The token limit for the AI model was exceeded. |
| Rate limit exceeded      | 429  |                           |The rate limit of the AI model was exceeded. |
