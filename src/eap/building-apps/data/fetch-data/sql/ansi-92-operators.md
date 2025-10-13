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
| `value1 = value2`                  | Whether _value1_ is equal to _value2_                                                                                                              | NULL if any operand is NULL                                 |
| `value1 <> value2`                 | Whether _value1_ is not equal to _value2_                                                                                                          | NULL if any operand is NULL                                 |
| `value1 > value2`                 | Whether _value1_ is greater than _value2_                                                                                                          | NULL if any operand is NULL                                 |
| `value1 >= value2`                 | Whether _value1_ is greater than or equal to _value2_                                                                                              | NULL if any operand is NULL                                 |
| `value1 < value2`                 | Whether _value1_ is less than _value2_                                                                                                             | NULL if any operand is NULL                                 |
| `value1 <= value2`                 | Whether _value1_ is less than or equal to _value2_                                                                                                 | NULL if any operand is NULL                                 |
| `value IS NULL`                   | Whether _value_ is null                                                                                                                            | TRUE if _value_ is NULL                                     |
| `value IS NOT NULL`                | Whether _value_ is not null                                                                                                                        | FALSE if _value_ is NULL                                    |
| `string1 LIKE string2`             | Whether _string1_ matches pattern _string2_<br/>The pattern may contain the `%` (zero or more characters) and `_` (one character) wildcards        | NULL if any operand is NULL                                 |
| `string1 NOT LIKE string2`         | Whether _string1_ does not match pattern _string2_<br/>The pattern may contain the `%` (zero or more characters) and `_` (one character) wildcards | NULL if any operand is NULL                                 |
| `value1 IN (value [, value]*)`    | Whether _value1_ is equal to a value in a list                                                                                                      | NULL if _value1_ is NULL or if the list only contains NULLs |
| `value1 NOT IN (value [, value]*)` | Whether _value1_ is not equal to every value in a list                                                                                              | NULL if _value1_ is NULL or if the list only contains NULLs |
| `value IN (sub-query)`            | Whether _value_ is equal to a row returned by _sub-query_                                                                                          | NULL if _value_ is NULL                                     |
| `value NOT IN (sub-query)`         | Whether _value_ is not equal to every row returned by _sub-query_                                                                                  | NULL if _value_ is NULL                                     |
| `EXISTS (sub-query)`               | Whether _sub-query_ returns at least one row                                                                                                       | Never NULL                                                  |
| `UNIQUE (sub-query)`               | Whether the rows returned by _sub-query_ are unique (ignoring null values)                                                                         | Never NULL                                                  |

### Known issues

* Operators which accept subqueries (such as `EXISTS`) are currently not supported in mashup queries.

## Logical operators

| Operator syntax       | Description                                      | Null Behaviour              |
|:----------------------|:-------------------------------------------------|-----------------------------|
| `boolean1 OR boolean2`  | Whether _boolean1_ is TRUE or _boolean2_ is TRUE | NULL if any operand is NULL |
| `boolean1 AND boolean2` | Whether _boolean1_ and _boolean2_ are both TRUE  | NULL if any operand is NULL |
| `NOT boolean`           | Whether _boolean_ is not TRUE                    | NULL if _boolean_ is NULL   |
| `boolean IS FALSE`      | Whether _boolean_ is FALSE                       | FALSE if _boolean_ is NULL  |
| `boolean IS NOT FALSE`  | Whether _boolean_ is not FALSE                   | TRUE if _boolean_ is NULL   |
| `boolean IS TRUE`      | Whether _boolean_ is TRUE                        | FALSE if _boolean_ is NULL  |
| `boolean IS NOT TRUE`  | Whether _boolean_ is not TRUE                    | TRUE if _boolean_ is NULL   |

## Arithmetic operators and functions { #arithmetic-operators-and-functions }

