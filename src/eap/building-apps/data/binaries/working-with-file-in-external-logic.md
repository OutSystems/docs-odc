---
guid: b2fb0646-b8e6-4098-b262-65d03ab3cf99
locale: en-us
summary: Working with file values in external libraries for OutSystems Developer Cloud (ODC), read, write, and test IOSFile content with IFileStorage.
figma:
coverage-type:
  - apply
topic:
  - declare-file-parameters
  - library-file-lifecycle
  - read-write-file-content
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - Developer
tags:
  - .NET
  - C#
  - Extensions
  - Libraries
  - Lifecycle
  - NuGet
  - Testing
outsystems-tools:
  - visual studio
isautopublish: true
---

# Working with file values in external libraries

External library functions support the **File** data type as input and output parameters. To work with **File** values in your custom code, declare parameters of type `IOSFile`, provided by the OutSystems External Libraries SDK. This lets your custom code read files that an ODC app provides, generate new files, and return them to the calling app. For an overview of the **File** data type, refer to [The File data type](binaries-native-cloud.md).

For general information about creating, building, and publishing an External Library, refer to [External libraries SDK README](../../external-logic/README.md).

## Prerequisites

Before you add **File** parameters to an External Library, make sure your project meets the following requirements:

* The project references `OutSystems.ExternalLibraries.SDK` version 1.7.0 or later. Earlier versions don't include the `IOSFile` type.
* The project references `OutSystems.ExternalLibraries.SDK.FileStorage` version 1.2.1 or later. Your code needs this package to read or create file content.

The project file contains references similar to the following:

```xml
<ItemGroup>
    <PackageReference Include="OutSystems.ExternalLibraries.SDK" Version="1.7.0" />
    <PackageReference Include="OutSystems.ExternalLibraries.SDK.FileStorage" Version="1.2.1" />
</ItemGroup>
```

## File input parameters

A **File** input parameter gives your function access to binary file content the calling app provides, such as a file stored in an entity or a file from a user upload. Declare the parameter as type `IOSFile` in your custom code.

Use a **File** input parameter when your function needs to work with existing binary content. For example, use it to convert file formats, extract data from a document or spreadsheet, validate or analyze content, or process the file's bytes directly.

## File output parameters

A **File** output parameter lets your function return a file to the calling app. Your function creates the file content during execution and returns an `IOSFile` value through the output parameter. The calling app receives the **File** value and uses it like any other **File** value in the app.

Use a **File** output parameter when your function produces a file as part of its logic, for example, to generate a report, convert a document, or produce any other binary output.

The following example declares a method that takes a **File** input parameter and returns a **File** output parameter:

```csharp
using OutSystems.ExternalLibraries.SDK;

namespace MyCompany
{
    [OSInterface]
    public interface IFileProcessor
    {
        IOSFile ConvertToPdf(IOSFile document);
    }
}
```

Although not required, to make the data type explicit in the method declaration, set `DataType = OSDataType.File` in the `OSParameter` attribute of the input parameter, and `ReturnType = OSDataType.File` in the `OSAction` attribute of the method:

```csharp
[OSAction(Description = "Converts a document to PDF.", ReturnName = "PdfFile", ReturnType = OSDataType.File)]
IOSFile ConvertToPdf(
    [OSParameter(DataType = OSDataType.File, Description = "The document to convert.")]
    IOSFile document);
```

## Read and write file content

The `IOSFile` type only carries file properties: `Key`, `Version`, `ContentType`, and `Size`. To read from a **File** input parameter or write content for a **File** output parameter, install the `OutSystems.ExternalLibraries.SDK.FileStorage` NuGet package in addition to `OutSystems.ExternalLibraries.SDK`. This package provides the `IFileStorage` interface, which your function gets an instance of by calling `FileStorage.GetInstance()`. The SDK selects the correct storage implementation for your deployment environment automatically, so you don't specify where the file is stored.

All `IFileStorage` methods are asynchronous, but the methods that the SDK exposes as server actions are synchronous. Implement the method declared in the interface as a synchronous method, put the file logic in a private `async` method, and call it once with `.GetAwaiter().GetResult()`.

The following example shows a possible implementation of the `ConvertToPdf` method:

