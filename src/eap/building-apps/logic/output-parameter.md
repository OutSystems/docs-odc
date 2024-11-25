---
helpids: 7012, 30101
summary: Learn how to use Output Parameters in OutSystems Developer Cloud (ODC) to return computed values from actions, enhancing data handling and integration.
locale: en-us
guid: a0388822-d4ea-4fbf-9bd2-d45b10183c0c
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3213%3A21660&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
tags: data handling, integration, client actions, server actions, output parameters
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
content-type:
  - procedure
  - reference
---

# Output Parameter


An Output Parameter allows you to return computed values from an action.

In the following example, the `GetWeatherData` Client Action has two Input Parameters (`City` and `Country`) and one Output Parameter (`WeatherInfo`):

![Screenshot of a Client Action with Input Parameters 'City' and 'Country' and an Output Parameter 'WeatherInfo'](images/input-parameter-client-action-example-ss.png "Client Action Input Parameters Example")

## How to use
To return a value from inside an action flow, you can use an Assign element to set the Output Parameter to the value you wish to return.

For example, consider the `GetWeatherData` Client Action presented previously. You can use an Assign to set the value of the `WeatherInfo` Output Parameter to the `Data` Output Parameter value returned by the `API_GetWeatherData` Server Action:

![Screenshot showing how to assign a value to the 'WeatherInfo' Output Parameter in a Client Action](images/output-parameter-example-ss.png "Assigning Value to Output Parameter")

You can access the value of an Output Parameter of an invoked action (in this case, the `API_GetWeatherData` Server Action) later in the flow using an expression with the following format:

`<flow_element_name>.<output_parameter_name>`

In the example presented above, the expression becomes the following:

`API_GetWeatherData.Data`

## Output Parameters availability

The following elements displayed in the element tree can have Output Parameters:
* Server Actions and Client Actions
* Processes, Process Activities, and Wait elements
* Exposed/Consumed REST Methods

Additionally, JavaScript elements (available on Client Actions) also have Output Parameters.

External integrations like consumed REST APIs have their logic defined in an external system. In this case, OutSystems fills the Output Parameter values from the values returned by the external system. You can then use the Output Parameter values in your business logic.

