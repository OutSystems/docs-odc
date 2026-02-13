---
summary: Learn how to activate and configure Content Security Policy (CSP) in OutSystems Developer Cloud (ODC) to enhance app security.
tags: web security, content security policy, csp, mobile apps, odc
guid: 6575ff95-52d4-4f2b-acf8-945066b73217
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/kw9RAhge7eEpiKLnvKnOek/Security-of-OutSystems-Developer-Cloud?node-id=5005-10
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - odc portal
coverage-type:
  - apply
---

# Implement content security policy

Implementing a content security policy (CSP) in ODC involves activating CSP for your stage and configuring directive values to match your app's security requirements. This document guides you through the activation and configuration process, explains the available directives and their default values, and describes the required values that ensure your apps work correctly.

Before you begin, ensure you understand what CSP is and how it protects your apps. For more information about CSP and mobile app considerations, refer to [Content security policy](configure-csp.md).

## Planning your CSP configuration

Identify your app's security requirements by analyzing the following areas relevant to both reactive web apps and native mobile apps:

**External service dependencies:**

* Authentication providers (OAuth, SAML, built-in identity)
* REST APIs and backend services
* Third-party services (analytics, crash reporting, push notifications)
* Content delivery networks (CDNs)
* Media streaming services

**App-specific integrations:**

* For mobile apps: Camera, media plugins, file storage/download, geolocation, mapping, custom Cordova/Capacitor plugins
* For reactive web apps: Integration with browser APIs, web-based widgets or toolkits, service workers, PWA features
* Social media integrations
* Payment gateway integrations

**Resource requirements:**

* External images, fonts, and media files
* Third-party JavaScript libraries
* External stylesheets
* Embedded content (iframes, videos)

Consider all services, plugins, and resources your app interacts with to ensure your CSP configuration allows necessary domains and protocols while maintaining security.

## Activate a CSP

The ODC Portal allows you to activate CSP per stage. By default, CSP directives are not activated, meaning that no security settings are configured. For example, no content or iframes will be blocked by default.

Once you activate your CSP, you can configure it as an **allow list**, permitting only the specified content in your apps while blocking all other sources by default.

### Prerequisites

You must have **CSP Management** permissions.  

### Activating a CSP {#activating-a-csp}

To activate a CSP for a stage, follow these steps:

1. From the ODC Portal, navigate to **Configure** > **Content security policy**.

1. Select the stage you want to apply the CSP to.

    ![Screenshot showing the selected stage to activate the CSP.](images/csp-stage-pl.png "Selected stage to activate the CSP")

1. Click **Edit**.

1. Toggle the **Status** to **Active** and click **Save**.

    The default directives are applied to all apps in the selected stage.

    ![Screenshot showing the CSP default values set to active.](images/csp-defaults-pl.png "CSP default values set to active")

    <div class="info" markdown="1">

    The total character limit for directive values per stage is 1500.

    </div>

## Configure a CSP

The ODC Portal allows you to configure a CSP's directive values. Customizing a CSP's default values is important because the default configuration may not align with your app's specific security needs, functionality, and architecture. For example, you can enable trusted third-party services such as YouTube or allow iframes for embedded content.

### Prerequisites

* You must have **CSP Management** permissions.

