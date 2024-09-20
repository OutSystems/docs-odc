---
summary: How to generate and sitemap and robot file. 
tags: 
guid: 7e883e55-675d-4cb8-a0b5-805d2eaf60dd
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=5895-800&node-type=canvas&t=zTqDJ1OjTTDkeMmV-0
---

# Generating sitemap and robots files

The `sitemap.xml` and `robots.txt` files let you control website crawlers and index the public pages in your apps. Use `robots.txt` rules to prevent crawling, and `sitemap.xml` to encourage crawling.

This diagram explains the connection between crawlers, sitemaps, and robots:

![Diagram showing the interaction between an SEO crawler, robots.txt file, and sitemap.xml. The crawler becomes aware of a site, lands in the robots.txt file, notices the sitemap reference, consumes the sitemap content, visits all sitemap endpoints, and parses sitemap URLs for indexing.](./images/seo-crawler-diag.png "Diagram of SEO Crawler Interaction with Sitemap and Robots.txt")

## Sitemap.xml

A sitemap is a file where you provide information about the pages, videos, and other files on your site, and the relationships between them. Having a sitemap speeds up content discovery by enabling search engines to identify your website structure and crawl your site more efficiently. A sitemap informs the search engines about what pages and files you think are important on your site, and also provides valuable information about them. For example, the sitemap provides information like the timepoint when the page was last updated and any alternate language versions of the page.

### Sitemap.xml formatting

<div class="info" markdown="1">

Access additional information about XML formatting rules on this [Sitemaps XML format](https://www.sitemaps.org/protocol.html) web page.

</div>

A sitemap is valid if its location attribute (URL) is in an XML format that follows the formatting rules and can be parsed by crawlers. When an app is under frequent development, the sitemap becomes outdated. As a solution, because most addresses are valid locations for a sitemap, use a REST API to create a sitemap for your apps. This REST API computes and returns a plan of your website following the XML formatting rules.

### Create a static sitemap.xml file

To create a static sitemap, follow these steps:

1. [Create a REST endpoint](#create-a-rest-endpoint) that lists URLs in your app.

1. Create a local `sitemap.xml` file using a text editor of your choice.

1. Reference the created REST endpoint to your `sitemap.xml`.

1. Deploy the `sitemap.xml` as a static file.

### Create a REST endpoint

1. In ODC Studio, go to the **Logic** tab and expand the **Integrations** folder.

1. Right-click **REST** and select **Expose REST API**.

1. Enter a name for the API.

1. Add a method that returns the sitemap details. To do this, right-click the newly created REST API and select **Add REST API Method**.

1. Enter a name for the method.

1. Add a text output parameter. The output parameter is used to iteratively build the sitemap.

The REST method’s output is an XML formatted list that includes all URL endpoints that are relevant for the search engine crawlers.

#### Example XML formatted list

```
<?xml version='1.0' encoding='UTF-8'?>
<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>
     <url>
        <loc>https://example.com/Home</loc>
     </url>
     <url>
        <loc>https://example.com/Login</loc>
     </url>
</urlset>
```

To achieve the XML formatted list that includes all URL endpoints, there must be a hostname that's the same for all URLs. Consider having a local variable to easily reuse this hostname across every screen.

To generate and validate a sitemap that includes both static and dynamic screens for an app:

1. Add URLs for screens without input parameters (static screens).

1. Compute and add URLs based on aggregate results for all screens that require input parameters (dynamic screens).

1. To validate the sitemap output, go to the method URL, right-click the **REST API** and select **Open documentation**. Then click **GET**, copy the Request URL and paste it in a new browser tab.

A list of URLs for your app’s screens are displayed. Validate if new URLs appear in the REST endpoint, verify that the number of URLs doesn't exceed 50,000 and that the filesize of the generated xml is below 50 mb.

### Add sitemap.xml to the root directory of a domain

ODC doesn't support the functionality to set an app at the root directory of a domain. Refer to [Sitemap.xml](./improve-seo-prerendering.md#sitemapxml) for how the sitemap is configured with the help of a Reverse Proxy or CDN.

## Robots.txt

The `robots.txt` is a text file with instructions for search engine crawlers. It defines which areas of a website the crawlers are allowed to search.

A `robots.txt` file consists of one or more rules. Each rule blocks or allows a crawler to access a specified file path on the domain or subdomain that hosts the `robots.txt` file. Using this text file, you can exclude domains, directories, subdirectories, or individual files from search engine crawling. The `robots.txt` file can also integrate a link to your sitemap, which gives search engine crawlers an overview of all URLs of your domain.

The `robots.txt` is stored in the root directory of a domain. Thus it is the first document that crawlers open when visiting your website.
`Robots.txt` files follow the Robots Exclusion Protocol and this is an example of what they look like:

```
User-agent:*
Allow: /

User-agent: Adsbot-Google
Allow: /store

User-agent: Googlebot
Allow: /
Disallow: /profile
```

### Create a static robots.txt file

To create a static `robots.txt` file, follow these steps:

1. Create a local `robots.txt` file using a text editor of your choice.

1. In the `robots.txt` file, reference the `sitemap.xml` endpoint and other directives that you need, following the structure of the Robots Exclusion Protocol.

### Add robots.txt to the root directory of a domain

ODC doesn’t support the functionality to set an app at the root directory of a domain. Refer to [Sitemap.xml](./improve-seo-prerendering.md#sitemapxml)for how the robots file can be configured with the help of a Reverse Proxy or CDN.
