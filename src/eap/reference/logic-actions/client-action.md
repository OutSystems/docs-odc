---
summary: Explore client-side logic execution and properties in ODC with detailed guidelines on exposed client actions and their restrictions.
locale: en-us
guid: 0B5C80E1-DE16-48CD-BA5C-171891C049B1
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
tags: client-side logic, exposed actions, session variables, entity/structure restrictions, action properties
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
---

# Client Action

Action that runs logic on the client side.  

## Exposed Client Action

A Client action cannot be exposed when:

* Is defined in an App.
* When in a Library it has a parameter that is defined using an Static Entity that is not exposed.

## Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Mandatory</th>
<th>Default value</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td title="Name">Name</td>
<td>Identifies an element in the scope where it is defined, like a screen or action.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Description">Description</td>
<td>Text that documents the element.</td>
<td></td>
<td></td>
<td>Useful for documentation purpose.<br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="Public">Public</td>
<td>When in a Library, set to Yes to allow the server action to be added as dependency by other libraries or apps.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td title="Function">Function</td>
<td>Set to Yes to define the action as a function. Functions must return a value and can be used in expressions.</td>
<td>Yes</td>
<td>No</td>
<td>This property is only available in global scope actions. Client actions set as functions can only be used in client action expressions.</td>
</tr>
<tr>
<td title="Icon">Icon</td>
<td>Picture to be displayed to help identify this element.</td>
<td>Yes</td>
<td></td>
<td>The recommended dimensions for the icon are 32 &#215; 32 pixels.</td>
</tr>
<tr>
<td title="Original Name">Original Name</td>
<td>Name of the element as defined in the library which implements it (producer). This property is read-only.</td>
<td>Yes</td>
<td></td>
<td>This property is only visible for referenced elements.</td>
</tr>
</tbody>
</table>
