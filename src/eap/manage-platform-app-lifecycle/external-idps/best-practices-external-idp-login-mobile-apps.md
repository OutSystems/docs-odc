---
guid: 43fe4180-d4a9-4194-8bd2-5d4e166ff6ed
locale: en-us
summary: Secure mobile IdP authentication on OutSystems Developer Cloud (ODC) using OAuth 2.0 best practices with Android Custom Tabs and iOS ASWebAuthenticationSession.
figma:
coverage-type:
  - evaluate
  - unblock
topic:
  - lockout
app_type: mobile apps
platform-version: odc
audience:
  - Developer
tags:
  - Authentication
  - Best Practices
  - External Authentication
  - IdP
  - Mobile app
  - OAuth
  - Security
outsystems-tools:
  - odc portal
helpids:
isautopublish: true
---
# Best Practices for external identity provider login in mobile apps

When configuring external Identity Provider(IdP) authentication within mobile applications, the platform relies on secure, system-level mechanisms rather than internal web views. The architecture explicitly uses native operating system containers to safely process logins. Understanding these mechanisms and avoiding common anti-patterns is essential for ensuring reliable authentication and preventing session failures.

## Secure core architecture and framework design

When configuring external Identity Provider (IdP) authentication within mobile applications, relying on internal or generic web views exposes the application to security vulnerabilities and disregards modern mobile security standards.

### Recommendations

Design the application's core architecture to explicitly use native operating system containers rather than generic browser plugins. Ensure implementation choices align with the industry-standard security practices established in OAuth 2.0 for native apps by utilizing the following native mechanisms:

* **Android Environments**: Natively utilize Android Custom Tabs to launch and manage the authentication redirect flow.  

* **iOS Environments**: Natively utilize `ASWebAuthenticationSession` to process secure login sessions.

Do not use the standard `InAppBrowser` plugin for this task, as it is intended for generic application web views rather than isolated system authentication frames.  

### Benefits

Using sandboxed native operating system containers isolates the authentication layer from the main application.

This prevents hostile credential interception, satisfies strict enterprise compliance frameworks (RFC 8252), and allows the app to leverage system-level session persistence safely.

## Avoid the OpenInWebView anti-pattern

Developers frequently make the mistake of intercepting the External Login URL and passing it into the `OpenInWebView` client action of the `InAppBrowser` plugin. This workaround is often chosen to suppress the browser's user interface components or to hide device-level deep-link confirmation screens.

### Recommendations

Allow standard redirect nodes to execute naturally rather than forcing workflows through application-level plugins.

External login sequences require explicit client-side handling to properly engage native operating system APIs. Bypassing this initialization breaks standard authentication handshakes.

### Benefits

Avoiding `OpenInWebView` ensures that crucial built-in safety wrappers are preserved, maintaining session persistence and preventing critical runtime crashes during the login loop.

## Troubleshoot the "page expired" failure loop

Wrapping the login sequence in custom web views instead of using the native architecture causes a session management failure. Because the app lacks native orchestration, it fires multiple login requests back-to-back.

When the backend receives these duplicate requests, it opens a brand-new session and automatically kills the first one to prevent security risks (session fixation). When the external IdP finishes checking the user and sends the login token back to that first, dead session, the system rejects it, causing the app to crash and show the error: "_This page expired. You've been inactive for a while. Reload the page to continue._"

### Recommendations

To prevent duplicate processing and ensure correct session initialization, implement a two-step native handover flow:

1. **Dynamically Fetch Endpoints**: Always obtain the target redirection URLs by calling the platform's built-in `GetExternalLoginURL` or `GetExternalLogoutURL` actions.  

1. **Execute a Native Handover**: Pass that dynamically generated URL directly into a standard _RedirectToURL_ node. This ensures the application runtime correctly transfers control over to the secure system frame.  

### Benefits

Implementing the proper native redirection handles token exchange sequentially. This prevents session de-synchronization, eliminates duplicate client-side requests, and completely resolves the "_Page Expired_" state crash.

## Understand native OS limitations and expected behaviors

Enterprise application deployments governed by strict device policies often require absolute control over visual elements. However, certain authentication elements are dictated entirely by the mobile operating system container and cannot be modified, customized, or programmatically hidden via application code.  

### Recommendations

Development teams and stakeholders must accept that certain user experience (UX) elements are controlled entirely by the mobile operating system and cannot be customized or hidden by application code. These include:

* **Visible Browser Elements**: Because the application relies on native system containers, the login screen displays the default device browser's top navigation bar, application URL, and share shortcuts (e.g., "Open in Chrome").

* **Deep-Link Confirmation Dialogs**: When the external IdP routes back to the app via a secure deep link, the underlying operating system (especially on Android) may display an unchangeable pop-up asking the user to confirm the application switch.

### Benefits

Accepting these platform boundaries saves development time that would otherwise be wasted attempting to customize unchangeable security layers. It also ensures that applications do not break or get rejected during app store reviews for violating native mobile sandbox behaviors.
