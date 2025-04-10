---
summary: Explore how OutSystems Developer Cloud (ODC) automatically manages REST API Structures for efficient app development.
tags: rest api integration, automated structure generation, api development, structure reuse, data mapping
locale: en-us
guid: f2d563a1-be66-42d3-b56f-ebfc33c32c9c
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3213%3A21329&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - understand
topic:
  - structures
---

# REST API Structures

When you consume REST API methods in your app, OutSystems automatically creates the Structures that define the information held by the input and output parameters. The name of each Structure is generated from:

* The HTTP Request type 
* The method name 
* If it will hold a Request or a Response

The data type of each input or output parameter is [mapped into an OutSystems data type](consume-a-rest-api.md#mapping-rest-data-types-to-outsystems-data-types).

For example, consider the following consumed REST API Method from Twitter:
    
HTTP Request type: `POST`  
URL: `https://api.twitter.com/1.1/account/settings.json?lang={mylanguage}`  
Response:  

```json
{
    "use_cookie_personalization": true,
    "language": "en"
}
```

The following Structure is automatically created for this method:

![Example of an OutSystems Structure created for a consumed REST API method from Twitter](images/ss-rest-consume-structures.png "OutSystems REST API Consumed Structure Example")

## Reuse of Structures

Whenever you add a new REST API method or modify an existing one, OutSystems checks for existing Structures that can be reused to define the information held by the new input and output parameters. This minimizes the number of Structures in your app.

OutSystems reuses an existing Structure when it is considered **compatible** with the requirements of the new method, according to the following rules:

* All attributes with the same name have the same or compatible type
* More than half of the new attributes are covered

When an existing Structure is reused, it may undergo some changes to comply with the different methods where the Structure is used.  
For example, the Structure name might change and get new attributes. The methods in your app already using that Structure won't be impacted by these changes.

### Reusing a Structure Example

Considering the previous Twitter's REST API example, we will now add the GetSettings method of the same REST API, keeping only some relevant response parameters:
    
HTTP Request type: `GET`  
URL: `https://api.twitter.com/1.1/account/settings.json`  
Response:

```json
{
    "use_cookie_personalization": true,
    "language": "en",
    "always_use_https": true
}
```

As the existing "PostSettingsResponse" Structure is compatible with the new method, the Structure is reused. The following changes take place:

* The Structure is renamed to "Settings" to match both methods where it is used
* An additional "Always_use_https" attribute is added to the Structure

![Illustration of reusing an OutSystems Structure for a new REST API method with compatible attributes](images/ss-rest-consume-structures-updated.png "OutSystems REST API Structure Reuse Example")

### Creating a new Structure Example

The following example adds a larger number of parameters to the Response example of the "GetSettings" method and removes one parameter that was already there:
    
```json
{
    "language": "en",
    "always_use_https": true,
    "discoverable_by_email": true,
    "screen_name": "theSeanCook",
    "show_all_inline_media": false,   
    "geo_enabled": true,
    "protected": false
}
```

As only three of the attributes are covered by the existing Structure, which is less than half of the attributes, the existing Structure is not reused. OutSystems creates a new Structure named "Setting" to hold the response of the "GetSettings" method:

![Example of creating a new OutSystems Structure for a REST API method with additional parameters](images/ss-rest-consume-structures-updated-2.png "OutSystems REST API New Structure Creation Example")

The previous "Settings" structure is not deleted since it is still used by the "PostSettings" method.

## Mapping REST data types to OutSystems data types

When [consuming REST API methods](consume-a-rest-api.md) in your app, OutSystems automatically generates the Structures for the Request and Response from the example you provide for them and maps the attributes into OutSystems data Types as follows:

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
