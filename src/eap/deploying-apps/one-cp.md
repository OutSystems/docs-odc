---
summary: OutSystems Developer Cloud (ODC) simplifies app and library publishing with an automated 1-Click Publish feature.
tags:
  - 1-Click Publish
  - Data Synchronization
  - Deploy
  - Development lifecycle
  - Libraries
  - Lifecycle
locale: en-us
guid: 2c3f88e1-c53a-450d-9e36-ac83a7bf7a5d
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/file/B7ap11pZif6ZobXV6HC1xJ/Deploy-your-apps?type=design&node-id=3436%3A10&mode=design&t=4YrXFNtkgIwzVp3T-1
audience:
  - Developer
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - understand
  - apply
isautopublish: true
topic:
  - 1-click-publish-steps
  - odc-publish-message
---

# Understanding 1-Click Publish

1-Click Publish builds your app or library for the Development stage. Each publish that changes the asset stores a new revision. You can optionally add a message describing your changes when publishing.

## Publishing an app

OutSystems Developer Cloud (ODC) automates app publishing with its 1-Click Publish button. When you click the 1-Click Publish button to publish an app in the Development stage, the button initiates the following steps:

1. The ODC compiler compiles the app and generates HTML, CSS, JavaScript, and C# code while bundling the necessary libraries.
1. The ODC compiler produces a debug build of the revision. A debug build stores the compiled files directly, which supports differential builds and shortens publish time.
1. The ODC Data tool generates database scripts to synchronize the app's data schema with the code's version, ensuring data consistency.
1. The ODC Deployment tool deploys the debug build in the Kubernetes cluster using app configurations set in the ODC Portal. Simultaneously, the ODC Data tool starts executing the database scripts.

![Diagram illustrating the app publishing workflow after 1-Click Publish in ODC, showing steps from ODC Studio to Kubernetes deployment.](images/1-click-publish-diag.png "App Publishing Workflow Diagram")

<div class="info" markdown="1">

In a multi-portfolio organization, refer to [Asset deployment with multiple portfolios](../manage-platform-app-lifecycle/portfolios/portfolios-deploy-assets.md).

</div>

Stages other than Development run release builds, which package a revision as a container image. Each deployment fetches the existing build and runs the database scripts for the target stage. When you deploy your app from the Development stage to the QA stage, ODC follows these steps:

1. ODC retrieves the release build for the selected revision of the app.
1. ODC generates and executes the database scripts for the QA stage.
1. ODC updates app configurations for the QA stage as per your updates in the ODC Portal.
1. ODC integrates the updated configurations into the container image and deploys it to the QA stage.

The **Deployments** screen shows these steps for each deployment, to Production as well as QA.

## Publishing a library

When you click the 1-Click Publish button to publish a library, ODC initiates the following steps:

1. The ODC compiler compiles the library and generates HTML, CSS, JavaScript, and C# code while bundling the necessary libraries.
1. The ODC compiler stores the result as a self-contained package.

A library reference is a strong reference, so ODC merges the library's package into the container of each asset that consumes it. A library runs inside its consumers, so the consuming asset owns the database scripts that ODC generates. Libraries define static entities that act as enumerations, and data storage and queries stay with the consuming app.

To make a library's elements available to other assets, you release it in the ODC Portal. For more information, refer to [Release a new version of a library](../building-apps/libraries/libraries.md#release-library).

## Adding a message when publishing

You can add a message when publishing to describe the changes you made. Messages help your team understand the intent behind each revision, improving traceability and collaboration.

![Screenshot of ODC Studio showing the Publish dropdown with 1-Click Publish and 1-Click Publish with Message options](images/publish-with-comment-odcs.png "1-Click Publish with Message in ODC Studio")

To publish with a message, do one of the following in ODC Studio:

* Click the dropdown arrow on the **Publish** button and select **1-Click Publish with message**.
* Press **Shift+F5** (Windows) or **Shift+Cmd+F5** (macOS).

In the dialog that opens, type your message and publish. The message is optional and supports up to 2,000 characters. After publishing, the message becomes a permanent, read-only record of that revision.

To review messages, open ODC Studio and go to **App** > **View revisions**.
