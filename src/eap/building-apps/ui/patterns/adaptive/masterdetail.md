---
summary: OutSystems Developer Cloud (ODC) supports the Master Detail Pattern for displaying lists and their details in applications.
tags: ui patterns, data management
locale: en-us
guid: 2839f103-9cc0-4712-b9df-d3cd6cc805e9
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A9323&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
  - apply
---

# Master Detail

You can use the Master Detail Pattern to display a master list of items and their related details, for example, a list of employees and their corresponding details.

![Overview of the Master Detail Pattern showing a list of items and their details](images/masterdetail-2.png "Master Detail Pattern Overview")

## How to use the Master Detail UI Pattern

1. In ODC Studio, in the Toolbox, search for `Master Detail`.

    The Master Detail widget is displayed.

    ![Screenshot of the Master Detail widget in the ODC Studio Toolbox](images/masterdetail-5-ss.png "Master Detail Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Master Detail widget into the Main Content area of your application's screen.

    ![Dragging the Master Detail widget into the Main Content area of an application screen](images/masterdetail-1-ss.png "Dragging Master Detail Widget")

    By default, the Master Detail widget contains a right placeholder and left placeholder which expects a list.

1. To populate the list, create an aggregate, by right-clicking your screen name, and selecting **Fetch Data from Database**.

    ![Creating an aggregate by fetching data from the database in ODC Studio](images/masterdetail-13-ss.png "Creating an Aggregate")

1. To add a database entity, click on the screen, select the relevant entity, and click **OK**. In this example, we use the **User** entity.

    ![Adding a User entity to the Master Detail Pattern in ODC Studio](images/masterdetail-3-ss.png "Adding a Database Entity")

    A name for the aggregate is added automatically. In this example the aggregate name is **GetUsers**.

1. On the **Interface** tab, double-click your screen name, and in the LeftContent placeholder, select the List widget. On the **Properties** tab, from the **Source** drop-down, select the aggregate you just created. In this example, **GetUsers.List**.

    ![Selecting the GetUsers aggregate from the Source drop-down in the Properties tab](images/masterdetail-4-ss.png "Selecting an Aggregate")

1. On the **Interface** tab, navigate to the attribute you want to display on the left side of the screen, and drag it into the List. In this example, we use the **Name** attribute.

    ![Dragging the Name attribute into the List to display user names on the left side of the screen](images/masterdetail-14-ss.png "Dragging Attribute into List")

    This displays all of the users names on the left side of the screen.

1. So that each of the items in the list can be selected by the user, create a user action by selecting and right-clicking the expression in the List, and selecting **Link to -> New Client Action**.  

    ![Creating a new client action for item selection in the Master Detail Pattern](images/masterdetail-6-ss.png "Creating a Client Action")

1. Double-click the new client action and enter a name. In this example, we call it **ClickSelectedUser**.

    ![Entering a name for the new client action called ClickSelectedUser](images/masterdetail-7-ss.png "Naming the Client Action")

1. From the Toolbox, add the **Assign** logic to the client action, and from the  **Value** drop-down, select the Expression Editor. Navigate to and double-click the current user Id and click **Close**.

    ![Adding the Assign logic to the ClickSelectedUser client action in ODC Studio](images/masterdetail-8-ss.png "Adding Assign Logic to Client Action")

1. To store this user Id, create a local variable by right-clicking on your screen name and selecting **Add Local Variable**. Enter a name for the variable. In this example, we call it **SelectedUserId**.

    ![Creating a local variable called SelectedUserId in ODC Studio](images/masterdetail-9-ss.png "Creating a Local Variable")

1. Select the **Assign** logic, and from the **Variable** drop-down, select the local variable you created (in this example, **SelectedUserId**).

    **Note**: You have now created all of the information that displays on the **left** side of the Master Detail widget. In the following steps, we will create the information to display on the **right** side of the Master Detail widget.

1. To display the selected user's details on the right side of the screen, create a new aggregate by right-clicking on your screen name and selecting **Fetch Data from Database**.

1. Enter a name for the aggregate. In this example, we call it **GetUserDetails**.

    ![Entering a name for the GetUserDetails aggregate to fetch user details from the database](images/masterdetail-11-ss.png "Naming the GetUserDetails Aggregate")

1. To add a database entity, click on the screen, select the relevant entity, and click **Select**. In this example, we use the **User** entity.

1. On the **GetUserDetails** screen, click **Filters**, then click **Add Filter**.

1. From the Filter Condition editor, enter the following condition and click **Close**.

    `User.Id = SelectedUserId`

    This filters all the results in the **User** entity to the currently selected user.

1. Double-click your client action name (in this example, **ClickSelectedUser**), and drag the GetUserDetails aggregate onto the client action. This executes the aggregate using the currently selected user.

    ![Dragging the GetUserDetails aggregate onto the client action to execute it](images/masterdetail-10-ss.png "Dragging GetUserDetails Aggregate")

1. Double-click your screen name, and from the **GetUserDetails** aggregate, drag the attributes you want to display into the RightContent placeholder. In this example, we use the Username and Email attributes.

    ![Dragging Username and Email attributes into the RightContent placeholder to display user details](images/masterdetail-12-ss.png "Dragging Attributes for Display")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property                           | Description                                                                                                            |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| LeftPercentage (Decimal): Optional | Set the LeftContent width using a percentage. Default value is 50%.                                                    |
| OpenedOnPhone (Boolean): Optional  | Variable to hold if the detail is opened on a phone. Default value is False.                                           |
| Height (Text): Optional            | Set the height of the widget (in pixels or %). By default, it is the height of the window, minus the title and header. |

## Compatibility with other patterns

This pattern should be used alone inside the screen content because it will adapt to the height of the parent. Additionally, you should avoid using the Master Detail pattern inside patterns with swipe events, such as Tabs.
