---
guid: a1eb42b8-4d85-4fa5-9bed-a1eb471425cc
locale: en-us
summary: OutSystems Developer Cloud (ODC) semantic search requires searchable entities, a chunking type, and a search element in your server action flow.
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?m=auto&node-id=9242-10&t=0H9QM3Txfr0rYjmr-1
coverage-type:
  - apply
topic:
  - implement-semantic-search
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - Developer
  - Tech lead
tags:
  - Data Model
  - Entities
  - Indexes
  - Monitoring
outsystems-tools:
  - odc studio
helpids:
isautopublish: true
---
# Use semantic search

<div class="info" markdown="1">

Semantic search is in Beta. For more information about Beta features, refer to [OutSystems product releases](https://success.outsystems.com/support/release_notes/outsystems_product_releases/#beta). If you want to try this new capability contact your OutSystems account team.

</div>

To use ODC's built-in semantic search, meet the following prerequisites:

1. Have an existing data model with entities with text attributes.
1. Your entities must have an entity identifier. Learn more about [Entity Identifiers](../../../building-apps/data/modeling/entity.md#primary-key).

## Make your entities searchable

To make your entities searchable, do the following:

1. In the ODC Studio **Data** tab, right-click the entity and select **Select searchable attributes...**.

    ![ODC Studio interface showing the option to select searchable attributes for an entity.](images/select-searchable-attributes-odcs.png "Selecting Searchable Attributes")
1. Select the attributes and the chunking type for each.

    ![Popup window in ODC Studio for selecting chunking methods for entity attributes.](images/chunking-selection-odcs.png "Chunking Method Selection")
1. Your entity and selected attributes can be used in a semantic search.

    ![Popup window in ODC Studio showing selected attributes for semantic search.](images/attributes-selections-odcs.png "Attributes Selection")

## Add a semantic search to your app

To add a semantic search to your app:

1. In a server action, drag the **Semantic Search** element from the toolbox to your flow.

    ![ODC Studio interface showing the semantic search element added to a server action flow.](images/semantic-search-odcs.png "Adding Semantic Search to Logic Flow")
1. In the semantic search properties, make sure to:
    1. Write the search query.
    1. Select the source: an entity that you've already made searchable.
    1. Check the searchable attributes to use in your search.

    ![ODC Studio interface showing the properties of a semantic search element, including search query and searchable attributes.](images/semantic-search-details-odcs.png "Semantic Search Properties")

The output of a semantic search is a List of structures, each containing one search result.
