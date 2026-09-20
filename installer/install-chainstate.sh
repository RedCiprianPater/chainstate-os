#!/usr/bin/env bash
set -Eeuo pipefail
: "${CHAINSTATE_AUTH_URL:?Set CHAINSTATE_AUTH_URL}"
: "${CHAINSTATE_BUNDLE:?Set CHAINSTATE_BUNDLE}"
: "${CHAINSTATE_WALLET:?Set CHAINSTATE_WALLET}"
: "${CHAINSTATE_ENTITLEMENT:?Set CHAINSTATE_ENTITLEMENT}"
: "${CHAINSTATE_SIGNATURE:?Set CHAINSTATE_SIGNATURE}"
command -v curl >/dev/null || { echo 'curl required' >&2; exit 1; }
command -v sha256sum >/dev/null || { echo 'sha256sum required' >&2; exit 1; }
test -f "$CHAINSTATE_BUNDLE" || { echo 'Bundle not found' >&2; exit 1; }
HASH=$(sha256sum "$CHAINSTATE_BUNDLE" | awk '{print $1}')
PAYLOAD=$(python3 - "$CHAINSTATE_WALLET" "$CHAINSTATE_ENTITLEMENT" "$HASH" "$CHAINSTATE_SIGNATURE" <<'PY'
import json,sys
wallet,entitlement,bundle_hash,signature=sys.argv[1:]
print(json.dumps({'wallet':wallet,'entitlementId':entitlement,'bundleSha256':bundle_hash,'signature':signature}))
PY
)
RESPONSE=$(curl --fail-with-body --silent --show-error --connect-timeout 10 --max-time 30 -H 'content-type: application/json' -X POST "$CHAINSTATE_AUTH_URL" --data "$PAYLOAD") || { echo 'Authorization unavailable; installation denied.' >&2; exit 1; }
python3 - "$RESPONSE" <<'PY'
import json,sys
data=json.loads(sys.argv[1])
if data.get('authorized') is not True or not data.get('installToken'):
    raise SystemExit('Installation denied by authorization service')
print('Payment and same-wallet authorization accepted by server.')
print('Attach only a reviewed, signed package installation step here.')
PY
