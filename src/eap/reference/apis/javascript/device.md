---
tags:
summary: Explore device capabilities in OutSystems Developer Cloud (ODC) with the `whenReady` function, ensuring native API readiness.
locale: en-us
guid: 013451b7-0d79-423f-9f0b-745024729929
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# Device

<div class="info" markdown="1">

Applies to Mobile Apps only

</div>

Provides functions to access native capabilities of a mobile device.

## Summary

|Functions|Description|
|---|---|
|[whenReady](#whenready)|Promise that is resolved when the 'deviceready' event is caught.|

## Functions

### whenReady

**whenReady(): Promise&lt;void&gt;**

Promise that is resolved when the 'deviceready' event is caught.

You should bind your code on this promise (`whenReady().then(...)`) instead of using the traditional approach of binding the event on `document.addEventListener("deviceready", ...)`. The event fires when Cordova is fully loaded, i.e. it signals that Cordova's device APIs are loaded and are ready for use.

Example:

```javascript
// get device information
if (cordova) {
  $public.Device.whenReady().then(function() {
    $parameters.DeviceModel = device.model;
    $parameters.CordovaVersion = device.cordova;
    $parameters.Platform = device.platform;
    $parameters.UUID = device.uuid;
    $parameters.Version = device.version;
    $parameters.Manufacturer = device.manufacturer;
    $parameters.IsSimulator = device.isVirtual;
    $parameters.SerialNumber = device.serial;
    $resolve();
  });
} else {
  // fallback when testing on desktop browser
  $resolve();
}
```

Returns: Promise&lt;void&gt;<br/>A `Promise` object that is fulfilled when the deviceready event is caught.

