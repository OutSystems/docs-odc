---
summary: Explore the KeyStore Plugin functionalities in OutSystems Developer Cloud (ODC), including client actions, and error handling.
locale: en-us
guid: 62c7a486-6e87-485c-92ef-e0a1dac971d4
app_type: mobile apps
platform-version: odc
figma:
coverage-type:
  - remember
tags:
  - Mobile app
  - Plugins
  - Security
audience:
  - Developer
outsystems-tools:
  - odc studio
isautopublish: true
---
# Key Store plugin reference

## Client actions

### `CheckKeyStorePlugin`

Verifies if the KeyStore Plugin is available or properly installed in the application.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| IsAvailable | Output | Boolean | Indicates if the plugin is available ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

### `GetValue`

Returns the value from the store, associated with the given key .

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Store | Input | Text | The name of the store where to set the value. |
| Key | Input | Text | The key that identifies the desired value. |
| Value | Output | Text | The value associated to the key in the store. |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

### `SetValue`

Creates or updates a key-value pair in the store.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Store | Input | Text | The name of the store where to set the value. |
| Key | Input | Text | The key that will identify the value. |
| Value | Input | Text | The value to be set. |
| KeyAuthentication | Input | Boolean | The authentication value for a specific key-value pair. By default, no authentication is required to access the pair ('False'). If ('True'), the access to the pair will require an authentication method. |
| InvalidateOnBiometricChange | Input | Boolean | Indicates if the stored value should be invalidated when the device's biometric configuration changes (for example, a new fingerprint is enrolled). Only takes effect when **KeyAuthentication** is ('True'). Only applies to secrets saved with this flag set to ('True'). Secrets previously saved without this flag are not affected. By default, the value is not invalidated on biometric change ('False'). |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

### `RemoveKey`

Removes the key-value pair from the store.

| Parameter | Type | Data Type | Description |
| - | - | - | - |
| Store | Input | Text | The name of the store that contains the key to be removed. |
| Key | Input | Text | The key to be removed. |
| Success | Output | Boolean | Indicates if the action was successful ('True') or not ('False'). |
| Error | Output | Error | Displays detailed information of an error, if applicable. |

### Error codes

For a complete list of mobile plugin errors, their causes, impact, and recommended solutions, see the [Mobile Plugins errors page](https://www.outsystems.com/tk/redirect?g=8ae41e18-fa7d-4cbe-a223-226a14abd8bf).
