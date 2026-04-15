---
summary: Discover how to call APIs in OutSystems Developer Cloud (ODC) using an access token, with step-by-step guidance for developers.
tags: api access token, rest api, odc, token validation, api call example
outsystems-tools:
  - odc portal
guid: 850e2e06-cdab-4e45-9ea6-2964c1a3a5ce
locale: en-us
app_type: reactive web apps, mobile apps
content-type:
  - procedure
audience:
  - full stack developers
  - backend developers
platform-version: odc
figma:
---
# Call API using the access token

Once the authorization server validates the credentials and generates an access token, you can call the APIs using the access token. The access token is valid only for 12 hours from the time it was generated. Use the access token within the validity period of to access the APIs.

Once the token expires, you must generate a new access token to call the API. This article explains how to call an API using the access token. It is intended for developers who want to access the ODC REST APIs from their app.

## Prerequisites

Before calling the API using the access token, ensure you have:

* Set the client credentials in the app

* [Generated the access token](get-access-token.md) using the client credentials

## Call API

With the access token, you are ready to make your first API call.

  <div class="info" markdown="1">

  OutSystems recommends that you consume the API in a library so that the API endpoints can be used across different apps. To explore a sample library, refer to User Management Connector in [ODC User Management Forge](https://www.outsystems.com/forge/component-overview/21016/users-management-odc) component.  

  </div>

To call an API using the access token, follow these steps:

1. [Consume the API](../../../../integration-with-systems/consume_rest/consume-a-rest-api.md) in ODC Studio. You can consume either one or multiple methods using the OpenAPI specification file.  

1. Set the **Base URL** for the API.

1. Add the access token in Authorization HTTP header as `Bearer {Access token value`. For detailed information, refer to [Adding a header for token-based authentication](../../../../integration-with-systems/consume_rest/simple-customizations.md#example-use-case-adding-a-header-for-token-based-authentication).

    You can use [OnBeforeRequest](../../../../integration-with-systems/consume_rest/simple-customizations.md#customize-the-request) callback to customize the header information.

1. Drag and drop the consumed API method into your app's logic flow. Pass the required input parameters and handle the API response in your app's logic. For detailed information, refer to [Use the API](../../../../integration-with-systems/consume_rest/intro.md#use-rest-apis-in-your-app).

## Related resources

### Consume API

* [Consume one or more REST API methods](../../../../integration-with-systems/consume_rest/consume-a-rest-api.md)
  
* [Customize API request and response headers](../../../../integration-with-systems/consume_rest/simple-customizations.md)

### API authentication and access

* [Configure API access using an API client](create-api-client.md)
  
* [Generate new client secret](generate-new-secret.md)
  
* [Get access token using client credentials flow](get-access-token.md)
  
### ODC REST API reference

* [User management API reference](../../identity-v1.md)

* [Portfolio API reference](../../portfolio-v1.md)
