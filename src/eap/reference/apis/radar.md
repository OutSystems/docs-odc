---
summary: Learn how to create and customize a Radar Chart in OutSystems Developer Cloud (ODC) using multiple series types and data points.
tags: data visualization, ui design
locale: en-us
guid: 0b784bc9-f546-41e5-9c30-832253c5bc6e
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
---

# Radar Chart

This example shows how you can create a simple Radar Chart with multiple series types.

1. From the Toolbox, drag the **Radar Chart** widget to the Screen.

    ![Screenshot showing the Radar Chart widget being dragged to the screen in the design interface](images/chartradardrag-ss.png "Dragging the Radar Chart Widget")

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Screenshot depicting the expansion of the Data Point List property in the properties tab](images/chartradar-expand-ss.png "Expanding the Data Point List Property")

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](data.md#populate-your-chart-with-fixed-data) or [variable data](data.md#populate-your-chart-with-variable-data).

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a point on the radar chart.  

    ![Screenshot illustrating how to set the label and value for a data point in the Radar Chart](images/chartradar-datapoint-ss.png "Setting a Data Point")

1. Set the **SeriesName** property.

    ![Screenshot showing the Series Name property being set in the Radar Chart configuration](images/chartradar-seriesname-ss.png "Setting the Series Name")

1. To add more data points, repeat steps 2 and 3.

    ![Screenshot demonstrating how to add additional data points to the Radar Chart](images/chartradar-extra-datapoints-ss.png "Adding More Data Points")

1. To customize a Series, in the AddOns placeholder, click **SeriesStyling** and on the **Properties** tab, set the **SeriesName** property to the Series you want to customize (in this example, Series 3).

    ![Screenshot of the SeriesStyling option being selected to customize a series in the Radar Chart](images/chartradar-customize-series-ss.png "Customizing the Series")

1. To customize the Series type, on the **Properties** tab, set the **SeriesType** to **Entities.SeriesType.Area**. This sets the Series type to Area.  

    ![Screenshot showing the Series Type property set to Area in the Radar Chart properties tab](images/chartradar-series-type-ss.png "Setting the Series Type")

After following these steps, you can publish your module:

![Image displaying the final result of the Radar Chart pattern after customization and configuration](images/chartradar-result.png "Final Radar Chart Pattern Result")
