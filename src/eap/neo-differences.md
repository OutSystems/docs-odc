---
summary: Summary of Neo differences for OutSystems 11 users.  
tags:
---

# Neo onboarding for OutSystems developers
(change to "Project Neo" in title after MindTouch changes)

This article summarizes behavior that developers familiar with OutSystems 11 may find helpful when learning about Project Neo.

## Overview

Project Neo is a cloud-native, application development platform that provides a modular, scalable environment in which to develop and deploy your applications. Project Neo lets you build and deploy enterprise-grade, mission-critical apps in weeks instead of months. With Project Neo, you can build web apps, web portals, mobile apps, and business workflows faster. You can then deploy your apps in a scalable, secure, and high performance environment.

Project Neo delivers a modern architecture based on best practices in cloud-native infrastructure, management, and operations. Benefits include:

* Scalable and reliable apps, built and deployed in a modern infrastructure that includes Linux containers and Kubernetes
* Built-in security with end-to-end encryption  
* Disaster recovery, with app-level high availability configuration   
* The ability to take advantage of the latest Project Neo versions with pain-free upgrades

## Unified experience 

The Portal for Project Neo consolidates your app and user management experience in one place. It consolidates functionality that previously existed across LifeTime, Service Center, and the Users application.

![portal-deployments](images/portal-deployments-ss.png "Deploy apps")

  
## Build once, deploy many times

Project Neo uses the term "stage" instead of "environment." A stage (Dev, QA or Prod) is a step within your continuous delivery pipeline that includes Runtime resources. Project Neo separates Platform and Runtime resources, allowing development to scale independently of apps deployed to stages. 

Project Neo has a centralized code repository, which enables you to build your app once, and then deploy it to multiple stages. In Project Neo, when you click 1-Click Publish in Service Studio, your code builds and your app gets deployed to the Dev stage. A container image also gets saved in a registry. When you're ready to promote your app to the next stage (for example, from Dev to QA), the version that exists in the registry gets promoted without the need to recompile any code. In Project Neo, Service Studio connects to the Platform, which pushes content to the Dev stage. Service Studio does not connect to the QA or Prod stage. 

In contrast, OutSystems 11 has a code repository per environment (Dev, QA, and Prod), which requires rebuilding each time you deploy to a new environment. Additionally, in OutSystems 11, Service Studio connects to each environment where you build and deploy your apps.   

## App-level development

Project Neo removes the concept of modules. You can't break apps into separate modules, as was recommended in OutSystems 11. This change is part of a longer-term strategy that aims to simplify dependencies, minimize code conflicts, and streamline collaboration.


## Libraries 

Project Neo elevates Libraries to a top-level concept. Libraries exist at the same level as Web Apps and Mobile Apps, and they have their own lifecycle. Apps can consume different versions of a Library, and you can choose which version an app uses. For example, you can make a branding change by updating the style guide in a Library. Then, you can roll out that change one app at a time, rather than updating all apps at once. Deployed apps can coexist with old and new branding, based on the Library version each app consumes. 

## Element reuse

In Project Neo, the way you reuse elements across apps differs from OutSystems 11. Apps can reuse elements from other apps, but only when they're loosely coupled. Apps can reuse elements that are tightly coupled from Libraries only. Project Neo prevents you from creating strong dependencies between apps (Web Apps or Mobile Apps). You can only have strong dependencies between an app (Web App or Mobile App) and a Library.

Note the following regarding reuse in Project Neo:

* Dependencies between apps (Web Apps or Mobile Apps) are always weak, which means that Entities shared between apps are always read-only; in Project Neo, to write to Entities, create a Service Action
* Relationships between Entities in different apps work differently. In Project Neo:
    * The delete rule is always set to ignore
    * A database constraint is not created in the database, as is done with OutSystems 11 
* Apps (Web or Mobile) can have strong dependencies to Libraries only; See [Reuse elements across apps](reuse-elements.md) for more information 
* Apps (Web or Mobile) consume a specific Library version; for example, app A can consume Library v1 and app B can consume Library v2
* Many elements that could be public in OutSystems 11 can't be public in Project Neo; See [Reuse elements across apps](reuse-elements.md) for more information.

The following screen capture shows your options when creating an app in Service Studio.

![Create Web App](images/create-service-ss.png "Create Web App")

## Debugging changes in Service Studio

When debugging apps in Service Studio, you see the following differences in Project Neo:

* The debug entry point now refers to the Entry App and not the Entry Module, as modules don't exist in Project Neo
* When debugging an app the Entry App only shows the current app
* When debugging a Library the Entry App lists the Apps that consume that Library

In Project Neo, when you debug an app in Service Studio, you see an Entry app field instead of an Entry module field. Because modules no longer exist, your debugging entry point is at the app level. For a Web or Mobile App that doesn't consume any Library elements, you only see the current app as an entry point option. When an app reuses elements in a Library, the producer Library appears in the Entry app list. When debugging a Library, the **Start debugging** option is only available when the Library is consumed by an app.

## Timers in Service Studio

Currently you can set timers in Service Studio. The format of timers differs from OutSystems 11. The UI for setting timers in Service Studio walks you through the valid values and formats.

Note the following related to timers in Project Neo:

* Currently, you can set timers in Service Studio, but not in the Portal
* Timers are set in UTC (Coordinated Universal Time)
* The "Weekday of month" option doesn't exist in Project Neo 

## Project Neo differences by task

The following table lists tasks you can complete in the Portal, as well as the interface used for the same task in OutSystems 11.

| Task | In O11 | In Project Neo |
| ----------- | ----------- | ----------- |
| Deploy an application to QA or Production | LifeTime, where you deploy apps to the QA or Production environment. | **Portal** > **Delivery** > **Deployments**. In Project Neo, you deploy to the QA or Prod stage. |
| Configure apps when deploying. Includes timers, site properties, email | LifeTime | **Portal** > **Apps** |
| View apps and app details. Delete and deactivate apps | LifeTime | **Portal** > **Apps** |
| Manage app dependencies | LifeTime & Service Studio | In Project Neo, you see errors in Service Studio when dependencies break. |
| Manage IT users, roles, and permissions | LifeTime | **Portal** > **Users & access**. |
| Manage end users | Users console | **Portal** > **Users & access** |
| View logs and audit information; set logging levels | LifeTime | **Portal** > **Monitoring** |
| Access Forge components | Forge URL | **Portal** > **Forge** |

## Terminology mapping

The following table summarizes terminology differences between OutSystems 11 and Project Neo.

| OutSystems 11 name | Project Neo name | Notes |
| ----------- | ----------- | ----------- |
| environment | stage | In Project Neo, the infrastructure where you develop and run your apps is fundamentally different. However, these terms (environment and stage), both represent the place where you deploy your apps to Dev, QA, and Prod. See [Deploy apps](deploy-apps.md) for more information about deploying apps in Project Neo. |
| Reactive Web App | Web App | All Web Apps are reactive in Project Neo. Traditional Web Apps are not supported. |
| app | Project | In Project Neo, Projects contain your Web App, and, optionally, a Library or Libraries. |
| N/A | organization | In Project Neo, an organization maps to a tenant, and can represent a company or a unit or group within a company. |
| module | N/A | Modules don't exist in Project Neo. |
