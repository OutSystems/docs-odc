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

The rate limit per organization per API domain is as follows:

| API | Rate Limit (requests per minute) | Notes |
| :--- | :--- | :--- |
| [User and access management](../identity-v1.md) | 100 | Exception: `POST /users/bulk` has a rate limit of **5** requests per minute|
| [Portfolio](../portfolio-v1.md) | 100 | |
| [Build Operations](https://www.outsystems.com/tk/redirect?g=a359bc7f-74a0-4723-9f13-ca851718dc89) | 100 | Exception: `POST /build-operations` has a rate limit of **10** requests per minute |
| [Deployments](https://www.outsystems.com/tk/redirect?g=acf7cd06-3fe1-4bd3-85e8-06cd11aa0a7d) | 100 | Exception: `POST /deployment-operations` and `POST /publish-operations` have a rate limit of **10** requests per minute|
| [Asset Repository](https://www.outsystems.com/tk/redirect?g=9598cb1d-a50e-48d7-a43a-6582e43fd48b) | 100 | Exception: `POST /assets` has a rate limit of **10** requests per minute |
| [Asset Configurations](https://www.outsystems.com/tk/redirect?g=cb142916-250b-42b9-a983-7ccdaa028480) | 100 | |
| [Dependency Management](https://www.outsystems.com/tk/redirect?g=8a687cef-649f-4387-85e3-027954ac92cf) | 100 | |

## Exceeding the rate limit

If you exceed the rate limit, you will receive an output `429 Too Many Requests` response.