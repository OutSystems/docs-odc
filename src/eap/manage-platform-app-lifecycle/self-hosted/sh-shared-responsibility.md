---
guid: 7d901e26-3b77-4d4f-923d-956d78cd146d
locale: en-us
summary: OutSystems Developer Cloud (ODC) self-hosted combines customer-managed infrastructure with cloud-managed development, defining clear responsibility boundaries.
figma: https://www.figma.com/design/la33iciyGndnV5JRqR359g/Managing-OutSystems-platform-and-apps?node-id=4714-13661
coverage-type:
  - understand
  - remember
topic:
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - architects
  - infrastructure managers
  - platform administrators
  - tech leads
tags: self-hosted,responsibility model,cloud,infrastructure,outsystems
outsystems-tools:
  - odc portal
  - self hosted console
helpids: 
---

# Self-hosted ODC shared responsibility model

OutSystems Developer Cloud (ODC) self-hosted offers a hybrid deployment model that combines the control and compliance benefits of customer-managed infrastructure with the stability and agility of a cloud-managed development experience.

In this model:

* The **ODC Portal** and **development stage** are hosted and operated by OutSystems in the cloud. Customers are responsible for the applications and data they create in this environment, but not for the infrastructure or platform services that support them.

* The **self-hosted stages** (such as Test and Production) run in infrastructure fully managed by the customer. These stages rely on OpenShift and PostgreSQL clusters provisioned and operated by the customer. However, key OutSystems components—such as runtime services, secrets management, and telemetry collectors—are deployed into these environments by OutSystems. While these services run within the customer’s infrastructure, they remain fully owned, patched, and evolved by OutSystems.

This architecture enables customers to meet regulatory, integration, and operational requirements while continuing to benefit from OutSystems’ managed platform updates and support. At the same time, it introduces a clear operational boundary: **OutSystems manages the platform; customers manage the runtime infrastructure**.

This article defines how responsibilities are split across that boundary. It's intended for:

* **Decision-makers** seeking clarity on governance, support, and compliance expectations.
* **Infrastructure and platform teams** provisioning and operating the self-hosted stages.
* **DevOps and SRE teams** responsible for observability, access control, and integration with enterprise systems.

By understanding this shared responsibility model, customers can:

* Avoid ambiguity in roles and support ownership.
* Ensure infrastructure readiness for platform operations.
* Confidently scale and operate their self-hosted ODC environments in coordination with OutSystems.

## Responsibility model

The ODC self-hosted model introduces a clear operational boundary between what OutSystems delivers and maintains, and what the customer must provision, operate, and secure.

Several OutSystems-managed components—such as runtime services and telemetry collectors—are deployed into the self-hosted stages. These services are not configurable, patchable, or replaceable by the customer. Their lifecycle remains fully under OutSystems’ control. The customer's responsibility is to **ensure the infrastructure remains healthy and accessible**, so that platform services can run reliably and receive updates when required.

The model distributes responsibilities along two axes:

* **Ownership**: Who is responsible for building, maintaining, and supporting the component?

* **Deployment location**: Is the component hosted in the OutSystems Cloud or in the customer’s infrastructure?

This distinction is essential in hybrid deployments. For example:

* The **runtime services** run in the customer’s infrastructure, but customers must not alter, patch, or replace them.

* The **APM tool** is customer-owned and external to ODC; OutSystems provides the app logs and traces data stream.

* The **Portal and Development stage** are fully managed by OutSystems in the cloud, but the customer is still responsible for the data and applications they create in those environments.

The shared responsibility model for ODC Self-Hosted can be visualized as a layered architecture.

The top layers represent OutSystems responsibilities. These include both cloud-hosted services (such as the ODC Portal and Development stage) and OutSystems self-hosted services that run inside the customer's infrastructure (such as the runtime services and secrets manager).

The lower layers reflect the customer's responsibilities. These include provisioning and operating the infrastructure that hosts the self-hosted stages, managing applications and data, and ensuring that all dependencies are in place for platform services to function correctly.

![Diagram of the ODC self-hosted shared responsibility model, showing OutSystems responsibilities for portal, development stage, and OutSystems services in the cloud and self-hosted infrastructure, and customer responsibilities for apps, data, infrastructure expertise, identity provider, network, databases, APM, and sizing.](images/sh-responsability-mode-diag.png "Shared responsibility model for ODC self-hosted across OutSystems cloud and customer infrastructure")

## OutSystems responsibilities

OutSystems is responsible for the design, operation, and continuous evolution of the ODC platform. In the self-hosted model, this includes components that run in the OutSystems cloud as well as services that are deployed into customer infrastructure.

### OutSystems cloud-hosted platform services

These services are fully operated by OutSystems and hosted in the cloud. Customers interact with them through standard platform interfaces, but do not provision or maintain them.

OutSystems is responsible for:

* Running the **ODC Portal**, where customers manage applications, environments, and deployments.
* Hosting the **Development stage**, where customers can build and test applications without managing the underlying infrastructure.
* Delivering supporting capabilities such as authentication integration, application packaging and deployment, and container management.

These services remain fully under OutSystems’ control for availability, security, scalability, and updates.

### OutSystems self-hosted services

These are services provided and maintained by OutSystems, but deployed inside the customer’s infrastructure to support the operation of the self-hosted stages.

OutSystems is responsible for:

* Providing these services as part of the platform.
* Maintaining their full lifecycle: patching, upgrades, and platform alignment.
* Ensuring their compatibility with the rest of the ODC platform.

