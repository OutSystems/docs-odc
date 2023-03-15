---
summary:
tags:
locale: en-us
guid: 2c67f5b6-b8b4-46ea-9217-493cffb20456
app_type: mobile apps, reactive web apps
platform-version: odc
---
# XML

## Actions

Action | Description
---|---
Serialization_RecordListToXml | Serializes RecordList into XML data. Only records with single entities/structures are supported.
Serialization_ObjectToXml | Serializes a Record or a RecordList into XML data. Only records with single entities/structures are supported.
Serialization_RecordToXml | Serializes a Record into XML data. Only records with single entities/structures are supported.
Serialization_XmlToRecordList | Deserializes a set of Entities definition from an XML data description.
XmlAttribute_GetValue | Returns the value of a Xml Attribute. 
XmlAttribute_SetValue | Sets the value of a Xml Attribute.
XmlDocument_CreateRootElement | Creates a root Xml Element in a Xml Document.
XmlDocument_GetRootElement | Returns the root element of a Xml Document.
XmlDocument_New | Creates an empty Xml DOM.
XmlDocument_Save | Saves the XML document to a string, using UTF-8 encoding.
XmlDocument_SelectNodes | Returns a list of Xml Elements or Xml Attributes as described by the XPath string. 
XmlDocument_SelectSingleNode | Returns a Xml Element or a Xml Attribute as described by the XPath string.
XmlElement_AppendAttribute | Appends a new Xml Attribute to the Element XmlElement.
XmlElement_AppendChildElement | Appends a new child Element to XmlElement.
XmlElement_GetAttribute | Returns a Xml Attribute with a given name. 
XmlElement_GetAttributeValue | Returns the value of a Xml Attribute with a give name. 
XmlElement_GetChildByIndex | Returns a child node by index. The index is 0-based.
XmlElement_GetChildCount | Returns the number of child nodes in a Xml Element.
XmlElement_GetInnerText | Returns the inner text of a Xml Element.
XmlElement_GetName | Returns the name of a Xml Element.
XmlElement_Remove | Removes a Xml Element.
XmlElement_RemoveAttribute | Removes a Xml Attribute. 
XmlElement_SelectNodes | Returns a list of Xml Elements or Xml Attributes as described by the XPath string.
XmlElement_SelectSingleNode | Returns a Xml Element or a Xml Attribute as described by the XPath string.
XmlElement_SetInnerText | Sets the inner text of a Xml Element.
XmlNode_GetParentNode | Gets the parent Xml Node of a Xml Node. 
XmlNode_GetXmlDocument | Gets the Xml Document to which a specific Xml Node belongs.
XmlNodeList_Count | Gets the number of nodes in the Xml Node List.
XmlNodeList_Item | Retrieves a node at the given index. 
Xsl_Transform | Transforms a Xml content using XLST.
