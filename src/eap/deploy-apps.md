---
summary: Deploy your apps to stages using the ODC (OutSystems Developer Cloud) Portal. Analyze impact of deployment for other apps and consumers.
tags:
locale: en-us
guid: d0aa50bf-0378-4bb9-8c4f-71b37092dd8b
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Deploy your apps

Use ODC Portal to deploy your apps. In OutSystems Developer Cloud (ODC), you deploy your apps to stages. A stage is a step within your delivery pipeline that includes runtime resources. ODC includes three stages by default: Development, QA, and Production.

ODC has a single code repository. When you deploy in ODC Studio, your app is containerized, deployed to the Development stage, and a container image is available. When you're ready to deploy your app to the next stage your app deploys without the need to recompile code again.  Libraries are also packaged in the same container as an app.

Apps in each stage are isolated from each other. When you publish an app to the Development stage, there is no impact to the apps running in QA or Production. Similarly, publishing apps to QA or Production doesn’t affect apps in Development.

Libraries contain functionality that's business agnostic so that you can use the same library with multiple apps. Libraries don't hold data, and can't use entities. You can define themes, UI patterns, and blocks in libraries.

## Deploy to stages

You use ODC Studio to create and publish your apps. Then you use the ODC Portal to deploy and move your apps to the different stages. 

In ODC Studio, when you build an app and then click **1 Click Publish**, your app becomes available in the Development stage. You can only publish to development and then deploy to other stages. Deploying to another stage only moves the apps runtime.

To deploy your app to a stage, go to the ODC Portal and click **Deployments**. A list of apps displays showing their stage, status, when deployed, and who deployed it. From the top right, choose the stage to which you want to deploy your app. The next Deployment screen provides you with instructions to deploy your app to a stage.

1. Click the app you want to deploy. A list of available revisions for your app displays.
1. Click  the revision of the app you want to deploy, and click **Continue**. The app with the revision you chose displays.  
1. When ready, click **Deploy Now**. Your app gets deployed to your selected stage. Optionally, if deploying to production you can change the version number before deploying. The [Impact analysis](#impact-analysis) runs when you click **Deploy Now**. 

<div class="info" markdown="1">

A deployment status displays. You can also click **View app** to see your deployed app.

</div>  

## Versions and Revisions

Versions and revisions help you keep track of changes in your apps and libraries and is beneficial when you develop digital assets.

App versions can only be deployed to Development. For QA and Production stages, you choose a revision that you want to deploy from the list of available revisions.

Version numbers are a 3-part number (2.1.1) that you can change to meet your needs. For example, suppose you create an app using a different product and the current version number is 3.1.1. Now you create the same app in ODC, and when you publish the app, ODC gives it a version number starting with "1" such as 1.1.1. You can modify this number to a different sequence number such as 4.1.1 to prevent conflicts with your previously published app.

Revision numbers are whole numbers that display below the name of the app on the Deployments screen.  This makes it easy for you to select the revision you want to deploy to the next stage.

## Impact analysis

ODC automatically runs an impact analysis when you deploy an app in ODC Portal. The impact analysis checks for dependency issues that might cause runtime errors in your app or its consumers. By identifying issues that might negatively impact your apps or the consumers, you can deliver better-performing apps. The analysis provides information for blockers and warnings.

**Blockers** prevent you from deploying your app. For example, a blocker occurs when there is an app name collision. This indicates another app on the target stage has the same name as the app you are deploying.

**Warnings** provide information but allow you to proceed. Warnings are mostly about [producers and consumers](building-apps/data/sharing.md). For example, a warning can occur in any of the following situations:

* Your app references other apps (producers) with missing or incompatible.
* Other apps (consumers) reference your app and have missing or incompatible elements.

To review the analysis, choose the app, then choose the revision, and click  **Analyze impact**. A list of blockers and warnings show in order of severity. First, you see the blockers and then the warnings, and in each section, you see producer issues followed by consumer issues.

Developers then review the impact analysis and make a deployment decision. If there are no blockers, the **Deploy Now** button becomes enabled. But, depending on the warnings, developers might not want to continue.

For example, developers might see some unexpected warnings and decide to fix the issues in ODC Studio before continuing with the deployment. Depending upon the warning, such as a missing app, developers might decide to deploy the missing app first. In this case, you can click the **Choose App** button to return to the **App** page and deploy the missing app. Then developers can deploy the original app.  

## Deployment status

An app's deployment status can be one of the following:

* **Running:** the deployment is in progress; wait for it to finish.
* **Finished with errors**: the deployment has finished, but it wasn't successful. Review the errors.
* **Finished successfully**: the deployment finished successfully. The app is available in the deployed stage.

Log information is available for each deployment listed by clicking the row for which you want more information.
