---
guid: 9fd76c47-ed85-47e9-94a6-f0582ef04972
locale: en-us
summary: Learn how to configure inbound traffic for your self-hosted ODC environment using a load balancer and the Gloo ingress gateway.
figma: https://www.figma.com/design/la33iciyGndnV5JRqR359g/Managing-OutSystems-platform-and-apps?node-id=4783-317
coverage-type:
  - remember
  - understand
  - apply
topic:
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - Platform administrator
  - Tech lead
  - Architect
tags:
  - Domains
  - Infrastructure
  - Security
outsystems-tools:
  - none
helpids: 30714
isautopublish: true
---
# Configure inbound app traffic for Self-hosted ODC

After preparing your infrastructure and network, you must configure how inbound traffic reaches your self-hosted applications. This configuration complements the [System and network requirements](sh-install-reqs.md) for Self-hosted ODC, focusing specifically on inbound connectivity: the path that user requests take to reach your apps.

In a Self-hosted ODC deployment, you’re responsible for configuring how external traffic reaches the apps running in your cluster. This involves setting up a load balancer and a domain that expose your applications to end users while maintaining secure and reliable routing within your network.

The diagram below illustrates how inbound requests travel from the end user through the load balancer to the Gloo ingress gateway, and finally to the correct stage within your cluster.

![Diagram of inbound app traffic where DNS routes test and prod domains to a load balancer, which terminates TLS, adds the X-OSEnvironment header, and forwards requests to the Gloo Edge ingress in a self-hosted cluster, which then routes them to the Test or Production runtime stage namespaces.](images/sh-domain-config-diag.png "Inbound traffic flow through load balancer, Gloo Edge, and self-hosted cluster stages")

Inbound traffic from end users first reaches a load balancer at the edge of your self-hosted network. The load balancer then forwards the requests to the cluster, where Gloo serves as the ingress gateway and routing layer. Inside the cluster, Gloo determines which runtime stage (such as Test or Production) should handle the request and forwards it to the corresponding stage namespace.

## Domain and DNS configuration

You must create and manage the DNS domains that resolve to your load balancer. Each application stage must have a unique domain name, for example, `test.apps.example.com` or `prod.apps.example.com`. The DNS records for these domains should point to the public address of your load balancer.

This domain configuration ensures that user requests can reach your load balancer through standard HTTPS connections. Once requests arrive, the load balancer is responsible for forwarding them to the cluster for further routing by Gloo.

## Load balancer setup and TLS termination

The load balancer acts as the entry point to your self-hosted cluster. It must be a layer 7 load balancer capable of handling HTTP and HTTPS traffic and performing TLS termination. The domain certificates must be installed at the load balancer to ensure secure HTTPS access for end users.

After terminating TLS, the load balancer forwards the traffic to the Gloo ingress gateway within the cluster over HTTP. Configure your load balancer to forward to the port on which you expose the Gloo ingress service in your cluster. This is the NodePort or service port you assign when exposing Gloo — it is not a fixed platform port.

This approach allows you to offload TLS management to the load balancer while maintaining secure communication with your cluster. You must also configure the required routing headers described in [Required routing headers](#required-routing-headers).

## Required routing headers {#required-routing-headers}

Within the cluster, Gloo uses the `X-OSEnvironment` HTTP header to determine which runtime stage should receive the request. This header carries a unique stage identifier (UUID) that maps to the target runtime stage. The UUID is provided at the end of the stage installation process and is displayed in the [installation procedure](install-sh.md#setup-configurator).

For example, a request for `prod.apps.example.com` must carry the following headers when it reaches Gloo:

```
X-Forwarded-Host: prod.apps.example.com
X-OSEnvironment: 123e4567-e89b-12d3-a456-426614174000
```

`X-Forwarded-Host` must carry the entry point domain [configured for the stage in ODC Portal](install-sh.md#configure-domain). `X-OSEnvironment` must carry the stage UUID. If either header is missing, Gloo can’t identify the target stage and routing fails.

These headers are typically set by your load balancer based on the request’s domain name, but any proxy upstream of Gloo, such as a CDN or WAF, can set them as long as they are present when the request arrives.
