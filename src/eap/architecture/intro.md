---
summary: OutSystems Developer Cloud is a cloud-native platform with multi-tenant services, isolated databases, and auto-scaling clusters for both the Platform and Runtime stages.
tags: 
locale: en-us
guid: 9a0cb62a-f11b-4d1a-9e79-0ca7d398e57b
app_type: mobile apps, reactive web apps
platform-version: odc
---

# Cloud-native architecture of OutSystems Developer Cloud

OutSystems Developer Cloud (ODC) is cloud-native. This means that the infrastructure of both the development **Platform**, for building and deploying apps, and the independent **Runtime**, for hosting and running the deployed apps, is built and deployed in the cloud. See [What Is Cloud Native?](https://www.outsystems.com/glossary/what-is-cloud-native/) for more information.

## OutSystems Developer Cloud

In addition to access to **ODC Studio** and [**ODC Portal**](../differences-o11/intro.md#ODC-portal), each OutSystems Developer Cloud customer has:

* Access to multi-tenant development **Platform** services.
* A standard Runtime setup of three isolated and independent stages: **Development**, **Test**, and **Production**.
* A set of isolated, encrypted, and scalable databases and data stores for the Platform services data. Secret data such as API keys are stored in a secret manager.
* An isolated, encrypted, and scalable relational database for each Runtime stage. 
* A built-in **Identity Service** to keep [user identities secure](identity.md).

The following diagram shows the high-level architecture of the OutSystems Developer Cloud.

![Architecture of the OutSystems cloud platform](images/architecture-diag.png "Architecture of the OutSystems cloud platform")

 NATS (Neural Autonomic Transport System), a secure messaging system, handles all internal requests between the Platform and Runtime stages. All external requests to both the Platform and each of the Runtime stages go through a Content Delivery Network (CDN) and Web Application Firewall (WAF). All internal and external requests are encrypted using Transport Layer Security (TLS). See [Cloud-native network architecture and security of OutSystems Developer Cloud](networking.md) to learn more.

#### Platform { #platform }

The development **Platform** comprises multiple services, each responsible for specific functions that facilitate the building and deployment of apps. All the Platform services benefit from a resilient microservices design with a REST API web service interface. Developers, DevOps engineers, and architects interact with these services using ODC Studio and ODC Portal. 

The Platform **Load Balancer** handles all requests to the services. 

An example of a service is the Build Service. When developers click the 1-Click Publish button in ODC Studio, the Build Service takes the OutSystems visual language model (OML project) and compiles it into a deployable app.

All the Platform services are multi-tenant and benefit from automatic recovery and continuous upgrades.

The following diagram shows the high-level architecture of the development Platform.

![Architecture of the development Platform](images/architecture-platform-diag.png "Architecture of the development Platform") 

#### Runtime { #runtime }

In OutSystems Developer Cloud, the **Runtime** is independent of the Platform and comprises multiple **stages**, each independent of the other, that serve to host and run the deployed apps. The standard Runtime setup is a Development stage, a Test stage, and a Production stage. Staging lets multiple teams deliver independently and in parallel, a foundational part of the **continuous integration** approach to software development.

The Runtime **Load Balancer** handles all requests to the apps.

The following diagram shows the high-level Runtime architecture.

![Runtime architecture](images/architecture-runtime-diag.png "Runtime architecture") 

## Key technologies of the cloud-native infrastructure

The following is an overview of the cloud technologies used by OutSystems Developer Cloud.

### Kubernetes

The core of both the Platform and each of the Runtime stages is the **Kubernetes cluster**. 

Powered by AWS Elastic Kubernetes Service (EKS), the Platform and each of the Runtime stages use a cluster: an isolated, scalable, and self-healing compute capacity. 

#### Platform cluster { #platform-cluster }

To run on a Kubernetes cluster, each Platform service is packaged into a **container**. A container is a lightweight, standalone, executable software package. It includes everything the app needs to run: code, runtime, system tools, system libraries, and settings. See [Security in OutSystems Developer Cloud](../security.md#containers) for more information about container security.

##### Auto scaling

The compute capacity for each running Platform service is scalable. Many developers can use the Build Service or any other service concurrently without any performance degradation of the Platform. This lets multiple teams rapidly scale the development process independently of the deployed apps.

The following diagram shows how auto scaling works inside the Platform cluster.

![Autoscaling of the development Platform](images/architecture-platform-k8s-diag.png "Autoscaling of the development Platform") 

The **auto scale controller** monitors the CPU and RAM usage of each running service. It continuously checks the usage against the cluster compute capacity allocated and allocates additional capacity if the CPU and RAM usage exceeds a defined threshold.

The auto scale controller makes the adjustment in real time, with no user interaction required.

The isolated Platform cluster resources its overall compute capacity from a multi-tenant pool. This means it's scalable.

#### Runtime cluster

In the example of the Build Service in the [previous section](#platform), the compiled app generated is a **container image**. An instance of a container image is a container. See [Security in OutSystems Developer Cloud](../security.md#containers) for more information about container security.

The Build Service packages each container image into a separate container, making the infrastructure resilient to individual resource-intensive app(s) that degrade the performance of other apps.

The auto scale controller replicates app containers running in each cluster of each of the Runtime stages across multiple availability zones to ensure **high availability (HA)**. An availability zone is a distinct location in the cloud that's engineered to be isolated from failure.

##### Auto scaling

The compute capacity for each app container running in each non-Development Runtime stage is scalable. This lets each app scale independently.

The following diagram illustrates how auto scaling works inside the Runtime cluster.

![Autoscaling of the runtime apps](images/architecture-runtime-scale-diag.png "Autoscaling of the runtime apps") 

The **auto scale controller** monitors the CPU and RAM usage of each app container. It continuously checks the usage against the cluster compute capacity allocated and allocates additional capacity if the CPU and RAM usage exceeds a defined threshold.

The auto scale controller makes the adjustment in real time, with no user interaction required.

The overall compute capacity for the isolated Runtime stage cluster is scalable because it's resourced from a multi-tenant pool.

### Databases and data stores

#### Platform data

Each Platform service makes calls to the databases and data stores.

The following table describes the Platform databases and data stores.

| Data Stored | Service Used | Service Description | Availability |
| - | - | - | - |
| App revisions and dependency information. | Amazon Aurora | A PostgreSQL-compatible relational database built for the cloud. | High availability (HA) by default (Aurora Serverless). |
| Current and historic app revisions, in the form of OML projects, stored as blob data. | S3 | An object storage service offering industry-leading scalability, data availability, security, and performance. | HA by default. |
| Configuration and metadata from the Platform Build Service. | DynamoDB | A fully managed, serverless, key-value NoSQL database designed to run high-performance apps at any scale. | HA by default. |
| Current and historic app container images. | Elastic Container Registry (ECR) | A fully-managed Docker container registry that makes it easy to store, share, and deploy container images. | HA by default. |

#### Runtime data

Each Runtime stage has an isolated Amazon Aurora Serverless database. The database for the Production stage is high-availability by default. The following diagram shows this.

![Runtime Production stage database](images/architecture-runtime-data-diag.png "Runtime Production stage database") 

Data is automatically written to three availability zones simultaneously.

The Amazon Aurora database architecture model decouples compute and storage. Storage volume automatically scales as the amount of data stored increases.

You can store secret data for your apps such as API keys as secret settings in a secret manager.

#### Platform to Runtime

Build Service stores the app container image and passes the image to a Runtime stage for deployment. OutSystems follows the "Build once, deploy anywhere" **continuous delivery** principle, which makes OutSystems Developer Cloud an efficient cloud product.

## Logging, monitoring, and analytics { #logging-monitoring-analytics }

Logs and metrics are collected from each of the app containers running in each Runtime stage cluster. Developers and DevOps engineers can filter logs on ODC Portal.

Automatic monitoring by EKS replaces unhealthy app containers running in each Runtime stage cluster with a healthy replica. An app container is unhealthy if it's continuously unresponsive.

See [Security in OutSystems Developer Cloud](../security.md#monitoring-and-support) for more information about monitoring and support in ODC.
