---
summary: Exposing REST APIs in your OutSystems applications.
tags: 
locale: en-us
guid: 79ddbf86-371c-41cf-b9c9-45545b74957f
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A22105&t=enlFI20VRi6L4Uys-1
platform-version: odc
---

# Exposing REST APIs

OutSystems allows you to [expose methods using a REST API](<expose-a-rest-api.md>). These methods can be organized under multiple REST APIs.

<div class="info" markdown="1">

If you want to **consume** a REST API, check [Consume REST APIs](../consume_rest/intro.md).

</div>


## REST API Method Flow

When a request to your REST API Method is received, OutSystems executes the following flow:

![Diagram illustrating the execution flow of a REST API method in OutSystems, including OnRequest, OnAuthentication, Parameters Deserialization and Validation, Execute Method, Parameters Serialization, and OnResponse callbacks.](images/rest-expose-method-flow-diag.png "REST API Method Execution Flow Diagram")

1. **OnRequest():** OnRequest callback allows you to run logic over the requests after receiving them. 
1. **OnAuthentication():** OnAuthentication callback allows you to add basic authentication or custom authentication to requests. 
1. **Parameters Deserialization and Validation:** Deserialization of the input parameters and validation of the data types, mandatory values, etc. 
1. **Execute Method:** Executes the action that implements the REST API Method. 
1. **Parameters Serialization:** Serialization of the output parameters to return in the response. 
1. **OnResponse():** OnResponse callback allows you to run logic over the responses before sending them. It is always executed, even in an error situation. 
