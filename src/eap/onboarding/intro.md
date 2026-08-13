---
summary: Explore key differences between OutSystems 11 (O11) and OutSystems Developer Cloud (ODC) in app development, lifecycle management of assets, and library usage.
tags: outsystems developer cloud, odc vs o11, app development, libraries, element reuse
locale: en-us
guid: cb10aa0f-4e5b-4a29-92ce-03fbc813bc14
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/RJa2jhHlZ3O7UDDV8zWIwZ/Onboarding-for-OutSystems-developers?node-id=2449-32709
audience:
  - Developer
  - Platform administrator
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - understand
topic:
  - outsystems-overview
isautopublish: true
---
# ODC for O11 developers

This article summarizes differences in functionality and features that developers familiar with OutSystems 11 (O11) may find helpful when learning about OutSystems Developer Cloud (ODC).

## App development

ODC introduces a new app paradigm. The concept of module doesn't exist in ODC, the equivalent concept is called an asset.

Assets can be of the following types:

* Web app
* Mobile app
* Agentic app
* Workflow
* Library
* Mobile library

The way O11 groups modules into an application, doesn't have an equivalent in ODC, each of the assets has its own lifecycle.

Apps are also, by the nature of how element reuse works, linked with weaker dependencies. This can influence how you think about your [app architecture](../app-architecture/intro.md). For more on the changes of consuming dependencies read [Element reuse](#element-reuse).

### Libraries {#libraries}

In ODC, libraries follow a specific lifecycle for release and deployment. After publishing a library revision in ODC Studio, you must release it in the ODC Portal by setting a version number and adding release notes. Once released, the library is ready for consumption, and different apps can consume different versions of the same library.

Unlike applications, libraries aren't deployed to stages independently. When an app is deployed, ODC automatically bundles a copy of the consumed library directly into the application's package.

For more information, refer to [Libraries in ODC](../building-apps/libraries/libraries.md).

### Element reuse {#element-reuse}

In ODC apps can reuse elements from other apps and libraries, but the elements that can be made public for each of them are different.

Key examples of changes to element reuse when compared to O11 include:

* Server actions can only be set to public in libraries.
* Entities set as public in apps are always read-only.
* Relationships between entities in different apps have the following differences:
    * The delete rule is always set to **ignore**.
    * A database constraint isn't created in the database.

For more information on which elements can be public, see [Reuse elements across apps](../app-architecture/reuse-elements.md).

Also take note that when apps consume a specific a library, you must choose a specific version, which might not always be the latest. For example, app "HR Portal" can consume library "CustomerWidgets" v1 and app "Mobile HR" can consume library "CustomerWidgets" v2. See [Libraries](#libraries) for more.

### SQL syntax

ODC uses a different database management system and you should be aware of the different PostgreSQL syntax when writing SQL queries. For more information read [SQL queries compared to OutSystems 11](./differences-sql.md).

Queries which include external databases should now follow ANSI-92 SQL. For more information read [Understand ANSI-92 syntax in SQL nodes](../building-apps/data/fetch-data/sql/ansi-92-syntax.md).

### DateTime data type

When stored in a entity, attributes of type DateTime are stored in UTC.

For more on Time data types refer to [Date and time notes](../building-apps/data/data-types.md#date-time-notes)

### Mobile

ODC introduces new capabilities for mobile development, including a new runtime and configuration schema.

#### Capacitor

ODC supports Capacitor as a runtime alternative to Cordova. Depending on the version of Mobile Apps Build Service (MABS) you choose to use, you can pick either Cordova or Capacitor. Find out more by reading [Capacitor native runtime support in mobile apps](../building-apps/mobile/intro.md#capacitor-native-runtime-support-in-mobile-apps)

#### Universal JSON schema

When setting extensibility configurations through the corresponding JSON files, ODC introduces a new JSON schema that supports both Capacitor and Cordova. To find more details about the new schema and to know when to use the universal schema or Cordova-based schema. Read [Universal extensibility configurations JSON schema](../building-apps/mobile/extensibility-configurations.md)

### External libraries

ODC replaces O11 Extensions with external libraries. They are still the way for you to extend your OutSystems apps with .NET code, but there some differences other than the name. Instead of using Integration Studio, in ODC you use [OutSystems External Libraries SDK](https://www.nuget.org/packages/OutSystems.ExternalLibraries.SDK), develop the extension in your preferred .NET IDE and then upload it into the ODC Portal.

To find more about developing external libraries, read [Extend your apps with custom code](../building-apps/external-logic/intro.md).

### Publishing

ODC has a single code repository, this contrasts with O11, where the different versions of code repositories are present in every environment.

When you publish an asset in ODC Studio, your code is uploaded, compiled, and the resulting container image is placed in a registry. If the asset you published is an app it's deployed to the lowest stage (for example, Development).

A library won't be deployed on its own to a stage. You need to choose to release a revision before it can be used by an app and deployed together with its consumer. See [Libraries](../building-apps/libraries/libraries.md) for more details.

When connected through ODC Studio to an ODC organization you always have access to the same code, and you always deploy to the lowest stage in the pipeline. To learn about deployments to other environments from the ODC Portal and how it's different from O11, read [deployment](#deployment).

### Debugging

Where in O11 you choose an entry point when setting up a debugger for an app, in ODC it is implicitly set to the current app.

For a library, in debug setup you have a list of possible **Entry apps**, that is populated by the consumers of that library.

Read more about [debugging in ODC](../debugging-apps/intro.md).

### Workflows and events

ODC replaces O11 Processes, sometimes simply called BPT (Business Process Technology) with other features. Workflows are the more direct replacement to BPT and they can be created and managed in the Workflow editor in the ODC Portal.

Workflows work hand in hand with events. For example, where in O11 you might have a conditional process start based on a Entity event on a entity, in ODC workflows are triggered to start by events. Refer to [Workflows in ODC](../building-apps/workflows/workflows-in-odc.md) to know more.

In ODC Studio the **Events** tab replaces the **Processes** tab. There you can events alongside timers.

Events are a versatile way for you to trigger an outcome in a given asset based on something that happened elsewhere. To know more about how events work in ODC refer to [event-driven architecture](../building-apps/events/intro.md).

### Timers

You can find Timers in the Events tab of ODC Studio, which replaces Service Studio's Processes tab. In the ODC Portal, timers that have already been published can be found in the configuration tab of each app.

There are small differences in the way timers are scheduled in ODC, such as:

* Timers are set in UTC (Coordinated Universal Time).
* The **Weekday of Month** option isn't available in ODC.
* ODC supports scheduling intervals as low as every 5 minutes.
* The **Schedule** property is not accessible in development in ODC.

For more on timers in ODC, you can read [Use Timers](../building-apps/timers/intro.md).

### AI and agentic apps

While development of AI powered apps is possible in O11, it requires a much larger effort to integrate with the various systems and models that make them function.

ODC supports direct integration with leading Large Language Models (LLMs). You can seamlessly connect and configure models from leading providers or use your own connections and models through custom API contracts. Support of Retrieval-Augmented Generation (RAG) allows you to ground foundation models in domain-specific knowledge, significantly reducing hallucinations.

Find out more by reading [Build AI-powered apps](../building-apps/build-ai-powered-apps/intro.md).

## App management

ODC brings together your app and user management experience in one place, the ODC Portal. It consolidates functionality that previously existed across LifeTime, Service Center, and the Users application.

For more information about the ODC Portal, refer to the following:

* [UI overview of ODC Portal](../getting-started/overview-portal-studio.md#odc-portal)
* [Deployment](../deploying-apps/deploy-apps.md)
* [Monitoring](../monitor-and-troubleshoot/monitor-apps.md)
* [User management](../user-management/intro.md)

### Deployment {#deployment}

LifeTime deployments allow you to include dependencies in the same deployment plan. In ODC, you deploy assets individually. If an asset has missing dependencies in the target stage, the ODC Portal warns you. You must then deploy the needed dependencies manually.

O11 has a code repository per environment, which requires rebuilding each time you deploy to a new environment. In contrast, in ODC, when you deploy your app to the next stage, for example, from Development to Test, ODC promotes the version in the registry without any recompilation.

For more on deployment read [Deploying assets](../deploying-apps/deploy-apps.md).

### Users

In ODC, both members (IT Users in O11) and end users authenticate through a unified identity provider. Furthermore, these user identities remain consistent across all pipeline stages. Rather than maintaining separate identity silos, ODC manages user types and access levels entirely through assigned roles

For more, refer to [User management](../user-management/intro.md).

## ODC differences by task

The following table lists tasks in the ODC compared to O11.

| Task | In O11 | In ODC |
| ----------- | ----------- | ----------- |
| [Apps configuration management](../manage-platform-app-lifecycle/configuration-management.md) | LifeTime | **ODC Portal** > **Apps** |
| Create a mobile package | Service Studio, Service Center | **ODC Portal** > **(app details)** > **Mobile distribution** |
| Deploy an app to a stage. | LifeTime | **ODC Portal** > **Delivery** > **Deployments**. |
| Manage users, roles, and permissions | LifeTime | **ODC Portal** > **Users & access** |
| Manage end-users | Users console | **ODC Portal** > **Users & access** |
| Set access to end-user with specific roles to a screen in ODC Studio | Screen > **Roles** | Screen > **Authorization** > **Accessible by** |
| View apps and app details. Delete and deactivate apps | LifeTime | **ODC Portal** > **Apps** |
| View logs and audit information | LifeTime | **ODC Portal** > **Monitor** |

## Terminology

The following table summarizes terminology differences between O11 and ODC.

| O11 | ODC | Notes |
| ----------- | ----------- | ----------- |
| environment | stage | In ODC, the infrastructure where you develop and run your apps is fundamentally different. However, these terms (environment and stage), both represent the place where you deploy your apps to, such as Development and Production. See [Deploy apps](../deploying-apps/deploy-apps.md) for more information about deploying apps in ODC. |
| Reactive Web App | Web App | All Web Apps are reactive in ODC. Traditional Web Apps aren't supported. |
| Site Properties | Settings | Site Properties are called Settings in ODC. |

## Related resources

* [From O11 to OutSystems Developer Cloud](https://learn.outsystems.com/training/journeys/from-o11-to-odc-569) online course
