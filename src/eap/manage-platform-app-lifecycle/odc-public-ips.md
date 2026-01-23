---
summary: Securely connect ODC applications to external systems using hostname-based access or whitelist public IPs.
tags: application security, network security, access control
locale: en-us
guid: 2356ff87-f2e9-4ab2-81bf-34ebcffe68c2
app_type: mobile apps, reactive web apps
figma:
platform-version: odc
audience:
  - platform administrators
  - tech leads
  - architects
outsystems-tools:
  - odc portal
coverage-type:
  - remember
  - understand
---

# Allowlisting ODC public IP addresses

Allowlisting is a security mechanism that restricts access to a network or system by only allowing specific IP addresses to connect.

In ODC, you may need to configure allowlisting in the following scenarios:

* [Runtime applications accessing internal resources](#runtime-accessing-internal):

    Your ODC apps may need to call internal APIs, databases, SMTP servers, or other private services. In this case, the recommended approach is to use  [ODC Private Gateway](private-gateway.md). As a fallback option, you may also allowlist the ODC runtime egress IPs in your firewalls or access policies so that these outbound requests are accepted.

* [Streaming observability and audit trails](#streaming-analytics-audit-trail): You can stream [observability data](../monitor-and-troubleshoot/stream-app-analytics/stream-app-analytics-overview.md) to APM tools and [audit trail logs](../monitor-and-troubleshoot/audit-trail/audit-trail-streaming.md) to SIEM tools. To receive them, these tools must expose a reachable ingestion endpoint. You can secure this setup by allowlisting the ODC Data platform egress IPs so only authorized traffic is permitted.

* [Platform unification between O11 and ODC](#platform-unification): For self-managed O11 infrastructures integrating with ODC, the O11 LifeTime must allow inbound connections from ODC. You can secure this setup by allowlisting the ODC Platform egress IPs.

<div class="info" markdown="1">

OutSystems tries to ensure that these IP addresses remain unchanged as much as possible, however, the list of public IPs may change over time due to infrastructure updates, though such changes would be rare and unexpected.
If you want to be informed of any IP address changes, please subscribe to updates to the [OutSystems status page](https://status.outsystems.com/).

</div>

## Runtime applications accessing internal resources {#runtime-accessing-internal}

OutSystems Developer Cloud (ODC) applications often need to connect to external or internal systems, such as APIs or databases. The recommended approaches for securely connecting ODC to private systems are, in order of preference:

1. Through the [ODC Private Gateway](private-gateway.md), which ensures tenant-specific isolation and tighter access control.
1. As a fallback option, using IP allowlisting.

<div class="info" markdown="1">

IP allowlisting can't be applied to:

* [custom code](../building-apps/external-logic/intro.md) that make outbound calls to internal resources.
* Requests from your ODC apps to AWS services (such as S3) that are located in the same region as your ODC tenant.

In these scenarios, the outbound traffic doesn't originate from the shared ODC public IP addresses, and therefore can't be controlled using IP allowlisting. To securely connect custom code to internal systems, you must use the [ODC Private Gateway](private-gateway.md).

</div>

For IP allowlisting, ODC provides a list of public IP addresses that are used to initiate outbound traffic. These can be allowlisted in your firewalls or access policies.

<div class="info" markdown="1">

This method uses shared IP addresses. All apps running on ODC, for all customers, in the same region and stage type will share these IPs. If this model doesn’t meet your security requirements, you should use a Private Gateway.

</div>

### ODC public runtime IP addresses

Use the following lists to configure inbound access from your ODC apps to your systems. Each set of IP addresses corresponds to a specific region and stage type (Development, Non-production, or Production). This allows you to tailor your firewall rules according to your security posture and deployment needs.

For example, you may allowlist only the IPs for the Production stages in your ODC region to restrict access from lower-risk environments. Alternatively, if you want to enable access from all your ODC environments, you can allowlist all stage types for the region of your subscription.

Each region is presented in its own section, review only the ones relevant to your deployment.

#### US East (North Virginia)

| Stage type | IP addresses |
| ----- | ----- |
| Development | 18.233.238.222, 23.22.255.9, 44.205.196.70 |
| Non-production | 3.82.131.249, 44.205.125.101, 44.205.77.32 |
| Production | 3.216.214.63, 44.199.4.230, 44.205.78.121 |

#### Canada (Central)

| Stage type | IP addresses |
| ----- | ----- |
| Development | 52.60.230.211, 3.98.251.18, 15.157.12.129 |
| Non-production | 15.222.221.81, 3.96.85.203, 52.60.209.55 |
| Production | 52.60.54.75, 15.156.196.113, 16.52.19.80 |

#### South America (São Paulo)

| Stage | IP Addresses |
| ----- | ----- |
| Development | 15.229.103.177, 15.229.108.183, 54.233.130.133 |
| Non-production | 54.207.70.193, 54.232.227.39, 54.232.35.188 |
| Production | 177.71.132.163, 54.233.150.19, 18.231.94.114 |

#### Europe (London)

| Stage type | IP addresses |
| ----- | ----- |
| Development | 18.134.51.5, 18.135.141.166, 18.135.43.211 |
| Non-production | 18.133.40.32, 18.168.96.203, 52.56.82.205 |
| Production | 18.134.166.61, 18.168.216.210, 52.56.140.63 |

#### Europe (Ireland)

| Stage type | IP addresses |
| ----- | ----- |
| Development | 176.34.238.77, 54.247.112.214, 52.30.168.24 |
| Non-production | 34.251.61.185, 52.18.84.11, 52.211.9.249 |
| Production | 54.76.0.216, 54.72.139.76, 52.51.220.40 |

#### Europe (Frankfurt)

|Stage type|IP addresses|
|-----|-----|
|Development|3.74.249.67, 3.74.54.131, 52.58.149.36|
|Non-production|3.126.108.4, 3.72.145.236, 3.74.85.23|
|Production|18.157.156.208, 18.197.117.16, 3.74.248.145|

#### South Africa (Cape Town)

| Stage type | IP addresses |
| ----- | ----- |
| Development | 13.246.216.152, 15.240.21.182, 15.240.31.136 |
| Non-production | 13.244.181.185, 13.247.253.92, 16.28.115.21 |
| Production | 13.244.83.19, 13.245.107.229, 15.240.18.88 |

#### Middle East (Tel Aviv)

| Stage | IP Addresses |
| ----- | ----- |
| Development | 51.16.115.71, 51.17.150.144, 51.17.139.151 |
| Non-production | 51.17.146.180, 51.17.116.166, 51.17.10.46 |
| Production | 51.17.144.174, 51.16.151.171, 51.16.223.64 |

#### Middle East (UAE)

| Stage | IP Addresses |
| ----- | ----- |
| Development | 3.29.220.63, 51.112.13.76, 40.172.77.157 |
| Non-production | 3.28.17.159, 3.29.44.203, 40.172.70.114 |
| Production | 51.112.133.114, 51.112.112.13, 3.29.220.101 |

#### Asia Pacific (Mumbai)

| Stage | IP Addresses |
| ----- | ----- |
| Development | 13.127.24.38, 13.200.113.30, 15.206.97.223 |
| Non-production | 13.200.133.20, 13.232.13.75, 15.207.30.181 |
| Production | 13.126.173.147, 15.207.216.212, 65.1.17.83 |

#### Asia Pacific (Singapore)

| Stage type | IP addresses |
| ----- | ----- |
| Development | 13.213.209.98, 13.215.181.79, 52.77.53.62 |
| Non-production | 18.139.252.98, 18.140.120.99, 3.0.140.149 |
| Production | 122.248.255.128, 18.136.137.115, 18.136.156.104 |

#### Asia Pacific (Seoul)

| Stage | IP Addresses |
| ----- | ----- |
| Development | 15.164.44.104, 3.34.18.206, 43.202.177.166 |
| Non-production | 13.125.137.180, 3.36.212.44, 52.78.196.0 |
| Production | 13.209.126.179, 3.37.161.90, 54.180.22.49 |

#### Asia Pacific (Tokyo)

| Stage | IP Addresses |
| ----- | ----- |
| Development | 13.115.101.217, 43.206.9.200, 54.95.243.193 |
| Non-production | 3.114.73.211, 54.65.22.77, 52.68.216.19 |
| Production | 13.113.135.146, 18.177.235.172, 43.206.17.115 |

#### Asia Pacific (Hong Kong)

| Stage | IP Addresses |
| ----- | ----- |
| Development | 95.40.151.52, 18.166.240.189, 18.163.106.244 |
| Non-production | 43.198.188.11, 18.163.17.217, 43.199.52.53 |
| Production | 43.199.192.1, 18.166.231.39, 54.46.28.133 |

#### Asia Pacific (Sydney)

| Stage | IP Addresses |
| ----- | ----- |
| Development | 13.238.188.193, 52.63.132.101, 54.253.21.211 |
| Non-production | 3.105.151.251, 3.24.144.50, 52.64.230.111 |
| Production | 13.237.131.221, 3.24.7.98, 3.24.78.93 |

#### Asia Pacific (Jakarta)

| Stage | IP Addresses |
| ----- | ----- |
| Development | 16.78.243.252, 16.78.98.58, 16.79.11.91 |
| Non-production | 108.137.107.109, 108.137.147.80, 16.78.156.70 |
| Production | 108.137.159.172, 16.79.51.184, 43.218.83.26 |

## Streaming analytics and audit trail data {#streaming-analytics-audit-trail}

ODC can stream data to external monitoring and compliance tools:

* **[Analytics stream](../monitor-and-troubleshoot/stream-app-analytics/stream-app-analytics-overview.md)**: Continuously streams observability data to external application performance monitoring (APM) tools.

* **[Audit trail streaming](../monitor-and-troubleshoot/audit-trail/audit-trail-streaming.md)**: Streams platform audit logs to Security Information and Event Management (SIEM) tools for real-time monitoring and compliance.

Both features use the same ODC Data platform egress IP addresses. When your APM or SIEM tool is hosted in a private network, you must allow inbound access from the ODC Data platform egress IP addresses. To do so, you need to know:

* The region where your ODC tenant is hosted.

* The public IP addresses of the Data platform region that serves your ODC region and the corresponding IP addresses you must allowlist.

The following table lists the Data platform IPs for each customer region. All connections use TCP port 443.

| Customer regions | Data platform region | Data platform IPs |
| --- | --- | --- |
| US East (North Virginia), CA (Canada Central) | US East (North Virginia) | 54.89.107.154, 54.84.58.61, 35.172.177.93 |
| South America (São Paulo) | South America (São Paulo) | 54.94.69.128, 18.229.244.40, 15.229.64.9 |
| Europe (Frankfurt), Europe (London), Middle East (Tel Aviv), Middle East (UAE), South Africa (Cape Town) | Europe (Frankfurt) | 3.73.166.181, 52.59.51.255, 18.194.166.197 |
| Asia Pacific (Singapore), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Hong Kong) | Asia Pacific (Singapore) | 52.76.74.134, 18.143.210.11, 52.74.33.192 |

## Platform unification between O11 and ODC{#platform-unification}

For Platform unification between O11 and ODC, the O11 LifeTime of self-managed infrastructures must allow inbound connections from ODC. Configure your firewall to allow TCP port 443 from the following IP addresses based on your ODC region:

| Region | IP addresses |
| --- | --- |
| US East (North Virginia) | 34.238.16.57, 35.171.116.62, 44.205.76.95 |
| Canada (Central) | 15.156.111.116, 15.157.157.17, 99.79.146.82 |
| South America (São Paulo) | 15.229.160.206, 15.229.178.94, 18.230.53.140 |
| Europe (London) | 13.41.171.86, 18.133.210.215, 3.11.141.71 |
| Europe (Ireland) | 108.128.109.103, 54.72.146.7, 63.34.80.90 |
| Europe (Frankfurt) | 18.156.39.89, 3.72.181.27, 3.74.37.89 |
| South Africa (Cape Town) | 13.247.5.224, 15.240.8.216, 16.28.128.241 |
| Middle East (Tel Aviv) | 51.17.142.29, 51.17.176.86, 51.17.196.54 |
| Middle East (UAE) | 3.29.29.17, 40.172.51.231, 40.172.58.40 |
| Asia Pacific (Mumbai) | 13.200.88.64, 3.111.176.42, 43.204.167.155 |
| Asia Pacific (Singapore) | 13.215.4.92, 13.250.223.227, 13.250.228.210 |
| Asia Pacific (Seoul) | 3.35.244.148, 43.200.195.81, 54.180.169.238 |
| Asia Pacific (Tokyo) | 13.231.89.119, 54.150.81.106, 54.92.69.227 |
| Asia Pacific (Hong Kong) | 16.162.148.223, 16.163.135.72, 43.199.227.110 |
| Asia Pacific (Sydney) | 52.64.237.50, 52.64.66.142, 54.79.135.111 |
| Asia Pacific (Jakarta) | 108.137.120.230, 16.79.9.133, 43.218.208.114 |
