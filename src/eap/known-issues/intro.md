---
summary: A list of known issues.
tags:
locale: en-us
guid: ebae908a-42f3-475f-be53-28aef8454497
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# Known issues

A list of known issues in ODC.

## Changing the app name breaks the experience in mobile apps { #changing-app-name } 

Avoid changing the app name. Currently, if you change the name of the app, ODC changes the URL that is the identifier of the app. If you change the app name, these are some of the impacts on the mobile apps already running on devices or in distribution:

* No updates over the air are delivered.
* All data and server actions result in failure.
* No application logs (native and runtime logs) show. Logs are stored locally on the device and associated with the application URL and lost due to the issue even after updating the native package to the new version, pointing to the new URL. 
* The outdated app version can still be opened and run and. Depending on the logic flow (use of server actions, for example), the app may have limited usability. In some cases, it might not be obvious to the user that a problem exists or that the app isn't functioning correctly.

## Inconsistent overflow behavior of LongIntegerToInteger

Depending on where you use LongIntegerToInteger and get an overflow, your logic returns the following:

* On server and client side, LongIntegerToInteger on overflow returns 0.
* On the database, LongIntegerToInteger on overflow throws an error.

## You can's preview a mobile app in the Safari browser within the ODC Portal

The preview of a mobile app in the Safari browser within the ODC Portal doesn't work. The app and the preview render within an iframe in different domains, and Safari can't access the content due to security restrictions by Apple.

OutSystems recommends Chrome browser for previewing the mobile app in the ODC Portal.

## Features currently not supported during external database integration

* CreateOrUpdateSome (Bulk Inserts/Updates) entity action is not supported.
* DiffMinutes and DiffSeconds built-in functions for Oracle have a limitation regarding the date interval. The allowed max intervals between dates are:
    * Seconds: 31 years, 9 months, 9 days, 1 hour, 46 minutes, and 39 seconds
    * Minutes: 1901 years, 4 months, 29 days, 10 hours, 39 minutes, and 59 seconds
* Data Preview and runtime queries with Unicode characters are not supported.
* Advanced SQL Nodes do not support external entities.