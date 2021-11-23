---
summary: Reuse elements to share across apps.  
tags: outsystems 11; resuse; app depenencies; public elements 
---

# Reuse elements across apps

You can share public elements across your applications to accelerate development and enable consistency across apps. Sharing elements creates dependencies between producer and consumer apps. In Project Neo, strong dependencies (for example, those in which a consumer executes logic from a producer) can only exist between the following app types: 

* Library (producer) and a Web or Mobile App (consumer) -- You can share Client Actions and Server Actions in libraries (producer), and use them in apps (consumer). Apps can’t be a producer when sharing Client and Server Actions. 
* Two libraries -- Libraries can be producers or consumers.

Weak dependencies (for example, reusing a static entity) can exist between the following app types: 

* Two apps (Web Apps or Mobile Apps) -- Web and Mobile Apps can share Service Actions, entities, status entities, and screens.

## Public elements

To expose and share a public element for reuse, you set the element’s Public property to Yes. Some elements can’t be shared, and in such cases, the element’s Public property is set to No and can’t be changed. For example, a Server Action within an app can’t be set to Public. 
The following table lists elements and their possible Public property values.

| Element type | Can element be public in apps?  | Can element be public in libraries? | 
| ----------- | ----------- | ----------- |
| Blocks | No | Yes | 
| Client Actions| No | Yes | 
| Images | No | No | 
| Local entities | No | Not applicable | 
| Processes | No | Not applicable | 
| Resources | No | No | 
| Roles | No | Not applicable | 
| Screens | Yes | No | 
| Scripts | No | No | 
| Server Actions | No | Yes | 
| Service Actions | Yes | Not applicable | 
| Static Entities | Yes | Yes | 
| Structures | No | No | 
| Themes | No | Yes | 

## Libraries

Project Neo elevates Libraries to a top-level concept. Libraries exist at the same level as Web Apps and Mobile Apps, and they have their own lifecycle. Apps can consume different versions of a Library, and you can choose which version an app uses. For example, you can make a branding change by updating the style guide in a Library. Then, you can roll out that change one app at a time, rather than updating all apps at once. Deployed apps can coexist with old and new branding, based on the Library version each app consumes. 

When a Library is updated in Dev, updates to consumer apps occur based on the type of change and the type of dependency. When “breaking” changes (changes that break a consumer app) occur, the newest library version gets applied automatically to consumer apps in the Dev stage. Apps in other stages (QA or Prod) aren't updated automatically, nor are they impacted by changes made to the version in Dev.

## Expose a Server Action in an app

You can’t share (that is, expose as Public) a Server Action from within an app. However, to achieve the same outcome:

1. Right-click the Server Action.
2. Select Expose as Service Action. This creates a Service Action that invokes the Server Action and its properties.  

Alternatively, you can create the Server Action in a Library, and have your app consume it.
