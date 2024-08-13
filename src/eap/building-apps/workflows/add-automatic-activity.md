---
summary: Learn how to add an automatic activity to your workflow
tags:
locale: en-us
guid: 2ed780f3-ca62-411b-97d4-252a201c7d80
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# Add automatic activity 

When implementing your workflow, you can include tasks to be done automatically without needing human intervention. This is accomplished by including an AutomaticActivity node in your workflow.

To include automatic activity in a workflow, follow these steps:

1. From the workflow editor, click the (+) icon between the two nodes and choose **Automatic activity**.

1. Select the service action to execute when the flow reaches the AutomaticActivity node. For example, in a loan approval workflow, you can include an AutomaticActivity node to request documents from the customer when receiving a new loan application. You can implement Request Docs as a service action in the ODC Loan app and invoke it in the AutomaticActivity node.

    **Note:** If the service action has one or more input parameters, enter values for the mandatory input parameters to execute the service action. Only input parameters with default data types can be used. The Binary data type is excluded.
