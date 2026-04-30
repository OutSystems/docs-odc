---
summary: Agentic development has constraints for both app generation in Mentor Web and app modification in Mentor Studio.
tags:
  - Agentic
  - AI
  - Mentor
  - Mentor Studio
  - Mentor Web
  - Troubleshooting
guid: 53247733-479b-4853-90a8-dd366ce0fba3
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - portal
  - odc studio
  - mentor web
  - mentor studio
coverage-type:
  - remember
  - understand
audience:
  - Front-end developer
  - Developer
topic:
  - creating-apps
isautopublish: true
---

# Known limitations

Agentic development is an emerging capability. Some limitations reflect the current state of AI code generation technology, which continues to evolve rapidly. Others are specific to how OutSystems has implemented AI assistance in ODC. As the technology matures and OutSystems refines its AI capabilities, OutSystems expects to address many of these limitations.

This page documents current constraints for both app generation and development in ODC Studio. Review these limitations alongside the capabilities for [Mentor Web](mentor-web/capabilities.md) and [Mentor Studio](mentor-studio/capabilities.md) when planning projects that use agentic development.

## App generation (Mentor Web)

The following limitations apply when creating new apps through Mentor Web.

### Session and conversation

Mentor Web does not persist conversations and work in progress automatically.

* **Session persistence.** Closing or refreshing the browser loses the conversation and blueprint. Save or publish work before closing.
* **Conversation length.** Mentor Web limits conversations to approximately 10 prompts. For longer sessions, publish the app and continue development in ODC Studio.

### Blueprint phase

You can configure some options only before generating the app for the first time.

* **Validation rules.** You can configure validation rules only before the first blueprint generation.
* **Theme configuration.** You can set or change the theme during the blueprint phase. After generation, theme changes require ODC Studio. The theme must have the layout block property set and include these placeholders: Header, Breadcrumbs, Title, Actions, and MainContent.

### Editor

After generation, Mentor Web restricts some modification capabilities in the editor.

* **Attribute renaming.** You cannot rename attributes in the editor.
* **Data type changes.** You cannot change attribute data types in the editor.
* **UI modifications.** UI changes are limited to adding or removing screens when the data model changes.

To discover available changes at any point, ask Mentor Web "What can I change through this conversational agent?"

## Development in ODC Studio (Mentor Studio)

The following limitations apply when modifying existing apps through Mentor Studio.

### Supported asset types

Mentor Studio supports a subset of OutSystems asset types.

* **Web apps only.** Mentor Studio supports web apps only. Build libraries, services, and mobile apps manually in ODC Studio.

### Scope of operations

Mentor Studio modifies app elements but does not perform environment-level operations.

* **App elements only.** Mentor Studio generates and modifies logic, UI, and data within the app. ODC Studio operations such as one-click publish, changing preferences, and managing dependencies are not supported through Mentor.

### Context awareness

Mentor Studio does not have full awareness of the current ODC Studio state.

* **No screen detection.** Mentor Studio does not detect the current screen view or active selection. Reference elements by name in prompts, such as "modify the ValidateEmail action" or "update the CustomerList screen."
* **Conversation length.** Long iterations may reach the maximum conversation length. Start a new conversation if responses become inconsistent.
* **No chat persistence.** Closing the app tab clears the conversation history.

### Dependencies

External elements require manual setup before Mentor Studio can use them.

* **Public elements.** Mentor Studio cannot add public elements directly. Add dependencies to the app first through **Manage Dependencies**, then ask Mentor to use them.

### Reliability

Mentor Studio can attempt any modification within a web app, but success varies by task complexity. Focused, atomic tasks, such as adding a single entity or creating a server action, tend to produce more consistent results than complex, multi-step changes. These limitations reflect the current state of AI code generation technology.

* **Success reporting.** Mentor Studio occasionally reports changes as successful even when not applied. Review affected elements in ODC Studio after each request to confirm changes.
* **Response latency.** Response times vary, even for straightforward tasks. Wait for Mentor Studio to finish before retrying the same request.
* **Apply errors.** "Failed to apply changes" errors occur in some cases, triggering repeated retries. If this happens, start a new conversation and rephrase the request.
* **Screen generation.** Screen generation and editing produces more errors than working with logic or data. Review screen changes carefully after each request.

## Related resources

These limitations reflect the current state of AI-assisted development and will evolve over time. For a broader view of what agentic development supports today, the following resources describe capabilities and workflows for each tool.

* For what Mentor Web generates, including supported UI patterns and dashboard types, refer to [Capabilities and patterns for Mentor Web](mentor-web/capabilities.md).
* For what Mentor Studio generates and modifies within existing apps, refer to [Capabilities and patterns for Mentor Studio](mentor-studio/capabilities.md).
* For Mentor Studio error codes and recommended actions, refer to [Mentor Studio errors](../../error/aisa/mentor-studio-errors.md).
* For an overview of both tools and guidance on when to use each, refer to [Introduction to agentic development](intro.md).
