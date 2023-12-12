---
summary: To add data to your chart, you can use fixed data or variable data.
tags:
locale: en-us
guid: 773767d0-b1c3-4f06-a98c-b18205802786
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---
# Data

To add data to your chart you must input **DataPoint** labels and values for the **DataPointList** property.

There are two different ways to add data to the **DataPointList** property: **Fixed data** and **Variable data**.

## Populate your chart with fixed data {#populate-your-chart-with-fixed-data} 

1. From the Toolbox, drag a Chart to the Screen. 

    This example uses the Line Chart.

    ![Screenshot showing how to drag a Line Chart to the screen in the design interface](images/chartline-drag-ss.png "Dragging a Line Chart to the Screen")

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.  

    ![Screenshot of the Properties tab with the DataPointList property expanded to add data points](images/chartline-expand-ss.png "Expanding the Data Point List Property")

1. To create a list with one data point, click **+[0]** and set the **Label** and **Value** properties.
    
    These properties define the first data point of the chart. Each data point corresponds to a point on the chart. Optionally, you can also set the **SeriesName**, **Tooltip**, and **Color** for the data points.

    ![Screenshot illustrating the addition of a data point with Label and Value properties in the chart configuration](images/chartline-datapoint-ss.png "Adding a Data Point to the Chart")

1. To add more data points, repeat steps 2 and 3.

After following these steps, you can publish your module.

![Line Chart displayed on the screen with fixed data points after configuration](images/chartline-result-data.png "Line Chart with Fixed Data")

## Populate your chart with variable data {#populate-your-chart-with-variable-data} 

Before you start, make sure you have a List of data points to use in your chart. Each data point must include a label and a numerical value.

1. From the Toolbox, drag a Chart to the Screen.

    This example uses the Column Chart.

    ![Screenshot showing the process of dragging a Column Chart to the screen in the design interface](images/chartcolumn-drag-ss.png "Dragging a Column Chart to the Screen")

1. On the **Properties** tab, set the **DataPointList** property to a List containing the data points for the chart.

    ![Screenshot of setting the DataPointList property to a list of data points in the Properties tab](images/chart-data-datapointlist-ss.png "Setting the Data Point List Property")

1. Map the **Value** and the **Label** of the **DataPointList** to the attributes from the List containing the data points for the chart.

    Optionally, you can also set **DataSeriesName**, **Tooltip**, and **Color** for the data points.

    ![Screenshot demonstrating how to map the Value and Label of the DataPointList to the chart's data attributes](images/chart-data-mapping-ss.png "Mapping Data Points to Chart")

After following these steps, you can publish your module. 

![Column Chart displayed on the screen with variable data points after configuration](images/chart-data-result.png "Column Chart with Variable Data")

## Create a chart with multiple series

To create a Chart with multiple series, follow one of the previous procedures and set the **SeriesName** property for the data points.

![Screenshot showing the process of adding multiple series to a chart by setting the SeriesName property](images/chart-data-addseries-ss.png "Adding Multiple Series to a Chart")
![Screenshot of a chart with multiple data series added in the design interface](images/chart-data-multiple-series-ss.png "Chart with Multiple Data Series")

After following these steps, you can publish your module. 

![Final view of a chart with multiple series displayed on the screen after configuration](images/chart-example-multiple-series.png "Example of a Chart with Multiple Series")
