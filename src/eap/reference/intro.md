---
summary: Reference content.
tags:
locale: en-us
guid: f9d530c1-f9fa-4b08-9e75-5dfb984402da
app_type: mobile apps, reactive web apps
---

# Reference

## Libraries
Libraries provided by OutSystems that you can use to extend the capabilities of your apps. To learn more about how to use these libraries see [here](../building-apps/logic/use-public-elements.md).

### Binary Data
The OutSystems BinaryData library provides actions to manipulate binary data, such as retrieving the length or transforming binary content into Text or Base64.

Action | Description | Available as function?
---|---|---
[Base64ToBinary](<libraries/binarydata.md#Base64ToBinary>) | Converts Base64 Text into BinaryData. | Yes
[BinaryDataSize](<libraries/binarydata.md#BinaryDataSize>) | Returns the size in bytes of a binary content. | Yes
[BinaryDataToHex](<libraries/binarydata.md#BinaryDataToHex>) | Converts the given binary data to hexadecimal representation. | Yes
[BinaryDataToText](<libraries/binarydata.md#BinaryDataToText>) | Reads the content of a text file using a given encoding. If no encoding is supplied, the system's default ANSI encoding will be used. | Yes
[BinaryToBase64](<libraries/binarydata.md#BinaryToBase64>) | Converts BinaryData into Base64 Text. | Yes
[Compare](<libraries/binarydata.md#Compare>) | Performs a binary comparison between two Binary Data contents. | Yes
[ConvertEncoding](<libraries/binarydata.md#ConvertEncoding>) | Converts a range of bytes in a BinaryData from one encoding to another. | Yes
[TextToBinaryData](<libraries/binarydata.md#TextToBinaryData>) | Converts a Text into binary content. If no encoding is supplied, the system's default ANSI encoding will be used. | Yes

### Date Time
The OutSystems DateTime library provides actions to access and manipulate DateTime objects, such as retrieving the quarter of a specific date or determining if a date is set on a leap year.

Action | Description | Available as function?
---|---|---
[DiffMonths](<libraries/datetime.md#DiffMonths>) | Returns the difference in months between 'Datetime1' and ‘Datetime2'; i.e. the number of months between the two dates. | Yes
[DiffQuarters](<libraries/datetime.md#DiffQuarters>) | Returns the difference in quarters between ‘Datetime1' and 'Datetime2'; i.e. the number of quarters between the two dates. | Yes
[DiffWeeks](<libraries/datetime.md#DiffWeeks>) | Returns the difference in weeks between ‘Datetime1' and ‘Datetime2'; i.e. the number of weeks between the two dates. | Yes
[DiffYears](<libraries/datetime.md#DiffYears>) | Returns the difference in years between ‘Datetime1' and ‘Datetime2'; i.e. the number of years between the two dates. | Yes
[GetTicks](<libraries/datetime.md#GetTicks>) | Returns the number of ticks of 'Datetime’. A single tick represents 100 nanoseconds or one ten-millionth of a second. There are 10,000 ticks in a millisecond. | Yes
[IsLeapYear](<libraries/datetime.md#IsLeapYear>) | Returns true if the year of ‘Datetime’ is a leap year. | Yes

### HTTP
Provides actions to manipulate HTTP requests and responses.

Action | Description | Available as function?
---|---|---
[AddAttributeToHtmlTag](<libraries/http.md#AddAttributeToHtmlTag>) | Adds an attribute to the outermost HTML tag of the document (e.g. xmlns, manifest...).<br/>This method has no effect in Ajax Requests. | Yes
[AddFaviconTag](<libraries/http.md#AddFaviconTag>) | Allows setting the favicon for the current page. You can use &quot;omlresources&quot; to add an icon file to your oml.<br/>This method has no effect in Ajax Requests. | Yes
[AddHeader](<libraries/http.md#AddHeader>) | Adds a header to the current HTTP response.<br/>This method has no effect in Ajax Requests. | No
[AddJavaScriptTag](<libraries/http.md#AddJavaScriptTag>) | Adds a &lt;script&gt; tag to the HTML of the current HTTP response.<br/>This method has no effect in Ajax Requests. | Yes
[AddLinkTag](<libraries/http.md#AddLinkTag>) | Adds a &lt;link&gt; tag to the HTML of the current HTTP response.<br/>This method has no effect in Ajax Requests. | Yes
[AddMetaHttpEquivTag](<libraries/http.md#AddMetaHttpEquivTag>) | Adds a &lt;meta&gt; tag with the http-equiv attribute to the HTML of the current HTTP response.<br/>This method has no effect in Ajax Requests. | Yes
[AddMetaTag](<libraries/http.md#AddMetaTag>) | Adds a &lt;meta&gt; tag to the HTML of the current HTTP response.<br/>This method has no effect in Ajax Requests. | Yes
[AddPostProcessingFilter](<libraries/http.md#AddPostProcessingFilter>) | This method has no effect in Ajax Requests.<br/>Not implemented in Java. | Yes
[AddSessionToURL](<libraries/http.md#AddSessionToURL>) | Adds the current session identifier to a specified URL. | Yes
[AddStyleSheetTag](<libraries/http.md#AddStyleSheetTag>) | Adds a &lt;link rel=&quot;stylesheet&quot;&gt; tag to the HTML of the current HTTP response.<br/>This method has no effect in Ajax Requests. | Yes
[GetCookie](<libraries/http.md#GetCookie>) | Gets a cookie value. | Yes
[GetEntryURL](<libraries/http.md#GetEntryURL>) | Returns the URL of an Entry. Includes the Personal Area and the session identifier if applicable. | Yes
[GetFormValue](<libraries/http.md#GetFormValue>) | Gets the value of a form field of the current HTTP request.<br/>If the field does not exist in the request an empty String will be returned. The same applies when the field exists but has an empty string as a value. | Yes
[GetIP](<libraries/http.md#GetIP>) | Gets the IP host address of the remote client (IP of the user machine performing the HTTP request). | Yes
[GetPageExtension](<libraries/http.md#GetPageExtension>) | Returns the extension of the physical page that corresponds to the current screen, including the dot. Examples: &quot;.aspx&quot; or &quot;.jsf&quot;. | Yes
[GetPageName](<libraries/http.md#GetPageName>) | Returns the name of the physical page that corresponds to the current screen. It is usually the same as the screen name, except when name clashes occur. | Yes
[GetRawURL](<libraries/http.md#GetRawURL>) | Returns the current relative requested URL, without the http://[server] part and without the session identifier.<br/>If SEO rules are being applied, the URL displayed in the user's browser is returned, and not the final URL after the rule is applied. | Yes
[GetReferrerURL](<libraries/http.md#GetReferrerURL>) |  | Yes
[GetRequest_AddArgument](<libraries/http.md#GetRequest_AddArgument>) | Builds the arguments string for an HTTP request with method GET, adding a new parameter to the arguments string. | Yes
[GetRequest_Submit](<libraries/http.md#GetRequest_Submit>) | Submit an HTTP GET request given the GET arguments and the URL. Returns the response content as a string and as binary data. | No
[GetRequestContent](<libraries/http.md#GetRequestContent>) | Gets the content of the current HTTP request. | Yes
[GetRequestDomain](<libraries/http.md#GetRequestDomain>) | Returns the host part of the current HTTP request as seen by the browser.<br/>Example: when the browser uses the address &quot;http://support.example.com/site/welcome.aspx?id=12345&quot;, GetRequestDomain() returns &quot;support.example.com&quot;. | Yes
[GetRequestFiles](<libraries/http.md#GetRequestFiles>) | Returns the list of files submitted in the current HTTP request. | Yes
[GetRequestHeader](<libraries/http.md#GetRequestHeader>) | Gets the value of a specific header in the current HTTP request. Returns an empty string if the header is not present or has no value. | Yes
[GetRunningESpaceJQueryVersion](<libraries/http.md#GetRunningESpaceJQueryVersion>) | Returns the jQueryVersion of the Running ESpace | Yes
[GetSessionId](<libraries/http.md#GetSessionId>) | Gets the session identifier of the current HTTP request. | Yes
[GetURL](<libraries/http.md#GetURL>) | Returns the current absolute requested URL, without the session identifier.<br/>If SEO rules are being applied, the final URL after the rule is applied is returned, and not the URL displayed in the user's browser. | Yes
[GetURLMethod](<libraries/http.md#GetURLMethod>) | Gets the request method (GET or POST) of the current requested URL. | Yes
[GetURLWithSession](<libraries/http.md#GetURLWithSession>) | Gets the current requested URL (with the session identifier). | Yes
[GetUserAgent](<libraries/http.md#GetUserAgent>) | Gets the user agent of the current HTTP request. | Yes
[GetUserLanguages](<libraries/http.md#GetUserLanguages>) | Gets a sorted record list of client language preferences. | Yes
[GetValueFromInputId](<libraries/http.md#GetValueFromInputId>) |  | Yes
[GetValueFromInputIdDecoded](<libraries/http.md#GetValueFromInputIdDecoded>) |  | Yes
[IsAjaxRequest](<libraries/http.md#IsAjaxRequest>) | Returns true if this is running in an AJAX request.<br/>Not Implemented in Java. | Yes
[IsSecureConnection](<libraries/http.md#IsSecureConnection>) | Tells if the current request is being made via HTTPS. | Yes
[MakeAbsoluteURL](<libraries/http.md#MakeAbsoluteURL>) | Makes an absolute URL based on the URL provided. | Yes
[PostRequest_AddArgument](<libraries/http.md#PostRequest_AddArgument>) | Builds arguments list for a POST HTTP request, adding a new text parameter to the arguments list. If argument name is not supplied, the post will only submit the supplied value (this can be used for xml posts for example). | Yes
[PostRequest_AddBinaryArgument](<libraries/http.md#PostRequest_AddBinaryArgument>) | Builds arguments list for an HTTP request, adding a new binary parameter to the arguments list. If argument name is not supplied, the post will only submit the supplied value (this can be used for xml posts for example). | Yes
[PostRequest_Submit](<libraries/http.md#PostRequest_Submit>) | Submit an HTTP POST request given the POST arguments and the URL. Returns the response content as a string and as binary data. | No
[ReplaceURLDomain](<libraries/http.md#ReplaceURLDomain>) | Replaces the domain in the URL by the new domain. This function doesn't accept JavaScript as an URL. If the new domain is not provided, the domain of the current request is used. | Yes
[RunJavaScript](<libraries/http.md#RunJavaScript>) | Runs the provided JavaScript code in the browser. | Yes
[SetBaseTag](<libraries/http.md#SetBaseTag>) | Sets the base tag of the HTML of the current HTTP response.<br/>This method has no effect in Ajax Requests. | Yes
[SetCookie](<libraries/http.md#SetCookie>) | Sets a cookie. | No
[SetLastModified](<libraries/http.md#SetLastModified>) | Sets the Last Modified Date HTTP header of the current response. | Yes
[SetPageTitle](<libraries/http.md#SetPageTitle>) | Sets the page title of the HTML of the current HTTP response.<br/>This method has no effect in Ajax Requests. | Yes
[SetRequestTimeout](<libraries/http.md#SetRequestTimeout>) | Sets the timeout of the current HTTP request. | No
[SetStatusCode](<libraries/http.md#SetStatusCode>) | Sets the status code of the current HTTP response. | No
[URLEncode](<libraries/http.md#URLEncode>) | Encodes a URL string for reliable HTTP transmission from the Web server to a client | Yes

### Math
The OutSystems Math library provides actions to compute complex math functions, such as logarithmic expression or pseudorandom number generation.

Action | Description | Available as function?
---|---|---
[Ceiling](<libraries/math.md#Ceiling>) | Returns the smallest long value that is greater than or equal to the decimal number 'Number'. | Yes
[Floor](<libraries/math.md#Floor>) | Returns the largest long value less than or equal to the decimal number 'Number' | Yes
[LogE](<libraries/math.md#LogE>) | Returns the logarithm of a specified decimal number (‘Number') in log base E. | Yes
[Log10](<libraries/math.md#Log10>) | Returns the logarithm of a specified decimal number (‘Number') in log base 10. | Yes
[Log2](<libraries/math.md#Log2>) | Returns the logarithm of a specified decimal number (‘Number') in log base 2. | Yes
[Random](<libraries/math.md#Random>) | Generates a random number using a pseudorandom number generator, within a range defined by a minimum value (‘MinVal') and maximum value ('MaxVal'). | Yes

### Sanitization
Library that provides methods to help you avoid code injection in HTML, JavaScript, and SQL snippets that need to include untrusted content, for example, content gathered from end users.

Action | Description | Available as function?
---|---|---
[BuildSafe_InClauseIntegerList](<libraries/sanitization.md#BuildSafe_InClauseIntegerList>) | Returns a comma-delimited text value containing all the integer values provided as input. The returned value can be safely used in a SQL &quot;IN&quot; clause. | No
[BuildSafe_InClauseTextList](<libraries/sanitization.md#BuildSafe_InClauseTextList>) | Returns a comma-delimited text value with the encoded version of all the text values provided as input. The returned value can be safely used in a SQL &quot;IN&quot; clause. | No
[SanitizeHtml](<libraries/sanitization.md#SanitizeHtml>) | Sanitizes the provided HTML using the HtmlSanitizer NuGet package. | Yes
[VerifyJavascriptLiteral](<libraries/sanitization.md#VerifyJavascriptLiteral>) | Ensures the provided JavaScript only contains JavaScript/JSON literals such as string, array, or Object literals. If it contains anything else, an INVALID JAVASCRIPT LITERAL exception is thrown. Learn more about JavaScript literals in the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#Literals). | Yes

### Security
The OutSystems Security library provides actions to perform several security related operations, such as encrypting and decrypting content or using JSON Web Tokens.

Action | Description | Available as function?
---|---|---
[AES_NewKey](<libraries/security.md#AES_NewKey>) | Generates a new random AES Key. | No
[AES_Encrypt](<libraries/security.md#AES_Encrypt>) | Provides authenticated encryption of the text using the provided key (this text will be UTF-8 encoded prior to encryption). Encrypts using AES in Cipher-Block Chaining mode with random initialization vector (IV) and PKCS7 padding. Authenticates by Encrypt-then-MAC with HMAC using the same key, performed over both IV and encrypted message. IV is prepended to the encrypted message. | No
[AES_Decrypt](<libraries/security.md#AES_Decrypt>) | Decrypts the text using the provided key. Decrypts using AES in Cipher-Block Chaining mode with initialization vector extracted for the start of the ciphertext and PKCS7 padding. Validates the authenticity of the encryption with HMAC using the same key. | No
[CryptoRandomInt](<libraries/security.md#CryptoRandomInt>) | Generates a random number using a cryptographic random number generator, within a range defined by a minimum value (‘MinVal') and maximum value ('MaxVal'). | No
[GenerateSecurePassword](<libraries/security.md#GenerateSecurePassword>) | Generates a secure password using a cryptographic random number generator.  | No
[ComputeHash](<libraries/security.md#ComputeHash>) | Computes the hash of the given data (this data will be UTF-8 encoded prior to hashing). | No
[ComputeMAC](<libraries/security.md#ComputeMAC>) | Computes the MAC of the given data (this data will be UTF-8 encoded prior). | No
[JWT_SetShowPII](<libraries/security.md#JWT_SetShowPII>) | Defines whether the personally identifiable information ('PII') is shown on exceptions raised when working with tokens. | No
[JWT_CreateToken](<libraries/security.md#JWT_CreateToken>) | Creates and signs a JWT token. | No
[JWT_ReadToken](<libraries/security.md#JWT_ReadToken>) | Extracts claims as well as validates a JWT token. | No
[RSA_NewKey](<libraries/security.md#RSA_NewKey>) | Generates a new RSA key. | No
[RSA_GetPublicKey](<libraries/security.md#RSA_GetPublicKey>) | Extracts the public key from an RSA key represented in XML. | No
[RSA_KeyFromPEM](<libraries/security.md#RSA_KeyFromPEM>) | Reads an RSA key from a PEM file. | No
[RSA_Decrypt](<libraries/security.md#RSA_Decrypt>) | Decrypts a ciphertext encrypted with RSA. | No
[RSA_Encrypt](<libraries/security.md#RSA_Encrypt>) | Encrypts a text with RSA (this text will be UTF-8 encoded prior to encryption). | No
[RSA_Sign](<libraries/security.md#RSA_Sign>) | Signs textual data with an RSA key to provide guarantees the text was produced by the owner of that key (this text will be UTF-8 encoded prior to encryption). | No
[RSA_VerifySignature](<libraries/security.md#RSA_VerifySignature>) | Verifies the signature of a piece of data against the corresponding RSA public key. | No

### Text
OutSystems Text library provides functionality to manipulate texts as, for example: search and replace using a regular expression, split, join, or format DateTimes.

Action | Description | Available as function?
---|---|---
[Format_DateTime](<libraries/text.md#Format_DateTime>) | Formats a DateTime by replacing the allowed keywords with their values.<br/>Available Keywords:<br/>[yyyy] - Represents the year as a four-digit number;<br/>[MM] - Represents the month as a number from 01 through 12;<br/>[MMM] - Represents the abbreviated name of the month;<br/>[MMMM] - Represents the full name of the month;<br/>[dd] - Represents the day of the month as a number from 01 through 31;<br/>[ddd] - Represents the abbreviated name of the day of the week;<br/>[dddd] - Represents the full name of the day of the week;<br/>[hh] - Represents the hour as a number from 01 through 12;<br/>[HH] - Represents the hour as a number from 00 through 23;<br/>[mm] - Represents the minute as a number from 0 through 59;<br/>[ss] - Represents the seconds as a number from 00 through 59; | Yes
[Regex_Replace](<libraries/text.md#Regex_Replace>) | Replaces all occurrences of a specified regular expression pattern with a replacement string. | Yes
[Regex_Search](<libraries/text.md#Regex_Search>) | Searches the input string for an occurrence of a regular expression. | No
[String_Join](<libraries/text.md#String_Join>) | Concatenates all the strings in a List, yielding a single string. The individual elements are separated, in the resulting string, by the string Separator. | Yes
[String_LastIndexOf](<libraries/text.md#String_LastIndexOf>) | Reports the index position of the last occurrence of a specified Pattern within a Text. | Yes
[String_Split](<libraries/text.md#String_Split>) | Splits a string into individual elements delimited by any of the characters in Delimiters. | Yes
[StringBuilder_Append](<libraries/text.md#StringBuilder_Append>) | Appends a string to a StringBuilder. | No
[StringBuilder_Create](<libraries/text.md#StringBuilder_Create>) | Creates a StringBuilder. Use it if you need to create a string by repeatedly appending substrings. A StringBuilder optimizes memory management when dealing with highly dynamic strings. | Yes
[StringBuilder_ToString](<libraries/text.md#StringBuilder_ToString>) | Returns the content of the StringBuilder's buffer. | Yes

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
[DecodeURL](<libraries/url.md#DecodeURL>) | Converts a string that has been encoded for transmission in a URL into a decoded text value. | Yes
[GetRelativeURL](<libraries/url.md#GetRelativeURL>) | Returns the relative URL from the base URL. | Yes
[GetURLProtocol](<libraries/url.md#GetURLProtocol>) | Returns the protocol of the given URL. | Yes
[GetURLHost](<libraries/url.md#GetURLHost>) | Returns the host of the given URL. | Yes
[IsURLRelative](<libraries/url.md#IsURLRelative>) | Returns true if the given URL is a relative URL. | Yes

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

|Name|Description|
|--- |--- |
|[BooleanToInteger](built-in-functions/data-conversion.md#booleantointeger)|Converts Boolean 'b' to an Integer value, either 1 if 'b' is True or 0 if 'b' is False.|
|[BooleanToText](built-in-functions/data-conversion.md#booleantotext)|Converts Boolean 'b' to a Text value, either "True" or "False".|
|[DateTimeToDate](built-in-functions/data-conversion.md#datetimetodate)|Converts Date Time 'dt' to a Date value dropping the Time component.|
|[DateTimeToText](built-in-functions/data-conversion.md#datetimetotext)|Converts Date Time 'dt' to a Text value in the format specified in the environment configuration (by default, "yyyy-MM-dd HH:mm:ss").|
|[DateTimeToTime](built-in-functions/data-conversion.md#datetimetotime)|Converts Date Time 'dt' to a Time value dropping the Date component.|
|[DateToDateTime](built-in-functions/data-conversion.md#datetodatetime)|Converts Date 'd' to a Date Time value, adding the Time component (built-in-functions/data-conversion.md#00:00:00#).|
|[DateToText](built-in-functions/data-conversion.md#datetotext)|Converts Date 'd' to a Text value in the format specified in the environment configuration (by default, "yyyy-MM-dd").|
|[DecimalToBoolean](built-in-functions/data-conversion.md#decimaltoboolean)|Converts Decimal 'd' to a Boolean value. Decimal value of 0.0 is False. Any other value is True.|
|[DecimalToInteger](built-in-functions/data-conversion.md#decimaltointeger)|Converts Decimal 'd' to an Integer value. In client-side and server-side logic, the function rounds the input using the round half to even method. In Aggregate expressions the function truncates to the integer part of the input.To check if the conversion is possible you can use the DecimalToIntegerValidate function.|
|[DecimalToIntegerValidate](built-in-functions/data-conversion.md#decimaltointegervalidate)|Returns true if Decimal 'd' can be converted to an Integer value.|
|[DecimalToLongInteger](built-in-functions/data-conversion.md#decimaltolonginteger)|Converts Decimal 'd' to a Long Integer value.In client-side and server-side logic, the function rounds the input using the round half to even method. In Aggregate expressions the function truncates to the integer part of the input.To check if the conversion is possible you can use the DecimalToLongIntegerValidate function.|
|[DecimalToLongIntegerValidate](built-in-functions/data-conversion.md#decimaltolongintegervalidate)|Returns true if Decimal 'd' can be converted to a Long Integer value.|
|[DecimalToText](built-in-functions/data-conversion.md#decimaltotext)|Converts Decimal 'd' to a Text value.|
|[LongIntegerToInteger](built-in-functions/data-conversion.md#longintegertointeger)|Converts Long Integer 'l' to an Integer value. If 'l' is outside the boundaries of the Integer values, the function will return the Integer default value. To check if the conversion is possible you can use the LongIntegerToIntegerValidate function.|
|[LongIntegerToIntegerValidate](built-in-functions/data-conversion.md#longintegertointegervalidate)|Returns true if Long Integer 'l' can be converted to an Integer value.|
|[LongIntegerToIdentifier](built-in-functions/data-conversion.md#longintegertoidentifier)|Converts Long Integer 'l' to a Long Integer Identifier.|
|[LongIntegerToText](built-in-functions/data-conversion.md#longintegertotext)|Converts Long Integer 'l' to a Text value.|
|[IdentifierToInteger](built-in-functions/data-conversion.md#identifiertointeger)|Converts Identifier 'Id' to an Integer value.|
|[IdentifierToLongInteger](built-in-functions/data-conversion.md#identifiertolonginteger)|Converts Identifier 'Id' to a Long Integer value.|
|[IdentifierToText](built-in-functions/data-conversion.md#identifiertotext)|Converts Identifier 'Id' to a Text value.|
|[IntegerToBoolean](built-in-functions/data-conversion.md#integertoboolean)|Converts Integer 'i' to a Boolean value. Boolean value of 0 is False. Any other value is True.|
|[IntegerToDecimal](built-in-functions/data-conversion.md#integertodecimal)|Converts Integer 'i' to a Decimal value.|
|[IntegerToIdentifier](built-in-functions/data-conversion.md#integertoidentifier)|Converts Integer 'i' to an Integer Identifier.|
|[IntegerToText](built-in-functions/data-conversion.md#integertotext)|Converts Integer 'i' to a Text value.|
|[NullDate](built-in-functions/data-conversion.md#nulldate)|Returns a null Date value.|
|[NullIdentifier](built-in-functions/data-conversion.md#nullidentifier)|Returns a null Identifier valid for Integer and Long Integer Identifiers.|
|[NullObject](built-in-functions/data-conversion.md#nullobject)|Returns a null Object value.|
|[NullBinary](built-in-functions/data-conversion.md#nullbinary)|Returns a null Binary Data value.|
|[NullTextIdentifier](built-in-functions/data-conversion.md#nulltextidentifier)|Returns a null Text Identifier.|
|[TextToDate](built-in-functions/data-conversion.md#texttodate)|Converts Text 't' to a Date value.If 't' can't be converted to a valid Date value, the function will return the Date default value. To check if the conversion is possible you can use the TextToDateValidate function.You should check the limits of the Date data type. You should also ensure that the date you type in the argument complies with the default date format (yyyy-mm-dd, yyyy/mm/dd, and yyyy.mm.dd) or the server's environment configuration. Note that, when using the date format defined in the environment configuration, the function will only accept the separator character defined in that date format. For example, if the environment date format is set to 'DD-MM-YYYY', you cannot use '/' or '.' as separators in 't'.|
|[TextToDateTime](built-in-functions/data-conversion.md#texttodatetime)|Converts Text 't' to a Date Time value.If 't' can't be converted to a valid Date Time value, the function will return a Date Time default value. To check if the conversion is possible you can use the TextToDateTimeValidate function.You should check the limits of the Date Time data type. You should also ensure that the Date Time you type in the argument complies with the default Date Time format (yyyy-mm-dd hh:mm:ss, yyyy/mm/dd hh:mm:ss, and yyyy.mm.dd hh:mm:ss) or the server's environment configuration. Note that, when using the date format defined in the environment configuration, the function will only accept the separator character defined in that date format. For example, if the environment date format is set to 'DD-MM-YYYY', you cannot use '/' or '.' as separators in 't'.|
|[TextToDateTimeValidate](built-in-functions/data-conversion.md#texttodatetimevalidate)|Returns true if Text 't' can be converted to a Date Time value.|
|[TextToDateValidate](built-in-functions/data-conversion.md#texttodatevalidate)|Returns true if Text 't' can be converted to a Date value.|
|[TextToDecimal](built-in-functions/data-conversion.md#texttodecimal)|Converts Text 't' to a Decimal value. The only allowed decimal separator is "." (period).If 't' is outside the boundaries of Decimal values, the function returns the Decimal default value. However, if you use TextToDecimal in an Aggregate and 't' is outside the boundaries of Decimal values, the function throws an exception. To check if the conversion is possible, use the TextToDecimalValidate function.|
|[TextToDecimalValidate](built-in-functions/data-conversion.md#texttodecimalvalidate)|Returns true if Text 't' can be converted to a Decimal value.|
|[TextToIdentifier](built-in-functions/data-conversion.md#texttoidentifier)|Converts Text 't' to a Text Identifier.|
|[TextToInteger](built-in-functions/data-conversion.md#texttointeger)|Converts Text 't' to an Integer value.If 't' is outside the boundaries of Integer values, the function returns the Integer default value. However, if you use TextToInteger in an Aggregate and 't' is outside the boundaries of Integer values, the function throws an exception. To check if the conversion is possible, use the TextToIntegerValidate function.|
|[TextToLongInteger](built-in-functions/data-conversion.md#texttolonginteger)|Converts Text 't' to a Long Integer value.If 't' is outside the boundaries of Long Integer values, the function returns the Long Integer default value. However, if you use TextToLongInteger in an Aggregate and 't' is outside the boundaries of Long Integer values, the function throws an exception. To check if the conversion is possible, use the TextToLongIntegerValidate function.|
|[TextToIntegerValidate](built-in-functions/data-conversion.md#texttointegervalidate)|Returns true if Text 't' can be converted to an Integer value.|
|[TextToLongIntegerValidate](built-in-functions/data-conversion.md#texttolongintegervalidate)|Returns true if Text 't' can be converted to a Long Integer value.|
|[TextToTime](built-in-functions/data-conversion.md#texttotime)|Converts Text 't' to a Time value.If 't' can't be converted to a valid Time value, the function will return the Time default value. To check if the conversion is possible you can use the TextToTimeValidate function.You should check the limits of the Time data type. You should also ensure that the Time you type in the argument complies with the Time format (hh:mm:ss).|
|[TextToTimeValidate](built-in-functions/data-conversion.md#texttotimevalidate)|Returns true if Text 't' can be converted to a Time value.|
|[TimeToText](built-in-functions/data-conversion.md#timetotext)|Converts Time 't' to a Text value in the format "HH:mm:ss".|
|[ToObject](built-in-functions/data-conversion.md#toobject)|Converts expression 'exp' to an Object value.|

### Date and Time

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="built-in-functions/dateandtime.html#AddDays">AddDays</a></td>
<td>Adds 'n' days to 'dt' and returns a valid Date Time.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#AddHours">AddHours</a></td>
<td>Adds 'n' hours to 'dt' and returns a valid Date Time.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#AddMinutes">AddMinutes</a></td>
<td>Adds 'n' minutes to 'dt' and returns a valid Date Time.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#AddMonths">AddMonths</a></td>
<td>Adds 'n' months to 'dt' and returns a valid Date Time.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#AddSeconds">AddSeconds</a></td>
<td>Adds 'n' seconds to 'dt' and returns a valid Date Time.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#AddYears">AddYears</a></td>
<td>Adds 'n' years to 'dt' and returns a valid Date Time.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#BuildDateTime">BuildDateTime</a></td>
<td>Returns a Date Time made up of the Date 'd' and Time 't'.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#CurrDate">CurrDate</a></td>
<td>- Client-side calls return the device date and time.<br/>- Server-side calls return the current date in UTC.<br/>- SQL query calls return the current date and time in UTC.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#CurrDateTime">CurrDateTime</a></td>
<td>- Client-side calls return the device date and time.<br/>- Server-side calls return the current date in UTC.<br/>- SQL query calls return the current date and time in UTC.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#CurrTime">CurrTime</a></td>
<td>- Client-side calls return the device date and time.<br/>- Server-side calls return the current date in UTC.<br/>- SQL query calls return the current date and time in UTC.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#Day">Day</a></td>
<td>Returns the day of 'dt'.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#DayOfWeek">DayOfWeek</a></td>
<td>Returns the week day of 'dt', ranging from 0 (Sunday) to 6 (Saturday).</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#DiffDays">DiffDays</a></td>
<td>Returns the difference in days between 'dt1' and 'dt2'; i.e. how many days have passed between these two dates:<br/><br/>- Returns a positive number if 'dt1' is smaller than 'dt2';<br/>- Returns a negative number if 'dt1' is bigger than 'dt2';<br/>- Returns 0 if the two dates are equal.<br/><br/>The Time component you provide in the parameters is ignored. The DiffDays function receives two Date Time parameters, and then replaces the Time component with 00:00:00. It calculates the elapsed time in milliseconds from the first date at 00:00:00 to the second date at 00:00:00, and then converts the difference in milliseconds into days.<br/><br/>Daylight Saving Time (DST) is ignored. The time zone considered for evaluating this function is always the time zone of the Platform Server, regardless of the regional settings of the end user.<br/><br/>The maximum supported value is (2^31)-1 days. This corresponds to approximately 5879489.8 years. If DiffDays(dt1, dt2) is bigger than (2^31)-1, you will get an unexpected value.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#DiffHours">DiffHours</a></td>
<td>Returns the difference in hours between 'dt1' and 'dt2'; i.e. how many hours have passed between these two dates:<br/><br/>- Returns a positive number if 'dt1' is smaller than 'dt2';<br/>- Returns a negative number if 'dt1' is bigger than 'dt2'.<br/>- Returns 0 if the two dates are equal.<br/><br/>Daylight Saving Time (DST) is ignored. The time zone considered for evaluating this function is always the time zone of the Platform Server, regardless of the regional settings of the end user.<br/><br/>The maximum supported value is (2^31)-1 hours. This corresponds to approximately 244978.74 years. If DiffHours(dt1, dt2) is bigger than (2^31)-1, you will get an unexpected value.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#DiffMinutes">DiffMinutes</a></td>
<td>Returns the difference in minutes between 'dt1' and 'dt2'; i.e. how many minutes have passed between these two dates:<br/><br/>- Returns a positive number if 'dt1' is smaller than 'dt2';<br/>- Returns a negative number if 'dt1' is bigger than 'dt2'.<br/>- Returns 0 if the two dates are equal.<br/><br/>Daylight Saving Time (DST) is ignored. The time zone considered for evaluating this function is always the time zone of the Platform Server, regardless of the regional settings of the end user.<br/><br/>The maximum supported value is (2^31)-1 minutes. This corresponds to approximately 4085.78 years. If DiffMinutes(dt1, dt2) is bigger than (2^31)-1, you will get an unexpected value.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#DiffSeconds">DiffSeconds</a></td>
<td>Returns the difference in seconds between 'dt1' and 'dt2'; i.e. how many seconds have passed between these two dates:<br/><br/>- Returns a positive number if 'dt1' is smaller than 'dt2';<br/>- Returns a negative number if 'dt1' is bigger than 'dt2'.<br/>- Returns 0 if the two dates are equal.<br/><br/>Daylight Saving Time (DST) is ignored. The time zone considered for evaluating this function is always the time zone of the Platform Server, regardless of the regional settings of the end user.<br/><br/>The maximum supported value is (2^31)-1 seconds. This corresponds to approximately 68.10 years. If DiffSeconds(dt1, dt2) is bigger than (2^31)-1, you will get an unexpected value.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#Hour">Hour</a></td>
<td>Returns the hour of 'dt'.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#Minute">Minute</a></td>
<td>Returns the minute of 'dt'.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#Month">Month</a></td>
<td>Returns the month of 'dt'.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#NewDate">NewDate</a></td>
<td>Returns a Date made up of year 'y', month 'm' and day 'd'.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#NewDateTime">NewDateTime</a></td>
<td>Returns a Date Time made up of year 'y', month 'mo', day 'd', hour 'h', minute 'mi' and second 's'.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#NewTime">NewTime</a></td>
<td>Returns a Time made up of hour 'h', minute 'm' and second 's'.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#Second">Second</a></td>
<td>Returns the seconds of 'dt'.</td>
</tr>
<tr>
<td><a href="built-in-functions/dateandtime.html#Year">Year</a></td>
<td>Returns the year of 'dt'.</td>
</tr>
</tbody>
</table>

### Email

|Name|Description|
|--- |--- |
|[EmailAddressCreate](built-in-functions/email.md#emailaddresscreate)|Returns a full email address string containing the display name (usually it's the name of the email address owner) and the email address itself. The resulting full email address may then be used in the Send Email element (action flows) or in the Send Email activity (process flows).|
|[EmailAddressValidate](built-in-functions/email.md#emailaddressvalidate)|Returns true if Text 'address' is a valid email address. Note that EmailAddressValidate("") returns True.This built-in function implements the validation specified by HTML5 (https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address) which has a practical approach to RFC 5322.|

### Format

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="built-in-functions/format.html#FormatCurrency">FormatCurrency</a></td>
<td>Builds a Text output of the specified Currency 'value', preceded by the currency 'symbol', using 'decimal_digits' after the decimal point. The decimal point is specified using 'decimal_separator', while the thousands can be separated with the 'group_separator'.<br/><br/>When rounding, the function behaves differently depending on where you use it:<br/><br/>- In <b>server-side logic</b>, it applies the method round half up (rounds to the nearest integer, 0.5 rounds up).<br/>- In <b>client-side logic</b>, it applies the method round half to even (rounds to the nearest integer, 0.5 rounds to the nearest even integer).</td>
</tr>
<tr>
<td><a href="built-in-functions/format.html#FormatDecimal">FormatDecimal</a></td>
<td>Builds a Text output of the specified Decimal 'value', using 'decimal_digits' after the decimal point. The decimal point is specified using 'decimal_separator', while the thousands can be separated with the 'group_separator'.<br/><br/>When rounding, the function behaves differently depending on where you use it:<br/><br/>- In <b>server-side logic</b>, it applies the method round half up (rounds to the nearest integer, 0.5 rounds up).<br/>- In <b>client-side logic</b>, it applies the method round half to even (rounds to the nearest integer, 0.5 rounds to the nearest even integer).</td>
</tr>
<tr>
<td><a href="built-in-functions/format.html#FormatPercent">FormatPercent</a></td>
<td>Builds a Text output of the specified Decimal 'value', followed by '%' using 'decimal_digits' after the decimal point. The decimal point is specified using 'decimal_separator'.<br/><br/>When rounding, the function behaves differently depending on where you use it:<br/><br/>- In <b>server-side logic</b>, it applies the method round half up (rounds to the nearest integer, 0.5 rounds up).<br/>- In <b>client-side logic</b>, it applies the method round half to even (rounds to the nearest integer, 0.5 rounds to the nearest even integer).</td>
</tr>
<tr>
<td><a href="built-in-functions/format.html#FormatPhoneNumber">FormatPhoneNumber</a></td>
<td>Builds a Text output of the specified phone number Text 'value', starting with the international separator 'int_separator', followed by the first 'int_code_digits' of 'value', then the 'area_separator', then the following 'area_code_digits' of 'value', then the 'phone_separator' and finally the following 'phone_digits' of 'value'.</td>
</tr>
<tr>
<td><a href="built-in-functions/format.html#FormatText">FormatText</a></td>
<td>Builds a Text output of the specified Text 'value', by limiting it to the specified 'max_chars' count. If 'value' has less than the 'min_chars' characters limit, enough 'padding_char' characters are added to expand the length to that limit. In this case, 'left_padding' determines where the padding should be added.</td>
</tr>
<tr>
<td><a href="built-in-functions/format.html#FormatDateTime">FormatDateTime</a></td>
<td>Builds a Text output of the specified Date Time 'value' using the specified 'format'. Formatting pattern can be any combination of the following:<br/>Day:<br/>- d: day without leading zero;<br/>- dd: day WITH leading zero;<br/>- ddd: abbreviated day name;<br/>- dddd: full day name;<br/>Month:<br/>- M: month without leading zero;<br/>- MM: month WITH leading zero;<br/>- MMM: abbreviated month name;<br/>- MMMM: full month name;<br/>Year:<br/>- y: last one or two digits of the year;<br/>- yy: last two digits of the year;<br/>- yyyy: year;<br/>Hour:<br/>- h: hour from 0 to 12 without leading zero;<br/>- hh: hour from 0 to 12 WITH leading zero;<br/>- H: hour from 0 to 24 without leading zero;<br/>- HH: hour from 0 to 24 WITH leading zero;<br/>Minute:<br/>- m: minutes without leading zero;<br/>- mm: minutes WITH leading zero;<br/>Second:<br/>- s: seconds without leading zero;<br/>- ss: seconds WITH leading zero;<br/>AM Designator:<br/>- t: first letter of AM or PM;<br/>- tt: AM or PM.<br/><br/>If you want to output any of these characters then precede it with '\'.<br/>Changing the environment date format does not change the way the FormatDateTime function formats the dates.</td>
</tr>
</tbody>
</table>

### Math

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="built-in-functions/math.html#Abs">Abs</a></td>
<td>Returns the absolute value (unsigned magnitude) of the decimal number 'n'.</td>
</tr>
<tr>
<td><a href="built-in-functions/math.html#Mod">Mod</a></td>
<td>Returns the remainder of decimal division of 'n' by 'm'.</td>
</tr>
<tr>
<td><a href="built-in-functions/math.html#Power">Power</a></td>
<td>Returns 'n' raised to the power of 'm'.</td>
</tr>
<tr>
<td><a href="built-in-functions/math.html#Round">Round</a></td>
<td>Returns the Decimal number 'n' rounded to a specific number of 'fractional digits'.</td>
</tr>
<tr>
<td><a href="built-in-functions/math.html#Sqrt">Sqrt</a></td>
<td>Returns the square root of the Decimal number 'n'.</td>
</tr>
<tr>
<td><a href="built-in-functions/math.html#Trunc">Trunc</a></td>
<td>Returns the Decimal number 'n' truncated to integer removing the decimal part of 'n'.</td>
</tr>
</tbody>
</table>

### Numeric

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="built-in-functions/numeric.html#Max">Max</a></td>
<td>Returns the largest number of 'n' and 'm'.</td>
</tr>
<tr>
<td><a href="built-in-functions/numeric.html#Min">Min</a></td>
<td>Returns the smallest number of 'n' and 'm'.</td>
</tr>
<tr>
<td><a href="built-in-functions/numeric.html#Sign">Sign</a></td>
<td>Returns -1 if 'n' is negative; 1 if 'n' is positive; 0 if 'n' is 0.</td>
</tr>
</tbody>
</table>

### Organization

|Name|Description|
|--- |--- |
|[GetCurrentLocale](built-in-functions/organization.md#GetCurrentLocale)|Returns the name of the current language locale of the user session. The name of the language locale is used for presentation purposes and follows the RFC 1766 standard format.|
|[GetUserAgent](built-in-functions/organization.md#GetUserAgent)|Returns the user agent, as indicated by the header of the HTTP message.|
|[GetAppName](built-in-functions/organization.md#GetAppName)|Returns the name of the app that is processing the request.|

### Text

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="built-in-functions/text.html#Chr">Chr</a></td>
<td>Returns a single-character string corresponding to the 'c' character code.</td>
</tr>
<tr>
<td><a href="built-in-functions/text.html#EncodeHtml">EncodeHtml</a></td>
<td>Replaces special characters in a string so that you can use it in HTML literals. Use this function when using un-escaped expressions that contain content provided by end users.<br/><br/>Warning: Since this function only encodes strings that will be used in HTML literals, it does not protect you from cross-site scripting (XSS) or JavaScript injection vulnerabilities on its own. <b>Do not</b> use this function to encode text that might get executed as JavaScript code, only to encode HTML literals.</td>
</tr>
<tr>
<td><a href="built-in-functions/text.html#EncodeJavaScript">EncodeJavaScript</a></td>
<td>Replaces special characters in a string so that you can use it in JavaScript literals. Use this function when using un-escaped expressions that contain content provided by end users.<br/><br/>Warning: Since this function only encodes strings that will be used in JavaScript literals, it does not protect you from cross-site scripting (XSS) or JavaScript injection vulnerabilities on its own. <b>Do not</b> use this function to encode text that might get executed as JavaScript code, only to encode JavaScript literals.</td>
</tr>
<tr>
<td><a href="built-in-functions/text.html#EncodeSql">EncodeSql</a></td>
<td>Replaces special characters in a string literal so that you can use it in a SQL statement. Use this function when the Expand Inline property of a Query Parameter is enabled to escape content provided by end users.<br/><br/>Warning: Since this function only encodes string literals, it does not protect you from SQL injection vulnerabilities on its own. <b>Do not</b> use this function to encode text that might get executed as part of the SQL statement. Check the OutSystems Best Practices documentation for more information on building dynamic SQL statements the right way.</td>
</tr>
<tr>
<td><a href="built-in-functions/text.html#EncodeUrl">EncodeUrl</a></td>
<td>Replaces all non-alphanumeric characters in a string, i.e. characters outside of the [0-9a-zA-Z] range, so that you can safely use it in URL parameter values. Use this function to build URLs in your app that may contain content provided by end users, e.g. when dynamically building URLs to an external site.</td>
</tr>
<tr>
<td><a href="built-in-functions/text.html#Index">Index</a></td>
<td>Returns the zero-based position in Text 't' where 'search' Text can be found. Returns -1 if 'search' is not found or if 'search' is empty.</td>
</tr>
<tr>
<td><a href="built-in-functions/text.html#Length">Length</a></td>
<td>Returns the number of characters in Text 't'.</td>
</tr>
<tr>
<td><a href="built-in-functions/text.html#NewLine">NewLine</a></td>
<td>Returns a string containing the New Line (Return) character.</td>
</tr>
<tr>
<td><a href="built-in-functions/text.html#Replace">Replace</a></td>
<td>Returns Text 't' after replacing all Text occurrences of 'search' with 'replace'.</td>
</tr>
<tr>
<td><a href="built-in-functions/text.html#Substr">Substr</a></td>
<td>Returns a sub-string of 't' beginning at 'start' zero-based position and with 'length' characters.</td>
</tr>
<tr>
<td><a href="built-in-functions/text.html#ToLower">ToLower</a></td>
<td>Converts Text 't' to the equivalent lowercase text.</td>
</tr>
<tr>
<td><a href="built-in-functions/text.html#ToUpper">ToUpper</a></td>
<td>Converts Text 't' to the equivalent uppercase text.</td>
</tr>
<tr>
<td><a href="built-in-functions/text.html#Trim">Trim</a></td>
<td>Removes all leading and trailing space characters (' ') from Text 't'.</td>
</tr>
<tr>
<td><a href="built-in-functions/text.html#TrimEnd">TrimEnd</a></td>
<td>Removes all trailing space characters (' ') from Text 't'.</td>
</tr>
<tr>
<td><a href="built-in-functions/text.html#TrimStart">TrimStart</a></td>
<td>Removes all leading space characters (' ') from Text 't'.</td>
</tr>
</tbody>
</table>

### URL

<table markdown="built-in-functions/url.html1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="built-in-functions/url.html#GetBookmarkableURL">GetBookmarkableURL</a></td>
<td>Returns the URL of the screen that is currently being processed.<br/>The URL returned by this function is a complete URL with the format http://server/module/personal_area/screen?param1=value&amp;param2=value... <br/>Parameters and their values aren't included when parameters are optional and their values aren't set.</td>
</tr>
<tr>
<td><a href="built-in-functions/url.html#GetOwnerURLPath">GetOwnerURLPath</a></td>
<td>Returns the URL path of the module that owns the element that is being processed. Note that this function does not return the complete URL but only the component containing the location of the resource within the domain and, if applicable, the personal area.</td>
</tr>
</tbody>
</table>
