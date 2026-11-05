---
guid: 993a13a9-9cbe-4bd5-8109-788c93c10ffb
locale: en-us
summary: ODC signed URLs grant time-limited file access in cloud storage; use GetFileSignedURL, set a short TTL, and follow safe-usage rules to prevent leaks.
figma:
coverage-type:
  - understand
  - apply
  - evaluate
topic:
  - expired-signed-url-idle-screens
  - generate-signed-urls
  - signed-url-safe-usage
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - Architect
  - Front-end developer
  - Developer
  - Tech lead
tags:
  - Authorization
  - Best Practices
  - Security
outsystems-tools:
  - odc studio
helpids:
isautopublish: true
---

# File access and signed URLs

When a user views or downloads a file, ODC delivers the content directly from cloud storage to the browser, without routing the bytes through the application server. This keeps the application server free for business logic and removes the size constraints that apply to application-handled binary transfers.

Direct delivery from cloud storage requires a controlled access mechanism. Raw storage paths provide unrestricted, permanent access to anyone who discovers them. Signed URLs solve this: a signed URL grants access to a specific file for a limited time. When the URL expires, access is revoked automatically.

This article explains how signed URLs work, how to generate them in your app, and the rules for using them safely.

For background on the **File** type and how it differs from **BinaryData**, refer to [The File data type](binaries-native-cloud.md).

## What a signed URL is

A signed URL is a URL with an access grant embedded in its query string. The grant encodes two things: the specific file the URL is valid for and an expiry time. Anyone who holds the URL can fetch the file directly from cloud storage without presenting credentials.

This makes a signed URL a bearer token. ODC does not check the identity of the caller when the URL is used. ODC checks only that the URL has not expired and that it matches the resource it was issued for.

## How ODC issues signed URLs

ODC provides two server actions for generating signed URLs: **GetFileSignedURL** generates a URL for one file, and **GetMultipleFilesSignedURLs** generates URLs for several files in a single call.

Use **GetMultipleFilesSignedURLs** when your screen renders a collection of files or images returned by an aggregate.

For the inputs and outputs of both actions, refer to [File system actions](../../../reference/system-actions/file.md).

A signed URL works for a file that another app in the same environment owns. Files from the same environment are shared between its apps for reading and downloading. To keep such a file, copy it into your app before you store it in an entity. For more information, refer to the [CopyFile](../../../reference/system-actions/file.md#copyfile) server action.

### Set the Content-Disposition header safely

The **ContentDisposition** value of the **ResponseHeaders** input is sent to the client as an HTTP response header. When you build the value from data that users supply, such as a file name, a crafted value can inject extra header content. Encode the file name before you add it to the value, and use the `filename*=UTF-8''` form:

```
"attachment; filename*=UTF-8''" + EncodeUrl(FileName)
```

Don't concatenate a raw file name into the value. A fixed value, such as `"attachment; filename=""report.pdf"""`, is safe because no user data is involved.

### Time to live { #ttl }

The TTL (time-to-live) controls how long a signed URL stays valid after it is issued. Set the **URLExpiration** input of **GetFileSignedURL** or **GetMultipleFilesSignedURLs** to configure it.

* **Default:** 30 minutes
* **Maximum:** 48 hours

ODC enforces the 48-hour maximum at runtime, when **URLExpiration** is evaluated, not when you publish your app. Because **URLExpiration** can be an expression instead of a constant, ODC can't validate it at publish time. A call with a **URLExpiration** value above 48 hours fails at runtime instead.

Use the shortest TTL that satisfies your use case. Longer TTLs widen the exposure window if a URL is leaked.

<div class="info" markdown="1">

A signed URL contains these components:

* **File path**: the absolute path to the file in cloud storage
* **Policy**: a base64-encoded value that specifies the resource and the expiry time
* **Signature**: a cryptographic signature over the policy
* **Key-Pair-Id**: identifies the key used to produce the signature
* **Response header overrides**: optional query string values that control the response headers, corresponding to the **ResponseHeaders** input of **GetFileSignedURL**

The delivery layer validates the Signature and the Policy on every request. The Policy enforces two conditions: the resource and the expiry time. The delivery layer does not validate request headers such as `Range`, `Authorization`, and `Content-Type`. The client controls those.

</div>

## Safe-usage rules

Because a signed URL grants access to anyone who holds it, follow these rules whenever you work with signed URLs.

* **Generate on demand**: generate a signed URL immediately before the client needs it. Do not generate URLs in advance and store them.
* **Use immediately**: pass the URL directly to the client in the same user interaction. Do not store it in a variable, a database column, or a cache entry.
* **Never reuse**: each client interaction should produce a fresh URL. A URL from a previous interaction has likely expired, and a URL stored in a log or a clipboard is accessible to anyone who reads it.
* **Keep TTLs short**: a leaked URL is accessible for the duration of its TTL. Use 30 minutes for most interactive use cases. Use a longer TTL only when the client needs extended access and the wider exposure window is acceptable.
* **Do not share signed URLs**: a signed URL is for a single user interaction. Sending it in an email, a message, or a document grants file access to anyone who receives it, for the lifetime of the TTL.

<div class="info" markdown="1">

ODC does not verify the identity of the caller when a signed URL is used. Any party that holds the URL can access the file until it expires.

</div>

## Idle screens and expired URLs

If a screen displays a file loaded from a signed URL and the user leaves the screen idle past the URL's TTL, requests for that file fail silently. Because the browser fetches the file directly from cloud storage instead of through an ODC server action, this failure doesn't surface an ODC error code or **ErrorMessage** your app logic can check.

To prevent this, don't rely on a signed URL generated once when the screen loads for content the user might view after being idle. Call **GetFileSignedURL** again to generate a fresh URL when the user resumes interacting with the screen, or right before the file is needed, and rebind the file source to the new URL.
