---
summary: ODC mobile app best practices covering app lifecycle, plugins, data loading, rendering, performance, push notifications, security, and testing.
guid: ccc853ce-b8fa-436e-ab93-33ee6a46127b
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
tags:
  - Best Practices
  - Mobile app
  - Native App
  - Optimization
  - Performance
  - Plugins
  - Security
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
coverage-type:
  - understand
isautopublish: true
---

# Mobile best practices

This section covers best practices for building high-performance mobile apps in OutSystems Developer Cloud (ODC). Mobile apps have specific performance requirements that differ from web apps. Devices have limited processing power, and users may experience variable network connectivity. Following these practices helps you deliver apps that are responsive and provide a smooth user experience.

The following articles cover specific areas of mobile app development:

* [Best practices for app lifecycle, navigation, and deep linking](best-practices-app-lifecycle-navigation.md): Configure the native shell correctly so your app stays responsive to the platform and predictable for users. This article includes recommendations for handling lifecycle transitions, system back navigation, deep links, system bars, and device orientation.

* [Best practices for native integrations and plugins](best-practices-native-plugins.md): Choose and integrate native plugins without compromising your build process or long-term maintenance. This article includes recommendations for selecting OutSystems-supported plugins, managing native dependencies, and avoiding common integration pitfalls.

* [Best practices for loading data on mobile screens](loading-data-mobile.md): Structure your data fetching so screens load as quickly as possible. This article includes recommendations for parallel and asynchronous fetching, request sequencing, and other techniques that minimize loading time and keep the UI responsive.

* [Best practices for rendering data on mobile screens](rendering-data-mobile.md): Make screens feel fast and organized once the data arrives. This article includes recommendations for placeholder images, content prioritization, and list loading strategies that improve how content displays on screen.

* [Best practices for keeping mobile apps responsive](performance-optimization-mobile.md): Keep your app running smoothly on the widest range of devices. This article includes recommendations for reducing data overhead, processing load, and network latency, with particular attention to constraints on low-end devices.

* [Best practices for push notifications](best-practices-push-notifications.md): Deliver reliable push notifications without draining battery or confusing users with mistimed permission prompts. This article includes recommendations for FCM setup, permission timing, token management, and foreground and background handling.

* [Best practices for mobile app security](best-practices-security.md): Protect your app and its data against threats unique to the mobile context. This article includes recommendations for securing data at rest, hardening network communications, and defending against reverse engineering and tampering.

* [Best practices for testing and debugging mobile apps](best-practices-testing-debugging.md): Catch issues early and diagnose problems efficiently across the web layer, the native layer, and the interaction between the two. This article includes recommendations for choosing the right testing and debugging tool for each type of problem.
