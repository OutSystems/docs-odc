---
summary: Explore how to create a Donut Chart using OutSystems Developer Cloud (ODC).
tags: mobile apps, data visualization, chart configuration
locale: en-us
guid: 7dd162ba-bb5a-4c61-902d-d8738c122a54
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
content-type:
  - procedure
---

# Donut Chart

This example shows how you can create a simple Donut Chart.

1. From the Toolbox, drag the **Donut Chart** widget to the Screen. 

    ![Screenshot showing the Donut Chart widget being dragged to the screen in the design interface](images/chartdonut-drag-ss.png "Dragging Donut Chart Widget")

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Screenshot depicting the expansion of the Data Point List property in the Donut Chart properties tab](images/chartdonut-expand-ss.png "Expanding Data Point List Property")

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](data.md#populate-your-chart-with-fixed-data) or [variable data](data.md#populate-your-chart-with-variable-data).

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a slice on the donut chart. 

    ![Screenshot illustrating the process of setting a label and value for a data point in the Donut Chart](images/chartdonut-datapoint-ss.png "Setting a Data Point")

1. To add more data points, repeat steps 2 and 3.
    
    ![Screenshot showing additional data points being added to the Donut Chart](images/chartdonut-extra-datapoints-ss.png "Adding More Data Points")

1. To customize the inner size of the Donut Chart, set the value of the **InnerSize** property. 

    In this example, the **InnerSize** property is set to 60% (by default, the **InnerSize** property is 50%).

    ![Screenshot demonstrating how to set the inner size of the Donut Chart to 60 percent](images/chartdonut-innersize-ss.png "Setting Inner Size of Donut Chart")

After following these steps, you can publish your module:

![Image of the final Donut Chart pattern as it appears after publishing the module](images/chartdonut-result.png "Final Donut Chart Pattern Result")
