---
helpids: 30474
summary: OutSystems Developer Cloud (ODC) ensures deployment consistency by analyzing and reporting potential inconsistencies during app deployment stages.
tags:
locale: en-us
guid: c8999d32-bc1f-4bea-86bf-271b07035672
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
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

* **Blockers** are inconsistencies that cause your app to break in runtime. Therefore, ODC prevents you from proceeding with the deployment.

* **Warnings** are inconsistencies that may cause runtime errors in your apps. Therefore, ODC runtime errors might occur if those parts of your code get used. The deployment might be OK if, for example, you are using feature toggles to hide the code or if the code is a work in progress that you know isn't reachable from your apps. Therefore, ODC doesn't block you from proceeding with the deployment.

The following are the types of inconsistencies you might encounter. Each message includes a short description to provide you with guidance.


## Incompatible element
  
### Entity attribute mismatch

* **Description:** The consumer app uses one or more attributes of an entity or static entity that don't exist in the producer app's definition.

### Entity attribute type mismatch

* **Description:** The consumer app expects an attribute from the producer's entity or static entity. The consumer's data type differs from the element's definition in the producer app. ODC is unable to implicitly convert it at runtime.

### Input parameter mismatch

* **Description:** The consumer asset uses one or more input parameters from an element that doesn't exist in the producer asset's definition. This can occur on screens and in service actions.

### Input parameter type mismatch

* **Description:** The consumer asset expects an input parameter from an element, but the data type in the producer asset has a different definition. ODC can't implicitly convert it at runtime. This can occur in screens and in service actions.

### Missing mandatory input parameter

* **Description**: The producer asset defines an element that has a mandatory input parameter, but that parameter doesn't exist in the consumer asset. This can occur in screens and in service actions.
  
### Missing mandatory structure attribute

* **Description:** The producer app defines a structure with a mandatory attribute, but that attribute doesn't exist in the consumer app.

### Missing record

* **Description:** The consumer app uses a record from a static entity that doesn't exist in the producer app's definition.
  
### Output parameter mismatch

* **Description:** The consumer asset has a service action that uses one or more output parameters of an element that doesn't exist in the producer asset's definition.

### Output parameter type mismatch

* **Description** The consumer asset expects an output parameter from an element whose data type is different from the element's definition in the producer asset, and ODC isn't able to implicitly convert it at runtime. This can occur in service actions.

### Record identifier mismatch

* **Description:** The consumer app expects the identifier attribute from the static entity to be different from the producer app's definition.


### Screen name mismatch

* **Description:** The name of a screen is different between the producer asset and the consumer asset.

### Screen URL discrepancy

* **Description**: The screen URL is different between the producer asset and the consumer asset.
  
## Screen page name mismatch

* **Description:** When using customer URLs, the screen name is different between the producer asset and the consumer asset.


### Screen URL structure mismatch

* **Description:** When using Custom URLs, the URL structure type of a screen is different between the producer asset and the consumer asset.

### Server entity name mismatch

* **Description:** The name of a static entity is different between the producer app and the consumer app.

### Structure attribute mismatch

* **Description:** The consumer app uses one or more attributes of a structure that doesn't exist in the producer app's definition.

### Structure attribute type mismatch

* **Description:** The consumer app expects an attribute of a structure data type. But, the data type is different from the element's definition in the producer app. ODC isn't able to implicitly convert it at runtime.

### Structure name mismatch

* **Description:** The name of a structure is different between the producer app and the consumer app.

## Missing element

### Missing event

* **Description:** The consumer asset uses an event that doesn't exist in the producer asset.

    **Note**: Workflows only use events, screens, service actions, and roles from apps. Apps use events, screens, service actions, roles, entities, and structures.


### Missing role

* **Description:** The consumer asset uses a role that doesn't exist in the producer asset.

### Missing screen

* **Description:** The consumer asset uses a screen that doesn't exist in the producer asset.

### Missing server entity

* **Description:** The consumer app uses an entity that doesn't exist in the producer app.

### Missing service action

* **Description:** The consumer asset uses a service action that doesn't exist in the producer asset.
 
### Missing static entity

* **Description:** The consumer app uses a static entity that doesn't exist in the producer app.

### Missing Structure

* **Description:** The consumer app uses a structure that doesn't exist in the producer app.

## General inconsistencies

### Name collision

* **Description:** An app already deployed in the target stage has the same name as the app being deployed. This is causing a name collision with the derived app URL.

### URL discrepancy

* **Description:** Another app already deployed in the target stage has the same URL as the App being deployed.

### Missing app

* **Description:** The consumer app uses public elements from the producer app, but the producer app is either not deployed in the target stage or was deleted from the organization.
