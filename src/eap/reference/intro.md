---
summary: Learn about OutSystems various elements and language.
tags:
locale: en-us
guid: f9d530c1-f9fa-4b08-9e75-5dfb984402da
app_type: mobile apps, reactive web apps
platform-version: odc
---

# OutSystems language and elements

## Libraries
Libraries provided by OutSystems that you can use to extend the capabilities of your apps. To learn more about how to use these libraries see [here](../building-apps/use-public-elements.md).

### Binary Data
The OutSystems BinaryData library provides actions to manipulate binary data, such as retrieving the length or transforming binary content into Text or Base64.

Action | Description | Available as function?
---|---|---
[Base64ToBinary](libraries/binarydata.md#Base64ToBinary) | Converts Base64 Text into BinaryData. | Yes
[BinaryDataSize](libraries/binarydata.md#BinaryDataSize) | Returns the size in bytes of a binary content. | Yes
[BinaryDataToHex](libraries/binarydata.md#BinaryDataToHex) | Converts the given binary data to hexadecimal representation. | Yes
[BinaryDataToText](libraries/binarydata.md#BinaryDataToText) | Reads the content of a text file using a given encoding. If no encoding is supplied, the system's default ANSI encoding will be used. | Yes
[BinaryToBase64](libraries/binarydata.md#BinaryToBase64) | Converts BinaryData into Base64 Text. | Yes
[Compare](libraries/binarydata.md#Compare) | Performs a binary comparison between two Binary Data contents. | Yes
[ConvertEncoding](libraries/binarydata.md#ConvertEncoding) | Converts a range of bytes in a BinaryData from one encoding to another. | Yes
[TextToBinaryData](libraries/binarydata.md#TextToBinaryData) | Converts a Text into binary content. If no encoding is supplied, the system's default ANSI encoding will be used. | Yes

### Date Time
The OutSystems DateTime library provides actions to access and manipulate DateTime objects, such as retrieving the quarter of a specific date or determining if a date is set on a leap year.

Action | Description | Available as function?
---|---|---
[DiffMonths](libraries/datetime.md#DiffMonths) | Returns the difference in months between 'Datetime1' and ‘Datetime2'; i.e. the number of months between the two dates. | Yes
[DiffQuarters](libraries/datetime.md#DiffQuarters) | Returns the difference in quarters between ‘Datetime1' and 'Datetime2'; i.e. the number of quarters between the two dates. | Yes
[DiffWeeks](libraries/datetime.md#DiffWeeks) | Returns the difference in weeks between ‘Datetime1' and ‘Datetime2'; i.e. the number of weeks between the two dates. | Yes
[DiffYears](libraries/datetime.md#DiffYears) | Returns the difference in years between ‘Datetime1' and ‘Datetime2'; i.e. the number of years between the two dates. | Yes
[GetTicks](libraries/datetime.md#GetTicks) | Returns the number of ticks of 'Datetime’. A single tick represents 100 nanoseconds or one ten-millionth of a second. There are 10,000 ticks in a millisecond. | Yes
[IsLeapYear](libraries/datetime.md#IsLeapYear) | Returns true if the year of ‘Datetime’ is a leap year. | Yes

### HTTP
Provides actions to manipulate HTTP requests and responses.

Action | Description | Available as function?
---|---|---
[Request_AbsoluteURL](libraries/http.md#Request_AbsoluteURL) | Generates an absolute URL based on the URL provided. | Yes
[Request_GetCookie](libraries/http.md#Request_GetCookie) | Returns the value for the specified cookie from the current HTTP request. | Yes
[Request_GetDomain](libraries/http.md#Request_GetDomain) | Returns the host part of the current HTTP request as seen by the browser. <br/> Examples: <br/> When the browser uses the address "http://support.domain.com/site/welcome.aspx?id=12345", Request_GetDomain() = "support.domain.com". | Yes
[Request_GetFiles](libraries/http.md#Request_GetFiles) | Returns the list of files submitted in the current HTTP request. | Yes
[Request_GetHeaders](<libraries/http.md#Request_GetHeaders>) | Returns the value of the specified header in the current HTTP request. | Yes
[Request_GetURL](libraries/http.md#Request_GetURL) | Returns the absolute URL of the current request. If SEO rules are applied, returns the resulting URL and not the URL displayed in the user's browser. | Yes
[Request_ReplaceDomain](libraries/http.md#Request_ReplaceDomain) | Replaces the domain in the URL with the given domain. This function doesn't accept JavaScript as a URL. | Yes
[Request_SubmitGetRequest](libraries/http.md#Request_SubmitGetRequest) |Submits an HTTP GET request given the respective arguments and URL, and returns the request response content. | No
[Response_AddHeader](libraries/http.md#Response_AddHeader) | Adds a header to the current HTTP response. | No
[Response_SetCookie](libraries/http.md#Response_SetCookie) | Sets a cookie in the current HTTP response. | No
[Response_SetStatusCode](libraries/http.md#Response_SetStatusCode) | Sets the status code of the current HTTP response. | No

### Math
The OutSystems Math library provides actions to compute complex math functions, such as logarithmic expression or pseudorandom number generation.

Action | Description | Available as function?
---|---|---
[Ceiling](libraries/math.md#Ceiling) | Returns the smallest long value that is greater than or equal to the decimal number 'Number'. | Yes
[Floor](libraries/math.md#Floor) | Returns the largest long value less than or equal to the decimal number 'Number' | Yes
[LogE](libraries/math.md#LogE) | Returns the logarithm of a specified decimal number (‘Number') in log base E. | Yes
[Log10](libraries/math.md#Log10) | Returns the logarithm of a specified decimal number (‘Number') in log base 10. | Yes
[Log2](libraries/math.md#Log2) | Returns the logarithm of a specified decimal number (‘Number') in log base 2. | Yes
[Random](libraries/math.md#Random) | Generates a random number using a pseudorandom number generator, within a range defined by a minimum value (‘MinVal') and maximum value ('MaxVal'). | Yes

### Sanitization
Library that provides methods to help you avoid code injection in HTML, JavaScript, and SQL snippets that need to include untrusted content, for example, content gathered from end users.

Action | Description | Available as function?
---|---|---
[BuildSafe_InClauseIntegerList](libraries/sanitization.md#BuildSafe_InClauseIntegerList) | Returns a comma-delimited text value containing all the integer values provided as input. The returned value can be safely used in a SQL &quot;IN&quot; clause. | No
[BuildSafe_InClauseTextList](libraries/sanitization.md#BuildSafe_InClauseTextList) | Returns a comma-delimited text value with the encoded version of all the text values provided as input. The returned value can be safely used in a SQL &quot;IN&quot; clause. | No
[SanitizeHtml](libraries/sanitization.md#SanitizeHtml) | Sanitizes the provided HTML using the HtmlSanitizer NuGet package. | Yes
[VerifyJavascriptLiteral](libraries/sanitization.md#VerifyJavascriptLiteral) | Ensures the provided JavaScript only contains JavaScript/JSON literals such as string, array, or Object literals. If it contains anything else, an INVALID JAVASCRIPT LITERAL exception is thrown. Learn more about JavaScript literals in the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#Literals). | Yes

### Security
The OutSystems Security library provides actions to perform several security related operations, such as encrypting and decrypting content or using JSON Web Tokens.

Action | Description | Available as function?
---|---|---
[AES_NewKey](libraries/security.md#AES_NewKey) | Generates a new random AES Key. | No
[AES_Encrypt](libraries/security.md#AES_Encrypt) | Provides authenticated encryption of the text using the provided key (this text will be UTF-8 encoded prior to encryption). Encrypts using AES in Cipher-Block Chaining mode with random initialization vector (IV) and PKCS7 padding. Authenticates by Encrypt-then-MAC with HMAC using the same key, performed over both IV and encrypted message. IV is prepended to the encrypted message. | No
[AES_Decrypt](libraries/security.md#AES_Decrypt) | Decrypts the text using the provided key. Decrypts using AES in Cipher-Block Chaining mode with initialization vector extracted for the start of the ciphertext and PKCS7 padding. Validates the authenticity of the encryption with HMAC using the same key. | No
[CryptoRandomInt](libraries/security.md#CryptoRandomInt) | Generates a random number using a cryptographic random number generator, within a range defined by a minimum value (‘MinVal') and maximum value ('MaxVal'). | No
[GenerateSecurePassword](libraries/security.md#GenerateSecurePassword) | Generates a secure password using a cryptographic random number generator.  | No
[ComputeHash](libraries/security.md#ComputeHash) | Computes the hash of the given data (this data will be UTF-8 encoded prior to hashing). | No
[ComputeMAC](libraries/security.md#ComputeMAC) | Computes the MAC of the given data (this data will be UTF-8 encoded prior). | No
[JWT_SetShowPII](libraries/security.md#JWT_SetShowPII) | Defines whether the personally identifiable information ('PII') is shown on exceptions raised when working with tokens. | No
[JWT_CreateToken](libraries/security.md#JWT_CreateToken) | Creates and signs a JWT token. | No
[JWT_ReadToken](libraries/security.md#JWT_ReadToken) | Extracts claims as well as validates a JWT token. | No
[RSA_NewKey](libraries/security.md#RSA_NewKey) | Generates a new RSA key. | No
[RSA_GetPublicKey](libraries/security.md#RSA_GetPublicKey) | Extracts the public key from an RSA key represented in XML. | No
[RSA_KeyFromPEM](libraries/security.md#RSA_KeyFromPEM) | Reads an RSA key from a PEM file. | No
[RSA_Decrypt](libraries/security.md#RSA_Decrypt) | Decrypts a ciphertext encrypted with RSA. | No
[RSA_Encrypt](libraries/security.md#RSA_Encrypt) | Encrypts a text with RSA (this text will be UTF-8 encoded prior to encryption). | No
[RSA_Sign](libraries/security.md#RSA_Sign) | Signs textual data with an RSA key to provide guarantees the text was produced by the owner of that key (this text will be UTF-8 encoded prior to encryption). | No
[RSA_VerifySignature](libraries/security.md#RSA_VerifySignature) | Verifies the signature of a piece of data against the corresponding RSA public key. | No

### Text
OutSystems Text library provides functionality to manipulate texts as, for example: search and replace using a regular expression, split, join, or format DateTimes.

Action | Description | Available as function?
---|---|---
[Format_DateTime](libraries/text.md#Format_DateTime) | Formats a DateTime by replacing the allowed keywords with their values.<br/>Available Keywords:<br/>[yyyy] - Represents the year as a four-digit number;<br/>[MM] - Represents the month as a number from 01 through 12;<br/>[MMM] - Represents the abbreviated name of the month;<br/>[MMMM] - Represents the full name of the month;<br/>[dd] - Represents the day of the month as a number from 01 through 31;<br/>[ddd] - Represents the abbreviated name of the day of the week;<br/>[dddd] - Represents the full name of the day of the week;<br/>[hh] - Represents the hour as a number from 01 through 12;<br/>[HH] - Represents the hour as a number from 00 through 23;<br/>[mm] - Represents the minute as a number from 0 through 59;<br/>[ss] - Represents the seconds as a number from 00 through 59; | Yes
[Regex_Replace](libraries/text.md#Regex_Replace) | Replaces all occurrences of a specified regular expression pattern with a replacement string. | Yes
[Regex_Search](libraries/text.md#Regex_Search) | Searches the input string for an occurrence of a regular expression. | No
[String_Join](libraries/text.md#String_Join) | Concatenates all the strings in a List, yielding a single string. The individual elements are separated, in the resulting string, by the string Separator. | Yes
[String_LastIndexOf](libraries/text.md#String_LastIndexOf) | Reports the index position of the last occurrence of a specified Pattern within a Text. | Yes
[String_Split](libraries/text.md#String_Split) | Splits a string into individual elements delimited by any of the characters in Delimiters. | Yes
[StringBuilder_Append](libraries/text.md#StringBuilder_Append) | Appends a string to a StringBuilder. | No
[StringBuilder_Create](libraries/text.md#StringBuilder_Create) | Creates a StringBuilder. Use it if you need to create a string by repeatedly appending substrings. A StringBuilder optimizes memory management when dealing with highly dynamic strings. | Yes
[StringBuilder_ToString](libraries/text.md#StringBuilder_ToString) | Returns the content of the StringBuilder's buffer. | Yes

### TextDictionary

Action | Description | Available as function?
---|---|---
TextDictionary_ContainsKey | Determines whether the Dictionary contains a specific key. | Yes
TextDictionary_Create | Initializes a new instance of the Dictionary class. | Yes
TextDictionary_Get | Retrieves an element with a specified key from the Dictionary. | Yes
TextDictionary_Remove | Removes an element with a specified key from the Dictionary. | No
TextDictionary_Set | Adds an element with the specified key and value into the Dictionary. | No

### URL
The OutSystems URL library provides actions to manipulate URLs, such as decoding them to text format or retrieving the URL host.

Action | Description | Available as function?
---|---|---
[DecodeURL](libraries/url.md#DecodeURL) | Converts a string that has been encoded for transmission in a URL into a decoded text value. | Yes
[EncodeURL](libraries/url.md#EncodeURL) | Encodes a URL string for reliable HTTP transmission from the Web server to a client.Converts a string for transmission in a URL into an encoded text value. | Yes
[GetRelativeURL](libraries/url.md#GetRelativeURL) | Returns the relative URL from the base URL. | Yes
[GetURLHost](libraries/url.md#GetURLHost) | Returns the host of the given URL. | Yes
[GetURLProtocol](libraries/url.md#GetURLProtocol) | Returns the protocol of the given URL. | Yes
[IsURLRelative](libraries/url.md#IsURLRelative) | Returns true if the given URL is a relative URL. | Yes

### XML

Action | Description | Available as function?
---|---|---
Serialization_RecordListToXml | Serializes RecordList into XML data. Only records with single entities/structures are supported. | No
Serialization_ObjectToXml | Serializes a Record or a RecordList into XML data. Only records with single entities/structures are supported. | No
Serialization_RecordToXml | Serializes a Record into XML data. Only records with single entities/structures are supported. | No
Serialization_XmlToRecordList | Deserializes a set of Entities definition from an XML data description. | No
XmlAttribute_GetValue | Returns the value of a Xml Attribute.  | No
XmlAttribute_SetValue | Sets the value of a Xml Attribute. | No
XmlDocument_CreateRootElement | Creates a root Xml Element in a Xml Document. | No
XmlDocument_GetRootElement | Returns the root element of a Xml Document. | No
XmlDocument_New | Creates an empty Xml DOM. | No
XmlDocument_Save | Saves the XML document to a string, using UTF-8 encoding. | No
XmlDocument_SelectNodes | Returns a list of Xml Elements or Xml Attributes as described by the XPath string.  | No
XmlDocument_SelectSingleNode | Returns a Xml Element or a Xml Attribute as described by the XPath string. | No
XmlElement_AppendAttribute | Appends a new Xml Attribute to the Element XmlElement. | No
XmlElement_AppendChildElement | Appends a new child Element to XmlElement. | No
XmlElement_GetAttribute | Returns a Xml Attribute with a given name.  | No
XmlElement_GetAttributeValue | Returns the value of a Xml Attribute with a give name.  | No
XmlElement_GetChildByIndex | Returns a child node by index. The index is 0-based. | No
XmlElement_GetChildCount | Returns the number of child nodes in a Xml Element. | No
XmlElement_GetInnerText | Returns the inner text of a Xml Element. | No
XmlElement_GetName | Returns the name of a Xml Element. | No
XmlElement_Remove | Removes a Xml Element. | No
XmlElement_RemoveAttribute | Removes a Xml Attribute.  | No
XmlElement_SelectNodes | Returns a list of Xml Elements or Xml Attributes as described by the XPath string. | No
XmlElement_SelectSingleNode | Returns a Xml Element or a Xml Attribute as described by the XPath string. | No
XmlElement_SetInnerText | Sets the inner text of a Xml Element. | No
XmlNode_GetParentNode | Gets the parent Xml Node of a Xml Node.  | No
XmlNode_GetXmlDocument | Gets the Xml Document to which a specific Xml Node belongs. | No
XmlNodeList_Count | Gets the number of nodes in the Xml Node List. | No
XmlNodeList_Item | Retrieves a node at the given index.  | No
Xsl_Transform | Transforms a Xml content using XLST. | No

### Zip

Action | Description | Available as function?
---|---|---
AddFile | Adds a file to a Zip. The Action CommitChanges must be called after adding all the files. | No
CommitChanges | Commits any changes made to a Zip in memory. If AddFile is used, this Action must be called before GetZipBinary or GetFiles.  | No
CreateZip | Creates a memory representation of a Zip file and returns a handle that must be passed to the other Actions. | No
GetFiles | Returns a list of files and directories contained in a Zip file. | No
GetZipBinary | Returns the binary content of a Zip loaded in memory. | No
LoadZip | Loads a Zip file into memory and returns a handle that must be passed to other Actions. | No

## Built-in functions
When designing the business logic of your apps, you can use built-in functions. They are available in the **Built-in Functions** folder of the expression editor.

### Data Conversion

|Name|Description (abbreviated)|
|--- |--- |
|[BooleanToInteger](built-in-functions/data-conversion.md#BooleanToInteger)|Converts Boolean 'b' to an Integer value, either 1 if 'b' is True or 0 if 'b' is False.|
|[BooleanToText](built-in-functions/data-conversion.md#BooleanToText)|Converts Boolean 'b' to a Text value, either "True" or "False".|
|[DateTimeToDate](built-in-functions/data-conversion.md#DateTimeToDate)|Converts Date Time 'dt' to a Date value dropping the Time component.|
|[DateTimeToText](built-in-functions/data-conversion.md#DateTimeToText)|Converts Date Time 'dt' to a Text value in the format specified in the environment configuration (by default, "yyyy-MM-dd HH:mm:ss").|
|[DateTimeToTime](built-in-functions/data-conversion.md#DateTimeToTime)|Converts Date Time 'dt' to a Time value dropping the Date component.|
|[DateToDateTime](built-in-functions/data-conversion.md#DateToDateTime)|Converts Date 'd' to a Date Time value, adding the Time component (built-in-functions/data-conversion.md#00:00:00#).|
|[DateToText](built-in-functions/data-conversion.md#DateToText)|Converts Date 'd' to a Text value in the format specified in the environment configuration (by default, "yyyy-MM-dd").|
|[DecimalToBoolean](built-in-functions/data-conversion.md#DecimalToBoolean)|Converts Decimal 'd' to a Boolean value. Decimal value of 0.0 is False. Any other value is True.|
|[DecimalToInteger](built-in-functions/data-conversion.md#DecimalToInteger)|Converts Decimal 'd' to an Integer value.|
|[DecimalToIntegerValidate](built-in-functions/data-conversion.md#DecimalToIntegerValidate)|Returns true if Decimal 'd' can be converted to an Integer value.|
|[DecimalToLongInteger](built-in-functions/data-conversion.md#DecimalToLongInteger)|Converts Decimal 'd' to a Long Integer value.|
|[DecimalToLongIntegerValidate](built-in-functions/data-conversion.md#DecimalToLongIntegerValidate)|Returns true if Decimal 'd' can be converted to a Long Integer value.|
|[DecimalToText](built-in-functions/data-conversion.md#DecimalToText)|Converts Decimal 'd' to a Text value.|
|[LongIntegerToInteger](built-in-functions/data-conversion.md#LongIntegerToInteger)|Converts Long Integer 'l' to an Integer value.|
|[LongIntegerToIntegerValidate](built-in-functions/data-conversion.md#LongIntegerToIntegerValidate)|Returns true if Long Integer 'l' can be converted to an Integer value.|
|[LongIntegerToIdentifier](built-in-functions/data-conversion.md#LongIntegerToIdentifier)|Converts Long Integer 'l' to a Long Integer Identifier.|
|[LongIntegerToText](built-in-functions/data-conversion.md#LongIntegerToText)|Converts Long Integer 'l' to a Text value.|
|[IdentifierToInteger](built-in-functions/data-conversion.md#IdentifierToInteger)|Converts Identifier 'Id' to an Integer value.|
|[IdentifierToLongInteger](built-in-functions/data-conversion.md#IdentifierToLongInteger)|Converts Identifier 'Id' to a Long Integer value.|
|[IdentifierToText](built-in-functions/data-conversion.md#IdentifierToText)|Converts Identifier 'Id' to a Text value.|
|[IntegerToBoolean](built-in-functions/data-conversion.md#IntegerToBoolean)|Converts Integer 'i' to a Boolean value. Boolean value of 0 is False. Any other value is True.|
|[IntegerToDecimal](built-in-functions/data-conversion.md#IntegerToDecimal)|Converts Integer 'i' to a Decimal value.|
|[IntegerToIdentifier](built-in-functions/data-conversion.md#IntegerToIdentifier)|Converts Integer 'i' to an Integer Identifier.|
|[IntegerToText](built-in-functions/data-conversion.md#IntegerToText)|Converts Integer 'i' to a Text value.|
|[NullDate](built-in-functions/data-conversion.md#NullDate)|Returns a null Date value.|
|[NullIdentifier](built-in-functions/data-conversion.md#NullIdentifier)|Returns a null Identifier valid for Integer and Long Integer Identifiers.|
|[NullObject](built-in-functions/data-conversion.md#NullObject)|Returns a null Object value.|
|[NullBinary](built-in-functions/data-conversion.md#NullBinary)|Returns a null Binary Data value.|
|[NullTextIdentifier](built-in-functions/data-conversion.md#NullTextIdentifier)|Returns a null Text Identifier.|
|[TextToDate](built-in-functions/data-conversion.md#TextToDate)|Converts Text 't' to a Date value.|
|[TextToDateTime](built-in-functions/data-conversion.md#TextToDateTime)|Converts Text 't' to a Date Time value.|
|[TextToDateTimeValidate](built-in-functions/data-conversion.md#TextToDateTimeValidate)|Returns true if Text 't' can be converted to a Date Time value.|
|[TextToDateValidate](built-in-functions/data-conversion.md#TextToDateValidate)|Returns true if Text 't' can be converted to a Date value.|
|[TextToDecimal](built-in-functions/data-conversion.md#TextToDecimal)|Converts Text 't' to a Decimal value.|
|[TextToDecimalValidate](built-in-functions/data-conversion.md#TextToDecimalValidate)|Returns true if Text 't' can be converted to a Decimal value.|
|[TextToIdentifier](built-in-functions/data-conversion.md#TextToIdentifier)|Converts Text 't' to a Text Identifier.|
|[TextToInteger](built-in-functions/data-conversion.md#TextToInteger)|Converts Text 't' to an Integer value.|
|[TextToLongInteger](built-in-functions/data-conversion.md#TextToLongInteger)|Converts Text 't' to a Long Integer value.|
|[TextToIntegerValidate](built-in-functions/data-conversion.md#TextToIntegerValidate)|Returns true if Text 't' can be converted to an Integer value.|
|[TextToLongIntegerValidate](built-in-functions/data-conversion.md#TextToLongIntegerValidate)|Returns true if Text 't' can be converted to a Long Integer value.|
|[TextToTime](built-in-functions/data-conversion.md#TextToTime)|Converts Text 't' to a Time value.|
|[TextToTimeValidate](built-in-functions/data-conversion.md#TextToTimeValidate)|Returns true if Text 't' can be converted to a Time value.|
|[TimeToText](built-in-functions/data-conversion.md#TimeToText)|Converts Time 't' to a Text value in the format "HH:mm:ss".|
|[ToObject](built-in-functions/data-conversion.md#ToObject)|Converts expression 'exp' to an Object value.|

### Date and Time

| Name | Description (abbreviated) |
| --- | --- |
| [AddDays](built-in-functions/dateandtime.md#AddDays) | Adds 'n' days to 'dt' and returns a valid Date Time. |
| [AddHours](built-in-functions/dateandtime.md#AddHours) | Adds 'n' hours to 'dt' and returns a valid Date Time. |
| [AddMinutes](built-in-functions/dateandtime.md#AddMinutes) | Adds 'n' minutes to 'dt' and returns a valid Date Time. |
| [AddMonths](built-in-functions/dateandtime.md#AddMonths) | Adds 'n' months to 'dt' and returns a valid Date Time. |
| [AddSeconds](built-in-functions/dateandtime.md#AddSeconds) | Adds 'n' seconds to 'dt' and returns a valid Date Time. |
| [AddYears](built-in-functions/dateandtime.md#AddYears) | Adds 'n' years to 'dt' and returns a valid Date Time. |
| [BuildDateTime](built-in-functions/dateandtime.md#BuildDateTime) | Returns a Date Time made up of the Date 'd' and Time 't'. |
| [CurrDate](built-in-functions/dateandtime.md#CurrDate) | Client-side calls return the device date and time. |
| [CurrDateTime](built-in-functions/dateandtime.md#CurrDateTime) | Client-side calls return the device date and time.|
| [CurrTime](built-in-functions/dateandtime.md#CurrTime) | Client-side calls return the device date and time. |
| [Day](built-in-functions/dateandtime.md#Day) | Returns the day of 'dt'. |
| [DayOfWeek](built-in-functions/dateandtime.md#DayOfWeek) | Returns the week day of 'dt', ranging from 0 (Sunday) to 6 (Saturday). |
| [DiffDays](built-in-functions/dateandtime.md#DiffDays) | Returns the difference in days between 'dt1' and 'dt2'; i.e. how many days have passed between these two dates. |
| [DiffHours](built-in-functions/dateandtime.md#DiffHours) | Returns the difference in hours between 'dt1' and 'dt2'; i.e. how many hours have passed between these two dates. |
| [DiffMinutes](built-in-functions/dateandtime.md#DiffMinutes) | Returns the difference in minutes between 'dt1' and 'dt2'; i.e. how many minutes have passed between these two dates. |
| [DiffSeconds](built-in-functions/dateandtime.md#DiffSeconds) | Returns the difference in seconds between 'dt1' and 'dt2'; i.e. how many seconds have passed between these two dates. |
| [Hour](built-in-functions/dateandtime.md#Hour) | Returns the hour of 'dt'. |
| [Minute](built-in-functions/dateandtime.md#Minute) | Returns the minute of 'dt'. |
| [Month](built-in-functions/dateandtime.md#Month) | Returns the month of 'dt'. |
| [NewDate](built-in-functions/dateandtime.md#NewDate) | Returns a Date made up of year 'y', month 'm' and day 'd'. |
| [NewDateTime](built-in-functions/dateandtime.md#NewDateTime) | Returns a Date Time made up of year 'y', month 'mo', day 'd', hour 'h', minute 'mi' and second 's'. |
| [NewTime](built-in-functions/dateandtime.md#NewTime) | Returns a Time made up of hour 'h', minute 'm' and second 's'. |
| [Second](built-in-functions/dateandtime.md#Second) | Returns the seconds of 'dt'. |
| [Year](built-in-functions/dateandtime.md#Year) | Returns the year of 'dt'. |

### Email

|Name|Description (abbreviated)|
|--- |--- |
|[EmailAddressCreate](built-in-functions/email.md#EmailAddressCreate)|Returns a full email address string containing the display name (usually it's the name of the email address owner) and the email address itself.|
|[EmailAddressValidate](built-in-functions/email.md#EmailAddressValidate)|Returns true if Text 'address' is a valid email address.|

### Format

| Name | Description (abbreviated) |
| --- | --- |
| [FormatCurrency](built-in-functions/format.md#FormatCurrency) | Builds a Text output of the specified Currency 'value', preceded by the currency 'symbol', using 'decimal\_digits' after the decimal point.|
| [FormatDecimal](built-in-functions/format.md#FormatDecimal) | Builds a Text output of the specified Decimal 'value', using 'decimal\_digits' after the decimal point.|
| [FormatPercent](built-in-functions/format.md#FormatPercent) | Builds a Text output of the specified Decimal 'value', followed by '%' using 'decimal\_digits' after the decimal point.|
| [FormatPhoneNumber](built-in-functions/format.md#FormatPhoneNumber) | Builds a Text output of the specified phone number Text 'value', starting with the international separator 'int\_separator', followed by the first 'int\_code\_digits' of 'value', then the 'area\_separator', then the following 'area\_code\_digits' of 'value', then the 'phone\_separator' and finally the following 'phone\_digits' of 'value'. |
| [FormatText](built-in-functions/format.md#FormatText) | Builds a Text output of the specified Text 'value', by limiting it to the specified 'max\_chars' count.|
| [FormatDateTime](built-in-functions/format.md#FormatDateTime) | Builds a Text output of the specified Date Time 'value' using the specified 'format'.|

### Math

| Name | Description |
| --- | --- |
| [Abs](built-in-functions/math.md#Abs) | Returns the absolute value (unsigned magnitude) of the decimal number 'n'. |
| [Mod](built-in-functions/math.md#Mod) | Returns the remainder of decimal division of 'n' by 'm'. |
| [Power](built-in-functions/math.md#Power) | Returns 'n' raised to the power of 'm'. |
| [Round](built-in-functions/math.md#Round) | Returns the Decimal number 'n' rounded to a specific number of 'fractional digits'. |
| [Sqrt](built-in-functions/math.md#Sqrt) | Returns the square root of the Decimal number 'n'. |
| [Trunc](built-in-functions/math.md#Trunc) | Returns the Decimal number 'n' truncated to integer removing the decimal part of 'n'. |

### Numeric

| Name | Description |
| --- | --- |
| [Max](built-in-functions/numeric.md#Max) | Returns the largest number of 'n' and 'm'. |
| [Min](built-in-functions/numeric.md#Min) | Returns the smallest number of 'n' and 'm'. |
| [Sign](built-in-functions/numeric.md#Sign) | Returns -1 if 'n' is negative; 1 if 'n' is positive; 0 if 'n' is 0. |

### Organization

|Name|Description|
|--- |--- |
|[GetCurrentLocale](built-in-functions/organization.md#GetCurrentLocale)|Returns the name of the current language locale of the user session. The name of the language locale is used for presentation purposes and follows the RFC 1766 standard format.|
|[GetUserAgent](built-in-functions/organization.md#GetUserAgent)|Returns the user agent, as indicated by the header of the HTTP message.|
|[GetAppName](built-in-functions/organization.md#GetAppName)|Returns the name of the app that is processing the request.|

### Text

| Name | Description (abbreviated) |
| --- | --- |
| [Chr](built-in-functions/text.md#Chr) | Returns a single-character string corresponding to the 'c' character code. |
| [EncodeHtml](built-in-functions/text.md#EncodeHtml) | Replaces special characters in a string so that you can use it in HTML literals.|
| [EncodeJavaScript](built-in-functions/text.md#EncodeJavaScript) | Replaces special characters in a string so that you can use it in JavaScript literals.|
| [EncodeSql](built-in-functions/text.md#EncodeSql) | Replaces special characters in a string literal so that you can use it in a SQL statement.|
| [EncodeUrl](built-in-functions/text.md#EncodeUrl) | Replaces all non-alphanumeric characters in a string, i.e. characters outside of the [0-9a-zA-Z] range, so that you can safely use it in URL parameter values.|
| [Index](built-in-functions/text.md#Index) | Returns the zero-based position in Text 't' where 'search' Text can be found. Returns -1 if 'search' is not found or if 'search' is empty. |
| [Length](built-in-functions/text.md#Length) | Returns the number of characters in Text 't'. |
| [NewLine](built-in-functions/text.md#NewLine) | Returns a string containing the New Line (Return) character. |
| [Replace](built-in-functions/text.md#Replace) | Returns Text 't' after replacing all Text occurrences of 'search' with 'replace'. |
| [Substr](built-in-functions/text.md#Substr) | Returns a sub-string of 't' beginning at 'start' zero-based position and with 'length' characters. |
| [ToLower](built-in-functions/text.md#ToLower) | Converts Text 't' to the equivalent lowercase text. |
| [ToUpper](built-in-functions/text.md#ToUpper) | Converts Text 't' to the equivalent uppercase text. |
| [Trim](built-in-functions/text.md#Trim) | Removes all leading and trailing space characters (' ') from Text 't'. |
| [TrimEnd](built-in-functions/text.md#TrimEnd) | Removes all trailing space characters (' ') from Text 't'. |
| [TrimStart](built-in-functions/text.md#TrimStart) | Removes all leading space characters (' ') from Text 't'. |

### URL

| Name |  Description (abbreviated) |
| --- | --- |
| [GetBookmarkableURL](built-in-functions/url.md#GetBookmarkableURL) | Returns the URL of the screen that is currently being processed.|

| [GetOwnerURLPath](built-in-functions/url.md#GetOwnerURLPath) | Returns the URL path of the app that owns the element that is being processed.|

## System actions
When designing the business logic of your apps, you can use built-in system actions. They're available in:

* **Client Actions** > **(System)** folder in the Logic tab in ODC Studio.
* **Server Actions** > **(System)** folder in the Logic tab in ODC Studio.

### Authentication
Authentication actions for built-in and/or external identity providers.

Action | Description | Client or Server? | Available as function?
---|---|---|---
[Login](system-actions/auth.md#login) | Performs a login in to the built-in identity provider using a username and password. If RememberDevice is true, keeps the user logged in for 2 weeks or until a Logout is performed. User profile information is synchronized to the User entity before this action is finished. Throws an exception if the built-in identity provider is disabled for the current app. | Client | No
[GetExternalLoginURL](system-actions/auth.md#getexternalloginurl)(*) | Returns the URL to which the user should be redirected in order to login in an external provider. | Client | No
[Logout](system-actions/auth.md#logout) | Logs out the user from the built-in identity provider. | Client | No
[GetExternalLogoutURL](system-actions/auth.md#getexternallogouturl)(*) | Returns the URL where the user can log out of an external identity provider, if one is configured, or "" otherwise. | Client | No

<div class="info" markdown="1">

(*) You must first add this action due to a temporary technical limitation. Navigate to the **Add public elements** icon on the top toolbar of ODC Studio or use the **Ctrl+Q** shortcut. Search for the action, select it, and click **Add**.

</div>

### User
User actions for built-in and/or external identity providers.

Action | Description | Client or Server? | Available as function?
---|---|---|---
[ChangePassword](system-actions/user.md#changepassword) | Allows a logged-in user to change their password. Throws an exception if the built-in identity provider is disabled for the current app. | Client | No
[FinishResetPassword](system-actions/user.md#finishresetpassword) | Finalizes the reset password operation, using a verification code that can be received by email. Throws an exception if the built-in identity provider is disabled for the current app. | Client | No
[FinishUserRegistration](system-actions/user.md#finishuserregistration)(*) | Sets the user as active and their password in the built-in identity provider and logs the user in.<br/>Call the action StartUserRegistration to register the user and obtain a temporary password. | Client | No
[GetPasswordComplexityPolicy](system-actions/user.md#getpasswordcomplexitypolicy) | Gets the configured password policy for the built-in identity provider. Used to enable client-side validation in a user registration flow. Throws an exception if the built-in identity provider is disabled for the current app. | Client | No
[GetUserProfile](system-actions/user.md#getuserprofile) | Returns logged-in user's information from the identity provider and updates the user entity with that information. | Client | No
[IsExternalUser](system-actions/user.md#isexternaluser) | Returns logged-in user's information from the identity provider and updates the user entity with that information. | Client | Yes
[ResetPassword](system-actions/user.md#resetpassword) | Allows a user to reset their password using a verification code received via email. Throws an exception if the built-in identity provider is disabled for the current app. | Client | No
[SendResetPasswordEmail](system-actions/user.md#sendresetpasswordemail) | Triggers the reset password flow, which sends an email to the user with a verification code used to reset the password. Throws an exception if the built-in identity provider is disabled for the current app. | Client | No
[StartResetPassword](system-actions/user.md#startresetpassword) | Triggers the reset password operation, returning a verification code that can be sent by email to the user. Use the FinishResetPassword action, which receives a verification code as an input, to complete the password reset operation. Throws an exception if the built-in identity provider is disabled for the current app. | Server | No
[StartUserRegistration](system-actions/user.md#startuserregistration)(*) | Registers the user in the built-in identity provider by creating the user as inactive and setting a temporary password. Synchronises the User entity with the identity provider.<br/>Call the action FinishUserRegistration to activate the user and change the password.<br/>It throws an exception if the built-in identity provider is disabled for the current app. | Server | No
[UpdateUserProfile](system-actions/user.md#updateuser) | Allows a logged-in user to edit profile information. The user email can't be changed using this action. Throws an exception if the built-in identity provider is disabled for the current app. | Server | No
[ValidatePasswordComplexity](system-actions/user.md#validatepasswordcomplexity) | Validates a user's password against the password complexity policy. Throws an exception if the built-in identity provider is disabled for the current app. | Client | No

<div class="info" markdown="1">

(*) You must first add this action due to a temporary technical limitation. Navigate to the **Add public elements** icon on the top toolbar of ODC Studio or use the **Ctrl+Q** shortcut. Search for the action, select it, and click **Add**.

</div>

