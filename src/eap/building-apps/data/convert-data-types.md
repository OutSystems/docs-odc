---
summary: Explore conversion functions in OutSystems Developer Cloud (ODC).
tags:
locale: en-us
guid: 62dd6548-d073-4ccb-90c1-8f4bfa4a0bfd
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# Convert data types

OutSystems enables the conversion between different data types. This can be made implicitly, or explicitly by using data type conversion functions.

### Implicit conversion functions

OutSystems automatically converts values of the following types:

Expected Type | Accepted Types | Notes
---|---|---
Boolean | - |
Currency | Decimal, Integer, Boolean, Entity Identifier(Integer) |
Date | Date Time |
Date Time | Date, Text, Time |
Integer | Decimal, Boolean, Currency, Entity Identifier(Integer) | When converting Decimal to Integer implicitly, the decimals are truncated.
Long Integer | Long Integer, Integer, Decimal, Boolean, Currency, Entity Identifier(Integer), Entity Identifier(Long Integer) |
Decimal | Integer, Boolean, Currency, Entity Identifier(Integer) |
Entity Identifier | Entity Identifier |  A certain Entity Identifier can be converted into another Entity's Identifier, but a warning is displayed.
Email | Text, Phone Number, Integer, Decimal, Boolean, Currency, Entity Identifier(Integer), Entity Identifier(Text), Date Time, Date, Time |
Phone Number | Text, Email, Integer, Decimal, Boolean, Currency, Entity Identifier(Integer), Entity Identifier(Text), Date Time, Date, Time |
Text | Integer, Decimal, Boolean, Currency, Phone Number, Email, Entity Identifier(Integer), Entity Identifier(Text) |

### Explicit conversion functions

To convert values from one data type to another use data type conversion functions.

Here is a summary about the possible explicit conversions:

From | To | Function
---|---|---
 Boolean | Integer<br/>Text | BooleanToInteger<br/>BooleanToText
Date | Date Time<br/>Text | DateToDateTime<br/>DateToText
Date Time | Date<br/>Text<br/>Time | DateTimeToDate<br/>DateTimeToText<br/>DateTimeToTime
Integer | Boolean<br/>Decimal<br/>Text<br/>Integer Identifier | IntegerToBoolean<br/>IntegerToDecimal<br/>IntegerToText<br/>IntegerToIdentifier
Long Integer | Long Integer Identifier<br/>Integer<br/>Text | LongIntegerToIdentifier<br/>LongIntegerToInteger<br/>LongIntegerToText
Decimal | Boolean<br/>Integer<br/>Text | DecimalToBoolean<br/>DecimalToInteger<br/>DecimalToText
Entity Identifier (Integer) | Integer | IdentifierToInteger
Entity Identifier (Long Integer) |  Long Integer  | IdentifierToLongInteger
Entity Identifier (Text) | Text | IdentifierToText
Text | Date<br/>Date Time<br/>Decimal<br/>Integer<br/>Time<br/>Text Identifier | TextToDate<br/>TextToDateTime<br/>TextToDecimal<br/>TextToInteger<br/>TextToTime<br/>TextToIdentifier
Time | Text | TimeToText
Any data type | Object | ToObject

To learn more about how to convert values from one data type to another, refer to [aggregate](./fetch-data/aggregate.md).
