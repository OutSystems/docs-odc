---
summary: Learn more about installing or updating a Forge asset for use in ODC Studio. 
tags:
helpids: 30477
locale: en-us
guid: 515576a8-5acd-449b-af7c-d2c0670056dd
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---

# Install or update a Forge asset

Forge assets become available only after they go through a submission and approval process. Once an asset is in Forge, users can install it in their organization. The asset is then accessible in ODC Studio. The label displays additional information on the details page. A Forge asset can have any of the following labels.

| Label / button | Description                                                                               |
| :-------------- | :----------------------------------------------------------------------------------------- |
| Install        | The asset is ready to install                                                             |
| Installing     | The asset is installing                                                                   |
| Installed      | The asset is installed and is ready to use                                                |
| Update         | The asset has an update that hasn't yet been installed in your organization’s environment |
| Updating       | The asset is updating                                                                     |
| Up-to-date     | The asset is current, up-to-date, and ready to use                                        |

Following are procedures to Install and Update a Forge asset.

## Install a Forge asset

Follow these steps to install an asset:

1. Open Forge to display the assets. If you don’t see your asset, you can use Search.
1. Do one of the following:

    * From the Forge assets card, click **Install**.
    * From the Forge assets card, click anywhere. The Details page opens for you to learn more about the asset. When ready, click **Install**.

    <div class="info" markdown="1">

    A progress spinner shows the installation status. When the installation successfully completes, an installed label displays on the card.

    </div>

1. To use the asset, open it in ODC Studio.

## Install an updated Forge asset

Occasionally, an asset owner makes updates to an asset that you already installed. If the asset has updates available, the **Update** button displays. In this case, you should update your asset so you can benefit from the latest changes. Follow the steps below to update an already installed asset.

1. Open Forge to display the assets. If you don’t see your asset, you can use Search.
1. Do one of the following:

    * From the Forge assets card, click **Update**.
    * From the Forge assets card, click anywhere. The Details page opens for you to learn more about the asset. When ready, click **Update**.

    <div class="info" markdown="1">

    A progress spinner shows the installation status. When the installation successfully completes, an installed label displays on the card.

    </div>

1. To use the asset, open it in ODC Studio.

## Modify an installed Forge asset

Although Forge provides reusable assets to help you build your apps, you might want to make changes to an asset. For example, you might want to modify an asset to change a connector that better meets your organization's needs.

When you install a Forge asset from the ODC Portal, the asset is automatically locked. You can’t edit Forge assets, but you can make changes by cloning the original asset. Your original Forge asset continues to be available in your tenant. If you have references to the original Forge asset, You might want to consider updating the  references to your cloned asset.

<div class="info" markdown="1">

Remember, cloned assets aren't supported. You lose the benefit of being able to easily take advantage of updates once you create your clone.

</div>

When you attempt to open a Forge asset in ODC Studio, a prompt displays asking if you want to create a clone. The clone is a duplicate of the original asset, but it’s no longer related to the original asset. OutSystems recommends using a naming convention that includes the word “clone” and a number such as clone_#_of_name_of _asset. You can publish cloned assets in your tenant. Once you publish your app, you can reference it as well.

If a new version of the original asset becomes available and has functionality you want to use and modify, you must copy it to your clone. To identify the differences between clone_1 (your original clone) and the updated Forge asset, you can use OutSystems **Compare and merge with another version** function. To use this function, you must create a clone of the updated asset. Then you can compare clone_1 to clone_2. The result shows you where the differences exist. Then, you can make the changes to clone_1.

Sometimes, documentation for a Forge asset includes the contact information for the owner. If the Forge asset owner is listed, you can contact them and discuss the updates you want to make.
