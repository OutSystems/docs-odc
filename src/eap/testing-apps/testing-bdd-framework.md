---
summary: Explore component testing in ODC using BDDFramework tools for automated testing of Actions and Services.
tags: component testing, automated testing, bddframework, gherkin syntax, api testing
locale: en-us
guid: 6969A397-CC0D-49E5-BF17-C2B71FDB7C91
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/r2zu8cQscEuqfT3j3sfTjm/Testing-Apps?node-id=4601-233
audience:
  - mobile developers
  - frontend developers
  - backend developers
  - full stack developers
outsystems-tools:
  - service studio
  - forge
coverage-type:
  - apply
  - understand
---

# Component testing with BDDFramework tools

This article describes how to install and start using the BDDFramework tools to implement automated and structured component testing. Component testing in OutSystems covers testing **Actions** and exposed **Services** that make up an application's logic.

Component testing in OutSystems includes the following standard test types:

* Unit Tests, which developers maintain, focus on individual units of code or components that a single team owns.
* Integration Tests, which test whether two or more components work together; these touch a broader application scope than unit testing and the tested code usually belongs to two or more teams.
* API Tests, which verify the contract between consumer and provider and the behavior of your application's existing API endpoints.

To start using the BDDFramework tool, install it from the Forge:

* [BDDFramework](https://www.outsystems.com/forge/component-overview/15745/bdd-framework-odc) - The component allows you to test public Server Actions

The tool provide the following features:

* Tests use Gherkin-like syntax and offer a visual representation of test execution.
* You create the test structure using UI Blocks that the tool provides.
* Test code is implemented through actions that are bound to each Block.
* Test Blocks are organized into screens called Test Suites.

## Installing the BDDFramework

You can install BDDFramework tool in your OutSystems infrastructure, just as you would other Forge components. You can also install them directly through ODC Studio or from the online [Forge portal](https://www.outsystems.com/forge/).

1. To install the BDDFramework, log in to **ODC Studio**.
1. Click in **Install from Forge** in your App list screen, you'll be redirected to the ODC Portal.
1. In the ODC Portal Forge screen, type BDDFramework, in the search box.
1. Click **Install**. You'll be prompted a Terms of Use warning, Accept it to carry on with the installation.

Once the installation is complete, it's time to start implementing tests.

## Getting started

The following steps walk through creating a test.

### Create a test application

1. Create an application in ODC Studio.
1. Add **BDD Framework** as a [public element](../building-apps/libraries/use-public-elements.md).
1. Adding the **BDD Framework** as a public element adds BDDFramework capabilities to your app:
    ![ODC Studio interface showing the addition of BDD Framework as a public element.](images/bdd-framework-1-odcs.png "Adding BDD Framework as a public element")
    ![ODC Studio interface displaying BDD Framework capabilities added to the app.](images/bdd-framework-2-odcs.png "BDD Framework capabilities added")

## Add a test

1. On the **Interface** tab menu on the right **Add Screen** to your app.

1. Then you can add a BDDScenario, for example, to your screen:

    ![Menu in ODC Studio with an option to add a new BDD Element to an app.](images/bdd-framework-3-odcs.png "Adding a BDD Scenario to a Screen")

1. This will create a new test scenario:
 
    ![ODC Studio screen with BDD Framework scenario showing the test structure.](images/bdd-framework-4-odcs.png "New scenario added")

    The screen contains a test structure.

1. Start implementing the code for your test. 
  See [Your Complete Guide to BDD Testing in OutSystems](https://www.outsystems.com/blog/posts/bdd-testing/) for more information on creating specific tests.
 