---
summary: This article explains the system requirements for OutSystems Developer Cloud (ODC) Portal, ODC Studio, and app users, as well as the request limits of ODC.
tags:
locale: en-us
guid: D940C32D-0409-4D49-B6FE-BB831E5EF12C
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# OutSystems system requirements for ODC

This article provides guidance to the versions of tools and software that OutSystems recommends when using OutSystems Developer Cloud (ODC) Portal and ODC Studio.

## ODC Portal

Use the most recent version of any of the following browsers:

* Edge
* Firefox
* Google Chrome
* Safari

## ODC Studio

Before you set up ODC Studio, make sure your computer meets the following requirements.

<div class="info" markdown="1">

Check [here](configure-http-proxy.md) the necessary configurations if you're working on a network where communications to the Internet need to go through an HTTP proxy.

</div>

### Minimum recommended hardware requirements

These are the recommended requirements, but keep in mind that many factors (such as workload) can affect performance.

* 1.8 GHz dual-core processor or better
* 2 GB of RAM (4 GB recommended)
* 1 GB of free disk space

For Apple devices using the Apple Silicon M1 processor, ODC Studio runs best under the Rosetta 2 emulation.

### Operating systems

OutSystems supports the following Operating Systems. This list is subject to change. OutSystems supports Operating Systems for six months after the manufacturer determines an end-of-life date. For example, if your Operating System reaches its end-of-life on May 1, then OutSystems supports your operating system until November 1.

* macOS:
    * macOS Big Sur
    * macOS Monterrey

* Windows:
    * Windows 10 (64-bit)

### Requirements for client-side debugging

To perform client-side debugging in ODC Studio using a desktop browser, use the most recent version of any of the following browsers:

* Google Chrome

## Software requirements for app users

The following sections specify the requirements that users of the apps developed with ODC must meet.

<div class="info" markdown="1">

**End User Requirements**:  OutSystems browser support continues for 6 months after OutSystems announces a date on which support ends. This support is for all end-users running OutSystems on that particular browser.

</div>

### Web apps

It's recommended that you use the most current version.

* Edge
* Firefox
* Google Chrome
* Safari

### Progressive Web Apps

* The default browser for the most current stable version of Android.
* The default browser for the most current stable version of iOS.

### Native mobile apps

See [Mobile Apps Build Service (MABS)](https://success.outsystems.com/support/release_notes/mobile_apps_build_service_versions/) for the latest supported Android and iOS platform versions and the minimum requirements to generate your mobile apps.

## Request limits

There are several known request limits that you should keep in mind when building apps.

### Upload request size

The maximum size of an upload file request is 28.6 MB.

### Server request timeout

The maximum value of the **Server Request Timeout** property is 60 seconds for queries or actions initiated on the client side. The default value of the property is 10 seconds. You can change the default at the app level in the app settings. In ODC Studio, from the **Data** tab, click the top-level element (app name) and the property shown in the top pane.

For queries or actions inside timer logic, the maximum timeout value is 60 minutes.

### Timers timeout

The maximum value of the **Timeout in Minutes** property is 60 minutes.
