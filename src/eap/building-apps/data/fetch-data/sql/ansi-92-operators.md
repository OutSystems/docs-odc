---
guid: 8487ccec-2b67-4271-933d-5b046e3bcbb5
locale: en-us
summary: Understand supported SQL operators and functions in queries with external entities in OutSystems Developer Cloud (ODC).
figma: 
coverage-type:
  - apply
  - remember
topic:
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - backend developers
  - full stack developers
  - tech leads
tags: sql operators,functions,external systems,null behavior,comparison operators
outsystems-tools:
  - odc studio
---

# ANSI-92 operators and functions

The tables below outline the supported SQL operators and functions when working with external systems.

When a query only references entities from one connection, the operator and function calls will be pushed down in the query to the external system in most cases. When this happens, the behaviour of the operator / function will be the same as the native equivalent on the external system.

When a query references entities from more than one connection (for example, in a [mashup query](../data-mash.md)), the operator and function calls are usually pushed down if they only reference attributes from one connection. If an operator or function call references attributes from multiple connections then it won't be pushed down and handled in ODC instead. When this happens, the operator or function may have different behaviour compared to the equivalent operator or function in any particular external system.

NULL behaviour can vary between external systems. For example, Oracle treats empty strings as NULL which means the expression `COALESCE([attribute], '') IS NULL` can evaluate as TRUE in Oracle but is always FALSE in other providers. If this expression is not pushed down, then it assumes the ODC behavior, in which case the empty string is not considered to be NULL.

## Comparison operators

| Operator syntax                  | Description                                                                                                                                        | NULL Behaviour                                              |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| `value1 = value2`                  | Whether *value1* is equal to *value2*                                                                                                              | NULL if any operand is NULL                                 |
| `value1 <> value2`                 | Whether *value1* is not equal to *value2*                                                                                                          | NULL if any operand is NULL                                 |
| `value1 > value2`                 | Whether *value1* is greater than *value2*                                                                                                          | NULL if any operand is NULL                                 |
| `value1 >= value2`                 | Whether *value1* is greater than or equal to *value2*                                                                                              | NULL if any operand is NULL                                 |
| `value1 < value2`                 | Whether *value1* is less than *value2*                                                                                                             | NULL if any operand is NULL                                 |
| `value1 <= value2`                 | Whether *value1* is less than or equal to *value2*                                                                                                 | NULL if any operand is NULL                                 |
| `value IS NULL`                   | Whether *value* is null                                                                                                                            | TRUE if *value* is NULL                                     |
| `value IS NOT NULL`                | Whether *value* is not null                                                                                                                        | FALSE if *value* is NULL                                    |
| `string1 LIKE string2`             | Whether *string1* matches pattern *string2*<br/>The pattern may contain the `%` (zero or more characters) and `_` (one character) wildcards        | NULL if any operand is NULL                                 |
| `string1 NOT LIKE string2`         | Whether *string1* does not match pattern *string2*<br/>The pattern may contain the `%` (zero or more characters) and `_` (one character) wildcards | NULL if any operand is NULL                                 |
| `value1 IN (value [, value]*)`    | Whether *value* is equal to a value in a list                                                                                                      | NULL if *value1* is NULL or if the list only contains NULLs |
| `value1 NOT IN (value [, value]*)` | Whether *value* is not equal to every value in a list                                                                                              | NULL if *value1* is NULL or if the list only contains NULLs |
| `value IN (sub-query)`            | Whether *value* is equal to a row returned by *sub-query*                                                                                          | NULL if *value* is NULL                                     |
| `value NOT IN (sub-query)`         | Whether *value* is not equal to every row returned by *sub-query*                                                                                  | NULL if *value* is NULL                                     |
| `EXISTS (sub-query)`               | Whether *sub-query* returns at least one row                                                                                                       | Never NULL                                                  |
| `UNIQUE (sub-query)`               | Whether the rows returned by *sub-query* are unique (ignoring null values)                                                                         | Never NULL                                                  |

## Logical operators

