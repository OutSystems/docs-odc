---
summary: Deploy your apps to stages using the Portal.   
tags:
---

# Deploy your apps
 
In Project Neo, you deploy your applications to stages. A stage (Dev, QA or Prod) is a step within your continuous delivery pipeline that includes Runtime resources. Project Neo includes three stages by default: development (Dev), Quality Assurance (QA), and production (Prod).
 
Project Neo has a single code repository. When you click 1-Click Publish in Service Studio,The code is containerized, deployed to the Dev stage, and a container image is stored in a registry. When you're ready to promote your app to the next stage (for example, from Dev to QA), your app is deployed without the need to recompile code.
 
Apps in each stage are isolated from each other. When you publish an app to Dev, apps running in QA or Prod aren't impacted. Additionally, when you promote apps to QA or Prod, apps in Dev aren't impacted. Each stage is also isolated from the Platform. Project Neo separates Platform and Runtime resources, allowing development to scale independently of apps deployed to stages, and enabling pain-free upgrades.
 
## Promoting apps
 
To promote an app to the QA or Prod stage:
 
1. Go to the Portal.
2. Go to **Delivery** > **Deployments**.
3. Select the app you want to promote, and then follow the guided staging process in the UI.
 
