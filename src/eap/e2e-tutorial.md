
# **End-to-end tutorial for public EAP**

In this tutorial you will create three apps: a Web app called **Calendar** that will uses **TaskList** to provide service actions of creating tasks and changing their status, along with a library called **Timeline**.

Both TaskList and Timeline will contain reusable components available to every app during development. 


## Create TaskList

**TaskList** provides service actions which, among other things, can be used to expose a service to be reused by other applications inside the same OutSystems environment.

To create **TaskList**: 



1. Launch **Service Studio**, click **New Application**, and select **Web App** and click **Next**.  

![Create Web App](images/create-service.png "Create Web App") 
 
2. In the next screen call the app **TaskList** and give it a short description. You may choose a color to customize the app’s interface and upload a customized icon. Then click **Create App**.  

![Fill in basic app information](images/fill-in-app-basic-information.png "Fill in basic app information")



### Create data model

Entities are elements that allow you to persist information in the database and to implement your database model. Think of them as database tables or views.  An Entity is defined through Entity Attributes that store the information related to it. Examples of entity attributes are Name, Address, Zip Code, City, among others.

Now we’re going to create an entity called **Task** with three attributes: **Description**, **DueDate**, and **IsCompleted**.



1. Go to the **Data** tab, right-click **Entities**, click **Add Entity**, and name it **Task**. 

![Add entity to database](images/add-entity.png "Add entity to database") 



2. Right-click the new **Task** entity, select **Add Entity Attribute**, and name it **Description**. 

![Add entity attribute](images/add-entity-attribute.png "Add entity attribute") 



3. Verify that OutSystems has correctly identified  **Data Type** of the new **Description** entity as** Text**. Change the entity **Length** to **100** and **Is Mandatory** to **Yes**. 

![Set entity attribute parameters](images/set-entity-attribute-parameters.png "Set entity attribute parameters") 



4. In the same way add an** Entity Attribute** called **DueDate** to the **Task** entity. Verify that Service Studio has identified its **Data Type** as **Date**. As above, set **Is Mandatory** to **Yes**.
5. Add a third **Entity Attribute** called **IsComplete** to the **Task** entity. Verify that **Service Studio** has identified its **Data Type** as **Boolean** and that **Is Mandatory** is set to **No**. 

![Set IsComplete entity attribute parameters](images/set-entity-attribute-parameter-boolean.png "Set IsComplete entity attribute parameters") 

### Create list and detail screens from **Task** entity

With the **Task** entity created, it is now time to give users a way to view and change items in the task list. 



1. Select the **Interface** tab, double-click **MainFlow**, and verify that **MainFlow** appears in the top right corner of the central working canvas. 

![MainFlow canvas](images/main-flow-canvas.png "MainFlow canvas") 

2. Return to the **Data** tab and drag the **Task** entity onto the **MainFlow** canvas.  

![Drag the task entity to the canvas](images/drag-task-entity-to-canvas.png "Drag the task entity to the canvas") 

3. OutSystems creates two interface screens, as seen below. 

![Two screen in MainFlow](images/two-screens-in-main-flow.png "Two screen in MainFlow") 

You may double-click either of the created screens to see how the entity has been expressed. The **Tasks** screen is shown below. 
    
![Tasks list screen](images/task-list-screen.png "Tasks list screen") 




### Change roles of screens to anonymous for testing

<div class="info" markdown="1">

EAP reportedly will not have roles. They still appear in the interface, so they are documented here.

<</div>



1. Go to the **Interface** tab and select **Tasks** in the **MainFlow**. Click **Anonymous** in the **Roles** area so it it is easier to test the app during development.

![Set Task entity to anonymous](images/set-task-entity-to-anonymous.png "Set Task entity to anonymous") 

2. In the same manner, select **TaskDetail** in the **MainFlow** and click **Anonymous** in the **Roles** area. 

    <div class="info" markdown="1">


    During the publish process you will receive the following security warning: You're exposing a Server Action for public access and without authentication. Consider removing the Anonymous Role from this Screen.


    For most business apps, access to interface screens is restricted to registered users. Before deployment to the quality or production environments, the role of these screens should be changed back to the default so they are not anonymous.


    </div>

3. Click the green **1-Click-Publish** button in the top center of the workspace so you can test your app to see if it works as expected.

When the app is published click the blue **Open in browser** button. There you can add a task, set it to completed, and verify that it appears as expected in the task list.


### Expose **Task** entity for use in other applications

In order for other apps to use the functionality of **TaskList**, it must be exposed for consumption.



1. From the **Data** tab select the **Task** entity and change the **Public** property to **Yes** so it can be consumed, or added as a dependency, to other apps.

![Make Data entity public](images/make-data-entity-public.png "Make Data entity public") 

2. In the **Logic** tab right-click **Service Actions** and click **Add Service Action** to create the **AddTask **service action.

![Add a service action](images/add-service-action.png "Add a service action") 

3. Right-click the **AddTask **service action, select  **Add Input Parameter** and call it **DueDate**. Verify that OutSystems identifies its **Data Type** as **Date** and set **IsMandatory** to **Yes**.

