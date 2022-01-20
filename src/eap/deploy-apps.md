---
summary: Deploy your apps to stages using the Portal.   
tags:
---

# Deploy your apps

In Project Neo, you deploy your applications to stages. A stage (Dev, QA or Prod) is a step within your continuous delivery pipeline that includes Runtime resources. Project Neo includes three stages by default: development (Dev), Quality Assurance (QA), and production (Prod).

Project Neo has a single code repository. When you 1-Click Publish in Service Studio, your app is containerized, deployed to the Dev stage, and a container image is stored in a registry. When you're ready to promote your app to the next stage (for example, from Dev to QA), your app is deployed without the need to recompile code.

Apps in each stage are isolated from each other. When you publish an app to Dev, apps running in QA or Prod aren't impacted. Similarly, when you promote apps to QA or Prod, apps in Dev aren't impacted. Each stage is also isolated from the Platform. Project Neo separates Platform and Runtime resources, allowing development to scale independently of apps deployed to stages.

## View deployment status

The portal allows you to view the status of apps deployed from **Delivery** > **Deployments**. The apps list is filtered by stage, and you can further filter by status or date.

An app's deployment status can be one of three options:

* Running
* Finished with errors (??how do you troubleshoot in this case??)
* Finished successfully
