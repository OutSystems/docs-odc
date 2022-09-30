---
summary: The OutSystems REST library provides actions to access and manipulate the REST request and response. These actions should be used in the OnBeforeRequestAdvanced and OnAfterResponseAdvanced REST callbacks.
tags: 
locale: en-us
guid: 67ca3d20-f19a-4cbc-8070-e73e1b63d6ba
app_type: mobile apps, reactive web apps
---
# REST

The OutSystems REST library provides actions to access and manipulate the REST request and response. These actions should be used in the OnBeforeRequestAdvanced and OnAfterResponseAdvanced REST callbacks.

## Actions

### Request_AddHeader { #Request_AddHeader }
Adds a header to the current REST request.

_Inputs_

HeaderName : mandatory; data type Text

The name of the header to be added.

HeaderValue : mandatory; data type Text

The value of the header to be added.

### Request_GetActionName { #Request_GetActionName }
Returns the action name from the REST request.

_Outputs_

ActionName; data type Text

The name of the action from the REST request.

### Request_GetHeaders { #Request_GetHeaders }
Returns the list of headers from the current REST request.

_Outputs_

Headers; data type RecordList

The list of headers from the current REST request.

### Request_GetURL { #Request_GetURL }
Returns the request URL from the REST request.

_Outputs_

URL; data type Text

The request URL from the REST request.

### Request_RemoveHeader { #Request_RemoveHeader }
Removes a header from the current REST request, if applicable.

_Inputs_

HeaderName: mandatory; data type Text

The name of the header to be removed.

### Request_SetCookie { #Request_SetCookie }
Sets a cookie in the REST request.

_Inputs_

CookieName: mandatory; data type Text

The name of the cookie to be set.

CookieValue: mandatory; data type Text

The value of the cookie to be set.

### Request_SetURL { #Request_SetURL }
Sets the request URL for the current REST request. The URL should be set before other properties in advanced REST extensibility or they may be lost.

_Inputs_

URL: mandatory; data type Text

The request URL to be set.

### Response_GetActionName { #Response_GetActionName }
Returns the action name from the REST response.

_Outputs_

ActionName; data type Text

The name of the action from the REST response.

### Response_GetBodyAsBinary { #Response_GetBodyAsBinary }
Returns the REST response body as binary data.

_Outputs_

Body; data type Binary Data

The body of the REST response, in binary data.

### Response_GetBodyAsText { #Response_GetBodyAsText }
Returns the REST response body as text.

_Outputs_

Body; data type Text

The body of the REST response, in text.

### Response_GetStatusCode { #Response_GetStatusCode }
Returns the status code of the REST response.

_Outputs_

StatusCode; data type Integer

The status code of the REST response.

### Response_SetBodyAsBinary { #Response_SetBodyAsBinary }
Sets the REST response body with a binary data object.

_Inputs_

Body: mandatory; data type Binary Data

The body to be set, in binary data.

### Response_SetBodyAsText { #Response_SetBodyAsText }
Sets the REST response body with a text object.

_Inputs_

Body: mandatory; data type Text

The body to be set, in text.

