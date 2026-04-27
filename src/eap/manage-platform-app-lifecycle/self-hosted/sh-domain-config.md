---
guid: 9fd76c47-ed85-47e9-94a6-f0582ef04972
locale: en-us
summary: Learn how to configure inbound traffic for your self-hosted ODC environment using a load balancer and the Gloo ingress gateway.
figma: https://www.figma.com/design/la33iciyGndnV5JRqR359g/Managing-OutSystems-platform-and-apps?node-id=4783-317
coverage-type:
  - apply
  - remember
topic:
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - Platform administrator
  - Tech lead
  - Architect
tags: inbound traffic, load balancer configuration, gloo ingress gateway, openshift routing, self-hosted odc networking
outsystems-tools:
  - none
helpids: 30714
---
# Configure inbound app traffic for Self-hosted ODC

After preparing your infrastructure and network, you must configure how inbound traffic reaches your self-hosted applications. This configuration complements the [System and network requirements](sh-install-reqs.md) for Self-hosted ODC, focusing specifically on inbound connectivity: the path that user requests take to reach your apps.

In a Self-hosted ODC deployment, you’re responsible for configuring how external traffic reaches the apps running in your OpenShift cluster. This involves setting up a load balancer and a domain that expose your applications to end users while maintaining secure and reliable routing within your network.

The diagram below illustrates how inbound requests travel from the end user through the load balancer to the Gloo ingress gateway, and finally to the correct stage within your OpenShift cluster.

![Diagram of inbound app traffic where DNS routes test and prod domains to a load balancer, which terminates TLS, adds the X-OSEnvironment header, and forwards requests to the Gloo Edge ingress in an OpenShift cluster, which then routes them to the Test or Production runtime stage namespaces.](images/sh-domain-config-diag.png "Inbound traffic flow through load balancer, Gloo Edge, and OpenShift stages")

Inbound traffic from end users first reaches a load balancer at the edge of your self-hosted network. The load balancer then forwards the requests to the OpenShift cluster, where Gloo serves as the ingress gateway and routing layer. Inside the cluster, Gloo determines which runtime stage (such as Test or Production) should handle the request and forwards it to the corresponding stage namespace.

## Domain and DNS configuration

You must create and manage the DNS domains that resolve to your load balancer. Each application stage must have a unique domain name, for example, `test.apps.example.com` or `prod.apps.example.com`. The DNS records for these domains should point to the public address of your load balancer.

This domain configuration ensures that user requests can reach your load balancer through standard HTTPS connections. Once requests arrive, the load balancer is responsible for forwarding them to the OpenShift cluster for further routing by Gloo.

## Load balancer setup and TLS termination

The load balancer acts as the entry point to your self-hosted cluster. It must be a layer 7 load balancer capable of handling HTTP and HTTPS traffic and performing TLS termination. The domain certificates must be installed at the load balancer to ensure secure HTTPS access for end users.

After terminating TLS, the load balancer forwards the traffic to the Gloo ingress gateway within the OpenShift cluster. This handoff can happen over HTTPS or, if your security policies allow, over HTTP. The load balancer should forward traffic to the appropriate Gloo ingress gateway on port 443 or 80, depending on your chosen configuration.

This approach allows you to offload TLS management to the load balancer while maintaining secure communication with your cluster.

## Routing behavior via X-OSEnvironment header

Within the cluster, Gloo uses the `X-OSEnvironment` HTTP header to determine which runtime stage should receive the request. This header carries a unique stage identifier (UUID) that maps to the target runtime stage. The value for this header is provided at the end of the stage installation process and is displayed in the [installation procedure](install-sh.md#setup-configurator), where you can retrieve it. The load balancer must add the correct value in the `X-OSEnvironment` header based on the request's domain name, since it’s essential to ensure proper traffic routing to the correct stage.

For example, when an inbound request for `prod.apps.example.com` reaches your load balancer, it automatically adds the `X-OSEnvironment` header with the stage UUID value before forwarding the request to Gloo. This allows Gloo to identify the correct runtime stage based on the header value:

```
Host: prod.apps.example.com  
X-OSEnvironment: 123e4567-e89b-12d3-a456-426614174000  
```

Gloo uses the UUID in this header to route the request to the correct stage namespace inside the OpenShift cluster. If the header is missing, Gloo can’t identify which environment should process the request, and routing fails.

The domain address must also be defined in ODC Portal at [this step](install-sh.md#configure-domain) of the installation procedure.
