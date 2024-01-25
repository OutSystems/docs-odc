---
summary: The article explains how to retrieve the full URL or URL path of the current screen in OutSystems applications
tags:
locale: en-us
guid: add42ac6-eb89-4448-8b6e-84ceb8a921df
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---
# URL

## GetBookmarkableURL

Returns the URL of the screen that is currently being processed.  
The URL returned by this function is a complete URL with the format `https://organization.outsystems.app/app/screen?param1=value&param2=value...`
Parameters and their values aren't included when parameters are optional and their values aren't set.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.

### Output

Type: Text  

### Examples

```
GetBookmarkableURL() = "http://myserverat.outsystemscloud.com/Customers/EditCustomer.aspx?CustomerId=1"
```

<div class="info" markdown="1">

The domain part of the URL is always the built-in domain.

</div>

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
