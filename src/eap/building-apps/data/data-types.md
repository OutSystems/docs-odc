---
summary: An overview of data types you can use in your apps.
tags:
locale: en-us
guid: 651e9382-9db0-4150-ad11-c160aa9c9835
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# Data types and conversions

This page describes the data types available in OutSystems, their default values and constraints, and the built-in functions to convert them into another data type.

## Basic data types

Type | Default Value | Example | Comment
---|---|---|---
Binary Data | Byte array with no elements | n/a |
Boolean | false | true or false |
Currency | 0.0 | 545870.025 | See Decimal type.
Date | #1900-01-01# | #1988-08-28# | The  supported range is [#1900-01-01#, #3000-12-31#]
Time | #00:00:00# | #12:20:56# | Minimum value: #00:00:00# <br/><br/>Maximum value: #23:59:59#
Date Time | #1900-01-01 00:00:00# | #1988-08-28 23:59:59# | The supported range is [#1900-01-01 00:00:00#, #3000-12-31 23:59:59#]<br/><br/>The date time is always in UTC.
Integer | 0 | 2147483600 | Minimum value: -2^31, which is -2147483648.<br/><br/>Maximum value: 2^31-1, which is 2147483647.
Long Integer | 0 | 5645245584135987412 | Minimum value: -2^63<br/>Maximum value: 2^63-1
Decimal | 0.0 | -158121.025 <br/>4000.0 | Integer and decimal parts must be separated by a period. <br/><br/>Minimum value: -2^96 <br/><br/>Maximum value: 2^96-1<br/><br/>The maximum number of digits in the decimal part is 8.
Email | "" (empty string) | "[user@example.com](mailto:user@example.com)" |
Phone Number | "" (empty string) | "+1 555 565 3730" |
Text | "" (empty string) | "Hello, wrold!" |
&lt;Entity&gt; Identifier | When an Entity is created, the &lt;Entity&gt; identifier data type is created for the identifier attribute. | |

## Compound data types

|Type|Comments|
|--- |--- |
|`<Entity>` or `<Structure>`|When an Entity or Structure is created, a data type is also created with all the attributes of that Entity or Structure. For example, when the Customer entity is created, the Customer data type is created. To create a variable of this data type, simply set its **Data Type** property to `Customer`.<br/>To access an attribute of the variable, use the following syntax: `.`, for example `MyCustomerVar.Name`.|
|Object|OutSystems supports the Object data type to allow to reuse your own .NET classes. The default value is NullObject().|
|Record|A Record is a data type that's composed of a fixed number of attributes, each one with its own data type. Use a Record to define a compound data type that is used for a single variable. If you need to define more than one variable with the same compound data type, use a Structure instead. Some use cases for using the Record data type are:<br/>• You need to return the result of an Aggregate on a User Action. In this case, you can define the user action output parameter using the record data type.<br/>• You need a user action that returns compound information, but don't want to define a new Structure.|
  
## Collection data types

|Type|Comments|
|--- |--- |
|List|A List is a sequence of elements of the same data type, either basic or compound. Elements can be inserted, fetched, and removed from a List.|
  
## Default and null values

OutSystems does not use the concept of the NULL value, except for the Entity Identifier data type. Therefore, each data type has an associated default value that is assigned at creation.

## Data type conversions

OutSystems enables the conversion between different data types. This can be made implicitly, or explicitly by using data type conversion functions.

### Implicit conversion

OutSystems automatically converts values of the following types:

Expected Type | Accepted Types | Obs.
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