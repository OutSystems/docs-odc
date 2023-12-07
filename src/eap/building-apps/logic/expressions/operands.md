---
summary: Operands, in an expression, tell the platform which data to use. Read more about literals, variables, and functions.
tags: 
locale: en-us
guid: 6c363890-b0af-4d1c-92ae-1cb346aa6f7d
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3214%3A21846&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Operands

An operand tells the platform which data to use to manipulate an expression. For example, in the expression `MyValue + 1`, `MyValue` and `1` are the operands. 

Use the [expression editor](expression-editor.md) to see which operands are available in the current scope. The expression editor checks what variable, parameters, functions, and other values, you can use for an operation in, for example, a screen or an action.

All operands always have a [data type](../../data/data-types.md).

## Literals

Literals are hard-coded values that you write in expressions, most often numbers and text. The following are some examples:

* In `Message = "Hello, world!"`, **Hello, world!** is a literal.
* In `1 + i`, **1** is a literal.
* In `isValid = False`, **False** is a literal.

Check out [basic data types](../../data/data-types.md#Basic-Data-Types) for other examples of how you can use literals in expressions.

## Variables

Variables are identifiers that point to values. Here are some examples.

* In `Message = "Hello, world!"`, **Message** is a variable.
* In `1 + i`, **i** is a variable.
* In `isValid = False`, **isValid** is a variable.

<div class="info" markdown="1">

Use smart names to set the data type automatically. For example, if you create a value or parameter, and name it **PurchaseDate**, ODC Studio sets the data type to **Date**.

</div>

## Functions

You can use functions as operands. The following are some examples:

* In `Sqrt(9) + 3`, **Sqrt()** is one of the built-in functions. 
* In `MyFunction(1000) * 100`, **MyFunction()** is a user-defined function. 

See [Built-in Functions](<../../../reference/built-in-functions/intro.md>) for more information.

## Example

The following is a screenshot showing an expression in the expression editor. The expression consists of:

* `3000`: a literal
* `MyInteger`: a local variable
* `Sqrt()`: a built-in function

![Screenshot showing an expression in the expression editor](images/operands-ss.png?width=650 "Expression Editor")