```csharp
using System.Threading;
using System.Threading.Tasks;
using OutSystems.ExternalLibraries.SDK;
using OutSystems.ExternalLibraries.SDK.FileStorage;

namespace MyCompany
{
    public class FileProcessor : IFileProcessor
    {
        private readonly IFileStorage _fileStorage = FileStorage.GetInstance();

        public IOSFile ConvertToPdf(IOSFile document)
        {
            return ConvertToPdfAsync(document).GetAwaiter().GetResult();
        }

        private async Task<IOSFile> ConvertToPdfAsync(IOSFile document, CancellationToken cancellationToken = default)
        {
            await using var contentStream = await _fileStorage.ReadFileAsStreamAsync(document, cancellationToken);
            using var pdfContentStream = ConvertStreamToPdf(contentStream);

            return await _fileStorage.CreateFileFromStreamAsync(
                fileName: "converted.pdf",
                contentType: "application/pdf",
                contentStream: pdfContentStream);
        }
    }
}
```

In the example, `ConvertStreamToPdf` stands for your own conversion logic.

`IFileStorage` provides the following methods to read a **File** input parameter's content:

* `ReadFileAsync`: returns the content as a byte array. Avoid this method for files larger than 10 MB.
* `ReadFileAsStreamAsync`: returns the content as a stream. Use this method for files of any size.
* `ReadFileRangeAsync`: returns a specific byte range of the content as a stream. Use this method to read only part of a file.

`IFileStorage` provides the following methods to write a **File** output parameter's content:

* `CreateFileAsync`: creates a file from an in-memory byte array. Avoid this method for files larger than 10 MB.
* `CreateFileFromStreamAsync`: creates a file by streaming content from a stream. Use this method when you already have a `Stream` (e.g., from another SDK or an HTTP call).
* `CreateFileFromWriterAsync`: creates a file by writing to a stream over multiple calls, without holding the full content in memory. Use this method to produce or transform large files incrementally.

