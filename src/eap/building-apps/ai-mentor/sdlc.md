---
summary: Understand how Mentor fits into the ODC software development lifecycle from generation through testing, deployment, maintenance, and governance.
tags: sdlc, software lifecycle, testing, deployment, governance, collaboration, maintenance
guid: 7c3b8a4f-2d1e-4b9a-9e7f-6a5d3c2b1f0e
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


# Mentor in the software development lifecycle

Apps generated with Mentor follow the standard ODC software development lifecycle. Understanding where each tool fits helps you plan your development workflow from initial concept through production deployment and ongoing maintenance.

## Place Mentor in the ODC development paradigm

Mentor fits into the OutSystems Developer Cloud (ODC) platform as an AI-accelerated entry point to the standard development lifecycle. Rather than replacing your existing development workflow, Mentor extends it by providing a conversational interface for the initial phases of app creation.

### For ODC developers

If you already develop in ODC Studio, think of Mentor as an alternative starting point for new apps. Instead of beginning with blank templates and manually configuring screens, entities, and roles, you can describe your requirements in natural language. Mentor generates the app scaffolding—complete with data models, UI layouts, and security roles—which you can then refine through the App Editor before transitioning to ODC Studio.

This transition happens naturally when your development needs move beyond what the App Editor supports. When you need custom client or server actions, advanced aggregates with complex filtering, or integrations with external systems through REST you move to ODC Studio for more control. For supported patterns, Mentor and ODC Studio work together bi-directionally. Changes you make in ODC Studio sync back to the App Editor, and changes in the App Editor reflect in Studio, giving you the flexibility to work in whichever environment suits your current task.

### For O11 developers

If you develop in OutSystems 11, you'll recognize familiar concepts in Mentor. The platform still relies on visual development and model-driven architecture, with the OutSystems compiler continuing to ensure that generated code meets established standards. What changes is the interface for initial app creation. Instead of manually clicking through Service Studio to configure entities and screens, you describe your requirements conversationally, and Mentor generates the foundation.

The workflow becomes: generate with prompts, refine visually in the App Editor, then transition to ODC Studio for advanced development. This represents an evolution in how you interact with the platform during early development stages, while the underlying principles of OutSystems development remain constant.

One architectural difference to note: ODC uses a cloud-native, stage-based deployment model. Apps deploy through Development, QA, and Production stages using the ODC deployment in Portal, which differs from the LifeTime-based deployment in O11.

## Generate initial app

The journey begins with Mentor App Generator, where you provide either natural language prompts or requirement documents. It interprets your input and creates a complete app foundation: a data model with entities, attributes, and relationships; a user interface with screens, layouts, and navigation; security roles and authorization rules; and basic business logic to tie everything together.

Once Mentor App Generator creates this foundation, Mentor App Editor becomes your workspace for refinement. Through iterative prompts, you can modify entities, adjust roles, change screen layouts, and add business logic. The App Editor's AI-powered suggestion system analyzes your changes and updates the app structure accordingly, showing you immediate visual feedback so you can evaluate each modification before committing to it.

## Transition to ODC Studio

As your app grows more complex, you'll eventually need capabilities that extend beyond Mentor App Editor's supported patterns. This is when you transition to ODC Studio. The transition happens naturally—when you need custom client or server actions, advanced aggregates with complex filtering, integrations with external systems through REST or SOAP, custom CSS or JavaScript, or complex business logic that requires the OutSystems visual language, ODC Studio provides the full development environment you need.

Mentor App Editor doesn't disappear after this transition. For supported patterns, it remains available alongside ODC Studio, and you can switch between the two tools as your needs dictate. Need to add a new entity or adjust security roles? Use Mentor App Editor. Need to write a complex server action? Use ODC Studio. The bi-directional nature of the integration means your work in either tool reflects in the other.

## Test, deploy, and maintain

Testing Mentor-generated apps follows the same approaches as any ODC app. You can test manually in the Development stage, automate your tests through ODC APIs, or conduct user acceptance testing before production deployment. There's no special process required because Mentor-generated apps are, fundamentally, ODC apps.

Deployment works identically as well. You move your app through the standard ODC stages—Development to QA to Production—using the deployment pipeline. From the deployment system's perspective, there's no difference between an app generated by Mentor and one built entirely in ODC Studio.

Long-term maintenance requires a balanced approach between tools. Use ODC Studio for your ongoing development work and bug fixes—the detailed, code-level work that happens throughout an app's lifetime. Return to Mentor App Editor when you need to make structural changes like adding entities, modifying data models, or adjusting security roles. These architectural modifications often work more efficiently through the App Editor's conversational interface. Version control and lifecycle management continue to follow standard ODC processes regardless of which tool you use for specific tasks.

## Govern and collaborate

From a governance perspective, Mentor-generated apps are indistinguishable from apps built manually in ODC Studio. The OutSystems compiler enforces the same security, performance, and architecture standards regardless of how the underlying model was created. This means administrators apply the same quality gates, conduct the same code reviews, and perform the same security reviews. Architecture governance policies that apply to your manually created apps apply equally to AI-generated ones.

This consistency enables natural collaboration across teams. Developers can iterate on requirements using Mentor App Editor, describing changes conversationally while the AI handles the implementation details. When implementation requires deeper technical work, developers move to ODC Studio for complex logic. Architects review the generated patterns and provide guidance just as they would for any app, ensuring the architecture aligns with organizational standards. Administrators manage deployment, monitoring, and governance through the same tools and processes they use for all ODC apps, maintaining consistency across your app portfolio.

## Related

* [How Mentor works](mentor.md)
* [Think with AI](thinking-with-ai.md)
