---
summary: Learn how to refresh REST web services in OutSystems Developer Cloud (ODC) to update consumed API methods efficiently.
tags: api integration, rest api, json, version control, service refresh
locale: en-us
guid: 1ba6b838-04bc-4c08-813d-5a2901954f8c
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3101%3A12107&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - backend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
topic:
  - consume-refresh-methods
---

# Refresh a REST web service

To change the services consumed from a REST API or to modify the list of consumed REST API methods, you can refresh the service in ODC Studio.
An earlier approach to updating a single method, described later in this article, is still valid. However, the refresh option is easier to use and the recommended approach.

To refresh a REST API service:

1. In the **Logic** tab, expand the **Integrations** folder and then expand **REST**.

1. Under **REST**, right-click the REST API and select **Refresh REST API**. In this example, the name of the REST API is **Customers**.

    ![Screenshot showing how to refresh a REST API named 'Customers' in ODC Studio](images/rest-refresh-1-odcs.png "Select REST API")

1. In the Refresh REST API popup, click **Yes**. 

    When you click **Yes**, any changes made to the previous version are lost.  

    ![Confirmation popup for refreshing a REST API in ODC Studio](images/rest-refresh-confirm-2-odcs.png "Refresh REST API")

1. Enter the REST API URL or upload a new file, and click **Refresh Methods**. 

    In this example, the URL points to a JSON file that contains the complete list of REST methods.

    ![Dialog box to enter REST API URL or upload a new file for refreshing methods in ODC Studio](images/rest-refresh-URL-3-odcs.png "Enter REST API URL")

1. Select the methods you would like to consume. 
    
    Note that:
    
    * The methods you select overwrite previously consumed methods for the service. Ensure you select all methods you want to consume, even if they haven't changed.
    * The following settings are **not** overridden when you refresh:
            
        * Basic authentication
        * Advanced settings (Date Format, On Before Request and On After Response)
        * HTTP headers

    The method format displays as **method name/relative endpoint** and, if applicable, **(Deleted)** or **(outdated)**.

    Where:
    
    * method name = the method you may select to consume or update
    *  /relative endpoint = endpoint relative to the base URL
    *  (Deleted) or (outdated) = if applicable, identifies methods that were previously imported but no longer exist in the latest specification

    This example shows all available methods selected. **GetCustomersWithOrders** shows as **Deleted**, which means you can't select it.

    ![List of available REST API methods with options to select for consumption in ODC Studio](images/rest-refresh-methods-4-odcs.png "Choose available methods")

1. Click **Finish** to add the selected methods.
Next, see [Adapt your application to the changes](#adapt-your-application-to-the-changes).

## Manually update a single REST API method

Before the refresh option existed, you could update a method using the following more manual approach. This approach is still valid.

To update a method using this procedure, look at the REST API documentation to understand what needs to change when invoking the REST API method.

To manually update a REST method:

1. In the **Logic** tab, open the **Integrations** folder and expand the REST element containing the method you want to change.

1. Double-click on the REST API Method you want to change.

1. Update the REST API Method information to reflect the change you want to execute, such as adding new parameters to the request structure:

    ![Interface for updating REST API method information in ODC Studio](images/rest-change-1-odcs.png "Update the REST API method information") 

1. Click **Finish**. 

## Adapt your application to the changes

When you change the definition of the REST API method, OutSystems automatically updates the REST API Method and the associated structures according to your changes:

![ODC Studio screen showing the updated REST API method and associated structures](images/rest-change-2-odcs.png "Adapt your application to the changes")

You can now adapt the action flows or screens of your application to reflect the updated functionality.
