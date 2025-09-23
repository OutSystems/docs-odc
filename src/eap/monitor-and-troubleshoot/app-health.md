---
summary: OutSystems Developer Cloud (ODC) features an App health dashboard for monitoring and analyzing app performance metrics.
tags: performance monitoring, app health analysis, dashboard usage, error debugging, app performance metrics
locale: en-us
guid: e190d5fb-6b99-4d9b-a64f-a3b34be3588d
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/IStE4rx9SlrBLEK5OXk4nm/Monitor-apps?type=design&node-id=3202%3A36&mode=design&t=tBANF8iUm5epKReC-1
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc portal
coverage-type:
  - understand
  - remember
---

# Monitor analytics in the ODC Portal

<div class="info" markdown="1">

This functionality uses the Data platform, which may process data outside your ODC organization region to provide its capabilities. For more information, refer to [Data platform](../manage-platform-app-lifecycle/platform-architecture/intro.md#data-platform).

</div>

OutSystems Developer Cloud (ODC) provides an analytics dashboard that monitors apps based on performance, usage, and errors.

The dashboard shows the following key metrics:

* Health score: How your apps perform, considering response times, successful requests, errors, and etc.
* Top apps by usage: A list of apps with the most users and requests per day.
* Requests: The total usage of your apps in the number of requests and their rates.
* Errors: The amount of errors and the error rate for all requests.
* Response time: The time the server takes to handle a request.
* Top AI models by request: Detailed metrics for a selected AI model.
* Top agents by request: Detailed metrics for a selected agent.

Based on the health score, the dashboard organizes the apps into **Critical**, **Moderate**, and **Good** categories, allowing you to focus on the poorly performing apps. You can identify and debug potential issues from the dashboard by drilling down into the app's historical trend of key metrics.

The analytics dashboard provides an overview of the apps of a selected stage for up to 30 days. You can click the graphs for metrics such as errors, response time, and requests to view detailed information.

![Screenshot of selecting a specific metric in ODC analytics.](images/specific-metirc-pl.png "Selecting a Specific Metric in ODC Analytics")

## App analytics

You can drill down into specific apps to get more information about how the app behaves.

![Screenshot of selecting a specific app in ODC analytics.](images/select-app-pl.png "Selecting a Specific App in ODC analytics")

For each app, the analytics dashboard provides insights such as:

* Health score
* Active users
* User geolocation with performance and error data by region
* Browser information
* Error and response time
* Element requests, response time, errors
* Request, request with errors, and slowest requests
* AI Model Requests
    * Requests
    * Request by consumer
    * Tokens
    * Tokens by consumer
    * Response time
    * Response time by consumer
    * Errors
* Agent requests  
    * Request time  
    * Requests  
    * Errors  
    * Element response time  
    * Element requests  
    * Element errors  
    * Requests with errors  
    * Slowest requests


<div class="info" markdown="1">

Geolocation information can take up to 20 minutes to synchronize with active user data.

</div>

Some of the benefits of these analytics dashboard insights are:

* Identify how many users experience issues and analyze their locations and browsers.
* Monitor app usage and assess performance trends across regions.
* Compare metrics to evaluate app performance in different locations.
* Understanding usage patterns for scaling purposes.

You can drill further down into an element and view the historical trends of the metrics. After identifying the elements causing issues in the app, reviewing the logs and traces from the error period can further help pinpoint the problem. The trace details include browser and user location.

![Screenshot of selecting a specific trace from an app in ODC analytics.](images/specific-trace-pl.png "Selecting a Specific Trace from an App in ODC Analytics")

You can click the request with errors and the slowest request to display a trace of that element to debug it. For more information about logs and traces, refer to [Monitor and troubleshoot apps](monitor-apps.md)

<div class="warning" markdown="1">

Apps published before November 11, 2024, might not send data geography metrics correctly for some traces.

</div>

## Metrics

Analytics helps you understand how your apps are performing. It summarizes the following metrics.

### Health score

An app's health score is expressed as a numerical score from 1 to 100 and is based on the app's response time and errors during the selected period of time (minimum 5 minutes, maximum 30 days). There are three health score categories:

* Critical (0-70)
* Moderate (70-85)
* Good (85-100)

An app's health score calculation follows the Application Performance Index (APDEX) industry standard. The score is calculated by dividing the number of successful requests to the app's elements by the total number of requests over the selected period. A request is successful if it's completed without errors and the response time is less than a defined threshold.

The APDEX calculation used is **APDEX = (a + b) / c**. Here's a breakdown of the APDEX calculation. You can use this calculation as is or adapt it to suit your specific needs. 

* **a** = Number of successful requests with latency **below 300ms**
* **b** = (Number of successful requests **between 300ms and 1199ms**) / 2
* **c** = Total number of requests

### Active users

The number of unique users visiting the app helps you understand its usage over time.

### Geography

Geographical distribution of users, errors, and overall end-user response time for this app. You can sort the data by unique users, errors, and user response time. There are three categories:

* Countries with users
* Countries with errors
* Response time by country

### Browser

Distribution of browser usage among end-users accessing this app. It categorizes browsers into Chrome, Safari, Edge, Firefox, and Opera. Any other browsers are grouped under **Other** in the data.

### Errors

Errors are the issues that occur when requests are made to an app, which causes it to malfunction or crash. There are three error metrics:

* Total errors: The total number of errors that occur when requests are made to an app.
* Error rate: The rate at which errors occur when requests are made to an app.
* Error percentage: The percentage of requests that resulted in errors.

### Response time

Response time is the amount of time taken to complete a request. The nth percentile response time is the duration under which n% of requests are completed. There are three response time metrics:

* P90:  90th percentile response time
* P95: 95th percentile response time
* P99: 99th percentile response time

### Requests

Requests are the number of app interactions done using screens, APIs, or timers. There are two request metrics:

* Total requests: The total number of requests made to an app.
* Request rate: The rate at which the requests are sent to an app.

## AI model Metrics

ODC provides monitoring for your configured AI Model connections, offering insights into their usage, performance, and any operational errors. These metrics help you track consumption, identify potential bottlenecks, and understand how your models are used by different consumer apps.

Visibility of detailed metric values, particularly those related to current consumption and specific error breakdowns, may depend on your ODC permissions for the relevant stage. You often require the **Access asset logs and traces** permission to access the full set of analytics data for AI Models.

* **Requests:** The number of requests to the AI model and their error rates.
* **Request by consumer:** The number of AI model requests from each consumer app.
* **Tokens:** The number of tokens used. Tokens can represent words, characters, or subwords.
* **Tokens by consumer:** The number of tokens used in input requests and output responses for each consuming app.
* **Response time:** The time taken for the AI model to process a request across all consuming apps. Response time metrics include:
    * P90: 90th percentile response time
    * P95: 95th percentile response time
    * P99: 99th percentile response time
* **Response time by consumer:** Each consuming app breaks down the time the AI model takes to process a request. Response time metrics include:
    * P90: 90th percentile response time
    * P95: 95th percentile response time
    * P99: 99th percentile response time
* **Errors:** Insights into the errors encountered by the AI model
* **Total errors:** Displays the total number of errors that have occurred.
* **Top error:** Identifies the most frequent type of error encountered.
* **The accompanying pie chart visually breaks down the distribution of different error types:**
    * Token limit: Indicates errors arising from requests exceeding the allowed token limit.
    * Rate limit: Shows errors due to exceeding the allowed request rate.
    * Content policy: Represents errors related to violations of content policies.
    * Timeout: Indicates errors caused by requests timing out.
    * Others: Encompasses all other less frequent error types.

## Agent metrics
 
 <div class="info" markdown="1">

Native ODC agent apps are only available to Early Access Program (EAP) customers.

</div>

ODC monitors your [agents](../building-apps/build-ai-powered-apps/intro.md), offering insights into their usage, performance, and operational errors. These metrics help you track agent activity, identify bottlenecks, and understand how your agents are used by different consumers

* **Requests**
    * **Total requests:** The total number of requests made to the agent.  
    * **Request rate:** The rate at which requests are sent to the agent per hour.  
    * **Requests by source element:** The number of requests from each source element.

* **Response time**

    Response time refers to the time taken for the agent to process a request across all consuming elements.

    * Response time metrics include:
        * **P90:** 90th percentile response time.  
        * **P95:** 95th percentile response time.  
        * **P99:** 99th percentile response time.  
    * **Response time by source element:** A breakdown of the time the agent takes to process a request for each consuming element.

* **Errors** This includes insights into the errors encountered by the agent.

    * **Total errors:** Displays the total number of errors that have occurred.  
    * **Error rate:** The rate at which errors occur when requests are made to an agent.  
    * **Error percentage:** The percentage of requests that resulted in errors.  
    * **Requests with errors:** Lists recent requests that encountered errors, including the timestamp, source element, and duration. 

* **Slowest requests**
    * **Slowest requests:** This list includes the requests with the longest duration, including the timestamp, source element, and duration.

## Element metrics

![Screenshot displaying various app metrics in ODC analytics.](images/Analytics-elements-dashboard-pl.png "Various App Metrics in ODC Analytics")

### Element requests

A list of elements by type and their daily amount of requests. There are two element metrics:

* Elements
* Elements types

### Element response time

A list of elements with the highest response times. There are two element metrics:

* Others
* Timers

### Element errors

A list of elements with the highest error percent.

### Request with errors

A list of requests from elements in this app that failed.

### Slowest errors

A list of requests from elements in this app that took 2 seconds or longer to execute.
