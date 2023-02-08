---
summary: You can delete apps and libraries through ODC Portal. You need to have a delete permission and you can delete apps or libraries in the development stage only. 
tags:
locale: en-us
guid: F5E3A7C3-EE70-42AC-A891-FFA5CC7AD64A
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Deleting apps and libraries

During the development process, you may create apps or libraries for testing. As time goes on, these apps or libraries may no longer be needed. OutSystems Developer Cloud (ODC) lets you safely delete apps, libraries, and with them data from the Development stage. Having a clean stage saves on resources and makes it faster to find the apps and libraries you need.

To delete an app or library first go to the ODC Portal and select the app or library you want to delete. In the details screen, click the three-dots button in the upper-right corner and select **Delete**. There are three likely outcomes:

* You can delete your app or library if it contains no dependencies or consumers.
* You can still delete your app or library in case of a warning. It raises errors in the dependent apps and libraries. 
* You can’t delete your app or library in case of a blocker. The deletion can affect other app and user data.

## What you can delete

To ensure you don’t accidentally delete an app or library that might be in use, ODC comes with some safety mechanisms. Only roles with permission to delete apps can delete apps and libraries. If you don’t have permission, then you won’t see the delete option. Your organization may have rules that determine who can have this permission. To verify if you can have access, contact your system admin.

In addition, to having the correct permission, you can only **delete an app** if:

* It's not a system app, such as OutSystems Sample Data
* It hasn’t been deployed beyond the Development stage
* It has dependencies that haven't been deployed beyond Development stage

You can also **delete an app template** if it isn’t a system app template such as a web app template, a Phone app template, a Table app template, a Screen template for Mobile or Web apps.

 <div class="info" markdown="1">

Keep the following in mind when deleting a library:

*  A library's code and configurations are bundled with the app's container image. Deleting a library doesn't immediately affect the consumer apps that display in the list with warnings at runtime. 
*  When you delete a library, its settings and configurations can't be changed.
*  From the ODC Portal, if you open the detail page of any of these consumer apps and try to retrieve the apps configuration, an error code (OS-CFGM-40406) displays.

</div>

## Impact analysis

To help you determine if performing a delete causes any issues, ODC runs an impact analysis before the delete operation takes place. This analysis checks for any dependencies with apps that might be impacted by deleting an app or library.

First, you select the app or library you want to delete. ODC displays a details page that shows Configurations (apps only), Consumers, and Producers.

On the Consumer and Producer tabs, you see what consumers might be impacted by the delete. When you select the app or library and then select **Delete**, ODC runs the impact analysis and checks for any blockers or warnings.

A **Warning** indicates that you can still delete the app or library. You need to refactor the app the warning refers to, as the app depends on the app or library you are deleting in the Development stage. When you continue with the **Delete**, ODC prompts you to confirm the deletion by entering the name of the app or library you want to delete.

A **Blocker** indicates that you can't delete the app or library before removing the dependency from the app that's blocking the delete. This happens because the app that's blocking the delete was already deployed beyond the Development stage with a dependency for the asset being deleted.

To help you determine how best to remove the dependency, an analysis report is available for download. The report provides details about the dependency. For blockers, besides removing the dependency between that consumer (direct or indirect) and the app or library you are trying to delete, you need to deploy the app to the stages on which it was originally deployed.

You remove the dependency in the development stage. But, if apps are **blocking** the delete, it's because they're deployed and still have those dependencies in other stages. To remove the dependencies, you must deploy your app again.
