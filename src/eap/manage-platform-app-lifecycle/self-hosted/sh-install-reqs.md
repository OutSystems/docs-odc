---
guid: 4c87877b-7066-40b0-878b-3c5ecd4f6902
locale: en-us
summary: Ensure infrastructure requirements for OutSystems Developer Cloud (ODC) with dedicated resources and specific database, IDP, and APM setup.
figma: https://www.figma.com/design/la33iciyGndnV5JRqR359g/Managing-OutSystems-platform-and-apps?node-id=4714-13660
coverage-type:
  - remember
topic:
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - infrastructure managers
  - platform administrators
  - tech leads
  - architects
tags: infrastructure,requirements,database,authentication,monitoring
outsystems-tools:
  - self hosted console
helpids: 30551, 30563
isautopublish: true
---
# System and network requirements for Self-hosted ODC

To run ODC Self-hosted, your infrastructure must meet specific baseline requirements that ensure stability, security, and reliable operation. These requirements are divided into two main categories: system requirements that define the infrastructure components you need, and network requirements that establish the connectivity your cluster needs to communicate with both internal and external services. Make sure to assess and procure the necessary resources before starting the installation process.

## System requirements {#system-reqs}

The system requirements are:

* A RedHat OpenShift cluster on version 4.17 through 4.20.

* The OpenShift cluster must have at least 5 worker nodes each with 8 CPU cores, 32GB of RAM, and 250GB of disk space.

* The cluster should only host [components installed via the self-hosted setup](sh-cluster-components.md) and applications deployed through ODC. Services not provided as part of the ODC self-hosted setup like databases, IdP, or APM should run outside the cluster. ODC services and apps may scale normally by adding pods. ODC platform components installed in the cluster are intended exclusively to support ODC runtime and must not be used by external applications or integrations.

* The OpenShift storage backend must be able to provision at least 769 GB of persistent storage. The installation process reserves this capacity through persistent volume claims (PVCs) for core services such as Vault, NATS, Keycloak, Redis, and internal PostgreSQL instances. The installation process creates these PVCs as it installs the services.

