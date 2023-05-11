---
summary: Learn more about necessary cookies in the ODC apps.
tags:
locale: en-us
guid: 8683a640-36ce-43e0-8e9d-7c47705ed89f
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Cookies in ODC

In compliance with directive 2009/136/EC of the European Parliament and of the Council of 25.11.2009, end-users must know what cookies the apps use, the data collected, and the intended usage of collected data.

## Cookies usage

When an end-user visits a web app, the app places a cookie on their device only if they accept cookies. Or, the app reads the cookie if they visited the app before and allowed cookies. Cookies help developers make web apps more user-friendly and can also be used to gather metrics and generate visitor statistics.

The ODC apps use cookies to identify end-users and improve the usability of the app. For example, cookies enable automatic sign-in to the app.

## Not accepting cookies

If end-users don't accept cookies from the ODC apps, the users can still access some parts of the app that don't require a sign-in. However, not accepting cookies may limit some functionalities of the app.

## Necessary cookies

ODC generates necessary cookies, such as osvisitor. If the app uses extra cookies from third-party solutions, developers should inform the end-users about their purpose. The following table describes the cookies created by the apps in ODC.

| Cookie name | osvisit `<AppKey>`  | osvisitor   |
|--| -- | -- |
| Description | When a user visits a web page for the first time, a osvist cookie is created with a unique value to indicate that the user accessed the site. If the user returns after the expiration of the cookie, the app creates a new cookie. The osvisit cookie stores values for each app separately. The format is `osvisit<AppKey without hyphens>`, for example osvisitfdb5808b381e41a894a9e8717b2d31de. |  A unique value is stored in a cookie when a user accesses a web page from a server for the first time. |
| Approx size (Bytes)  | 40  | 45 |
| Expiration           | 30 mins  | never |
| HTTP only            | Yes   | Yes  |
| Secure               | No    | No   |
| Stores personal data | No  | No  |
