---
summary: Learn how Mentor transforms requirements into apps through a three-stage process of interpretation, model generation, and compilation.
tags: app generation, mentor workflow, model-driven development, prompt engineering, ai-assisted development
guid: 8f4a2e1d-9b7c-4a3f-8d6e-5c9f3a2b1e0d
locale: en-us
app_type: reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - portal
  - ai mentor studio
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

Mentor uses a three-stage process to transform requirements into apps: interpretation, model generation, and compilation.

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

This model-driven approach separates intent (what you want) from implementation (how it's built), letting you focus on requirements while the platform handles code generation.

## Refine iteratively

After initial generation, use the App Editor to refine your app through conversational prompts. Each prompt triggers the interpretation and model generation steps again, applying changes incrementally. The App Editor shows immediate visual feedback with sample data, helping you evaluate changes before publishing.

## Related

* [Think with AI](thinking-with-ai.md)
* [Mentor in the software development lifecycle](sdlc.md)
