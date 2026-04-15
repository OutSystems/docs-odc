---
summary: Learn how to start a workflow
tags: workflow editor, event triggering, node configuration, workflow design, workflow management
locale: en-us
guid: 43686a97-7a1c-4ae6-a775-bffb57ac2cd9
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?m=auto&node-id=6048-7&t=ykwyzPl8nKCnnRYC-1
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
---

# Start a workflow

Every workflow in the Workflow editor begins with a **Start** node. This node serves as the entry point that connects your ODC app's user interface to automated business processes. When users interact with your app, such as submitting a loan application or placing an order, these actions trigger events that initiate workflows through the **Start** node.

Using events to trigger workflows follows an [**event-driven architecture**](../events/intro.md) where user actions translate into business process events. For example, when a user submits a loan application through your app's form, it triggers a `LoanApplicationSubmitted` event. The **Start** node receives this event along with all the relevant data (user information, loan amount, documents) and passes it to the subsequent workflow activities for processing.

For detailed information about creating and handling events in ODC, refer to [Implement events](../events/implement-events.md).

You can also use [conditional starts](add-conditional-start.md) to handle other events that might occur while your main workflow is running. For example, in a loan approval workflow, you might add a conditional start that triggers a cancellation process if the user decides to cancel their loan application while it's being reviewed.

## How to start a workflow

To trigger the workflow execution, follow these steps:

1. Assign an event to the **Start** node.

    When this event is triggered, the workflow begins.

1. (Optional) Add an [Instance label](#instance-label).

    An instance label uniquely identifies an instance, making it useful when troubleshooting workflow instances and in workflow logs.

    ![Screenshot of instance label expression](images/instance-label-we.png "Instance label")

## Instance label { #instance-label }

When working with workflows, technical IDs such as ``Process_12345`` don't provide much information. Instance labels allow you to create meaningful names such as ``Loan 67890 - John Smith`` that make it easy to identify specific workflow instances.

You can define an **Instance label** in the **Start** node. The instance label assigns a custom identifier to each workflow instance. Each time a workflow is triggered, a new instance is created, and the instance label helps you uniquely identify that specific instance.

Instance labels help you:

* **Identify workflows**: Use user-friendly names instead of technical IDs

* **Troubleshoot issues**: Quickly find specific workflow instances in logs

* **Track progress**: Monitor and distinguish between workflow instances in the Portal

When creating instance labels, keep the following in mind:

* **What you can use**: The instance label is a dynamic expression that accepts values such as the start event's input parameters, runtime properties, and built-in functions. It has access to the ``ActivityInstanceId``, ``ProcessInstanceId``, and any values from the **Start** node.

* **How to write it**: Create an expression using text, variables, and functions

* **Character limit**: Maximum 100 characters (longer expressions are truncated at runtime)

The following is an example of how to structure an instance label:

For a loan request approval, you might want a custom label that describes the instance ID and the ID of the loan that triggered that workflow. This way, when troubleshooting multiple instances, you can easily identify which instance corresponds to a certain loan request.

```
"Process with Id" + ProcessInstanceId + "started by a new loan with ID" + Start.NewLoan.LoanId
```

![Screenshot of instance label expression](images/instance-label-output-we.png "Instance label")

## Next steps

* [Add human activity](add-human-activity.md)

* [Add automatic activity](add-automatic-activity.md)

* [Add decisions](add-decisions.md)

* [Add wait](add-wait.md)

## Related resources

* [Start a workflow based on specific conditions](add-conditional-start.md)

* [Troubleshooting workflows](troubleshooting-workflows.md)

* [Deploy workflows](../../deploying-apps/deploy-apps.md)