These services include the core runtime services that execute applications, along with supporting components for secrets management, telemetry collection, deployment orchestration, and infrastructure integration.

Although these services run inside the customer’s OpenShift environment, customers **must not modify, patch, or replace them**. Instead, customers are responsible for:

* Provisioning and maintaining the infrastructure where these services run.
* Ensuring that infrastructure meets system and network requirements and is accessible for updates.

This split allows customers to maintain control over their data and hosting model, while preserving OutSystems’ ability to deliver a consistent and supportable platform experience.

## Customer responsibilities

In the ODC self-hosted model, customers take ownership of the hosting environment where the self-hosted stages run. This includes provisioning and operating the infrastructure, securing access, and managing the data and applications that live within these environments.

To ensure a successful deployment, customers are responsible for maintaining a stable, secure, and accessible hosting environment that meets the platform’s system requirements.

### Customers must have infrastructure expertise

Because the self-hosted stages depend on infrastructure components operated by the customer, teams must have the skills and experience to manage that environment. This includes:

* Container orchestration and RedHat OpenShift.
* PostgreSQL database management.
* Enterprise networking, including DNS, routing, and firewalls.

OutSystems does not manage or support the infrastructure layer directly. Customers must ensure they have qualified personnel to provision, monitor, and troubleshoot the hosting environment.

Customers are responsible for sizing the infrastructure that hosts self-hosted stages. This includes the OpenShift and PostgreSQL clusters and any supporting services. Infrastructure must be provisioned with enough capacity to support ODC self-hosted [installation requirements](sh-install-reqs.md), application workloads, and operational continuity, including during updates and peak usage periods.

### Customers must secure access and identity

Customers are responsible for securing access to their infrastructure and runtime stages. This includes:

* Providing and maintaining an OIDC-compliant identity provider.
* Managing role-based access control (RBAC) within their cluster.
* Enforcing security policies (for example, network segmentation, firewall rules).

OutSystems integrates with customer-provided identity systems but does not control access policies within the self-hosted environment.

### Customers are responsible for application lifecycle and observability

Customers are fully responsible for the applications they develop and deploy into both cloud-hosted and self-hosted stages. This includes:

* Developing, testing, and deploying applications.
* Managing application data and user data.
* Monitoring application behavior and performance using their APM tools.

OutSystems provides telemetry data through the monitoring platform, but customers must host and operate their own observability destination.

### Customers must ensure readiness for platform services updates

OutSystems is responsible for updating the self-hosted services, but those updates require cooperation from the customer. Customers are expected to:

* Maintain connectivity between their hosting environment and the OutSystems cloud.
* Ensure that update channels are open and not blocked by firewall or proxy configurations.
* Avoid changes that could interfere with the deployment or operation of OutSystems-managed components.

Customers are not responsible for the self-hosted services update logic itself, but must ensure their infrastructure does not prevent it.

### Customers must ensure database upgrades

ODC follows a versioning and compatibility strategy for the PostgreSQL databases used in self-hosted stages.

OutSystems may require customers to upgrade their self-hosted databases to newer PostgreSQL versions. This is necessary to ensure continued platform support, benefit from upstream performance and security improvements, and maintain compatibility between self-hosted stages and the OutSystems cloud.

When such an upgrade is required, OutSystems will:

* Provide advance notice and clear guidance on the supported versions.
* Define a specific upgrade window during which both the old and new database versions are supported.
* Ensure platform compatibility for both versions during this upgrade window.

**Customers are responsible for performing the actual upgrade of their PostgreSQL databases within the upgrade window.**

Failing to upgrade within the defined window may result in loss of support or compatibility issues with future platform updates.

To avoid such risks, customers should:

* Monitor version support announcements from OutSystems in the Portal.
* Plan internal upgrade cycles to align with the platform's supported versions.
* Provision new tenants with self-hosted stages on the most recent supported PostgreSQL version.

## Best practices for a smooth operation

To ensure the long-term success and supportability of an ODC self-hosted deployment, customers should adopt practices that align with the shared responsibility model and anticipate key operational requirements.

### Maintain infrastructure readiness for platform updates

OutSystems self-hosted services fetch periodic updates. While the update logic is handled by OutSystems, successful delivery depends on network requirements to be met.

* Validate outbound connectivity from your infrastructure to the OutSystems cloud.  
* Avoid firewall or proxy changes that may block critical update channels.  
* Monitor infrastructure health to prevent issues that could disrupt deployment or patching.

### Monitor your own infrastructure and applications

OutSystems does not operate the customer’s hosting environment or application workloads. Customers are responsible for ensuring infrastructure and applications perform as expected.

* Use appropriate tooling to monitor OpenShift, PostgreSQL, networking, and storage health.
* Configure observability and alerting in your APM tool to track application behavior.
* Investigate incidents starting from your infrastructure and app layers before escalating to OutSystems.

### Keep your system versions and configuration aligned with prerequisites

OutSystems publishes system requirements and version compatibility guidelines. Staying within those parameters avoids deployment failures and support risks.

* Regularly review system requirement updates.
* Plan upgrades to OpenShift or PostgreSQL in coordination with OutSystems recommendations.
* Avoid unsupported customizations to infrastructure components.

### Assign clear internal ownership for each responsibility area

The hybrid architecture touches multiple domains—platform, infrastructure, security, and observability. Clarity on who owns what within the customer organization helps reduce misalignment and delays.

* Define ownership for infrastructure, applications, APM tooling, and access control.
* Align roles with the responsibility diagram to avoid overlapping assumptions.
* Ensure your team structure supports coordination with OutSystems when needed.
