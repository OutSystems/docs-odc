---
summary: OutSystems Developer Cloud (ODC) automatically generates REST API documentation from method properties and descriptions upon app publication.
tags: api documentation, swagger, rest api, automatic documentation, integration
locale: en-us
guid: 08460e49-ec25-478c-abce-d4dc5d1abe2b
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3213%3A21228&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
content-type:
  - procedure
---

# Document an Exposed REST API

Adding documentation to your REST API is essential as it helps developers to integrate their applications with your system.

OutSystems facilitates documenting your REST API by automatically generating the documentation when you publish the app. The platform generates the documentation from the properties of the REST API, the REST API methods, and their parameters. Subsequent changes to the exposed REST API (for example, when endpoints or parameters and added or changed) are automatically updated in the generated documentation.

Do the following:

1. In ODC Studio, make sure that your REST API methods and their parameters have their "Description" property filled in. You can use [Markdown](http://daringfireball.net/projects/markdown/syntax) in the description to format the text.

1. Publish the app.

OutSystems publishes the documentation under the base URL of the REST API. To open it do the following:

1. In ODC Studio, right-click the tree element of your REST API.

1. Choose **Open Documentation**.

    ![Screenshot showing how to open REST API documentation in ODC Studio](images/rest-open-documentation-ss.png "Open REST API Documentation")


The resulting documentation is a standard swagger. You can see a [live example of a Contacts REST API here](https://expertsmobile.outsystems.com/ContactsAPI/rest/v1/).

![Screenshot of OutSystems REST API documentation interface with various HTTP method types for the Contacts API.](images/contacts-rest-swagger.png "Overview of REST API Documentation")

By expanding each of the endpoints, you'll be able to see details, like the request URL, parameters, examples, and responses:

![Detailed view of a PUT method in OutSystems REST API documentation showing request URL, parameters, and response structure.](images/contacts-rest-swagger-detail.png "Detailed REST API Documentation View")
