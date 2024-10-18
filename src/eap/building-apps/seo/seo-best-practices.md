---
summary: SEO best practices.
tags: 
guid: e4937d41-b341-4d6b-bd84-7b7958672549
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: 
---

# SEO best practices

This article outlines key technical considerations that, if not implemented, may impose SEO limitations when ranking a public app (website).

These considerations are listed in order of priority. Skipping any of these steps compromises the following requirements. Please be aware that SEO is a broad subject, and there are additional topics not addressed in this article. For more information on SEO, refer to [Google SEO Start Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide).

## Crawlability requirements

Refer to [Improve SEO with prerendering](improve-seo-prerendering.md) for a suggested method for enabling improved crawlability of OutSystems Reactive apps for SEO purposes. 

### HTTP Status

Correct HTTP status codes are crucial for optimizing a website's visibility and performance in search engine results. For more information about Prerender, refer to [Prerender.io](http://Prerender.io).

### URL standardization

Implement URL standardization to avoid penalties for multiple URL versions of the same page. Follow the established standards below:

* All lowercase characters

* Ending with "/" (slash)

* Special characters replaced by "-" (hyphen)

* Spaces replaced by "-" (hyphen)

* Replace more than one hyphen together with a single "-" (hyphen)

* Conversion of “_” (underscore) to “-” (hyphen)

* Ensure you have a secure "https://" connection

* Force the inclusion or removal of `www.` through pre-selection

* External URLs not conforming to this standard should trigger a 301 permanent redirect to the standard format in OutSystems.

To help achieve this URL standardization, create app and screen names in lowercase and use lowercase for any links when using URL parameters between screens. Forge components such as [SEO Utils on Steroids](https://www.outsystems.com/forge/component-overview/18898/seo-utils-on-steroids-odc) can be helpful in some of these cases. It provides functions such as `Text_Normalize` which you can use to create slugs and/or clean URL parameters.

### Robots.txt file

A robots file needs to be accessible at the root level of a domain. ODC doesn't support this functionality. Using a reverse proxy or CDN supports this use case. For more information, refer to [robots.txt](generating-sitemap-robot-files.md#robotstxt-robot).

### Sitemap.xml file

A sitemap file is accessible at the root level of a domain. ODC doesn’t support this functionality. However, using a reverse proxy or CDN supports this use case. For more information, refer to [sitemap.xml](generating-sitemap-robot-files.md#sitemapxml-sitemap). 

### Rel="canonical"

All pages must have a `rel="canonical"` filled by default with the current page URL (also known as self-canonical logic). However, pages set with the `<meta name="robots" content="noindex, nofollow"` or blocked by a `Robots.txt` file don't need `rel="canonical"`.

To help achieve this, Forge components can be helpful such as [SEO Utils on Steroids](https://www.outsystems.com/forge/component-overview/18898/seo-utils-on-steroids-odc) which provides functions such as `Metadata_AddLinkValueName`.

When constructing links, be sure to use the best URL to serve that page, not necessarily the URL that the end-user is currently using. Remember to normalize the URL as described earlier. For example, you can access the Default screen of an app by two URLs: example.com/appname/ and domain.com/appname/screenname.

### HTML a href attribute links

Search engine bots don’t crawl JavaScript links. Consequently, convert all internal links from JavaScript to `<a href="URL">` format to ensure crawlability.

In ODC applications, this means being cautious and avoiding using widgets that use OnClick events to run client actions that link to/navigate to other screens. Instead, consider using Button and Link components to link directly to URLs.

### Qualify Outbound Links

Google considers links from one site to another an endorsement. Therefore, setting the correct type of external links helps ensure proper functionality.

For more information, refer to [Qualify your outbound links to Google](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links).

In ODC, you achieve this by using extended properties to insert the relevant metadata.

## Indexability requirements

### HTML Title Tag

All pages require a Title Tag displayed on Google's Search Engine Result Page. The tag must be unique and no more than 60 characters in length.

In ODC Studio, you can set this via a screen's Title property.

### HTML Meta Description

All pages require a meta description displayed on Google's Search Engine Result Page. The tag must be unique and no more than 160 characters long.

Forge components may help. For instance, the component [SEO Utils on Steroids](https://www.outsystems.com/forge/component-overview/18898/seo-utils-on-steroids-odc) provides the action `Metadata_AddToPage`, allowing you to add metadata.

### HTML H1 Tag

All pages should include an H1 tag, which needs to appear on only one page, and its content must be unique across the website.

In ODC, you can add this tag using the HTML Element widget and set the Tag to H1.

### HTML Image alt text

All images should include alternative text that describes the image. This helps Google understand the image and enhances accessibility for blind users, enabling screen readers to describe image details.

In ODC, you can achieve this by using extended properties to insert the alt tags.

### Schema Markups

Google uses structured data on the web to understand page content and gather information about websites. This standardized format provides information about a page and classifies its content, enabling more engaging search results that encourage user interaction with a website.

### Avoid interstitials 

Intrusive dialogs and interstitials make it hard for Google and other search engines to understand your content, which may lead to poor search performance.

For more information, refer to [Avoid intrusive interstitials and dialogs](https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials).
