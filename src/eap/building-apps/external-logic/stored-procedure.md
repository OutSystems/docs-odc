---
summary: Learn how to extend your code using stored procedures in OutSystems Developer Cloud (ODC).
tags: stored procedures, sql database, custom code, database operations, c# integration
guid: b6caded7-82fc-4ce9-a8a2-6bd771c9e33b
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?m=auto&node-id=5851-7&t=SKufX46qUUZNk3AR-1
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
content-type:
  - conceptual
---

# Supporting stored procedure in ODC

Stored procedures allow you to execute a predefined set of commands as a single unit. You can encapsulate frequent complex operations making them both reusable and efficient.

In OutSystems Development Cloud (ODC) Studio, you can use stored procedures as custom code (C#) to integrate complex database operations directly into your apps. For example, if you frequently need to update multiple tables after a specific operation, you can use a stored procedure to automate this process efficiently.

![A flowchart describing the interaction between ODC Studio, custom C# code, and the SQL database.](images/stored-procedure.png "Interaction between ODC Studio, custom C# code, and the SQL database")

[The sample code snippet](https://github.com/OutSystems/OutSystems.ExternalLibraries.SDK-templates/blob/main/templates/storedProcedure/StoredProcedure.cs) guides you on how to use stored procedures with a private gateway in SQL database. 

To learn more about custom code, refer to [Extend your apps with external logic using custom code](intro.md)
