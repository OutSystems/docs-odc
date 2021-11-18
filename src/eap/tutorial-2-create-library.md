---
summary: Learn how to create a Library to expose elements to other projects. 
tags: 
---
# Task 2: Create a Library

In Neo, apps can have strong dependencies to Libraries only. <!--Libraries are versioned and projects reuse elements from a specific Library version. -->For more information about reusing elements in Neo, see [Reuse elements across apps](reuse-elements.md).

This task walks you through creating a Library and exposing an element for reuse.

## Before you begin

Make sure you completed [Task 1: Create a Web App](tutorial-1-create-web-app.md) before continuing.

## Create a Library and a Block

Follow these steps

1. Close the TaskList app and create a new **Library** called `TimeLine`.

    ![Create Library](images/create-library-ss.png "Create library") 

1. Add OutSystems UI as a dependency to the **Timeline** Library. First search for `OutSystems` in other apps.

    ![Search for dependencies in other apps](images/search-for-dependencies-in-other-apps-ss.png "Search for dependencies in other apps") 

    <div class="info" markdown="1">

    All procedures and screens from this point forward are taken from O11 and must be changed. 

    </div>
    
1. Select **OutSystemsUI** and click **Add Dependency**.

    ![Add dependency](images/add-dependency-ss.png "Add dependency") 

1. In a like manner at the other three OutSystems UI themes:
    * **OSUIMobileBase**
    * **OSUIMobiliePhone**
    * **OSUIMobileTablet**

1. In the **Interface** tab right-click **UIFlow**, select **Add UI Flow** and give it the name **UIFlow1**. 

    ![Add UI flow](images/add-ui-flow-ss.png "Add UI flow") 

1. Click the **Theme** dropdown and select **OutsystemsUI**.

    ![Select theme for flow](images/select-theme-for-flow-ss.png "Select theme for flow") 

1. Create a reusable UI that has a table widget. Right-click **UIFlow1**, select **Add Block**, and name it `Timeline`.

    ![Add block for flow](images/add-block-to-uiflow-ss.png "Add block for flow") 

1. Set the **Timeline** block **Public** property to **Yes** and then drag a **Table** widget to the canvas.  

    ![Add table to timeline block](images/add-table-to-timeline-block-ss.png "Add table to timeline block") 

## Create a source for the table

After you drag the table to the canvas, OutSystems warns you that it requires a source. Normally the source is an entity. However, entities are not available in libraries, and libraries must be stateless.

In this case the source is provided by input parameters and structures to receive data.

1. In the **Data** tab, right-click **Structures**, call it `TimelineEntry`, and set the **Public** attribute to **Yes**. 

    ![Add structure](images/add-structure-ss.png "Add structure") 

1. Right-click the **TimelineEntry** structure, select **Add Structure Attribute**, call it `Description`, and set the **Is Mandatory** attribute to **Yes**. Verify that OutSystems identified its **Data Type** as **Text**.

    ![Add structure attribute](images/add-structure-attribute-ss.png "Add structure attribute") 

1. In a similar manner, right-click the **TimelineEntry** structure, select **Add Structure Attribute**, and call it `Date`, and set the **Is Mandatory** attribute to **Yes**. Verify that OutSystems identified its **Data Type** as **Date**.

    ![Add date structure attribute](images/add-date-structure-attribute-ss.png "Add date structure attribute") 

1. In the **Interface** tab right-click **Add Input Parameter** and call it `Source`.

    ![Add input parameter to timeline](images/add-input-paramter-to-timeline-ss.png "Add input parameter to timeline") 

1. Select the **Source** input parameter, scroll down the **Data Type** options, and select **List…**.

    ![Change data type to source](images/change-data-type-to-list-ss.png "Change data type to source") 

1. In the **Element Type Window**, scroll down to the **Structures** folder, select the **TimelineEntry** structure you previously created, and click **Select**.

    ![List element type](images/list-element-type-window-ss.png "List element type") 

1. Drag the **Source** input parameter of the **Timeline** block to add two columns to the table and set the source of the table to these input parameters.

    ![Drag block source to table](images/drag-block-source-to-table-ss.png "Drag block source to table") 

1. Select the table in the canvas, click the **Event** dropdown, and select **onchange**.

    ![Select onchange table event](images/select-onchange-table-event-ss.png "Select onchange table event")  


    <div class="info" markdown="1">

    A **New on Sort** is only available for aggregates that cannot be used in a Library.

    </div>


1. Right-click the **Timeline** block, select **Add Client Action**,  and call it `ListSort`.

    ![Add event handler](images/add-event-handler-ss.png "Add event handler") 

1. Select the table in the canvas, click the **Handler** dropdown, and select **ListSort**.

    ![Make listsort the handler](images/make-listsort-the-handler-ss.png "Make listsort the handler")  

1. Drag the **Run Client Action** widget from the toolbox to the flashing blue node in the logic flow on the canvas.

    ![Drag client action](images/drag-client-action-ss.png "Drag client action") 

1. Scroll down to the **ListSort** action in the **Select Action** window and click **Select**.

    ![Select action window](images/select-action-window-ss.png "Select action window") 

1. With the **ListSort** action selected, click the **List** attribute dropdown and accept the OutSystems suggestion of **Source**.

    ![List sort attribute](images/list-sort-attribute-ss.png "List sort attribute") 

1. In a like manner, select **Date** as the **By** attribute.

    ![Set by attribute](images/set-by-attribute-ss.png "Set by attribute") 

At this point click the **1-Click Publish** button to make this Library available to other projects in your environment.

## Next step

After follow the steps above, go to [Task 3: Create a consumer Web App](tutorial-3-create-calendar.md) and follow the steps to complete the tutorial.
