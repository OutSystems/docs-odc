---
guid: 2433ca96-db20-493f-b04b-0e82e33c424e
locale: en-us
summary: Understand the architecture of ODC Self-hosted, runtime stages on customer infrastructure, OpenShift orchestration, outbound connectivity, and security requirements.
figma: https://www.figma.com/design/la33iciyGndnV5JRqR359g/Managing-OutSystems-platform-and-apps?node-id=4714-13020
coverage-type:
  - evaluate
  - understand
topic:
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - platform administrators
  - tech leads
  - architects
  - infrastructure managers
tags: self-hosted,data security,regulatory compliance,customization,hybrid
outsystems-tools:
  - odc portal
  - self hosted console
helpids:
isautopublish: true
---

# ODC Self-hosted

The OutSystems Developer Cloud (ODC) offers a flexible deployment model that allows you to choose between a fully cloud-managed solution and a self-hosted deployment. The self-hosted model is designed to meet the needs of organizations that prioritize data security, regulatory compliance, and infrastructure customization. This model allows businesses to maintain control over their data and infrastructure while leveraging the power of the ODC platform for application development and management.

ODC's self-hosted model provides an alternative for customers who need to maintain control over their IT environment, while still benefiting from the capabilities of a modern, cloud-based application platform. This deployment model allows organizations to manage sensitive data locally, comply with regulatory standards, and customize their infrastructure to fit unique business needs, all while staying connected to the ODC cloud for platform-level services and updates.

As cloud computing becomes more popular, self-hosted deployments continue to hold significant value, especially for businesses with strict compliance requirements or unique infrastructure needs. ODC's self-hosted model addresses:

* **Data sovereignty and compliance**: Enables customers to host sensitive runtime data in compliance with local regulations, such as GDPR. This is particularly crucial for industries such as finance, healthcare, and government, where data residency and protection are top priorities.  
* **Customization and control**: Provides complete control over customization and data management, empowering customers to adapt the deployment to their unique IT environment. Customers can manage resources, fine-tune performance, and adjust configurations based on specific operational requirements.  
* **Hybrid flexibility**: Supports hybrid models, allowing customers to connect their self-managed infrastructure with cloud services. This flexibility makes it possible for organizations to adopt a hybrid cloud strategy, combining the benefits of on-premises and cloud-based services.

## Use cases {#use-cases}

* **Data-sensitive environments**: Businesses operating in industries with stringent data regulations, such as finance or healthcare, can leverage the self-hosted model to comply with local data sovereignty laws. By keeping sensitive data within their own infrastructure, these organizations can meet regulatory requirements without compromising on application capabilities.

* **Infrastructure flexibility**: Organizations with multiple facilities, such as manufacturing plants or branches, can deploy infrastructure on-site to meet specific operational needs. The self-hosted model allows these facilities to operate independently while remaining integrated with the overall application ecosystem, providing resilience and reducing dependency on cloud connectivity.

* **On-premise integration**: Customers with existing on-premise resources and Kubernetes clusters can integrate them seamlessly with ODC, reducing latency and improving connectivity. This is particularly advantageous for organizations that need low-latency access to their applications or have significant investments in on-premises infrastructure.

* **High customization needs**: Companies that require unique infrastructure configurations or have proprietary technologies can use the self-hosted model to achieve the level of customization needed. This deployment option allows for tailored configurations that align with specialized operational requirements, providing the flexibility to innovate without constraints.

## Key features {#key-features}

* **Self-hosted runtime stages**: Customers can deploy runtime stages such as Test and Production on their own infrastructure, while the ODC Portal, platform services, and Development stage continue to be managed in the OutSystems Cloud. This separation allows customers to maintain full control over their runtime, while preserving a unified development experience.

* **Control over infrastructure**: Customers control infrastructure components, including Kubernetes clusters and PostgreSQL databases, with full responsibility for patching and updates. RedHat OpenShift assists in orchestrating these clusters, automating tasks such as scaling, resource allocation, and failover.

* **Security and compliance**: self-managed identity providers (OIDC-compliant) and support for secrets management ensure that data remains secure. The model allows for integration with enterprise-grade security practices, giving customers peace of mind regarding data integrity and compliance.

* **Outbound-only connections to the OutSystems Cloud**: Communication between the self-hosted environment and the ODC platform is established via outbound connections over a TLS channel, providing additional security. This design minimizes exposure and enhances the security posture of the self-hosted environment.

## High-level system architecture {#architecture}

The self-hosted deployment model allows customers to run application runtime stages on their own infrastructure, using Kubernetes clusters and PostgreSQL databases. OpenShift plays a critical role in managing these Kubernetes clusters by providing a robust orchestration layer that simplifies deployment, scaling, and monitoring of containerized applications. Customers are expected to have knowledge of container technologies and OpenShift to manage and maintain these environments effectively. The architecture maintains a clear division of responsibilities:

* **OutSystems Cloud**: This section of the architecture is responsible for managing the **Portal**, **Platform services** (such as Identity, Deploy, Build, and other services), and the **Development runtime stage**. These components are hosted and maintained by OutSystems to ensure that the platform remains evergreen and continues to receive updates without customer intervention. OutSystems Cloud provides a stable and secure foundation for application development, allowing developers to focus on building features rather than maintaining infrastructure.

