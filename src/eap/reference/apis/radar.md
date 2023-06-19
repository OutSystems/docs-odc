---
summary: 
tags: 
locale: en-us
guid: 0b784bc9-f546-41e5-9c30-832253c5bc6e
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Radar Chart

This example shows how you can create a simple Radar Chart with multiple series types.

1. From the Toolbox, drag the **Radar Chart** widget to the Screen.

    ![Drag the Radar Chart widget to the screen ](images/chartradardrag-ss.png)

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Expand the Data Point List property](images/chartradar-expand-ss.png)

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](data.md#populate-your-chart-with-fixed-data) or [variable data](data.md#populate-your-chart-with-variable-data).

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a point on the radar chart.  

    ![Set the data point](images/chartradar-datapoint-ss.png)

1. Set the **SeriesName** property.

    ![Set the series name](images/chartradar-seriesname-ss.png)

1. To add more data points, repeat steps 2 and 3. 

    ![Add more data points](images/chartradar-extra-datapoints-ss.png)

1. To customize a Series, in the AddOns placeholder, click **SeriesStyling** and on the **Properties** tab, set the **SeriesName** property to the Series you want to customize (in this example, Series 3).

    ![Customize the Series](images/chartradar-customize-series-ss.png)

1. To customize the Series type, on the **Properties** tab, set the **SeriesType** to **Entities.SeriesType.Area**. This sets the Series type to Area.  

    ![Set the Series type](images/chartradar-series-type-ss.png)

After following these steps, you can publish your module:

![Result](images/chartradar-result.png)