| Operator syntax                 | Description                                                                                          | NULL Behaviour              |
|---------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------|
| `+ numeric`                      | Returns _numeric_                                                                                    | NULL if _numeric_ is NULL   |
| `- numeric`                       | Returns negative _numeric_                                                                           | NULL if _numeric_ is NULL   |
| `numeric1 + numeric2`            | Returns _numeric1_ plus _numeric2_                                                                   | NULL if any operand is NULL |
| `numeric1 - numeric2`             | Returns _numeric1_ minus _numeric2_                                                                  | NULL if any operand is NULL |
| `numeric1 \* numeric2`            | Returns _numeric1_ multiplied by _numeric2_                                                          | NULL if any operand is NULL |
| `numeric1 / numeric2`            | Returns _numeric1_ divided by _numeric2_                                                             | NULL if any operand is NULL |
| `MOD(numeric1, numeric2)`        | Returns the remainder after _numeric1_ is divided by _numeric2_                                      | NULL if any operand is NULL |
| `POWER(numeric1, numeric2)`       | Returns _numeric1_ raised to the power of _numeric2_                                                 | NULL if any operand is NULL |
| `ABS(numeric)`                    | Returns the absolute value of _numeric_                                                              | NULL if _numeric_ is NULL   |
| `SQRT(numeric)`                   | Returns the square root of _numeric_                                                                 | NULL if _numeric_ is NULL   |
| `FLOOR(numeric)`                 | Rounds _numeric_ down, returning the largest integer that is less than or equal to _numeric_         | NULL if _numeric_ is NULL   |
| `ROUND(numeric1 [, numeric2])`    | Rounds _numeric1_ to optionally _numeric2_ (if not specified 0) places right to the decimal point    | NULL if any operand is NULL |
| `TRUNCATE(numeric1 [, numeric2])` | Truncates _numeric1_ to optionally _numeric2_ (if not specified 0) places right to the decimal point | NULL if any operand is NULL |

### Known issues

* Mashup queries may return an error when MOD encounters a NULL divisor.
* Mashup queries may return an error when ABS, ROUND, or TRUNCATE encounter a NULL value.
* In MySQL, the `MOD` built-in function with 0 as the dividend returns NULL without an exception.

## Character string operators and functions { #character-string-operators-and-functions }

| Operator syntax                                                                  | Description                                                                                                                                                                                                   | NULL Behaviour              |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| `string || string`                                                               | Concatenates two character strings                                                                                                                                                                            | NULL if any operand is NULL |
| `CHAR_LENGTH(string)`                                                            | Returns the number of characters in a character string                                                                                                                                                        | NULL if _string_ is NULL    |
| `CHAR_INDEX(string, string [integer])`                                           | Same as `POSITION`                                                                                                                                                                                            | NULL if any operand is NULL |
| `CHARACTER_LENGTH(string)`                                                       | Same as `CHAR_LENGTH`                                                                                                                                                                                         | NULL if _string_ is NULL    |
| `UPPER(string)`                                                                  | Returns a character string converted to upper case                                                                                                                                                            | NULL if _string_ is NULL    |
| `LOWER(string)`                                                                  | Returns a character string converted to lower case                                                                                                                                                            | NULL if _string_ is NULL    |
| `POSITION(string1 IN string2)`                                                   | Returns the position (1 - N) of the first occurrence of _string1_ in _string2_                                                                                                                                | NULL if any operand is NULL |
| `POSITION(string1 IN string2 FROM integer)`                                      | Returns the position (1 - N) of the first occurrence of _string1_ in _string2_ starting at a given point                                                                                                      | NULL if any operand is NULL |
| `TRIM( { BOTH | LEADING | TRAILING } string1 FROM string2)`                      | Removes the longest string containing only the characters in _string1_ from the start/end/both ends of _string1_                                                                          | NULL if any operand is NULL |
| `SUBSTRING(string FROM integer)`                                                 | Returns a substring of a character string starting at a given point                                                                                                                                           | NULL if any operand is NULL |
| `SUBSTRING(string FROM integer FOR integer)`                                     | Returns a substring of a character string starting at a given point with a given length                                                                                                                       | NULL if any operand is NULL |
| `expression COLLATE collationId`                                                 | Overrides the default collation of the _expression_ result with the specified _collationId_.<br/>_collationId_ must be a valid reference to a collation in the database that produced the _expression_ result | NULL if any operand is NULL |

### Known issues

* `COLLATE` is currently not supported in mashup queries.
* In MySQL, the `SUBSTRING` built-in function with 0 as the starting position returns an empty string.
* In MySQL, the `POSITION` built-in function with 0 or negative `FROM` returns 0.

