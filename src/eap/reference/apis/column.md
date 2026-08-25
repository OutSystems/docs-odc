---
summary: 'Column Chart widget in OutSystems Developer Cloud (ODC): add data points, configure SeriesName, and show data labels.'
tags:
  - Front-End
  - OutSystems UI
  - UI
  - UI Patterns
  - Widgets
locale: en-us
guid: 8651448f-4ebe-47c6-8d2e-676f33a830b0
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=10550-12
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
coverage-type:
  - apply
topic:
  - add-widget-ui-pattern
isautopublish: true
---

# Column chart

<div class="info" markdown="1">

Applies to the OutSystems UI framework only.

</div>

This example shows how to create a simple Column Chart with data labels.

1. From the Toolbox, drag the **Column Chart** widget to the Screen.

    ![Screenshot showing the Column Chart widget being dragged to the screen in the design interface](images/chartcolumn-drag-ss.png "Dragging the Column Chart Widget")

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Screenshot depicting the expansion of the Data Point List property in the Column Chart widget properties tab](images/chartcolumn-expand-ss.png "Expanding the Data Point List Property")

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](data.md#populate-your-chart-with-fixed-data) or [variable data](data.md#populate-your-chart-with-variable-data).

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a point on the column chart.

    ![Screenshot illustrating how to set the Label and Value properties for a data point in the Column Chart widget](images/chartcolumn-datapointlist-ss.png "Setting the Data Point Properties")

1. Set the **SeriesName** property.

    ![Screenshot showing the SeriesName property being set in the Column Chart widget properties](images/chart-seriesname-ss.png "Setting the Series Name")

1. To add more data points, repeat steps 2 and 3.

    ![Screenshot demonstrating how to add additional data points to the Column Chart widget](images/chartcolumn-extradatapoints-ss.png "Adding More Data Points")

1. To show the values of each data point, click on the **SeriesStyling** in the **AddOns** placeholder, and on the **Properties** tab, set the **ShowDataPointValues** property to **True**.

    Since the **SeriesName** property was not set, this property will be applied to all series.

    ![Screenshot showing the ShowDataPointValues property set to True to display values on the Column Chart](images/chartcolumn-showdatapoint-ss.png "Enabling Data Point Value Display")

After following these steps, you can publish your module:

![Screenshot of the published Column Chart with data labels](images/chartcolumn-result.png "Column Chart with Data Labels")
