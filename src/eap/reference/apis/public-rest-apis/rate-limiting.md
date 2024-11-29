---
summary: This article describes the rate limiting information for ODC REST APIs. 
tags: 
guid: 00b00239-a7db-4759-be9c-47c3d59255fb
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: 
outsystems-tools: 
content-type: 
    - best practice
    - conceptual
audience: 
---

# Rate limits for the APIs

Rate limiting is a mechanism used to control the number of API requests a user, application, or IP address can make within a defined period. This helps prevent system overload, ensures fair resource distribution, and safeguards against malicious activities like denial-of-service (DoS) attacks.

The global rate limit per organization per domain is as follows:

|API domain|Rate limit|
|-----------|----------|
|User and access management|100 requests per minute|
|Portfolio management|100 requests per minute|

The rate limit for the [Bulk create](../identity-v1.md#post-/identity/v1/users/bulk) API is **5 requests per minute**. 

## Exceeding the rate limit

If you exceed the rate limit, you will receive an output `429 Too Many Requests response` along with a `x-envoy-ratelimited: true response header`. 
















