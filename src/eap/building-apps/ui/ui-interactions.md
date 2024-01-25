---
summary: A user interface (UI) is where a user interacts and communicates with a device.
tags:
locale: en-us
guid: 743F0F2C-6ADF-4A7A-899E-3802A1249925
app_type: reactive web apps
platform-version: odc
figma:
---
# UI Interactions

A user interface (UI) is where a user interacts and communicates with a device. Devices can include display screens, keyboards, and a mouse. It's also the way users interact with an app.

You can define the action that occurs when users click a button or enter text. For example, when users click a dropdown arrow, the screen displays a list of options from which to make a selection.

Create screens to present information to users. Users access screens through navigation, a type of interaction. When thinking about the UI, consider how to create seamless user journeys. You don't want users to click or scroll for more information constantly.  

You can present different data to your users when navigating to another screen. Buttons and links are common ways to navigate. For example, you can use:

* **Buttons** - for users to move forward a screen or backward a screen, or refresh a screen.
* **Links** - for users to pass an input parameter to another screen. Links enable users to enter information on one screen and then use or display that information on another screen.

## Fetching data for the UI

You design screens to present information to their users by fetching and displaying data. You must define the data source from which to get the data. You define the data source in the properties of the element.

Design your app to fetch a single record or a list of records. You might fetch a single record to display detailed information such as an employee's name and address. You might fetch a list of records to show a table of all employees that work in a specific location. You can use aggregates to fetch data. Aggregates support combining several entities and advanced filtering.

Once you have the data, you are ready to display the data. To display the data, you can use widgets or OutSystems patterns.

## Refreshing data in the UI

If you build your apps with screen templates or accelerators that contain sample data, you probably want to replace the data with your data. In ODC (OutSystems Developer Cloud) Studio you can use logic to refresh data, get data from existing data sources, and provide current data to your users.

In cases where your widget supports automatic data replacement (forms, tables, lists, and gallery widgets), you can drag the new entity that contains your data to the widget. Then verify that data shows correctly and that the app is without errors.