| Operator syntax       | Description                                      | Null Behaviour              |
|:----------------------|:-------------------------------------------------|-----------------------------|
| `boolean1 OR boolean2`  | Whether *boolean1* is TRUE or *boolean2* is TRUE | NULL if any operand is NULL |
| `boolean1 AND boolean2` | Whether *boolean1* and *boolean2* are both TRUE  | NULL if any operand is NULL |
| `NOT boolean`           | Whether *boolean* is not TRUE                    | NULL if *boolean* is NULL   |
| `boolean IS FALSE`      | Whether *boolean* is FALSE                       | FALSE if *boolean* is NULL  |
| `boolean IS NOT FALSE`  | Whether *boolean* is not FALSE                   | TRUE if *boolean* is NULL   |
| `boolean IS TRUE`      | Whether *boolean* is TRUE                        | FALSE if *boolean* is NULL  |
| `boolean IS NOT TRUE`  | Whether *boolean* is not TRUE                    | TRUE if *boolean* is NULL   |

## Arithmetic operators and functions

| Operator syntax                 | Description                                                                                          | NULL Behaviour              |
|---------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------|
| `+ numeric `                      | Returns *numeric*                                                                                    | NULL if *numeric* is NULL   |
| `- numeric`                       | Returns negative *numeric*                                                                           | NULL if *numeric* is NULL   |
| `numeric1 + numeric2 `            | Returns *numeric1* plus *numeric2*                                                                   | NULL if any operand is NULL |
| `numeric1 - numeric2`             | Returns *numeric1* minus *numeric2*                                                                  | NULL if any operand is NULL |
| `numeric1 \* numeric2`            | Returns *numeric1* multiplied by *numeric2*                                                          | NULL if any operand is NULL |
| `numeric1 / numeric2 `            | Returns *numeric1* divided by *numeric2*                                                             | NULL if any operand is NULL |
| `MOD(numeric1, numeric2) `        | Returns the remainder after *numeric1* is divided by *numeric2*                                      | NULL if any operand is NULL |
| `POWER(numeric1, numeric2)`       | Returns *numeric1* raised to the power of *numeric2*                                                 | NULL if any operand is NULL |
| `ABS(numeric)`                    | Returns the absolute value of *numeric*                                                              | NULL if *numeric* is NULL   |
| `SQRT(numeric)`                   | Returns the square root of *numeric*                                                                 | NULL if *numeric* is NULL   |
| `FLOOR(numeric) `                 | Rounds *numeric* down, returning the largest integer that is less than or equal to *numeric*         | NULL if *numeric* is NULL   |
| `ROUND(numeric1 [, numeric2])`    | Rounds *numeric1* to optionally *numeric2* (if not specified 0) places right to the decimal point    | NULL if any operand is NULL |
| `TRUNCATE(numeric1 [, numeric2])` | Truncates *numeric1* to optionally *numeric2* (if not specified 0) places right to the decimal point | NULL if any operand is NULL |

### Known issues

* MOD is not supported with Microsoft SQL Server.
* Mashup queries may return an error when MOD encounters a NULL divisor.
* Mashup queries may return an error when ABS, ROUND, or TRUNCATE encounter a NULL value.

## Character string operators and functions

| Operator syntax                                                     | Description                                                                                                      | NULL Behaviour              |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|-----------------------------|
| `string || string`                                       | Concatenates two character strings                                                                               | NULL if any operand is NULL |
| `CHAR_LENGTH(string)`                                                | Returns the number of characters in a character string                                                           | NULL if *string* is NULL    |
| `CHAR_INDEX(string, string [\,integer])`                               | Same as `POSITION`                                                                                              | NULL if any operand is NULL |
| `CHARACTER_LENGTH(string)`                                            | Same as `CHAR_LENGTH`                                                                                            | NULL if *string* is NULL    |
| `UPPER(string)`                                                       | Returns a character string converted to upper case                                                               | NULL if *string* is NULL    |
| `LOWER(string)`                                                      | Returns a character string converted to lower case                                                               | NULL if *string* is NULL    |
| `POSITION(string1 IN string2)`                                      | Returns the position (1 - N) of the first occurrence of *string1* in *string2*                                   | NULL if any operand is NULL |
| `POSITION(string1 IN string2 FROM integer)`                          | Returns the position (1 - N) of the first occurrence of *string1* in *string2* starting at a given point         | NULL if any operand is NULL |
| `TRIM( { BOTH | LEADING | TRAILING } string1 FROM string2)` | Removes the longest string containing only the characters in *string1* from the start/end/both ends of *string1* | NULL if any operand is NULL |
| `SUBSTRING(string FROM integer)`                                      | Returns a substring of a character string starting at a given point                                              | NULL if any operand is NULL |
| `SUBSTRING(string FROM integer FOR integer)`                          | Returns a substring of a character string starting at a given point with a given length                          | NULL if any operand is NULL |

