---
guid: db2a0c35-5aba-405d-ac53-338d3627a5c6
locale: en-us
summary: Requirements, provider credentials, TLS, and credential management for a custom OCI registry in Self-hosted ODC.
figma: https://www.figma.com/design/la33iciyGndnV5JRqR359g/Managing-OutSystems-platform-and-apps?node-id=5080-577
coverage-type:
  - understand
  - remember
  - apply
topic:
  - configure-registry-credentials
  - reopen-self-hosted-configurator
  - stage-prerequisites
app_type: reactive web apps,mobile apps
platform-version: odc
audience:
  - Architect
  - Platform administrator
tags:
  - Authentication
  - Authorization
  - Infrastructure
  - Security
outsystems-tools:
  - self hosted configurator
helpids:
isautopublish: true
---

# Set up the custom OCI registry for self-hosted stages

Self-hosted ODC uses a container registry to store and serve the application container images that run in your cluster. When you deploy an application, ODC builds a container image in the cloud and syncs it to this registry, making it available to your self-hosted stages.

On OpenShift, you can let OutSystems services provision and manage an in-cluster registry, or you can provide your own. On all other distributions, you must provide a custom OCI-compliant registry.

This article covers the requirements and configuration for a custom OCI registry in Self-hosted ODC. If you use the OutSystems-managed registry, available on OpenShift only, this article doesn't apply.

The registry must exist and be reachable before you start the Self-hosted configurator. During setup, the configurator asks you to select a provider and enter credentials. The registry provider and endpoint can't be changed after setup.

You can share your OCI registry with other workloads. ODC does not require dedicated credentials. OutSystems stores images under a `self_hosted/` prefix to avoid naming collisions with other content in the registry. This includes the images of your apps, which ODC stores in one repository for each app under the same prefix.

