---
summary: Overview of the infrastructure architecture of Project Neo.
tags: 
locale: en-us
guid: 9a0cb62a-f11b-4d1a-9e79-0ca7d398e57b
app_type: mobile apps, reactive web apps
---

# Cloud-native architecture of Project Neo

<div class="info" markdown="1">

Project Neo documentation is under construction. It's frequently updated and expanded.

</div>

Project Neo is cloud-native. This means that the infrastructure of both the development **Platform**, for building and deploying apps, and the independent **Runtime**, for hosting and running the deployed apps, live in the cloud.

## OutSystems cloud platform

In addition to access to **Service Studio**, each Project Neo customer has access to an **OutSystems cloud platform**. This consists of the following:

* Access to the [**Project Neo Portal**](../neo-differences.md#neo-portal).
* Access to multi-tenant development **Platform** services.
* A default Runtime setup of three stages: a **Development** stage, a **Test** stage, and a **Production** stage.
* A set of isolated, encrypted, and scalable databases and data stores for the Platform services data.
* An isolated, encrypted, and scalable relational database for each Runtime stage.
* An **Identity Service** to keep [user identities secure](../manage-users.md).

The following diagram shows the high-level architecture of the OutSystems cloud platform.

![Architecture of the OutSystems cloud platform](images/cloud-architecture-diag.png "Architecture of the OutSystems cloud platform")

 NATS, a secure messaging system, handles all internal requests between the Platform and Runtime stages. All external requests to both the Platform and each of the Runtime stages go through a Content Delivery Network (CDN) and Web Application Firewall (WAF). All internal and external requests are encrypted using Transport Layer Security (TLS). See [Cloud-native network architecture and security of Project Neo](networking.md) to learn more.

#### Platform { #platform }

The development **Platform** comprises multiple services, each responsible for specific functions that facilitate the building and deployment of apps. All the Platform services benefit from a resilient microservices design with a REST API web service interface. Developers, DevOps engineers, and architects interact with these services using tools such as Service Studio and the Project Neo Portal. 

The Platform **Load Balancer** handles all requests to the services. 

An example of a service is the Build Service. Triggered by a developer clicking the 1-Click Publish in Service Studio, the Build Service takes the visual language model (.oml file) and compiles it to a deployable app. 

All the Platform services are multi-tenant and benefit from automatic recovery and continuous upgrades.

The following diagram shows the high-level architecture of the development Platform.

![Architecture of the development Platform](images/cloud-architecture-platform-diag.png "Architecture of the development Platform") 

#### Runtime { #runtime }

In Project Neo, the **Runtime** is independent of the Platform and comprises multiple **stages**, each independent of the other, that serve to host and run the deployed apps. The default Runtime setup is a Development stage, a Test stage, and a Production stage. Staging lets multiple teams deliver independently and in parallel, a foundational part of the **continuous integration** approach to software development.

The Runtime **Load Balancer** handles all requests to the apps.

The following diagram shows the high-level Runtime architecture.

![Runtime architecture](images/cloud-architecture-runtime-diag.png "Runtime architecture") 

## Key technologies of the cloud-native infrastructure

The following is an overview of the cloud technologies used by Project Neo.

### Kubernetes

The core of both the Platform and each of the Runtime stages is the **Kubernetes cluster**. 

Powered by AWS Elastic Kubernetes Service (EKS), the Platform and each of the Runtime stages use a cluster: an isolated, scalable, and self-healing compute capacity. 

#### Platform cluster { #platform-cluster }

To run on a Kubernetes cluster, each Platform service into packaged into a **container**. A container is a lightweight, standalone, executable software package. It includes everything the app needs to run: code, runtime, system tools, system libraries, and settings. 

##### Auto scaling

The compute capacity for each running Platform service is scalable. Many developers can use the Build Service or any other service concurrently without any performance degradation of the Platform. This lets multiple teams rapidly scale the development process independently of the deployed apps.

The following diagram shows how auto scaling works inside the Platform cluster.

![Autoscaling of the development Platform](images/cloud-architecture-platform-k8s-diag.png "Autoscaling of the development Platform") 

The **auto scale controller** monitors the CPU and RAM metrics of each running service. It continuously checks these metrics against the cluster compute capacity allocated to each service. It can:

* Replicate the running service to optimize the use of the allocated compute capacity.
* Allocate additional cluster compute capacity to the running service if the CPU and RAM metrics for the service exceed a threshold.

The auto scale controller makes the adjustment in real time, with no user interaction required.

The isolated Platform cluster resources its overall compute capacity from a multi-tenant pool. This means it's scalable.

#### Runtime cluster

In the example of the Build Service in the [previous section](#platform), the compiled app generated is a **container image**. An instance of a container image is a container.

The Build Service packages each app into a separate container, making the infrastructure resilient to individual resource-intensive app(s) that degrade the performance of other apps.

The auto scale controller replicates app containers running in each cluster of each of the Runtime stages across multiple availability zones (AZs) to ensure **high availability (HA)**.

##### Auto scaling

The compute capacity for each app container running in each Runtime stage is scalable. This lets each app scale independently.

The following diagram illustrates how auto scaling works inside the Runtime cluster.

![Autoscaling of the runtime apps](images/cloud-architecture-runtime-scale-diag.png "Autoscaling of the runtime apps") 

The **auto scale controller** monitors the CPU and RAM metrics of each app container. It continuously checks these metrics against the cluster compute capacity allocated to each app container. It can: 

* Replicate the app container to optimize the use of the allocated compute capacity and distribution across AZs.
* Allocate additional cluster compute capacity to the app container if the CPU and RAM metrics for the app container exceed a threshold.

The auto scale controller makes the adjustment in real time, with no user interaction required.

The overall compute capacity for the isolated Runtime stage cluster is scalable because it's resourced from a multi-tenant pool.

### Databases and data stores

#### Platform data

Each Platform service makes calls to the databases and data stores.

The following table describes the Platform databases and data stores.

| Data Stored | Service Used | Service Description | Availability |
| - | - | - | - |
| App revisions and dependency information. | Amazon Aurora | A PostgreSQL-compatible relational database built for the cloud. | High availability and high data durability by default (Aurora Serverless). |
| Current and historic app revisions, in the form of .oml files, stored as blob data. | S3 | An object storage service offering industry-leading scalability, data availability, security, and performance. | HA by default. |
| Configuration and metadata from the Platform Build Service. | DynamoDB | A fully managed, serverless, key-value NoSQL database designed to run high-performance apps at any scale. | HA by default. |
| Current and historic app container images. | Elastic Container Registry (ECR) | A fully-managed Docker container registry that makes it easy to store, share, and deploy container images. | HA by default. |

#### Runtime data

Each Runtime stage has an isolated Amazon Aurora database that scales for both compute and storage and has HA through instance replication across multiple AZs. The database replicates data across multiple AZs, ensuring high data durability.

The following diagram shows how the database achieves this.

![Database autoscaling](images/cloud-architecture-db-scale-diag.png "Database autoscaling") 

The Amazon Aurora database architecture model decouples compute and storage.

Cluster storage volumes automatically scale as the amount of data stored increases.

#### Platform to Runtime

Build Service stores the app container image and passes the image to a Runtime stage for deployment. OutSystems follows the "Build once, deploy anywhere" **continuous delivery** principle, which makes Project Neo an efficient cloud product.

## Logging, monitoring, and analytics

The auto-scale controller collects logs and metrics from each of the app containers running in each Runtime stage cluster. Developers and DevOps engineers can filter logs on the Project Neo Portal.

Automatic monitoring by EKS replaces unhealthy app containers running in each Runtime stage cluster with a replica.

Automated monitoring supports Site Reliability Engineering (SRE) on the Platform.