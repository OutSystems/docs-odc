---
summary: OutSystems Developer Cloud (ODC) apps implement logic through actions. Build them with Mentor Studio or manually in ODC Studio.
tags:
  - Logic
  - Programming Model
locale: en-us
guid: 4968c372-2dc8-4131-8f37-7951fec8f431
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
  - mentor studio
coverage-type:
  - understand
  - apply
  - evaluate
topic:
  - creating-actions
isautopublish: true
---

# Application logic

In OutSystems, the logic of your apps is implemented through **Actions**. While developing your apps, you can create your own custom actions and use the actions OutSystems provides you.

You build logic by describing the change to Mentor Studio and validating what it proposes, or by building the elements manually in ODC Studio. For more information, refer to [Modify an app with AI in ODC Studio](../../agentic-development/mentor-studio/modify-app.md).

## Correct logic output

The platform guarantees that the model is valid, and you decide whether the logic does what your requirement needs. Whether you build manually or review a Mentor Studio proposal, the following checks apply. They are examples, not a complete list.

* **Actions.** The logic is implemented in custom actions or in the actions OutSystems provides.
* **Parameters.** Every call passes the value you intend for each mandatory Input Parameter, and the flow of an action you build assigns each Output Parameter. For a consumed REST API, OutSystems fills the Output Parameters from the response of the external system. For more information, refer to [Input Parameter](input-parameter.md) and [Output Parameter](output-parameter.md).
* **Variables.** Each variable has the scope your logic needs. For more information, refer to [Local Variable](local-variable.md).
* **Expressions.** Each expression is valid and uses operators that its data types allow. For more information, refer to [Expressions](expressions.md).
* **Practices.** The flow follows the recommendations for performance and security. For more information, refer to [Best practices for logic](best-practices-logic.md).

## Related resources

The following resources describe training for logic and what you check in a Mentor Studio proposal.

* [Logic](https://learn.outsystems.com/training/journeys/logic-641) online course
* For what the platform guarantees and what you validate, refer to [Platform guarantees and AI interpretation](../../agentic-development/odc-ai-and-platform.md).
