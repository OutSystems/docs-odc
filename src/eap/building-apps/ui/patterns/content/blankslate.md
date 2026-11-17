---
tags:
  - Accessibility
  - Front-End
  - Mobile app
  - OutSystems UI
  - UI Patterns
  - UX
  - Widgets
summary: Explore how to implement the Blank Slate UI Pattern in OutSystems Developer Cloud (ODC) to enhance user interfaces when no data is available.
locale: en-us
guid: 8f31ca3f-5223-4225-b292-304330d0e17e
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A10392&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
coverage-type:
  - apply
  - remember
topic:
  - add-widget-ui-pattern
isautopublish: true
---

# Blank Slate

<div class="info" markdown="1">

Applies to the OutSystems UI framework only.

</div>

You can use the Blank State UI Pattern to inform end-users, for example, to complete a task or when there is no data available for display etc.

![Example of a Blank Slate UI Pattern in a mobile app interface](images/blankslate-5-ss.png "Blank Slate UI Pattern Example")

## How to use the blank slate UI pattern

1. In ODC Studio, in the Toolbox, search for `Blank Slate`.

    The Blank Slate widget is displayed.

    ![Blank Slate widget displayed in the ODC Studio Toolbox](images/blankslate-2-ss.png "Blank Slate Widget in ODC Studio Toolbox")

1. From the Toolbox, drag the Blank Slate widget into the Main Content area of your application's screen.

    ![Dragging the Blank Slate widget into the main content area of an application screen](images/blankslate-3-ss.png "Dragging Blank Slate Widget into Main Content Area")

    By default, the Blank Slate widget contains icon, content, and action placeholders.

1. Add your content to the placeholders.

    In this example, we change the icon to a calendar icon, enter some text in the Content placeholder, and add a button to the Actions placeholder. This button, when clicked, redirects the user to another page.

    ![Customized Blank Slate widget with a calendar icon, text content, and an action button](images/blankslate-4-ss.png "Customizing Blank Slate Widget with Content")

After following these steps and publishing the app, you can test the pattern in your app.

## Properties

| Property | Description |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FullHeight (Boolean): Optional | Displays a larger Blank Slate, taking over full page height. If True, the Blank Slate takes over the full page height. This is the default value. If False, the Blank Slate doesn't take over the full height of the page. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS.<p>Examples</p><ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. |

## Accessibility – WCAG 2.2 AA compliance {#accessibility}

Starting with OutSystems UI version **2.29.0**, the **Blank Slate** is compliant with WCAG 2.2 AA accessibility standards by default. No changes or manual work are required. If you customized the pattern, validate your implementation to ensure it still meets accessibility requirements.

<div class="info" markdown="1">

**For versions earlier than 2.29.0**: If you use an OutSystems UI version earlier than **2.29.0** and manually applied accessibility fixes as described below, remove the manual code added by following the steps in this section before updating to version **2.29.0**.

</div>

### Manual fix required (for versions before 2.29.0)

By default, the Blank Slate UI pattern requires a small update to fully comply with WCAG 2.2 AA standards. Add the correct role so that screen readers interpret it properly.

Doing so ensures the pattern is accessible for all users, including people with visual or motor disabilities.

#### Fix Blank Slate role

1. In **ODC Studio**, go to the **Interface** tab.

1. Select the **Screen/Block** where the Blank Slate is used.

1. In the **Screen/Block** properties, select the **OnReady** event.

    A client action is created.

    ![Creating the OnReady action in ODC Studio](images/blankslate-roleready-ss.png "Create the OnReady action")

1. In the **OnReady** client action, drag a **JavaScript** node to the flow.

    ![Adding a JavaScript node to the OnReady action in ODC Studio](images/blankslate-addnodejs-ss.png "Add a JavaScript node to the OnReady action")

1. In the **JavaScript** node, add an input parameter named **WidgetId** (type **Text**).

1. Set **WidgetId** to the Blank Slate block/widget ID (for example, `BlankSlate.Id`).

    ![Setting the WidgetId parameter to the Blank Slate block ID in ODC Studio](images/blankslate-setwidgetid-ss.png "Set WidgetId for the Blank Slate block ID")

1. Choose one of the following roles, depending on your use case:

    **a) Blank Slate represents a static section**

    If the Blank Slate is used to represent an empty list of results (for example, an inbox or item list with no entries), set the role to **region**.

    ```javascript
    // Set role on the first Blank Slate element
    const blankSlate = document.getElementById($parameters.WidgetId);
    if (blankSlate) {
        blankSlate.children[0].setAttribute("role", "region");
    }
    ```

    ![Adding the script to the JavaScript node in ODC Studio](images/blankslate-addrolescript-ss.png "Add the script to the JavaScript node")

    **b) Blank Slate updates dynamically**

    If the Blank Slate updates dynamically (for example, search results: **No results found** or a shopping cart: **Your cart is empty**), set the role to **status**.

    ```javascript
    // Set role on the text content Blank Slate element
    const blankSlate = document.getElementById($parameters.WidgetId);
    if (blankSlate) {
        const dynamicContent = blankSlate.querySelector('.blank-slate-description');
        if(!dynamicContent) return;
        dynamicContent.setAttribute("role", "status");
    }
    ```

    <div class="info" markdown="1">

    When using this option, place the Blank Slate inside a **Block**, and enclose the block in an **If**. Alternatively, add the script to the **action that triggers the Blank Slate** to appear. If the script runs in **OnReady** and the block isn't present, the role won't be added to the HTML.

    </div>

1. Publish the app.

#### Result

The Blank Slate now has the correct role applied.

Test it in your app to confirm the update.
