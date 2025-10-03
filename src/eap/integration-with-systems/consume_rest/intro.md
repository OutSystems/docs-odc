---
summary: Learn how to consume REST APIs using OutSystems Developer Cloud (ODC) by understanding API documentation, security requirements, and data type mappings.
helpids: 30484
tags: rest apis, api authentication, data type mapping, api security, api documentation
locale: en-us
guid: b7e2daa5-b34c-4907-885b-56574bf14295
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=3101-11328
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - understand
  - remember
topic:
  - consume-refresh-methods
---

# Use REST APIs in your app

You can use REST APIs in your app to retrieve or update data from an external systems or leverage the resources of your ODC tenant, such as users, groups, app roles. For detailed information about using resources of your ODC tenant at runtime, refer to [ODC REST APIs](../../reference/apis/public-rest-apis/overview.md). 

To use the REST APIs in your app, you must consume the APIs in ODC Studio. 

Before you consume the API, ensure that you have the following details from the API reference documentation.

* Base URL
* Security and authentication requirements
* Methods definition (HTTP Method, URL Path, response format)

For authenticating the APIs, you must follow the authentication requirements of the external API.
The external API can support any one of the following authentication methods:

* **Basic authentication** - Configure the authentication credentials such as username and password while consuming the APIs. For detailed information, refer to [Configure basic authentication](#configure-basic-authentication).
* **Token-based authentication** - For token-based authentication such as OAuth 2.0, you must implement logic to generate the access token and include the token in the header. ODC REST APIs follows OAuth 2.0 for authentication. 
* **API Keys or other methods** – For any other authentication methods, get the keys and implement logic for configuring the neceessary headers.

Here's the high-level process for consuming REST APIs in ODC Studio:

* [Add a single API method](consume-a-rest-api.md#add-a-single-rest-api-method--single-method-) or [Add multiple API methods](consume-a-rest-api.md#add-several-methods-of-a-rest-api--all-methods-) by importing the OpenAPI specification file.
  
* [Configure the API authentication](#configure-the-api-authentication) details for the REST API. For configuring basic authentication, refer to [Configure basic authentication](#configure-basic-authentication). For configuring token-based authentication, refer to [Configure token-based authentication](#configure-token-based-authentication).
  
* (Optional) [Customize](simple-customizations.md) the request and response headers using specific callbacks.
  
* If you want to configure base URL or basic authentication credentials for every stage then from ODC portal, [Configure](consume-a-rest-api.md#configure-api-endpoints-and-basic-authentication) the base URL and basic authentication credentials such as username and password.
  
* [Use the API](consume-a-rest-api.md#use-a-rest-api-method-in-your-app--use-) in your app.

<div class="info" markdown="1">

If you want to **expose** an OutSystems REST API, check [Expose REST APIs](../exposing_rest/intro.md).

</div>

## Configure API authentication

Each REST API you consume has its own security and authentication requirements. This means you may need to create an account, obtain an API key, or use access tokens. To successfully consume a REST API in OutSystems, you must understand and comply with the security model defined by the API provider.

ODC has built-in support for REST APIs that support **basic authentication**. For detailed information, refer to [Configure basic authentication](#configure-basic-authentication). 

To use other token-based authentication methods, refer to [Configure token-based authentication](#configure-token-based-authentication).

<div class="warning" markdown=1>

OutSystems does not support self-signed certificates. The REST API must have a valid public certificate with a public certificate authority to ensure the request is accepted, either at the client or server side.

</div>

### Configure basic authentication

To configure basic authentication for the REST API, follow these steps:

1. Once you have added the API in ODC Studio, from the properties of the API, choose the **Authentication Type** as **Basic authentication**.
1. Go to **ODC portal** and from the app configuration, set the credentials (username and password) for basic authentication. The basic authentication credentials can be configured for every stage. For detailed information on configuration, refer to [Configuration base URL and authentication credentials](./consume-a-rest-api.md#configure-api-endpoints-and-basic-authentication).

For detailed information, refer to [Consuming a REST API ODC training](https://learn.outsystems.com/training/journeys/consuming-rest-api-207/consuming-a-rest-api/odc/7996).

### Configure token-based authentication

ODC does not provide built-in support for token-based authentication such as OAuth 2.0 authorization. In such cases to authenticate the API call you must:

1. [Generate the access token.](generate-reuse-oauth-token.md) 
   
1. Include the [token in the request header](simple-customizations.md#example-use-case-adding-a-header-for-token-based-authentication) using the **OnBeforeRequest** callback. 

## Related resources

### Getting started

* [Consume one or more REST API methods](consume-a-rest-api.md)

### Authentication and security

* [Configure base URL and basic authentication credentials](consume-a-rest-api.md#configure-api-base-url-and-basic-authentication)
  
* [Generate OAuth access token](generate-reuse-oauth-token.md)
  
* [Customize API request and response headers](simple-customizations.md)

### Use API

* [Use API in your app](consume-a-rest-api.md#use-a-rest-api-method-in-your-app--use-)

### Online training

* [Consuming REST APIs ODC Online training](https://learn.outsystems.com/training/journeys/consuming-rest-api-207) online course
  