---
summary: OutSystems Developer Cloud (ODC) supports BPMN practitioners with a comprehensive guide to process modeling notation and execution.
tags: bpmn, business process modeling, process notation, workflows, odc
guid: 7a860538-98c2-4264-b7fd-9d6aef199a8e
locale: en-us
app_type: mobile apps, reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?m=auto&node-id=7661-248&t=j6TLVC2hYtnw4FQo-1
api-render: false
outsystems-tools:
  - none
coverage-type:
content-type:
audience:
  - none
topic:
---
# Notation Reference for BPMN Practitioners

OutSystems allows designing and executing business processes through [workflows](workflows-in-odc.md). This technical note describes the notation used for Process Modeling targeted at practitioners currently modeling processes using BPMN.

| **BPMN 1.2** |**Description**|**OutSystems Business Process Technology**|**Description**|
|-------------|-----------|-------------|---------------|
|![BPMN icon representing a plain start event.](images/notation-reference-for-bpmn-practitioners-0.png "BPMN Plain Start Event")| Plain Start Event|![OutSystems icon representing a start event with a green play button.](images/start-pl.png "OutSystems Start Event") |**Start**, initiates the process.|
|![BPMN icon representing a plain end event.](images/notation-reference-for-bpmn-practitioners-2.png "BPMN Plain End Event")| Plain End Event|![OutSystems icon representing an end event with a green square.](images/end-pl.png "OutSystems End Event")|  **End**, finishes a process flow. Theprocess may continue in parallelflows.|
|![BPMN icon representing a terminate event.](images/notation-reference-for-bpmn-practitioners-4.png "BPMN Terminate Event")| Terminate Event|![OutSystems icon representing a terminate event with a green terminate label.](images/terminate-pl.png "OutSystems Terminate Event")|  **End with Terminate property set to Yes**, ends all flows of the process.|
|![BPMN icon representing a start event with various catching triggers.](images/notation-reference-for-bpmn-practitioners-6.png "BPMN Start Event with Catching Trigger")| Start Event with a catching trigger: Message; Timer; Conditional; Signal or Multiple|![OutSystems icon representing a conditional start event with a lightning bolt symbol.](images/conditional-start-pl.png "OutSystems Conditional Start")| **Conditional Start**, initiates an alternative flow and may be triggered by a DB event or an explicit API call.|
|![BPMN icon representing an intermediate event with various catching triggers.](images/notation-reference-for-bpmn-practitioners-8.png "BPMN Intermediate Event with Catching Trigger")|  Intermediate Event with a catching trigger: Message; Timer; Conditional; Signal or Multiple | ![OutSystems icon representing a wait event with an hourglass symbol.](images/wait-pl.png "OutSystems Wait Event")| **Wait**, pauses the flow waiting for a timeout, a DB event, an API call or for a custom business logic returning true.|
|![BPMN icon representing an intermediate event with various throwing triggers.](images/notation-reference-for-bpmn-practitioners-10.png "BPMN Intermediate Event with Throwing Trigger")| Intermediate Event with a throwing trigger: Message; Signal or Multiple|![OutSystems icon representing an automatic activity with a broadcast symbol.](images/automatic-activity-pl.png "OutSystems Automatic Activity")| **Automatic Activity**, can be used to broadcast an event (via DB) or call an API to deliver an event to a specific activity or process.|
|![BPMN icon representing a task of type service, script, or send.](images/notation-reference-for-bpmn-practitioners-12.png "BPMN Task of Type Service, Script, or Send")| Task of type: Service, Script or Send (if not email)|![OutSystems icon representing an automatic activity with a gear symbol.](images/automatic-activity-pl.png "OutSystems Automatic Activity")| **Automatic Activity**, performs custom business logic in the application or in external systems.|
|![BPMN icon representing a task of type user or manual.](images/notation-reference-for-bpmn-practitioners-14.png "BPMN Task of Type User or Manual")| Task of type: User or Manual|![OutSystems icon representing a human activity with a user silhouette.](images/human-activity-pl.png "OutSystems Human Activity")|  **Human Activity**, waits for a user or group to complete the given task.This activity shows up in the taskbox of one or more users.|
|![BPMN icon representing a task of type receive.](images/notation-reference-for-bpmn-practitioners-16.png "BPMN Task of Type Receive")| Task of type: Receive|![OutSystems icon representing a wait for receive event with an envelope symbol.](images/wait-pl.png "OutSystems Wait for Receive")| **Wait**, for the Receive semantics the application should call the Close Wait API when a message is received.|
|![BPMN icon representing an exclusive data-based decision gateway.](images/notation-reference-for-bpmn-practitioners-22.png "BPMN Exclusive Data-Based Decision Gateway")| Exclusive Data-Based Decision (Gateway)|![OutSystems icon representing a decision activity with a diamond symbol.](images/decision-pl.png "OutSystems Decision Activity")| **Decision**, directs to one outgoing gates based on custom business logic.|
|![BPMN icon representing a parallel split fork.](images/notation-reference-for-bpmn-practitioners-26.png "BPMN Parallel Split Fork")|Parallel Split (Fork)|![OutSystems icon representing a parallel activity with multiple arrows.](images/parallel-pl.png "OutSystems Fork Activity")| **Parallel**, two or more outgoing connectors (except when starting from a Decision) divide the flow into parallel paths.|
|![BPMN icon representing a fork and join using a parallel gateway.](images/notation-reference-for-bpmn-practitioners-28.png "BPMN Fork and Join using Parallel Gateway")| Fork and Join using a Parallel Gateway|![OutSystems icon representing a parallel activity with multiple arrows converging.](images/parallel-pl.png "OutSystems Fork and Join Activity")| **Parallel**, is implemented by calling a sub-process with the two or more parallel paths that must be joined. The parent process only proceeds after all flows of the subprocess have ended.|
|![BPMN icon representing a text annotation.](images/notation-reference-for-bpmn-practitioners-30.png "BPMN Text Annotation")| Text Annotation|![OutSystems icon representing a comment annotation with a yellow note symbol.](images/comment-pl.png "OutSystems Comment Annotation")| **Comment**, can be used to annotate any element or area of the process model.|
