---
summary: "OutSystems Developer Cloud (ODC) data type conversion: implicit rules and explicit functions like BooleanToInteger and TextToDate."
tags:
  - Data
  - Logic
locale: en-us
guid: 62dd6548-d073-4ccb-90c1-8f4bfa4a0bfd
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
  - remember
  - apply
  - evaluate
topic:
  - built-in-conversion-functions
  - implicit-conversion-rules
isautopublish: true
---

# Convert data types

OutSystems enables the conversion between different data types. This can be made implicitly, or explicitly by using data type conversion functions. You apply a conversion by describing it to Mentor Studio and validating the result, or by choosing the conversion manually in ODC Studio.

## Convert a data type with Mentor Studio

Convert a data type by describing the element and the target data type in Mentor Studio, and validate the conversion where the element is used before you publish.

In your prompt, name the element, the source data type, and the target data type. Alternatively, paste the data type warning that ODC Studio shows. For example, "Fix the 'Data Type Mismatch' warning that appears when the Text variable TicketIdText is assigned to the TicketId attribute of type Ticket Identifier."

For more prompt examples, refer to [Prompts for Mentor Studio](../../agentic-development/mentor-studio/prompts.md#fix-errors-and-warnings).

For the requirements and the steps to prompt Mentor Studio and review the change, refer to [Modify an app with AI in ODC Studio](../../agentic-development/mentor-studio/modify-app.md) and [Review and accept the plan](../../agentic-development/mentor-studio/how-it-works.md#accept-plan).

### Validate the conversion

The platform guarantees that the model is valid, and you decide whether the conversion is correct for your data. Check the following against the tables on this page:

* A conversion that isn't in the implicit conversion table uses the explicit function for the source and target types, such as `TextToDecimal` or `DateTimeToDate`.
* The function returns the target data type. `TextToIdentifier` returns a Text Identifier only. For an entity identifier of type Long Integer, the conversion chains two functions, such as `LongIntegerToIdentifier(TextToLongInteger(TicketIdText))`.
* An implicit conversion from Decimal to Integer truncates the decimals. If the decimals matter, the logic doesn't convert implicitly.
* An implicit conversion from one Entity Identifier to the identifier of another Entity displays a warning. The warning is intended only when the two identifiers represent the same record.
* No data type mismatch warning remains on the element after the change.

## Convert a data type manually in ODC Studio

To convert a data type manually, use implicit conversion where the following table allows it, and use an explicit conversion function everywhere else.

## Implicit conversion functions

OutSystems automatically converts values of the following types:

| Expected Type | Accepted Types | Notes |
| --- | --- | --- |
| Boolean | - | |
| Currency | Decimal, Integer, Boolean, Entity Identifier(Integer) | |
| Date | Date Time | |
| Date Time | Date, Text, Time | |
| Integer | Decimal, Boolean, Currency, Entity Identifier(Integer) | When converting Decimal to Integer implicitly, the decimals are truncated. |
| Long Integer | Long Integer, Integer, Decimal, Boolean, Currency, Entity Identifier(Integer), Entity Identifier(Long Integer) | |
| Decimal | Integer, Boolean, Currency, Entity Identifier(Integer) | |
| Entity Identifier | Entity Identifier | A certain Entity Identifier can be converted into another Entity's Identifier, but a warning is displayed. |
| Email | Text, Phone Number, Integer, Decimal, Boolean, Currency, Entity Identifier(Integer), Entity Identifier(Text), Date Time, Date, Time | |
| Phone Number | Text, Email, Integer, Decimal, Boolean, Currency, Entity Identifier(Integer), Entity Identifier(Text), Date Time, Date, Time | |
| Text | Integer, Decimal, Boolean, Currency, Phone Number, Email, Entity Identifier(Integer), Entity Identifier(Text) | |

## Explicit conversion functions

To convert values from one data type to another use data type conversion functions.

Here is a summary about the possible explicit conversions:

| From | To | Function |
| --- | --- | --- |
| Boolean | Integer<br/>Text | BooleanToInteger<br/>BooleanToText |
| Date | Date Time<br/>Text | DateToDateTime<br/>DateToText |
| Date Time | Date<br/>Text<br/>Time | DateTimeToDate<br/>DateTimeToText<br/>DateTimeToTime |
| Integer | Boolean<br/>Decimal<br/>Text<br/>Integer Identifier | IntegerToBoolean<br/>IntegerToDecimal<br/>IntegerToText<br/>IntegerToIdentifier |
| Long Integer | Long Integer Identifier<br/>Integer<br/>Text | LongIntegerToIdentifier<br/>LongIntegerToInteger<br/>LongIntegerToText |
| Decimal | Boolean<br/>Integer<br/>Long Integer<br/>Text | DecimalToBoolean<br/>DecimalToInteger<br/>DecimalToLongInteger<br/>DecimalToText |
| Entity Identifier (Integer) | Integer | IdentifierToInteger |
| Entity Identifier (Long Integer) | Long Integer | IdentifierToLongInteger |
| Entity Identifier (Text) | Text | IdentifierToText |
| Text | Date<br/>Date Time<br/>Decimal<br/>Integer<br/>Long Integer<br/>Time<br/>Text Identifier | TextToDate<br/>TextToDateTime<br/>TextToDecimal<br/>TextToInteger<br/>TextToLongInteger<br/>TextToTime<br/>TextToIdentifier |
| Time | Text | TimeToText |
| Any data type | Object | ToObject |

For the parameters and output of each function, and for the functions that check whether a conversion is possible, such as `TextToLongIntegerValidate`, refer to [Data Conversion](../../reference/built-in-functions/data-conversion.md).

To learn more about how to convert values from one data type to another, refer to [aggregate](./fetch-data/aggregate.md).

## Related resources

The following resource describes what the platform guarantees and what you check in a Mentor Studio proposal.

* For what the platform guarantees and what you validate, refer to [Platform guarantees and AI interpretation](../../agentic-development/odc-ai-and-platform.md).
