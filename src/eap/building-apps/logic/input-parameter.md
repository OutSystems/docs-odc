---
kinds: ServiceStudio.Model.Variables+ConstantDBInputParameter+Kind, ServiceStudio.Model.Variables+GenericInputParameter+Kind, ServiceStudio.Model.Variables+JSInputParameter+Kind, ServiceStudio.Model.Variables+ProcessInput+Kind, ServiceStudio.Model.Variables+SerializableInputParameter+Kind, ServiceStudio.Model.Variables+SyntheticInputParameter+Kind, ServiceStudio.Model.Variables+URLSerializableInputParameter+Kind, ServiceStudio.Model.Variables+WebReferenceGenericInputParameter+Kind, ServiceStudio.Model.Variables+ReferenceGenericInputParameter+Kind, ServiceStudio.Model.Variables+ReferenceProcessInput+Kind, ServiceStudio.Model.Variables+ReferenceSerializableInputParameter+Kind
helpids: 7011, 30100
summary: An Input Parameter allows you to provide data to an element for further use.
locale: en-us
guid: 4007d09b-8038-4fc4-ad49-8093c6a97650
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3213%3A21492&t=ZwHw8hXeFhwYsO5V-1
platform-version: odc
---

# Input Parameter


An Input Parameter allows you to provide data to an element for further use. The Input Parameter becomes available in that element's scope.

For example, if you add an Input Parameter to a Client Action you can:

* Provide a value for that Input Parameter when calling the Client Action.

* Use the value in the logic flow of the Client Action, for example in expressions or as a part of Input Parameter values of other calls.

In the following example, the `GetWeatherData` Client Action has two Input Parameters (`City` and `Country`) and one Output Parameter (`WeatherInfo`):

![Example of Client Action with two Input Parameters and one Output Parameter](images/input-parameter-client-action-example-ss.png)

Input Parameters can be mandatory or optional, according to their **Is Mandatory** property.

If you call other Actions from the Client Action you can no longer access the Input Parameter because it's not longer in the Client Action scope. To make the Input Parameter value accessible to other calls, include the Input Parameter in the arguments of the Action Call.

## How to use

When invoking an element with Input Parameters, like a Client Action, you must specify the **values** for all the mandatory Input Parameters sent to the Client Action as part of the invocation, optionally specifying values for Input Parameters that are optional. Input Parameter values are also known as input **arguments**.

For example, considering the same `GetWeatherData` Client Action presented before, you could invoke this Client Action setting the values for the `City` and `Country` Input Parameters in the following manner:

![Setting Input Parameter values when calling a Client Action (example)](images/input-parameter-set-value-ss.png)

You define the Input Parameter values in the properties of the Run Client Action element. These arguments appear indented from the remaining properties.

To set an Input Parameter value, enter an expression in the corresponding property.

## Input Parameters availability

The following elements displayed in the element tree can have Input Parameters:

* Server Actions and Client Actions
* Screens and Blocks
* Processes
* Exposed/Consumed REST Methods
* Callback and Authentication actions for REST integrations (although you can't modify the default Input Parameters of these actions)
* Emails
* External Sites
* JavaScript elements (available on Client Actions)
