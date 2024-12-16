---
summary: Learn how to create and customize Screens in OutSystems Developer Cloud (ODC) for both web and mobile applications.
locale: en-us
tags: ui development, app design
guid: 7c01a3db-3807-4e86-bbbb-e88ba5c28346
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3101%3A10561&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
---

# Create screen from scratch

A Screen is a user interface (UI) element that contains other UI elements for users to interact. An empty Screen contains a basic layout for you to add widgets. A Screen based on a Screen Template has predefined content that works as a demo.

How Screens show in an app to you users depends on the app type:

* In a Web App, Screens render as web pages in a browser.
* In Mobile Apps, Screens render as screens of a mobile app.

## Creating a Screen

To create a Screen, follow these steps in ODC Studio:

1. Go to the **Interface** tab, and then expand the **UI Flows** folder.

    ![Screenshot of the Interface tab with UI Flows expanded in ODC Studio](images/interface-tab-ui-flows-odcs.png "Interface Tab and UI Flows in ODC Studio")

1. From the **UI Flows**, right-click **MainFlow** and in the menu select **Add Screen**.

    ![Context menu in ODC Studio showing the option to Add Screen](images/add-screen-odcs.png "Adding a New Screen")

1. Select one of the following:
    
    * **Empty**, to create an empty Screen
    * A Screen Template, to create a Screen based on a template

    ![Dialog in ODC Studio to create a new Screen with options for Empty or Template](images/create-blank-screen-odcs.png "Create Blank Screen Option")

1. Optionally, enter a name in the **Screen name** field.

1. Click **Create Screen**.
