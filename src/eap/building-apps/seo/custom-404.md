---
summary: Display a custom 404 error page when a specific URL can't be found. 
tags: 
guid: 0b037701-1e07-4ace-983f-6a20d500aa1f
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: 
---

# Custom 404 pages

Display a custom 404 error page for SEO purposes and end-user friendliness when a specific URL can't be found.

Achieve this by using a reverse proxy or CDN.

Refer to [Improve SEO with prerendering](./improve-seo-prerendering.md#domain) which outlines how to configure the reverse proxy Nginx in front of ODC.

The following steps enable custom 404 pages to be served:

1. The user makes a request.

1. ODC serves the request through the reverse proxy.

1. If ODC returns a 404 error, Nginx points to a specific resource in ODC.

    * The resource is a static HTML file uploaded inside an application, which has an iframe pointing to an ODC page.

Steps to configure a custom 404 page:

1. Create an ODC application to hold your 404 page.

1. Add a custom error page to that application on ODC Studio.

1. Create a static HTML file with an iframe pointing to that custom error page, for instance, notfound.html.

1. Add the static HTML file as a resource to your custom 404 application.

1. Configure the Nginx reverse proxy to point to that static file for 404 errors.

   1. Modify the file `nginx/sites-available/default`

   1. Add the following code to the `location / {...}` block

```
proxy_intercept_errors on;
error_page 404 /NotFound/notfound.html;
```

In this example, any app that throws a 404 Not Found HTTP status code redirects to the custom 404 page. Create a standalone 404 ODC app that can be designed/customized to fit requirements; however, it's possible to host the 404 page in an existing app if preferred.
