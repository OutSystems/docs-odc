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

Allowlisting is a security mechanism that restricts access to a network or system by only allowing specific IP addresses to connect. OutSystems Developer Cloud (ODC) applications often need to connect to external or internal systems, such as APIs or databases. The recommended approaches for securely connecting ODC to private systems are, in order of preference:

1. Through the [ODC Private Gateway](private-gateway.md), which ensures tenant-specific isolation and tighter access control.
1. As a fallback option, using IP allowlisting.

<div class="info" markdown="1">

IP allowlisting can't be applied to [custom code](../building-apps/external-logic/intro.md) that make outbound calls to internal resources. In these scenarios, the outbound traffic doesn't originate from the shared ODC public IP addresses, and therefore can't be controlled using IP allowlisting. To securely connect custom code to internal systems, you must use the [ODC Private Gateway](private-gateway.md).

</div>


For IP allowlisting, ODC provides a list of public IP addresses that are used to initiate outbound traffic. These can be allowlisted in your firewalls or access policies.

<div class="info" markdown="1">

This method uses shared IP addresses. All apps running on ODC, for all customers, in the same region and stage type will share these IPs. If this model doesn’t meet your security requirements, you should use a Private Gateway.

OutSystems tries to ensure that these IP addresses remain unchanged as much as possible, however, the list of public IPs may change over time due to infrastructure updates, though such changes are expected to be rare.

</div>


## ODC public IP addresses

Use the following lists to configure inbound access from ODC to your systems. Each set of IP addresses corresponds to a specific region and stage type (Development, Non-production, or Production). This allows you to tailor your firewall rules according to your security posture and deployment needs.

For example, you may allowlist only the IPs for the Production stages in your ODC region to restrict access from lower-risk environments. Alternatively, if you want to enable access from all your ODC environments, you can allowlist all stage types for the region of your subscription.

Each region is presented in its own section, review only the ones relevant to your deployment.


### US East (North Virginia)

| Stage type | IP addresses |
| ----- | ----- |
| Development | 18.233.238.222, 23.22.255.9, 44.205.196.70 |
| Non-production | 3.82.131.249, 44.205.125.101, 44.205.77.32 |
| Production | 3.216.214.63, 44.199.4.230, 44.205.78.121 |

### Canada (Central)

| Stage type | IP addresses |
| ----- | ----- |
| Development | 52.60.230.211, 3.98.251.18, 15.157.12.129 |
| Non-production | 15.222.221.81, 3.96.85.203, 52.60.209.55 |
| Production | 52.60.54.75, 15.156.196.113, 16.52.19.80 |

### South America (São Paulo)

| Stage | IP Addresses |
| ----- | ----- |
| Development | 15.229.103.177, 15.229.108.183, 54.233.130.133 |
| Non-production | 54.207.70.193, 54.232.227.39, 54.232.35.188 |
| Production | 177.71.132.163, 54.233.150.19, 18.231.94.114 |

### Europe (London)

| Stage type | IP addresses |
| ----- | ----- |
| Development | 18.134.51.5, 18.135.141.166, 18.135.43.211 |
| Non-production | 18.133.40.32, 18.168.96.203, 52.56.82.205 |
| Production | 18.134.166.61, 18.168.216.210, 52.56.140.63 |

### Europe (Frankfurt)

| Stage type | IP addresses |
| ----- | ----- |
| Development | 3.74.249.67, 3.74.54.131, 52.58.149.36 |
| Non-production | 3.126.108.4, 3.72.145.236, 3.74.85.23 |
| Production | 18.157.156.208, 18.197.117.16, 3.74.248.145  |

### Middle East (Tel Aviv)

| Stage | IP Addresses |
| ----- | ----- |
| Development | 51.16.115.71, 51.17.150.144, 51.17.139.151 |
| Non-production | 51.17.146.180, 51.17.116.166, 51.17.10.46 |
| Production | 51.17.144.174, 51.16.151.171, 51.16.223.64 |

### Middle East (UAE)

| Stage | IP Addresses |
| ----- | ----- |
| Development | 3.29.220.63, 51.112.13.76, 40.172.77.157 |
| Non-production | 3.28.17.159, 3.29.44.203, 40.172.70.114 |
| Production | 51.112.133.114, 51.112.112.13, 3.29.220.101 |

### Asia Pacific (Mumbai)

| Stage | IP Addresses |
| ----- | ----- |
| Development | 13.127.24.38, 13.200.113.30, 15.206.97.223 |
| Non-production | 13.200.133.20, 13.232.13.75, 15.207.30.181 |
| Production | 13.126.173.147, 15.207.216.212, 65.1.17.83 |

### Asia Pacific (Singapore)

| Stage type | IP addresses |
| ----- | ----- |
| Development | 13.213.209.98, 13.215.181.79, 52.77.53.62 |
| Non-production | 18.139.252.98, 18.140.120.99, 3.0.140.149 |
| Production | 122.248.255.128, 18.136.137.115, 18.136.156.104 |

### Asia Pacific (Seoul)

| Stage | IP Addresses |
| ----- | ----- |
| Development | 15.164.44.104, 3.34.18.206, 43.202.177.166 |
| Non-production | 13.125.137.180, 3.36.212.44, 52.78.196.0 |
| Production | 13.209.126.179, 3.37.161.90, 54.180.22.49 | 

### Asia Pacific (Tokyo)

| Stage | IP Addresses |
| ----- | ----- |
| Development | 13.115.101.217, 43.206.9.200, 54.95.243.193 |
| Non-production | 3.114.73.211, 54.65.22.77, 52.68.216.19 |
| Production | 13.113.135.146, 18.177.235.172, 43.206.17.115 |

### Asia Pacific (Sydney)

| Stage | IP Addresses |
| ----- | ----- |
| Development | 13.238.188.193, 52.63.132.101, 54.253.21.211 |
| Non-production | 3.105.151.251, 3.24.144.50, 52.64.230.111 |
| Production | 13.237.131.221, 3.24.7.98, 3.24.78.93 |