![Add an input parameter to the service action](images/add-service-action-input-parameter.png "Add an inpute parameter to the service action") 

4. In the same way, add a second input parameter to the **AddTask **service action and call it **Description**. Verify that OutSystems identifies its **Data Type** as **Text** and set **IsMandatory** to **Yes**.

![Add a second input parameter to the service action](images/add-second-service-action-input-parameter.png "Add a second input parameter to the service action") 

5. Go to the **Data** tab and drag the **CreateTask** entity attribute to the flashing blue node in the **AddTask** logic flow.

![Add CreateTask to flow](images/add-create-task-to-flow.png "Add CreateTask to flow") 

6. Select the **CreateTask** entity action that you just dragged into the flow and expand the **Source** options in the property editor to view the required sources, **Description** and **DueDate**.

![Expand the CreateTask Sources](images/expand-createtask-source.png "Expand the CreateTask Sources") 

7. Click the **Description** dropdown and accept the option suggested by OutSystems.

![Set description source](images/add-create-task-source.png "Set description source") 

8. In a like manner accept the option suggested by OutSystems in the **DueDate** dropdown.

![Set DueDate source](images/add-second-create-task-source.png "Set DueDate source") 


Click the **1-Click Publish** button to make **TaskList** available for other apps.


## Create a library app

Intro: what is a library.



1. Close the TaskList app and create a new **Library** called **TimeLine**.

![Create library](images/create-library.png "Create library") 

2. Add OutSystems UI as a dependency to the **Timeline** library.  First search for “OutSystems” in other apps.

![Search for dependencies in other apps](images/search-for-dependencies-in-other-apps.png "Search for dependencies in other apps") 

<div class="info" markdown="1">

All procedures and screens from this point forward are taken from O11 and must be changed. 

</div>
3. Select OutSystemUI and click **Add Dependency**.

![Add dependency](images/add-dependency.png "Add dependency") 

4. In a like manner at the other three OutSystems UI themes:
    * OSUIMobileBase
    * OSUIMobiliePhone
    * OSUIMobileTablet
5. In the **Interface** tab right-click **UIFlow**, select **Add UI Flow** and give it the name **UIFlow1**. \
![Add UI flow](images/add-ui-flow.png "Add UI flow") 

6. Click the **Theme** dropdown and select **OutsystemsUI**.

![Select theme for flow](images/select-theme-for-flow.png "Select theme for flow") 

7. Create a reusable UI that has a table widget. Right-click **UIFlow1**, select **Add Block**, and name it **Timeline**.

![Add block for flow](images/add-block-to-uiflow.png "Add block for flow") 

8. Set the **Timeline** block **Public** property to **Yes** and then drag a **Table** widget to the canvas.  

![Add table to timeline block](images/add-table-to-timeline-block.png "Add table to timeline block") 



### Create a source for the table

After you drag the table to the canvas, OutSystems warns you that it requires a source. Normally the source is an entity. However, entities are not available in library apps, and libraries must be stateless.

In this case the source is provided by input parameters and structures to receive data.



1. In the **Data** tab, right-click **Structures**, call it **TimelineEntry**, and set the **Public** attribute to **Yes**. 

![Add structure](images/add-structure.png "Add structure") 

2. Right-click the **TimelineEntry** structure, select **Add Structure Attribute**, call it **Description**, and set the **Is Mandatory** attribute to **Yes**. Verify that OutSystems identified its **Data Type** as **Text**.

![Add structure attribute](images/add-structure-attribute.png "Add structure attribute") 

3. In a similar manner, right-click the **TimelineEntry** structure, select **Add Structure Attribute**, and call it **Date**, and set the **Is Mandatory** attribute to **Yes**. Verify that OutSystems identified its **Data Type** as **Date**.

![Add date structure attribute](images/add-date-structure-attribute.png "Add date structure attribute") 

4. In the **Interface** tab right-click **Add Input Parameter** and call it **Source**.

![Add input parameter to timeline](images/add-input-paramter-to-timeline.png "Add input parameter to timeline") 

5. Select the **Source** input parameter, scroll down the **Data Type** options, and select **List…

**![Change data type to source](images/change-data-type-to-list.png "Change data type to source") 

6. In the **Element Type Window**, scroll down to the **Structures** folder, select the **TimelineEntry** structure you previously created, and click **Select**.

![List element type](images/list-element-type-window.png "List element type") 

7. Drag the **Source** input parameter of the **Timeline** block to add two columns to the table and set the source of the the table to these input parameters.

![Drag block source to table](images/drag-block-source to table.png "Drag block source to table") 

8. Select the table in the canvas, click the **Event** dropdown, and select **onchange**.

![Select onchange table event](images/select-onchange-table-event.png "Select onchange table event")  


<div class="info" markdown="1">

A **New on Sort** is only available for aggregates that cannot be used in a library.

</div>



9. Right-click the **Timeline** block, select **Add Client Action**,  and call it **ListSort**.

![Add event handler](images/add-event-handler.png "Add event handler") 

