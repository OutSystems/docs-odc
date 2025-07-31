---
summary: none
tags: none
guid: b17a8f2d-c767-49b4-9f50-381329442aba
locale: en-us
app_type: reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?m=auto&node-id=6814-98&t=06ppRqezdRkEkuAh-1
outsystems-tools:
  - odc studio
coverage-type:
  - understand 
audience:
  - frontend developers
  - backend developers
  - full stack developers
  - ui designers
---

# About Mentor App Generator and Editor

OutSystems Mentor is a suite of GenAI capabilities that accelerates the application development lifecycle. Mentor addresses common challenges like time-consuming prototyping and converting requirements into functional code.

The **Mentor App Generator** transforms ideas into a full-stack, scalable OutSystems application. The App Generator uses natural language prompts or requirement documents, grounding its suggestions with your existing enterprise data to ensure contextual relevance.

The **Mentor App Editor** helps you visually iterate on the generated application using AI-powered suggestions. For the patterns that Mentor recognizes, the App Editor is bi-directionally interoperable with ODC Studio, providing a seamless workflow from initial idea to enterprise-grade deployment. We'll expand the supported patterns as App Editor evolves.

OutSystems Mentor App Generator and App Editor build apps faster while maintaining high-quality standards. Benefits include:

* Creates initial designs and validates app prototypes quickly.
* Converts product requirements into functional code, data models, business logic, and UI automatically.
* Streamlining early-stage apps saves costs and resources. Teams can focus on complex, high-value tasks without wasting time or effort on repetitive coding.

![Icons representing the benefits of Mentor App: designs and validates, converts requirements effortlessly, reduces costs efficiently.](images/benefits-mentor-app-ams.png "Benefits of Mentor App")

## Getting started with AI Mentor

OutSystems Mentor transforms app development by starting with your natural language description instead of blank screens and complex configurations. Mentor interprets your requirements and generates a complete app with data models, user interfaces, security roles, and business logic. After generation, you can refine your app through the visual App Editor or enhance it further in ODC Studio. This AI-driven approach helps you go from concept to working prototype while focusing on what your application should accomplish rather than technical complexities.

<div class="info" markdown="1">

