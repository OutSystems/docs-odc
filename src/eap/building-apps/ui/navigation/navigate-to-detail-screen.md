---
summary: Allow end-users to check the details of a record by navigating to a different screen
tags:
locale: en-us
guid: 32d89cec-ecb5-4c30-9d43-548cc4077425
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3101%3A10809&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---
# Navigate to a Detail Screen

You can allow end-users to check the details of a given record by navigating to a different screen while providing the item identifier as an input parameter.

## In Web and Mobile

To navigate to a detail screen in Web and Mobile:

1. On the screen that displays the list, select the List Item widget. 
1. In the properties of the List Item widget, select the target detail screen as handler for the On Click event and define the identifier of the current list item as an input argument to the target screen. 

![Screenshot showing the properties of the List Item widget with the target detail screen selected as the handler for the On Click event](images/navigate-mobile-odcs.png "Properties of the List Item Widget")
