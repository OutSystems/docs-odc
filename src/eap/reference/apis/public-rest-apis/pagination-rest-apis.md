---
summary: This article explains how to page through a list of resources retrieved in the API result.
tags: rest api, pagination, offset-limit, api requests, http get
guid: 9d2b8682-d5f4-440e-bd29-cf7f3922a7ab
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
outsystems-tools:
  - none
content-type:
  - conceptual
  - procedure
audience:
  - full stack developers
---

# Page through lists of resources

When a response from the REST API, such as `GET /users` includes many results, the results are paginated, and each page provides a subset of the total results.

ODC REST APIs adopts **offset-limit** pagination strategy using the following query parameters in the API request.

**offset**: The starting point or position of the first result returned. For example, if you want to retrieve 15 items from a resource and specify the _limit=5_, then you can retrieve the entire set of results in 3 successive requests by varying the _offset_ values as _offset=0_, _offset=5_, and _offset=10_.  It is a **zero-based index**, meaning an offset of 0 retrieves the first item. The default value is 0.

**limit**: The maximum number of results returned for a single request. This parameter can be considered the page size. If no limit is specified, the default value is 100. The allowed values are 1 to 100.

To fetch successive pages, you must adjust the offset parameter. The new offset is calculated by adding the previous offset and limit.

For example, in the following request the API retrieves information about 10 users starting from the 6th user.

```curl
   
    GET /users?limit=10&offset=5"

```

## Response structure

The API response consists of the requested resource items and the following pagination metadata for navigation:

- count: The number of results on the current page.

* limit: Maximum number of results returned for a request 

- offset: The offset for the current page of results.

* nextPageOffset: The offset for the next page of results. This is calculated as limit+offset. To move to the next page of results, this parameter is used as the offset for the next request.

- totalResults: The total number of results for the request.

* totalPages: The total number of pages for the result. This is calculated as totalResults/limit.

## Example

This example shows how to make a request to the users resource, limiting the results to 2 users per page. The total number of users in the list is 10, and the results of the first two pages are provided below:

```curl

    curl -X GET "https://ODC_PORTAL_DOMAIN/api/identity/v1/users?limit=2&offset=0"
       -H "Authorization: Bearer ACCESS_TOKEN"

```

Where 

ODC\_PORTAL\_DOMAIN is the domain of your Organization

ACCESS\_TOKEN - Access token generated using the client credentials

Here’s the first page displaying the first 2 users in the result

```json

    Response
    {
      "results": [
        {
          "key": "0413d4d6-6e1e-4b80-a464-ddc6b0464d68",
          "name": "example1",
          "email": "example1",
          "status": "Invited",
          "access": {
            "hasOrganizationRoles": true,
            "hasApplicationRoles": false
          },
          "lastLoginAt": null,
          "isActive": false,
          "photoUrl": null,
          "isEmailVerified": false,
          "isTermsAndConditionsAccepted": false
        },
        {
          "key": "096c6734-0b24-465e-8ec4-9a02512fc6ac",
          "name": "",
          "email": "example2",
          "status": "Inivited",
          "access": {
            "hasOrganizationRoles": true,
            "hasApplicationRoles": false
          },
          "lastLoginAt": null,
          "isActive": false,
          "photoUrl": null,
          "isEmailVerified": false,
          "isTermsAndConditionsAccepted": false
        }
      ],
      "page": {
        "count": 2,
        "limit": 2,
        "offset": 0,
        "nextPageOffset": 2,
        "totalResults": 10,
        "totalPages": 5
      }
    }

Here's the request to retrieve the next two users in the list.

```curl

    curl -X GET "https://ODC_PORTAL_DOMAIN/api/identity/v1/users?limit=2&offset=2"
       -H "Authorization: Bearer ACCESS_TOKEN"

```

Where 

ODC\_PORTAL\_DOMAIN is the domain of your Organization

ACCESS\_TOKEN - Access token generated using the client credentials


Here’s the second page displaying the next 2 users in the result.

```json
    {
      "results": [
        {
          "key": "134bd5e9-0c08-48fa-a05f-82a5f1a3b2f7",
          "name": "",
          "email": "example3",
          "status": "Invited",
          "access": {
            "hasOrganizationRoles": true,
            "hasApplicationRoles": false
          },
          "lastLoginAt": null,
          "isActive": false,
          "photoUrl": null,
          "isEmailVerified": false,
          "isTermsAndConditionsAccepted": false
        },
        {
          "key": "216042ab-836d-4631-95c7-2a2af2db5011",
          "name": "",
          "email": "example4",
          "status": "Invited",
          "access": {
            "hasOrganizationRoles": true,
            "hasApplicationRoles": false
          },
          "lastLoginAt": null,
          "isActive": false,
          "photoUrl": null,
          "isEmailVerified": false,
          "isTermsAndConditionsAccepted": false
        }
      ],
      "page": {
        "count": 2,
        "limit": 2,
        "offset": 2,
        "nextPageOffset": 4,
        "totalResults": 10,
        "totalPages": 5
      }
    }

```

## Best practices

* Set the limit explicitly to control the number of results per page.

* Determine the `limit` value (page size) to balance performance and usability. Smaller page sizes minimize response payloads, potentially improving performance, while larger sizes reduce the number of API calls needed.
