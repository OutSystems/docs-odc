---
guid: 114d55d2-bea2-4d7a-9a1e-5124f339b938
locale: en-us
summary: Overview of the steps involved in installing a self-hosted OutSystems Developer Cloud (ODC) stage, outlining each major phase from infrastructure to final configuration.
figma: https://www.figma.com/design/la33iciyGndnV5JRqR359g/Managing-OutSystems-platform-and-apps?node-id=4714-13662
coverage-type:
topic:
app_type: reactive web apps, mobile apps
platform-version: odc
audience:
  - Platform administrator
  - Architect
tags: self-hosted installation, outsystems developer cloud, infrastructure provisioning, database configuration, platform setup
outsystems-tools:
  - self hosted console
helpids:
---
# Self-hosted ODC installation overview

Installing a self-hosted ODC stage involves coordinating infrastructure provisioning, database configuration, and platform setup. This article walks you through the end-to-end process, helping you understand how each major step fits together before you begin.

While this overview doesn't provide detailed execution instructions for each task, it gives you the context and connections you need to approach the installation with confidence. For step-by-step procedures, you'll find links to detailed guides throughout this article.

1. [Procure the infrastructure](#procure-infra)

1. [Set up the database](#setup-db)

1. [Configure and install the stage](#install-stage)

1. [Configure inbound app traffic](#config-traffic)

1. [Finish the stage configuration](#finish-config)

You'll repeat this process for each additional stage you want to install.

## Procure the infrastructure {#procure-infra}

Before you can install a self-hosted stage, you need to provision the infrastructure that will host it. This means setting up the compute, storage, and networking resources required to run your applications reliably and securely.

These components form the foundation of your self-hosted environment. Make sure your team has the necessary expertise in container orchestration, OpenShift, and enterprise networking to provision and maintain this infrastructure. For complete specifications and requirements, see the [installation requirements](sh-install-reqs.md).

## Set up the database {#setup-db}

Each self-hosted stage requires its own dedicated PostgreSQL database to store application data.

While you have full control over the application data stored in the database, you must not alter the database schema or its underlying structure.

During the installation process, you'll provide the database connection details to the Self-hosted configurator, which will test the connection and ensure the database is properly configured. Make sure your database is accessible from the OpenShift cluster and meets all connectivity requirements before proceeding to the next step.

For guidelines on database configuration, see the [database setup guidelines](sh-db-setup.md).

## Configure and install the stage {#install-stage}

Once your infrastructure and database are ready, you'll use the Self-hosted configurator to bootstrap the platform services on your OpenShift cluster. The Self-hosted configurator handles the complex orchestration of installing and configuring platform services, so you don't have to manually deploy each component. For complete step-by-step instructions, see [Install Self-hosted ODC stages](install-sh.md).

Here's an overview of the process:

1. **Onboard in the ODC Portal**: You'll initiate the stage configuration from the Portal, which generates credentials and provides you with an installation command to run on your cluster.

1. **Install the Self-hosted configurator**: Run the installation command. This installs the configurator, which opens an interface for the remaining setup.

1. **Authenticate and configure**: Using the credentials from the ODC Portal, authenticate in the configurator and provide the necessary details for the APM endpoint and PostgreSQL connection.

1. **Deploy platform services**: The configurator installs the OutSystems services onto your OpenShift cluster. These services include the runtime components that execute your applications, along with supporting components for secrets management, telemetry collection, and infrastructure integration.

1. **Get your stage ID**: At the end of the configuration, you'll receive a unique stage identifier (UUID). Copy this ID, you'll need it in the next step to configure your load balancer and domain routing.

## Configure inbound app traffic {#config-traffic}

With the platform services deployed and your stage ID in hand, you now need to configure how external users will access your applications. This involves setting up DNS, a load balancer, and the routing logic that directs traffic to the correct stage.

In a self-hosted deployment, you're responsible for exposing your applications to end users. This means:

* Creating DNS records

* Configuring your load balancer to handle HTTPS traffic and perform TLS termination.

For detailed configuration instructions, see [Configure inbound app traffic for Self-hosted ODC](sh-domain-config.md).

## Finish the stage configuration {#finish-config}

The final step brings you back to the ODC Portal to [complete the stage setup](install-sh.md#add-domain). With your infrastructure running and traffic routing configured, you'll now tell ODC Portal how to reach your stage and how users should authenticate.

In this step, you'll:

* Add your domain

* Configure identity providers

Once you complete these steps, your stage will appear as **Configured** in the ODC Portal.
