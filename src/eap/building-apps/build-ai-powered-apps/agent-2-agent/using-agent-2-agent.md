---
summary: Configure A2A connections to external agents in OutSystems Developer Cloud (ODC), setting URLs, reviewing skills, and choosing OAuth, bearer, or API key auth.
tags:
  - AI
  - Agentic
  - Authentication
  - OAuth
guid: 8764e4f7-25f3-4a21-b6a9-000c59f4a93a
locale: en-us
app_type: reactive web apps
platform-version: odc
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=9637-33
outsystems-tools:
  - odc portal
coverage-type:
  - apply
content-type:
audience:
  - Developer
  - Platform administrator
topic:
isautopublish: true
---
# Adding external agents in the ODC portal using A2A

This article provides a step-by-step guide on how to add connections to external agents in the ODC portal using the Agent-to-Agent (A2A) communication protocol. **Please note that ODC A2A connector supports only A2A 0.3.0 protocol version.**

To add connections to external agents in the ODC portal using A2A:

1. Go to the ODC portal and navigate to the **Integrate** section and select **Connections**.

    ![ODC portal Connections page showing an empty list of connections and the Create connection button highlighted in the top-right corner.](images/creating-connection-pl.png "Connections page with Create connection button in ODC portal")

1. Click on **Create connection** and select **A2A**.

    ![Connections dialog in the ODC portal with the A2A provider tile highlighted among the available connection providers.](images/a2a-connection-pl.png "Select A2A provider when creating a connection")

1. Give a **Name** to your connection and provide the **URL** of the agent you want to connect to. This should be the base URL of the agent's A2A endpoint.

    ![A2A connection configuration screen showing the Overview section with the Name field and the Setup connection section with the agent URL field highlighted.](images/a2a-details-pl.png "Configure A2A connection name and URL")

1. Click on **Get details** to fetch the agent card. The agent card is a JSON document that describes the agent's capabilities, skills, and how to interact with it.

    ![A2A connection screen displaying the Agent card Details tab populated with the agent name, description, provider, and version after clicking Get details.](images/a2a-get-details-pl.png "View agent card details after fetching A2A metadata")

1. Review the details to ensure they match your expectations and select the **Skills** tab to check the agent skills and authentication requirements.

    ![A2A connection screen with the Agent card Skills tab open, listing skills with their descriptions, tags, and supported authentication methods in the Authentication column.](images/a2a-supported-auth-pl.png "Review agent skills and authentication requirements")

1. Select the appropriate authentication mechanism from the drop-down and provide the necessary credentials or tokens as specified in the agent card. The supported authentication mechanisms are:

    * **System to System (OAuth)**. This mechanism requires a server token URL, a Client ID, and a Client Secret to obtain an access token for authenticating requests to the agent.

    * **Bearer token**. This mechanism requires a static token, included in the Authorization header of each request to the agent.

    * **API Key** This mechanism requires an API key, included in the request headers or query parameters as specified by the agent card and a Key name to identify the header or query parameter where the API key should be included.

    * **Basic.** This mechanism requires a username and password, encoded and included in the Authorization header of each request to the agent.

    <div class="info" markdown="1">

    Note that the dropdown shows both the OutSystems supported authentication methods and the authentication methods declared in the agent card. If the agent card declares an authentication method that is not currently supported by OutSystems, you won't be able to select it in the dropdown.

    </div>

1. Once you have provided the necessary information and credentials, click on **Test connection** to establish the connection to the external agent.

1. If the connection is successful you can define the connection individually for the other stages of your tenant or  you can click **Apply to all stages** to propagate the connection to all stages in your tenant.

1. Then click on **Save** to save the connection.

    ![A2A connection screen showing API key authentication selected with key fields filled in, a green successful connection test message, and the Save button highlighted.](images/a2a-auth-details-pl.png "Set API key authentication and save A2A connection")

1. The external agent is added to your connections lists and it's now available for use in your ODC applications and workflows, allowing you to leverage its capabilities through the A2A protocol.

    ![Connections page in the ODC portal showing a single A2A connection named Remote Agent in the list of connections.](images/a2a-connection-created-pl.png "A2A connection listed in ODC portal Connections page")

<div class="info" markdown="1">

If an agent card is updated, edit the connection, click **Get details** again, click **Test connection**, and then click **Save** to apply the updated agent card.

</div>
When you create the A2A connection, a `SendMessage` server action is automatically created for you to send messages to the remote agent. You can use this action in your ODC agentic apps to communicate with the remote agent and leverage its capabilities in your applications.
This server action's description comes from the remote agent-card JSON file. It should include the remote agent's name, description, and skills, so the ODC agent knows how to delegate requests to the right remote agent using this action as a tool.
A2A protocol support sending the message with multiple parts and each part can be of TextPart, FilePart, and DataPart types.

## Using an external agent in your ODC applications

To use the external agent in your ODC applications:

1. In your client agentic app add the `SendMessage` action from your A2A connection as a public element.

    ![ODC Studio dialog for adding public elements, with the SendMessage action from the RemoteAgent module selected in the list.](images/a2a-public-element-odcs.png "Add SendMessage as a public element in ODC Studio")

1. Inside your client agentic app logic flow, open the call Agent action.

1. Inside the call agent details, click **Add action** on the Action calling tab and select the SendMessage action from your A2A connection.

    ![ODC Studio Select ActionHandler dialog with the RemoteAgent SendMessage server action highlighted for use in the agent’s action calling configuration.](images/a2a-call-odcs.png "Select SendMessage action in agent action calling settings")

1. Then, provide the necessary input parameters for the SendMessage action, such as the Task ID, Message content, and any required metadata. The Task ID should be unique for each task you want to create with the remote agent.

    ![Action calling configuration panel for the SendMessage action showing editable input parameters such as ContextId, TaskId, and UserMessage with descriptions generated by AI.](images/a2a-call-details-odcs.png "Configure SendMessage input parameters for the agent call")

## Guidance for agents that receive/send files

When working with agents that receive or send files, using the right model is crucial to ensure proper handling of file data. Make sure to test with different models to find the one that best suits your needs.

Also, it's recommend that you enrich the system message with clear instructions on how the agent should handle file inputs and outputs.
For example, add to the system message `Each UserMessage, must include exactly one of textContent, fileContent, or dataContent.`