The `fileName` specified in these operations is only a file attribute, so it doesn't need to be unique across files. `IOSFile` doesn't expose the file name directly. To retrieve the original file name of a **File** input parameter, call `GetFileMetadataAsync`, as shown in [Store and read file metadata](#store-and-read-file-metadata).

Refer to [The File data type](binaries-native-cloud.md) for the maximum supported file size.

## Examples of file operations

The following examples show how to call each `IFileStorage` method. They assume that `_fileStorage` holds the instance that `FileStorage.GetInstance()` returns, and that the code runs inside a private `async` method.

### Read and create small files

For small payloads, `ReadFileAsync` and `CreateFileAsync` work with byte arrays. The arguments of the create methods are the file name, the content type, and the content. The following example creates a text file and reads it back:

```csharp
byte[] content = Encoding.UTF8.GetBytes("hello");
IOSFile file = await _fileStorage.CreateFileAsync("hello.txt", "text/plain", content);
byte[] sameContent = await _fileStorage.ReadFileAsync(file);
```

### Create a file from an existing stream

When the content already exists as a stream, for example, the response of an HTTP call, pass the stream to `CreateFileFromStreamAsync`:

```csharp
using Stream source = await httpClient.GetStreamAsync(url);
IOSFile file = await _fileStorage.CreateFileFromStreamAsync("download.bin", "application/octet-stream", source);
```

### Read part of a file

`ReadFileRangeAsync` takes a start byte and an end byte. The end byte is inclusive, so the range `0` to `1023` returns 1,024 bytes. The following example reads the first kilobyte of a file:

```csharp
await using Stream preview = await _fileStorage.ReadFileRangeAsync(file, startByte: 0, endByte: 1023);
using var reader = new StreamReader(preview);
string firstKilobyte = await reader.ReadToEndAsync();
```

### Generate a large file incrementally

`CreateFileFromWriterAsync` takes a callback that writes the content to a destination stream. The FileStorage SDK owns the destination stream, so don't close it in your callback. If you wrap the destination stream in a `StreamWriter`, set `leaveOpen: true`.

The following example reads a text file with one value per line and writes a CSV file with one result per line. Both files are processed as streams, so the full content is never in memory.

```csharp
private Task<IOSFile> ProcessLinesAsync(IOSFile inputFile, CancellationToken cancellationToken = default)
{
    return _fileStorage.CreateFileFromWriterAsync("results.csv", "text/csv",
        async (destination, token) =>
        {
            await using var source = await _fileStorage.ReadFileAsStreamAsync(inputFile, token);
            using var reader = new StreamReader(source);
            await using var writer = new StreamWriter(destination, new UTF8Encoding(false), leaveOpen: true);
            await writer.WriteLineAsync("Value,Result");

            string? line;
            while ((line = await reader.ReadLineAsync(token)) is not null)
            {
                await writer.WriteLineAsync($"{line},{Process(line)}");
            }
        }, null, cancellationToken);
}
```

In the example, `Process` stands for the logic that handles each line.

## Store and read file metadata

Every create method accepts an optional `additionalUserData` dictionary. The FileStorage SDK stores these key-value pairs with the file.

The FileStorage SDK validates the file name and the `additionalUserData` entries before it stores anything. If any of them breaks one of the following rules, the create method throws an `ArgumentException` exception that names the offending key or argument.

* **Key casing**: keys are case-insensitive. The SDK stores and exposes keys in lowercase, and every lookup ignores casing. Keys that differ only by casing, such as `SourceKey` and `sourcekey`, are duplicates and cause an error.
* **Key characters**: keys are non-empty and use only ASCII letters, digits, and the following characters: ``! # $ % & ' * + - . ^ _ ` | ~``.
* **Value characters**: values, including the file name, aren't `null` and use only printable ASCII characters. Non-ASCII characters, such as the `ó` in `Relatório.pdf`, and control characters, such as line breaks, cause an error.
* **Reserved file name key**: the SDK sets the `IFileMetadata.Keys.FileName` key from the `fileName` argument. The SDK ignores a `FileName` key, in any casing, in `additionalUserData`.
* **Size limit**: metadata is limited to 1500 bytes. The limit applies to the whole metadata, including the file name. The size is the UTF-8 bytes of every key and value, plus 12 bytes for each entry.

To stay within the size limit, keep keys short, and store references, such as a file key or a record ID, instead of large values.

To store a value that contains non-ASCII characters, encode the value in an ASCII-safe format, such as Base64, before you create the file. Decode the value when you read it back from the file metadata. The encoded value counts toward the 1500-byte limit, and Base64 increases the size of a value by about one third.

The following example records the key of the source file in the file it creates:

```csharp
var userData = new Dictionary<string, string> { ["SourceFileKey"] = inputFile.Key };
IOSFile output = await _fileStorage.CreateFileFromWriterAsync("results.csv", "text/csv", writeAsync, userData);
```

The FileStorage SDK also stores the file name in the metadata, under the `IFileMetadata.Keys.FileName` key. To read the file name and the user metadata, call `GetFileMetadataAsync`:

```csharp
IFileMetadata metadata = await _fileStorage.GetFileMetadataAsync(file);
string? fileName = metadata.GetMetadata(IFileMetadata.Keys.FileName);
string? sourceFileKey = metadata.GetMetadata("SourceFileKey");
```

Key lookups ignore casing, so `GetMetadata("sourcefilekey")` returns the same value. To list all the entries, iterate over `metadata.UserData`. The keys in `UserData` are lowercase, for example `filename` and `sourcefilekey`.

## Handle file storage errors

The FileStorage SDK throws typed exceptions from the `OutSystems.ExternalLibraries.SDK.FileStorage.Exceptions` namespace. All of them derive from `FileStorageException`. Invalid arguments, including file names and metadata that break the rules in [Store and read file metadata](#store-and-read-file-metadata), cause an `ArgumentException` instead.

The SDK throws the following exceptions:

* `FileSizeLimitExceededException`: the file is larger than the maximum supported file size.
* `ConcurrentWriteException`: concurrent writes to the same file caused a conflict.
* `FileStorageException`: the base class for every other file storage error.

Catch these exceptions in the method that the SDK exposes as a server action, log the error with the file key, and rethrow the exception. Rethrowing lets the calling app handle the error in its own logic. The following example handles a size-limit error and a general file storage error:

```csharp
using OutSystems.ExternalLibraries.SDK.FileStorage.Exceptions;

public IOSFile ProcessLines(IOSFile inputFile)
{
    try
    {
        return ProcessLinesAsync(inputFile).GetAwaiter().GetResult();
    }
    catch (FileSizeLimitExceededException ex)
    {
        _logger.LogError(ex, "Results for file {FileKey} exceed the file size limit. Split the input file.", inputFile.Key);
        throw;
    }
    catch (FileStorageException ex)
    {
        _logger.LogError(ex, "File storage error while processing file {FileKey}", inputFile.Key);
        throw;
    }
}
```

## File lifecycle

Files created by an External Library function are stored temporarily, following the same platform-managed lifecycle described in [File lifecycle](file-reference-lifecycle.md). The runtime deletes temporary files automatically after a short period.

To retain a file after the function returns, the calling app must save the **File** reference to an entity. Saving the reference to an entity record promotes the file to permanent storage.

Files are isolated per function invocation. Files written during one invocation aren't accessible from other invocations of the same or different functions. The runtime manages file storage locations. Files produced by External Library functions can't be moved or renamed.

## Unit test code that uses file storage

Outside ODC, there's no file storage for the FileStorage SDK to connect to. `FileStorage.GetInstance()` returns the file storage registered with `FileStorage.Configure`. In ODC, the External Library runtime registers the real file storage before any action runs. To unit test your library, register an in-memory implementation with `FileStorage.Configure` in your test project only. Your library code stays the same as the code you publish to ODC.

The [advanced IBAN checker template](https://github.com/OutSystems/OutSystems.ExternalLibraries.SDK-templates/tree/main/templates/advanced) includes the following test helpers in the `FileStorageTesting` folder of its unit test project:

* **InMemoryFileStorage.cs**: an in-memory implementation of the full `IFileStorage` interface. Like the FileStorage SDK, it stores metadata keys in lowercase, matches them regardless of casing, rejects keys that differ only in casing with an `ArgumentException` exception, and ignores a `FileName` key in `additionalUserData`. Unlike the FileStorage SDK, it doesn't check any other metadata rule.
* **InMemoryFileStorageTests.cs**: optional unit tests for `InMemoryFileStorage`.

<div class="warning" markdown="1">

Never call `FileStorage.Configure` or `FileStorage.Reset` from library code. Only test projects call them. If the External Library calls them, the published library replaces or drops ODC file storage.

</div>

`InMemoryFileStorage` doesn't reproduce every behavior of ODC file storage. Tests that pass against `InMemoryFileStorage` don't guarantee the same results in ODC. Test your library in an ODC app before you release it.

To use the test helpers in your own test project, follow these steps:

1. Copy the `FileStorageTesting` folder from the template to your test project.

1. In the copied files, change the `namespace` to match your test project.

1. In your test class, call `FileStorage.Reset()` and then `FileStorage.Configure` before you create the class under test. Call `FileStorage.Reset()` again after each test. `Reset()` clears the cached instance and the registered factory, so every test registers a new, empty fake.

1. In each test, create the input files with `CreateFileAsync` and call the method you're testing.

If you don't configure file storage, `FileStorage.GetInstance()` throws an `InvalidOperationException` exception. `FileStorage` is process-wide state, so mark every test fixture that uses it with `[NonParallelizable]`.

The following example uses NUnit to test a `CalculateSha256` method that returns the SHA-256 hash of a file:

```csharp
private InMemoryFileStorage _storage = null!;
private FileProcessor _processor = null!;

[SetUp]
public void SetUp()
{
    FileStorage.Reset();
    _storage = new InMemoryFileStorage();
    FileStorage.Configure(() => _storage);
    _processor = new FileProcessor();
}

[TearDown]
public void TearDown() => FileStorage.Reset();

[Test]
public async Task CalculateSha256MatchesKnownDigest()
{
    IOSFile file = await _storage.CreateFileAsync("input.txt", "text/plain", Encoding.UTF8.GetBytes("hello"));

    string hash = _processor.CalculateSha256(file);

    Assert.That(hash, Is.EqualTo("2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824"));
}
```

To test how your code handles the size limit, set the `MaxFileSizeBytes` property of `InMemoryFileStorage`. `MaxFileSizeBytes` isn't part of `IFileStorage`, so the test class keeps the fake in a field of type `InMemoryFileStorage`:

```csharp
_storage.MaxFileSizeBytes = 10;
Assert.Throws<FileSizeLimitExceededException>(() => _processor.ProcessLines(input));
```

## Related resources

The following resources provide more information about **File** values and External Libraries:

* [The File data type](binaries-native-cloud.md)
* [File lifecycle](file-reference-lifecycle.md)
* [External libraries SDK README](../../external-logic/README.md)
* [Best practices for using external libraries](../../external-logic/best-practices.md)
* [Advanced IBAN checker template](https://github.com/OutSystems/OutSystems.ExternalLibraries.SDK-templates/tree/main/templates/advanced)
