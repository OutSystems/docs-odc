---
summary: Handle the impact on modifications to elements that are being reused between apps and libraries.
locale: en-us
guid: 80bb4604-c06b-48c7-8e8b-382416c95368
app_type: mobile apps, reactive web apps
platform-version: odc
figma:
---
# Handle changes in exposed functionality

A key benefit of centralizing and reusing elements is the ability to change their implementation and signature in a single place and share those changes with the consumers without duplicating efforts.

When exposed functionality is changed, an important aspect to remember is that some changes are compatible, meaning that the consumers can continue to reuse that element without changing their implementation, while other changes are breaking changes that force the consumers to update their implementation to continue reusing that element.

Another essential aspect is that these changes take effect differently depending if the producer is a [strong or a weak dependency](intro.md).

## Handle breaking changes

As a best practice, you should avoid breaking changes since they imply that consumers need to update their implementation. To handle breaking changes in exposed functionality, you need to version that element by duplicating it (copy & paste), renaming it, and then changing its implementation. This way, you can safely introduce changes to that new element without impacting consumers, and subsequently, consumers can progressively update their implementations to use the new element. 

For example, if you need to break a change on a reusable Service Action, one option to version it is to copy and paste it into a new one (ServiceAction_v2), change the signature of the new Service Action, and progressively update the consumers to replace ServiceAction with ServiceAction_v2 with the necessary adjustments in the implementation.

## Handle changes in producer 

The impact of changes in functionality you expose in your producers on the consumers at runtime depends on the kind of changes you perform and the type of dependency between your producer and the consumers.
After you make changes to the producer and publish them, one of the following scenarios may occur in a consumer at runtime.

### Immediate and not impactful changes 

Any changes you perform on weak dependencies become immediately available to the consumers at runtime. Depending on the type of changes, this may immediately impact the consumer at runtime. Examples of changes that do not immediately impact the consumers:

|**Scenario**|**Elements**|
|------------|------------|
|Add an optional Input Parameter<br/>Change a mandatory Input Parameter to optional<br/>Delete an Input Parameter<br/>Reorder Input Parameters<br/>Add an Output Parameter<br/>Delete an unused Output Parameter|Service Action|
|Change the content of a Screen|Screen|
|Change a mandatory Attribute to optional<br/>Delete an unused Attribute<br/>Reorder Attributes|Entity (Database), Static Entity, Structure|
|Add an optional Attribute (any data type)|Entity (Database), Static Entity|
|Add an optional Attribute ([basic data types](../data/data-types.md#basic_data_types) only)|Structure|
|Add a Record<br/>Delete an unused Record|Static Entity|
|Change Description|All elements|
|Expose new elements|Screen, Service Action, Structure, Entity (Database), Static Entity| 

### Immediate and impactful changes 

The following examples of changes immediately impact the consumers and eventually result in runtime errors:
    
|**Scenario**|**Elements**|**Notes**|
|------------|------------|------------|
|Add a mandatory input parameter<br/>Change the data type of an input parameter|Service Action, Screen|  Some data type changes might be compatible at runtime and not produce an immediate error. For example: changing from Integer to Long Integer or any simple type to Text. <br/>
The consumer does not send the input parameter value; the default value is assumed, which may result in runtime errors. |
|Delete an output parameter|Service Action| The producer does not send the output parameter value; the default value is assumed, which may result in runtime errors.|
|Change the data type of an attribute<br/>Delete a used attribute|Entity (Database), Static Entity| Some data type changes might be compatible at runtime and not produce an immediate error. For example: changing from Integer to Long Integer or any simple type to Text. |
|Delete a used record|Static Entity| |
|Delete a used element|All [public elements](../architecture/reuse-elements.md#public-elements--public-elements-)| |
|Rename|All [public elements](../architecture/reuse-elements.md#public-elements--public-elements-)| |

### Non-immediate changes

Any changes you perform on strong dependencies do not impact the consumers immediately. The impact of those changes is only visible when you open consumers in ODC Studio - which updates the dependencies automatically - and only takes effect when the consumer is published using the 1CP button. Again, some compatible changes require no change in the consumer's implementation, while other changes are breaking changes and introduce errors that become visible in the TrueChange panel. Examples of changes that are compatible and do not produce TrueChange errors:

|**Scenario**|**Elements**|
|------------|------------|
|Add an optional input parameter<br/>Add an output paramter|Server Action, Client Action|
|Add an attribute|Static Entity, Structure|
|Add a record|Static Entity|
|Exposing new elements|Client Action, Server Action, Block, Image, Theme, Static Entity, Structure, Script|

Examples of changes that produce TrueChange errors:

|**Scenario**|**Elements**|**Notes**|
|------------|------------|------------|
|Add a mandatory input parameter<br/>Delete a used output parameter|Server Action, Client Action| |
|Delete a used record|Static Entity| |
|Delete a used attribute<br/>Change data type of an attribute|Static Entity, Structure| Some data type changes might be compatible and produce a TrueChange warning instead of an error. For example: changing from Integer to Long Integer or any simple type to Text. |
|Delete| Client Action, Server Action, Block, Image, Theme, Static Entity, Structure, Script| |
