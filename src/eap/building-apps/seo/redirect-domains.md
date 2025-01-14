---
summary: How to navigate to a root domain and access a default ODC app.
tags: seo, redirection, reverse proxy, nginx configuration, cdn
guid: b622d85c-f6f8-4833-984e-6f825c68754b
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
coverage-type:
  - apply
audience:
  - backend developers
  - full stack developers
  - infrastructure managers
outsystems-tools:
  - odc studio
  - odc portal
---
# Redirect domains

<div class="warning" markdown="1">

This page provides a suggestion on how to achieve improved SEO performance with ODC Applications using third party tools as a workaround and isn't an official supported product offering.

Please be aware of existing [Platform Limits](../../getting-started/system-requirements.md#platform-limits) and that Platform changes can subject unsupported workarounds to breaking changes without warning.

</div>

For SEO purposes and end-user friendliness, allow an end-user to navigate to a root domain and access a default ODC app.

Achieve this by using a reverse proxy or CDN.

Refer to [Improve SEO with prerendering](improve-seo-prerendering.md#domain) which outlines how to configure the reverse proxy Nginx in front of ODC.

Using a reverse proxy or CDN, you can redirect a root domain or other subdomain, e.g., example.com to a default ODC app located at `www.example.com/appx/home` (`{domain}/{app}/{screen}`).

The following snippet is an example of how to achieve this using Nginx reverse proxy: 

Modify the file `nginx/sites-available/default`

Add a new or edit an existing `server {...}` section

```
server {
    server_name example.com;
    listen 443 ssl;
    rewrite ^ $scheme://www.example.com/appx/home;
}
```

To redirect the root domain URL to the default ODC app URL with a 302 HTTP status code, follow this approach.

For example, to redirect `www.example.com` to `www.example.com/appx/home`, use the following configuration snippet:

```
location = / {
    return 302 /appx/home;
}
```

Add this configuration to the `nginx/sites-available/default` file by editing the `location = / {...}` section.

This method is useful when you need to redirect from the root of a domain to a specific route on the same domain, such as the path to a default ODC app.
