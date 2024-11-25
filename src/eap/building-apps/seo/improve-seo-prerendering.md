---
summary: Improve SEO with prerendering.
tags:
guid: 3f649fec-07c4-4a49-843f-a61c22dbf3e5
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
content-type:
  - procedure
---

# Improve SEO with prerendering

<div class="warning" markdown="1">

This page provides a suggestion on how to achieve improved SEO performance with ODC Applications using third party tools as a workaround and isn't an official supported product offering.

Please be aware of existing [Platform Limits](../../getting-started/system-requirements.md#platform-limits) and that Platform changes can subject unsupported workarounds to breaking changes without warning.

</div>

OutSystems Reactive apps are Single Page Applications (SPAs). These are web apps that load a single page and update content dynamically. They offer benefits like dynamic content, smooth navigation, improved performance, offline capabilities, and development simplicity.

When a user accesses the app, the server returns a bare HTML file and some JavaScript that executes on the client side to render the UI. This also allows fetching data asynchronously in parallel with page rendering.

However, when you have very complex logic, or you retrieve a large amount of data, you might experience longer initial loading times due to reliance on client-side rendering (CSR). This can present SEO challenges as search engine bots render the page to index it. 

In these situations, you benefit from using the pre-render technology. Although this improves your app's Core Web Vitals, it doesn't affect the end-user experience.

This article explains how to integrate the OutSystems platform with a third-party pre-rendering solution called [Prerender](http://prerender.io).

<div class="info" markdown="1"> 

There are other pre-render solutions on the market. OutSystems recommends [Prerender](http://prerender.io) as one of your pre-rendering options due to its significant SEO improvements. OutSystems isn't affiliated with or sponsored by Prerender, and doesn’t receive any economic or financial benefit from customers subscribing to their services.

</div>

## Prerequisites

### Custom domain

To integrate an external prerender solution, you need a custom domain. For more information, refer to [Configure custom domains for apps](../../manage-platform-app-lifecycle/custom-domains.md).

### Prerender account

To configure your pre-render solution, you need an account with Prerender. Select a [plan](https://prerender.io/pricing/) that meets your budget and requirements.

For more information on the criteria to consider when selecting a plan, refer to [Prerender usage and configuration](prerender-usage-config.md).

### Reverse Proxy/CDN

Prerender offers several options to integrate with your application. Integrating with ODC can be achieved using a [Reverse Proxy or CDN](https://docs.prerender.io/docs/integrations-1).

## Integrating Prerender with Nginx Reverse Proxy

When a search engine or a social media bot requests a page, Prerender provides the response. If the requested page is already cached, a cached version is served. If not, Prerender fetches the page from your OutSystems app, renders its JavaScript, and serves the fully rendered page to the bot.

<div class="info" markdown="1">

This process is subject to change. For any updates and additional information, refer to [Prerender knowledge base](https://docs.prerender.io/docs/nginx-1).

</div>

### Domain

The first step is to configure the custom domain. Use [Configure custom domains for apps](../../manage-platform-app-lifecycle/custom-domains.md) as a guide to configure custom domains. To work with a Reverse Proxy or CDN, update the domain DNS records to configure a CNAME or A record that directs to the selected Reverse Proxy or CDN.

### Domain and certificate configuration

Acquire an SSL certificate for a custom domain to use with the Proxy/CDN. If using a CDN, verify with the CDN provider to see if they can issue certificates directly. For a reverse Proxy, obtain a certificate from a certificate authority such as [Let’s Encrypt](https://letsencrypt.org/) which offers certificates for free. Tools such as [CertBot](https://certbot.eff.org/) can be used to automate this process.

The following is an example of configuring Nginx to support an SSL certificate:

Modify the file `nginx/sites-available/default` and add the following inside the `server` section: 

Note: Replace `example.com` with your domain.

```
# Standard configuration
listen 80;

# SSL configuration
listen 443 ssl default_server;

# Default of 1meg may be too small
# ODC will not allow more than 28M by default
client_max_body_size = 28M;

# Custom domain
# use customer domain here
server_name example.com;

# To fix authentication issues
proxy_busy_buffers_size   512k;
proxy_buffers   4 512k;
proxy_buffer_size   256k;
# Certificate configuration - use the paths returned by Let's Encypt / certbot as an example
ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem; 
```

Add the following inside the `location /` section:

```
# The address of the destination Cloudfront
# You can retrieve this from ODC portal for
# custom domains
proxy_pass <custom-odc-cloudfront-address>;
# Without this it doesn't work
proxy_ssl_server_name on;
# Other reverse proxy configuration
proxy_ssl_name $host;
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
```

In the `nginx.conf` file, configure these settings within the `http` section:

```
gzip on;
gzip_vary on;
gzip_proxied any;
gzip_comp_level 6;
gzip_http_version 1.1;
gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
```

### Prerender Nginx integration

[Prerender provides instructions](https://docs.prerender.io/v1/docs/nginx-1#reverse-proxy) on configuring their product with the Nginx web server acting as a reverse proxy. The solution involves modifying the Nginx config files.

You can configure which bots are sent to the prerendered version of your pages. To select the bots, modify the `map{...}` section in the `nginx.conf` file. Look for the following lines of code:

```
map $http_user_agent $prerender_ua {
    default       0;
    "~*Prerender" 0;
    ...
}
```

Adjust the list to keep only the bots you need with a value of 1. For more details on why this is important, refer to [Optimize the number of user agents](./prerender-usage-config.md#optimize-the-number-of-user-agents).

### Sitemap.xml { #sitemap } 

To effectively use prerender technology, provide crawlers with a complete website structure through a `sitemap.xml` file.

Ensure the file is available at the domain's root level. For instance, if the domain is example.com, the sitemap is example.com/sitemap.xml. To achieve this result, configure a working route using an ODC app and a reverse proxy or CDN.

Refer to [Generating sitemap and robots files](generating-sitemap-robot-files.md) on creating a sitemap file within an ODC app.

To create and publish a new app to use to host the `sitemap.xml` file, do the following: 

1. In ODC Studio, right-click **Resources** within **Data** tab and select **Import Resource**.

2. Select the newly created `sitemap.xml` file.

3. Select the `sitemap.xml` file and set the **Deploy Action** field to **Deploy to Target Directory**.

As a result, the file is available under MyApp/sitemap.xml. You can publish your app.

4. Configure Reverse Proxy or CDN to serve sitemap to the root directory of the domain. 

Example configuration in an Nginx reverse proxy `sites-available/default` file within the `server{}` section.

```
location = /sitemap.xml {
  # replace with the name of the CDN defined in the
  # domains section of the ODC portal
  proxy_pass https://<CDN_URL>/<APP>/sitemap.xml;
  proxy_ssl_name $host;
  proxy_set_header Host $host;
  proxy_ssl_server_name on;
  proxy_set_header X-Real-IP $remote_addr;
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  proxy_set_header X-Forwarded-Proto $scheme;
}
```

5. Test by going to example.com/sitemap.xml.

### Robots.txt  { #robots }

To effectively use prerender technology, provide crawlers with access to a `robots.txt` file. 

Ensure the file is available at the domain's root level. For instance if the domain is example.com, the robots file should be at example.com/robots.txt. To achieve this result, configure a working route using an ODC app and a reverse proxy or CDN.

Refer to [Generating sitemap and robot files](./generating-sitemap-robot-files.md#robotstxt) on creating a robots file within an ODC app. 

To create and publish a new app to use to host the `robots.txt` file, do the following: 

1. In ODC Studio, right-click **Resources** within **Data** tab and select **Import Resource**.

2. Select the newly created `robots.txt` file.

3. Select the `robots.txt` file, set the **Deploy Action** field to **Deploy to Target Directory**.

As a result, the file is available under MyApp/robots.txt. You can publish your app.

4.  Configure Reverse Proxy or CDN to serve sitemap to root directory of domain.

Example configuration in an Nginx reverse proxy `sites-available/default` file within the `server{}` section.

```
location = /robots.txt {
  # replace with the name of the CDN defined in the
  # domains section of the ODC portal
  proxy_pass https://<CDN_URL>/<APP>/robots.txt;
  proxy_ssl_name $host;
  proxy_set_header Host $host;
  proxy_ssl_server_name on;
  proxy_set_header X-Real-IP $remote_addr;
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  proxy_set_header X-Forwarded-Proto $scheme;
}
```

5. Test by going to example.com/robots.txt.

<div class="info" markdown="1">

If making use of `robots.txt` and `sitemap.xml`, both can be hosted in the same ODC app.

</div>

## Test your implementation

Test your implementation by using the Prerender dashboard and by using a curl command.

### Prerender dashboard

Logging in to the Prerender dashboard for the first time shows a modal window that allows you to test your integration. Follow these steps:

1. Select other integrations.

1. Paste the URL of your app (it has to be exposed to the world).

1. Click **Test**.

1. Select the **Recent Crawler Visits** section. 

All websites redirected to the prerendered version of your app are visible

### Using Curl command

You can mimic a request from a bot by using the curl command and compare it with a user request. Ensure that you target your Reverse Proxy or CDN URL and not the actual site directly. 

#### Prerendered version

Open cmd and type the following. Make sure you replace {example.com} with your real server name and {YourReactiveApp} with the real name of your app:

```
curl -A "googlebot" https://{example.com}/{YourReactiveApp}/
```

With this command, you mimic Google’s crawler call to your website. If it works, you should see the full HTML for your rendered page, including all its content.

#### Live version

Run a similar command to the one you executed before, also replacing the placeholders with the same values.

    curl https://{example.com}/{YourReactiveApp}/

Note that instead of showing the full HTML for your rendered page, you call different JavaScript files. These are the files that render the content of your app to the final users when they open it.

It's advisable to manually test an app without authentication and to test file upload functionality if used to ensure that the reverse proxy/CDN is configured correctly.
