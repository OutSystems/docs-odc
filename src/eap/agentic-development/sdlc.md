---
summary: Agentic development integrates into the ODC software development lifecycle across generation, testing, deployment, maintenance, and governance.
tags:
  - Agentic
  - AI
  - Deploy
  - Development lifecycle
  - Mentor
  - Mentor Studio
  - Testing
guid: 7c3b8a4f-2d1e-4b9a-9e7f-6a5d3c2b1f0e
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
audience:
  - Developer
  - Platform administrator
topic:
  - creating-apps
isautopublish: true
---


# Agentic development in the SDLC

Apps created through agentic development follow the standard ODC software development lifecycle. Understanding how this paradigm integrates with your existing workflow helps you plan from initial concept through production deployment and ongoing maintenance.

## Integrate agentic development into ODC

Agentic development fits into OutSystems Developer Cloud as an accelerated entry point to the standard development lifecycle. Rather than replacing your existing workflow, prompt-based development extends it by providing a conversational interface for the initial phases of app creation.

### For ODC teams

If you already develop in ODC Studio, think of agentic development as an alternative starting point for new apps. Instead of beginning with blank templates and manually configuring screens, entities, and roles, you describe your requirements in natural language. ODC generates the app scaffolding, complete with data models, UI layouts, and security roles, which you then refine through prompts before transitioning to ODC Studio.

As your development needs grow beyond common patterns, you work in ODC Studio. There, Mentor Studio and manual development handle custom client or server actions, advanced aggregates with complex filtering, and external integrations.

### For O11 teams

If you develop in OutSystems 11, you'll recognize familiar concepts. ODC still relies on visual development and model-driven architecture, with the OutSystems compiler applying established standards to the generated model as it does to any app. What changes is the interface for initial app creation. Instead of manually clicking through Service Studio to configure entities and screens, you describe your requirements conversationally, and ODC generates the foundation.

One difference to note: ODC uses a cloud-native, stage-based deployment model. Apps deploy through development, QA, and production stages using ODC deployment in Portal, which differs from the LifeTime-based deployment in O11.

## Generate and transition to ODC Studio

The workflow follows the same generate-review-refine cycle described in [Thinking with AI](thinking-with-ai.md). You provide prompts or requirement documents, review the blueprint, generate the app, and refine through iteration. When your app needs capabilities beyond common patterns, such as custom actions, advanced aggregates, external integrations, or complex business logic, you build them in ODC Studio with Mentor Studio or manual development.

## Test, deploy, and maintain

Apps created through agentic development are standard ODC apps and follow the same lifecycle processes.

* **Testing.** Test manually in the development stage, automate tests through ODC APIs, or conduct user acceptance testing before production deployment. No additional process is required.
* **Deployment.** Move your app through the standard ODC stages (development to QA to production) using the deployment pipeline. From the deployment system's perspective, there is no difference between an app created through agentic development and one built entirely in ODC Studio.
* **Maintenance.** Use ODC Studio for ongoing development work and bug fixes. Return to agentic development for structural changes like adding entities, modifying data models, or adjusting security roles. Version control and lifecycle management follow standard ODC processes regardless of which tool you use.

## Govern and collaborate

From a governance perspective, apps created through agentic development are indistinguishable from apps built manually in ODC Studio. The OutSystems compiler enforces the same security, performance, and architecture standards regardless of how you created the underlying model. This means administrators apply the same quality gates, conduct the same code reviews, and perform the same security reviews. Architecture governance policies that apply to your manually created apps apply equally to AI-generated ones.

This consistency enables collaboration across teams. You can iterate on requirements using agentic development, describing changes conversationally while the AI handles implementation details. When implementation requires deeper technical work, you move to ODC Studio for complex logic. Architects review generated patterns and provide guidance just as they would for any app, ensuring the architecture aligns with organizational standards. Administrators manage deployment, monitoring, and governance through the same tools and processes they use for all ODC apps, maintaining consistency across your app portfolio.

### Control who can use Mentor

Beyond app-level governance, administrators control who can use the Mentor tools. Tenant administrators grant the **Mentor** > **Use** permission through organization roles in the ODC Portal. The built-in **Developer** role includes this permission by default. For custom roles, administrators add the permission explicitly.

<div class="info" markdown="1">

Enabling or disabling this permission has no effect on who can access Mentor Web or Mentor Studio. OutSystems is rolling out Mentor access enforcement in phases, starting with this permission so administrators can configure their custom roles ahead of enforcement.

</div>

Role changes that grant or revoke the **Mentor** > **Use** permission appear in your organization's audit trail alongside other role changes.

For more information about the Mentor permission and how to assign it through roles, refer to [Roles and permissions for members (IT-users)](../user-management/roles.md). For more information about reviewing access changes, refer to [Audit trails](../monitor-and-troubleshoot/audit-trail/audit-trail.md).

## Related resources

Agentic development integrates into your existing testing and deployment processes, and introduces access controls for who can use Mentor. The following resources cover the tools and concepts that support each phase of the lifecycle.

* For the conceptual shift to prompt-based development and iteration strategies, refer to [Thinking with AI](thinking-with-ai.md).
* For an overview of both Mentor tools and guidance on when to use each, refer to [Introduction to agentic development](intro.md).
* For technical details on how AI agents interact with the OutSystems compiler and app model, refer to [Architecture](architecture.md).