10. Select the table in the canvas, click the **Handler** dropdown, and select **ListSort**.

![Make listsort the handler](images/make-listsort-the-handler.png "Make listsort the handler")  

11. Drag the **Run Client Action** widget from the toolbox to the flashing blue node in the logic flow on the canvas.

![Drag client action](images/drag-client-action.png "Drag client action") 

12. Scroll down to the **ListSort** action in the **Select Action** window and click **Select**.

![Select action window](images/select-action-window.png "Select action window") 

13. With the **ListSort** action selected, click the **List** attribute dropdown and accept the OutSystems suggestion of **Source**.

![List sort attribute](images/list-sort-attribute.png "List sort attribute") 

14. In a like manner, select **Date** as the **By** attribute.

![Set by attribute](images/set-by-attribute.png "Set by attribute") 


At this point click the **1-Click Publish** button to make this library available to other apps in your environment.


## Create a calendar app

The calendar app will use the library and service previously created. It will include:



* An onboarding screen
* Use the Timeline block of the library
* Show data from the DataList service

To create the calendar app:



1. Return to the Applications
2. Create Web app and name it **Calendar**.


### Create onboarding screen

With the **Calendar** app created, begin with adding an onboarding screen.



1. Drag the **Screen** widget from the toolbox to the canvas. 

![Drag screen for Calendar app](images/drag-screen-for-calendar-app.png "Drag screen for Calendar app") 

2. In the **New Screen** window, choose the **Onboardings** category, select the **Onboarding** **with animation** template, and click **Create Screen**.

![Onboarding screen](images/create-onboarding-screen.png "Onboarding screen") 

3. Click the **Get Started** button and change the default **On Click** event to **New Screen**.

![Set onclick action](images/set-on-click-for-onboarding.png "Set onclick action") 

4. In the **New Screen** window, select the **Empty** template, call it **HomePage**, and click **Create Screen**.

![Create Homepage](images/create-homepage.png "Create Homepage") 



### Add Dependencies

The **Calendar** app uses UI elements from the library app and data from the service app. In order to use them they have to be added as dependencies, as follows:



1. Type **Timeline** in the search bar (in the upper right of the **Service Studio** workspace) and click **Search in other Modules**.

![Search for timeline block dependency](images/search-for-timeline-block.png "Search for timeline block dependency") 

2. In the **Search in other Modules** window filter the search results by **Block** and select the **Timeline** app you created earlier. Then click **Add Dependency**.

![Add timeline block dependency](images/add-timeline-block-dependency.png "Add timeline block dependency") 

3. The UI element brought in from the **Timeline** library now needs a source for its data, which the app can consume from the **Task** entity you created in the **TasksList** app you created earlier. So as before, search for **Task** in the search bar, select **Search in other Modules,** sort by **Entity**, select the **Task** entity from the **TasksList** app, and click **Add Dependency**.

![Add tasks entity dependency](images/add-tasks-entity-dependency.png "Add tasks entity dependency") 

4. Now add the functionality to add a task. Search for **AddTask**, as above, and then click **Add Dependency**.

![Add addtask dependency](images/add-addtask-dependency.png "Add addtask dependency") 



### Use dependencies in Calendar



1. In the **Data** tab, drag the Data aggregate to the canvas. Then click **1-Click Publish**. 

![Drag task entity to main screen](images/drag-task-entity-to-mainscreen.png "Drag task entity to main screen") 

2. Drag the **Timeline** block to the **MainContent** area in the **Homepage** canvas. 

![Drag timeline block to main screen](images/drag-timeline-block-to-main-area.png "Drag timeline block to main screen") 


The resulting table, as can be seen, requires a source for data. 
    
![Missing data source](images/missing-source-for-data.png "Missing data source") 


3. In the **Interface** tab right click **Homepage** and select **Fetch Data from Database** and call it **GetTasks**. 

![Fetch data from database](images/fetch-data-from-database.png "Fetch data from database") 

4. With **Homepage** selected, click the table on the canvas and select **Expression Editor** from the **Source** dropdown. 

![Select expression editor for source](images/select-expression-editor-for-source.png "Select expression editor for source") 

5. In the **Expression Editor** window double-click **List** under the **GetTasks** folder to add the expression GetTasks.List. Then click **Close**. 

![Expression editor](images/expression-editor.png "Expression editor") 

6. Drag a **Button** widget to the **Click to add actions** area of the canvas change the button **Text** to **Add Tasks**. 

![Drag button](images/add-button.png "Drag button") 

7. Double-click the new **Add Tasks** button to see the **AddTaskonClick** action flow in the canvas. From the **Logic** tab drag the **AddTask** server action to the flashing blue node.

![Add task button](images/add-addtask-action.png "Add task button") 

8. Click the **DueDate** parameter dropdown and accept CurrDate(). In the **Description** parameter type an appropriate name such as **Calendar App**.

![Add task parameters](images/addtask-parameters.png "Add task parameters") 


Now click the **1-Click Publish** button to test the app.


## Next steps

Customize UI styles

