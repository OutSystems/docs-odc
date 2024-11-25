---
summary: Prerender usage and configuration best practices.
tags:
guid: 99def5e6-f2d0-41cb-821a-20116a620182
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
content-type:
  - reference
---

# Prerender usage and configuration

Prerender serves a cached page in response to the user agent's request. Prerender acts like a browser, that is, it opens the page, waits for the JavaScript to load, and then adds the page to the cache. The system counts each of these occurrences as a render. A re-cache (manual or automatic) replaces the previous content but the system considers it a new cache and charges for it. To keep the cost to a minimum, limit your caches. You can adopt the following best practices to keep your prerender costs down. OutSystems recommends periodically monitoring your cache consumption using SEO tools, dashboards and Prerender to make suitable configuration adjustments.

## Exclude unnecessary content

Exclude pages from your website that don't appear in web search results. For instance, if your website, `www.example.com`, has a section like `www.example.com/documents` that you want to keep out of search results, create a new behavior in your Reverse Proxy or CDN. Use the path pattern /documents/. Configure it to ensure that requests to this path aren't forwarded to Prerender.

## Optimize the number of user agents

Adjust the list of bots so that Prerender responds to the necessary ones included in your prerender policy. Only include the necessary bots to help reduce costs. Refer to the [Prerender integration documentation](https://docs.prerender.io/docs/what-integrations-are-already-out-there) to find where you can configure the bot list for your selected integration.

## Adopt cache/re-cache strategy

Adopt an optimal cache/re-cache strategy to minimize costs, as every cache incurs a charge.

Set an automatic re-cache interval for frequently updated website content. Use the Prerender [recache API](https://docs.prerender.io/docs/6-api) to instantly refresh new or updated content without extra permissions or external tools. The recache API allows you to disable automatic cache expiration and re-cache only the changed pages. This reduces the number of recaches and helps significantly lower cache and re-cache costs.

## Update your sitemaps

Prerender crawls the active sitemaps weekly and compares cached URLs with those in the sitemaps. If Prerender finds any new or updated URLs, it adds them to the priority queue for caching. Periodically upload your sitemap to Prerender, and activate its synchronization. For more information, refer to [Prerender's Sitemap Crawler](https://docs.prerender.io/docs/sitemap).

## Provide correct HTTP status codes

If your pages return an HTTP status code other than 200, add meta tags to inform Prerender of the correct HTTP status code. These tags allow you to specify an alternative status code or headers for crawlers and override the default behavior of the HTML page that consistently returns a 200 status code. For example, if a page moves to a new URL, keep the old URL with a blank page and return a 301 status code. Set the meta tags and Prerender returns a 301 to the crawler with the page's new location.

```
<meta name="prerender-status-code" content="301">
<meta name="prerender-header" content="Location: http://www.example.com">
```

To do that, you can leverage the JavaScript node in ODC Studio and add the meta tag to a page if its location changed:

```
var headObject = document.getElementsByTagName("head")[0];
var metaName = "prerender-status-code";
var metaValue = "310";
var metaObject = document.getElementsByName(metaName);
if (metaObject != undefined && metaObject.length != 0) {
    metaObject.forEach((item) => { item.remove() });
}
var metaObject = document.createElement("meta");
metaObject.name = metaName;
metaObject.content = metaValue;
headObject.appendChild(metaObject);
```

Repeat this code for each meta tag you add by replacing the values of variables' metaName and metaValue. By adding meta tags, you ensure that the crawler doesn't store 200 for a page that changed its location and that the crawler history is accurate.

Alternatively, you can leverage Forge Components such as the `Metadata_AddTagValueName` Client Action available on the [SEO Utils on Steroids](https://www.outsystems.com/forge/component-overview/18898/seo-utils-on-steroids-odc) Forge component to achieve the same result.

For more information on Prerender best practices, refer to Prerender [best practices](https://docs.prerender.io/docs/11-best-practices).