This functionality uses the Data platform, which may process data outside your ODC organization region to provide its capabilities. For more information, refer to [Data platform](../../manage-platform-app-lifecycle/platform-architecture/intro.md#data-platform).

</div>

To create an app with AI Mentor:

1. Go to **Portal** > **Apps** > **Create** > **Web app** > **Generate with Mentor**.
1. In the **Create app** screen, enter your prompt or upload your requirements file, or use some of the example prompts. Confirm to let Mentor show the suggested data and roles.

    ![Create app screen with a prompt to create an Inventory Management app, including example prompts for Ticket Management, Employee Onboarding, and Order Management.](images/ai-mentor-create-app-prompt-pl.png "Create App Prompt")

1. Edit the data model and roles if needed. Click **Generate** to generate the app and open it in the App Editor.

    ![Screen to edit data model and roles before generating the app, showing Inventory Management app with data entities and roles.](images/ai-mentor-edit-data-roles-generate-pl.png "Edit Data and Roles")
    
1. The App Editor helps you fine-tune your app with prompts. When you're happy with the app, click **Publish**.

    ![App Editor interface displaying the app overview with user, product, and order lists and detail views, and roles for Admin and Manager.](images/ai-mentor-edit-app-interface-pl.png "App Editor Interface")

## How Mentor works

To understand how Mentor functions, it's helpful to be familiar with these core concepts.

### From prompt to application

Mentor abstracts the complexity of application generation into a clear, model-driven workflow:

1. **Prompt or document input**: You provide your application requirements using natural language or by uploading a document.  
1. **Model generation**: The system generates and modifies the OutSystems Model, which is a high-level abstraction of the application.  
1. **Code compilation**: The OutSystems compiler takes the verified model and generates the final, production-ready application code, ensuring it meets established security, performance, and architecture standards.

## Capabilities and patterns

Mentor recognizes and generates various application components and patterns.

### Mentor App Generator

The App Generator applies several patterns to build a well-structured application from your initial input.

* **Data integration**: Integrates with Data Fabric and public entities, with full support for both reading and writing data.  
* **Entity editing**: You can edit entities before generating an app by adding, changing, or removing the suggested entity.  
* **Predefined roles**: The generated app includes a predefined set of roles that you can modify before generating it.  
* **Authorization rules**: Supports medium-complexity authorization rules related to the logged-in user, such as viewing or editing a user's own records or records associated with their team or department. This mechanism also supports authorizations at entity level, controlling which entity can be read or edited by the available roles.  
* **Static entity detection**: AI detects static entities and related records, automatically displaying them as tags in the UI for status or task management use cases.  
* **Dashboard generation**: Respects your intent if you specify whether to include a dashboard. It gives each section an appropriate title and chooses to use a table, gallery, or chart.  
* **Data management**: You can download existing data or upload new data to replace sample data generated by the app.  
* **UI generation and themes**: The header color of the generated app is randomly chosen, switching between white and the primary color. You can also select any public theme available on your tenant to set as the base theme.  
* **Context-aware screen layouts**: Generates specific screen layouts based on data context, such as a "List screen with Map View" for entities containing addresses or a "cardPerson" detail screen for entities with personal attributes.  
* **AI-suggested icons**: Automatically suggests and applies relevant Font Awesome icons for each item in the app menu. This applies to the app logo as well.

### Mentor App Editor

After an app is generated, the App Editor provides tools and AI-powered suggestions to help you refine and evolve it.

The following high-level changes suggested in the App Editor can impact several places in your app. Colored indicators display where these changes apply.

* **AI-powered suggestions**: Analyzes your app to offer context-aware suggestions for adding new entities, modifying attributes, adjusting security roles, and changing static entity enumerations. Suggestions can handle complex structures, including many-to-many relationships, and can mix local and external entities.  
* **Entity management**: You can add or delete entities and their attributes. AI generates all the attributes, including static entities or static entity records, screens, menu items, and the relationships to and from them.  
* **Security adjustments**: Adjust security by adding and deleting roles and adjusting the logged-in user authorizations.  
* **Data model refinements**: Make data model refinements by adding new attributes to existing entities.  
* **Business logic**: Add business logic through prompts that specify new actions or workflows.  
* **Effortless refinement with a WYSIWYG interface**: Visually explore screens and data models. When a suggestion is applied, the change is immediately visible in screen previews populated with sample data.  
* **Bi-directional interoperability with ODC Studio**: For the patterns that Mentor is able to recognize, seamlessly switch to ODC Studio for advanced development. Changes made in ODC Studio are reflected back in the App Editor. The supported patterns will grow as App Editor evolves.  
* **Centralized authorization management**: A dedicated panel allows you to manage authorization levels for individual entities.  
* **Direct app customization**: You can customize the app name and icon directly within the editor.

<div class="info" markdown="1">

**Current limitations:** The suggestions only support **add** operations. Operations such as **change** and **rename** aren't supported yet.

</div>

## Best practices

Follow these best practices for your input to get the most accurate and relevant results from the Mentor App Generator.

<div class="info" markdown="1">

AI Mentor is designed to support the English language. You can input prompts and requirements documents in other languages, but for the most accurate results, English is recommended.

</div>

### Natural language prompts

When providing input via a direct text prompt, clarity and structure are key to getting the best results.

![Icons illustrating best practices for natural language prompts: ensure clarity concisely, organize data model, add role-specific details.](images/natural-language-prompts-best-practices-ams.png "Best Practices for Natural Language Prompts")

* **Be clear and concise**. Include the app name, purpose, and main functionality in one to two sentences.  
    * Example: Create an Employee Onboarding app that tracks employee details, onboarding steps, and status updates. It should have a list and edit screens and roles for HR and Managers.
* **Structure the data model**. Mention entities and attributes if you know them.  
    * Example: The app should have entities for Employees (Name, ID, Department, Role) and Onboarding steps (Step name, Status, Due date).
* **Add role-specific details**. Mention the roles and permissions required if you know them.
    * Example: Managers can update onboarding steps. HR can add and edit employee records.

Here's an example of a prompt following the best practices:

"Create an Inventory Management app to track Products (Name, ID, Stock) and Orders (Order ID, Product, Quantity, Status). Managers can view stock. Admins can update inventory."

### Requirement document

For more complex applications, providing a structured requirement document is an effective way to define your needs.

* **Use supported formats**. Supported formats include .txt, .docx, and .pdf. The file size limit is 5 MB.  
* **Organize requirements logically**. Include separate sections for app purpose, entities and attributes, and roles and permissions.  
* **Avoid excessive detail**. Use the document for functional requirements, not implementation details.  
* **Avoid irrelevant content, screenshots, or tables**. This content is not processed and may hamper the generation process.

Refer to [Order Management System Requirements Document](resources/order-management-system-requirements.docx) for a sample requirement document.

![Icons illustrating best practices for requirement documents: use supported formats, organize requirements logically, avoid excessive details, ensure relevant content, avoid media usage.](images/requirement-best-practices-ams.png "Best Practices for Requirement Documents")

## Mentor App Editor best practices

Follow these best practices for effective keyword prompting for suggestions:

* **Be specific about changes**. Use short prompts to add data.
    * Example: Add validation rules to the email field.
* **Use role-based prompts**. Include roles explicitly to enhance security.
    * Example: Add a new role: Manager.
* **Focus on data model refinements**. Specify exactly what you want to add.
    * Example: Add salary to Employee.
* **Avoid ambiguity**. Avoid using vague prompts such as "Make the app better."
    * Example: Instead of "improve the app," use "add email validation to the contact form."

![Icons illustrating best practices for keyword prompts: specify required changes, use role-based prompts, refine data models, avoid ambiguity.](images/prompt-best-practices-ams.png "Best Practices for Keyword Prompts")

## Security and data privacy

Mentor is designed with enterprise-grade security and data handling policies to ensure your applications and data are always protected.

* **Model-driven generation**: The AI capabilities modify the OutSystems Model, not raw code. The final code is generated by the OutSystems compiler, ensuring it meets established standards.  
* **Data privacy**: Your data, prompts, and requirement documents are fully isolated and are not used to train third-party models. All data is encrypted with tenant-specific keys.  
* **Compliance**: The platform is SOC 2 compliant and adheres to GDPR standards.

For information about AI Mentor technical limitations, refer to [OutSystems system requirements for ODC](../../getting-started/system-requirements.md#ai-mentor).


