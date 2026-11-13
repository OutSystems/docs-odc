---
summary: Implement semantic search in ODC in three phases, from making content searchable to testing the search, with the role and the tool for each task.
tags:
  - AI
  - Data
  - Entities
  - Indexes
  - Logic
  - Roles
  - Testing
guid: 5392a1db-9f53-46f3-b985-6e431c5147bd
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=11021-32
coverage-type:
  - apply
  - understand
topic:
  - implement-semantic-search
  - test-semantic-search
audience:
  - Architect
  - Developer
  - Platform administrator
  - Tech lead
outsystems-tools:
  - odc studio
  - odc portal
helpids:
isautopublish: true
---

# Implementing semantic search in ODC

To let apps and agents find your content by meaning, you make the content searchable and add a search to the logic of your app. Then, you test that the search returns your content. The tasks depend on where the content lives: in text or File attributes of an entity, or in documents in a knowledge base. A developer works in ODC Studio, an administrator works in the ODC Portal, and the ODC platform indexes the content and runs the search.

Implementing semantic search, also known as Native Semantic Search, has three phases, and each phase produces the result that the next phase needs. The following diagram shows the phases, the role that performs each task, and the tool where the role performs it.

![Swimlane diagram of the semantic search process. In phase 1, make content searchable, the developer selects searchable attributes in ODC Studio and publishes the app, and the ODC platform indexes the entity records. For a knowledge base, the administrator creates the knowledge base and uploads files in the ODC Portal, and the ODC platform generates the search action and indexes the uploaded files. In phase 2, add search to your app, the developer adds the Semantic Search node or the SearchKB action and uses the results. In phase 3, test the search, the developer publishes the app and runs a search after indexing finishes, and the ODC platform returns ranked results.](images/semantic-search-process-diag.png "Semantic search process")

## Prerequisites

Confirm the following before you start:

* Semantic search is available in the runtime region of each stage where your app runs. Availability differs for text attributes, File attributes, and knowledge bases. For more information, refer to [Regions and languages for semantic search](search-regions-languages.md).
* The developer uses ODC Studio 1.7.15 or later for text attributes and knowledge bases, or ODC Studio 1.7.20 or later for File attributes.
* For a knowledge base, the role of the administrator includes the permissions to create a knowledge base and upload files. For more information, refer to [Create and manage a knowledge base in the ODC Portal](../knowledge-base/create-manage-knowledge-base.md).

## Make content searchable

In the first phase, you mark the content for semantic search, and the platform indexes it. A search returns only the content that the platform has indexed, so this phase comes first. The tasks depend on the search option.

For entity content, the developer configures and publishes in ODC Studio, and the platform then indexes the existing records and keeps the index current:

* **Developer, ODC Studio**: Selects the searchable attributes of an entity and chooses a chunk method for each attribute. The chunk method sets how the platform splits the content into the passages that a search returns. For more information, refer to [Make entity attributes searchable](make-attributes-searchable.md).
* **Developer, ODC Studio**: Publishes the app. Publishing applies the semantic search configuration to the app.
* **ODC platform**: Indexes the records that already exist in the entity. While the app runs, the platform updates the index when records or files are created, updated, or deleted.

For a knowledge base, the administrator sets up the knowledge base and uploads the files in the ODC Portal, and the platform generates the search action and indexes each file:

* **Administrator, ODC Portal**: Creates the knowledge base and chooses its chunk method. The chunk method can't change after the knowledge base exists. For more information, refer to [Create and manage a knowledge base in the ODC Portal](../knowledge-base/create-manage-knowledge-base.md).
* **ODC platform**: Generates the `SearchKB<KnowledgeBaseName>` server action, which apps use to search the knowledge base.
* **Administrator, ODC Portal**: Uploads the files to the knowledge base.
* **ODC platform**: Indexes each uploaded file. The ODC Portal shows the status of each file.

The knowledge base and its chunk method are shared by all stages, and the files are separate in each stage. The administrator uploads the files in each stage where the app runs.

**Result**: Searchable attributes or a knowledge base, which the platform indexes in the background. You can start the second phase while the indexing runs.

## Add search to your app

In the second phase, you add the search to a server action and decide how your app uses the results. The Semantic Search node searches entity attributes, and the `SearchKB<KnowledgeBaseName>` action searches a knowledge base. For more information, refer to [Add semantic search to your app](add-semantic-search.md).

* **Developer, ODC Studio**: For text or File attributes, adds the Semantic Search node to a server action and selects the searchable attributes.
* **Developer, ODC Studio**: For a knowledge base, adds the `SearchKB<KnowledgeBaseName>` action to the app as a public element and calls it in a server action.
* **Developer, ODC Studio**: Uses the results in the app logic, passes them to an AI model as grounding data, or exposes the server action to an agent as an agent action.

**Result**: A server action that runs the search and uses the results.

## Test the search

In the third phase, you confirm that the search returns your content. Run the test after the platform finishes indexing, because a search omits the content that the platform hasn't indexed yet.

* **Developer, ODC Studio**: Publishes the app, adds content that matches a test query, and runs the server action. For a knowledge base, the test file must be in the knowledge base of the stage where the app runs, because each stage has its own files.
* **ODC platform**: Compares the query with the indexed content and returns the matching content as ranked results.

**Result**: A search that returns your content to your app and agents.

## Next steps

Continue with the procedure for your search option:

* To make text or File attributes searchable, refer to [Make entity attributes searchable](make-attributes-searchable.md).
* To create a knowledge base and upload files, refer to [Create and manage a knowledge base in the ODC Portal](../knowledge-base/create-manage-knowledge-base.md).
* To add the search to a server action and test it, refer to [Add semantic search to your app](add-semantic-search.md).
* To set the search inputs and use the results, refer to [Semantic search inputs and results](search-inputs-results.md).
