#!/bin/sh
# Claude Code headersHelper for the OutSystems MCP server, authenticated as an ODC API client.
#
# Mints an OAuth2 client_credentials access token from the tenant's identity service
# and prints {"Authorization": "Bearer <token>"} on stdout. Claude Code runs it on every
# (re)connect, and re-runs it once when a tool call comes back 401, so an expired token
# is replaced without a browser login.
#
# Configuration (environment):
#   ODC_TENANT          tenant host, e.g. mycompany.outsystems.dev
#   ODC_CLIENT_ID       API client id
#   ODC_CLIENT_SECRET   API client secret (optional; see lookup order below)
#
# Secret lookup order: ODC_CLIENT_SECRET, ODC_CLIENT_SECRET_FILE (a file holding only the
# secret), the macOS keychain, then libsecret on Linux. For the last two, store it once:
#   macOS:  security add-generic-password -s odc-mcp -a "$ODC_CLIENT_ID" -w
#   Linux:  secret-tool store --label odc-mcp service odc-mcp account "$ODC_CLIENT_ID"
#
# Requires only sh, curl and sed. Nothing is cached on disk.
set -eu

fail() {
    echo "odc-mcp-token: $*" >&2
    exit 1
}

tenant=${ODC_TENANT:?set ODC_TENANT to the tenant host}
client_id=${ODC_CLIENT_ID:?set ODC_CLIENT_ID to the API client id}

secret=${ODC_CLIENT_SECRET:-}
if [ -z "$secret" ] && [ -n "${ODC_CLIENT_SECRET_FILE:-}" ]; then
    secret=$(cat "$ODC_CLIENT_SECRET_FILE")
fi
if [ -z "$secret" ] && command -v security >/dev/null 2>&1; then
    secret=$(security find-generic-password -s odc-mcp -a "$client_id" -w 2>/dev/null || true)
fi
if [ -z "$secret" ] && command -v secret-tool >/dev/null 2>&1; then
    secret=$(secret-tool lookup service odc-mcp account "$client_id" 2>/dev/null || true)
fi
[ -n "$secret" ] || fail "no client secret found for $client_id"

# The realm's token endpoint, from the tenant's OIDC discovery document.
discovery=$(curl -fsS --max-time 15 "https://$tenant/identity/.well-known/openid-configuration") ||
    fail "OIDC discovery failed for $tenant"
token_endpoint=$(printf '%s' "$discovery" | sed -n 's/.*"token_endpoint" *: *"\([^"]*\)".*/\1/p')
[ -n "$token_endpoint" ] || fail "no token_endpoint in $tenant discovery document"

# Credentials go through curl's stdin config (client_secret_basic), so they never appear in argv.
response=$(printf 'user = "%s:%s"\n' "$client_id" "$secret" |
    curl -sS --max-time 15 -K - -d grant_type=client_credentials "$token_endpoint") ||
    fail "token request to $token_endpoint failed"
token=$(printf '%s' "$response" | sed -n 's/.*"access_token" *: *"\([^"]*\)".*/\1/p')
[ -n "$token" ] || fail "token endpoint returned no access_token: $(printf '%s' "$response" | sed -n 's/.*"error_description" *: *"\([^"]*\)".*/\1/p')"

printf '{"Authorization": "Bearer %s"}\n' "$token"
