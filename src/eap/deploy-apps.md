---
summary: Deploy your apps to stages using the Portal.   
tags:
---

# Deploy your apps

<div class="info" markdown="1">

Project Neo documentation is under construction. It's frequently updated and expanded. Leave your feedback and help us build the most useful content.

</div>

In Project Neo, you deploy your applications to stages. A stage is a step within your continuous delivery pipeline that includes Runtime resources. Project Neo includes three stages by default: Development, Test, and Production.

Project Neo has a single code repository. When you 1-Click Publish in Service Studio, your app is containerized, deployed to the Development stage, and a container image is stored in a registry. When you're ready to promote your app to a next stage your app deploys without the need to recompile code.

Apps in each stage are isolated from each other. When you publish an app to the Development stage, the apps running in Test or Production aren't impacted. Similarly, when you promote apps to Test or Production, apps in Development aren't impacted. Each stage is also isolated from the Platform. Project Neo separates Platform and Runtime resources, allowing development to scale independently of apps deployed to stages.

## View deployment status

The portal lets you view the deployment status of the apps, from **Delivery** > **Deployments**. The apps list is filtered by stage, and you can further filter by status or date.

An app's deployment status can be one of the following:

* Running
* Finished with errors
* Finished successfully
