---
guid: 8517ea53-04e1-4f9d-b707-524259744ff9
locale: en-us
summary: In this article you will learn how to create events, trigger events, and handle events
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=3213-21341
coverage-type:
  - apply
  - unblock
topic:
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - backend developers
  - mobile developers
tags: event handling, asynchronous communication, odc, backend development, mobile development
outsystems-tools:
  - odc studio
helpids:
---
# Implement events in ODC

Events allow apps to communicate changes and updates asynchronously. You can create events in an app to notify other apps when specific actions occur. These events can then be triggered within the app's logic and handled either in the same app or in other apps that consume the event. This article explains the following:

* [Create an event](#create-an-event)

* [Trigger an event](#trigger-an-event)

* [Handle an event](#handle-an-event)

* [Error processing in events](#handling-errors-in-events)

## Create an event

You can create events in your ODC apps to capture and communicate important changes. Events enables asynchronous communication between apps. For example, in an eCommerce app, you can create an **OnPurchaseStarted** event that is triggered whenever a customer initiates a purchase. You can pass details such as the product ID in your event and communicate asynchronously to other apps, such as an Inventory app to update stock levels or a Fraud Detection app to monitor suspicious transactions.

To create an event in an app, follow these steps:

1. Go to **ODC Studio**.

1. On the **Events** tab, right-click **Events**, and select **Add Event**.

1. Set the relevant properties for the new event:

   1. If you want other apps to [handle or process](./backend-events.md#publishersubscriber-model) the event, you must set the **Public** property to **Yes**.

   2. If you want to handle the event in the same app, select the **Handler** for the event. The handler can either be a new server action or an existing server action. For detailed information about processing events in a different consumer app, refer to [Handle an event](#handle-an-event).

1. To pass information to the event using the event payload, right-click the newly created event and select **Add Input Parameter**. For detailed information about event payload, refer to [Properties of ODC events](events-properties.md).

Once the event is created, you can trigger the event in the logic flow of your app.

## Trigger an event

After creating an event, you must trigger it within the same app to ensure that other consumer apps can handle it. You can trigger the event using either a server action or a service action. For example, in an eCommerce app, you can trigger the event **OnPurchaseStarted** within a server action that executes when a user clicks the **Purchase** button, allowing other apps, such as the Inventory app or Fraud Detection app, to handle the event asynchronously.

This procedure assumes that you are triggering the event in the server action.

To trigger an event in the producer app, follow these steps:

1. Go to **ODC Studio**.

1. On the **Logic** tab, right-click **Server Actions**, and select **Add server action**.

1. Drag the **Trigger Event** element to the server action flow. The Select Event popup displays.

![ODC Studio interface showing how to trigger an event in the server action flow.](images/trigger-backend-event-odcs.png "Trigger Event in ODC Studio")

1. Select the event to be triggered.

1. Publish the app.

Once the producer app is successfully published, the event is now available to be consumed and handled by other consumer apps.

## Handle an event

You can handle an event either within the same app where it was created or in other consumer apps using a server action. For example, in an eCommerce app, when the **OnPurchaseStarted** event is triggered, consumer apps such as the Inventory app can handle it by updating stock levels, and the Fraud Detection app can analyze the transaction for any suspicious activity.

To handle an event in the consumer app, follow these steps.

1. Go to ODC Studio.

1. On the **Events** tab, right-click **Events**, and select **Add public element**. The public element popup displays.

![ODC Studio interface showing the option to add a public element for handling events.](images/public-event-odcs.png "Add Public Element in ODC Studio")

1. Select the producer app and choose the event you want to add.

   1. The selected event and its input parameters are now added to the consumer app. 

1. From the event properties panel, click **Handler** and select the server action that handles the event. The sever action implements the logic to handle the event.

To handle an event in the producer app, you can select the server action to handle the event at the time the event was created.

## Error processing in events

When you trigger events, exceptions are raised in the producer app in the following scenarios:

* The event payload exceeds the maximum size of 10KB.

* The event queue is full, with more than 10000 events.

* The event cannot be delivered as the maximum number of retries has been reached.

These exceptions must be handled in the producer app using the **All Exceptions** exception handler.

When you consume events, an exception is raised in the consumer app if the execution time of the event handler exceeds 2 mins. You must handle this exception in the consumer app using **All Exceptions**.

## Additional resources

* [Event-driven architecture in ODC](backend-events.md)

* [Properties of ODC events](events-properties.md)
