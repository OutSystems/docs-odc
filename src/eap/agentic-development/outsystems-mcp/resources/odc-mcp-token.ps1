# Claude Code headersHelper for the OutSystems MCP server, authenticated as an ODC API client.
# Windows counterpart of odc-mcp-token.sh: same environment variables and output.
#
# Secret lookup order: ODC_CLIENT_SECRET, ODC_CLIENT_SECRET_FILE, then Windows Credential
# Manager (generic credential "odc-mcp:<client id>", read through the CredentialManager
# module when it is installed: Install-Module CredentialManager -Scope CurrentUser).
#
# Register with: "headersHelper": "pwsh -NoProfile -File C:/path/odc-mcp-token.ps1"
$ErrorActionPreference = 'Stop'

function Fail([string] $message) {
    [Console]::Error.WriteLine("odc-mcp-token: $message")
    exit 1
}

$tenant = $env:ODC_TENANT
$clientId = $env:ODC_CLIENT_ID
if (-not $tenant) { Fail 'set ODC_TENANT to the tenant host' }
if (-not $clientId) { Fail 'set ODC_CLIENT_ID to the API client id' }

$secret = $env:ODC_CLIENT_SECRET
if (-not $secret -and $env:ODC_CLIENT_SECRET_FILE) {
    $secret = (Get-Content -Raw $env:ODC_CLIENT_SECRET_FILE).Trim()
}
if (-not $secret -and (Get-Command Get-StoredCredential -ErrorAction SilentlyContinue)) {
    $stored = Get-StoredCredential -Target "odc-mcp:$clientId"
    if ($stored) { $secret = $stored.GetNetworkCredential().Password }
}
if (-not $secret) { Fail "no client secret found for $clientId" }

try {
    $discovery = Invoke-RestMethod -TimeoutSec 15 "https://$tenant/identity/.well-known/openid-configuration"
} catch {
    Fail "OIDC discovery failed for ${tenant}: $($_.Exception.Message)"
}

try {
    $response = Invoke-RestMethod -TimeoutSec 15 -Method Post -Uri $discovery.token_endpoint -Body @{
        grant_type    = 'client_credentials'
        client_id     = $clientId
        client_secret = $secret
    }
} catch {
    Fail "token request failed: $($_.Exception.Message)"
}

@{ Authorization = "Bearer $($response.access_token)" } | ConvertTo-Json -Compress
