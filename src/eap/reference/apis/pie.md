---
summary: Learn how to create and customize a Pie Chart with labeled data points using OutSystems Developer Cloud (ODC).
tags: pie charts, data visualization, tutorials for beginners
locale: en-us
guid: fda78656-7247-472a-8d79-c79accc91556
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
topic:
  - add-widget-ui-pattern
---

# Pie Chart

<div class="info" markdown="1">

Applies to the OutSystems UI framework only.

</div>

This example shows how you can create a simple Pie Chart showing the labels of the data points instead of the legend.

1. From the Toolbox, drag the **Pie Chart** widget to the Screen.

    ![Screenshot showing the Pie Chart widget being dragged to the screen in the design interface](images/chartpiedrag-ss.png "Dragging the Pie Chart Widget")

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Screenshot of the Properties tab with the DataPointList property expanded to show options](images/chartpie-expand-ss.png "Expanding the Data Point List Property")

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](data.md#populate-your-chart-with-fixed-data) or [variable data](data.md#populate-your-chart-with-variable-data).

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a slice on the pie chart.

    ![Screenshot illustrating how to set the Label and Value properties for a data point in the Pie Chart](images/chartpie-datapointlist-ss.png "Setting the Data Point Properties")

1. To add more data points, repeat steps 2 and 3.

    ![Screenshot demonstrating the addition of multiple data points to the Pie Chart configuration](images/chartpie-extrapoints-ss.png "Adding More Data Points")

1. To show each of the data point values, in the **AddOns** placeholder, click **SeriesStyling**, and on the **Properties** tab, set the **ShowDataPointValues** property to **True**.

    **Note**: Since the **SeriesName** property was not set, this property is applied to all of the series.

    ![Screenshot showing the SeriesStyling options with ShowDataPointValues property set to True](images/chartpie-datapointvalues-ss.png "Showing Data Point Values")

1. To remove the chart legend, delete the **Chart Legend** Addon.

    ![Screenshot depicting the process of removing the chart legend from the Pie Chart settings](images/chartpie-delete-legend-ss.png "Deleting the Chart Legend")

After following these steps, you can publish your module:

![Image of the final Pie Chart pattern with labels on data points and without a legend](images/chartpie-result.png "Final Pie Chart Pattern Result")
