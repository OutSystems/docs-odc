---
summary: Deploy your apps to stages using the Portal. Analyze impact of deployment for other apps and consumers.
tags:
locale: en-us
guid: d0aa50bf-0378-4bb9-8c4f-71b37092dd8b
app_type: mobile apps, reactive web apps
---

# Deploy your apps

<div class="info" markdown="1">

Project Neo documentation is under construction. It's frequently updated and expanded.

</div>

Use Portal to deploy your apps. In Project Neo, you deploy your apps to stages. A stage is a step within your delivery pipeline that includes runtime resources. Project Neo includes three stages by default: Development, Test, and Production.

Project Neo has a single code repository. When you publish in Service Studio, your app is containerized, deployed to the Development stage, and a container image is available in a registry. When you're ready to promote your app to the next stage your app deploys without the need to recompile code.

Apps in each stage are isolated from each other. When you publish an app to the Development stage, there is no impact to the apps running in Test or Production. Similarly, promoting apps to Test or Production doesn’t affect apps in Development.

## Impact analysis

Project Neo automatically runs an impact analysis when you deploy an app in Portal. The impact analysis checks for dependency issues that might cause runtime errors in your app or its consumers. By identifying issues that might negatively impact your apps or the consumers, you can deliver better-performing apps. The analysis provides information for blockers and warnings.

**Blockers** prevent you from deploying your app. For example, a blocker occurs when there is an app name collision. This indicates another app on the target stage has the same name as the app you are deploying.

**Warnings** provide information but allow you to proceed. Warnings are mostly about [producers and consumers](./building-apps/data/sharing.md). For example, a warning can occur in any of the following situations:

* Your app references other apps (producers) with missing or incompatible.
* Other apps (consumers) reference your app and have missing or incompatible elements.

To review the analysis, choose the app, then choose the revision, and click  **Analyze impact**. A list of blockers and warnings show in order of severity. First, you see the blockers and then the warnings, and in each section, you see producer issues followed by consumer issues.

Developers then review the impact analysis and make a deployment decision. If there are no blockers, the **Deploy Now** button becomes enabled. But, depending on the warnings, developers might not want to continue.

For example, developers might see some unexpected warnings and decide to fix the issues in Service Studio before continuing with the deployment. Depending upon the warning, such as a missing app, developers might decide to deploy the missing app first. In this case, you can click the **Choose App** button to return to the **App** page and deploy the missing app. Then developers can deploy the original app.  

## Deployment status

An app's deployment status can be one of the following:

* **Running:** the deployment is in progress; wait for it to finish.
* **Finished with errors**: the deployment has finished, but it wasn't successful. Review the errors.
* **Finished successfully**: the deployment finished successfully. The app is available in the deployed stage.

Log information is available for each deployment listed by clicking the row for which you want more information.
