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

    ![Drag the Line Chart widget to the screen ](images/chartline-drag-ss.png)

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Expand the Data Point List property](images/chartline-expand-ss.png)

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](data.md#populate-your-chart-with-fixed-data) or [variable data](data.md#populate-your-chart-with-variable-data).

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a point on the line chart. 

    ![Set datapoint](images/chartline-datapoint-ss.png)

1. Set the **SeriesName** property.

    ![Set the series name](images/chart-seriesname-ss.png)

1. To add more data points, repeat steps 2 and 3.

    ![Add more data points](images/chartline-extradatapoints-ss.png)

1. To enable the Spline Line, set the **Spline** property to **True**.

    ![Set the Spline property](images/chartline-spline-ss.png)

1. To customize a Series, click on the **SeriesStyling** in the **AddOns** placeholder, and on the **Properties** tab, set the **SeriesName** property to the Series you want to customize (in this case, **Series 1**).

    ![Select the series to customize](images/chartline-addon-ss.png)

1. Expand the **Marker** property and set the extra configurations to customize the marker.

    ![Set marker properties](images/chartline-marker-ss.png)

After following these steps, you can publish your module:

![Example Line Chart](images/chartline-result.png)
