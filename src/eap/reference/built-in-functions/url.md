---
summary: OutSystems Developer Cloud (ODC) URL built-in functions GetBookmarkableURL and GetOwnerURLPath, with availability, output, and custom URL patterns.
tags:
  - Logic
  - Screens
locale: en-us
guid: add42ac6-eb89-4448-8b6e-84ceb8a921df
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
coverage-type:
  - remember
isautopublish: true
---

# URL

> This reference lists the URL-related built-in functions currently available in OutSystems Developer Cloud (ODC). Functions documented here, such as GetBookmarkableURL and GetOwnerURLPath, are available in ODC Studio. Other URL functions that may exist in different OutSystems platforms (for example, GetDefaultDomain) might not be available in ODC.

## GetBookmarkableURL

Returns the URL of the screen that is currently being processed.  
The URL returned by this function is a complete URL with the format `https://organization.outsystems.app/app/screen?param1=value&param2=value`

Parameters and their values aren't included when parameters are optional and their values aren't set.  

Available in:  

* Server-side logic: Yes
* Client-side logic: Yes
* Database: Function is evaluated before the aggregate is executed.

### Output

Type: Text  

### Examples

```
GetBookmarkableURL() = "https://my-org.outsystems.app/Customers/EditCustomer?CustomerId=1"
```

### Custom URLs

If a screen has the **Custom URL** property set to **Yes**, `GetBookmarkableURL()` returns the URL with the screen's custom **Page Name** instead of the default screen name. The format of the returned URL depends on the screen's **URL Structure** property:

* **Query string**: the custom page name replaces the screen name in the URL, and input parameters remain query string parameters.
* **Path**: input parameters are embedded in the URL path, following the pattern defined in the **URL Pattern** property, using `{ParameterName}` placeholders.

For example, take a screen with **Custom URL** set to **Yes** and **Page Name** set to `mycustompage`, with an input parameter named `CustomerId`. With **URL Structure** set to **Query string**, `GetBookmarkableURL()` returns a URL like this:

```
GetBookmarkableURL() = "https://my-org.outsystems.app/MyApp/mycustompage?CustomerId=1"
```

With **URL Structure** set to **Path** and **URL Pattern** set to `mycustompage/{CustomerId}`, `GetBookmarkableURL()` returns a URL like this:

```
GetBookmarkableURL() = "https://my-org.outsystems.app/MyApp/mycustompage/1"
```

## GetOwnerURLPath

Returns the URL path of the app that owns the element that is being processed. Note that this function does not return the complete URL but only the component containing the location of the resource within the domain and, if applicable, the personal area.  

Available in:  

* Server-side logic: Yes
* Client-side logic: Yes
* Database: Function is evaluated before the aggregate is executed.

### Output

Type: Text  

### Examples

```
GetOwnerURLPath() = "/Customers/"
```
