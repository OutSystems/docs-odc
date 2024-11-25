---
summary: Removing _ts from query strings.
tags:
guid: 70399158-64c3-4630-91ee-46c3bb17ead7
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
content-type:
  - reference
---

# Remove _ts from query strings

<div class="warning" markdown="1">

This page provides a suggestion on how to achieve improved SEO performance with ODC Applications using third party tools as a workaround and isn't an official supported product offering.

Please be aware of existing [Platform Limits](../../getting-started/system-requirements.md#platform-limits) and that Platform changes can subject unsupported workarounds to breaking changes without warning.

</div>

OutSystems apps use caching to increase page performance and load times. To track whether a page requires an update after a new deployment, OutSystems reactive apps use a query string parameter called _ts. An OutSystems app can check the value of this parameter to calculate whether it needs to refresh assets.

This parameter isn't mandatory for a page to load. e.g. if a customer accesses an OutSystems app at `https://example.com/exampleapp` the app renders the Home screen. However, when navigating between pages of an app, the URL navigated to may look like `https://example.com/exampleapp/home?_ts=3123123`.

This parameter has no effect on the user experience for general use. However, in cases where an app is being crawled by a bot for SEO purposes, the presence of the _ts parameter can cause a bot to detect duplicate pages, e.g., `https://example.com/exampleapp/home?_ts=3123123` and, after an app deployment, `https://example.com/exampleapp/home?_ts=412345`.

To minimize the effect this behavior has on SEO performance, a Reverse Proxy or CDN can perform a 301 redirect when a bot is detected. This tells the bot to index the page without the _ts parameter.

Refer to this example of achieving this using the Nginx reverse proxy. Refer to [Improve SEO with prerendering](improve-seo-prerendering.md#domain) for information on configuring a reverse proxy with custom domains on ODC.

nginx_installation_directory/nginx.conf

```
http {
    # ... other http configurations ...

    # check if the request comes from a bot crawler
    # in this configuration example the list of bots
    # is not complete for simplicity
    map $http_user_agent $is_crawler {
        default 0;
        "~*(googlebot|bingbot|yandex|baiduspider|...)" 1;
    }
}
```

nginx_installation_directory/sites-available/default

```
server {
    # ... other server configurations ...

    location / {
        # mask to say if we should rewrite the url
        # mask "{contains_ts}{is_crawler}"
        set $bot_ts_mask "";
            
        # check if the arguments contain a _ts
        if ($args ~ (^)_ts=[0-9]+(.*)|^(.*)&_ts=[0-9]+(.*)) {
            # build the mask
            set $bot_ts_mask "1${is_crawler}";
            # save the arguments of the uri without _ts
            set $args_no_ts $1$3$2$4;
        }

         # if the args contain _ts and is a crawler
         if ($bot_ts_mask = "11") {
            # set the args to the list of args without _ts
            set $args $args_no_ts;
            # rewrite the uri to no _ts form - generates 301
            rewrite ^(.*)$ $uri permanent;
          }

            # ... other location / configurations ...
        }
    }
```
  