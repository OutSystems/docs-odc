---
summary: Summary of Neo differences for OutSystems 11 users.  
tags: outsystems-11; neo; deploy apps; portal 
---

# Neo onboarding for OutSystems developers

This article summarizes behavior that developers familiar with OutSystems 11 may find helpful when learning Neo.

## Overview

Neo is a cloud-native, application development platform that provides a modular, scalable environment in which to develop and deploy your applications. OutSystems lets  you build and deploy enterprise-grade, mission-critical apps in weeks instead of months. With OutSystems, you can build web apps, web portals, mobile apps, and business workflows faster. You can then deploy your apps in a scalable, secure, and high performance environment.

Neo delivers a modern architecture based on best practices in cloud-native infrastructure, management, and operations. Benefits include:

* Scalable and reliable apps that run on containers
* Modern, industry-standard technologies that let you quickly deploy and maintain your apps
* The ability to take advantage of the latest Neo versions without disruption

## Consolidated Neo Portal

The Neo Portal consolidates your app and user management experience in one place. It consolidates functionality that previously existed across apps such as LifeTime and Service Center.

![portal-deployments](images/portal-deployments.png "Deploy apps")

## Build once, deploy many times

The Neo architecture changes the way you deploy apps . Instead of deploying to environments, you deploy your apps to stages. A stage (Dev, QA or Prod) is a tenant namespace within a cluster where your apps run. Each stage resides in a separate cluster, and the Platform Service resides in its own cluster.

Service Studio connects to the Platform Service, where you develop and build your apps. When you publish an app in Service Studio, the target deployment stage is always Dev. You can no longer connect Service Studio to other stages (QA or Prod). When you publish (1-Click Publish) in Service Studio, your app is built and deployed to Dev, and a portable app pod is created. This app pod contains everything needed to run your app. When you’re ready to promote the app to another stage (QA or Prod), you promote the app pod, without any need to rebuild code. Staging always follows the sequence: Dev to QA to Prod.

See [Deploy apps](deploy-apps.md) for more information.

## Projects, Libraries, and element reuse  

**Projects and Libraries** -- Neo introduces the term Project to the Service Studio hierarchy. When you begin development in Service Studio, you create a Project. Your Project holds your Web or Mobile App, and, optionally, any Libraries associated with it. In later Neo versions, Projects can include Services. Apps always reuse elements from a specific Library version, and once deployed to the QA or Prod stage, are locked to that version. Any updates made in Dev do not impact apps deployed to the QA or Prod stage.

**No more modules** -- Neo doesn't include the concept of modules. An app is no longer broken into separate modules, as recommended in OutSystems 11. This change is part of a longer-term strategy that aims to simplify dependencies, minimize code conflicts, and streamline collaboration.

**Element reuse** -- In Neo, the way you reuse elements across apps and Projects differs from OutSystems 11. Neo prevents you from creating strong dependencies between Web or Mobile Apps. You can only have strong dependencies between a Web or Mobile app and a Library.

Note the following behavior when developing your apps in Neo:

* Dependencies between Web and Mobile Apps are always weak, which means:
    * Entities shared between apps are read-only; in Neo, create a Service Action to share an entity as read/write
    * The delete rule for foreign keys is always set to ignore when sharing entities between apps
* Web or Mobile Apps can have strong dependencies to Libraries only; See [Reuse elements across apps](reuse-elements.md) for more information 
* Web or Mobile Apps consume a specific Library version; for example, app A can consume Library v1 and app B can consume Library v2
* Libraries aren't staged or deployed
* Many elements that could be public in OutSystems 11 can't be public in Neo; See [Reuse elements across apps](reuse-elements.md) for more information.
* Modules don't exist in Neo

The following screen capture shows your options when creating a Project in Service Studio.

![Create Web App](images/create-service.png "Create Web App")

## Debugging changes in Service Studio

In Neo, when you debug an app in Service Studio, you see an Entry app field instead of an Entry module field. Because modules no longer exist, your debugging entry point is at the app level. For a Web or Mobile App that doesn't consume any Library elements, you only see the current app as an entry point option. When an app reuses elements in a Library, the producer Library appears in the Entry app list. When debugging a Library, the **Start debugging** option is only available when the Library is consumed by an app.

## Timers in Service Studio

At this point, you can only set timers in Service Studio. You can't set timers in the Neo Portal, as you could in LifeTime in OutSystems 11. Additionally, the format of timers has changed. The UI for setting timers in Service Studio walks you through the valid values and formats.

## Neo differences by task

The following table lists tasks you can complete in the Neo Portal, as well as the interface used for the same task in OutSystems 11.

| Task | In O11 | In Neo |
| ----------- | ----------- | ----------- |
| Deploy an application to QA or Production | LifeTime, where you deploy apps to the QA or Production environment. | **Portal** > **Delivery** > **Deployments**. In Neo, you deploy to the QA or Prod stage. |
| Configure apps when deploying. Includes timers, site properties, email | LifeTime | **Portal** > **Apps** |
| View apps and app details. Delete and deactivate apps | LifeTime | **Portal** > **Apps** |
| Manage app dependencies | LifeTime | In Neo, you see errors in Service Studio when dependencies break. |
| Manage IT users, roles, and permissions | LifeTime | **Portal** > **Users & access**. |
| Manage end users | Users console | **Portal** > **Users & access** |
| View logs and audit information; set logging levels | LifeTime | **Portal** > **Monitoring** |
| Access Forge components | Forge URL | **Portal** > **Forge** |

## Terminology mapping

The following table summarizes terminology differences between OutSystems 11 and Neo.

| OutSystems 11 name | Project Neo name | Notes |
| ----------- | ----------- | ----------- |
| environment | stage | In Neo, the infrastructure where you develop and run your apps is fundamentally different. However, these terms (environment and stage), both represent the place where you deploy your apps to Dev, QA, and Prod. See [Deploy apps](deploy-apps.md) for more information about deploying apps in Neo. |
| Reactive Web App | Web App | All Web Apps are reactive in Neo. Neo doesn't support Traditional Web Apps. |
| app | Project | In Neo, Projects contain your Web App, and, optionally, a Library or Libraries. In future Neo versions, Projects will also include Services. |
| site properties | settings | Eventually, you'll configure settings in the Neo Portal |
| N/A | organization | In Neo, an organization maps to a tenant, and can represent a company or a unit or group within a company. |
| module | N/A | Modules don't exist in Neo. |
