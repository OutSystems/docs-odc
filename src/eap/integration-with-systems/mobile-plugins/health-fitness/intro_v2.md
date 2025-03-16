---
summary: Explore the integration of health and fitness data using HealthKit and Google Fit APIs in mobile apps with OutSystems Developer Cloud (ODC).
tags: healthkit integration, google fit integration, mobile health data, plugin development, permissions handling
locale: en-us
guid: 131bec56-8c60-457c-a9ba-63801f2c54bc
app_type: mobile apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=5364%3A193&mode=design&t=Xf7kazC2UjQKDaiy-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - forge
  - odc studio
coverage-type:
  - understand
  - apply
  - remember
topic:
  - using-cordova-plugins
---

# Health and Fitness Plugin using HealthKit and Google Fit 

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

The Health & Fitness plugin enables you to access and use health and fitness data in a mobile app. The plugin provides access to the Apple HealthKit and Google Fit APIs by letting you use data relevant to your health and fitness use cases.

The plugin is unaware of the provider you use for data, but you always need to request permissions from users to access data. The plugin saves no health and fitness data in the device. In cases where your app writes data to the APIs, the package name is the identifier of the data source. 

As a good practice, verify the plugin is available in the app and prevent the app from crashing. Use the **Logic** > **Client Actions** > **HealthFitnessPlugin** > **CheckHealthFitnessPlugin** action to check for the plugin availability. If the plugin isn't available to the app, display an error to your users.

<div class="info" markdown="1">

To learn how to install and reference a plugin in your **OutSystems** apps see [Installing plugins](../intro.md).

</div>

## Sample app

**OutSystems** provides a sample app that contains logic for common use cases. Install the Health & Fitness sample app from Forge and then open it in ODC Studio.

This sample app shows you how to do the following with the health and fitness data:

* Request permission to access
* Do simple queries that return the last logged value
* Do advanced queries for a specific period that return a list of values
* Retrieve raw data related to workouts for a specific period (iOS only).
* Use the data in user interface, such as cards, tables, and graphs

![Screenshot of the Health & Fitness sample app interface](images/sample-app.png "Health & Fitness Sample App") 

## Enabling your users to track their health and fitness data

The following steps show how to design a use case that includes health and fitness data.

1. Create logic to request permission to access health and fitness data.
1. Create a user interface.
1. Create logic to access and store health and fitness data.
1. Create logic to access and use workout data (iOS only).
1. Optionally, create logic to write and store new health and fitness data.
1. Create logic to define a background job.

<div class="info" markdown="1">

Refer to the sample app for examples.

</div>

### Requesting access to health and fitness data

Before your app can access data, request permission from the users to access their health and fitness data. From ODC Studio, select the **Logic** > **Client Actions** > **HealthFitnessPlugin** and use the **RequestPermission** action.

You can define the variables and the following permissions access types:

* Read
* Write
* Read and write

In the screen logic, request the permissions from the app users, in an action that's triggered by **On Initialize** event.

The plugin comes with groups of permissions. Use the groups of permissions as accelerators to check for access when you request data.

The plugin has groups of default variables in **Data** > **Entities** > **HealthFitnessPlugin** that define the permission type for:

* HealthVariables
* FitnessVariables
* ProfileVariables
* SummaryVariables
* WorkoutVariables

![Screenshot showing how to request permissions by group in the Health & Fitness plugin](images/get-permissions-by-group-odcs.png "Requesting Permissions by Group")

<div class="info" markdown="1">

Refer to the sample app for more examples.

</div>

### Creating a user interface

Start, for example, by defining a variable that corresponds to the type of output you want to show. Create a variable that holds the data so that you can access, store, and display the number of steps taken in a day (1).

![Screenshot of a sample user interface displaying health data like daily step count](images/sample-interface-odcs.png "Sample User Interface for Health Data") 

To show the step count for the day, you can use an **Expression** and customize the look and feel of the parent widget (2).

### Create logic to access and use health and fitness data

The plugin reads and writes the data through the **AdvancedQuery** client action. In the **AdvancedQuery** action, set the values for the predefined variables.

The health or fitness query parameters might include:  

* period: start, end
* time unit: second, minute, hour, day, week, month, year
* operation type: sum, min, max, average 
  
![Screenshot demonstrating how to access health and fitness data using the AdvancedQuery action](images/get-fitness-data-odcs.png "Accessing Health and Fitness Data") 

<div class="info" markdown="1">

Verify that access and storage of health or fitness data on the device works. Check the value of **AdvancedQuery**. If **Success** is True, handle the data in **AdvancedQuery.** by assigning it to a variable of the same data type. Refer to the sample app for an example.

</div>

#### Notes about AdvancedQuery on iOS

* When querying the **Sleep** variable, the results correspond to the "IN BED INTERVALS" that are registered in the Health app from the system. Using different time units or operations won't alter the results returned.

### Create logic to access and use workouts data (iOS only)

