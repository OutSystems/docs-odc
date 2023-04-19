---
summary: You can delete apps and libraries through the ODC Portal, with the delete permission in the development or QA stages. 
tags:
locale: en-us
guid: F5E3A7C3-EE70-42AC-A891-FFA5CC7AD64A
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Deleting apps and libraries

During the development process, you may create apps or libraries for testing. As time goes on, you may no longer need these apps or libraries. OutSystems Developer Cloud (ODC) lets you safely delete apps, and libraries from the Development and QA stages. Having a clean stage makes it faster to find the apps and libraries you need.

To delete an app or library, go to the ODC Portal and select the app or library you want to delete. From the details screen, click the three-dots in the upper-right corner and select **Delete**.


## What you can delete

To ensure you don’t accidentally delete an app or library that might be in use, ODC comes with some safety mechanisms. Only roles with permission to delete apps can delete apps and libraries. If you don’t have permission, then you won’t see the delete option. Your Organization may have rules that determine who can have this permission. To verify if you can have access, contact your ODC administrator.

In addition, to having the correct permission, you can only **delete an app** if:

* It's not a system app, such as OutSystems Sample Data
* It hasn’t been deployed beyond the QA stage
* If it has no unresolved blockers and dependencies
  
You can also **delete an app template** if it isn’t:

* A system app template such as a Web app template
* A Phone app template
* A Table app template
* A Screen template for Mobile
* A Web apps
  
 <div class="info" markdown="1">

Keep the following in mind when deleting apps and libraries:

* A library's code and configurations are bundled with the app's container image. Deleting a library doesn't immediately affect the consumer apps that display in the list with warnings at runtime.
* When you delete a library, its settings and configurations can't be changed.
* From the ODC Portal, if you open the detail page of any of these consumer apps and try to retrieve the apps configuration, an error code (OS-CFGM-40406) displays.
* When you delete an app or library you are deleting it from your Organization. Your app or library is still available from the **My Assets** page in Forge.
* When you delete the app or library you lose all historical data.

</div>

## Impact analysis

To help you determine if performing a delete causes any issues, ODC runs an impact analysis before the deletion. This analysis checks for any dependencies that might be impacted by deleting an app or library.

First, you select the app or library you want to delete. ODC displays a details page that shows configurations (apps only), consumers, and producers.

On the Consumer and Producer tabs, you see what consumers might be impacted by the delete. When you select the app or library and then select **Delete**, the impact analysis runs and checks for blockers and warnings.

A **Warning** indicates that there is a problem, but you can delete the app or library. Before continuing, you should refactor the app or library. The warning identifies the app or library needing refactoring. When you continue with the **Delete**, ODC prompts you to confirm the deletion by entering the name of the app or library you want to delete.

A **Blocker** indicates that you can't delete the app or library until you resolve the dependency from the app that's blocking the delete. This happens when the app that's blocking the delete was already deployed beyond the QA stage with a dependency for the asset you want to delete.

To help you determine how best to remove the dependency, you can download an analysis report. The report provides details about the dependency. To remove blockers and delete the app you must remove the dependency between the consumers (direct or indirect) and the app or library. You must also deploy the app to the stages on which it was originally deployed.

You remove the dependency in the development stage. But, if apps are **blocking** the delete, it's because they're deployed and still have those dependencies in other stages. To remove the dependencies, you must deploy your app again.
