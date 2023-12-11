---
summary: Learn how you can create a simple Line Chart with a Spline line and custom markers.
tags: 
locale: en-us
guid: 7d5b86f8-dcc0-4ea7-a5f8-3f6d1e2c56c5
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# Line Chart

This example shows how you can create a simple Line Chart with a Spline line and custom markers.

1. From the Toolbox, drag the **Line Chart** widget to the Screen.

    ![Screenshot showing the Line Chart widget being dragged to the screen in the design interface](images/chartline-drag-ss.png "Dragging the Line Chart Widget")

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Screenshot of the Properties tab with the DataPointList property expanded to show options](images/chartline-expand-ss.png "Expanding the Data Point List Property")

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](data.md#populate-your-chart-with-fixed-data) or [variable data](data.md#populate-your-chart-with-variable-data).

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a point on the line chart. 

    ![Screenshot demonstrating how to set the Label and Value properties for a data point in the Line Chart](images/chartline-datapoint-ss.png "Setting a Data Point")

1. Set the **SeriesName** property.

    ![Screenshot showing the SeriesName property being set in the Line Chart properties](images/chart-seriesname-ss.png "Setting the Series Name")

1. To add more data points, repeat steps 2 and 3.

    ![Screenshot illustrating the process of adding additional data points to the Line Chart](images/chartline-extradatapoints-ss.png "Adding More Data Points")

1. To enable the Spline Line, set the **Spline** property to **True**.

    ![Screenshot depicting the Spline property set to True to enable the Spline Line in the Line Chart](images/chartline-spline-ss.png "Enabling the Spline Line")

1. To customize a Series, click on the **SeriesStyling** in the **AddOns** placeholder, and on the **Properties** tab, set the **SeriesName** property to the Series you want to customize (in this case, **Series 1**).

    ![Screenshot showing the SeriesStyling option in the AddOns placeholder for customizing a series in the Line Chart](images/chartline-addon-ss.png "Customizing a Series")

1. Expand the **Marker** property and set the extra configurations to customize the marker.

    ![Screenshot displaying the Marker property expanded with extra configurations for customizing the marker in the Line Chart](images/chartline-marker-ss.png "Setting Marker Properties")

After following these steps, you can publish your module:

![Image of the final result showing a completed Line Chart pattern with a Spline line and custom markers](images/chartline-result.png "Final Line Chart Pattern Result")
