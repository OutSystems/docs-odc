---
summary: Manage technical debt and enhance code quality in OutSystems Developer Cloud (ODC) using Code Quality powered by Mentor for optimal performance, maintainability, and security.
tags: code quality, technical debt, mentor, code analysis, outsystems development cloud
guid: 6be15662-74c5-4c35-9a7d-16a28816614c
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/IStE4rx9SlrBLEK5OXk4nm/Monitor-and-troubleshoot-apps?node-id=3522-10
coverage-type:
  - understand
audience:
  - full stack developers
  - tech leads
outsystems-tools:
  - none
---
# Manage technical debt in ODC

**Code quality**, powered by Mentor, is an OutSystems Developer Cloud (ODC) solution to help improve your team's code quality and manage technical debt. Managing your technical debt increases your team's agility and productivity while lowering the maintenance costs of developing your apps.

**Code quality** analyzes your code against established best practices and coding patterns. It scans your apps for potential issues in four key areas: security vulnerabilities, performance problems, maintainability concerns, and architecture patterns. When the analysis is complete, it provides a detailed report showing specific findings with guidance on how to fix them.

You can use **Code quality** to:

* **Get strategic visibility** into code quality trends and technical debt distribution across your organization.

* **Access detailed findings** with specific guidance and direct navigation to problem areas in ODC Studio.

* **Proactively identify and prioritize** common issues across your organization's apps to prevent future occurrences and improve overall quality.

* **Track progress** over time and measure the effectiveness of your improvement efforts.

## Code analysis

**Code quality** analyzes your apps and identifies potential issues that could impact your code quality. The analysis runs regularly and examines your code against established best practices in four key areas:

* **Performance** - Issues that could slow down your apps or consume excessive resources
* **Architecture** - Patterns that could affect code organization and maintainability  
* **Maintainability** - Problems that make code harder to read, modify, or extend
* **Security** - Vulnerabilities that could expose your apps to security risks

When **Code quality** identifies issues, it creates findings - specific instances where your code deviates from recommended patterns. Each finding provides details about the problem and actionable guidance on how to fix it.

For more information about findings, refer to [Working with Code quality](working-with-code-quality.md#investigate-specific-findings).

## Code quality in the software development lifecycle

Both developers and technical leads use **Code quality** during the development phase. Developers fix technical debt before apps move to the testing phase. Technical leads identify improvement areas and common pitfalls, allowing them to grow their teams' proficiency.

## For technical leads

As a technical lead, you can view code quality metrics across your team's apps. This shows you the current state of technical debt, which apps have the most issues, and what types of problems are most common.

Furthermore, **Code quality** helps you scale by providing your developers with an automated code review. This promotes autonomy for your developers, by helping them deliver better code before you do a formal code review. **Code quality** also provides relevant context on the coding issues, helping them grow their OutSystems knowledge.

![Dashboard showing code quality metrics for technical leads, including managing technical debt and mitigating security risks.](images/overview-tl.png "Overview for Technical Leads")

For more information, refer to [Getting started with Code quality as a technical lead](getting-started-aims-tl.md).

## For developers

As a developer, you typically use **Code quality** for automated code reviews. It identifies specific parts of your code that may need changes to reduce technical debt and mitigate security concerns.

This review includes guidance and best practices for the issues it finds, helping you grow your OutSystems knowledge as you deliver value to your organization.

![Dashboard showing code quality metrics for developers, including automated code review and fostering developer growth.](images/overview-dev.png "Overview for Developers")

For more information, refer to [Getting started with Code quality as a developer](getting-started-aims-dev.md).

## Related resources

* [Working with Code quality](working-with-code-quality.md)
* [Setting up Code quality](how-does-aims-works.md)
