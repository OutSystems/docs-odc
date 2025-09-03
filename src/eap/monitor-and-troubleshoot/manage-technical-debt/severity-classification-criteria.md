---
summary: Detailed severity classification criteria for Code Quality findings across Security, Performance, Maintainability, and Architecture categories in OutSystems Developer Cloud (ODC).
tags: code quality, severity levels, technical debt, security, performance, maintainability, architecture
guid: 7c9d5f2a-8b3e-4d1f-9a2c-3e8f6b7d9c1a
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
coverage-type:
  - understand
  - remember
audience:
  - full stack developers
  - tech leads
  - platform administrators
outsystems-tools:
  - none
figma:
---

# Code quality categories and severity levels

**Code quality** analyzes your code patterns and assigns severity levels to help you prioritize which findings to address first. The severity classification considers multiple factors, including impact scope, likelihood of occurrence, and potential runtime behavior.

**Code quality** evaluates findings across the following categories:

* Security (vulnerabilities and exploits)

* Performance (speed and resource impact)

* Maintainability (code readability and changeability)

* Architecture (design alignment and team autonomy)

Each finding is assigned both a **category** (what type of issue it is) and a **severity level** (how serious that issue is). For example, a finding might be categorized as **Security** with a **High** severity level, or **Performance** with a **Medium** severity level.

## Severity levels

**Critical**- Issues that require immediate attention due to their significant impact on apps and end-users. These findings can affect multiple apps or cause system-wide problems.

**High** - Serious issues that will likely cause noticeable problems in your apps. While not as urgent as critical findings, these should be prioritized in your development cycle.

**Medium** - Issues that may cause problems in certain circumstances or under specific conditions. These findings represent poor practices that should be addressed to prevent future complications.

**Low** - Minor deviations from best practices with minimal immediate impact. While these don't require urgent attention, addressing them helps maintain overall code quality.

## How code quality scores are calculated

**Code quality** assigns an overall score to each app based on the number and severity of findings. The scoring system prioritizes more severe issues and weighs categories differently. Security and performance findings have more impact than architecture and maintainability findings.

Assets receive one of three score classifications:

* **Good** (85-100%) - Apps with minimal technical debt and high code quality standards

* **Needs attention** (50-84%) - Apps with moderate technical debt that should be addressed in upcoming development cycles

* **Poor** (0-49%) - Apps with significant technical debt requiring immediate attention

**Critical findings** have the highest impact on scores. Even a single critical finding can significantly lower an app's score, and multiple critical findings result in a poor score.

**High findings** also substantially impact scores. One high finding can move an app from a good score to needing attention, while, for example, three or more high security findings can result in a poor score.

**Medium findings** can accumulate to affect scores, especially in security and performance categories. A larger number of medium findings can move an app to a poor score.

**Low findings** have minimal impact on the overall score and alone will not result in a poor score. However, they do contribute to the overall assessment of code quality.

**Dismissed findings** are excluded from score calculations, allowing teams to focus on the issues most relevant to their context. Also, score penalties associated with findings already marked as resolved are not removed until a new analysis is run.

## Severity classification criteria

The following tables detail the specific criteria **Code quality** uses to assign severity levels to findings in each category:

## Security

| Severity | Definition |
|----------|------------|
| **Low** | Minor deviation from best practices. While it poses minimal risk now, it should be addressed to prevent potential future vulnerabilities as the app evolves.|
| **Medium** | Poor security practice that does not directly expose a vulnerability.|
| **High** | Confirmed vulnerability with a limited scope or one that requires a hard-to-trigger exploit (for example, passing identity information as a server action parameter). |
| **Critical** | Directly exploitable vulnerability with a broad scope and a low-effort exploit (for example, exposed REST services without authentication, SQL injection).|

## Performance

| Severity | Definition |
|----------|------------|
| **Low** | Inefficient code that has a negligible impact on app performance, even under load. Rarely affects app performance. |
| **Medium** | In some circumstances, may cause noticeable inefficiencies. Under heavy load, it can impact parts of the app. |
| **High** | Always causes noticeable performance issues. May cause timeouts under load and potentially impact other apps.|
| **Critical** | Severe performance bottlenecks that significantly degrade user experience. Affects multiple apps and blocks scalability. |

## Maintainability

| Severity | Definition |
|----------|------------|
| **Low** | Minor readability or style issues. Code can be modified with minimal context. |
| **Medium** | Logic is hard to follow or modify. Requires team-level knowledge to make changes safely. Increases onboarding. |
| **High** | High risk of introducing bugs when making changes. Requires deep knowledge to modify code safely. Significantly slows development iterations. |
| **Critical** | Extremely difficult to change without major refactoring. Affects multiple apps or shared modules, creating development bottlenecks across teams. |

## Architecture

| Severity | Definition |
|----------|------------|
| **Low** | Minor misalignment with architectural guidelines. Limited to isolated features. No impact on other parts of the asset or team workflow.|
| **Medium** | Mixed responsibilities or misplaced logic, but contained within one asset or team. Doesn't affect other assets or teams.|
| **High** | Creates cross-team dependencies or significant code duplication. Affects reusability and team autonomy. Changes in one team can block another. |
| **Critical** | Systemic architectural problems causing widespread cross-team dependencies. Teams can't deploy or evolve independently, leading to slower delivery and quality problems.|
