---
guid: 35892a80-96be-43bf-a89f-8d535b5b6f09
locale: en-us
summary: This article explains what are build action and how you can use build action to configure your mobile apps.
figma: 
coverage-type:
  - apply
  - understand
topic:
  - customize-mobile-apps
app_type: mobile apps
platform-version: odc
audience:
  - mobile developers
tags: Mobile,mobile app configuration,Extensibility
outsystems-tools:
  - odc studio
helpids: 
---

# Build Actions

You use Build Actions to configure mobile apps beyond what's available in the low-code environment. Build Actions use  YAML-based configuration file and a set of predefined constructs to define and apply modifications to a mobile app during the build process. 

Build Actions are integrated into the mobile app build process via **Advanced Extensibility**. The actions execute after the `cap sync` command during the build. 

## How build actions work

To use Build Actions, follow these steps:

1. Create a YAML file
 Define your build actions in a `config.yaml file`. Define variables at the root level of your YAML file using the `variables` property. These variables can be strings, numbers, arrays, or objects and can be referenced later in your build actions.  You also must include a `platforms` property to define platform-specific operations. The allowed child keys are `android` and `ios`.

1. Add the YAML file as a resource
In ODC Studio, add the YAML file as a resource. Set  **Deploy Action** to **Deploy to Target Directory**.

1. Configure Extensibility
Under **Extensibility** in app properties, add the configuration to resolve variables defined within the YAML file. `parameters` property is used to resolve the variables.

1. Build the app
Build the app in the ODC Portal. While building the package, ensure that you selected MABS 12 or greater.

### Conditional execution of build actions

Many build actions support conditional execution. This allows you to run an action only when a specified condition is met. The supported conditional expressions include:

eq: Checks if two arguments are equal (as strings).

ne: Checks if two arguments are not equal (as strings).

ge: Checks if the left argument is greater than or equal to the right (arguments must be numeric).

le: Checks if the left argument is less than or equal to the right (arguments must be numeric).

gt: Checks if the left argument is greater than the right (arguments must be numeric).

lt: Checks if the left argument is less than the right (arguments must be numeric).
 