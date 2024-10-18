---
summary: OutSystems Developer Cloud (ODC) system requirements guide for optimal use of ODC Portal and ODC Studio.
tags:
locale: en-us
guid: D940C32D-0409-4D49-B6FE-BB831E5EF12C
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/design/zohMj3VpAEA6P9J9azwqQq/Getting-started-with-ODC?node-id=3406%3A10&t=SDUOaeXeeu7S6LQG-1
platform-version: odc
---

# OutSystems system requirements for ODC

This article provides recommendations for compatible tools and software versions that you can use with OutSystems Developer Cloud (ODC) Portal and ODC Studio.

To access ODC portal and connect to ODC Studio, ensure your local network allows access to `*.outsystems.dev` domains. For end-users to access ODC apps, their network must allow access to the `*.outsystems.app` domain or the [custom domain](../manage-platform-app-lifecycle/custom-domains.md) defined for each stage.

## ODC Portal

Use the most recent version of any of the following browsers:

* Edge
* Firefox
* Google Chrome
* Safari

## ODC Studio

Before you set up ODC Studio, make sure your computer meets the following requirements.

<div class="info" markdown="1">

If you are working on a network where communications to the Internet are routed via an HTTP proxy, then refer to [How to configure HTTP proxy in ODC studio](configure-http-proxy.md) for configuration instructions.

</div>

### Minimum recommended hardware requirements

The following are the minimum recommended hardware requirements,however, keep in mind that many factors such as workload can affect performance.

* 1.8 GHz dual-core processor or better
* 2 GB of RAM (4 GB recommended)
* 1 GB of free disk space

### Operating systems

OutSystems supports the following Operating Systems. This list is subject to change. OutSystems supports Operating Systems for six months after the manufacturer's end-of-life date. For example, if your Operating System reaches its end-of-life on May 1, then OutSystems supports your operating system until November 1.

* macOS:
    * macOS Monterrey
    * macOS Ventura since ODC Studio 1.4.10
    * macOS Sonoma since ODC Studio 1.4.10 

* Windows:
    * Windows 11 (64-bit) since ODC Studio 1.3.15
    * Windows 10 (64-bit)

### Requirements for client-side debugging

To perform client-side debugging in ODC Studio using a desktop browser, use the most recent version of any of the following browsers:

* Google Chrome
* Microsoft Edge (only available for Windows)

## Software requirements for app users

The following sections specify the software requirements for Apps developed in ODC. 

<div class="info" markdown="1">

**End User Requirements**:  Support for OutSystems browser continues for 6 months after end of support date announcement. This support applies to all end-users running OutSystems on that particular browser.

</div>

### Web apps

Use the most current version of the following browsers:

* Edge
* Firefox
* Google Chrome
* Safari

### Progressive web apps

* The default browser for the most current stable version of Android.
* The default browser for the most current stable version of iOS.

### Native mobile apps

For more information about the latest supported Android and iOS platform versions and the minimum requirements to generate mobile apps, refer to [Mobile Apps Build Service (MABS)](https://success.outsystems.com/support/release_notes/mobile_apps_build_service_versions/)

### Client-side traces

ODC supports the following client-side trace request limits: 

* Up to 400 trace requests every minute and 3500 requests daily per stage.

## Platform limits

The following table shows the limits of the ODC to keep in mind when you are building apps. Unless otherwise noted, each limit is stage-specific. These limits cannot be exceeded and may cause errors or a drop in performance if reached.

| **Name**                                 | **Limit** | **Description** |
| ---------------------------------------- | --------: | ----------------------------------------------------------------------------------------------------------------------- |
| App log retention (days)                 |        28 | The maximum number of days that logs are retained (plus 21 days of additional backup retrievable via support ticket). |
| Concurrent events                        |       100 | The maximum number of events that can run concurrently. |
| Concurrent timers                        |         6 | The maximum number of timers that can run concurrently. |
| Custom code execution duration (seconds) |        95 | The maximum time a single custom code function can execute. |
| Custom code memory (MB)                  |     1,024 | The maximum memory available for custom code functions while executing. |
| Custom code storage (MB)                 |       512 | The maximum amount of ephemeral storage available for custom code functions while executing. |
| DB backup retention (days)               |        30 | The maximum number of days database backups are retained. |
| Event duration (minutes)                 |         2 | The maximum duration of a handler of an event in minutes. |
| Events per queue                         |    10,000 | The maximum number of events that can be queued. Upon reaching the limit, an exception is thrown. |
| Expose REST API method timeout (seconds) |        60 | The maximum amount of time an Expose REST API method executes before timing out. |
| Log rate/minute (thousands)              |         2 | The maximum rate at which logs can be captured, in thousands per minute. |
| Max requests (per IP)                    |     5,000 | The maximum number of HTTP requests that can be made from a given IP address within a 5-minute window across all stages. |
| Service action timeout (seconds)         |       100 | The time a service action waits for a response before timing out. |
| Timer execution timeout (minutes)        |        60 | The maximum time a timer can execute. |
| Trace retention (days)                   |        28 | The maximum number of days that traces are retained (plus 21 days of additional backup retrievable via support ticket). |
| Trace size (MB)                          |        15 | The maximum size of traces. Traces exceeding this are dropped. |
| Trace spans rate/minute (thousands)      |        50 | The maximum rate at which trace spans can be captured, in thousands per minute. |
| Client side trace requests every minute per stage  |        400 | The maximum number of client-side trace requests every minute. |
| Client side trace requests daily per stage  |           3500 | The maximum number of client-side trace requests daily. |
| Upload request size (MB)                 |      28.6 | The maximum file size allowed when uploading. |
| Workflow activity max duration (seconds) |       120 | The maximum duration of a workflow activity. |
| Workflow concurrent versions             |         5 | The maximum number of workflow versions that can run concurrently. |

### Server request timeout

The maximum value of the **Server Request Timeout** property is 60 seconds for queries or actions initiated on the client side. The default value of the property is 10 seconds. You can change the default value in the app's property editor.

![Screenshot of app's property editor](images/edit-app-properties-odcs.png "Edit App Properties")

For queries or actions inside timer logic, the maximum timeout value is 60 minutes.
