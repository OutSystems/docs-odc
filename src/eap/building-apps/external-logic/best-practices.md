---
guid: b80a6b0e-69be-435d-85bc-29c194c28126
locale: en-us
summary: This articles explains the best practices for using external libraries.
figma:
coverage-type:
  - evaluate
topic:
  - custom-code-integration
app_type: mobile apps,reactive web apps
platform-version: odc
audience:
  - backend developers
  - architects
  - full stack developers
  - tech leads
tags: external libraries, best practices, private gateway, cloud connectivity, architecture
helpids:
outsystems-tools:
  - none
---
# Best practices for using external libraries

## Use with the private gateway feature

You can connect your external library to private data and private services ("endpoints") that aren't accessible by the internet by using the [Private Gateway feature](../../manage-platform-app-lifecycle/private-gateway.md).

Once you've configured a private gateway to your network, you can use the connected endpoint(s) in your custom code using the hostname defined by the environment variable `SECURE_GATEWAY`. You use that hostname in conjunction with the configured ports.

For example, if you want to connect to a REST API endpoint on port 8080 you could use a string to define the Base URL as `$"https://{Environment.GetEnvironmentVariable("SECURE_GATEWAY")}:8080/"` if the endpoint is connected to cloud-connector over TLS/SSL or `http` if it's not.

Ensure that your code file includes the `using System;` directive at the top to have access to the `System` namespace, which is necessary for utilizing the `Environment.GetEnvironmentVariable` method.

## Architecture

Server actions built in the OutSystems visual language execute directly in the [ODC Runtime](../../manage-platform-app-lifecycle/platform-architecture/intro.md#runtime), sharing the same execution context as the app. This means that any state or context established during the execution of these server actions is maintained within the scope of the app's lifecycle.

On the other hand, server actions exposed through external libraries execute differently. Each time your app calls a server action from an external library, it makes an HTTPS call to an external service that hosts and runs the custom code. As a result, the execution context of these server actions is separate from the app.

This architecture has several important implications:

* **Statelessness:** The external libraries you build should be designed to be stateless. This means they shouldn't maintain any state information between calls. Any state or context needed to execute the external library should be passed explicitly as an input parameter. For example, storing state as fields in the library's class isn't supported. However, be aware that successive calls may reuse the execution context, so it's important to ensure the [release of memory resources](#memory-usage) to avoid memory leaks.

* **Latency:** Since an HTTPS call is made each time a server action in an external library is called, a small amount of latency is introduced in the execution time. Minimizing the number of calls to external libraries and batching operations where possible can help mitigate the impact of this latency.

* **Independence:** External libraries run independently of the ODC app. This means they don't have direct access to the app's resources, context, or state, other than what you explicitly provide as an input parameter.

By designing your external libraries with these considerations in mind, you can ensure that they function correctly and efficiently within the broader architecture of your ODC apps.

## Memory usage

To prevent memory leaks it's important to properly dispose of objects that manage system resources. In .NET, classes that implement the `IDisposable` interface require explicit cleanup. You can use [`using` statements](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/using) to ensure these objects are properly disposed when they go out of scope.

To check if an object needs disposal, look for the `IDisposable` interface in the class documentation or use your IDE's IntelliSense. Common disposable objects include Stream classes (FileStream, MemoryStream, NetworkStream), database connections, file handles, graphics resources, and network connections.

For example:

```csharp
// Wrong: Resources are not disposed when method returns
var stream = new MemoryStream();  // MemoryStream implements IDisposable
var data = new byte[1024];        // byte[] does not implement IDisposable

// Correct: Only wrap disposable objects in using statements
using var stream = new MemoryStream();  // Will be disposed automatically
var data = new byte[1024];              // No using needed
```

To catch disposal issues early, enable the CA2000 code analysis rule in your project by adding this to your `.editorconfig` file:

```
dotnet_diagnostic.CA2000.severity = warning
```

## Use with large binary files

Server actions from external libraries have a total input size limit of 5.5MB. This includes all input parameters (in particular binary data), parameter names, and serialization overhead.

<div class="warning" markdown="1">

If you try to pass inputs that exceed this limit (for example, a large binary file) to a server action during runtime, an **Input payload is too large** error will be thrown and logged as a runtime error in the app's logs.

</div>

To use a large binary file in custom code you can:

1. Expose the binary file in a [REST API endpoint](../../integration-with-systems/exposing_rest/intro.md) from your app and then implement logic in your custom code to consume the file from the endpoint.
1. Host the binary file on a file-sharing service and implement logic in your custom code to download the file from the URL.

## Related resources

* [Extend your apps with custom code](intro.md)

* [External libraries SDK README](README.md)
