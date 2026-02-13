---
summary: Enhance app security on OutSystems Developer Cloud (ODC) with Content Security Policy (CSP) to prevent XSS attacks and block unapproved resources.
tags: web security, content security policy, csp, mobile apps, odc
guid: fb46979d-73a3-43ad-9c85-a6b96381c2a6
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: 
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - odc portal
coverage-type:
  - understand
  - apply
---
# Content security policy

<div class="info" markdown="1">

CSP applies to all web and PWA apps. For mobile apps, CSP is enforced only in apps built with MABS 12 (released on February 13th, 2026) or later MABS version.

</div>

A content security policy (CSP) is a web security standard that helps protect your web, mobile, and progressive web apps (PWA) apps from various security threats, such as malicious code execution or the loading of untrusted content. By controlling which content sources browsers can load, CSP shields your app from malicious scripts, unapproved resources, and other security threats, ensuring its integrity and safety.

The benefits of a CSP include:

* **Prevents XSS attacks**: Stops unauthorized scripts from running and executing malicious actions.

* **Blocks malicious resources**: Restricts the loading of unapproved images, plugins, or frames, reducing exposure to harmful content.

* **Strengthens app security**: Reduces vulnerabilities and protects your app's integrity by enforcing stricter content loading policies.

To [implement a CSP](implement-csp.md), you define a policy in HTTP headers, set explicit content rules that browsers enforce, and reduce points of vulnerability. For example, the `script-src` directive controls where JavaScript can load from, and browsers block any content that doesn't comply with the policy.

## Understanding CSP in mobile apps

ODC mobile apps are hybrid apps that combine web technologies with native capabilities. Hybrid apps use WebView components that function like embedded web browsers. Hybrid mobile apps are vulnerable to web-based attacks because WebView components can load and execute content similar to regular web browsers. CSP provides an additional security layer by restricting which scripts can run and which external sources can load content, protecting against cross-site scripting (XSS) attacks and unauthorized resource loading.

<div class="info" markdown="1">

You activate or deactivate CSP at the stage level, not per individual mobile app.

</div>

### How CSP is implemented in ODC mobile apps

ODC mobile apps enforce CSP by using a native caching system that delivers CSP settings to the WebView through HTTP headers. When you activate, update, or deactivate a CSP, the policy changes automatically apply to all mobile apps without requiring a new build. However, the updates may not take effect immediately, as each mobile app picks up the new CSP status the next time it contacts the server.

When you generate a mobile app with CSP activated, the current policies are bundled with the app package and used as a fallback if the app launches offline immediately after installation. If you update the CSP later, the bundled fallback policy drifts from the current policy. However, once the app launches online again, the updated CSP changes are fetched immediately.

The process that retrieves and saves the new CSP runs at launch but does not block the app from loading. As a result, the process may finish later depending on factors such as network speed or system load. The updated CSP therefore only takes effect the next time the app is launched.

## iOS specific considerations

iOS native mobile apps have unique CSP requirements due to how iOS handles content loading in WebViews.

iOS loads content in native mobile apps using the `outsystems://` protocol instead of the standard `https://` protocol. This creates a CSP validation issue:

Without the `https://` protocol, iOS attempts to match `outsystems://*.amazonaws.com` which
does not match your intended resource: `https://*.amazonaws.com`. Therefore CSP blocks the resource, causing failures.

With the `https://` protocol, CSP allows `https://*.amazonaws.com` and iOS correctly translates this for validation. Therefore, the resources load successfully

For detailed troubleshooting, refer to [Login failed when logging into an app using iOS devices](https://success.outsystems.com/support/troubleshooting/incident_models/incident_models_outsystems_developer_cloud/login_failed_when_logging_into_an_app_using_ios_devices/)

### Required configuration for iOS

For all external domains in the following directives, always include the explicit `https://` protocol:

* `connect-src`
* `script-src`
* `style-src`
* `img-src`
* `font-src`
* `media-src`

### iOS configuration examples

Incorrect configuration (causes iOS failures):

```
connect-src: 'self' *.amazonaws.com [your-domain].outsystems.app/identity
img-src: 'self' data: blob: cdn.example.com
script-src: 'self' 'unsafe-inline' 'unsafe-eval' maps.googleapis.com
```

Correct configuration (works on iOS and Android):

```
connect-src: 'self' https://*.amazonaws.com https://[your-domain].outsystems.app/identity
img-src: 'self' data: blob: https://cdn.example.com
script-src: 'self' 'unsafe-inline' 'unsafe-eval' https://maps.googleapis.com
```

### Using iframes in iOS apps

If you want to use both CSP directives and iframes in your iOS apps, add the following to the **frame-ancestors** directive field:

```
    outsystems://YOUR_APP_URL
    https://YOUR_APP_URL

```

Failure to do so prevents content from rendering. You can identify the issue by searching for the **Interrupting main resource load due to CSP frame-ancestors or X-Frame-Options** error log.

For additional information about using iframes in iOS devices, refer to [Troubleshooting OutSystems apps on iOS devices](https://success.outsystems.com/support/enterprise_customers/troubleshooting/troubleshooting_outsystems_apps_on_ios_devices/)

## Operational and security considerations

Operational and security considerations are crucial when implementing a CSP. A poorly configured CSP can break functionality, while a weak one provides inadequate protection. Therefore, careful planning and testing are essential. When configuring a CSP, take the following risks of misconfiguration into account:

* **Missing policies**: Ensure you configure policies that allow all sources used in your apps. Otherwise, users may have issues such as videos not showing or CSS not being applied.

* **Too permissive policies**: Be cautious when allowing resources to be loaded from everywhere (by using ``\*`` in the domain list). Hackers may use links, scripts, or other resources in your apps to redirect users to malicious pages.

**Protocol requirement:** Always use explicit `https://` protocols in all CSP directive domains to ensure your apps work correctly across iOS and Android.

**Directive length limit:** Each stage can have a maximum of 1500 characters for all directive values combined.

## Related resources

* [Implement content security policy](implement-csp.md)
  
* [Impacts of removing unsafe directives](impacts-removing-unsafe-directives.md)
