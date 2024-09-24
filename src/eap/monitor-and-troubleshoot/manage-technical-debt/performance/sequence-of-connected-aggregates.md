---
summary: Sequence of Aggregates that reference one another.
tags: 
guid: 8fa32beb-6cca-412c-a16d-5a33c658c6f9
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3525-213&t=ZHJybqzEUX6B7aIU-1
---

# Sequence of connected Aggregates

Sequence of Aggregates that reference one another.

## Impact

A sequence of Aggregates referencing one another usually leads to unnecessary data fetching. Considering that each Aggregate executes a request to the database, this results in unnecessary database communication overhead.

## Why is this happening?

Aggregates reference one another leading to multiple database queries, causing unnecessary data-fetching and latency. 

![An action flow diagram showing a sequence of two aggregates referencing one another.](images/odcs-connected-aggregates.png "Sequence of connected Aggregates")

## How to fix

Merge the sequence of Aggregates into a single Aggregate using a join to retrieve all the needed data.
