---
summary: Add documentation to your REST API to help developers to integrate their applications with your system.
tags: 
locale: en-us
guid: 08460e49-ec25-478c-abce-d4dc5d1abe2b
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3213%3A21228&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Document an Exposed REST API

Adding documentation to your REST API is essential as it helps developers to integrate their applications with your system.

OutSystems facilitates documenting your REST API by automatically generating the documentation when you publish the app. The platform generates the documentation from the properties of the REST API, the REST API methods, and their parameters.

Do the following:

1. In ODC Studio, make sure that your REST API methods and their parameters have their "Description" property filled in. You can use [Markdown](http://daringfireball.net/projects/markdown/syntax) in the description to format the text.

1. Publish the app.

OutSystems publishes the documentation under the base URL of the REST API. To open it do the following:

1. In ODC Studio, right-click the tree element of your REST API.

1. Choose **Open Documentation**.

    ![](images/ss-rest-open-documentation.png)