For additional isolation, you can use a registry-level path structure during initial configuration (for example, a Harbor project or a GAR repository path) to scope ODC images to a specific location within the registry (for example, `<registry>/outsystems/<image>`). For Google Cloud GAR, this path is required. For the endpoint format of each provider, refer to [Provider credentials](#provider-credentials).

## Requirements {#requirements}

Your custom OCI registry must meet the following requirements:

* It must implement the Docker Registry V2 Distribution API and return a `Docker-Distribution-API-Version: registry/2.0` header on `GET /v2/`.
* It must be accessible over HTTPS. Custom ports are supported if included in the endpoint URL (for example, `registry.example.com:8443`).
* It must exist and be reachable from the cluster before you start the Self-hosted configurator.

ODC creates and deletes repositories in your registry, so you don't need to pre-configure image paths. ODC creates a repository the first time it stores the images of an app, and deletes repositories it no longer uses, such as the repository of a deleted app. For AWS ECR, ODC calls the `CreateRepository` API before the first push, which is why `ecr:CreateRepository` is required. For all other providers, such as ACR, GAR, Harbor, Artifactory, and Docker Hub, the registry creates the repository on the first push. For the permissions these operations need, refer to [Required registry permissions](#required-permissions).

For Google Artifact Registry, the repository resource itself must be pre-created before setup, since the endpoint URL requires specifying it and IAM is bound at the repository level. Image paths within it are still created automatically.

## Capacity and retention {#capacity-retention}

Provision an initial 150 GB of storage for the initial setup. Ensure the storage is scalable, as the overall size of the container registry will grow as more applications are promoted to self-hosted stages.

When configuring retention and garbage collection policies on your registry, follow these rules:

* Do not create cleanup policies to delete images or tags.
* Do not restrict repositories to a single tag.
* Pruning untagged manifests older than 7 days is permitted.

Immutability is optional. ODC uses SHA256 digest references for internal consistency, so tag-locking doesn't affect functionality. You can enable it on production repositories for compliance purposes without impacting ODC operations.

## TLS and certificates {#tls-certificates}

Your registry must present a TLS certificate trusted by the cluster's CA bundle.

The named providers (AWS ECR, Azure ACR, Google Cloud GAR) use publicly trusted certificate authorities, and usually, no additional configuration is needed.

For registries that use a private or self-signed certificate authority, add the CA certificate to the cluster's trusted certificate store before running the Self-hosted configurator.

## Required registry permissions {#required-permissions}

ODC uses your registry credentials to manage both repositories and images. The credentials must allow the following operations:

| Operation | What ODC uses it for |
| --- | --- |
| Create repositories | Store the images of an app the first time you deploy the app to a self-hosted stage. |
| Push images | Sync app and platform images from the ODC cloud registry to your registry. |
| Pull images | Run app and platform images in your cluster. |
| List images | Check which images and tags already exist in your registry. |
| Delete images | Remove images that ODC no longer uses. |
| Delete repositories | Remove repositories that ODC no longer uses, such as the repository of a deleted app. |

The exact permission names differ by provider. For the permissions to grant on each provider, refer to [Provider credentials](#provider-credentials).

### Credential checks in the Self-hosted configurator {#credential-checks}

When you click **Test connection** or save the registry configuration, the Self-hosted configurator checks every operation in the preceding table against your registry. It pushes a test image, creates and deletes a test repository named `outsystems-validation-test/repository-probe` under the `self_hosted/` prefix, and then removes the test content.

If any check fails, the configurator rejects the credentials and keeps your existing configuration. The error message names the operation that failed and the permission to grant.

<div class="warning" markdown="1">

If your credentials can create repositories but can't delete them, the test repository `self_hosted/outsystems-validation-test/repository-probe` stays in your registry. The error message shows its full path. After you grant the missing permission, delete the test repository manually.

</div>

## Provider credentials {#provider-credentials}

Set up credentials on your registry provider before you start the Self-hosted configurator. The configurator asks for these during setup and can't proceed without them. Required fields and permissions vary by provider. The permissions listed for each provider cover all the operations in [Required registry permissions](#required-permissions).

### AWS ECR {#aws-ecr}

Before you start the Self-hosted configurator, create an IAM access key for a user or role and have the following ready from your AWS account.

| Field | Description |
| --- | --- |
| **Endpoint server** | The ECR registry URL, for example `AWS_ACCOUNT_ID.dkr.ecr.AWS_REGION.amazonaws.com`. |
| **Access key ID** | The access key ID for the IAM user or role. |
| **Secret access key** | The corresponding secret access key. |
| **Credentials expiration** | How long until the credential expires: 30, 90, 180, or 365 days. |

The IAM user or role must have the following permissions. Apply them account-wide with `"Resource": "*"`. Some permissions, such as `ecr:GetAuthorizationToken`, can't be scoped to individual repository ARNs.

* `ecr:GetAuthorizationToken`
* `ecr:BatchCheckLayerAvailability`
* `ecr:GetDownloadUrlForLayer`
* `ecr:BatchGetImage`
* `ecr:ListImages`
* `ecr:DescribeImages`
* `ecr:PutImage`
* `ecr:InitiateLayerUpload`
* `ecr:UploadLayerPart`
* `ecr:CompleteLayerUpload`
* `ecr:CreateRepository`
* `ecr:BatchDeleteImage`
* `ecr:DeleteRepository`

### Azure ACR {#azure-acr}

Before you start the Self-hosted configurator, create a service principal in Azure Active Directory and have the following ready from your Azure account.

| Field | Description |
| --- | --- |
| **Endpoint server** | The ACR login server URL, for example `REGISTRY_NAME.azurecr.io`. |
| **Client ID** | The service principal application (client) ID. |
| **Client secret** | The service principal client secret. |
| **Tenant ID** | (Optional) The Azure Active Directory tenant ID. |
| **Credentials expiration** | How long until the credential expires: 30, 90, 180, or 365 days. |

Assign the service principal the `AcrPull`, `AcrPush`, and `AcrDelete` roles. `AcrPush` covers pushing images and creating repositories, and `AcrDelete` covers deleting images and repositories. Scope the assignment to the entire registry, because ODC creates a repository for each app when the app is first deployed.

If your registry uses the **RBAC Registry + ABAC Repository Permissions** role assignment mode, Azure ignores the `AcrPull`, `AcrPush`, and `AcrDelete` roles. Assign the `Container Registry Repository Contributor` role instead, scoped to the entire registry.

### Google Cloud GAR {#google-cloud-gar}

Before you start the Self-hosted configurator, create a service account and have the following ready from your Google Cloud account.

| Field | Description |
| --- | --- |
| **Endpoint server** | The registry endpoint, including project and repository path, for example `REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY`. |
| **Service account key** | The service account JSON key file. |
| **Credentials expiration** | How long until the credential expires: 30, 90, 180, or 365 days. |

In Google Cloud GAR, the repositories that ODC creates and deletes are image paths inside the repository in the **Endpoint server** value.

Assign the service account the `roles/artifactregistry.repoAdmin` role, scoped at the repository level through IAM binding. This role covers pushing, pulling, listing, and deleting images, and deleting image paths. Don't use `roles/artifactregistry.writer`. That role doesn't include delete permissions, so the Self-hosted configurator rejects the credentials.

### Other {#other}

Before you start the Self-hosted configurator, have the following ready from your registry.

| Field | Description |
| --- | --- |
| **Endpoint server** | The registry endpoint URL. |
| **Username** | The username for authentication. |
| **Token** | The access token or password. |
| **Credentials expiration** | How long until the credential expires: 30, 90, 180, or 365 days. |

The token must allow all the operations in [Required registry permissions](#required-permissions) on the target repository.

The following table shows the credential type and required permissions for common registries that use the Other path.

| Registry | Credential type | Required permissions | Scope |
| --- | --- | --- | --- |
| Harbor | Robot account | Repository: List, Pull, Push, and Delete. Artifact: List and Delete. | Specific project |
| STACKIT Container Registry | Robot account | Repository: List, Pull, Push, and Delete. Artifact: List and Delete. | Specific project |
| Artifactory | User token | Read, Deploy/Cache, and Delete/Overwrite | Specific repositories |
| Docker Hub | Personal access token | Read, Write, and Delete | User namespace |

For Harbor, STACKIT Container Registry, and Artifactory, ODC stores images in the project or repository named in the **Endpoint server** value, for example `harbor.example.com/outsystems` or `artifactory.example.com/docker-local`. If the **Endpoint server** value is only the host name, ODC uses a project or repository named `self_hosted`. The project or repository must exist before you start the Self-hosted configurator.

The Self-hosted configurator checks repository deletion for Harbor, STACKIT Container Registry, and Artifactory. Other registries, such as Docker Hub, have no API that ODC uses to delete repositories. For these registries, the configurator returns a warning instead of rejecting the credentials, and the test repository `self_hosted/outsystems-validation-test/repository-probe` stays in your registry. Delete the test repository manually. ODC doesn't delete the repositories of deleted apps on these registries, so delete them manually too.

## Credentials expiration {#credentials-expiration}

During setup, you select how long your registry credentials are valid: 30, 90, 180, or 365 days. The value you enter must match the actual expiration of the token you generated on your registry provider. The platform relies solely on this value and never validates it against the registry.

When credentials are about to expire or have expired, the Self-hosted configurator displays a warning or an error on the **Container registry** tab in the settings homepage. For example:

![Self-hosted configurator Container registry tab with a yellow banner warning that the registry token is about to expire.](images/sh-manage-registry-warning-shc.png "Container registry tab showing token expiry warning")

OutSystems sends an email notification ahead of the expiration date to all users with the **Manage stages** permission.

When credentials expire, the sync between the ODC cloud registry and your self-hosted registry stops. Apps already running are unaffected. Deployments of new revisions to self-hosted stages may fail due to the image not being present in the self-hosted OCI.

When you update and save new credentials, the sync catches up automatically. No revisions published during the outage are lost and no manual steps are needed.

## Manage credentials after setup {#manage-credentials}

The **Container registry** tab in the Self-hosted configurator settings is available only for custom registry configurations. If you use the OutSystems-managed registry in OpenShift, this tab is not shown.
To access the settings, reopen the Self-hosted configurator. Refer to [Reopen the Self-hosted configurator](sh-open-configurator.md).

AWS ECR, Azure ACR, and Google Cloud GAR all support multiple active credentials simultaneously, so you can activate new credentials before revoking the old ones. This makes zero-downtime rotation possible. For **Other** registries, verify this with your provider before rotating.

To update or rotate your credentials, follow these steps:

1. If rotating, generate a new credential on your registry provider first. The new credential must have all the permissions in [Required registry permissions](#required-permissions). Otherwise, the Self-hosted configurator rejects it and keeps the current credential.
1. In the Self-hosted configurator, go to the **Settings** page and select **Container registry**.

    ![Self-hosted configurator Container registry tab showing endpoint, username, token, and credentials expiration fields with the Edit button highlighted.](images/sh-manage-registry-edit-shc.png "Editing container registry configuration")

1. Click **Edit**, update the authentication fields and, if needed, the **Credentials expiration** value.
1. Click **Test connection**. When the test succeeds, click **Save**. The platform propagates the new credential within seconds.
1. If rotating, confirm deployments work, then revoke the old credential on your provider.
