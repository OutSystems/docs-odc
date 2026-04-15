---
summary: Analyze code quality in OutSystems Developer Cloud (ODC) for performance, architecture, maintenance, and security insights.
tags: code quality, ai mentor system, code analysis, odc, performance
guid: CA38C82A-E390-425B-B588-D6BD3F692928
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3621-877
coverage-type:
  - understand
  - apply
audience:
  - full stack developers
  - platform administrators
  - tech leads
outsystems-tools:
  - odc studio
  - odc portal
topic:
  - manage-tech-debt
---

# Setting up Code quality

To get started with **Code quality** in ODC, you must first activate it in your organization. Once activated, **Code quality** analyzes your code for patterns related to performance, architecture, maintainability, and security.

<div class="info" markdown="1">

Code quality uses the Data platform, which may process data outside your ODC organization region to provide its capabilities. For more information, refer to [Data platform](../../manage-platform-app-lifecycle/platform-architecture/intro.md#data-platform).

</div>

## Prerequisites

To activate **Code quality**, you must have the **View Code Quality findings** permission.

## Activating Code quality

To activate **Code quality**, follow these steps:

1. In the Portal, go to **Analyze** > **Code quality**.

1. Click **Activate code quality**.

    ![Activate code quality button in the ODC Portal with a description of code quality analysis.](images/aims-activation-pl.png "Activate Code Quality")

Code quality is activated and begins analyzing your apps. The initial analysis may take several minutes, depending on the number and size of your apps. Once complete, you can view the results on the Code quality dashboard. For more information about the **Code quality** dashboard, refer to [Working with Code quality](working-with-code-quality.md).

## Known limitations

* **App analysis frequency.** App analysis runs every 12 hours. After performing a 1CP (1-Click Publish), you must wait until the next scheduled analysis to view the updated findings in the **Code quality** Console.
* **Availability of resolved findings.** Resolved findings are retained in the Code Quality Console for up to 90 days. After this period, they are no longer available.
* **Detection of new code patterns**. Newly introduced code patterns aren't detected retroactively for existing apps. To detect these patterns, perform a 1-Click Publish on the respective app.

## Known issues

* **Flow visualization rendering**. Flow visualization may fail to render findings that are older than 90 days in the console. To resolve this issue, perform a 1-Click Publish on the affected apps.

## Related resources

* [Working with Code quality](working-with-code-quality.md)

* [Getting started with Code quality as a technical lead](getting-started-aims-tl.md)

* [Getting started with Code quality as a developer](getting-started-aims-dev.md)