* You must have a [CSP activated.](#activating-a-csp)

### Configuring a CSP {#configuring-a-csp}

To configure the CSP, follow these steps:

1. From the ODC Portal, navigate to **Configure** > **Content security policy**

1. Click **Edit**.

    ![Screenshot showing the option to edit CSP settings.](images/csp-edit-pl.png "Edit CSP settings")

1. Edit the directive values.

    ![Screenshot showing the configuration of CSP directive values.](images/csp-configure-pl.png "Configure CSP directive values")

1. Click **Save**.

    The configured directive values are applied to all the apps in that stage.

    <div class="info" markdown="1">

    Some image file content configurations may take up to 24 hours to be applied or removed.

    </div>

You can reset the CSP's directive values to their default values at any time by clicking **Reset to defaults** and then **Save**.

## Default directives

The table below describes the list of default directives for OutSystem's content security policy. The [Default values](#default-values) column indicates the values that OutSystems automatically applies when you activate a content security policy. These defaults are set to be as restrictive as possible, maximizing security configuration while also enabling full app runtime functionality. You can customize these default values to suit your needs. For more details, refer to [Configure a CSP](#configuring-a-csp). Some default values cannot be removed; for more information, refer to the [required values](#required-values) section.

<div class="warning" markdown="1">

**Critical for iOS:** All domains in `connect-src` and other source directives must include the explicit `https://` protocol. Refer to [iOS specific configuration](./configure-csp.md#ios-specific-considerations) for details.

</div>

| Directive | Description | Default values |
| ------------- | ------------------------------------ | -------------- |
| base-uri | The domains that can be used as base URLs for app screens. The source expression ``'self'`` refers to the origin from which the protected document is being served, including the same URL scheme and port number. You must include the single quotes. Example: ``base-uri 'self';`` | ``'self'`` |
| connect-src | The domains from which apps are allowed to load resources using script interfaces.<br/> The ``*.amazonaws.com`` value is required when using ODC's built-in identity provider. <br/> The ``<yourBuiltInDomain-stage>.outsystems.app/identity`` value is required when using ODC's built-in identity provider and a custom domain. | ``'self'``<br/>  ``*.amazonaws.com``<br/>  ``<yourBuiltInDomain-stage>.outsystems.app/identity`` |
| default-src | The domains from which apps are allowed to load resources by default. Any resource type dedicated directive (such as ``object-src`` or ``img-src``) that's not defined will inherit this configuration. | ``'self'`` |
| font-src | The domains from which apps are allowed to load fonts. | ``'self'``<br/>``data:`` |
| frame-ancestors | The domains that are allowed to embed apps in a frame. | ``'self'`` |
| frame-src | The domains that are allowed to embed apps in a frame. | ``'self'`` |
| img-src | The domains from which apps are allowed to load images. | ``'self'``<br/> ``data:`` <br/> ``blob:`` |
| media-src | The domains from which apps are allowed to load media files. | ``'self'`` |
| object-src | The domains from which apps are allowed to load objects (for ``<object>``, ``<embed>`` and ``<applet>`` elements). | ``'self'`` |
| script-src | The domains from which apps are allowed to load scripts. | ``'self'``<br/> ``'unsafe-inline'``<br/>``'unsafe-eval'`` |
| style-src | The domains from which apps are allowed to load styles. | ``'self'``<br/> ``'unsafe-inline'`` |

## Default values {#default-values}

OutSystems recommends default values to ensure the platform works as expected. If these values are removed, OutSystems recommends you test your apps to ensure they work as expected.

* ``'self'``: Allows content to be loaded only from the same origin as the app. This helps prevent unauthorized content from being loaded.

* ``data``: Allows resources to be loaded, such as images and fonts, using data: URLs. This is often required for inline assets.

* ``blob``: Enables support for binary large object (blob) URLs, which are often used for dynamically generated media content and file downloads.

* ``*.amazonaws.com``: Allows access to AWS-hosted services, including the managed identity service necessary for authentication.

* ``<yourBuiltInDomain-stage>.outsystems.app/identity``: Ensures compatibility with the built-in identity service when using a custom domain. Only the built-in domain is preconfigured and does not require additional setup. All other domains, including custom domains or the built-in domain, must be explicitly configured.

## Required values {#required-values}

The **Required values** are the values that ODC automatically applies to the directive for the apps to work correctly. These values can be removed, but doing so may impact the functionality of your apps.

* ``unsafe-inline``: The unsafe-inline directive allows the use of inline resources such as inline ``<script>``and ``<style>`` elements, ``javascript: URLs``, and inline event handlers that are currently used by the platform.

* ``unsafe-eval``: The unsafe-eval directive allows the web pages to evaluate strings as code. This directive consists of the eval function, the function constructor, and some usages of the setTimeout and setInterval functions that are currently used by the platform.

For more details about the impacts of removing `unsafe-eval` and `unsafe-inline` directives, refer to [Impacts of removing unsafe directives](impacts-removing-unsafe-directives.md).

## Related resources

* [Impacts of removing unsafe directives](impacts-removing-unsafe-directives.md)

* [Login failed when logging into an app using iOS devices](https://success.outsystems.com/support/troubleshooting/incident_models/incident_models_outsystems_developer_cloud/login_failed_when_logging_into_an_app_using_ios_devices/)
  
* [Troubleshooting OutSystems apps on iOS devices](https://success.outsystems.com/support/enterprise_customers/troubleshooting/troubleshooting_outsystems_apps_on_ios_devices/)
