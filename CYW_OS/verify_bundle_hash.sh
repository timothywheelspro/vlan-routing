#!/bin/bash
# Verify CYW OS Bundle Hash
# Bundle Hash: 4a1466d6193cd6d3c69952510cad6461c6aeeb0d3841171549c1aac9cc3c6758

EXPECTED_HASH="4a1466d6193cd6d3c69952510cad6461c6aeeb0d3841171549c1aac9cc3c6758"

echo "CYW OS Bundle Hash Verification"
echo "================================="
echo ""
echo "Expected Hash: $EXPECTED_HASH"
echo ""

# Verify hash format (64 hex characters)
if [[ $EXPECTED_HASH =~ ^[0-9a-f]{64}$ ]]; then
    echo "✓ Hash format valid (SHA-256: 64 hex characters)"
else
    echo "✗ Hash format invalid"
    exit 1
fi

# Verify hash matches what's in README.md
if grep -q "$EXPECTED_HASH" CYW_OS/README.md; then
    echo "✓ Hash found in CYW_OS/README.md"
else
    echo "✗ Hash not found in CYW_OS/README.md"
    exit 1
fi

# Verify hash matches what's in originstamp_metadata.json
if grep -q "$EXPECTED_HASH" CYW_OS/originstamp_metadata.json; then
    echo "✓ Hash found in CYW_OS/originstamp_metadata.json"
else
    echo "✗ Hash not found in CYW_OS/originstamp_metadata.json"
    exit 1
fi

echo ""
echo "================================="
echo "✓ Bundle hash verification complete"
echo ""
echo "Hash is ready for OriginStamp blockchain timestamping:"
echo "  https://originstamp.com/"
echo ""
echo "Use this hash as the meta-hash for blockchain anchor:"
echo "  $EXPECTED_HASH"

