---
summary: Edit expressions in OutSystems Developer Cloud (ODC) Studio using its comprehensive expression editor with autocomplete and documentation features.
tags: expression editing, user interface design, autocomplete features
locale: en-us
guid: 1ad176b7-bb78-41f9-ae4a-69d3e0e06a13
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3214%3A21844&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
coverage-type:
  - remember
  - understand
topic:
  - write-expressions-guide
---

# Edit expressions

Edit expressions with the expression editor in ODC Studio. Launch the expression editor by double-clicking one of the following:  

* Expression widget
* Property fields
* Errors and warnings in the TrueChange pane

The following are the parts of the expression editor, with notes on how you can use them.

![Screenshot of the expression editor interface in ODC Studio highlighting the expression field, toolbar, scope pane, description pane, and expression status](images/expression-editor-odcs.png "Expression Editor in ODC Studio")

Expression field
:    Edit your expressions in the expression field (1). Use **Ctrl+Space** to autocomplete a word or show a list of suggestions to use in the expression.

Toolbar
:    The buttons in the toolbar (2) are the operators developers use most often. Click the button to insert the element in the expression field.

Scope pane
:    The scope pane (3) shows the elements you can use in the expression, such as variables, built-in functions, and scripts. The availability of local elements depends on where in the app you're editing the expression. Note that only actions that you set as functions show in the scope pane.

Description pane
:    You can read the details about an element in the description pane (4). If a function has documentation, the documentation shows in the description pane.

Status
:     The expression status (5) tells you if the expression you're editing is valid or not.

## Notes

The following are notes about expression and the expression widget, and the concepts that are closely related to the expression editor.

### Expression, operands, operators

An expression is what you edit in the expression editor. An expression consists of operands and operators. Check out the following topics for more information:

* [Introduction to expressions](../expressions.md)
* [Operands](operands.md)
* [Operators](operators.md)

### Expression widget

To quickly display the result of an expression, use the Expression widget. 
