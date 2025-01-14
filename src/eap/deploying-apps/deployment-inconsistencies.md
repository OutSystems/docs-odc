---
helpids: 30474
summary: OutSystems Developer Cloud (ODC) ensures deployment consistency by analyzing and reporting potential inconsistencies during app deployment stages.
tags: deployment, impact analysis, consistency checking, deployment blockers, deployment warnings
locale: en-us
guid: c8999d32-bc1f-4bea-86bf-271b07035672
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - remember
---

# Guidance for deployment inconsistencies

When you deploy an asset (app or workflow) to a stage, ODC checks for inconsistencies between what you're deploying and what you previously deployed. For example, it checks for differences between names and elements.

When the impact analysis finishes, you can view how the inconsistencies might affect your assets. Using the information from the analysis report, you can make an informed decision and decide on the next best action.

On the **Deployment** screen, a history of the asset deployments and their status is displayed. You start by choosing an asset to deploy, then select the asset revision, and then ODC analyzes the impacts. 

The **Impact Analysis** report shows the results in sections. A section only displays if the analysis found an inconsistency. If no inconsistency is found, and the report indicates everything is OK, you can proceed.

The Impact Analysis report includes the following sections:

* **General**: Inconsistencies such as name collisions.

* **Workflows**: Inconsistencies related to workflows that depend on the asset you're deploying because they use one or more public elements.

* **Producer**: Inconsistencies related to other assets from which the asset you're deploying uses one or more public elements, such as a service action.

* **Consumer**: Inconsistencies related to other assets that depend on your deploying asset because they use one or more public elements, such as an entity.

You can also see if the severity of the inconsistency is a blocker or a warning.

* **Blockers** are inconsistencies that cause your asset to break in runtime. Therefore, ODC prevents you from proceeding with the deployment.

* **Warnings** are inconsistencies that may cause runtime errors in your assets. Therefore, ODC runtime errors might occur if those parts of your code get used. The deployment might be OK if, for example, you are using feature toggles to hide the code or if the code is a work in progress that you know isn't reachable from your assets. Therefore, ODC doesn't block you from proceeding with the deployment.

To learn more about reusing public elements across your assets, refer to [Reuse elements](../app-architecture/reuse-elements.md)

The following are the types of inconsistencies you might encounter. Each message includes a short description and instructions for fixing the inconsistency.

## Incompatible element
  
### Entity attribute mismatch

The consumer asset uses one or more attributes of an entity or static entity that doesn't exist in the producer asset. To fix this, you can either:

* Remove the missing attributes in the consumer asset.
* Add the missing attributes in the producer asset.

### Entity attribute type mismatch

The consumer asset expects an attribute with a different data type in the producer asset. To fix this, you can either:

* Change the attribute's data type in the consumer asset.
* Change the attribute's data type in the producer asset.

### Input parameter mismatch

The consumer asset uses one or more input parameters from an element that doesn't exist in the producer asset's definition. To fix this, you can either:

* Remove the missing input parameters in the service actions, screens, and events of the consumer asset.
* Add the missing input parameters in the service actions, screens, and events of the producer asset.

### Input parameter type mismatch

The consumer asset expects an input parameter with a different data type in the producer asset, and ODC cannot implicitly convert it at runtime. To fix this, you can either:

* Change the input parameter's data type in the consumer asset and review related service actions, screens, and events.
* Change the input parameter's data type in the producer asset and review related service actions, screens, and events.

### Missing mandatory input parameter

The producer asset defines an element with a mandatory input parameter that doesn't exist in the consumer asset. To fix this, you can either:

* Add the missing mandatory input parameter in the consumer asset.
* Make the input parameter optional.
* Remove the mandatory input parameter from the producer asset.

### Missing mandatory structure attribute

The producer asset defines a structure with a mandatory attribute that doesn't exist in the consumer asset. To fix this, you can either:

* Add the missing mandatory structure in the consumer asset.
* Make the structure attribute optional.
* Remove the mandatory structure from the producer asset.

### Missing record

The consumer asset uses a record from a static entity that doesn't exist in the producer asset's definition. To fix this, you can either:

* Remove the missing records from the static entities in the consumer asset.
* Add the missing records to the static entities in the producer asset.
  
### Output parameter mismatch

The consumer asset has a service action that uses one or more output parameters from an element that doesn't exist in the producer asset's definition. To fix this, you can either:

* Remove the missing output parameters in the service actions of the consumer asset.
* Add the missing output parameters in the service actions of the producer asset.

### Output parameter type mismatch

The consumer asset expects an output parameter with a different data type in the producer asset, and ODC cannot implicitly convert it at runtime. To fix this, you can either:

* Change the output parameter's data type in the consumer asset's service actions.
* Change the output parameter's data type in the producer asset's service actions.

### Record identifier mismatch

