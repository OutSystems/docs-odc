---
summary: Use AI companion tools to enhance your workflow with Mentor, including an interactive prompt coach and a requirement document generator.
tags: ai tools, prompt engineering, requirement documents, gemini gem, ai assistants
guid: 3e8f9a2b-4c5d-6e7f-8a9b-0c1d2e3f4a5b
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - portal
  - ai mentor
coverage-type:
  - understand
  - apply
audience:
  - frontend developers
  - backend developers
  - full stack developers
  - ui designers
topic:
  - creating-apps
---

# AI tools for working with Mentor

Two AI companion tools provide interactive guidance for working with Mentor:

* **OutSystems Mentor prompt coach**: A Google Gemini Gem that answers questions about prompting techniques, requirement documents, and Mentor capabilities.
* **Requirement document generator**: A prompt template that transforms meeting notes, user stories, and other artifacts into structured requirement documents.

<div class="info" markdown="1">

If you have feedback or ideas, submit them in the feedback box on this page.

</div>

## OutSystems Mentor prompt coach

The OutSystems Mentor prompt coach is a Google Gemini Gem trained on the complete Mentor documentation. It answers questions, provides guidance, and suggests improvements for prompts and requirement documents.

### Access the prompt coach

Using the prompt coach requires a Google account and signing in to Google Gemini.

Access the [OutSystems Mentor prompt coach](https://gemini.google.com/gem/1tI9yvDyJwt6-CNdfPD-i1Fgt9hqsCOTg).

### Capabilities

The following table describes topics the prompt coach can assist with.

| Topic | How it helps |
| ------- | -------------- |
| Prompting techniques | Suggests how to phrase prompts for specific UI patterns, data models, and roles based on Mentor's recognized patterns |
| Requirement documents | Guides you through structuring requirements for complex apps, explaining what to include and how to format sections |
| Mentor capabilities | Explains what Mentor can generate and its current limitations, helping you understand when to use Mentor versus ODC Studio |
| Troubleshooting | Helps diagnose why Mentor might not interpret your requirements as expected and suggests ways to improve your prompts |
| Best practices | Provides tips for the generate-review-refine workflow and helps you iterate more effectively |

### Example use cases

The following examples show common ways to use the prompt coach:

* **Learning prompt patterns**: Ask "How do I create a master-detail layout for customer records?" to get specific guidance on phrasing your prompt
* **Structuring requirements**: Share your app concept and ask for help organizing it into a requirement document structure
* **Understanding constraints**: Ask "Why can't I use a popup pattern for this entity?" to understand Mentor's pattern limitations
* **Refining prompts**: Paste a prompt that didn't work as expected and ask for suggestions on how to improve it

## Requirement document generator

The requirement document generator is a prompt template that transforms raw artifacts into well-structured requirement documents optimized for Mentor.

### When to use it

The generator converts informal documentation into Mentor-ready requirement documents. Use it when you have:

* Meeting transcripts or notes from requirements gathering sessions
* Existing requirement documents that need restructuring
* User stories or technical specifications
* Business process descriptions or wireframes

### How to use it

Using the generator requires access to an AI assistant such as Claude, ChatGPT, or Gemini.

To generate a requirement document:

1. Download the [requirement document generator prompt](resources/mentor-prompt-generator.txt).
1. Copy the entire prompt into your AI assistant.
1. Replace the placeholder text at the end of the prompt with your raw artifacts (meeting notes, transcripts, user stories).
1. Review and refine the generated document before uploading to Mentor.

The output follows Mentor's best practices, including proper data types, entity relationships, roles and permissions, and screen specifications.

### What it generates

The generator creates structured documents with the following sections:

* **App overview**: Description of purpose, goals, and key users
* **Data model**: Entities with data types, relationships, and static entities
* **Roles and permissions**: Entity-level and row-level access control specifications
* **Main features and screens**: Screen types, patterns, and business logic requirements
* **Dashboards**: Counter and chart specifications when applicable
* **External integrations**: Integration requirements when specified

The output follows the structure recommended in [Use requirement documents](requirements-doc.md) and can be uploaded to Mentor as `.txt` or `.docx` files.

## Related resources

The following resources provide additional guidance for working with Mentor:

* [Prompting guide](prompts.md): Proven patterns for different UI layouts and data structures
* [Use requirement documents](requirements-doc.md): How to structure requirement documents for Mentor
