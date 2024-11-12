---
summary: Learn how to add decisions to your workflow in OutSystems Developer Cloud (ODC).
tags:
locale: en-us
guid: c5d2a739-ccde-4f66-b9f9-9b8b7a3e46f7
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# Add decisions 

When implementing your workflow, use a Decision node to create multiple paths based on conditions. By default, the Decision node provides two outcomes. Define the condition for each outcome. The conditions are evaluated one at a time and can only follow through on one outcome.

You can select one or more service actions for your Decision node to fetch additional data for your conditions. For example, select the GetManagerUserID service action to get a user's manager information. Use this User ID in your conditions to check if the manager has approved the user's vacation.

To include decisions in a workflow, follow these steps:

1. From your workflow editor,  click the (+) icon between two nodes and select the **Decision** process node.

1. Enter the following details in the sidebar:

   a. **Add description**: (Optional) Brief description of the decision task to be carried out.

   b. **Fetch more data**: (Optional) Select a service action from the corresponding ODC app and enter the service action's corresponding input parameters. For example, you can select a service action (GetFinancialStatus) and then define the condition for the Outcomes.

   c. **Outcome 1**: Enter the condition to evaluate. If the condition is evaluated as true, then the workflow follows this path. 

   d. **Outcome 2**:  If the condition for Outcome 1 is false, enter the condition to evaluate for this outcome. 

   e. **Otherwise branch:** If all conditions fail, the workflow follows this branch. **Note:** The order of the outcomes determines the position on the sidebar, with the last position being the otherwise branch. You can rename Outcomes to provide more meaningful names for the conditional paths.

If your workflow involves multiple conditional paths, you can add more than two outcomes to a decision. The following elements are available for use in the expression editor while specifying the condition: 

* Output parameters from previously executed elements in the process flow path

* Input parameters from previously executed events

* Process input and output parameters

* Decision local variable

* Actions output parameters invoked in the **Decision** node

* Queries Invoked in the **Decision** node

* Built-in functions
