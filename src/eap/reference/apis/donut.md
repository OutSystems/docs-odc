---
summary: Learn how you can create a simple Donut Chart.
tags: 
locale: en-us
guid: 18b47e8e-8355-49e2-852d-b7ae8580460e
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Donut Chart

This example shows how you can create a simple Donut Chart.

1. From the Toolbox, drag the **Donut Chart** widget to the Screen.

    ![Drag the Line Chart widget to the screen](images/chartdonut-drag-ss.png)

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Expand the Data Point List property](images/chartdonut-expand-ss.png)

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](data.md#populate-your-chart-with-fixed-data) or [variable data](data.md#populate-your-chart-with-variable-data).

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a slice on the donut chart. 

    ![Set datapoint](images/chartdonut-datapoint-ss.png)

1. To add more data points, repeat steps 2 and 3.
    
    ![Add more datapoint](images/chartdonut-extra-datapoints-ss.png)

1. To customize the inner size of the Donut Chart, set the value of the **InnerSize** property. 

    In this example, the **InnerSize** property is set to 60% (by default, the **InnerSize** property is 50%).

    ![Set inner size of donut](images/chartdonut-innersize-ss.png)

After following these steps, you can publish your module:

![Result](images/chartdonut-result.png)
