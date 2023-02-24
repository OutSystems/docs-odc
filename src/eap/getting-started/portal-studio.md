---
summary: Learn how to navigate ODC Portal and ODC Studio
tags:
locale: en-us
guid:f57be837-d09a-4ea7-aec8-2ca79b0921cd
app_type: web apps,  mobile apps
platform-version: odc
---

# ODC Studio Overview

<div class="info" markdown="1">

Before you start using ODC Studio, you need to have access to Outsystems Developer Cloud (ODC) environment.  You access ODC Studio from the ODC Portal. 

</div>

ODC Studio is a  low-code visual development environment that lets you:

* Create applications
* Create the user interfaces (UI) for Web and Mobile Apps
* Define the data model
* Define business processes and timers (batch processes)
* Debug your apps

## (REVIEW THIS NO LONGER WORKS LIKE THIS)
Before you open ODC Studio to start developing your app, you must have a username and your password and be authenticated in your organization.

After you successfully connect to ODC Studio, you see icons for all the applications that are on the server and for which you have access. In the Environment tab where you can:

## FROM P0RTAL - REWRITE OR MOVE OR BOTH0
* Create a new application.
* Install applications and components from the [OutSystems Forge](https://www.outsystems.com/forge/).
* View and access your existing applications.
* Install applications or components from the OutSystems Forge.


![ODC Studio development environment](images/service-studio-development-environment.png)

You can use the Search box on the top-left to find your application. The Search box is also available depends on the current stage. 

Once you create a new application or access an existing one, you navigate to the app detail screen:

![ODC Studio app details](images/service-studio-app-details.png)

In the app detail screen you have the following areas:

## App details

Edit button
:   Click to edit the name, description, icon, and bootstrap color of your application.

Delete button
:   Click to delete the app from your environment.

Download button
:   Click to download your app as an OutSystems Application Pack `.oap` file)

Test In Browser button
:   Click to open your application quickly in a browser for testing.

## App tabs

Develop tab
:   This is where you manage the modules of your application. You can also view the application's dependencies - other applications or components used by your application.

Distribute tab
:   In this area, you can generate your mobile app for iOS or Android. This is also where you turn on the PWA distribution of your app.

## The workspace

The workspace of Service Studio is where you design, deploy, and debug the modules of your applications.

![Service Studio workspace details ](images/service-studio-workspace-details.png)

The following areas organize the workspace:

### Main editor

Here is where you design the interface and logic of your application.

### Toolbar

Contains shortcuts to the most common operations.

### Toolbox

Contains the tools and widgets to develop the screens and logic of your application.

### Development tabs

This area displays the following tabs:
    
* TrueChange tab: displays the existing errors and warnings of your module. Double-clicking a specific error or warning takes you directly to that occurrence.

* Debugger tab: use this tab to debug your application. Here you can start the debugger and see the content of your variables step by step.

* 1-Click Publish tab: when you deploy your module, this area shows the progress and result of the deployment process.

* Search Results tab: lists the results of a search performed in the module. Double-clicking a specific result takes you directly to that occurrence.

### Status bar

Displays information about the user and the current environment, and when the application was last published.

### Application layer tabs

Each tab contains the elements of a specific application layer - processes, user interface, logic, and data model.

### Properties editor

Here you can view and set the properties of the selected element.

### 1-Click Publish button

Starts the deployment of your application module to the current environment. If your module has errors, this operation isn't available.

## Related information