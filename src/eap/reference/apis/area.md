---
summary: Learn how to create a stacked area chart using OutSystems Developer Cloud (ODC) with this step-by-step guide.
tags:
locale: en-us
guid: 181b8675-7323-4afd-bab7-b315c237d709
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---
# Area Chart

This example shows how you can create a simple Area Chart with a Stacked Series. 

1. From the Toolbox, drag the **Area Chart** widget to the Screen.

    ![Screenshot showing the Area Chart widget being dragged to the screen in the development environment](images/chartarea-drag-ss.png "Dragging the Area Chart Widget")

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Screenshot of the Properties tab with the Data Point List property expanded](images/chartarea-expand-ss.png "Expanding the Data Point List Property")

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](data.md#populate-your-chart-with-fixed-data) or [variable data](data.md#populate-your-chart-with-variable-data). 

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a point on the area chart. 

    ![Screenshot illustrating how to set the Label and Value properties for a data point in the Area Chart](images/chartarea-datapointlist-ss.png "Setting the Data Point Properties")

1. Set the **SeriesName** property.

    ![Screenshot showing the SeriesName property being set in the Area Chart properties](images/chart-seriesname-ss.png "Setting the Series Name")

1. To add more data points, repeat steps 2 and 3.

    ![Screenshot demonstrating how to add additional data points to the Area Chart](images/chartarea-extradatapoints-ss.png "Adding More Data Points")

1. To enable the Stacked Series, set the **StackingType** property to **Entities.StackingType.Stacked**.

    ![Screenshot depicting the StackingType property set to Stacked in the Area Chart settings](images/chartarea-stackingtype-ss.png "Setting the Stacking Type")

After following these steps, you can publish your module:

![Image of the final result showing a completed Area Chart with a Stacked Series](images/chartarea-result.png "Final Area Chart Result")
