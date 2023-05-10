---
summary: 
tags:
locale: en-us
guid: 37f6d7d2-565c-4535-b386-5cfe094ececf
app_type: mobile apps, reactive web apps
platform-version: odc
---

# External Libraries SDK REFERENCE

## Contents

- [OSActionAttribute](#T-OutSystems-ExternalLibraries-SDK-OSActionAttribute 'OutSystems.ExternalLibraries.SDK.OSActionAttribute')
  - [Description](#P-OutSystems-ExternalLibraries-SDK-OSActionAttribute-Description 'OutSystems.ExternalLibraries.SDK.OSActionAttribute.Description')
  - [IconResourceName](#P-OutSystems-ExternalLibraries-SDK-OSActionAttribute-IconResourceName 'OutSystems.ExternalLibraries.SDK.OSActionAttribute.IconResourceName')
  - [OriginalName](#P-OutSystems-ExternalLibraries-SDK-OSActionAttribute-OriginalName 'OutSystems.ExternalLibraries.SDK.OSActionAttribute.OriginalName')
  - [ReturnName](#P-OutSystems-ExternalLibraries-SDK-OSActionAttribute-ReturnName 'OutSystems.ExternalLibraries.SDK.OSActionAttribute.ReturnName')
  - [ReturnType](#P-OutSystems-ExternalLibraries-SDK-OSActionAttribute-ReturnType 'OutSystems.ExternalLibraries.SDK.OSActionAttribute.ReturnType')
- [OSDataType](#T-OutSystems-ExternalLibraries-SDK-OSDataType 'OutSystems.ExternalLibraries.SDK.OSDataType')
  - [BinaryData](#F-OutSystems-ExternalLibraries-SDK-OSDataType-BinaryData 'OutSystems.ExternalLibraries.SDK.OSDataType.BinaryData')
  - [Boolean](#F-OutSystems-ExternalLibraries-SDK-OSDataType-Boolean 'OutSystems.ExternalLibraries.SDK.OSDataType.Boolean')
  - [Currency](#F-OutSystems-ExternalLibraries-SDK-OSDataType-Currency 'OutSystems.ExternalLibraries.SDK.OSDataType.Currency')
  - [Date](#F-OutSystems-ExternalLibraries-SDK-OSDataType-Date 'OutSystems.ExternalLibraries.SDK.OSDataType.Date')
  - [DateTime](#F-OutSystems-ExternalLibraries-SDK-OSDataType-DateTime 'OutSystems.ExternalLibraries.SDK.OSDataType.DateTime')
  - [Decimal](#F-OutSystems-ExternalLibraries-SDK-OSDataType-Decimal 'OutSystems.ExternalLibraries.SDK.OSDataType.Decimal')
  - [Email](#F-OutSystems-ExternalLibraries-SDK-OSDataType-Email 'OutSystems.ExternalLibraries.SDK.OSDataType.Email')
  - [InferredFromDotNetType](#F-OutSystems-ExternalLibraries-SDK-OSDataType-InferredFromDotNetType 'OutSystems.ExternalLibraries.SDK.OSDataType.InferredFromDotNetType')
  - [Integer](#F-OutSystems-ExternalLibraries-SDK-OSDataType-Integer 'OutSystems.ExternalLibraries.SDK.OSDataType.Integer')
  - [LongInteger](#F-OutSystems-ExternalLibraries-SDK-OSDataType-LongInteger 'OutSystems.ExternalLibraries.SDK.OSDataType.LongInteger')
  - [PhoneNumber](#F-OutSystems-ExternalLibraries-SDK-OSDataType-PhoneNumber 'OutSystems.ExternalLibraries.SDK.OSDataType.PhoneNumber')
  - [Text](#F-OutSystems-ExternalLibraries-SDK-OSDataType-Text 'OutSystems.ExternalLibraries.SDK.OSDataType.Text')
  - [Time](#F-OutSystems-ExternalLibraries-SDK-OSDataType-Time 'OutSystems.ExternalLibraries.SDK.OSDataType.Time')
- [OSIgnore](#T-OutSystems-ExternalLibraries-SDK-OSIgnore 'OutSystems.ExternalLibraries.SDK.OSIgnore')
- [OSInterfaceAttribute](#T-OutSystems-ExternalLibraries-SDK-OSInterfaceAttribute 'OutSystems.ExternalLibraries.SDK.OSInterfaceAttribute')
  - [Description](#P-OutSystems-ExternalLibraries-SDK-OSInterfaceAttribute-Description 'OutSystems.ExternalLibraries.SDK.OSInterfaceAttribute.Description')
  - [IconResourceName](#P-OutSystems-ExternalLibraries-SDK-OSInterfaceAttribute-IconResourceName 'OutSystems.ExternalLibraries.SDK.OSInterfaceAttribute.IconResourceName')
  - [Name](#P-OutSystems-ExternalLibraries-SDK-OSInterfaceAttribute-Name 'OutSystems.ExternalLibraries.SDK.OSInterfaceAttribute.Name')
  - [OriginalName](#P-OutSystems-ExternalLibraries-SDK-OSInterfaceAttribute-OriginalName 'OutSystems.ExternalLibraries.SDK.OSInterfaceAttribute.OriginalName')
- [OSParameterAttribute](#T-OutSystems-ExternalLibraries-SDK-OSParameterAttribute 'OutSystems.ExternalLibraries.SDK.OSParameterAttribute')
  - [DataType](#P-OutSystems-ExternalLibraries-SDK-OSParameterAttribute-DataType 'OutSystems.ExternalLibraries.SDK.OSParameterAttribute.DataType')
  - [Description](#P-OutSystems-ExternalLibraries-SDK-OSParameterAttribute-Description 'OutSystems.ExternalLibraries.SDK.OSParameterAttribute.Description')
  - [OriginalName](#P-OutSystems-ExternalLibraries-SDK-OSParameterAttribute-OriginalName 'OutSystems.ExternalLibraries.SDK.OSParameterAttribute.OriginalName')
- [OSStructureAttribute](#T-OutSystems-ExternalLibraries-SDK-OSStructureAttribute 'OutSystems.ExternalLibraries.SDK.OSStructureAttribute')
  - [Description](#P-OutSystems-ExternalLibraries-SDK-OSStructureAttribute-Description 'OutSystems.ExternalLibraries.SDK.OSStructureAttribute.Description')
  - [OriginalName](#P-OutSystems-ExternalLibraries-SDK-OSStructureAttribute-OriginalName 'OutSystems.ExternalLibraries.SDK.OSStructureAttribute.OriginalName')
- [OSStructureFieldAttribute](#T-OutSystems-ExternalLibraries-SDK-OSStructureFieldAttribute 'OutSystems.ExternalLibraries.SDK.OSStructureFieldAttribute')
  - [DataType](#P-OutSystems-ExternalLibraries-SDK-OSStructureFieldAttribute-DataType 'OutSystems.ExternalLibraries.SDK.OSStructureFieldAttribute.DataType')
  - [Decimals](#P-OutSystems-ExternalLibraries-SDK-OSStructureFieldAttribute-Decimals 'OutSystems.ExternalLibraries.SDK.OSStructureFieldAttribute.Decimals')
  - [DefaultValue](#P-OutSystems-ExternalLibraries-SDK-OSStructureFieldAttribute-DefaultValue 'OutSystems.ExternalLibraries.SDK.OSStructureFieldAttribute.DefaultValue')
  - [Description](#P-OutSystems-ExternalLibraries-SDK-OSStructureFieldAttribute-Description 'OutSystems.ExternalLibraries.SDK.OSStructureFieldAttribute.Description')
  - [IsMandatory](#P-OutSystems-ExternalLibraries-SDK-OSStructureFieldAttribute-IsMandatory 'OutSystems.ExternalLibraries.SDK.OSStructureFieldAttribute.IsMandatory')
  - [Length](#P-OutSystems-ExternalLibraries-SDK-OSStructureFieldAttribute-Length 'OutSystems.ExternalLibraries.SDK.OSStructureFieldAttribute.Length')
  - [OriginalName](#P-OutSystems-ExternalLibraries-SDK-OSStructureFieldAttribute-OriginalName 'OutSystems.ExternalLibraries.SDK.OSStructureFieldAttribute.OriginalName')

<a name='T-OutSystems-ExternalLibraries-SDK-OSActionAttribute'></a>
## OSActionAttribute `type`

##### Namespace

OutSystems.ExternalLibraries.SDK

##### Summary

Use this attribute to decorate a public .NET method you want to expose as an OutSystems Server Action.
The method must be in the scope of a .NET interface decorated with OSInterface.

<a name='P-OutSystems-ExternalLibraries-SDK-OSActionAttribute-Description'></a>
### Description `property`

##### Summary

Defines the Description of the exposed OutSystems Server Action.

<a name='P-OutSystems-ExternalLibraries-SDK-OSActionAttribute-IconResourceName'></a>
### IconResourceName `property`

##### Summary

Defines the name of the embedded resource containing the icon for the exposed OutSystems Server Action.

<a name='P-OutSystems-ExternalLibraries-SDK-OSActionAttribute-OriginalName'></a>
### OriginalName `property`

##### Summary

Allows renaming the .NET method without breaking ODC apps consuming the exposed OutSystems Server Action.
This property holds the original name of the method, so the key generated from the method name remains unchanged.

<a name='P-OutSystems-ExternalLibraries-SDK-OSActionAttribute-ReturnName'></a>
### ReturnName `property`

##### Summary

If this .NET method has a returned value, this property defines the name for the exposed OutSystems Server Action Output Parameter.
If not specified, the name is the name of the method.

<a name='P-OutSystems-ExternalLibraries-SDK-OSActionAttribute-ReturnType'></a>
### ReturnType `property`

##### Summary

If this .NET method has a returned value, this property defines the type for the exposed OutSystems Server Action Output Parameter.
The specified type must be compatible with the .NET returned type.
If not specified, the OutSystems type is inferred from the .NET type.

<a name='T-OutSystems-ExternalLibraries-SDK-OSDataType'></a>
## OSDataType `type`

##### Namespace

OutSystems.ExternalLibraries.SDK

##### Summary

Represents an enumeration of the OutSystems data types.

<a name='F-OutSystems-ExternalLibraries-SDK-OSDataType-BinaryData'></a>
### BinaryData `constants`

##### Summary

Binary type

<a name='F-OutSystems-ExternalLibraries-SDK-OSDataType-Boolean'></a>
### Boolean `constants`

##### Summary

Boolean type

<a name='F-OutSystems-ExternalLibraries-SDK-OSDataType-Currency'></a>
### Currency `constants`

##### Summary

Currency type

<a name='F-OutSystems-ExternalLibraries-SDK-OSDataType-Date'></a>
### Date `constants`

##### Summary

Date type

<a name='F-OutSystems-ExternalLibraries-SDK-OSDataType-DateTime'></a>
### DateTime `constants`

##### Summary

DateTime type

<a name='F-OutSystems-ExternalLibraries-SDK-OSDataType-Decimal'></a>
### Decimal `constants`

##### Summary

Decimal type

<a name='F-OutSystems-ExternalLibraries-SDK-OSDataType-Email'></a>
### Email `constants`

##### Summary

Email type

<a name='F-OutSystems-ExternalLibraries-SDK-OSDataType-InferredFromDotNetType'></a>
### InferredFromDotNetType `constants`

##### Summary

OutSystems data type is inferred from the .NET type.

<a name='F-OutSystems-ExternalLibraries-SDK-OSDataType-Integer'></a>
### Integer `constants`

##### Summary

Integer type

<a name='F-OutSystems-ExternalLibraries-SDK-OSDataType-LongInteger'></a>
### LongInteger `constants`

##### Summary

Long Integer type

<a name='F-OutSystems-ExternalLibraries-SDK-OSDataType-PhoneNumber'></a>
### PhoneNumber `constants`

##### Summary

Phone number type

<a name='F-OutSystems-ExternalLibraries-SDK-OSDataType-Text'></a>
### Text `constants`

##### Summary

Text type

<a name='F-OutSystems-ExternalLibraries-SDK-OSDataType-Time'></a>
### Time `constants`

##### Summary

Time type

<a name='T-OutSystems-ExternalLibraries-SDK-OSIgnore'></a>
## OSIgnore `type`

##### Namespace

OutSystems.ExternalLibraries.SDK

##### Summary

Use to decorate a public property/field within a .NET struct decorated with OSStructure to specify that it shouldn't be exposed as an OutSystems Structure Attribute.

<a name='T-OutSystems-ExternalLibraries-SDK-OSInterfaceAttribute'></a>
## OSInterfaceAttribute `type`

##### Namespace

OutSystems.ExternalLibraries.SDK

##### Summary

Use this attribute to decorate the entry point for the External Library.
Only one .NET interface can be decorated with this attribute in the External Library.
The interface must be implemented by a public class with a public parameterless constructor.
All public methods within this .NET interface are exposed as OutSystems Server Actions.

<a name='P-OutSystems-ExternalLibraries-SDK-OSInterfaceAttribute-Description'></a>
### Description `property`

##### Summary

Defines the description of the External Library.

<a name='P-OutSystems-ExternalLibraries-SDK-OSInterfaceAttribute-IconResourceName'></a>
### IconResourceName `property`

##### Summary

Defines the name of the embedded resource containing the icon for the corresponding External Library.

<a name='P-OutSystems-ExternalLibraries-SDK-OSInterfaceAttribute-Name'></a>
### Name `property`

##### Summary

Defines the name of the External Library. 
If not specified, that name is the name of the .NET interface without the "I" prefix.
This property allows users to set a custom name for the External Library.

<a name='P-OutSystems-ExternalLibraries-SDK-OSInterfaceAttribute-OriginalName'></a>
### OriginalName `property`

##### Summary

Allows renaming the .NET interface without breaking ODC apps consuming it.
This property holds the original name of the library (previous version namespace + previous version library name), so the key generated from the library name remains unchanged, and app references are not broken.

<a name='T-OutSystems-ExternalLibraries-SDK-OSParameterAttribute'></a>
## OSParameterAttribute `type`

##### Namespace

OutSystems.ExternalLibraries.SDK

##### Summary

Use this attribute to decorate a .NET method parameter you want to expose as an OutSystems Server Action Parameter.
The method parameter must be in the scope of a .NET interface decorated with OSInterface.

<a name='P-OutSystems-ExternalLibraries-SDK-OSParameterAttribute-DataType'></a>
### DataType `property`

##### Summary

Defines the type for the exposed OutSystems Server Action Parameter.
The specified type must be compatible with the .NET parameter type.
If not specified, the OutSystems type is inferred from the .NET type.

<a name='P-OutSystems-ExternalLibraries-SDK-OSParameterAttribute-Description'></a>
### Description `property`

##### Summary

Defines the Description of the exposed OutSystems Server Action Parameter.

<a name='P-OutSystems-ExternalLibraries-SDK-OSParameterAttribute-OriginalName'></a>
### OriginalName `property`

##### Summary

Allows renaming the .NET method parameter without breaking ODC apps consuming it.
This property holds the original name of the method parameter, so the key generated from the method parameter remains unchanged, and app references are not broken.

<a name='T-OutSystems-ExternalLibraries-SDK-OSStructureAttribute'></a>
## OSStructureAttribute `type`

##### Namespace

OutSystems.ExternalLibraries.SDK

##### Summary

Use this attribute to decorate a .NET struct you want to expose as an OutSystems Structure.
All public fields and properties within the struct are exposed as OutSystems Structure Attributes.

<a name='P-OutSystems-ExternalLibraries-SDK-OSStructureAttribute-Description'></a>
### Description `property`

##### Summary

Defines the description of the exposed OutSystems Structure.

<a name='P-OutSystems-ExternalLibraries-SDK-OSStructureAttribute-OriginalName'></a>
### OriginalName `property`

##### Summary

Allows renaming the .NET struct without breaking OutSystems apps consuming it.
This property holds the original name of the struct, so the key generated from the struct name remains unchanged, and app references are not broken.

<a name='T-OutSystems-ExternalLibraries-SDK-OSStructureFieldAttribute'></a>
## OSStructureFieldAttribute `type`

##### Namespace

OutSystems.ExternalLibraries.SDK

##### Summary

Use this attribute to decorate a .NET struct public property/field you want to expose as an OutSystems Structure Attribute.
The property/field must be within the scope of a .NET struct decorated with OSStructureAttribute.

<a name='P-OutSystems-ExternalLibraries-SDK-OSStructureFieldAttribute-DataType'></a>
### DataType `property`

##### Summary

Defines the type of the exposed OutSystems Structure Attribute.
The specified type must be compatible with the .NET parameter type. If not specified, the OutSystems type will be inferred from the .NET type.

<a name='P-OutSystems-ExternalLibraries-SDK-OSStructureFieldAttribute-Decimals'></a>
### Decimals `property`

##### Summary

Defines the number of decimal places of the exposed OutSystems Structure Attribute.
This only applies to Decimal types. Default = 8.

<a name='P-OutSystems-ExternalLibraries-SDK-OSStructureFieldAttribute-DefaultValue'></a>
### DefaultValue `property`

##### Summary

Defines the default value of the .NET struct property/field.

<a name='P-OutSystems-ExternalLibraries-SDK-OSStructureFieldAttribute-Description'></a>
### Description `property`

##### Summary

Defines the type of the exposed OutSystems Structure Attribute.
The specified type must be compatible with the .NET parameter type. If not specified, the OutSystems type will be inferred from the .NET type.

<a name='P-OutSystems-ExternalLibraries-SDK-OSStructureFieldAttribute-IsMandatory'></a>
### IsMandatory `property`

##### Summary

Defines if the exposed OutSystems Structure Attribute requires a value to be set.

<a name='P-OutSystems-ExternalLibraries-SDK-OSStructureFieldAttribute-Length'></a>
### Length `property`

##### Summary

Defines the maximum character length of the exposed OutSystems Structure Attribute.
This only applies to Decimal and Text types. Default = 50.

<a name='P-OutSystems-ExternalLibraries-SDK-OSStructureFieldAttribute-OriginalName'></a>
### OriginalName `property`

##### Summary

Allows renaming the .NET struct property/field without breaking ODC apps consuming it.
This property holds the original name of the struct property/field, so the key generated from the struct name remains unchanged, and app references are not broken.
