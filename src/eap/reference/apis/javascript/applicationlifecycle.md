---
tags:
summary: OutSystems Developer Cloud (ODC) provides tools to manage the application lifecycle, including monitoring upgrades and customizing the loading process.
locale: en-us
guid: adf14b4f-4bef-4989-8ffe-9661392a4e54
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# ApplicationLifecycle

Provides information about the status of the application's lifecycle. Used to protect the app during upgrades, when local model access shouldn't be allowed, and to customize the application loading process.

Example:

```javascript
// Check if the app is currently being upgraded
var isUpgrading = $public.ApplicationLifecycle.isUpgradingVersion();

var progressCallback = function(loaded, total) {
  // do something on upgrade progress
};

var loadCompleteCallback = function() {
  // do something on finish
};

$public.ApplicationLifecycle.listen({
  onUpgradeProgress: isUpgrading ? progressCallback : null,
  onLoadComplete: loadCompleteCallback
});
```

## Summary

|Functions|Description|
|---|---|
|[isUpgradingVersion](#isupgradingversion)|Returns `true` if the application version is currently being upgraded. Used to determine the kind of feedback to provide when the application is initialized (e.g. splash screen).|
|[listen](#listen)|Registers listeners for application load events.|

## Functions

### isUpgradingVersion

**isUpgradingVersion(): boolean**

Returns `true` if the application version is currently being upgraded. Used to determine the kind of feedback to provide when the application is initialized (e.g. splash screen).

Returns: boolean

### listen

**listen(eventHandlers: [ApplicationLoadEventHandlers](applicationlifecycle.md#applicationloadeventhandlers)): void**

Registers listeners for application load events.

Parameters:

* **eventHandlers**: [ApplicationLoadEventHandlers](#applicationloadeventhandlers)<br/> Object containing callbacks for the application loading events you want to listen to.

Returns: void

## Type aliases

### ApplicationLoadEventHandlers

**ApplicationLoadEventHandlers: object**

An object containing event handlers to be called when the status of the application load changes.

Used in the [ApplicationLifecycle.listen](#listen) function.

#### (Optional) **onLoadComplete**: function

An optional callback for when the application is fully loaded and ready to use.

`(): void`

Returns: void

#### (Optional) **onUpgradeProgress**: function

An optional callback for when there is progress made during a version upgrade.

`(loaded: number, total: number): void`

Parameters:

* **loaded**: number - the number of files that have been upgraded so far.
* **total**: number - the total number of files to upgrade.

Returns: void

