---
summary: Learn the best practices for creating your app's logic.
tags: 
outsystems_tools: 
guid: b3c30de3-477e-4f09-99d0-e4b2e711f917
locale: en-us
app_type: mobile apps, reactive web apps
content_type: 
audience: 
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?m=auto&node-id=6404-238&t=Rja8WKQPyVX2gJzO-1
---

# Best practices for logic

In OutSystems, your apps' logic is implemented through actions. Follow these recommendations to ensure efficiency and good performance.

## Avoid multiple server calls in a client action flow

Multiple server aggregates or server action requests inside client actions can lead to performance issues. Each call results in a separate server request, leading to numerous round trips between the client and server, which can increase latency. 

The following is an example of a client action flow with several sequenced server calls, which is not a good practice:

![A Client Action flow with multiple Run Server Action nodes.](images/multiple-server-requests-odcs.png "Multiple Server requests inside a Client Action")

### Recommendation

If you need to make multiple server calls in a client action, wrap all those server calls into a single server action and use that in the client action instead:

![A Client Action flow with a single Run Server Action node.](images/single-server-action-odcs.png "Single Server request inside a Client Action")

### Benefits

Having all required server logic in a single server action reduces the number of server requests, which improves your app's performance.

## Don't add aggregates or SQL queries inside a cycle

Aggregates or SQL queries inside a For Each cycle mean repeated database calls for each iteration. This results in significant performance degradation, particularly with large datasets or nested loops.

### Recommendations

When adding aggregates or SQL queries to an action flow, consider the following:

* Avoid executing aggregates or SQL queries inside a For Each cycle. 

* Instead of adding an aggregate or SQL query inside a cycle, add a more complex one that gets all the needed information before the cycle.

* If you have an aggregate to fetch the master entity before the cycle, followed by another aggregate inside the cycle to fetch the details, consider eliminating the inner aggregate. Add a join to the outer aggregate instead.

### Benefits

Keeping database calls outside the cycle prevents you from executing the same call repeatedly, thus improving performance.
