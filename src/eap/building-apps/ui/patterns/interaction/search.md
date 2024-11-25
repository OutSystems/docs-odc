---
tags: ui patterns, search functionality, user experience, local variables, widgets
summary: OutSystems Developer Cloud (ODC) features a Search UI Pattern that enables users to find content within applications by entering queries.
locale: en-us
guid: 1914dd20-040d-4a96-8293-e35756cb8e6a
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A17253&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
content-type:
  - reference
  - procedure
---

# Search

You can use the Search UI Pattern to provide users with a search field. Use the Search UI Pattern to allow users find pieces of content by entering queries. Unlike navigation, knowledge of the content's location isn't required and searching is often the primary means of finding content.

![Overview of the Search UI Pattern in a mobile app interface](images/search-5-ss.png "Search UI Pattern Overview")

**How to use the Search UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Search`.

    The Search widget is displayed.

    ![Search widget found in the ODC Studio Toolbox ready to be dragged into the app](images/search-1-ss.png "Search Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Search widget into the Main Content area of your application's screen.

    ![Dragging the Search widget into the Main Content area of the application screen](images/search-2-ss.png "Placing Search Widget in Main Content Area")

    By default, the Search widget contains an Input placeholder and widget.

1. Select the Input widget, and on the **Properties** tab, create a local variable by selecting the **Variable** dropdown and selecting **New Local Variable**.

    ![Creating a new local variable for the Search widget in the Properties tab](images/search-3-ss.png "Creating a Local Variable for Search")

1. Enter a name for the variable.

    In this example, we enter `SearchText`.

    ![Entering a name for the local variable as 'SearchText' in the Search widget properties](images/search-4-ss.png "Naming the Search Text Variable")

    This variable holds the value entered by the user. This variable can be reused throughout your app.

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Properties                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>Blank - No custom styles are added (default value). </li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. |
