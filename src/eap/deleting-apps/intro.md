---
summary: OutSystems Developer Cloud (ODC) enables safe deletion of apps and libraries from non-production stages, with built-in safety mechanisms and impact analysis.
tags: application lifecycle management, development stage management, access control, deployment
locale: en-us
guid: F5E3A7C3-EE70-42AC-A891-FFA5CC7AD64A
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - odc portal
coverage-type:
  - understand
topic:
  - delete-apps-libraries
---

# Deleting apps and libraries

During the development process, you may create apps or libraries for testing. As time goes on, you may no longer need these apps or libraries. OutSystems Developer Cloud (ODC) lets you safely delete apps, and libraries from stages such as Development. You can't delete apps and libraries from your Production stage. Having a clean stage makes it faster to find the apps and libraries you need.

To delete an app or library, open ODC Portal and select **Apps** from the left nav menu. Click on the app or library you want to delete. In the details screen that opens click the three-dots in the upper-right corner and select **Delete app** or **Delete library**.

You cannot delete apps and libraries deployed to the Production stage.

* To delete an app already deployed to Production, you must first undeploy the app from the Production stage.
* To delete a library already deployed to Production, you must first update all consumers of the library deployed to the Production stage, remove the dependency to the library from those consumers, and then promote those new revisions to the Production stage.

## What you can delete

To ensure you don’t accidentally delete an app or library that might be in use, ODC comes with some safety mechanisms. Only roles with permission to delete apps can delete apps and libraries. If you don’t have permission, then you won’t see the delete option. Your Organization may have rules that determine who can have this permission. To verify if you can have access, contact your ODC administrator.

In addition, to having the correct permission, you can only **delete an app** if:

* It's not a system app, such as OutSystems Sample Data
* It hasn’t been deployed to the Production stage
* If it has no unresolved blockers and dependencies

You can also **delete an app template** if it isn't a system app template, such as a Template Web App, or a screen template, such as Screen Templates Web.

 <div class="info" markdown="1">

Keep the following in mind when deleting apps and libraries:

* The delete operation is irreversible and non-recoverable. This means permanently deleting historical data, all app revisions, and the app's data in the database.
* A library's code and configurations are bundled with the app's container image. Deleting a library doesn't immediately affect the consumer apps that display in the list with warnings at runtime.
* When you delete a library, its settings and configurations can't be changed.
* From the ODC Portal, if you open the detail page of any of these consumer apps and try to retrieve the apps configuration, an error code (OS-CFGM-40406) displays.
* When you delete an app or library, you remove it only from your Organization. If the app or library is a Forge component, whether from a third party or one you've published to the Forge, the delete operation does not remove the component from the Forge.

</div>

## Impact analysis

To help you determine if performing a delete causes any issues, ODC runs an impact analysis before the deletion. This analysis checks for any dependencies that might be impacted by deleting an app or library.

First, you select the app or library you want to delete. ODC displays a details page that shows configurations (apps only), consumers, and producers.

On the Consumer and Producer tabs, you see what consumers might be impacted by the delete. When you select the app or library and then select **Delete**, the impact analysis runs and checks for blockers and warnings.

A **Warning** indicates that the impact analysis has detected a potential impact. You can proceed with the delete operation but should evaluate these warnings carefully. Proceeding with the delete operation can result in runtime errors on the consumers of the app or library you are deleting.

It's necessary to refactor the consumers of the app or library to address the warning and remove the dependency causing it. You can perform this task before or after completing the delete operation. When you proceed with the deletion, you'll be prompted to confirm by entering the name of the app or library you're deleting.

A **Blocker** indicates that you cannot delete the app or library until you resolve the dependency from the app blocking the deletion. This happens when the app blocking the delete is already deployed to the Production stage with a dependency on the asset you want to delete.

To help you determine how best to remove the dependency, you can download an analysis report. The report provides details about the dependency. To remove blockers and delete the app you must remove the dependency between the consumers (direct or indirect) and the app or library. You must also deploy the app to the stages on which it was originally deployed.

You remove the dependency in the development stage. But, if apps are **blocking** the delete, it's because they're deployed and still have those dependencies in other stages. To remove the dependencies, you must deploy your app again.
