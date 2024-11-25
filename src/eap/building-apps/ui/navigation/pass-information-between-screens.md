---
summary: Learn how to pass data between screens using Input Parameters in OutSystems Developer Cloud (ODC).
tags: navigation, user interface, data transfer, app development, screen design
locale: en-us
guid: f1443b9a-dbfa-440b-b618-69835bbcb361
app_type: mobile apps, reactive web apps
figma: https://www.figma.com/file/6G4tyYswfWPn5uJPDlBpvp/Building-apps?type=design&node-id=3101-10808&t=jVWF79X470YE6UeE-0
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - odc studio
content-type:
  - procedure
  - process
---

# Pass Data Between Screens With Input Parameters

Screens sometimes require input information. This is common in navigation, when users click on a link wanting to see more about an item. The destination Screen receives the information about the item, for example an identifier of a product. You pass information between screens with Input Parameters.

To pass information with Input Parameters:

1. In the destination Screen add an Input Parameter.
2. In the source Screen add a link to the destination Screen and set the Input Parameter value.

## Add a new Input Parameter in the destination Screen

To add an Input Parameter to a Screen in ODC Studio:

1. Go to **Interface** > **UI Flows** > **MainFlow** and locate your Screen.

    ![Screenshot showing a selected screen within ODC Studio's UI Flows section](images/screen-selected-odcs.png "Selected Screen in ODC Studio")

    <div class="info" markdown="1">

    You can use Input Parameters with Blocks as well. 

    </div>
    
   
2. Right-click the Screen and select **Add Input Parameter**. A new Input Parameter appears. 

    ![Context menu in ODC Studio with an option to add an Input Parameter to a screen](images/help-menu-input-parameter-odcs.png "Help menu to Create Input Parameter")

3. ODC Studio selects the name of the Input Parameter and sets the focus for you to enter the name. Enter the name of the Input Parameter and press the Enter key.

    ![New Input Parameter field in ODC Studio with the text name highlighted for editing](images/new-input-parameter-odcs.png "Input Parameter with selected text name")

## Send a value from the source Screen

In the Screen from which you're linking (source) to the Screen that receives the value (destination), add a widget and supply a value in the **On Click Event**. Here is an example with a Link widget, but the same works with a Button.

1. Search for the **Link** widget and drag it to the Screen. Then, enter your link text, for example "A link to another page".
   
    ![ODC Studio screen interface showing a Link widget with placeholder text](images/screen-with-link-odcs.png "A Screen with a link")

    Right now you can't publish the app because the 1-Click Publish button is red and there's an error. That is expected, as you need to set a destination for your Link as well. 

2. Select the Link widget, go to **Properties** > **Events** > **On Click**, and in the list select your destination Screen. Notice how the Input Parameter shows below the Screen name in the properties.

    ![Properties panel in ODC Studio displaying the selected Link widget and its associated Input Parameter](images/link-properties-input-parameter-odcs.png "Link widget properties with the input parameter")
    
3. Still in the Link widget properties, under the Screen you selected, set the value for the Input Parameter.

    ![Input field for setting the value of an Input Parameter in the Link widget properties within ODC Studio](images/link-properties-input-parameter-set-odcs.png "Set value for the input parameter")

    In our example, we entered **100** directly in the Input Parameter field. Usually you set a dynamic value, for example, with a Local Variable.

4. Publish the app. When you click the link in the source Screen, the user navigates to the destination Screen. The destination Screen opens and receives **100** as the value of the Input Parameter.
