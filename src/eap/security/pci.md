---
guid: ed54cb24-49f0-41f5-b1af-f8c081d526ed
locale: en-us
summary: Ensure PCI compliance with OutSystems Developer Cloud (ODC) by using secure payment gateways, iFrame, URL redirection, and tokenization.
figma: 
coverage-type:
  - understand
  - apply
topic:
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - architects
  - tech leads
tags: pci compliance,payment gateways,tokenization,security
outsystems-tools:
  - odc portal
  - odc studio
helpids: 
---

# PCI compliance with ODC

The PCI (Payment Card Industry) Security Standards Council aims to help secure payments worldwide. This council is also responsible for ensuring that organizations meet the requirements through validation and certification.

[Sentry for ODC](https://www.outsystems.com/low-code-platform/security/sentry/) (OutSystems Developer Cloud) provides PCI compliance. ODC Sentry is compliant with PCI DSS SAQ D service provider standards.

To comply with PCI eData Security Standard (DSS), companies processing credit card data must ensure that cardholder data is safe.

You can ensure the compliance of your applications with PCI DSS by delegating credit card payments to a 3rd party PCI-compliant payment gateway using one of the following methods:

* **URL Redirection**:  When users are ready to make a payment on your website, they’re redirected to the PCI DSS compliant Service Provider's secure payment page. Payment information is entered directly on the secure payment page hosted by the payment gateway. After the payment is processed, the user may be redirected to your website for confirmation or to complete the transaction.  

* **iFrame Integration**:  Use an iFrame integration, where the payment form is embedded within an iFrame on your website. The actual payment data is entered into the PCI DSS-compliant provider's site, reducing your exposure to sensitive information.

If you need more control over the payment process, you can use tokenization, where sensitive cardholder data is replaced with a unique token. This token can be used for transactions without exposing the actual card data. By using tokenization, you have a few additional options available:

* **Direct Post Method**: Employ a direct post method where the payment form is hosted on the PCI DSS Service Provider's infrastructure. The sensitive data is posted directly to the service provider’s servers, bypassing your application systems.  

* **Secure APIs**: Use secure APIs provided by your service provider to transmit and receive payment data securely.

You should always ensure that no payment card information is ever stored or processed in OutSystems applications. For more details on the supported integration options, refer to your PCI DSS-certified processor.

[Sentry for ODC](https://www.outsystems.com/low-code-platform/security/sentry/) ensures your ODC usage is PCI compliant. In accordance with the [OutSystems Cloud shared responsibility model](https://www.outsystems.com/tk/redirect?g=b04339ce-7b9f-4c93-94b7-e4cf397eab47), apps should be designed to meet PCI guidance, and a third-party audit may be required to ensure apps are PCI compliant. To confirm that you're using ODC Sentry, check your [Subscription console](../manage-platform-app-lifecycle/subscription-console.md). Contact your account manager for assistance.
