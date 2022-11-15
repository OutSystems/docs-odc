---
summary: Differences in using SQL compared to OutSystems 11.  
tags:
locale: en-us
guid: db4685f5-477f-436a-b4cc-92af8e347c02
app_type: mobile apps, reactive web apps
---

# SQL queries compared to OutSystems 11

In OutSystems 11, you can choose to use SQL Server, Azure SQL Database, Oracle or DB2 as the database for your apps. In OutSystems Developer Cloud (ODC), your apps use Aurora PostgreSQL.

Where SQL Server and Azure SQL Database are relational database systems, Aurora PostgreSQL is an object-relational database. This means in ODC you can build SQL queries with complex data types and object inheritance.

In ODC you build SQL queries for your apps using the SQL logic element as in OutSystems 11. But because of the different underlying database technology when you build SQL queries there are some important syntax differences. The following table shows the main ones.

Topic | OutSystems 11 example (SQL Server or Azure SQL Database) | ODC equivalent (Aurora PostgreSQL)
---|---|---
Comparison of Time data type | `[…] WHERE {UseCase_Time}.[Time] > '11:01:41'` | `[…] WHERE {UseCase_Time}.[Time]::time > '11:01:41'`
Concatenate text string | `[…] WHERE {Org}.[Name] = 'First' + 'Last'` | `[…] WHERE {Org}.[Name] = 'First' \|\| 'Last'`
INSERT | `INSERT INTO {Product} ({Product}.[Name])`<br/>`VALUES ('abc')` | `INSERT INTO {Product}([Name])`<br/>`VALUES ('abc')`
ISNULL | `[…] WHERE`<br/>`ISNULL({Department}.[CompanyId])` | `WHERE {Department}.[CompanyId] IS NULL`
LIKE (Case and accent insensitive) | `[…] WHERE {Org}.[Name] LIKE`<br/>`'%asd%'` | `[…] WHERE`<br/>`caseaccent_normalize({Org}.[Name] collate "default") LIKE caseaccent_normalize('%asd%')`<br/><br/>See [this section](#case-and-accent) for further examples.
Limiting records | `SELECT {Organization}.* FROM {Organization} TOP 10` | `SELECT {Organization}.* FROM {Organization} LIMIT 10` 
Random records | `SELECT TOP 1`<br/>`* FROM table`<br/>`ORDER BY NEWID()` | `SELECT * FROM table_name`<br/>`ORDER BY RANDOM()`<br/>`LIMIT 1;` 
Selecting attributes | `SELECT * FROM {Organization}` | `SELECT {Organization}.* FROM {Organization}`
UPDATE | `UPDATE {Products}`<br/>`SET {Products}.[Name] = 'abc'`<br/>`WHERE {Products}.[Id]= 2` | `UPDATE {Products}`<br/>`SET [Name] = 'abc'`<br/>`WHERE {Products}.[Id] = 2`

 You can read more information on PostgreSQL syntax in the [official documentation](https://www.postgresql.org/docs/).

## Case and accent insensitive queries { #case-and-accent }

You need to pay attention to how you write case and accent insensitive SQL queries. Aurora PostgreSQL is a case and accent sensitive database. To allow case and accent insensitive text operations (CIAI), PostgreSQL introduces the concept of [non-deterministic collations](https://www.postgresql.org/docs/12/collation.html).

The non-deterministic collation in ODC is, by default, defined at the singular level and for all the columns that ODC creates. This means:

* The SQL database operators (=, <>, >, >=, <, <=) are CIAI and the default comparison in ODC.
* The pattern matching operators of LIKE, SIMILAR, and REGEX aren't supported through non-deterministic collations.

The **pattern matching operators aren't supported and result in runtime errors**. For example, you get an error like "DataBaseException Error in advanced query SQL1 (...) with nondeterministic collations, in which these operators are not supported."

**For pattern matching operators use the function caseaccent_normalize** directly in the SQL Node (AdvancedQuery), in each pattern matching operator.

Here is an example for LIKE:

    SELECT * from table
    WHERE caseaccent_normalize(col1 collate "default")
    LIKE caseaccent_normalize(col2 collate "default");

The `collate "default"` part is only needed when the pattern is applied to a column with non-deterministic collation, which is in all the text-based columns. You can skip `collate "default"` in something that uses literals like:

    SELECT * from table
        WHERE caseaccent_normalize(col1 collate "default")
        LIKE caseaccent_normalize('%something'); 

Here is an example for **regexp_replace**:

    SELECT regexp_replace(caseaccent_normalize(col1 collate "default"), '.stuff to replace.', '') FROM table;