## Date/time functions { #datetime-functions }

| Operator syntax                               | Description                                                                                                                                   | NULL Behaviour                             |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| `CURRENT_TIME`                                | Returns the current time in the server time zone, in a value of datatype TIMESTAMP WITH TIME ZONE                                             | Never NULL                                 |
| `CURRENT_DATE`                                | Returns the current date in the server time zone, in a value of datatype DATE                                                                 | Never NULL                                 |
| `CURRENT_TIMESTAMP`                           | Returns the current date and time in the server time zone, in a value of datatype TIMESTAMP WITH TIME ZONE                                    | Never NULL                                 |
| `EXTRACT(timeUnit FROM datetime)`             | Extracts and returns the value of a specified datetime field from a datetime value expression                                                 | NULL if _datetime_ is NULL                 |
| `MONTH(datetime)`                             | Equivalent to `EXTRACT(MONTH FROM datetime)`. Returns an integer between 1 and 12                                                             | NULL if _datetime_ is NULL                 |
| `WEEK(datetime)`                              | Equivalent to `EXTRACT(WEEK FROM datetime)`. Returns an integer between 1 and 53                                                              | NULL if _datetime_ is NULL                 |
| `DAYOFYEAR(datetime)`                         | Equivalent to `EXTRACT(DOY FROM datetime)`. Returns an integer between 1 and 366                                                              | NULL if _datetime_ is NULL                 |
| `DAYOFMONTH(datetime)`                        | Equivalent to `EXTRACT(DAY FROM datetime)`. Returns an integer between 1 and 31                                                               | NULL if _datetime_ is NULL                 |
| `DAYOFWEEK(datetime)`                         | Equivalent to `EXTRACT(DOW FROM datetime)`. Returns an integer between 1 and 7                                                                | NULL if _datetime_ is NULL                 |
| `HOUR(datetime)`                              | Equivalent to `EXTRACT(HOUR FROM datetime)`. Returns an integer between 0 and 23                                                              | NULL if _datetime_ is NULL                 |
| `MINUTE(datetime)`                            | Equivalent to `EXTRACT(MINUTE FROM datetime)`. Returns an integer between 0 and 59                                                            | NULL if _datetime_ is NULL                 |
| `SECOND(datetime)`                            | Equivalent to `EXTRACT(SECOND FROM datetime)`. Returns an integer between 0 and 59                                                            | NULL if _datetime_ is NULL                 |
| `TIMESTAMPADD(timeUnit, integer, datetime)`   | Returns _datetime_ with an interval of (signed) _integer_ *timeUnit*s added.<br/>Equivalent to `datetime + INTERVAL (integer) timeUnit`       | NULL if _integer_ or _datetime_ is NULL    |
| `TIMESTAMPDIFF(timeUnit, datetime1, datetime2)` | Returns the (signed) number of _timeUnit_ intervals between _datetime1_ and _datetime2_.<br/>Equivalent to `(datetime2 - datetime1) timeUnit` | NULL if _datetime1_ or _datetime2_ is NULL |
| `FORMAT_DATE(date, format)`                   | Converts a _date_ into a string using the given format, see [Date/Time Formatting](#datetime-formatting)                                      | NULL if any operand is NULL                |
| `FORMAT_TIMESTAMP(timestamp, format)`         | Converts a _datetime_ into a string using the given _format_, see [Date/Time Formatting](#datetime-formatting)                                | NULL if any operand is NULL                |
| `TO_DATE(string, format)`                     | Converts a _string_ into a date using the specified _format_, see [Date/Time Formatting](#datetime-formatting)                                | NULL if any operand is NULL                |
| `TO_TIMESTAMP(string, format)`                | Converts a _string_ into a timestamp using the specified _format_, see [Date/Time Formatting](#datetime-formatting)                           | NULL if any operand is NULL                |

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

### Known issues

* `TIMESTAMPADD` and `TIMESTAMPDIFF` will return an error if used with `CURRENT_DATE` or `CURRENT_TIMESTAMP`. The same issue also occurs with the `+ INTERVAL` and `datetime2 - datetime1`syntax.
* In MySQL, the `WEEK` built-in function returns the week number for a given date, a number from 0 to 53.
* In MySQL, the `TO_TIMESTAMP` and `TO_TIMESTAMP` built-in functions can't convert strings that don't represent a valid date. They only accept valid date formats with year, month, and day.

## Conditional functions and operators { #conditional-functions }

| Operator syntax                                                                                                                     | Description                                                                                                                                                                                                                              | NULL Behaviour                                                                                                                    |
|:------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| `CASE value`<br/>`WHEN value1 [, value11 ]* THEN result1`<br/>`[ WHEN valueN [, valueN1 ]* THEN resultN ]*`<br/>`[ ELSE resultZ ]`<br/> `END` | This is a simple CASE expression.<br/>If _value_ is equal to any of the values in a given WHEN then the result from the associated THEN is returned.<br/>If no matches are found and ELSE is specified, the result from ELSE is returned | NULL if no matches are found and ELSE is omitted.<br/>WHEN NULL will never match due to the null behaviour of the equals operator |
| `CASE`<br/>`WHEN condition1 THEN result1`<br/>`[ WHEN conditionN THEN resultN ]*`<br/>`[ ELSE resultZ ]`<br/>`END`                            | This is a searched CASE expression.<br/>If the condition in a given WHEN is TRUE then the result from the associated THEN is returned.<br/>If none of the conditions are TRUE and ELSE is specified, the result from ELSE is returned    | NULL if no conditions are TRUE and ELSE is omitted.<br/>WHEN NULL will never match since NULL is neither TRUE nor FALSE           |
| `NULLIF(value1, value2)`                                                                                                              | Returns NULL if _value1_ is equal to _value2_, otherwise returns _value1_                                                                                                                                                                   | NULL if _value1_ is NULL or _value1_ matches _value2_                                                                             |
| `NULL_OR_VALUE(value1 , value2, value3)`                                                                                              | Returns NULL if _value1_ or _value2_ is NULL, otherwise returns _value3_                                                                                                                                                                 | NULL if any operand is NULL                                                                                                       |
| `COALESCE(value, value [, value ]*)`                                                                                                  | Returns the first value in the sequence which IS NOT NULL                                                                                                                                                                                | NULL if all operands are NULL                                                                                                     |

### Known issues

* Mashup queries may return an error when using NULLIF, consider using `CASE value1 WHEN value2 THEN NULL ELSE value1` instead.

## Aggregate functions { #aggregate-functions }

Syntax:

```sql
agg ( * ) [ FILTER (WHERE condition) ]

agg ( [ ALL | DISTINCT ] value [, value ]* ) [ FILTER ( WHERE condition ) ] 
```

Where _agg_ is one of the operators in the following table.

If `FILTER` is present, the aggregate function only considers rows for which _condition_ evaluates to TRUE.

If `DISTINCT` is present, duplicate argument values are eliminated before being passed to the aggregate function.

| Operator syntax                          | Description                                            | NULL Behaviour                      |
|------------------------------------------|--------------------------------------------------------|-------------------------------------|
| `ANY_VALUE( [ ALL | DISTINCT ] attribute)`                           | Returns one of the values of _attribute_ from a set of records                 | NULL if the set of records is empty |
| `AVG( [ ALL | DISTINCT ] numeric)`                             | Returns the average (arithmetic mean) of _numeric_ for a set of records        | NULL if the set of records is empty |
| `COUNT(*)`                               | Returns the count for a set of records                 | Never NULL                          |
| `COUNT( [ ALL | DISTINCT ] value [, value ]*)`                    | Returns the count for a set of records where the specified values are not null | Never NULL                          |
| `MAX( [ ALL | DISTINCT ] value)`                                | Returns the maximum of _value_ for a set of records                            | NULL if the set of records is empty |
| `MIN( [ ALL | DISTINCT ] value)`                                | Returns the minimum of _value_ for a set of records                            | NULL if the set of records is empty |
| `MODE(value)`                            | Returns the most frequent _value_ for a set of records | NULL if the set of records is empty |
| `SUM( [ ALL | DISTINCT ] numeric)`                              | Returns the sum of _numeric_ for a set of records                              | NULL if the set of records is empty |

### Known issues

* `COUNT DISTINCT` isn't supported with attributes of type `BOOLEAN` for Salesforce.

## Window functions { #window-functions }

Syntax:

```sql
windowFunction OVER { windowName | ( windowDefinition ) }

windowDefinition:
        [ existingWindowName ]
        [ PARTITION BY expression [, expression ]* ]
        [ ORDER BY orderItem [, orderItem ]* ]
        [ { RANGE | ROWS } BETWEEN windowBound AND windowBound ]

windowBound:
        CURRENT ROW
    |   { UNBOUNDED | value } { PRECEDING | FOLLOWING }
```

| Operator syntax                       | Description                                                                                                                                                          | Requires ORDER BY |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `COUNT(attribute [, attribute]*)`     | Returns number of records in window for which the attributes are not null                                                                                            | No                |
| `COUNT(*)`                            | Returns number of records in window                                                                                                                                  | No                |
| `AVG(numeric)`                        | Returns arithmetic mean of numeric for the records in window                                                                                                         | No                |
| `SUM(numeric)`                        | Returns sum of numeric for the records in window                                                                                                                     | No                |
| `MAX(attribute)`                      | Returns maximum value of attribute for the records in window                                                                                                         | No                |
| `MIN(attribute)`                      | Returns minimum value of attribute for the records in window                                                                                                         | No                |
| `RANK()`                              | Returns rank of the current record based on ORDER BY attribute with gaps                                                                                             | Yes               |
| `DENSE_RANK()`                        | Returns rank of the current record based on ORDER BY attribute without gaps                                                                                          | Yes               |
| `ROW_NUMBER()`                        | Returns position of the current record within it's partition counting from 1                                                                                         | No                |
| `FIRST_VALUE(attribute)`              | Returns attribute from the first record in the window frame                                                                                                          | No                |
| `LAST_VALUE(attribute)`               | Returns attribute from the last record in the window frame                                                                                                           | No                |
| `LEAD(attribute [, offset, default])` | Returns attribute from offset records after the current record, or default if there is no such record. When not specified, offset defaults to 1 and default is NULL  | Yes               |
| `LAG(attribute [, offset, default])`  | Returns attribute from offset records before the current record, or default if there is no such record. When not specified, offset defaults to 1 and default is NULL | Yes               |
| `NTH_VALUE(attribute, n)`             | Returns attribute at the nth record of the window frame                                                                                                              | No                |
| `NTILE(value)`                        | Returns an integer ranging from 1 to value, dividing the partition as equally as possible                                                                            | Yes               |

### Known issues

* `ROW_NUMBER` requires `ORDER BY` when used with Microsoft SQL Server or Oracle.
* `NTH_VALUE` isn't supported with Microsoft SQL Server.
* `NTILE` can't be used with a window which has a `RANGE` or `ROWS` clause with Microsoft SQL Server.
* Window functions aren't supported with Salesforce and SAP OData.
* MySQL doesn't support `PARTITION BY <expression>` when `<expression>` is a constant.

## Type conversion functions { #type-conversion }

It's recommended to specify explicit conversions rather than rely on implicit or automatic conversions.

* SQL statements are easier to understand when you use explicit datatype conversion functions.
* Implicit conversion depends on the context in which it occurs and may not work the same way in every case. For example, implicit conversion from a datetime value to a VARCHAR value may return an unexpected format.

In particular, it's recommended to always `CAST` dynamic parameters. Queries using dynamic parameters may fail to plan or execute if the type of the dynamic parameter is ambiguous and can't be inferred from the context in which it occurs.

`CAST` is generally not required when working with literal values and attributes from external systems unless a type conversion needs to be forced (for example, VARCHAR to a TIMESTAMP).

Refer to [Data types in SQL with external entities](ansi-92-data-types.md) for more information about the available types and how they map to types in external systems.

| Operator syntax                        | Description                                 | Accepted Types                    | NULL Behaviour                |
|----------------------------------------|---------------------------------------------|-----------------------------------|-------------------------------|
| `DECIMAL_TO_TEXT(numeric)`             | Converts a numeric argument to VARCHAR      | NUMERIC<br/>DECIMAL               | NULL if _numeric_ is NULL     |
| `INTEGER_TO_DECIMAL(integer)`          | Converts an integer argument to DECIMAL     | TINYINT<br/>SMALLINT<br/>INTEGER  | NULL if _integer_ is NULL     |
| `LONG_INTEGER_TO_DECIMAL(longInteger)` | Converts a long integer argument to DECIMAL | BIGINT                            | NULL if _longInteger_ is NULL |
| `TEXT_TO_DECIMAL(text)`                | Converts a text argument to DECIMAL         | CHAR<br/>VARCHAR                  | NULL if _text_ is NULL        |
| `TEXT_TO_INTEGER(text)`                | Converts a text argument to INTEGER         | CHAR<br/>VARCHAR                  | NULL if _text_ is NULL        |
| `TEXT_TO_LONG_INTEGER(text)`           | Converts a text argument to BIGINT          | CHAR<br/>VARCHAR                  | NULL if _text_ is NULL        |

### CAST behaviour { ##cast-behaviour }

| Value Type                                                         | Target Type                                                  | Notes                                                                                                                                        | Examples                                                                                      |
|--------------------------------------------------------------------|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| BOOLEAN                                                            | CHAR<br/>VARCHAR                                             |                                                                                                                                              | TRUE -> 'TRUE'<br/>FALSE -> 'FALSE'                                                           |
| TINYINT<br/>SMALLINT<br/>INTEGER<br/>BIGINT<br/>NUMERIC<br/>DECIMAL<br/>DOUBLE<br/>FLOAT<br/>REAL | BOOLEAN                                                      | Returns `FALSE` if the value is `0`, otherwise returns `TRUE`                                                                                | 1 -> TRUE<br/>0 -> FALSE<br/>-1 -> TRUE<br/>-0.001 -> TRUE<br/>0.001 -> TRUE<br/>1.234E2 -> TRUE |
| TINYINT<br/>SMALLINT<br/>INTEGER<br/>BIGINT                        | CHAR<br/>VARCHAR                                             |                                                                                                                                              | 123 -> '123'<br/>-123 -> '-123'                                                               |
| TINYINT<br/>SMALLINT<br/>INTEGER<br/>BIGINT                        | NUMERIC<br/>DECIMAL<br/>FLOAT<br/>REAL<br/>DOUBLE            |                                                                                                                                              | 123 -> 1.23E2                                                                                 |
| TINYINT<br/>SMALLINT<br/>INTEGER<br/>BIGINT                        | TIMESTAMP                                                    | Milliseconds since 1970-01-01 00:00:00                                                                                                       | 123 -> 1970-01-01 00:00:00.123                                                                |
| DECIMAL<br/>NUMERIC                                                | TINYINT<br/>SMALLINT<br/>INTEGER<br/>BIGINT                  | Truncates the value, removing the fractional component                                                                                       | 12.7 -> 12                                                                                    |
| DECIMAL<br/>NUMERIC                                                | FLOAT<br/>REAL<br/>DOUBLE                                    | Will result in a loss of precision                                                                                                           | 12.34 -> 1.234E1                                                                              |
| DECIMAL<br/>NUMERIC                                                | TIMESTAMP                                                    | Milliseconds since 1970-01-01 00:00:00<br/>Returns an error if scale is not zero                                                             | 123 -> 1970-01-01 00:00:00.123                                                                |
| FLOAT<br/>REAL<br/>DOUBLE                                          | DECIMAL<br/>NUMERIC                                          |                                                                                                                                              | 1.234E2 -> 123.4                                                                              |
| FLOAT<br/>REAL<br/>DOUBLE                                          | TIMESTAMP                                                    | Milliseconds since 1970-01-01 00:00:00<br/>Fractional component is truncated                                                                 | 1.234E2 -> 1970-01-01 00:00:00.123                                                            |
| CHAR<br/>VARCHAR                                                   | BOOLEAN                                                      | Must be 'TRUE' or 'FALSE' (case insensitive) or returns an error                                                                             | 'TRUE' -> TRUE                                                                                |
| CHAR<br/>VARCHAR                                                   | TINYINT<br/>SMALLINT<br/>INTEGER<br/>BIGINT                  | Must be a valid integer or returns an error                                                                                                  | '123' -> 123<br/>'-123' -> -123                                                               |
| CHAR<br/>VARCHAR                                                   | DECIMAL<br/>NUMERIC<br/>FLOAT<br/>REAL<br/>DOUBLE            | Must be a valid number or returns an error                                                                                                   | '123.1234' -> 123.1234                                                                        |
| CHAR<br/>VARCHAR                                                   | DATE                                                         | Must be a valid date in 'YYYY-MM-DD' format.<br/>Other formats may yield unexpected results or errors                                        | '2020-03-21' -> 2020-03-21                                                                    |
| CHAR<br/>VARCHAR                                                   | TIME                                                         | Must be a valid time in 'HH24:MI' or 'HH24:MI:SS' format.<br/>Other formats may yield unexpected results or errors                           | '16:30' -> 16:30:00<br/>'07:20:01' -> 07:20:01                                                |
| CHAR<br/>VARCHAR                                                   | TIMESTAMP                                                    | Must be a valid date or datetime in 'YYYY-MM-DD' or 'YYYY-MM-DD HH24:MI:SS' format.<br/>Other formats may yield unexpected results or errors | '2020-03-21' -> 2020-03-21 00:00:00<br/>'2020-03-21 14:30:59' -> 2020-03-21 14:30:59          |
| BINARY<br/>VARBINARY                                               | CHAR<br/>VARCHAR                                             | Returns base64 representation of the binary data                                                                                             | '01ab'                                                                                        |
| DATE                                                               | CHAR<br/>VARCHAR                                             | Returns date as a string in 'YYYY-MM-DD' format                                                                                              | 2020-03-21 -> '2020-03-21'                                                                    |
| DATE                                                               | TIMESTAMP                                                    | Converts a date to a timestamp with time 00:00:00                                                                                            | 2020-03-21 -> 2020-03-21 00:00:00                                                             |
| TIME                                                               | CHAR<br/>VARCHAR                                             | Returns time as a string in 'HH24:MI:SS' format                                                                                              | 14:59:37 -> '14:59:37'                                                                        |
| TIMESTAMP                                                          | BIGINT<br/>DECIMAL<br/>NUMERIC<br/>FLOAT<br/>REAL<br/>DOUBLE | Milliseconds since 1970-01-01 00:00:00                                                                                                       | 1970-01-01 00:00:01 -> 1000                                                                   |
| TIMESTAMP                                                          | CHAR<br/>VARCHAR                                             | Returns timestamp as a string in 'YYYY-MM-DD HH24:MI:SS' format                                                                              | 1970-01-01 00:00:01 -> '1970-01-01 00:00:01'                                                  |
| TIMESTAMP                                                          | DATE                                                         | Discards the time component of the timestamp, returning the date component                                                                   | 1970-01-01 00:00:01 -> 1970-01-01                                                             |
| TIMESTAMP                                                          | TIME                                                         | Discards the date component of the timestamp, returning the time component                                                                   | 2020-03-21 14:30:59 -> 14:30:59                                                               |

### Known issues

* Some character string operators / functions will return an error when the attribute collation is not compatible with the database default collation.

* When using the `CHAR_INDEX`, `LIKE`, and `POSITION` operators with PostgreSQL, the operands will be collated to the database default collation. This may lead to unexpected results when working with attributes which have a non-default collation.

* Mashup queries may return an error when either `UPPER` or `LOWER` encounter a `NULL` value.

* When working with dynamic parameters in MySQL, use the `CAST` function to ensure the correct data type is applied. Without an explicit cast, dynamic parameters may fall back to the default type based on their value, potentially causing unexpected behavior. If `CAST` is not used, dynamic parameters are resolved to the following types:
    * Boolean: returned as `BIGINT`
    * Integer: returned as `BIGINT`
    * Timestamp: returned as `VARCHAR`
    * Time: returned as `VARCHAR`
    * Date: returned as `VARCHAR`

* The `CAST` to `BOOLEAN` from `DOUBLE`, `FLOAT` and `REAL` is not supported by PostgreSQL. Trying to `CAST` one of these data types to `BOOLEAN` will result in an error similar to `cannot cast type [type] to boolean`.

* For Oracle databases the `CAST` to `BOOLEAN` from `VARCHAR`/`CHAR` will return an error when using `true` or `false` strings (regardless the case used). However, it will return `TRUE` when using string `1` and `FALSE` when using string `0`.
