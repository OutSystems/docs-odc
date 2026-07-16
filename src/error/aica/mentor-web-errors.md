---
summary: Explore common Mentor Web errors in OutSystems Developer Cloud (ODC) and their solutions.
tags:
  - Agentic
  - AI
  - Mentor
  - Mentor Web
  - Troubleshooting
guid: bfb13f74-a224-4b19-a4da-85d23d41f7e7
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - mentor web
coverage-type:
  - apply
  - unblock
isautopublish: true
---

# Mentor Web errors

Mentor Web turns natural language prompts into working apps in ODC Portal, and stays available to refine the app after generation. The errors on these pages cover three areas: failures during generation and refinement, errors in the AI Provider service that powers Mentor Web, and a generic platform error.

For a feature overview, refer to [AI development in Mentor Web](../../eap/agentic-development/mentor-web/how-it-works.md). For the generation flow these errors apply to, refer to [Architecture](../../eap/agentic-development/architecture.md).

## Error sources

The error codes group into two categories based on where the failure occurs.

* **Generation and refinement.** Errors while Mentor Web processes a prompt, tracks conversation state, or calls the underlying AI provider, including rate limits, usage caps, and upstream outages.
* **Platform.** A generic error returned when an unexpected problem occurs elsewhere in the platform while you're using Mentor Web.

Use the error code to locate the error message. Then use the information to understand the cause and impact. To resolve the error, follow the recommended action.
