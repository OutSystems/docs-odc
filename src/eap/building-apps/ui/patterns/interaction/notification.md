---
tags: user notifications, ui design
summary: Learn how to implement and configure the Notification UI Pattern in OutSystems Developer Cloud (ODC) to enhance user communication.
locale: en-us
guid: b60bb989-895e-49a1-a261-76d9bb540425
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3203%3A16275&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - apply
  - remember
topic:
  - add-widget-ui-pattern
---

# Notification

<div class="info" markdown="1">

Applies to the OutSystems UI framework only.

</div>

The Notification UI Pattern is a contextual short message that provides important information to the user, such as app crashes, new updates, task reminders, and new messages.

**How to use the Notification UI Pattern**

1. In ODC Studio, in the Toolbox, search for `Notification`.

    The Notification widget is displayed.

    ![Screenshot of the Notification widget in ODC Studio's Toolbox](images/notification-widget-ss.png "Notification Widget in ODC Studio")

1. From the Toolbox, drag the Notification widget into the Main Content area of your application's screen and on the **Properties** tab, enter a **Name**.

    ![Dragging the Notification widget into the Main Content area of the application screen](images/notification-dragwidget-ss.png "Dragging Notification Widget to Screen")

1. Add the relevant content to the Content placeholder.

    In this example, an icon and some text are added.

    ![Example of adding an icon and text to the Notification widget's content placeholder](images/notification-content-ss.png "Notification Content Example")

1. From the Toolbox, drag 2 **Button** widgets into the Main Content area of your application's screen to **Open** and **Close** the Notification.

    ![Two Button widgets added to the Main Content area for opening and closing the Notification](images/notification-buttons-ss.png "Notification Open and Close Buttons")

1. Define the actions for the buttons and set the **WidgetId** to the Notification widget.

    In this example, for the **Open** button, the **On Click** event is set to a **New Client Action** that runs the **NotificationOpen** client action. For the **Close** button, the **On Click** event is set to a **New Client Action** that runs the **NotificationClose** client action.

    ![Setting the On Click event to a New Client Action for the Open button of the Notification](images/notification-open-ss.png "Defining Action for Open Button")

    ![Setting the On Click event to a New Client Action for the Close button of the Notification](images/notification-close-ss.png "Defining Action for Close Button")

1. You can configure the Notification by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties. For more configurations, expand the **OptionalConfigs** property.

    ![Configuring optional properties of the Notification pattern in the Properties tab](images/notification-properties-ss.png "Notification Properties Configuration")

After following these steps and publishing the app, you can test the pattern in your app.

![Example of a Notification UI Pattern as it appears in a published app](images/notification-example.png "Notification UI Pattern Example")

## Properties

| Property | Description |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| StartsOpen(Boolean): Optional | If True, the notification is immediately visible on screen. If False, the notification is not visible on screen. The default value is False. <br/> Use one of the following actions to change the value after the :<ul><li>NotificationOpen</li><li>NotificationClose</li></ul> |
| Width(Text): Optional | Set the Notification width. Accepts any kind of unit (for example, px, %, vw). |
| Position(Position Identifier): Optional | Set where the notification appears on the screen. The predefined options are as follows:<ul><li>Bottom</li><li>BottomLeft</li><li>BottomRight</li><li>Center</li><li>Left</li><li>Right</li><li>Top</li><li>TopLeft</li><li>TopRight</li></ul><br/>Examples<ul><li>``Entities.Position.Right`` - The notification is displayed on the right side of the screen.</li><li>``Entities.Position.Bottom`` - The notification is displayed on the bottom of the screen.</li></ul> |
| OptionalConfigs.InteractToClose(Boolean): Optional | If True, the notification closes when it's clicked. If False, the notification can't be clicked. the default value is True. |
| OptionalConfigs.CloseAfterTime(Integer): Optional | Set the delay time, in ms, to close the notification. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your custom style classes in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. |
