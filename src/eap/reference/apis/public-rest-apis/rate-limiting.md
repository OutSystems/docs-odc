---
summary: This article describes the rate limiting information for ODC REST APIs.
tags: rate limiting, apis, rest api, best practices, outsystems
guid: 00b00239-a7db-4759-be9c-47c3d59255fb
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - none
content-type:
  - best practice
  - conceptual
audience:
  - backend developers
  - platform administrators
---

# Rate limits for the APIs

The global rate limit per organization per domain is as follows:

|API domain|Rate limit|
|-----------|----------|
|User and access management|100 requests per minute|
|Portfolio management|100 requests per minute|

The rate limit for the [Bulk user create](../identity-v1.md#post-/identity/v1/users/bulk) API is **5 requests per minute**. 

## Exceeding the rate limit

If you exceed the rate limit, you will receive an output `429 Too Many Requests` response.
















