---
summary: Calculated attribute in an ODC aggregate lets you add expression-based columns to query results, with steps to group, count, and populate a Dropdown.
tags:
  - Aggregates
locale: en-us
guid: 8d55b7fe-ff2d-4a80-b306-e8d7820ea579
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3101%3A2486&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - Front-end developer
  - Developer
outsystems-tools:
  - odc studio
  - mentor studio
coverage-type:
  - apply
  - evaluate
topic:
  - create-calculated-attribute
isautopublish: true
---

# Create a Calculated Attribute in an Aggregate

There are situations when the data fetched from the database isn't enough and you need to add more information to each record, namely based on the values returned. You can add new attributes to the records that an Aggregate returns, based on the value of the other attributes. You create the attribute by describing it to Mentor Studio and validating the result, or manually in ODC Studio.

## Create a calculated attribute with Mentor Studio

Add a calculated attribute by describing it in terms of the attributes that the aggregate returns in Mentor Studio, and validate its values before you publish.

In your prompt, name the aggregate, the new attribute, and the formula in terms of the attributes that the aggregate already returns. For example, "In the GetProducts aggregate, group by Category.Id and Category.Label and count Product.Id. Add a calculated attribute named DropdownLabel that shows the label followed by the count in parentheses, or Not categorized followed by the count when the label is empty."

For more prompt examples, refer to the logic section of [Prompts for Mentor Studio](../../../agentic-development/mentor-studio/prompts.md#logic).

For the requirements and the steps to prompt Mentor Studio and review the change, refer to [Modify an app with AI in ODC Studio](../../../agentic-development/mentor-studio/modify-app.md) and [Review and accept the plan](../../../agentic-development/mentor-studio/how-it-works.md#accept-plan).

### Validate the calculated attribute

The platform guarantees that the model is valid, and you decide whether the aggregate returns the correct data for your requirement. In ODC Studio, check the following:

* The aggregate has a new attribute with the name that you described.
* The formula refers only to attributes that the aggregate returns, such as the grouped `Label` and the `Count`.
* The formula returns the intended value for every case in your description, including an empty value.
* The aggregate groups and counts the way you described. In the example, the count is the number of products for each category.

## Create a calculated attribute manually in ODC Studio

To add a calculated attribute yourself, do the following in ODC Studio:

1. In the Aggregate, click **New Attribute** to add a new attribute to the Aggregate and name it.
1. Open the attribute menu and select **Edit formula...**
1. Define the expression to calculate the value.

### Example

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

## Related resources

The following resource describes what the platform guarantees and what you check in a Mentor Studio proposal.

* For what the platform guarantees and what you validate, refer to [Platform guarantees and AI interpretation](../../../agentic-development/odc-ai-and-platform.md).
