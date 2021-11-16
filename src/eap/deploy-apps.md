---
summary: Summary of Neo differences for OutSystems 11 users.  
tags: deploy apps 
---

# Deploy your apps

You deploy your OutSystems applications to stages, which are tenant namespaces where a containerized app runs. By default, your OutSystems infrastructure includes three stages: development (Dev), Quality Assurance (QA), and production (Prod). Apps you publish during development reside in the Dev stage. For example, when you use the 1-Click Publish button in Service Studio, you compile the app and publish it to the Dev stage. The QA stage is where your teams can conduct more thorough app testing. The Prod stage is where users interact with and access your application in production.

Apps in each stage are isolated from each other. Thus when you publish an app to Dev, no impact occurs to existing versions in QA or Prod. Additionally, promoting apps to QA or Prod does not impact versions of the app running in Dev. Each stage is also isolated from changes made to the OutSystems Platform Service. Updates to the OutSystems Platform Service version in your infrastructure, which is a transparent process handled by OutSystems, do not impact apps running in QA or Prod.

## Build once, deploy many times

When you publish an app to the Dev stage, the Build Service creates a container image, which is a portable version of the app. This portable app, or app pod, includes everything needed to run the app in any stage. When you’re ready to promote an app, the previously compiled app is promoted to QA or Prod, with no impact to the version in Dev. Additionally, no build occurs when promoting an app because the app version and all its dependencies already exist in a portable app pod. Thus you can build your app once and deploy (or stage) it multiple times.

## Promoting apps

To promote an app to the QA or Prod stage:

1. Go to the Neo Portal.
2. Go to **Delivery** > **Deployments**.
3. Select the app you want to promote, and then follow the guided staging process in the UI.

