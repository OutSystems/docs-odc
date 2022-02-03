---
summary: Overview of the infrastructure architecture of Project Neo.
tags: 
---

# Cloud-native architecture of Project Neo

<div class="info" markdown="1">

Project Neo documentation is under construction. It's frequently updated and expanded. Leave your feedback and help us build the most useful content.

</div>

This article provides an overview of Project Neo's cloud-native architecture.

## Project Neo's cloud-native architecture

Project Neo is cloud-native. This means that the infrastructure of both the development **Platform**, for building and deploying applications, and the independent **Runtime**, for hosting and running the deployed applications, live in the cloud.

### OutSystems cloud platform

In addition to access to **Service Studio**, each customer is granted access to an **OutSystems cloud platform**. This consists of the following:

* Access to the **Project Neo Portal**.
* Access to multi-tenant development **Platform** services.
* A default Runtime setup of three stages: a **Development** stage, a **Test** stage, and a **Production** stage.
* A set of isolated, encrypted, and scalable databases and data stores for the Platform services data.
* An isolated, encrypted, and scalable relational database for each Runtime stage.
* An **Identity Service** to keep [user identities secure](manage-users.md).

The following diagram shows the high-level architecture of the OutSystems cloud platform.

![OutSystems cloud platform](images/infrastructure-architecture-cloud.png)

Each OutSystems cloud platform is isolated by network namespace, ensuring complete network isolation. All internal requests between the Platform and Runtime stages are made over Transport Layer Security (TLS) through NATS, a secure messaging system. All external requests to both the Platform and the Production stage of the Runtime go through a Content Delivery Network (CDN) and Web Application Firewall (WAF).

#### Platform { #platform }

The development **Platform** comprises multiple services, each responsible for specific functions that facilitate the building and deployment of applications. All the Platform services benefit from a resilient microservices design with a web service interface. Developers, DevOps engineers, and architects interact with these services using tools such as Service Studio and the Project Neo Portal.

An example of a service is the Build Service. Triggered by a developer clicking the 1-Click Publish button in Service Studio, the Build Service takes the visual language model developed in Service Studio (.oml file) and turns it into a compiled application to deploy. 

All the Platform services are multi-tenant and benefit from automatic recoveries and continuous upgrades.

The following diagram shows the high-level architecture of the development Platform.

![Platform](images/infrastructure-architecture-platform.png) 

#### Runtime { #runtime }

In Project Neo, the **Runtime** is independent of the Platform and comprises multiple **stages**, each independent of the other, that serve to host and run the deployed applications. The default Runtime setup is a Development stage, a Test stage, and a Production stage. Staging lets multiple teams deliver independently and in parallel, a foundational part of the **continuous integration** approach to software development.

The following diagram shows the high-level architecture of the Runtime. This diagram represents the Production stage with users connecting.

![Runtime](images/infrastructure-architecture-runtime.png) 

## Key technologies of the cloud-native infrastructure

The following is an overview of the best-in-class cloud technologies that Project Neo uses.

### Kubernetes

The core of both the Platform and each of the Runtime stages is the **Kubernetes cluster**. 

Powered by AWS Elastic Kubernetes Service (EKS), the Platform and each of the Runtime stages use a cluster: an isolated, scalable, and self-healing compute capacity. 

#### Platform cluster

For the Platform, each service creates one or more jobs in the Platform cluster to process. For example, for the Build Service, these jobs would include generating the compiled code from the OutSystems visual language model (.oml file), optimizing the compiled code, and then generating the compiled application. Jobs are finite tasks running in the Platform cluster that facilitate the building and deployment of applications (_Job 1 Job 2 Job 3 (...) Job N_ in the [Platform diagram](#platform)). The Platform cluster compute capacity is scalable, which means multiple developers can use the Build Service or any other service concurrently without any performance degradation of the Platform. This lets multiple teams rapidly scale the development process independently of the deployed applications.

#### Runtime cluster

**Applications** run in each cluster of each of the Runtime stages (_App 1 App 2 App 3 (...) App N_ in the [Runtime diagram](#runtime), this happens to be the Production stage). 

To run on a Kubernetes cluster, applications are packaged into a **container**—a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries, and settings.<sup>[[1]](https://www.docker.com/resources/what-container)</sup> In the example of the Build Service jobs in the previous section, the compiled application generated is a **container image**. An instance of a container image is a container.

Each application is packaged into a separate container, making the infrastructure resilient to individual resource-intensive application(s) that degrade the performance of other applications.

Application containers running in the Production stage cluster are replicated across multiple availability zones (AZs) to ensure **high availability (HA)** for applications running in production. 

### Databases and data stores

#### Platform data

Service Studio and Project Neo Portal connect to the Platform API Gateway, which handles all the requests to the Platform services. Each service creates one or more jobs for the cluster to process, which make calls to the databases and data stores through the Data Service service—think of this as a data access layer. 

The following table lists and describes the Platform databases and data stores.

| Data stored | Service used | Service description (via AWS) | Availability |
| - | - | - | - |
| Application version and dependency information. | Amazon Aurora | A PostgreSQL-compatible relational database built for the cloud. | HA by default (Aurora Serverless). High data durability by default (Aurora Serverless). |
| Current and historic application revisions, in the form of .oml files, stored as blob data. | S3 | An object storage service offering industry-leading scalability, data availability, security, and performance. | HA by default. |
| Configuration and metadata from the Platform Build Service. | DynamoDB | A fully managed, serverless, key-value NoSQL database designed to run high-performance applications at any scale. | HA by default. |
| Current and historic application container images. | Elastic Container Registry (ECR) | A fully-managed Docker container registry that makes it easy to store, share, and deploy container images. | HA by default. |

#### Runtime data

Each Runtime stage has an isolated Amazon Aurora database that scales for both compute and storage and has High Availability through replication across multiple AZs. High data durability is ensured through data replication across multiple AZs.

#### Platform to Runtime

In addition to storing the application container image in the Elastic Container Registry (ECR), the Build Service passes it to the Application Deployment service on the specified Runtime stage for deployment. The Application Deployment service coordinates the deployment of the application container to the cluster.

The idea of "Build once, deploy anywhere"—the build process not making strong assumptions about the environment the application is to be deployed into—is a foundational part of the **continuous delivery** approach to software development.

## Logging, monitoring, and analytics

Logs and metrics are collected from each of the application containers running in each Runtime stage cluster. Logs can be filtered on the Project Neo Portal between a user-defined time range and with a text search that uses Elasticsearch capabilities.

Automatic monitoring by EKS replaces unhealthy application containers running in each Runtime stage cluster with a replica.

Site Reliability Engineering on the Platform is supported by automated monitoring.
