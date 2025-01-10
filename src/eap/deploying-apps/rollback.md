---
summary: OutSystems Developer Cloud (ODC) allows you to rollback apps in ODC Portal.
tags: rollback, versioning, dependency management, application deployment, odc
guid: 340707ce-9540-4d8e-a025-aba9119da926
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/B7ap11pZif6ZobXV6HC1xJ/Deploy-your-apps?node-id=3496-71&t=XDhAhNM4YGofhRUm-1
coverage-type:
  - understand
audience:
  - full stack developers
  - platform administrators
outsystems-tools:
  - odc portal
---
# Rollback apps

When apps have dependencies, managing versions is critical to ensure stability. An update to one app can unintentionally cause errors in another app, especially when dependencies exist between apps. Rolling back is necessary when an update introduces issues, such as compatibility problems between dependent apps. If an app crashes or behaves unexpectedly after an update, rolling back to a previous version is the fastest way to restore functionality.

 Versioning allows you to manage backward compatibility, control changes, and roll an app back in case of deployment issues. This ensures smoother and more predictable updates.

![Diagram of rolling back an app in ODC Portal example](images/rollback-asset-odcs.png "Example application rollback")

For example, consider App A, which depends on App B. You publish a new version for App B, which causes deployment inconsistencies with App A. To fix this, you must roll App B back to a stable version.

To roll an app back, follow these steps:

1. Go to the ODC Portal and click **Deployments**. 

1. From the **Deploy to** dropdown, select the stage to which you want to deploy your app.

1. Select the app you want to deploy.

1. Select the revision you want to rollback to and click **Continue**. 

1. To rollback the app, click **Deploy Now**. 

For more information about the deploying apps, refer to [Deploying apps](deploy-apps.md).