### Known issues

* Mashup queries may return an error when either UPPER or LOWER encounter a NULL value.

## Date/time functions { #datetime-functions }

| Operator syntax                               | Description                                                                                                                                   | NULL Behaviour                             |
|:----------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| `CURRENT_TIME`                                | Returns the current time in the server time zone, in a value of datatype TIMESTAMP WITH TIME ZONE                                             | Never NULL                                 |
| `CURRENT_DATE`                                | Returns the current date in the server time zone, in a value of datatype DATE                                                                 | Never NULL                                 |
| `CURRENT_TIMESTAMP`                           | Returns the current date and time in the server time zone, in a value of datatype TIMESTAMP WITH TIME ZONE                                    | Never NULL                                 |
| `EXTRACT(timeUnit FROM datetime)`             | Extracts and returns the value of a specified datetime field from a datetime value expression                                                 | NULL if *datetime* is NULL                 |
| `MONTH(datetime)`                             | Equivalent to `EXTRACT(MONTH FROM datetime)`. Returns an integer between 1 and 12                                                             | NULL if *datetime* is NULL                 |
| `WEEK(datetime)`                              | Equivalent to `EXTRACT(WEEK FROM datetime)`. Returns an integer between 1 and 53                                                              | NULL if *datetime* is NULL                 |
| `DAYOFYEAR(datetime)`                         | Equivalent to `EXTRACT(DOY FROM datetime)`. Returns an integer between 1 and 366                                                              | NULL if *datetime* is NULL                 |
| `DAYOFMONTH(datetime)`                        | Equivalent to `EXTRACT(DAY FROM datetime)`. Returns an integer between 1 and 31                                                               | NULL if *datetime* is NULL                 |
| `DAYOFWEEK(datetime)`                         | Equivalent to `EXTRACT(DOW FROM datetime)`. Returns an integer between 1 and 7                                                                | NULL if *datetime* is NULL                 |
| `HOUR(datetime)`                              | Equivalent to `EXTRACT(HOUR FROM datetime)`. Returns an integer between 0 and 23                                                              | NULL if *datetime* is NULL                 |
| `MINUTE(datetime)`                            | Equivalent to `EXTRACT(MINUTE FROM datetime)`. Returns an integer between 0 and 59                                                            | NULL if *datetime* is NULL                 |
| `SECOND(datetime)`                            | Equivalent to `EXTRACT(SECOND FROM datetime)`. Returns an integer between 0 and 59                                                            | NULL if *datetime* is NULL                 |
| `TIMESTAMPADD(timeUnit, integer, datetime)`   | Returns *datetime* with an interval of (signed) *integer* *timeUnit*s added.<br/>Equivalent to `datetime + INTERVAL (integer) timeUnit`       | NULL if *integer* or *datetime* is NULL    |
| `TIMESTAMPDIFF(timeUnit, datetime1, datetime2)` | Returns the (signed) number of *timeUnit* intervals between *datetime1* and *datetime2*.<br/>Equivalent to `(datetime2 - datetime1) timeUnit` | NULL if *datetime1* or *datetime2* is NULL |
| `FORMAT_DATE(date, format)`                   | Converts a *date* into a string using the given format, see [Date/Time Formatting](#datetime-formatting)                                      | NULL if any operand is NULL                |
| `FORMAT_TIMESTAMP(timestamp, format)`         | Converts a *datetime* into a string using the given *format*, see [Date/Time Formatting](#datetime-formatting)                                | NULL if any operand is NULL                |
| `TO_DATE(string, format)`                     | Converts a *string* into a date using the specified *format*, see [Date/Time Formatting](#datetime-formatting)                                | NULL if any operand is NULL                |
| `TO_TIMESTAMP(string, format)`                | Converts a *string* into a timestamp using the specified *format*, see [Date/Time Formatting](#datetime-formatting)                           | NULL if any operand is NULL                |

### Date/time formatting { #datetime-formatting }

| Format Specifier | Description                                                      |
|------------------|------------------------------------------------------------------|
| YYYY             | Year with century as a decimal number                            |
| YY               | Last two digits of year                                          |
| MM               | Month as a two digit decimal number (01 - 12)                    |
| MON              | Abbreviated month name                                           |
| MONTH            | Full month name                                                  |
| DAY              | Abbreviated day of week name (Mon, Tue, Wed, Thu, Fri, Sat, Sun) |
| DD               | Day of the month as a two digit decimal number (01 - 31)         |
| D                | Day of week as a decimal number (1 - 7)                          |
| HH24             | The hour (24-hour clock) as a two digit decimal number (00 - 23) |
| HH12             | The hour (12-hour clock) as a two digit decimal number (01 - 12) |
| MI               | The minute as a two digit decimal number (00 - 59)               |
| SS               | The second as a decimal number (00 - 59)                         |
| AM / PM          | Meridiem indicator (AM / PM)                                     |

#### Examples

```sql
FORMAT_DATE(DATE '2020-03-01', 'DD/MM/YYYY')
-- Result: '01/03/2020'

TO_TIMESTAMP('01/03/2020 2:30:45 pm', 'DD/MM/YYYY HH12:MI:SS AM')
-- Result: 2020-03-01 14:30:45
```

### Known Issues

* `TIMESTAMPADD` and `TIMESTAMPDIFF` will return an error if used with `CURRENT_DATE` or `CURRENT_TIMESTAMP`. The same issue also occurs with the `+ INTERVAL` and `datetime2 - datetime1`syntax.

## Conditional functions and operators

| Operator syntax                                                                                                                     | Description                                                                                                                                                                                                                              | NULL Behaviour                                                                                                                    |
|:------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| `CASE value`<br/>`WHEN value1 [, value11 ]* THEN result1`<br/>`[ WHEN valueN [, valueN1 ]* THEN resultN ]*`<br/>`[ ELSE resultZ ]`<br/> `END` | This is a simple CASE expression.<br/>If *value* is equal to any of the values in a given WHEN then the result from the associated THEN is returned.<br/>If no matches are found and ELSE is specified, the result from ELSE is returned | NULL if no matches are found and ELSE is omitted.<br/>WHEN NULL will never match due to the null behaviour of the equals operator |
| `CASE`<br/>`WHEN condition1 THEN result1`<br/>`[ WHEN conditionN THEN resultN ]*`<br/>`[ ELSE resultZ ]`<br/>`END`                            | This is a searched CASE expression.<br/>If the condition in a given WHEN is TRUE then the result from the associated THEN is returned.<br/>If none of the conditions are TRUE and ELSE is specified, the result from ELSE is returned    | NULL if no conditions are TRUE and ELSE is omitted.<br/>WHEN NULL will never match since NULL is neither TRUE nor FALSE           |
| `NULLIF(value1, value2)`                                                                                                              | Returns NULL *value1* is equal to *value2*, otherwise returns *value1*                                                                                                                                                                   | NULL if *value1* is NULL or *value1* matches *value2*                                                                             |
| `NULL_OR_VALUE(value1 , value2, value3)`                                                                                              | Returns NULL if *value1* or *value2* is NULL, otherwise returns *value3*                                                                                                                                                                 | NULL if any operand is NULL                                                                                                       |
| `COALESCE(value, value [, value ]*)`                                                                                                  | Returns the first value in the sequence which IS NOT NULL                                                                                                                                                                                | NULL if all operands are NULL                                                                                                     |

### Known issues

* Mashup queries may return an error when using NULLIF, consider using `CASE value1 WHEN value2 THEN NULL ELSE value1` instead.

## Aggregate functions

Syntax:

```sql
agg ( * ) [ FILTER (WHERE condition) ]

agg ( [ ALL | DISTINCT ] value [, value ]* ) [ FILTER ( WHERE condition ) ] 
```

Where *agg* is one of the operators in the following table.

If `FILTER` is present, the aggregate function only considers rows for which *condition* evaluates to TRUE.

If `DISTINCT` is present, duplicate argument values are eliminated before being passed to the aggregate function.

| Operator syntax                                   | Description                                                                    | NULL Behaviour                      |
|---------------------------------------------------|--------------------------------------------------------------------------------|-------------------------------------|
| `ANY_VALUE( [ ALL | DISTINCT ] attribute)`     | Returns one of the values of *attribute* from a set of records                 | NULL if the set of records is empty |
| `AVG( [ ALL | DISTINCT ] numeric)`             | Returns the average (arithmetic mean) of *numeric* for a set of records        | NULL if the set of records is empty |
| `COUNT(*)`                                         | Returns the count for a set of records                                         | Never NULL                          |
| `COUNT( [ ALL | DISTINCT ] value [, value ]*)` | Returns the count for a set of records where the specified values are not null | Never NULL                          |
| `MAX( [ ALL | DISTINCT ] value)`               | Returns the maximum of *value* for a set of records                            | NULL if the set of records is empty |
| `MIN( [ ALL | DISTINCT ] value)`               | Returns the minimum of *value* for a set of records                            | NULL if the set of records is empty |
| `MODE(value)`                                       | Returns the most frequent *value* for a set of records                         | NULL if the set of records is empty |
| `SUM( [ ALL | DISTINCT ] numeric)`             | Returns the sum of *numeric* for a set of records                              | NULL if the set of records is empty |

## Type conversion { #type-conversion }

It's recommended to specify explicit conversions rather than rely on implicit or automatic
conversions.

* SQL statements are easier to understand when you use explicit datatype conversion functions.
* Implicit conversion depends on the context in which it occurs and may not work the same way in every case. For example, implicit conversion from a datetime value to a VARCHAR value may return an unexpected format.

In particular, it's recommended to always `CAST` dynamic parameters. Queries using dynamic parameters may fail to plan or execute if the type of the dynamic parameter is ambiguous and can't be inferred from the context in which it occurs.

`CAST` is generally not required when working with literal values and attributes from external systems unless a type conversion needs to be forced (for example, VARCHAR to a TIMESTAMP).

Refer to [Data types in SQL with external entities](ansi-92-data-types.md) for more information about the available types and how they map to types in external systems.

| Operator syntax                      | Description                                 | Accepted Types                    | NULL Behaviour                |
|:-------------------------------------|:--------------------------------------------|-----------------------------------|-------------------------------|
| `DECIMAL_TO_TEXT(numeric)`             | Converts a numeric argument to VARCHAR      | NUMERIC<br/>DECIMAL               | NULL if *numeric* is NULL     |
| `INTEGER_TO_DECIMAL(integer)`          | Converts an integer argument to DECIMAL     | TINYINT<br/>SMALLINT<br/>INTEGER  | NULL if *integer* is NULL     |
| `LONG_INTEGER_TO_DECIMAL(longInteger)` | Converts a long integer argument to DECIMAL | BIGINT                            | NULL if *longInteger* is NULL |
| `TEXT_TO_DECIMAL(text)`                | Converts a text argument to DECIMAL         | CHAR<br/>VARCHAR                  | NULL if *text* is NULL        |
| `TEXT_TO_INTEGER(text)`                | Converts a text argument to INTEGER         | CHAR<br/>VARCHAR                  | NULL if *text* is NULL        |
| `TEXT_TO_LONG_INTEGER(text)`           | Converts a text argument to BIGINT          | CHAR<br/>VARCHAR                  | NULL if *text* is NULL        |

### CAST behaviour { ##cast-behaviour }

| Value Type                                  | Target Type                                                  | Notes                                                                                                                                        | Examples                                                                             |
|:--------------------------------------------|:-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| BOOLEAN                                     | CHAR<br/>VARCHAR                                             |                                                                                                                                              | TRUE -> 'TRUE'<br/>FALSE -> 'FALSE'                                                  |
| TINYINT<br/>SMALLINT<br/>INTEGER<br/>BIGINT | CHAR<br/>VARCHAR                                             |                                                                                                                                              | 123 -> '123'<br/>-123 -> '-123'                                                      |
| TINYINT<br/>SMALLINT<br/>INTEGER<br/>BIGINT | NUMERIC<br/>DECIMAL<br/>FLOAT<br/>REAL<br/>DOUBLE            |                                                                                                                                              | 123 -> 1.23E2                                                                        |
| TINYINT<br/>SMALLINT<br/>INTEGER<br/>BIGINT | TIMESTAMP                                                    | Milliseconds since 1970-01-01 00:00:00                                                                                                       | 123 -> 1970-01-01 00:00:00.123                                                       |
| DECIMAL<br/>NUMERIC                         | TINYINT<br/>SMALLINT<br/>INTEGER<br/>BIGINT                  | Truncates the value, removing the fractional component                                                                                       | 12.7 -> 12                                                                           |
| DECIMAL<br/>NUMERIC                         | FLOAT<br/>REAL<br/>DOUBLE                                    | Will result in a loss of precision                                                                                                           | 12.34 -> 1.234E1                                                                     |
| DECIMAL<br/>NUMERIC                         | TIMESTAMP                                                    | Milliseconds since 1970-01-01 00:00:00<br/>Returns an error if scale is not zero                                                             | 123 -> 1970-01-01 00:00:00.123                                                       |
| FLOAT<br/>REAL<br/>DOUBLE                   | DECIMAL<br/>NUMERIC                                          |                                                                                                                                              | 1.234E2 -> 123.4                                                                     |
| FLOAT<br/>REAL<br/>DOUBLE                   | TIMESTAMP                                                    | Milliseconds since 1970-01-01 00:00:00<br/>Fractional component is truncated                                                                 | 1.234E2 -> 1970-01-01 00:00:00.123                                                   |
| CHAR<br/>VARCHAR                            | BOOLEAN                                                      | Must be 'TRUE' or 'FALSE' (case insensitive) or returns an error                                                                             | 'TRUE' -> TRUE                                                                       |
| CHAR<br/>VARCHAR                            | TINYINT<br/>SMALLINT<br/>INTEGER<br/>BIGINT                  | Must be a valid integer or returns an error                                                                                                  | '123' -> 123<br/>'-123' -> -123                                                      |
| CHAR<br/>VARCHAR                            | DECIMAL<br/>NUMERIC<br/>FLOAT<br/>REAL<br/>DOUBLE            | Must be a valid number or returns an error                                                                                                   | '123.1234' -> 123.1234                                                               |
| CHAR<br/>VARCHAR                            | DATE                                                         | Must be a valid date in 'YYYY-MM-DD' format.<br/>Other formats may yield unexpected results or errors                                        | '2020-03-21' -> 2020-03-21                                                           |
| CHAR<br/>VARCHAR                            | TIME                                                         | Must be a valid time in 'HH24:MI' or 'HH24:MI:SS' format.<br/>Other formats may yield unexpected results or errors                           | '16:30' -> 16:30:00<br/>'07:20:01' -> 07:20:01                                       |
| CHAR<br/>VARCHAR                            | TIMESTAMP                                                    | Must be a valid date or datetime in 'YYYY-MM-DD' or 'YYYY-MM-DD HH24:MI:SS' format.<br/>Other formats may yield unexpected results or errors | '2020-03-21' -> 2020-03-21 00:00:00<br/>'2020-03-21 14:30:59' -> 2020-03-21 14:30:59 |
| BINARY<br/>VARBINARY                        | CHAR<br/>VARCHAR                                             | Returns base64 representation of the binary data                                                                                             | '01ab'                                                                               |
| DATE                                        | CHAR<br/>VARCHAR                                             | Returns date as a string in 'YYYY-MM-DD' format                                                                                              | 2020-03-21 -> '2020-03-21'                                                           |
| DATE                                        | TIMESTAMP                                                    | Converts a date to a timestamp with time 00:00:00                                                                                            | 2020-03-21 -> 2020-03-21 00:00:00                                                    |
| TIME                                        | CHAR<br/>VARCHAR                                             | Returns time as a string in 'HH24:MI:SS' format                                                                                              | 14:59:37 -> '14:59:37'                                                               |
| TIMESTAMP                                   | BIGINT<br/>DECIMAL<br/>NUMERIC<br/>FLOAT<br/>REAL<br/>DOUBLE | Milliseconds since 1970-01-01 00:00:00                                                                                                       | 1970-01-01 00:00:01 -> 1000                                                          |
| TIMESTAMP                                   | CHAR<br/>VARCHAR                                             | Returns timestamp as a string in 'YYYY-MM-DD HH24:MI:SS' format                                                                              | 1970-01-01 00:00:01 -> '1970-01-01 00:00:01'                                         |
| TIMESTAMP                                   | DATE                                                         | Discards the time component of the timestamp, returning the date component                                                                   | 1970-01-01 00:00:01 -> 1970-01-01                                                    |
| TIMESTAMP                                   | TIME                                                         | Discards the date component of the timestamp, returning the time component                                                                   | 2020-03-21 14:30:59 -> 14:30:59                                                      |

### Known issues

* CAST to TIMESTAMP is not supported for Oracle, however the [TO_TIMESTAMP](#datetime-functions) function can still be used.
