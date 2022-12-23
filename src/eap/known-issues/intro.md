---
summary: A list of known issues.
tags:
locale: en-us
guid: ebae908a-42f3-475f-be53-28aef8454497
app_type: mobile apps, reactive web apps
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
