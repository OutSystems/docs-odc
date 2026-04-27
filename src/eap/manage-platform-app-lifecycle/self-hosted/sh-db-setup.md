---
guid: 095d05c1-f9d5-49d4-b831-d78311fb4a14
locale: en-us
summary: Learn how to prepare and configure a PostgreSQL database for your self-hosted OutSystems Developer Cloud (ODC) stage before connecting it during installation.
figma:
coverage-type:
topic:
app_type: reactive web apps, mobile apps
platform-version: odc
audience:
  - Platform administrator
  - Architect
tags: postgresql configuration, self-hosted stages, database requirements, outsystems developer cloud, infrastructure setup
outsystems-tools:
  - self hosted console
helpids:
isautopublish: true
---
# Set up the database for self-hosted stages

Before setting up a self-hosted PostgreSQL database for OutSystems, ensure that your configuration meets the requirements described below. This database will host application data for a specific runtime stage and must be prepared before you start the [installation procedure](install-sh.md).

## Infrastructure

### Hardware requirements

The database instance must meet the following minimum hardware requirements:

* **vCPU:** 2 cores, depending on your expected application workload.
* **Memory:** 4 GB.
* **IOPS:** Auto-scaling or provisioned according to workload to ensure stable performance.

These values serve as a baseline and should be adjusted based on your organization’s performance and scaling needs.

### Storage

There are no fixed minimum storage requirements beyond what you estimate your apps data will need.
OutSystems Developer Cloud (ODC) doesn’t store platform metadata in your application database, so there’s no overhead beyond your apps’ data.

### Database version

Your database must run the version specified in the [system requirements](sh-install-reqs.md).
Database engine upgrades must only occur when the Development stage database is upgraded as well. Automatic engine upgrades aren’t supported.

### Required PostgreSQL extensions

The following PostgreSQL extensions must be supported and available for installation. The Self-hosted configurator installs them automatically, but you should ensure they remain enabled after setup.

Required extensions:

* `unaccent` — Removes accents and diacritical marks from text, improving full-text search matching and standardizing user input.
* `pg_trgm` — Enables trigram-based similarity searches, supporting faster and more flexible text comparisons and pattern matching.
* `btree_gin` — Provides B-tree–equivalent indexing classes that let GIN indexes handle typical B-tree operators, improving query efficiency on text fields.
* `uuid-ossp` — Generates universally unique identifiers (UUIDs) for primary keys and reference fields, ensuring global uniqueness across distributed systems.
* `vector` — Supports vector data types used in AI- or embedding-based searches, enabling efficient similarity operations for vectorized data.

## Configuration

### Dedicated cluster

Each database must be dedicated to a single ODC runtime stage and can’t be shared with other applications or services.
While you have full control over your application data, don’t modify the database schema or its underlying structure. Changing schema elements may cause application malfunction or data loss that OutSystems can’t recover or fix.

For this setup, you must use the `postgres` user for the database connection, so make the `postgres` user is active.

### Auto-scaling

If your PostgreSQL service supports auto-scaling or serverless options, ensure that the instance doesn’t scale down to zero.
ODC requires the database to remain available for ongoing platform operations.

### Timezone

To maintain consistent date and time handling across all ODC components, the database instance timezone must be set to **UTC**.

### Collation and character set

The database must be case-insensitive and use UTF-8 encoding.

* **Encoding:** UTF8
* **Collation:** en_US.utf8 or an equivalent case-insensitive UTF-8 collation
* **LC_COLLATE** and **LC_CTYPE:** Must support case-insensitive comparisons

### User permissions

Use a PostgreSQL admin user with permissions to manage and promote changes to the database cluster.
Don’t change the permissions of the OutSystems service user after setup.

**Password restrictions:** To ensure compatibility with ODC SQL generation, exclude the following characters from the database password:
`{ } , ; + % < > & $`

### Timeout configurations

Configure the following PostgreSQL parameters to ensure proper handling of long-running transactions:

```
statement_timeout = 7200000
idle_in_transaction_session_timeout = 7200000
```

Apply these configurations on the next database reboot.
