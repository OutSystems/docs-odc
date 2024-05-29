---
summary: Commit changes to database before running aggregates to ensure the retrieval of newly inserted or updated records.
locale: en-us
guid: 4d56d131-ab84-401a-950f-ba81eebd716c
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?m=auto&node-id=5493-10&t=RAac4dB4CBOEAXd8-1
platform-version: odc
---

# Commit changes on the OutSystems database before running  aggregates

When you insert a record into an internal entity and then combine an aggregate in the same flow with an external entity, the aggregate doesn't return the inserted record because mashup queries are executed in different transactions. This issue does not occur with queries using external connections to combine different data sources. External connections have auto-commit enabled. Transactions are not supported on integrations with external systems.

![Diagram showing the flow of transactions and mashup queries in OutSystems.](images/intro-transactions-mashup.png "Diagram of transactions and mashup queries")

You should commit any changes to the OutSystems database before running mashup aggregates. This ensures the aggregate retrieves the inserted or updated record. This scenario applies to Server actions, Service Actions, Client Actions, Data Actions, runtime, and Timers. OutSystems recommends using the CommitTransaction Server Action when inserting or updating an OutSystems entity and then running a mashup query that includes the same entity.

![Screenshot of ODC Studio displaying an aggregate combining data from different sources.](images/data-mash-aggregate-odcs.png "Screenshot of ODC Studio with aggregate")

Another scenario where the problem occurs is If you create or update an entity action for an OutSystems entity followed by a Server action with an aggregate to combine data from an OutSystems entity and an external entity. The aggregate won't return the newly inserted or updated record from the previous action.

![Screenshot of ODC Studio showing a server action with an aggregate combining data from an OutSystems entity and an external entity.](images/data-mash-transaction-odcs.png "Screenshot of ODC Studio with server action")

If you run a create or update action for an OutSystems entity within a Client Action, and the aggregate is implemented at the screen level, the refresh aggregate returns the inserted or updated record. In this scenario, you do not need to use CommitTransaction.

![Screenshot of ODC Studio showing a client action where the aggregate is implemented at the screen level, not requiring a commit transaction.](images/data-mash-no-commit-odcs.png "Screenshot of ODC Studio without the need to commit transaction")

To learn more about isolation in transactions, refer to [dirty transactions](../../../../reference/isolation.md). 
