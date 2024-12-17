---
summary: Learn how to configure and integrate external data sources with AI search services for use in OutSystems Developer Cloud (ODC).
tags: data integration, cloud services, ai search services, search service configuration
locale: en-us
guid: 425ba4ef-f4a7-42e1-9687-88a5e5021336
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - ai agent builder
coverage-type:
  - apply
---

# Configure your data sources

You can configure and add external data sources, such as your internal knowledge base, and integrate it with [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search) service or [Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html) search service. This allows you to leverage the Retrieval Augmented Generation (RAG) technique in AI models and build generative AI search experiences on top of your enterprise data source. Be sure to check the prerequisite sections for each search service. 

Here’s some best practices for preparing the content for use with the AI model:

* Use .md or .txt files. You can also use pdf files. 
*[Process](https://learn.microsoft.com/en-us/azure/search/cognitive-search-concept-image-scenarios)  the images to make it searchable.
* Keep each file under a maximum size limit of 16 MB.
* Aim for smaller files not only in size but also in content.
* Divide content into chunks, aiming for approximately 2 to 3 pages per file.
* Avoid using large files with extensive content to prevent hitting the token limit when utilizing additional context with the AI model.

To add data sources and use them in the AI Agent Builder you must: 

1. Configure and set up a search service service in [Azure](configure-azure-data-source.md) or [AWS](configure-aws-data-source.md), depending on the search service you choose.

2. Get your index, endpoint access, and access keys for your model.

3. Add your index, access keys, and end-point access information to the AI Agent Builder.

4. Create your agents and use the data source in the AI Agent Builder.

## Related resources

* [Configure Azure AI search with BLOB storage](configure-azure-data-source.md)

* [Add Azure AI Search data source in the AI Agent Builder app](add-azure-data-source-to-aibuilder.md)

* [Set up Amazon Kendra with a data source](configure-aws-data-source.md)

* [Add the Amazon Kendra data source to the AI Agent Builder app](add-aws-data-source-to-aibuilder.md)

* [Add a custom data source to the AI Agent Builder app](add-custom-data-source.md)