The consumer asset expects the identifier attribute of a static entity to be different from the one in the producer asset. To fix this, you can either:

* Add the identifier attribute of the static entity in the consumer asset's static entities.
* Remove the identifier attribute of the static entity from the producer asset's static entities

### Screen name mismatch

The name of a screen is different between the producer asset and the consumer asset. To fix this, you can either:

* Add the missing screen in the consumer asset.
* Add the missing screen in the producer asset.

### Screen URL discrepancy

The screen URL is different between the producer asset and the consumer asset. To fix this, you can either:

* Update the URL in the consumer asset to match the producer asset.
* Update the URL in the producer asset to match the consumer asset.
  
## Screen page name mismatch

When using custom URLs, the screen name is different between the producer asset and the consumer asset. To fix this, you can either:

* Add the missing screen in the consumer asset's screen page names.
* Add the missing screen in the producer asset's screen page names.

### Screen URL structure mismatch

When using custom URLs, the URL structure type of a screen is different between the producer asset and the consumer asset. To fix this, you can either:

* Add the missing screens in the consumer asset's screen URL structures.
* Add the missing screens in the producer asset's screen URL structures.

### Server entity name mismatch

The name of an entity is different between the producer asset and the consumer asset. To fix this, you can either:

* Add the missing entity in the consumer asset to match the producer asset.
* Add the missing entity in the producer asset to match the consumer asset.

### Static entity name mismatch

The name of a static entity differs between the producer and consumer assets. To fix this, you can either:

* Add the missing static entity in the consumer asset to match the producer asset.
* Add the missing static entity in the producer asset to match the consumer asset.

### Structure attribute mismatch

The consumer asset uses one or more attributes of a structure that do not exist in the producer asset. To fix this, you can either:

* Add the missing attributes in the consumer asset's structures.
* Add the missing attributes in the producer asset's structures.

### Structure attribute type mismatch

The consumer asset expects a structure attribute with a different data type in the producer asset, and ODC cannot implicitly convert it at runtime. To fix this, you can either:

* Change the structure attribute's data type in the consumer asset.
* Change the structure attribute's data type in the producer asset.

### Structure name mismatch

The structure's name differs between the producer asset and the consumer asset. To fix this, you can either:

* Add the missing structure in the consumer asset to match the producer asset.
* Add the missing structure in the producer asset to match the consumer asset.

## Missing element

### Missing event

The consumer asset uses an event that doesn't exist in the producer asset. To fix this, you can either:

* Remove the event in the consumer asset to match the producer asset.
* Add the event in the producer asset to match the consumer asset.

<div class="info" markdown="1">

Workflows only use events, screens, service actions, and roles from apps. Apps use events, screens, service actions, roles, entities, and structures.

</div>

### Missing role

The consumer asset uses a role that doesn't exist in the producer asset. To fix this, you can either:

* Remove in the consumer asset to match the producer asset.
* Add in the producer asset to match the consumer asset.

### Missing screen

The consumer asset uses a screen that doesn't exist in the producer asset. To fix this, you can either:

* Remove the missing screen in the consumer asset to match the producer asset.
* Add the missing screen in the producer asset to match the consumer asset.

### Missing server entity

The consumer asset uses an entity that does not exist in the producer asset. To fix this, you can either:

* Remove the missing server entity in the consumer asset to match the producer asset.
* Add the missing server entity in the producer asset to match the consumer asset.

### Missing service action

The consumer asset uses a service action that doesn't exist in the producer asset. To fix this, you can either:

* Remove the service action in the consumer asset to match the producer asset.
* Add the service action in the producer asset to match the consumer asset.

### Missing static entity

The consumer asset uses a static entity that does not exist in the producer asset. To fix this, you can either:

* Remove the static entity in the consumer asset to match the producer asset.
* Add the static entity in the producer asset to match the consumer asset.

### Missing structure

The consumer asset uses a structure that does not exist in the producer asset. To fix this, you can either:

* Remove the structure in the consumer asset to match the producer asset.
* Add the structure in the producer asset to match the consumer asset.

## General inconsistencies

### Name collision

There is another asset deployed in the target stage with the same name as the one being deployed. To fix this, you can either:

* Change the new asset's name.
* Change the existing asset's name.

<div class="warning" markdown="1">

This is a blocker for deploying your asset. To learn more about blockers, refer to [Impact analysis](deploy-apps.md#impact-analysis).

</div>

### URL discrepancy

The currently deployed version of the asset uses the same URL as another asset. To fix this, you can either:

* Change the new asset's URL.
* Change the existing asset's URL.

### Missing app

The consumer asset uses public elements from the producer asset, but the producer asset is either not deployed in the target stage or was deleted from the stage. To fix this, you can either:

* Remove the public elements from the consumer asset that are dependent on the missing app or library.
* Add the missing public elements to the producer asset and publish the updates.
