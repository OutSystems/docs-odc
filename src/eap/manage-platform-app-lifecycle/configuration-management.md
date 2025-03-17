---
summary: OutSystems Developer Cloud (ODC) enables efficient app configuration management without the need for redeployment.
tags: configuration management, deployment, infrastructure management, app settings, stage-specific configuration
locale: en-us
guid: e32e1f5f-83b6-4b00-a593-83ba5017fc16
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/AOyPMm22N6JFaAYeejDoge/Configuration-management?type=design&node-id=2449%3A32709&t=hXGTDybYCg38Lul5-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - understand
topic:
  - changing-endpoints
  - app-settings
---

# Configuration management

OutSystems Developer Cloud (ODC) Portal lets you adjust the configuration values for your apps. Changes to configuration values don't require you to redeploy your app. This increases the speed in which changes to the app are available to customers and reduces the number of times a deployment is necessary.

You configure the supporting infrastructure for your apps at the stage level. Supporting infrastructure includes custom domains and external identity providers. Applying a configuration to a stage applies to all the apps deployed to that stage.

## How configuration management works

For app configurations, developers create settings with default values in ODC  Studio. From the ODC Portal, you select the stage on which you want to work. Then you can view and modify some configuration and settings values for apps deployed on that stage.

You can override the configuration values from ODC Studio in non-development stages. When you deploy your app to Test, you can change the configuration values to mirror production values for testing and troubleshooting. Then when you move this configuration to Production you can change your values using real data. The changes you make are specific to a stage. This process occurs without needing to publish your app again.

![How configuration management works](images/config-management-works-diag.png "How configuration management works")

App configurations can use one of the following values:

* **Default**. The value set in ODC Studio for the configuration. You can use this value in any of your stages, such as Development, Test, or Production.

* **Current**. The value currently in use, if defined, otherwise the default value is the current value in use.

The values you change take effect when the asynchronous apply process completes. The apply process saves the new values and updates the configuration.

![Apply configurations](images/config-management-apply-diag.png "Apply configurations")

## Managing settings

Settings are custom public values that change the behavior of the app or library in a stage. Once you create the setting values in ODC Studio and publish the app, you can override the default values in the ODC Portal without having to republish or redeploy the app.

For more information about configuring app settings, refer to [Configure app settings](configure-app-settings.md).

## Managing timers

Timers execute logic in apps. In ODC Studio, your developers set the default values for the timers. For example, you can use timers to:

* Run batch tasks
* Run logic in an app at a specific time
* Start actions that are machine intensive during high availability times
* Set how long a task should run before it times out

You can change the values in the ODC Portal. Access timers from the **Configuration** tab in ODC Portal. When you open the **Timers** section, a list of timers displays along with the schedule name and status. When you click on the name of a timer, the current values display in the sidebar.

<div class="info" markdown="1">

When you deactivate a timer on the ODC Portal, you prevent it from running.

</div>

## Managing REST integrations

In the ODC Studio, you define which systems you want to integrate with to present an integrated view of the data or provide data to another system. From the ODC Portal, the REST information you see is for the app on the selected stage.

To access the list of REST integrations, go to the **Configuration** tab for your app. From here you can get access to the **Consumed REST APIs**. The bubble to the right of the section name shows the number of APIs in each category.

When you click **Consumed REST APIs**, a list of the consumed APIs displays. To manage a Consumed REST integration, click on the integration name. The sidebar opens for you to make updates. When you apply your changes, ODC saves them, and your new Consumed REST integrations settings are available.
