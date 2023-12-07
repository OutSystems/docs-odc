---
summary: How to create a new attribute to a data query and base its value on the other record's attributes.
tags: 
locale: en-us
guid: 8d55b7fe-ff2d-4a80-b306-e8d7820ea579
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3101%3A2486&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Create a Calculated Attribute in an Aggregate

There are situations when the data fetched from the database isn't enough and you need to add more information to each record, namely based on the values returned. OutSystems allows you to do it. You can add new attributes to the records returned by the Aggregate based on the value of the other attributes:

1. In the Aggregate, click **New Attribute** to add a new attribute to the Aggregate and name it.
1. Open the attribute menu and select **Edit formula...**
1. Define the expression to calculate the value.

## Example

StoreApp, a Web App to check the products in a store, has a screen to list products.

In this screen, you want to address the following requirement: the end-user can filter the listed products by category, by selecting an available category from a Dropdown. In each entry of the Dropdown, the app displays the number of products that have that specific category along with the category name.

![Screenshot of the process to create a calculated attribute in an Aggregate for listing products by category in OutSystems](images/listed-products-by-category-odcs.png "Creating a Calculated Attribute in an Aggregate")

To calculate this data and add it to each entry of the Dropdown, do the following:

1. As this is a Web App, right-click the screen and select the option **Fetch Data from Database** to add an Aggregate to the screen.

1. Add the `Product` entity to the Aggregate.

1. In the Aggregate, do the following:

    1. Click **Add source** and add the `Category` entity to the Aggregate, choosing products `Only With` category for the join rule.

    1. Group by `Category.Id`.

    1. Count by `Product.Id` to have the number of products per category.

    1. Group by `Category.Label` to get the label of each category.

    1. Open the last grouped column menu and add a new attribute. Name it `DropdownLabel`.

    1. Assign the following expression to the created column:

        `If ( Label <> "", Label + " (" + Count + ")" , "Not categorized" + " (" + Count + ")" )`

        `Label` and `Count` variables are two of the previously grouped columns.

    ![Step-by-step visual guide on how to assign an expression to a new calculated attribute in an OutSystems Aggregate](images/calculate-data-odcs.png "Assigning Expression to Calculated Attribute")

1. Go to the screen and add a Dropdown. Set the Dropdown values to be the returning list of the Aggregate using the `DropdownLabel` attribute as the options text.