* The OpenShift cluster must be able to reach public endpoints and be able to resolve public hostnames. Check the [network requirements](#network-reqs) for more details.

* A PostgreSQL database on major version 16, on release of 16.6 or lower. Versions 16.7 and above are not supported. This database must be dedicated to the ODC runtime stage it is configured for and should not be used for other purposes. While you have full control over the application data, you must not alter the database schema or its underlying structure. Any manipulation of the schema could lead to application malfunction or data loss that OutSystems will not be able to recover or fix.

* An Identity Provider that supports OIDC to manage authentication and authorization.

* An app monitoring (APM) tool compatible with OpenTelemetry to receive logs and traces.

* A load balancer is required to handle incoming traffic and expose the applications running in your self-hosted cluster to end users. For more details on load balancer setup, domain configuration, and TLS termination, see [Configure inbound traffic for applications](sh-domain-config.md).

Once you have the necessary system components in place, you must ensure your infrastructure has the proper network connectivity to support ODC operations.

## Network requirements {#network-reqs}

The Self-hosted ODC setup requires outbound connectivity for ongoing operation, as it communicates with OutSystems cloud services. This ensures your infrastructure remains up-to-date, integrated, and observable.  
Inbound connectivity is only required for end users to access the applications deployed on your OpenShift cluster. A load balancer sits at the edge of the network and facilitates this communication, routing traffic.  
The network requirements allow for zero trust principles. However, you have the flexibility to relax these principles by configuring connectivity rules at the cluster level, allowing all pods to communicate with the listed destinations, if desired.  
The network diagram below highlights the main connectivity requirements for your Self-hosted ODC.

![Diagram showing outbound and inbound TCP connections between the OutSystems cloud and a Self-hosted ODC OpenShift cluster, including namespaces for registry, messaging, monitoring, operator, stage databases, APM, IDP, and the load balancer and admin workstation entry points.](images/sh-network-reqs-diag.png "Network connectivity diagram for Self-hosted ODC")

### Outbound connectivity requirements {#outbound}

The OpenShift cluster requires outbound connectivity to endpoints both inside and outside your self-hosted network.  
Inside your network, you have the databases serving applications on each stage, the IDP service and APM tools.
Outside your network, you have OutSystems cloud services to ensure that your installation remains up-to-date, integrated, and observable. To reach these destinations, the cluster must be able to resolve public hostnames.

<div class="info" markdown="1">

Outbound HTTP/HTTPS traffic from the self-hosted cluster must be direct. Forward proxies between the cluster and any of its required external endpoints aren't supported since proxy traversal can introduce behaviors the platform doesn't account for.

</div>

The following table lists the details of the necessary outbound connectivity from the OpenShift cluster:

| Source | Destination | Protocol and ports | Destination description |
| --- | --- | --- | --- |
| Namespace: `sh-registry` | `*.amazonaws.com` | TCP 443 | OutSystems Cloud container registry |
| Namespace: `self-hosted-operator` | `<your-tenant>.outsystems.dev` | TCP 443 | OutSystems Cloud platform API |
| Namespace: `nats-leaf` | `*.nats.stamp.outsystemscloudrd.net` | TCP 443 | OutSystems Cloud messaging |
| Namespace: `outsystems-otel` | `https://logs-prod-036.grafana.net` <br/>`https://tempo-prod-26-prod-us-east-2.grafana.net` <br/>`https://prometheus-prod-56-prod-us-east-2.grafana.net` | TCP 4317 and 4318 | OutSystems Cloud monitoring platform |
| Namespace: `outsystems-otel` | The address of the APM you manage | TCP 4317 and 4318 | Self-hosted APM |
| Namespace `keycloak-aurora-cluster-1` | The address of the IDP you manage | TCP 443 | Self-hosted IDP |
| Stage namespace | Stage database address defined during setup | TCP 5432 | Self-hosted stage database |
| Namespace: `runtime-services` | All the stage’s database addresses defined during setup | TCP 5432 | Introspection over all self-hosted stage databases |
| Cluster <br/> Admin workstation | public.ecr.aws/m5i8c6m7/ea | TCP 443 | Download Self-hosted configurator |

* **OutSystems Cloud container Registry:** Connecting to this endpoint keeps your self-hosted registry in sync with the OutSystems Cloud. This ensures your services are updated and the latest app versions from the cloud development stage are available locally for deployment.

* **OutSystems Cloud platform API**: Used to authenticate in the Self-hosted configurator when installing or configuring stages. Its destination is the address of your tenant as seen when you access Portal.

* **OutSystems Cloud messaging:** Integrates the messaging systems of your self-hosted installation with their counterparts in the OutSystems Cloud, allowing for message interchange across all components.

* **OutSystems Cloud monitoring platform:** Destination for logs, traces, and metrics generated by your self-hosted ODC services.  These endpoints use Grafana endpoints that don't have a fixed IP address, but Grafana has public DNS lookup services to resolve the hostnames. You could leverage this DNS lookup with your OpenShift network policies to only allow outbound access from your OpenShift cluster to the resolved IPs. This telemetry data is used exclusively by OutSystems to monitor platform health, proactively detect issues, and assist with troubleshooting. OutSystems doesn't collect your end-user data or business-logic data, and doesn't monitor your underlying Kubernetes cluster or hardware infrastructure—these remain entirely under your control.

* **Self-hosted APM:** This is the address of your APM tool of choice and it’s configured during setup [in this step](install-sh.md#setup-configurator). It’s the local destination for logs, traces and metrics generated by your self-hosted ODC apps.

* **Self-hosted IDP:** This is the address of the identity provider (IDP) you manage, used for authentication and authorization services across your apps. Its address is provided to your Self-hosted ODC setup [in this step](install-sh.md#setup-idps).

* **Self-hosted stage database:** Connectivity between the PostgreSQL database and its dedicated stage. Apps in a stage can only access that stage’s database, while the OutSystems services deployed in your cluster can access all stage databases. The database address for each stage is provided to the Self-hosted configurator during setup in [this step](install-sh.md#setup-configurator) and the stage namespaces are returned [just before domain configuration](install-sh.md#configure-domain).

* **Introspection over all self-hosted stage databases:** the database introspection service requires connectivity to all the stage databases to support ODC core functions such as generating database update scripts upon app deployment.

* **Download Self-hosted configurator**: When installing a new self-hosted stage it’s necessary to download the Self-hosted configurator that will run in the cluster. Once the stage is fully installed this connectivity is no longer required.

### Inbound connectivity requirements {#inbound}

While the self-hosted infrastructure primarily requires outbound connectivity, inbound connectivity is necessary for end users to access the apps deployed on your OpenShift cluster. This is handled by a load balancer sitting at the edge of the self-hosted network.

The load balancer must be configured with all the stage's domain certificates necessary to ensure TLS offload, handing off the traffic to the OpenShift cluster via HTTPS or optionally, via HTTP. For more details, refer to [Configure inbound app traffic](sh-domain-config.md).

Another inbound access goes to the Self-hosted configurator during the setup and installation phase. After setup is done, this connectivity is no longer required.

The following table lists the details of the necessary inbound connectivity:

| Source | Destination address | Protocol and ports | Destination description |
| --- | --- | --- | --- |
| Load balancer | Gloo ingress gateway | TCP 443 or 80 | Application traffic |
| Load balancer | IDP address defined during setup | TCP 443 | Self-hosted IDP |
| Admin workstation | OpenShift API server `api.<cluster-domain>` | TCP 6443 | Self-hosted configurator |

* **Application traffic:** The load balancer must ensure traffic is delivered to the Gloo ingress gateway according to the instructions at [Configure inbound traffic for applications](sh-domain-config.md).

* **Self-hosted IDP:** Your identity provider (IDP) used for authentication and authorization services across your apps. Its address is provided to your ODC Self-hosted setup [in this step](install-sh.md#setup-idps).

* **Self-hosted configurator:** During the installation process for each stage, a script is used to install the Self-Hosted configurator that will handle the configuration of ODC on your OpenShift cluster. The script can be run on any Windows, Linux or MacOS machine (admin workstation) and will use the OpenShift CLI to open a connection to OpenShift's API server. This connection will only be necessary during the setup process or when changes are necessary to the configurations done in the Self-Hosted configurator such as the stage database connection details, for example.
