---
summary: Learn to integrate external JavaScript libraries in ODC while avoiding DOM manipulation.
tags: integration, javascript, script management, external libraries, best practices
locale: en-us
guid: A8E1C4A8-CD24-4707-823B-6FD5702E7BE5
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/hdmSs8a8ifLQTmDBJmkJnD/Integration-with-external-systems?node-id=6601-138
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
---

# Use JavaScript Code from an External Library

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

<div class="info" markdown="1">

OutSystems doesn't recommend using JavaScript libraries that directly manipulate the DOM, such as jQuery. Such libraries can break Reactive and Mobile apps and make them difficult to maintain.

</div>

Before using JavaScript code from an external library or contained in a `.js` file, do the following:

1. Import or create a script under the **Scripts** tree folder. This script may reside in the app (that is, it was created using the context menu options "Create Script" or "Import Script", when right-clicking the "Scripts" folder), or can be a reference to a script defined in a library.

    ![Screenshot showing the context menu options to add a script in OutSystems, with 'Import Script' and 'Create Script' highlighted.](images/module-add-script-odcs.png "Adding a Script in OutSystems")

1. In the **Interface** tab, select the screen/block where you want to add the JavaScript code, and its properties select the script in the **Required Scripts** property:

    ![Screenshot of the OutSystems interface tab displaying the screen properties with the 'Select Required Script' dropdown expanded, showing 'Scripts.MyScript' as an option.](images/screen-add-required-script-odcs.png "Selecting a Required Script in OutSystems")

The script added as a required script is evaluated in the global scope.
Thus, you can use functions and objects initialized in this script in any JavaScript element of the screen/block.

## Loading of JavaScripts

The JavaScript imported as a required script is loaded with every other base script necessary for the app to launch.
Since the execution of the app is blocked until all defined JavaScripts are loaded, the defined scripts is available in **On Application Ready** system event.

The block required scripts and screen required scripts are loaded before the corresponding element is rendered.

## Execution of JavaScripts

In runtime, JavaScript in O11 apps is executed in a specific order depending on where it was added. The order is as follows:

1. Module required scripts

1. Block required scripts

1. Screen required scripts
