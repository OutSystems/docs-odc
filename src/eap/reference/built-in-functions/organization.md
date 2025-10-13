---
summary: OutSystems Developer Cloud (ODC) supports functions like GetCurrentLocale and GetUserAgent for app customization and session management.
tags: localization, session management, http headers, language support, user experience customization
locale: en-us
guid: f28abaec-a3f6-406b-9282-94f30588a1cd
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
  - remember
---

# Organization

## GetCurrentLocale

Returns the name of the current language locale of the user session. The name of the language locale is used for presentation purposes and follows the RFC 1766 standard format.  

Available in:  

* Server-side logic: Yes
* Client-side logic: Yes
* Database: Function is evaluated before the aggregate is executed.

### Output

Type: Text  

### Examples

```
GetCurrentLocale() = "en-US"
```

## GetUserAgent

Returns the user agent, as indicated by the header of the HTTP message.  

Available in:  

* Server-side logic: Yes
* Client-side logic: Yes
* Database: Function is evaluated before the aggregate is executed.

### Output

Type: Text  

### Examples

```
GetUserAgent() = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"
GetUserAgent() = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
```

## GetAppName

Returns the name of the app that is processing the request.

### Examples

```
GetAppName() = "MyApp"
```
