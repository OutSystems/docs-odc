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

API rate limits work at two levels:

* **Domain-wide limits**: All requests to endpoints within an API domain share a total request pool per minute.
* **Specific endpoint limits**: Some endpoints have individual limits, but these requests still count toward the domain-wide limit.

The rate limits per organization are as follows:

| API Domain | Domain-wide limit (requests per minute) | Specific endpoint limits (requests per minute) |
| :--- | :--- | :--- |
| [User and access management](../identity-v1.md) | 100 | `POST /users/bulk`: **5** |
| [Portfolio](../portfolio-v1.md) | 100 | None |
| [Build Operations](https://www.outsystems.com/tk/redirect?g=a359bc7f-74a0-4723-9f13-ca851718dc89) | 100 | `POST` methods: **10** (per endpoint) |
| [Deployments](https://www.outsystems.com/tk/redirect?g=acf7cd06-3fe1-4bd3-85e8-06cd11aa0a7d) | 100 | `POST` methods: **10** (per endpoint) |
| [Asset Repository](https://www.outsystems.com/tk/redirect?g=9598cb1d-a50e-48d7-a43a-6582e43fd48b) | 100 | `POST /assets`: **10** |
| [Asset Configurations](https://www.outsystems.com/tk/redirect?g=cb142916-250b-42b9-a983-7ccdaa028480) | 100 | None |
| [Dependency Management](https://www.outsystems.com/tk/redirect?g=8a687cef-649f-4387-85e3-027954ac92cf) | 100 | None |
| [External Library Generation](https://www.outsystems.com/tk/redirect?g=47875596-0618-4d20-824a-fbbaea2d353b) | 100 | `POST` methods: **10** (per endpoint) |

## Exceeding the rate limit

If you exceed the rate limit, you will receive an output `429 Too Many Requests` response.
