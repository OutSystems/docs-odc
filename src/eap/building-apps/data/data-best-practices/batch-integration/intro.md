---
summary: Batch integration in OutSystems Developer Cloud (ODC) processes large data volumes using sequential or parallel patterns with Timers and Events.
tags:
  - Batch Processing
  - Best Practices
  - Data
  - Data Synchronization
  - Events
  - Timers
guid: 78a00755-7f85-4488-aa40-0d24866bdc98
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
coverage-type:
  - understand
  - apply
  - evaluate
topic:
  - choose-batch-processing-approach
  - manage-large-data-volumes
  - track-batch-progress
audience:
  - Developer
  - Architect
  - Tech lead
outsystems-tools:
  - odc studio
isautopublish: true
---

# Batch integration

Some workloads need to move or transform a large volume of records: migrating data between systems, synchronizing an external system of record, or applying a change across many rows. Running this work synchronously, as part of an interactive request, blocks the user, risks request timeouts, and competes with live traffic for resources. Batch integration runs the work as an unattended job that processes records in chunks instead. A chunk is a set of records the job processes and commits together before moving on to the next set.

## When to use this pattern

Use this pattern when you need to move or transform a large volume of records outside an interactive request. It's a strong fit when one or more of the following also apply:

* The work is latency-tolerant and can run on a schedule or on demand, for example a nightly synchronization or a one-time migration.
* You want to process the data in chunks that you can resume or retry without reprocessing the records that already completed.
* You want to control the rate of work to stay within the throughput the source or target system can sustain.

## Choosing a processing approach

This article presents two approaches: sequential, where chunks run one after another, and parallel, where several run at the same time.

Start with sequential processing. It's simpler to build, test, and operate, and it handles most volumes within a reasonable window. Move to parallel processing only when sequential can't finish in the time you have and the work is safe to parallelize.

The two approaches trade off as follows:

| Dimension | Sequential | Parallel |
| :--- | :--- | :--- |
| Efficiency and throughput | Lower | Higher |
| Implementation and debugging | Easier | Harder |
| Resume after an interruption or timeout | Easier | Harder |
| Robustness | Higher | Lower |
| Best fit | Smaller or moderate datasets | Larger datasets |

The comparison favors sequential processing on every dimension except throughput, so treat throughput as the reason to move to parallel, not as the default choice. Parallel processing also has prerequisites that the table doesn't capture. Choose it only when all of the following hold:

* Sequential processing can't complete within the required window.
* The records split into independent chunks with no ordering or cross-record dependencies.
* The source and target systems can sustain the concurrent load without contention, deadlocks, or rate-limit rejections.

If any of these don't hold, sequential processing is the safer choice.

## Tracking integration progress {#tracking-integration-progress}

To manage your integration runs, regardless of what approach you choose you should consider setting up a data-model to support tracking progress.

Having your data model track which records or chunks are still pending and which are already done, allows not only to manage running the next chunk, it also makes it resumable at any point. Create an entity keyed to the records or add control columns to your existing schema, so each chunk processes the next set of pending records, and an interrupted run resumes without reprocessing records that already completed.

Here are common control columns for tracking resumability at the record level. Add any others your use case needs:

* **Status** (Text, or a [static entity](../../modeling/entity-static.md)): Tracks where a record or chunk is in the pipeline, for example `Pending`, `Processing`, `Completed`, or `Failed`. A run selects records by status and updates it as processing advances. A single boolean, such as **IsProcessed**, is enough for the simplest cases, but a status with distinct values separates records that failed and need a retry from those not yet started.
* **LastProcessedOn** (Date Time): Records when a record or chunk last processed or attempted the record. Use it to audit progress, apply a retry window, or identify records stuck in `Processing`.
* **RetryCount** (Integer): Counts how many times processing failed for a record or chunk. Use it to cap retries and move records that keep failing to a `Failed` state for separate handling.

For larger datasets, consider adding [indexes](../../modeling/entity.md#indexes) on the control columns each query filters on, particularly **Status**. The query that fetches the next set of pending records runs on every Timer run, so an index keeps it fast as the volume of data grows.

Because each chunk commits its own status, an interrupted run resumes by querying for the records still marked `Pending` or `Failed`, and doesn't repeat work that already completed.

## Implementing batch integration

To implement this pattern in OutSystems Developer Cloud (ODC) apps, make use of ODC building blocks such as Timers and Events.

An important concept regardless if you pick sequential or parallel, is controlling the time of execution of each chunk to fit the platform's limits. The amount of records in a chunk or **chunk size** is one of the main levers available to us to do this.

Both sequential and parallel approaches process records in chunks as an unattended job. They differ in whether the chunks run one after another or several at the same time. Refer to the approach you chose for a step-by-step implementation:

* [Sequential processing](sequential.md): chunks run one after another. Simpler to build, test, and resume, and the right default for most volumes.
* [Parallel processing](parallel.md): several chunks run at the same time. Higher throughput for large datasets, at the cost of more complexity.

## Related resources

* [Best practices for data management](../intro.md)
* [Data archiving best practice](../data-archiving.md)
* [Data purging best practice](../data-purging.md)
