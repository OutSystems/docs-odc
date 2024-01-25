---
tags: 
summary: The Pagination UI Pattern helps users find a specific item on long listings.
locale: en-us
guid: d5aa86c4-874b-4d6d-91c6-c4a18c096f0a
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3208%3A17402&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Pagination

You can use the Pagination UI pattern to help users find a specific item on long listings. This pattern is typically used on listings, such as e-commerce category pages, search engines, and article archives.

![Screenshot of Pagination UI pattern overview in a mobile app](images/pagination-5-ss.png "Pagination UI Overview")

**How to use the Pagination UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Pagination`.
  
    The Pagination widget is displayed.

    ![Screenshot showing the Pagination widget in the ODC Studio Toolbox](images/pagination-1-ss.png "Pagination Widget in Toolbox")

1. From the Toolbox, drag the Pagination widget into the Main Content area of your application's screen.

    In this example, we drag the Pagination widget below a table of Application data.

    ![Screenshot of dragging the Pagination widget into the Main Content area in ODC Studio](images/pagination-3-ss.png "Dragging Pagination Widget")

    By default, the Pagination widget contains Previous and Next placeholders with icons.

1. Add 2 local variables - one to store the starting index value and the other to store the maximum number of records per page. In this example, we add the **StartIndex**  and **MaxRecords** variables. Both are of type integer and we set the default value of the **MaxRecords** to 50. This means there are 50 records shown per page.

    ![Screenshot of adding StartIndex and MaxRecords local variables for Pagination](images/pagination-9-ss.png "Adding Local Variables for Pagination")

1. Select the Pagination widget, and on the **Properties** tab, set the **StartIndex** and **MaxRecords** properties to the respective local variables we just created.

    ![Screenshot of setting StartIndex and MaxRecords properties in the Pagination widget](images/pagination-10-ss.png "Setting Pagination Widget Properties")

1. Staying on the **Properties** tab, set the **TotalCount** to the number of records fetched in the aggregate that is the source of the table.  in this example, we set it to **GetApplications.Count**.

    ![Screenshot showing the TotalCount property configuration for Pagination](images/pagination-11-ss.png "Configuring TotalCount Property")

1. To define what happens when the end-user changes from one page to another, from the **Handler** dropdown, select **New Client Action**. By default the **New Client Action** contains a **NewStartIndex** input.

1. To set the start index of the pagination, drag the **StartIndex** onto the client action and set its value to **NewStartIndex**. When a user changes page, the start index will change accordingly.

    ![Screenshot of defining the client action for page change in Pagination](images/pagination-12-ss.png "Defining Page Change Handler")

1. Refresh the data by re-executing the aggregate so the data for the new page appears in the table.

    ![Screenshot illustrating the refresh action when changing pages in Pagination](images/pagination-13-ss.png "Refreshing Data on Page Change")

    In this example, when the user changes page, and the refresh action runs, it will take into account the current **StartIndex** and the **MaxRecords** to determine the **NewStartIndex** (in this case 50 for the new page.)

1. So that we only fetch the data we need for each page, select the aggregate and set the **Start Index** and **Max. Records** properties to the the variables we created earlier, **StartIndex** and **MaxRecords**.

    ![Screenshot of setting Start Index and Max. Records properties in the aggregate for Pagination](images/pagination-14-ss.png "Setting Aggregate Properties for Pagination Widget")



After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| StartIndex (Integer): Mandatory  | Sets the initial index to start pagination.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| MaxRecords (Integer): Mandatory  | Number of records to display per page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| TotalCount (Integer): Mandatory  | Total number of records in the list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ShowGoToPage (Boolean): Optional | If True, there's an input box that allows the user to enter and jump to a specific page. If False, there is no functionality to jump to a specific page. This is the default.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ExtendedClass (Text): Optional   | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
