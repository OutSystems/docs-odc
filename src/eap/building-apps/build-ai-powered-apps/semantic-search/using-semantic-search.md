---
guid: a1eb42b8-4d85-4fa5-9bed-a1eb471425cc
locale: en-us
summary: Implement semantic search in OutSystems Developer Cloud (ODC) with data models, choosing attributes and search types, and integrating it into your app's logic flow.
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?m=auto&node-id=9242-10&t=0H9QM3Txfr0rYjmr-1
coverage-type:
  - apply
  - remember
topic:
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - frontend developers
  - backend developers
  - tech leads
  - full stack developers
tags: semantic search, odc studio, data models, mobile apps, reactive web apps
outsystems-tools:
  - odc studio
helpids:
---
# Use semantic search

<div class="info" markdown="1">

Semantic search is in Beta. For more information about Beta features, refer to [OutSystems product releases](https://success.outsystems.com/support/release_notes/outsystems_product_releases/#beta). If you want to try this new capability contact your OutSystems account team.

</div>

For you to use ODC semantic search built-in mechanism, you need to:

1. Have an existing data model with entities with text attributes.
1. Your entities must have an entity identifier. Learn more about [Entity Identifiers](../../../building-apps/data/modeling/entity.md#primary-key).

## Make your entities searchable

To make your entities searchable, do the following:

1. In the ODC Studio **Data** tab, right-click on the entity you want to add semantic search to and select **Select searchable attributes...**.

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
    1. Write a Search Query to be used by the semantic search to perform the search.
    1. Select the source. This will require to select an entity that you've made searchable before.
    1. Check all the searchable attributes that you want to use on your search

    ![ODC Studio interface showing the properties of a semantic search element, including search query and searchable attributes.](images/semantic-search-details-odcs.png "Semantic Search Properties")

The output of a semantic search is a List that holds a structure in it, with the search result.
