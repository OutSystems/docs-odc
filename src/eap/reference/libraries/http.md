---
summary: Provides actions to manipulate HTTP requests and responses.
tags: 
locale: en-us
guid: 8ab99495-136e-4261-a791-bee1c58d4a79
app_type: mobile apps, reactive web apps
---

# HTTPRequestHandler

The OutSystems HTTP library provides actions to manipulate HTTP requests and responses.

## Actions

### Request_AbsoluteURL

Generates an absolute URL based on the URL provided.

*Inputs*

URL
:   Type: Text. Mandatory.  
    Relative or absolute URL.

*Outputs*

AbsoluteURL
:   Type: Text.  
    Absolute URL.


### Request_GetCookie

Returns the value for the specified cookie from the current HTTP request.

*Inputs*

Name
:   Type: Text. Mandatory.  
    The name of the cookie to be retrieved.

*Outputs*

Value
:   Type: Text.  
    The value for the specified cookie. If no cookie exists, returns empty.


### Request_GetDomain

Returns the host part of the current HTTP request as seen by the browser.

Examples:

When the browser uses the address "http://support.domain.com/site/welcome.aspx?id=12345", Request_GetDomain() = "support.domain.com".

*Outputs*

Domain
:   Type: Text.  
    The domain of the current HTTP request.


### Request_GetFiles 

Returns the list of files submitted in the current HTTP request.

*Outputs*

RequestFiles
:   Type: RecordList of [RequestFile](<#Structure_RequestFile>).  
    Record list of files submitted in the current HTTP request.


### Request_GetHeaders 

Returns the value of the specified header in the current HTTP request.

*Inputs*

Name
:   Type: Text. Mandatory.  
    The name of the header.

*Outputs*

Value
:   Type: Text.  
    The value of the specified header. If the header is not present or has no value, returns empty.


### Request_GetURL 

Returns the absolute URL of the current request. If SEO rules are applied, returns the resulting URL and not the URL displayed in the user's browser.

*Outputs*

URL
:   Type: Text.  
    The URL of the current request.


### Request_ReplaceDomain 

Replaces the domain in the URL with the given domain. This function doesn't accept JavaScript as a URL.

*Inputs*

URL
:   Type: Text. Mandatory.  
    The URL in which to replace the domain.

Domain
:   Type: Text.  
    The new domain to put in the URL. If no value is given, the domain of the current request is used.

*Outputs*

NewURL
:   Type: Text.  
    The URL with the new domain.


### Request_SubmitGetRequest 

Submits an HTTP GET request given the respective arguments and URL, and returns the request response content

*Inputs*

URL
:   Type: Text. Mandatory.  
    The URL of the HTTP GET request.
    
Arguments
:   Type: Text. Mandatory.  
    The arguments of the HTTP GET request.

Timeout
:   Type: Integer.  
    The number of milliseconds before the request times out. If no value is given, no timeout is set.

KeepAlive
:   Type: Boolean.  
    Indicates if the connection to the Internet resource is persistent. If no value is given, defaults to false.

*Outputs*

TextContent
:   Type: Text.  
    The response content, in text.

BinaryContent
:   Type: BinaryData.  
    The response content, in binary data.

BinaryContentType
:   Type: Text.  
   The value of the Content-Type header returned with the response.


### Response_AddHeader 

Adds a header to the current HTTP response.

*Inputs*

Name
:   Type: Text. Mandatory.  
    The name of the header to be added.

Value
:   Type: Text. Mandatory.  
   The value of the header to be added.


### Response_SetCookie 

Sets a cookie in the current HTTP response.

*Inputs*

CookieName
:   Type: Text. Mandatory.  
    The name of the cookie to be set.

CookieValue
:   Type: Text.  
    The value of the cookie to be set. If no value is given, defaults to an empty string.

CookieExpirationSpan
:   Type: Integer.  
    The expiration span of the cookie, in minutes. If lower than or equal to zero, or if no value is given, the cookie will only be valid during the current session.

CookiePath
:   Type: Text.  
    The path that must exist in the requested URL for the browser to send the Cookie header. If no value is given, defaults to the path of the current application.

CookieDomain
:   Type: Text.  
    The host to which the cookie will be sent. If no value is given, defaults to the host of the current document URL, not including subdomains.

CookieHttpOnly
:   Type: Boolean.  
    Indicates if the cookie is HttpOnly. If no value is given, defaults to false. If set to true the cookie value will not be available in JavaScript. This is normally used in security-sensitive cookies.

CookieSecure
:   Type: Boolean.  
    Indicates if the cookie is secure. If no value is given, defaults to what is defined in the security settings for the current environment.
    It's not possible to lower the security specified at the environment level.

CookieSameSite
:   Type: Text.  
    The value of the Cookie SameSite attribute. Can be one of the following: "", "None", "Lax", and "Strict". If no value is given, defaults to what is defined in the security settings for the current environment.


### Response_SetStatusCode 

Sets the status code of the current HTTP response.

*Inputs*

StatusCode
:   Type: Integer. Mandatory.  
    The status code of the response, such as 404, 403.