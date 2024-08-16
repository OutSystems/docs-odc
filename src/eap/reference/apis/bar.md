---
summary: Explore how to create and customize a Bar Chart using OutSystems Developer Cloud (ODC).
tags:
locale: en-us
guid: ee86596b-1473-4fe8-8da5-1e65352a0997
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---
# Bar Chart

This example shows how you can create a simple Bar Chart with a customized legend. 

1. From the Toolbox, drag the **Bar Chart** widget to the Screen.

    ![Screenshot showing the Bar Chart widget being dragged to the screen in the design interface](images/chartbar-drag-ss.png "Dragging the Bar Chart Widget")

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Screenshot of the Properties tab with the DataPointList property expanded to show options](images/chartbar-expand-ss.png "Expanding the Data Point List Property")

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](data.md#populate-your-chart-with-fixed-data) or [variable data](data.md#populate-your-chart-with-variable-data).

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a point on the bar chart.

    ![Screenshot illustrating how to set the Label and Value properties for a data point in the Bar Chart](images/chartbar-datapoint-ss.png "Setting Data Point Properties")

1. Set the **SeriesName** property.

    ![Screenshot showing the SeriesName property being set in the Bar Chart widget properties](images/chart-seriesname-ss.png "Setting the Series Name")

1. To add more data points, repeat steps 2 and 3.

1. To customize the legend, in the **AddOns** placeholder, click **ChartLegend**, and on the **Properties** tab, set the **Position** property to **Entities.LegendPosition.TopRight** and the **Layout** to **Entities.LegendLayout.Vertical**.

    ![Screenshot displaying the ChartLegend options with Position and Layout properties set to TopRight and Vertical](images/chartbar-addon-ss.png "Configuring the Chart Legend Position and Layout")

1. Set the extra configurations to customize the legend.

    ![Screenshot showing additional customization options for the ChartLegend in the Bar Chart](images/chartbar-customize-ss.png "Customizing the Chart Legend")

After following these steps, you can publish your module:

![Image of the final result displaying a Bar Chart with a customized legend in the published module](images/chartbar-result.png "Final Bar Chart Result")
