---
summary: Learn how Mentor transforms requirements into apps through a three-stage process of interpretation, model generation, and compilation.
tags: app generation, mentor workflow, model-driven development, prompt engineering, ai-assisted development
guid: 8f4a2e1d-9b7c-4a3f-8d6e-5c9f3a2b1e0d
locale: en-us
app_type: reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=8589-38
outsystems-tools:
  - portal
  - ai mentor
coverage-type:
  - understand
audience:
  - frontend developers
  - backend developers
  - full stack developers
  - ui designers
topic:
  - creating-apps
---

# How Mentor works

Mentor uses AI to transform natural language into working apps. You describe what you need, and Mentor generates the data model, screens, and permissions—handling the foundational setup so you can focus on refining the details.

For example, when you describe a customer management app where managers can edit records and sales reps can only view, Mentor interprets those requirements, identifies the entities and roles, and generates a working foundation. Each step  from your description to the deployable app follows a consistent process.

The following sections explain that process, helping you understand what Mentor produces and how to guide it toward better results.

![How Mentor works](images/mentor-architecture-diag.png "The diagram shows how Mentor works and how it integrates with OutSystems Model and ODC Studio")

## Choose an input method

Mentor offers two input methods for different scenarios:

* **Prompts**: Natural language descriptions for rapid generation and iterative changes. Use prompts when starting simple apps or making incremental modifications to existing apps. To learn how to write prompts, see the [Prompts cookbook](prompts.md).
* **Requirement documents**: Structured documents that serve as a detailed blueprint. Use requirement documents for complex apps with defined data models, specific roles and permissions, and detailed screen requirements. For details, see [Use requirement documents](requirements-doc.md).

Both input methods support a "generate and refine" workflow. Start with an initial generation, then iterate using the App Editor.

## Generation process

Regardless of the input method, Mentor follows the same process:

1. **Input interpretation**: Mentor analyzes your app requirements, identifying entities, relationships, user roles, and UI patterns.
1. **Model generation**: Mentor generates or modifies the OutSystems Model, a high-level abstraction representing your app's structure, data, logic, and UI. The AI works at this model level, not with raw code.
1. **Code compilation**: The OutSystems compiler translates the model into app code following platform standards for security, performance, and architecture.

This approach separates what you want from how it's built. You focus on requirements; the platform generates the code.

## Understand the architecture

Mentor combines several components to transform natural language into deployable apps.

### Large Language Model

A Large Language Model (LLM) powers Mentor's ability to understand natural language. When you write a prompt or upload a requirement document, the LLM interprets your intent and maps it to OutSystems development patterns. This enables you to describe requirements conversationally rather than configuring options through menus.

### App Generator and App Editor

Mentor includes two specialized tools:

* **App Generator** creates new apps from your initial input. It interprets prompts or requirement documents and generates a complete app foundation with data models, screens, roles, and basic logic.

* **App Editor** modifies existing apps through conversational refinement. After initial generation, you use the App Editor to iterate on your app with focused prompts, adjusting entities, roles, layouts, and logic incrementally.

Both tools work with the OutSystems Model—they generate or modify the model, not raw code.

### OutSystems Model

The OutSystems Model represents your app's structure, data, logic, and UI. It captures what you want to build, not how to build it. When you publish, the compiler transforms this model into deployable code that meets platform standards for security, performance, and architecture.

### ODC Studio

From the App Editor, you can open your app in ODC Studio for advanced development. Use ODC Studio when you need capabilities beyond the App Editor's supported patterns—custom actions, complex aggregates, external integrations, or detailed logic.

<div class="info" markdown="1">

Opening in ODC Studio continues development in a different tool. Use the App Editor for structural changes like adding entities or adjusting roles. Use ODC Studio for implementation details and advanced logic.

</div>

## Refine iteratively

After initial generation, use the App Editor to refine your app through conversational prompts. Each prompt triggers the interpretation and model generation steps again, applying changes incrementally. The App Editor shows immediate visual feedback with sample data, helping you evaluate changes before publishing.

## Related

* [Think with AI](thinking-with-ai.md)
* [Mentor in the software development lifecycle](sdlc.md)
