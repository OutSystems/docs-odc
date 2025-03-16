---
summary: This article provides a guide on configuring a HTTP proxy server in the operating system and ODC Studio for OutSystems Developer Cloud (ODC) connectivity.
tags: proxy configuration, http proxy, windows configuration, macos configuration, network settings
locale: en-us
guid: 00ad2577-20fe-41d3-8d0f-c6626c50b587
figma: https://www.figma.com/file/zohMj3VpAEA6P9J9azwqQq/Getting-started-with-ODC?type=design&node-id=3302%3A148&mode=design&t=3Hp6aoBfFsQyOIhR-1
app_type: mobile apps, reactive web apps
platform-version: odc
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - odc studio
coverage-type:
  - apply
topic:
  - download-and-set-up
---

# How to configure a HTTP proxy server in ODC Studio

This article explains how to configure a HTTP proxy server on your local computer to be used by ODC Studio. This applies when developers are working on a network where communications to the Internet need to go through an HTTP proxy.

To configure a HTTP proxy server:
1. [Configure the proxy server in the operating system](#configure-proxy-OS)
1. [Configure the proxy authentication in ODC Studio](#configure-proxy-odc-studio)

## Configure the proxy server in the operating system {#configure-proxy-OS}

ODC Studio relies on the proxy servers (HTTP and HTTPS) that are defined in the operating system (Windows or MacOS) when connecting to an OutSystems Developer Cloud. This means the configuration steps depend on the operating system.

### Windows setup

1. Click the **Start** icon and select **Settings**. 

    ![Opening Windows Settings for HTTP Proxy configuration](images/windows-http-proxy-settings.png "Windows HTTP Proxy Settings")

1. Select **Network & Internet**.

    ![Selecting Network & Internet in Windows Settings](images/windows-http-proxy-network-internet.png "Windows Network and Internet Selection")

1. Select **Proxy**.

1. On the proxy configurations screen:

    1. Enable the **Use a proxy server** toggle.

    1. In the **Address** field, enter ``http=example.net:9090;https=example.net:9090``replacing ``example.net`` with your proxy server name or IP address and ``9090`` with your proxy server port. 

    1. Leave the **Port** field empty.

        ![Entering proxy server details in Windows proxy configuration screen](images/windows-http-proxy-setup.png "Windows Proxy Configuration")

    1. Click **Save**.

### MacOS setup

1. Open **System Preferences**.

1. Search for **Proxies**.

    ![Searching for Proxies in MacOS System Preferences](images/mac-http-proxy-search.png "MacOS Proxy Search")

1. In the **Select a protocol to configure** section, choose **Web Proxy (HTTP)**.

    1. In the **Web proxy server** field, enter the proxy server name or IP address and port. In the example below, the proxy server is ``example.net`` and the proxy port is ``9090``.

        ![Configuring Web Proxy (HTTP) settings in MacOS](images/mac-http-proxy-web-settings.png "MacOS Web Proxy Configuration")

1. In the **Select a protocol to configure** section, select **Secure Web Proxy (HTTPS)** and enter the proxy server name or IP address and port.

    ![Configuring Secure Web Proxy (HTTPS) settings in MacOS](images/mac-http-proxy-secure-settings.png "MacOS Secure Web Proxy Configuration")

1. Click **Ok**.

## Configure the proxy authentication in ODC Studio {#configure-proxy-odc-studio}

Some proxy servers require user authentication. In this case, you must provide the proxy credentials in the ODC Studio Preferences dialog.

1. Open ODC Studio.

1. In the hamburger menu, open **Edit** > **Preferences...**.

1. Enable the **Use proxy authentication** option.

1. Enter the **Proxy username** and **Proxy password**.

    ![Entering proxy authentication details in ODC Studio Preferences](images/mac-http-proxy-authen.png "ODC Studio Proxy Authentication")

1. Click **Apply**.
