---
summary: Accessibility guidelines for the Switch widget to meet WCAG 2.2 AA compliance in ODC apps.
tags:
  - Accessibility
  - Front-End
  - UI
  - Web
  - Widgets
locale: en-us
guid: f102d83a-0de6-43f5-ba1f-ee39db127ac7
app_type: reactive web apps
figma: https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=10980-39
platform-version: odc
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - odc studio
coverage-type:
  - remember
  - apply
  - unblock
topic:
  - accessibility-screen-reader
isautopublish: true
---

# Switch

Use the following guidelines to make the **Switch** widget meet WCAG 2.2 AA compliance in your apps.

## Accessibility – WCAG 2.2 AA compliance {#accessibility}

By default, the **Switch** widget may not expose the correct ARIA attributes for assistive technologies. Set the appropriate roles so that screen readers identify it as a switch and accurately announce its state.

### Set the correct ARIA attributes

1. In **ODC Studio**, go to the **Interface** tab and select the **Screen/Block** that uses the **Switch**.

1. In the **Widget Tree**, select the **Switch** widget.  

    ![Switch in the Widget Tree](images/switch-selectswitch-odcs.png "Switch in Widget Tree")

1. In the **Switch Properties**, under **Attributes**, set `role="switch"`.  

    ![Set role in Attributes](images/switch-setattrole-odcs.png "Switch Role Attribute")

1. Then add a new attribute `aria-checked` with the following condition:

    ```text
    If([switch variable], "true", "false")
    ```

    ![Set aria-checked in Attributes](images/switch-setattariachecked-odcs.png "Aria-Checked Attribute Condition")

1. Publish the app.

### Result

After completing these steps, screen readers correctly announce the Switch as a toggle control and describe whether it's on or off, improving accessibility for all users.

Test the pattern in your app to confirm the update.
