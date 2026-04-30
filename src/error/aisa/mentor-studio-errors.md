---
summary: Explore common Mentor Studio errors in OutSystems Developer Cloud (ODC) and their solutions.
tags:
  - Agentic
  - AI
  - Mentor
  - Mentor Studio
  - Troubleshooting
guid: 47a11d41-8a0d-48e5-8e70-14578fcf6f85
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - mentor studio
coverage-type:
  - apply
  - unblock
isautopublish: true
---

# Mentor Studio errors

Mentor Studio brings conversational AI into ODC Studio. You describe goals in natural language, and Mentor analyzes the app model, plans the change, and applies it after you review the implementation plan. The errors on these pages cover failures across the Mentor Studio service, the AI Provider service that powers it, and the conversation state that tracks each session.

For a feature overview, refer to [AI development in Mentor Studio](../../eap/agentic-development/mentor-studio/how-it-works.md). For the modification flow these errors apply to, refer to [Architecture](../../eap/agentic-development/architecture.md).

## Error sources

The error codes group into three categories based on where the failure occurs.

* **Mentor Studio service.** Errors during connection setup, request processing, or app model retrieval.
* **AI Provider service.** Errors from the underlying language model service, including rate limits, usage caps, and upstream outages.
* **Conversation state.** Errors that result from the dialog reaching a limit or transitioning into an unsupported state.

Use the error code to locate the error message. Then use the information to understand the cause and impact. To resolve the error, follow the recommended action.
