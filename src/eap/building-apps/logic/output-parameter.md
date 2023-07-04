---
helpids: 7012, 30101
summary: An Output Parameter allows you to return computed values from an action, process, or process flow element.
locale: en-us
guid: a0388822-d4ea-4fbf-9bd2-d45b10183c0c
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3213%3A21660&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Output Parameter


An Output Parameter allows you to return computed values from an action.

In the following example, the `GetWeatherData` Client Action has two Input Parameters (`City` and `Country`) and one Output Parameter (`WeatherInfo`):

![Example of Client Action with two Input Parameters and one Output Parameter](images/input-parameter-client-action-example-ss.png)

## How to use
To return a value from inside an action flow, you can use an Assign element to set the Output Parameter to the value you wish to return.

For example, consider the `GetWeatherData` Client Action presented previously. You can use an Assign to set the value of the `WeatherInfo` Output Parameter to the `Data` Output Parameter value returned by the `API_GetWeatherData` Server Action:

![Example of setting and using an Output Parameter in ODC Studio](images/output-parameter-example-ss.png)

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

