---
summary: Summary of Neo differences for OutSystems 11 users.  
tags: 
---

# Neo cheat sheet (WIP)

This article highlights some of the differences in Neo. 

Neo is a cloud-native, application development platform that provides a modular, scalable environment in which to develop and deploy your applications. OutSystems allows you to build and deploy enterprise-grade, mission-critical applications in weeks instead of months. With OutSystems, you can build web applications, web portals, mobile apps, and business workflows faster. You can then deploy your apps in a scalable, secure, and high performance environment. 

Neo delivers a modern architecture based on best practices in cloud-native infrastructure, management, and operations. Benefits include:

* Scalable and reliable apps that run on containers
* Modern, industry-standard technologies that allow you to quickly deploy and maintain your apps
* Ability to take advantage of the latest Neo versions without disruption

## The Portal

The new Neo Portal consolidates your app and user management experience in one place. The Portal consolidates functionality that previously existed across the LifeTime, Service Center, and Users consoles. 

![portal-deployments](images/portal-deployments.png "Deploy apps") 

## Build once, deploy many times

The new Neo architecture changes the app deployment process. Instead of deploying to environments, you deploy your apps to stages. A stage (Dev, QA or Prod) is a tenant namespace within a cluster, and it’s where your apps run. Each stage resides in a separate cluster, and no development or code compiling occurs within the context of a stage. Development and build activities occur in a separate cluster, which is closely coupled with the Dev stage. 

Service Studio connects to the Platform Service, which is where you develop your apps. When you publish an app in Service Studio, the target deployment stage is always Dev. You can no longer connect Service Studio to other stages (QA or Prod). When you publish (1CP) in Service Studio, your app is built and deployed to Dev, and a portable app pod is also created. This app pod contains everything needed to run your app. When you’re ready to promote the app to another stage (QA or Prod), you promote the app pod, without any need to rebuild code. The staging sequence is always Dev to QA to Prod, in that order. 

## Modules are deprecated

Neo apps don’t have modules. This change is part of a  longer-term strategy that aims to simplify dependencies, minimize code conflicts, and streamline collaboration. See Manage dependencies for more information.

## Libraries

Projects in Neo contain apps and libraries. When reusing code in your app, strong dependencies can only exist between your app and a library. When your app reuses elements in a library, the app’s dependency is tied to a specific library version. Libraries are versioned, and they aren’t staged or deployed. When you deploy your app, the library version used gets locked to the app version. Any updates to future app or library versions in Service Studio and Dev have no impact on apps running in QA or Prod. 

![Create Web App](images/create-service.png "Create Web App") 

## Reuse elements across apps 

In Neo, you can’t have strong dependencies between web apps or mobile apps. Dependencies between web and mobile apps are always weak. Apps can only have strong dependencies to libraries. Consequently, many elements you previously could set to public in an app can no longer be public. For example, you can’t set Server Actions as public in an app. See <<>> for more information.

## Debugging In Service Studio (TBD)

## Timers in Service Studio

## Neo differences by task-- stopped here

The following table lists common tasks and where you complete them in OutSystems 11 and in Neo. 

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

## Terminology mapping (WIP)

The following table summarizes terminology differences between OutSystems 11 and Neo. 

| OutSystems 11 name | Project Neo name | Notes | 
| ----------- | ----------- | ----------- |
| Environment | Stage | In Neo, the infrastructure where you develop and run your apps is fundamentally different. However, these terms (environment and stage), both represent the place where you deploy your apps to Dev, QA, and Prod. See xxx for more information about deploying apps in Neo. | 
| Reactive web app | Web app | All web apps are reactive in Neo. Neo doesn't support traditional web apps. | 


