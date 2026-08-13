---
guid: b210750a-7591-40e8-8338-f25ab604c019
locale: en-us
summary: Upgrade ODC environments to PostgreSQL 16 for performance improvements and new features; review breaking changes to ensure application compatibility.
figma:
coverage-type:
  - apply
  - understand
topic:
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - Platform administrator
tags: postgresql upgrade, runtime database, performance improvement, breaking changes, database management
outsystems-tools:
  - odc portal
helpids: 30744
---
# Upgrade to PostgreSQL 16

ODC environments are supported by a Runtime Database that runs on a PostgreSQL database, currently running on a PostgreSQL 13 major version.

ODC is doing an operation to upgrade this major version to PostgreSQL 16.

This operation is beneficial as this latest PostgreSQL version contains several performance improvements and new features available.

<div class="info">

It's recommended that you re-schedule your updates to run as soon as possible so that you have time to properly test the upgrade. It's also recommended that you do the upgrade by stages, starting in your development stage and only after you successfully completed the upgrade there, move to the next stages.

</div>

## Impact

During this operation, you can have impacts on your environments normal operation, namely:

* A maximum duration of 1 hour for the whole update operation.

* A maximum downtime period of 30 minutes while the operation is running. During this time, the application runtime can have some disturbance.

* As in any database upgrade between major versions, there's the possibility and risk of existing breaking changes. These breaking changes are changes in behavior between the 2 major versions and affect the Runtime of your applications

In the next section, you can find the set of potential breaking changes that exist between version PostgreSQL 13 and PostgreSQL 16 (it includes the breaking changes from versions PostgreSQL 14 and PostegreSQL 15 as well).

These breaking changes are the ones that can happen at an OutSystems application level.

All these potential breaking changes should be reviewed internally in each infrastructure to guarantee that there are no behavioral differences at the runtime level for all the existing application.

## Breaking changes

### EXTRACT function return type change

Queries with EXTRACT return different values in PG16 and PG 13.

#### How to find

For example:

If you have a time stamp on your database with the value: `2024-06-01 00:00:01`

Running the following query:

```
SELECT EXTRACT(EPOCH FROM {Entity1}.[Timestamp]) / 3600 AS hours_since_epoch

FROM {Entity1}
```

The returned value for PG13 is different in the number of decimals, `477000.000277778` (9 decimals), from the result in PG16 `477000.000277777778` (12 decimals) when executed in PG16.

#### How to fix

T keep the PG13 behavior in PG16, the adjust the previous query to explicitly cast to the same data type used in PG13 (numeric) or PG16 (double precision), by changing the query to one of the following:

* To match PG13 behavior:

```
SELECT EXTRACT(EPOCH FROM {TimestampEntity}.[Timestamp])::double precision / 3600 AS hours_since_epoch

FROM {TimestampEntity}
```

* To match PG16 behavior:

```
SELECT EXTRACT(EPOCH FROM {TimestampEntity}.[Timestamp])::numeric / 3600 AS hours_since_epoch

FROM {TimestampEntity}

```

### Statistical functions NaN handling

PG16 handles NaN differently from PG13.

#### How to find

For example, if you have an entity with a decimal column with 1 record of value NaN, inserted through a SQL node:

```
TRUNCATE {DecimalEntity};
INSERT INTO {DecimalEntity} ([Decimal]) VALUES ('NaN);

```

If we run the following query:

```
SELECT var_samp({DecimalEntity}.[Decimal]::numeric)::text
FROM {DecimalEntity};
```

In PG13 the result is `NaN` but on PG16 the result is `NULL`

#### How to fix

Use the COALESCE function on your query to output NaN if necessary.

Keep in mind that it shouldn't be used to handle the NULL values as, these functions start returning an empty value.

### Regex - `\\D and \\W shorthands now match newlines in regular expression newline-sensitive mode`

Regular Expression engine handles the "Non-Word" character class (\W) when combined with the newline flag (n) differently. This means that:

* In PostgreSQL 13 the pattern \W identified symbols and punctuation but ignores the newline character (\n) in this specific context. The same happens to \D on numeric values.

* In PostgreSQL 16 the pattern \W is strictly interpreted. It identifies the newline character (\n) as a "Non-Word" character and selects it for replacement. The same happens to \D on numeric values.

#### How to find

For example, if you have an address in the format:

```
my street name, 100
myCity

```

and you want to transform it to:

```
my-street-name--100
myCity
```

Until now, you need your SQL to execute:

