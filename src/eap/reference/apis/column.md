---
summary: Learn how you can create a simple Column Chart with data labels.
tags: 
locale: en-us
guid: 8651448f-4ebe-47c6-8d2e-676f33a830b0
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# Column Chart

This example shows how to create a simple Column Chart with data labels.

1. From the Toolbox, drag the **Column Chart** widget to the Screen.

    ![Drag the Column Chart widget to the screen ](images/chartcolumn-drag-ss.png)

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Expand the Data Point List property](images/chartcolumn-expand-ss.png)

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](data.md#populate-your-chart-with-fixed-data) or [variable data](data.md#populate-your-chart-with-variable-data).

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a point on the column chart. 

    ![Set datapoint](images/chartcolumn-datapointlist-ss.png)

1. Set the **SeriesName** property.

    ![Set the series name](images/chart-seriesname-ss.png)

1. To add more data points, repeat steps 2 and 3.

    ![Add more data points](images/chartcolumn-extradatapoints-ss.png)

1. To show the values of each data point, click on the **SeriesStyling** in the **AddOns** placeholder, and on the **Properties** tab, set the **ShowDataPointValues** property to **True**.

    Since the **SeriesName** property was not set, this property will be applied to all series.

    ![Show data point values](images/chartcolumn-showdatapoint-ss.png)

After following these steps, you can publish your module:

![Example Area Chart](images/chartcolumn-result.png)
