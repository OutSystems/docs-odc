---
guid: e1827f34-4fea-4b24-a211-923889adf008
locale: en-us
summary: "OutSystems Developer Cloud (ODC) Self-hosted configurator: reopen on a bootstrapped cluster to update APM, database, or container registry settings."
figma: https://www.figma.com/design/la33iciyGndnV5JRqR359g/Managing-OutSystems-platform-and-apps?node-id=5082-133
coverage-type:
  - apply
topic:
app_type: reactive web apps, mobile apps
platform-version: odc
audience:
  - Platform administrator
tags:
  - Authentication
  - Infrastructure
  - Security
  - Settings
outsystems-tools:
  - self hosted configurator
helpids:
isautopublish: true
---

# Open the Self-hosted configurator

After your self-hosted cluster is set up, you may need to reopen the Self-hosted configurator to make changes to your configuration. Common reasons include:

* Updating your APM tool endpoint or credentials.
* Updating a stage's database connection details, for example to rotate credentials or change the port.
* Continuing stage setup.
* Updating your container registry credentials.

This article covers how to reopen the configurator on an already-bootstrapped cluster. It is not the same as running a new installation. The platform services are already installed, so you won't go through the full setup wizard again.

## Prerequisites {#prerequisites}

Refer to [Install Self-hosted ODC stages](install-sh.md#prerequisites) for the full list of prerequisites.

## Reopen the configurator {#reopen-configurator}

1. In the ODC Portal, go to **Management** > **Organization**.

    ![ODC Portal Organization page showing Details, Domain, and a Stages table with Development (Online), Test (Configured), and Production (Configured).](images/sh-organization-stages-pl.png "Organization page with self-hosted stages")

1. In the **Stages** table, click the self-hosted stage you want to open the configurator for, such as **Test** or **Production**.

1. On the stage detail page, select the **Self-hosted** tab.

    ![Test stage detail page in ODC Portal showing the Settings and Self-hosted tabs, with the Self-hosted tab selected and a Self-hosted configurator command block for Windows.](images/sh-stage-selfhosted-tab-pl.png "Self-hosted tab on the stage detail page")

1. From the drop-down list, choose your operating system, and copy the **Self-hosted configurator command**.

1. In a shell session with the target cluster set as the current context, run the copied command.

    This opens the Self-hosted configurator. Because the cluster is already bootstrapped, this command opens the existing configurator rather than running a new installation.

    <div class="info" markdown="1">

    If the **Log in to Self-hosted setup** page does not open automatically, copy the URL (for example, `http://localhost:5050/`) from the shell session and paste it in your browser.

    </div>

1. On the same **Self-hosted** tab, scroll down to **Self-hosted configurator credentials**.

1. Copy your credentials, or generate a new client secret if the existing one has expired.

1. In the Self-hosted configurator, on the **Log in to Self-hosted setup** page, authenticate using your credentials.

    What you see next depends on your cluster setup:

    * **At least one stage is already configured** — the configurator takes you directly to **Self-hosted settings**. Continue with the next step.
    * **No stages are configured yet** — the prerequisites check page appears. Select **Start configuration** to open the **Configure stages** step in the setup wizard and complete stage configuration.

1. In **Self-hosted settings**, select the tab for what you need to change:
    * **Stages** to update the database connection details for a stage, for example to rotate credentials or change the port.
    * **APM tool** to update your APM endpoint or credentials.
    * **Container registry** to update your registry credentials.

    ![Self-hosted configurator settings page showing Stages, APM tool, and Container registry tabs, with Test and Production stages listed as Configured.](images/sh-settings-shc.png "Self-hosted settings in the configurator")
