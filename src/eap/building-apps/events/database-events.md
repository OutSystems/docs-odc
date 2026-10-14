---
guid: 73db3695-0270-4495-915a-df56d5f993c1
locale: en-us
summary: ODC database events trigger after an entity record changes and the transaction commits. Set them up with Mentor Studio or in ODC Studio.
figma:
coverage-type:
  - apply
  - understand
  - evaluate
topic:
  - create-database-event
  - database-event-behavior
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - Developer
  - Architect
tags:
  - Data Integrity
  - Entities
  - Events
  - Triggers
outsystems-tools:
  - odc studio
  - mentor studio
helpids:
isautopublish: true
---

# Database events

Database events are a type of ODC events that are automatically triggered when changes occur in the database entity records. They're triggered only after the database transaction is successfully committed, ensuring data integrity. You can define events that trigger on create, update, or delete operations, such as when a new record is added to an entity through an entity action or through a SQL node.

For detailed information about the properties of database events, refer to [Properties of ODC events](events-properties.md).

## Key benefits

Here are some benefits of using database events.

* Eliminates manual intervention by automating tasks such as logging, sending notifications, or synchronizing data when changes occur.  

* Maintains consistency and reliability of the database since events are triggered only after a successful transaction commit.  

* Responds to data changes immediately, enabling real-time data updates. This ensures that related records, reports, or analytics remain current.

## Use cases

Here are some examples where you can use database events:

**Enforcing referential integrity in multi-app setup**  
 In a microservices architecture, multiple apps write to a shared database. If an app deletes a parent record without considering dependent child records, a database event can enforce referential integrity by automatically deleting or updating dependent records.

**Applying business rules at the database level**  
In a banking app, a customer initiates a payment. The **OnUpdate** database event is raised only after the request transaction succeeds, e.g., after a successful check against the account balance and the account balance is updated in the database. The triggering of the event allows all consumers to be certain that the event is executed only when the payment operation transaction is completed successfully.

**Auto cleanup of orphaned records**  
When a user account is deleted, related records (e.g., user preferences, session data) must also be removed to prevent orphaned data. An **OnDelete** database event ensures cleanup always happens at the database level, independent of app behavior.

## Create a database event with Mentor Studio

Create a database event by describing the entity, the trigger, and the event in Mentor Studio, and validate the event before you publish.

In your prompt, include the following:

* The entity
* The trigger event (**OnCreate**, **OnUpdate**, or **OnDelete**)
* The event to trigger
* The input parameters

For example, the following sentence is a prompt:

* "Add an OnUpdate database event to the Payment entity that triggers the PaymentUpdated event with the Payment identifier as its input parameter, and handle PaymentUpdated with a new server action named NotifyAccountOwner."

### Validate the database event

The platform guarantees that the model is valid, and you decide whether the database event matches your requirement. In the **Data** tab of ODC Studio, select the entity and check the following:

* The **Trigger Event** property selects the operation you need. The entity has at most one event for each trigger event type.
* The **Event** property selects the event you expect.
* The only input parameters are entity identifiers.
* The handler doesn't depend on the order in which the platform triggers the events.
* The handler logic reads the committed data, because the platform triggers the event only after the transaction commits.
* After you publish the app, a record change through an entity action or a SQL node triggers the event, and the handler runs once for each trigger.

## Create a database event manually in ODC Studio

Create database events in ODC apps for **Create**, **Update**, or **Delete** entity actions. These events trigger automatically when the entity actions execute and commit. For example, in a banking app, a customer initiates a payment. The **OnUpdate** database event is raised only after the request transaction succeeds, e.g., after a successful check against the account balance and the account balance is updated in the database. The triggering of the event allows all consumers to be certain that the event is executed only when the payment operation transaction is completed successfully.

To create a database event, follow these steps:

1. Go to the **Data** tab and select the entity to create a database event.

1. From the properties panel, choose either **OnCreate**, **OnUpdate**, or **OnDelete** from the **Trigger Event** drop-down.

    <div class="info" markdown="1">

    You can only add one event of each trigger event type for an entity.

    </div>

1. Select the **Event** to be triggered. You can also create a new event from here. For detailed information about creating a new event, refer to [Create a new event](implement-events.md#create-event).  

1. Select the input parameters for the event.

    <div class="info" markdown="1">

    You can only use entity identifiers as an event input parameter.

    </div>

1. Publish the app.

The platform creates a database event whenever the corresponding entity action executes.
The platform guarantees that it processes all events. However, the implemented logic may determine a different processing order than the trigger order.

For each trigger event, the handler logic executes exactly once. The platform produces no duplicates.

For detailed information about handling database events, refer to [Handle an event](implement-events.md#handle-an-event).

For detailed information about handling errors in events, refer to [Error processing in events](implement-events.md#error-processing-in-events)

## Related resources

The following resources describe Mentor Studio prompts, event implementation, event properties, error handling, and what the platform guarantees.

### Mentor Studio

For prompt examples and the steps to prompt Mentor Studio, refer to the following:

* For more prompt examples, refer to [Prompts for Mentor Studio](../../agentic-development/mentor-studio/prompts.md#logic).
* For the requirements and the steps to prompt Mentor Studio and review the change, refer to [Modify an app with AI in ODC Studio](../../agentic-development/mentor-studio/modify-app.md) and [Review and accept the plan](../../agentic-development/mentor-studio/how-it-works.md#accept-plan).

### Platform guarantees

For what the platform guarantees and what you validate, refer to the following:

* [Platform guarantees and AI interpretation](../../agentic-development/odc-ai-and-platform.md)

### Implement events in ODC

For more information on implementing events in ODC, refer to the following:

* [Event-driven architecture in ODC](backend-events.md)

* [Implements events in ODC](implement-events.md)

### Event properties

For more information on event properties, refer to the following:

* [Properties of events](events-properties.md)

### Error handling

For more information on error handling, refer to the following:

* [Error processing in events](implement-events.md#error-processing-in-events)
