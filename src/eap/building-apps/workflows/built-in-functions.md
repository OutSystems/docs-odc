---
summary: Lear more about the built-in fucntions availbale for workflows in ODC
tags: workflow functions, logic implementation, built-in functions in workflows, outsystems development, workflow development
guid: 2370adfe-ecfc-4e6a-ab9e-0f94b74ac148
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
---

# Using built-in functions in workflows

Just as [built-in functions](https://success.outsystems.com/documentation/11/reference/outsystems_language/logic/built_in_functions/) are used in app development, they are also available when creating workflows. During workflow implementation, expressions can be applied in various scenarios, including decision conditions, inputs for service actions, and parameters or messages for human activities

The following table details the built-in functions available in ODC Studio for workflows. 

|  |  |
| --- | --- |
| **Built-in function group** | **Available for workflows** |
| Math | Yes|
| Numeric | Yes  |
| Text  | Yes  |
| Date and Time| Yes |
| Data Conversion | Partially<p>**NullObject()** and **ToObject()** are not available.</p> <p> The **object** data type is not supported for workflows. </p>|
| Format  | Yes |
| Email| Yes |
| Organization | No |
| URL| No |
| Miscellaneous | Yes|
| Roles | Yes|
| Security| No |        

## Related resources

* [Implement workflows](using-workflows.md)

* [Troubleshooting workflows](troubleshooting-workflows.md)
