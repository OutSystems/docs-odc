---
summary: OutSystems Developer Cloud (ODC) supports seamless integration with external databases for enhanced app development.
helpids: 30191, 30483
tags: database integration, data security, data fabric, private gateways, configuration management
locale: en-us
guid: 67608c14-0b83-4e69-bf46-ba023ed730f4
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
audience:
  - platform administrators
  - full stack developers
  - mobile developers
  - frontend developers
outsystems-tools:
  - odc studio
  - odc portal
coverage-type:
  - apply
  - remember
---

# Integrate with external data sources using Data Fabric

OutSystems Data Fabric simplifies access and integration of complex enterprise data into your app. You can aggregate information from hundreds of sources, such as Salesforce or SAP, eliminating the complexity of combining data across different systems.

Regardless of the external system you’re integrating with, Data Fabric enables you to use [Aggregates](../../building-apps/data/fetch-data/aggregate.md) to query data seamlessly, as your data will be represented as [Entities](../../building-apps/data/modeling/entity.md).

How it works:

1. First, from the ODC Portal, admins [create connections](create-connection-external-data.md) to the external data source and select the entities. For the supported external data sources, refer to the [OutSystems system requirements for ODC](../../getting-started/system-requirements.md#supported-external-data-sources).
1. Then, in ODC studio, developers use Aggregates to fetch the data in their apps, having the option to [combine data from different data sources](../../building-apps/data/fetch-data/data-mash.md).

See how OutSystems [handles your external data in Data Fabric](../../manage-platform-app-lifecycle/platform-architecture/intro.md#data-fabric).
