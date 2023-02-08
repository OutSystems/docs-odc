---
summary: This article explains the system requirements for OutSystems Developer Cloud (ODC) Portal, ODC Studio, and app users, as well as the request limits of ODC.
tags:
locale: en-us
guid: D940C32D-0409-4D49-B6FE-BB831E5EF12C
app_type: web apps, reactive apps, mobile apps
platform-version: odc
---

# OutSystems system requirements for ODC

The following provides guidance as to the versions of tools and software that OutSystems recommends when using OutSystems Developer Cloud (ODC) Portal and ODC Studio.

## ODC Portal

Use the most recent version of any of the following browsers:

* Edge
* Firefox
* Google Chrome
* Safari

## ODC Studio

Before you set up ODC Studio, make sure your computer meets the following requirements.

### Minimum recommended hardware requirements

These are the recommended requirements, but keep in mind that many factors (such as workload) can affect performance. 

* 1.8 GHz dual-core processor or better
* 2 GB of RAM (4 GB recommended)
* 1 GB of free disk space

For Apple devices using the Apple Silicon M1 processor, ODC Studio runs best under the Rosetta 2 emulation.

### Operating systems

<div class="info" markdown="1">

OutSystems only supports versions up to 6 months after the end of life defined by the manufacturer. 

</div>

* macOS
* Windows (64-bit)

### Requirements for client-side debugging

To perform client-side debugging in ODC Studio using a desktop browser, use the most recent version of any of the following browsers:

* Edge
* Firefox
* Google Chrome
* Safari

## Software requirements for app users

The following sections specify the requirements that users of the apps developed with ODC need to meet.

<div class="info" markdown="1">

**End User Requirements**:  OutSystems browser support continues for six months after the OutSystems announces a date on which support ends. This support is for all end users running OutSystems on that particular browser.

</div>

### Web apps

It's recommended that you use the most current version. 

* Edge
* Firefox
* Google Chrome
* Safari

### Progressive Web Apps

* The default browser for the most current stable version of Android 
* The default browser for the most current stable version of iOS 

### Native mobile apps

See **Mobile Apps Build Service (MABS)** for the latest supported Android and iOS platform versions and the minimum requirements to generate your Mobile Apps.

## Request limits

There are several known request limits that you should keep in mind when building apps.

### Upload request size

The maximum size of an upload file request is 28.6 MB.

### Server request timeout

The maximum value of the **Server Request Timeout** property is 60 seconds for queries or actions initiated on the client side. The default value of the property is 10 seconds. You can change the default at the app level in the app settings. In ODC Studio, from the **Data** tab, click the top-level element (app name) and the property is listed in the top pane.

For queries or actions inside timer logic, the maximum timeout value is 60 minutes.

### Timers timeout

The maximum value of the **Timeout in Minutes** property is 60 minutes.