To enrich the data obtained from the **AdvancedQuery**, you can retrieve data related to workouts using the **GetWorkoutsData** client action. To do this, set the values for the following input parameters:

* Period: start and end
* Workout type and variable map: list of a structure that relates a Workout Type and a list of Variables to a query

For the Workout Type and Variable map structure, the plugin already provides the following default values:

* If there's no list or the list is empty, the plugin considers all workout types available and applies two variables to each: **Heart Rate** and **Active Energy Burned**.
* If the list contains an item that has a workout type set but has no variable list associated (or an empty one) with it, the plugin considers two variables: **Heart Rate** and **Active Energy Burned**.

![Screenshot showing the process of retrieving workout data with the GetWorkoutsData action](images/get-workouts-odcs.png "Retrieving Workout Data")

<div class="info" markdown="1">

Verify that access and storage of health or fitness workout data on the device works. Check the value of **GetWorkoutsData**. If **Success** is True, handle the data in **GetWorkoutsData.** by assigning it to a variable of the same data type.

</div>

### Create logic to write health and fitness data

To write health and fitness data you can use the **WriteData** action. Set the parameters for the type of health or fitness variable you want and the new value you want to store.

To check that writing the health or fitness data on the device is working, verify the value of **WriteData.Success** is **True**.

### Create logic to define a background job

To define a background job you can use the **SetBackgroundJob** action. Set the parameters for the type of health or fitness variable you want to keep evaluating, define the notification trigger condition and its frequency, and define the notification content. 

<div class="info" markdown="1">

From Android 15 onwards, users can install an app in the [Private space](https://developer.android.com/about/versions/15/features#private-space). Users can lock their private space at any time. Once locked, all background jobs of the app inside the private space are stopped, and notifications are not shown until the user unlocks the private space.

It is not possible to detect if an app is installed in the private space. Therefore, if your app shows any critical notifications, inform your users to avoid installing the app in the private space.

For more information about the behavior changes of your app related to the private space, refer to [Android documentation](https://developer.android.com/about/versions/15/behavior-changes-all#private-space-changes).

</div>

Parametrization for two different use cases of a background job is shown below:

#### Setting up a daily steps goal

In the case of a daily steps goal evaluator, you will probably want to issue a single notification per day if the daily steps goal is met. To achieve this you can use the following parametrization:

![Screenshot illustrating the setup of a background job for monitoring daily steps goal](images/set-background-job-odcs.png "Setting Up a Daily Steps Goal Background Job")

#### Setting up a heart rate monitoring alarm

In the case of a heart rate monitoring alarm, try to strike a balance between job frequency and notification frequency. For example, you may want to check your heart rate every ten seconds. However, you would probably find it intrusive to receive notifications every time your heart rate goes above, or drops below, a certain value.

Consider the following parametrization for a background job that will notify you if your heart rate is above 190 bpm, with a maximum notification frequency of one notification per minute:

![Screenshot showing the parametrization for a heart rate monitoring background job](images/set-background-job2-odcs.png "Setting Up a Heart Rate Monitoring Alarm")


After you have created your background job you can update it or delete it using the **UpdateBackgroundJob** action or the **DeleteBackgroundJob** action, respectively.

To verify that the background job was successfully created, check if the value of **SetBackgroundJob.Success** is **True**.

### Create logic to disconnect your Android app from Google Fit

To disconnect your Android app from Google Fit, and consequently revoke all permissions, recording subscriptions, and sensor registrations, you can use the **DisableGoogleFit** action. To check that your app is no longer connected to Google Fit, verify that the value of **DisableGoogleFit.Success** is **True**.

After calling this action, you can also verify that the app no longer has access to any data by calling **AdvancedQuery**, **GetFitnessData**, **GetHealthData**, or **GetProfileData**.

<div class="info" markdown="1">

Your app should be implemented so that when a user chooses to disconnect it from Google Fit, it does not try to fetch any data or request any permissions until the user changes their decision.

</div>

### Handling errors

The app with the plugin can run on many Android or iOS devices, with different hardware and configurations. To ensure a good user experience and prevent the app from crashing, handle the errors within the app.

Following is a list of actions you can use to make sure there are no errors:

| Variable        | Action                   | Description                                                    |
| --------------- | ------------------------ | -------------------------------------------------------------- |
| **IsAvailable** | CheckHealthFitnessPlugin | True if the plugin is available in the app.                    |
| **Success**     | AdvancedQuery            | True if there aren't errors while accessing and storing data.  |
| **Success**     | GetWorkoutsData          | True if there aren't errors while accessing and storing data.  |
| **Success**     | GetFitnessData (*)       | True if there aren't errors while accessing and storing data.  |
| **Success**     | WriteData                | True if there aren't errors while writing data.                |
| **Success**     | SetBackgroundJob         | True if there aren't errors while creating a background job.   |
| **Success**     | DisconnectFromGoogleFit  | True if there aren't errors while disconnecting from Google Fit.|

(*) There are several actions in the Health & Fitness plugin that begin with **Get** and have a **Success** variable.
