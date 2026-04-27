---
summary: Effective prompting strategies help Mentor generate and modify apps accurately across Mentor Web and Mentor Studio.
tags: prompts, agentic development, best practices
guid: d7c3bf86-c4be-439e-b61a-bd413fba3c8e
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
  - understand
  - apply
audience:
  - Front-end developer
  - Developer
isautopublish: true
---

# Effective prompts for Mentor

Prompting is a skill that improves with practice. The way you phrase a request directly affects what the Mentor tools in ODC generate: vague prompts produce generic results, while specific prompts produce targeted outcomes.

These strategies apply whether you're creating apps in Portal or modifying them in ODC Studio. The principles are the same: state your goal clearly, provide relevant context, and be specific about what you want.

<div class="info" markdown="1">

Mentor is designed to support English. You can enter prompts in other languages, but English is recommended.

</div>

## What is prompting

A prompt is a natural language instruction that tells an AI system what to do. Unlike traditional interfaces where you click buttons and fill forms, prompting requires you to describe your intent in words. The AI interprets your description and generates a response.

Prompting shifts the interaction model from "select from options" to "describe what you want." This shift requires a different mindset, explored in [Thinking with AI](thinking-with-ai.md): instead of navigating menus, you communicate goals. The quality of your description directly determines the quality of the output.

Mentor interprets prompts literally and matches them against patterns it recognizes. It doesn't read between the lines or infer unstated requirements. If you omit information, Mentor fills gaps with defaults or makes assumptions. Understanding this behavior helps you write prompts that produce predictable results.

## Writing clear prompts

Effective prompts share common characteristics: they're specific, structured, and provide enough context for Mentor to act without guessing. When Mentor has to infer missing details, it makes assumptions that may not match your intent. The following practices help you communicate requirements precisely.

* **Be clear and concise.** Include the app name, purpose, and main functionality in one to two sentences.
* **Structure information logically.** Group related details together. Mention entities, then attributes, then relationships.
* **Add role-specific details.** Mention roles and permissions when relevant to the task.
* **Be specific, avoid ambiguity.** Instead of "make it better," specify "add email validation to the contact form."

<div class="warning" markdown="1">

Don't include personally identifiable information (PII) in prompts or requirement documents. Use placeholder or fictional data instead of real names, email addresses, phone numbers, or other sensitive data.

</div>

## Prompt structure

A well-structured prompt follows a pattern: state the goal, provide context, then specify details. This ordering helps Mentor prioritize information correctly.

| Element | Description | Example |
| --------- | ------------- | --------- |
| **Goal** | Start with what you want to accomplish. Mentor uses this to frame the entire response. | "Create an Inventory Management app" |
| **Context** | Mention relevant entities, attributes, or existing elements that Mentor should consider. | "to track Products (Name, SKU, Stock, Price) and Orders (OrderID, Product, Quantity, Status)" |
| **Details** | Add specifics like field names, validation rules, or UI preferences. | "Managers can view stock. Administrators can update inventory. Use the 'Professional' theme." |

### Prompt structure example

The following prompt combines all three elements into a single request:

"Create an Inventory Management app to track Products (Name, SKU, Stock, Price) and Orders (OrderID, Product, Quantity, Status). Managers can view stock. Administrators can update inventory. Use the 'Professional' theme."

## Iterative refinement

Complex apps emerge through iteration, not a single prompt. Trying to specify everything up front often leads to overstuffed prompts that Mentor struggles to interpret. Instead, start with a broad description and refine incrementally. Each prompt builds on the previous result.

* **Start broad.** Describe the overall app concept first. Let Mentor generate a foundation with the core data model, main screens, and basic roles.
* **Refine in small steps.** Add one feature or adjustment per prompt rather than combining multiple changes.
* **Rephrase as additions.** Mentor handles additions well. To modify existing elements, describe what to add rather than what to change.
* **Know when to start fresh.** If responses become inconsistent after many iterations, start a new conversation.

## Entity-first thinking

Mentor builds apps from the data model outward. Screens, permissions, and logic all derive from entities and their relationships. When you describe entities clearly, Mentor infers appropriate screens and patterns. When you describe screens without entities, Mentor has to guess the underlying data structure.

To apply entity-first thinking, structure your prompts in this order:

1. Define what entities exist and their attributes.
1. Describe how entities relate to each other.
1. Layer on screens, roles, and behaviors.

This ordering mirrors how Mentor processes requests internally.

Example: "Track Products (Name, SKU, Price, Stock) and Orders (OrderID, Customer, Status). Each Order contains multiple Products." This gives Mentor a clear foundation before you mention dashboards or card lists.

## Decomposition

Complex requirements become clearer when broken into focused requests. Instead of describing an entire app in one prompt, separate concerns: data model first, then screens, then permissions, then refinements. Each prompt addresses one aspect.

Decomposition reduces the chance of conflicting instructions and makes it easier to identify what went wrong when results don't match expectations. If a single prompt produces unexpected results, you can isolate which part caused the issue.

For complex apps, consider this sequence:

1. Describe the core data model and relationships
1. Request specific screen patterns for key entities
1. Define roles and permissions
1. Add refinements like validation rules or styling

## Prompts vs requirement documents

Prompts and requirement documents are two ways to communicate intent to Mentor. The same principles apply to both: entity-first thinking, specificity, and pattern vocabulary all improve results regardless of format.

The difference is scale:

* **Prompts** work well for simple apps or incremental refinement.
* **Requirement documents** work better for complex apps where you know the full scope up front.

A requirement document is a pre-decomposed prompt: its sections (app overview, data model, roles, screens) mirror the decomposition sequence recommended for complex prompts.

For guidance on structuring requirement documents, refer to [Use requirement documents](mentor-web/requirements-doc.md).

## Pattern vocabulary

Mentor recognizes specific keywords that trigger particular UI patterns and behaviors. Using these keywords explicitly produces more predictable results than generic descriptions.

* **Layout patterns**: table, card list, gallery, master detail, dashboard, popup, accordion, sidebar
* **Dashboard elements**: counter, chart, bar chart, pie chart, donut chart, line chart
* **Data operations**: add entity, delete attribute, add role, edit permissions
* **Relationships**: one-to-many, many-to-many, foreign key

When you use pattern vocabulary, Mentor maps your request directly to known implementations. When you use generic descriptions like "show the data nicely," Mentor must interpret your intent and choose a pattern on your behalf.

## Common mistakes

Certain prompting patterns consistently produce poor results. Recognizing these patterns helps you avoid them. If Mentor's output doesn't match your expectations, check whether your prompt falls into one of these categories.

* **Vague language.** Prompts like "make the app better" or "improve the UI" give Mentor no direction.
* **Overstuffed prompts.** Combining too many requirements in one prompt increases the chance of misinterpretation. Use [decomposition](#decomposition) to break complex requests into focused steps.
* **Missing context.** Referring to "the entity" or "that screen" without naming it forces Mentor to guess.
* **Conflicting instructions.** Requesting a popup for an entity with 10 attributes contradicts pattern constraints.

## Platform-specific guidance

The strategies on this page apply to all Mentor interactions. However, each tool has its own patterns and capabilities that affect what you can request and how you phrase it. The following resources provide prompt examples specific to each platform.

* **Mentor Web**: For UI pattern prompts and app generation examples, refer to [Prompts for Mentor Web](mentor-web/prompts.md).
* **Mentor Studio**: For logic and modification prompts, refer to [Prompts for Mentor Studio](mentor-studio/prompts.md).
