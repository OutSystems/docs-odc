---
summary: Learn how to consume REST APIs using OutSystems Developer Cloud (ODC) by understanding API documentation, security requirements, and data type mappings.
helpids: 30484
tags: rest apis, api authentication, data type mapping, api security, api documentation
locale: en-us
guid: b7e2daa5-b34c-4907-885b-56574bf14295
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
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

# Consume REST APIs

When you need to retrieve or manipulate information from another system, and that system provides REST APIs for that effect, you can consume a REST API in your application.  
Start by looking into the documentation of the REST API you want to use and understand how it works. You'll need to gather the following information:

* Base URL
* Security and authentication requirements
* Methods definition (HTTP Method, URL Path, response format)

Check how you can [Consume one or more REST API Methods](consume-a-rest-api.md) in ODC Studio.

<div class="info" markdown="1">

If you want to **expose** an OutSystems REST API, check [Expose REST APIs](../exposing_rest/intro.md).

</div>

## REST API authentication

Each consumed REST API will have their own model of security and authentication process, which may imply the creation of an account, the registration for an API key or the usage of tokens. To consume a REST API in OutSystems you must understand and follow the provider's security model.

REST APIs using **Basic Authentication** are supported out of the box in the "Consume REST API Method" dialog box described below. You can use the REST customization capabilities to add support for other authentication methods:

> **Warning:** OutSystems does not support self-signed certificates. The REST API must have a valid public certificate with a public certificate authority to ensure the request is accepted, either at the client or server side.

* For token-based authentication, use the **OnBeforeRequest** callback to add the required HTTP authorization header to the outgoing requests. 

## Mapping REST data types to OutSystems data types

When [consuming REST API Methods](consume-a-rest-api.md) in your app, OutSystems automatically generates the Structures for the Request and Response from the example you provide for them and maps the attributes into OutSystems Data Types as follows:

| JSON example | OutSystems Data Type | Comments |
| ---| ---| ---- |
| `{"quantity": 123456789}`| Long Integer | Highest value: 2^63-1 |
| `{"totalprice": 12345678901, "amount": -3935.120}`| Decimal | If the value is an integer, but greater than or equal to 2^63, a decimal parameter is created. |
| `{"createdon": "2014-12-31T23:59:59+01:00", "shippedon": "2015-01-01T19:00:00.256"}` | Date Time | If the ISO date contains information about the time zone, it's automatically converted to the local time of the server, with daylight savings applied. |
| `{"scheduledstart": "/Date(1388534400000)/"}`| Date Time | WCF format |
| `{"createdon": "2014-12-24"}`| Date | Format: YYYY-MM-DD |
| `{"canupdate": true}`| Boolean |  |
| `{"image-png": "data:image/png;base64,sample-base64-data"}`| Binary | The platform sends binary data as base64, and converts received base64 to binary when the attribute is set to binary. |
| `{"name": "Christine Sharp"}`| Text | |

Data that can't be converted to one of the above data types is converted to Text.

## Related resources

* [Consuming REST APIs](https://learn.outsystems.com/training/journeys/consuming-rest-api-207) online course