* **Self-hosted infrastructure**: Customers have control over this environment, which includes managing the infrastructure, databases, and ensuring security. Hosts non-production and production runtime stages, including application data and end-user data, all of which is within the self-hosted boundary:
    * OpenShift is leveraged to ensure efficient orchestration of the runtime stages, providing features like automated scaling, self-healing, and monitoring to help customers maintain their clusters effectively. Your organization should have experience with containers and OpenShift to successfully manage and maintain these stages.
    * Dedicated **OpenShift clusters** host the runtime stages, such as **Test runtime stage** and **Production runtime stage**.
    * It also includes the necessary services like an OIDC-compliant **Identity Provider**, and **Application Performance Monitoring (APM)** tool and the runtime databases.
    * All app **data** and end-user data are managed within the self-hosted infrastructure boundary.
    * Connections are always initiated outbound from the self-hosted cluster, to the OutSystems cloud, ensuring a secure interaction.

![High-level diagram showing OutSystems Cloud hosting the Portal, Dev runtime stage, OutSystems services, and Dev database, connected to a self-hosted OpenShift cluster that runs Test and Prod runtime stages with their own databases, OutSystems services, an APM tool, and an identity provider.](images/self-hosted-diag.png "High-level architecture of ODC Self-hosted")

Understanding the division of responsibilities is critical for successful deployment. For details, see the [Self-hosted ODC shared responsibility model](sh-shared-responsibility.md).

## Detailed architecture view

The diagram below expands on the high-level view above, showing how the two main environments (OutSystems Cloud and your self-hosted cluster) are internally organized and how they connect. It depicts a single-cluster deployment but ODC also supports multi-cluster deployments, where different self-hosted stages run in different clusters.

![Detailed architecture diagram showing OutSystems Cloud with members using ODC Studio, platform services, and the Dev runtime stage pushing images to a container registry, which syncs to a self-hosted OpenShift cluster that includes CI/CD services, secrets management, monitoring and telemetry, messaging, system storage, network and traffic components, Test and Production runtime stages with dedicated databases, plus external APM and identity provider, with app end users accessing through an ingress controller.](images/sh-detail-arch-diag.png "Detailed architecture of ODC Self-hosted deployment")

**OutSystems Cloud** hosts the Portal and the platform services that power the development experience: It also runs the Development runtime stage, where the OutSystems runtime services (timers, workflows, app authentication, and others) run under OutSystems management.

A container registry sits at the boundary between cloud and self-hosted, acting as the handoff point. When a build completes in the cloud, the resulting container image is synced to the OCI registry inside your cluster, making it available for deployment into your self-hosted stages.

**Your self-hosted cluster** runs on an OpenShift cluster that contains both the OutSystems runtime services and the supporting services OutSystems installs alongside them. The runtime services are the same ones that power the Development stage in the cloud, but here they run under your infrastructure, supporting your Test and Production stage apps. The supporting services are grouped by function:

* **CI/CD services** (OCI Registry, Flux CD): receive the synced container images and deploy them into the correct runtime stage.
* **Secrets management** (HashiCorp Vault): stores credentials, tokens, and certificates used by platform services, without embedding them in configuration.
* **Messaging** (NATS): provides the communication backbone between distributed services inside the cluster.
* **System storage** (SeaweedFS): handles persistent file storage for platform artifacts and services.
* **Monitor and telemetry** (Prometheus, OpenTelemetry, FluentBit): collect metrics, traces, and logs from both platform services and your apps, and route them to your APM tool.
* **Network and traffic** (Gloo Edge, Istio): control how traffic flows between services inside the cluster and how your applications are exposed externally.

Each runtime stage connects to a dedicated PostgreSQL database. Test and Production each have their own. Outside the cluster, your self-hosted ODC integrates with two customer-managed components: the APM tool that receives observability data, and the Identity Provider that handles authentication across your apps.

All inbound traffic from app end users enters through the Ingress controller, which routes it to the appropriate runtime stage via Gloo Edge. All communication between the self-hosted cluster and OutSystems Cloud is initiated outbound.
For network and infrastructure prerequisites, refer to [System requirements to install Self-hosted ODC](sh-install-reqs.md). For configuration guidance about this inbound traffic path, refer to [Configure inbound app traffic for self-hosted ODC](sh-domain-config.md).

For a detailed description of each installed service and its role, see [Services installed in a self-hosted cluster](sh-cluster-components.md).

## Before setup {#before-setup}

In order to set up your self-hosted stages, ensure you have:

* **Platform operations:** Customers must bring personnel knowledgeable in configuring and managing Red Hat OpenShift, as well as the required network, databases, identity provider, and application performance monitoring (APM) solutions. This ensures the self-hosted environment is properly set up, maintained, and integrated.

* **Infrastructure**: A self-managed OpenShift cluster and PostgreSQL databases are required to support the runtime stages.You should have experience managing containerized infrastructure and be comfortable working with Kubernetes and OpenShift. This knowledge is essential for maintaining the health, scalability, and reliability of the self-hosted environment. The infrastructure must be capable of handling production workloads, and it is recommended that customers provision sufficient resources to ensure high availability.

* **Identity and security**: Customers must provide their own OIDC-compliant identity provider. This ensures that the self-hosted environment integrates seamlessly with your existing security framework, providing a consistent and secure identity management solution.

* **Connectivity**: An always-on outbound connection from the self-hosted environment to the OutSystems Cloud is required for platform updates. This connection enables ongoing synchronization and ensures that the platform remains up to date, while also providing a secure communication channel between the cloud and customer-managed environments.

* **APM tool:** for application health monitoring and troubleshooting; logs and traces are exported in OpenTelemetry format, compatible with platforms such as New Relic, Dynatrace, and Splunk.

* **Load balancer**: A customer-managed component, such as a load balancer, API gateway, or reverse proxy, required to expose applications running in the self-hosted cluster to end users.

See the [installation requirements](sh-install-reqs.md) for further details.
