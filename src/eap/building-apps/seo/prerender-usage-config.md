---
summary: Prerender.io usage and configuration best practices. 
tags: 
guid: 99def5e6-f2d0-41cb-821a-20116a620182
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: 
---

# Prerender.io usage and configuration

Prerender serves a cached page in response to the user agent's request. Prerender.io acts like a browser, that is, it opens the page, waits for the JavaScript to load, and then adds the page to the cache. The system counts each of these occurrences as a render. A re-cache (manual or automatic) replaces the previous content but the system considers it a new cache and charges for it. To keep the cost to a minimum, limit your caches. You can adopt the following best practices to keep your Prerender.io costs down. OutSystems recommends periodically monitoring your cache consumption using SEO tools, dashboards and Prerender.io to make suitable configuration adjustments.

## Exclude unnecessary content

Exclude pages from your website that don't appear in web search results. For instance, if your website, www.yourserver.com, has a section like wwww.yourserver.com/documents that you want to keep out of search results, create a new behavior in your Reverse Proxy or CDN. Use the path pattern /documents/. Configure it to ensure that requests to this path are not forwarded to prerender.io.

## Optimize the number of user agents

Adjust the list of bots so that Prerender responds to the necessary ones included in your prerender policy. Only include the necessary bots to help reduce costs. Refer to the [Prerender integration documentation](https://docs.prerender.io/docs/what-integrations-are-already-out-there) to find where you can configure the bot list for your selected integration.

## Adopt cache / re-cache strategy

Adopt an optimal cache/re-cache strategy to minimize costs, as every cache incurs a charge.

Set an automatic re-cache interval for frequently updated website content. Use the Prerender.io [recache API](https://docs.prerender.io/docs/6-api) to instantly refresh new or updated content without extra permissions or external tools. The recache API allows you to disable automatic cache expiration and re-cache only the pages that have changed. This reduces the number of recaches and helps significantly lower cache and re-cache costs.

## Update your sitemaps

Prerender.io crawls the active sitemaps weekly and compares cached URLs with those in the sitemaps. If Prerender.io finds any new or updated URLs, it adds them to the priority queue for caching. Periodically upload your sitemap to Prerender.io, and activate its synchronization. For more information on the Prerender.io sitemap, refer to [Sitemap](https://docs.prerender.io/docs/sitemap).

## Provide correct HTTP status codes

If your pages return an HTTP status code other than 200, add meta tags to inform Prerender.io of the correct HTTP status code. These tags allow you to specify an alternative status code or headers for crawlers and override the default behavior of the HTML page that consistently returns a 200 status code. For example, if a page moves to a new URL, keep the old URL with a blank page and return a 301 status code. Set the meta tags and Prerender.io return a 301 to the crawler with the page's new location.

```
<meta name="prerender-status-code" content="301">
<meta name="prerender-header" content="Location: http://www.yourserver.com">
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

For more information on Prerender.io best practices, refer to Prerender.io [best practices](https://docs.prerender.io/docs/11-best-practices).
