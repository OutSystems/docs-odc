---
summary: Deploy your apps to stages using the Portal.   
tags:
---

# Deploy your apps

<div class="info" markdown="1">

Project Neo documentation is under construction. It's frequently updated and expanded. Leave your feedback and help us build the most useful content.

</div>

In Project Neo, you deploy your applications to stages. A stage is a step within your continuous delivery pipeline that includes runtime resources. Project Neo includes three stages by default: Development, Test, and Production.

Project Neo has a single code repository. When you 1-Click Publish in Service Studio, your app is containerized, deployed to the Development stage, and a container image is stored in a registry. When you're ready to promote your app to the next stage your app deploys without the need to recompile code.

Apps in each stage are isolated from each other. When you publish an app to the Development stage, the apps running in Test or Production aren't impacted. Similarly, when you promote apps to Test or Production, apps in Development aren't impacted. 

## Deployment history

You can find a list of the apps' deployment history and status by navigating to **Delivery** > **Deployments**. The list is filtered by stage, but you can also  filter by status and date.

An app's deployment status can be one of the following:

* Running: the deployment is in progress, wait for it to finish.
* Finished with errors: the deployment has finished but it wasn't successful. Review the errors.
* Finished successfully: the deployment finished successfully. The app is available on the deployed stage.
