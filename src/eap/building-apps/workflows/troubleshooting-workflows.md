---
summary: Learn more about how to troublehsoot errors in your workflows
tags: 
guid: bf12c288-f7ad-4253-b6b7-bdf502c33e9b
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=5860-10
---

# Troubleshooting workflows

After you deploy a workflow in a specific environment, an instance of that  workflow can end up with an **Active with errors** status for one of the following reasons:

* **App-side error**

    * Error in a service action

* **Process-side error**

    * Service action in an error state

    * Activity timeout

    * Error in an expression

Any errors in a workflow can be viewed from the Portal on the **Instances** tab of the workflow detail. 

To investigate the error further, follow these steps:

1. Click the **Active with errors** instance.

    ![Screenshot of workflows instances with their statuses](images/error-instance-pl.png "Workflow instances with their statuses")

1. Select the erroneous workflow activity to display the error details. 

    ![Screenshot of error details for the erroneous workflow activity](images/error-detail-pl.png "error details for the erroneous workflow activity")

1. Fix the error.   

Additionally, for more information about the error, you can navigate to the related Trace, when available. 