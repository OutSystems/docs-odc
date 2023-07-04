---
summary:
tags:
locale: en-us
guid: e71294ee-82b8-420f-b10f-057f1c4e3bcf
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# Zip

## Actions

Action | Description
---|---
AddFile | Adds a file to a Zip. The Action CommitChanges must be called after adding all the files.
CommitChanges | Commits any changes made to a Zip in memory. If AddFile is used, this Action must be called before GetZipBinary or GetFiles. 
CreateZip | Creates a memory representation of a Zip file and returns a handle that must be passed to the other Actions.
GetFiles | Returns a list of files and directories contained in a Zip file.
GetZipBinary | Returns the binary content of a Zip loaded in memory.
LoadZip | Loads a Zip file into memory and returns a handle that must be passed to other Actions.