```
INSERT INTO {yourtable} ([Scenario], [Original], [Processed])
VALUES 
    (
        'TEST', 
        'my street name, 100' || chr(10) || 'myCity', 
        regexp_replace(
            'my street name, 100' || chr(10) || 'myCity','\W', '-','gn'
        )
    );

```

In PostgresSQL 16 the outcome will be no longer correct as it transforms it to:

```
my-street-name--100-myCity
```

The example above is also valid for `\D` operator.

#### How to fix

Instead of using just `\D` and `\W`, use `[^\d\n]` or `[^\w\n]`, that way you are explicitly excluding the new line from the replacement.

Using the same previous example:

```
INSERT INTO {yourtable} ([Scenario], [Original], [Processed])
VALUES 
    (
        'TEST', 
        'my street name, 100' || chr(10) || 'myCity', 
        regexp_replace(
            'my street name, 100' || chr(10) || 'myCity','[^\w\n]', '-','gn'
        )
    );

```

### Regex - back-reference behavior change

Regular Expression engine handles Back-references (\1, \2) when the original capture group contains PostgreSQL-specific boundary constraints (like \y for word boundary or \M for end-of-word) differently. This means that:

* In PostgreSQL 13 the pattern \1 was context-aware. It matched the captured text AND implicitly respected the boundary constraints defined in the original group.

* In PostgreSQL 16 the pattern \1 is strictly interpreted as a literal string copy. It copies the text captured in Group 1 but ignores the original boundary constraints, leading to incorrect partial matches.

#### How to find

For example, you have a validation for currency:

```
INSERT INTO {yourTable} ([Scenario], [Original], [Processed])
VALUES 
    (
        'TEST: Currency (\y)', 
        '$5 $50', 
        -- Expectation: $5 is distinct from $50. No match.
        regexp_replace('$5 $50', '(\$\d+\y) \1', '[ERROR]', 'g')
    );
```

In PostgreSQL 16 the outcome is different and because it ignores the boundary constraints results in an error.

The above example is also valid for \M scenarios.

#### How to fix

You need to modify the Regex pattern to explicitly re-state the constraint immediately after the back-reference.

For example:

* For \y: Change \1 to \1\y.

* For \M: Change \1 to \1\M.

So in the example above you need to fix your query to have:

```
INSERT INTO {yourTable} ([Scenario], [Original], [Processed])
VALUES 
    (
        'TEST: Currency (\y)', 
        '$5 $50', 
        -- Expectation: $5 is distinct from $50. No match.
        regexp_replace('$5 $50', '(\$\d+\y) \1\y', '[ERROR]', 'g')
    );
```

### Regex - `\w disallowed as range start/end in character classes`

There is a critical syntax compliance issue in how the Regular Expression engine handles Shorthand Character Classes (like \w, \d, \s) when used as the start or end of a Range inside a bracket expression `[0-\w]`.

In this scenario, the Regex pattern attempts to create a range from a single character to a "set" of characters (\w). This is mathematically invalid in standard POSIX regular expressions.

This was already an issue in PostgreSQL 13 and continues to be in PostgreSQL 16:

* In PostgreSQL 13 the environment enforces strict validation and rejects this pattern, causing the application to crash with `SQL Error 2201B`. Resulting, on a backend Runtime error: `Error executing ExecuteReaderAsync (2201B: invalid regular expression: invalid character range) with statement ...`

* In PostgreSQL 16 the strict enforcement continues. The query fails immediately with the same error

#### How to find

In the following example:

```
INSERT INTO {yourTable} ([Scenario], [Original], [Processed])
VALUES 
    (
        'TEST : Invalid Range End', 
        'Testing_123', 
        -- Attempting to create a range from '0' to '\w'
        -- This causes SQL Error 2201B in PG13
        regexp_replace('Testing_123', '[0-\w]', 'X', 'g')
    );

```

The execution fails with the previously mentioned error for both PostgreSQL versions.

#### How to fix

To fix this, remove the hyphen or move it to a position where it's treated as a literal character.

Example:

```
INSERT INTO {yourTable} ([Cenario], [Original], [Processado])
VALUES 
    (
        'Universal Fix: Union Logic', 
        'Testing_123', 
        -- FIX: Remove the hyphen. 
        -- Logic: Match '0' OR 'any Word Character'.
        regexp_replace('Testing_123', '[0\w]', 'X', 'g')
    ),
    (
        'Universal Fix: Literal Hyphen', 
        'Testing-123', 
        -- FIX: Move hyphen to the end to match it literally.
        -- Logic: Match 'Word Characters' OR 'z' OR 'Hyphen'.
        regexp_replace('Testing-123', '[\wz-]', 'X', 'g')
    );

```

Both methods solve this regex issue for both versions.
