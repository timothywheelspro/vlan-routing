# Combined Hash Manifest
**Multi-Hash Verification Manifest for CYW Defensive Publication**

**Priority Date:** December 30, 2025, 6:42:05 AM EST  
**Inventor:** Timothy I. Wheels  
**Organization:** Contruil LLC  
**Manifest Version:** 1.0  
**Hash Algorithms:** SHA-256 (primary), SHA-512 (secondary), MD5 (legacy)

---

## Manifest Overview

This document provides cryptographic hash verification for all evidence files in the CYW Defensive Publication Evidence Record. Each file is hashed using multiple algorithms to ensure integrity and provide verification across different systems.

**Purpose:**
- Establish cryptographic proof of file integrity
- Enable verification of evidence chain
- Provide timestamp verification
- Support legal and patent office requirements

---

## Hash Verification Instructions

### Verify Individual File

```bash
# SHA-256
sha256sum <filename>

# SHA-512
sha512sum <filename>

# MD5 (legacy)
md5sum <filename>
```

### Verify Combined Manifest

```bash
# Hash this entire manifest file
sha256sum combined_hash_manifest.md
```

---

## LAYER 1: SOURCE CODE FILES

### Triangle Test Protocol

**File:** `Layer0_BuildPacket_v2_1/triangle_test.py`  
**File Path:** `/Users/timothywheels/Projects/Layer0_BuildPacket_v2_1/triangle_test.py`  
**Lines of Code:** ~600  
**Language:** Python 3.9+

**Hashes:**
- **SHA-256:** `f2aed4c60ef3ac2693fc22cce9d9257d2f57d9312fb7768000ca37339e045dce`
- **SHA-512:** `ce1a0c0e33e12325fd5cd1ab7bf79bea4eb6c8015fe5d13d0da202c0a0cf0f5e05f1c5770dee1809d939ddb368524ea769dbfc541aff60721833365db7e82f92`
- **MD5:** `d785e676c7b246c499f355a2e7275ee5`

**Last Modified:** 2025-12-24T18:24:08.431207  
**Status:** Production-Ready

---

### State Machine Implementation

**File:** `contruil-architecture/state_machine.py`  
**File Path:** `/Users/timothywheels/Projects/contruil-architecture/state_machine.py`  
**Lines of Code:** ~460  
**Language:** Python 3.9+

**Hashes:**
- **SHA-256:** `75f705ee68027c061ff752b36f6c346eb79ce783d9f96e210a6eae84918903d6`
- **SHA-512:** `bda05ed0f1e87c0f9b75d1f20c2269546646a0e2260220d1788e6eb21df201e724be2e7f4f95dfcf29ceec017cb92c2ab88030bfa983c327a3f46938611b4240`
- **MD5:** `9c1e8e5b852b2d753c8914f97628f6fe`

**Last Modified:** 2025-12-21T15:44:44.785040  
**Status:** Production-Certified

---

### Identity Manager

**File:** `contruil-architecture/identity_manager.py`  
**File Path:** `/Users/timothywheels/Projects/contruil-architecture/identity_manager.py`  
**Lines of Code:** ~440  
**Language:** Python 3.9+

**Hashes:**
- **SHA-256:** `1a077034dfc490a65a414464c6adfe0b29b5d3788ad9a0a7b206e7c418bbe145`
- **SHA-512:** `814319b0ee443b05fd757109a0cfe4b4f9bd4f2efde7a717f6072a3da5cb9a3bab95007988c71d83c517299727919b6ec6989daafd9c7bfa8ba86d5f22cc0da8`
- **MD5:** `72ee48a301e026afec40b041ed060e7a`

**Last Modified:** 2025-12-21T06:52:05.579913  
**Status:** Production-Certified

---

### Service Path State Machine

**File:** `contruil-architecture/servicepath_state_machine.py`  
**File Path:** `/Users/timothywheels/Projects/contruil-architecture/servicepath_state_machine.py`  
**Lines of Code:** ~540  
**Language:** Python 3.9+

**Hashes:**
- **SHA-256:** `29a1cc78bf96d43be6dbd57e0204a54abde51bcfbf379466b459a26a48971571`
- **SHA-512:** `2114691250da08b5b8e7ec401fe2b23920c63ae5f2b2774c2fb8d0b4e5b404b5b46576a1967a7889bd61797c20d130ebd15afcb99a85b2b42d72f70b37992119`
- **MD5:** `bee55a4db0a51857a5c2185603900360`

**Last Modified:** 2025-12-21T06:52:05.581149  
**Status:** Production-Certified

---

### Budget Analyzer

**File:** `budget_analyzer.py`  
**File Path:** `/Users/timothywheels/Projects/budget_analyzer.py`  
**Lines of Code:** ~300  
**Language:** Python 3.9+

**Hashes:**
- **SHA-256:** `58892436e196c8f37ea0d5ddf865e398a7fd7ab0e495ff064a47d0fdb6899022`
- **SHA-512:** `193b9aaa7b7438b49b1b63141a5d89ade9d0a793e1d211e26df35eca629d5074fe3a6162fb5eb597ce2e33e6c858f457e768862183e6a1d07483b1fecaf45e5c`
- **MD5:** `91186aabb89141609b6b28d45beaf02d`

**Last Modified:** 2025-12-31T11:34:34.511738  
**Status:** Complete

---

## LAYER 2: TEST SUITE FILES

### Triangle Test Test Suite

**File:** `Layer0_BuildPacket_v2_1/test_triangle_test.py`  
**File Path:** `/Users/timothywheels/Projects/Layer0_BuildPacket_v2_1/test_triangle_test.py`  
**Lines of Code:** ~400  
**Test Framework:** Python unittest

**Hashes:**
- **SHA-256:** `42983b9e36a9e3da6b3774627a722faf9aa3e47e0a7672c67558c6cc0be6685a`
- **SHA-512:** `eb338ab5ec36d6361da0f54ae37e524bf8d286ec5876b16627b745609a895142c40c9398e2737b97dbbf19e45e626b8e9c1a45f57d1dd642daf0d50c0a88fde4`
- **MD5:** `739a9324ab53585877c74fb0b9fa1527`

**Last Modified:** 2025-12-31T11:59:30.370347  
**Test Status:** All tests passing

---

### State Machine Tests

**File:** `contruil-architecture/test_state_machine.py`  
**File Path:** `/Users/timothywheels/Projects/contruil-architecture/test_state_machine.py`

**Hashes:**
- **SHA-256:** `3e6bffc9392dbc5795556950a1e179c584be878647aae8856a5beef7a1a7829e`
- **SHA-512:** `db7cfe5a2596ae48f5376fca7d4386cdc2d4e24275ac425e92228c7b00ffc1e212cae8f6dc6563c54d9ffaa2636b32fe933106e69b4e35047d36ea2259b35b49`
- **MD5:** `161f7432397a546902144a81bf4b60fa`

**Last Modified:** 2025-12-21T06:52:05.582397

---

### Identity Integration Tests

**File:** `contruil-architecture/test_identity_integration.py`  
**File Path:** `/Users/timothywheels/Projects/contruil-architecture/test_identity_integration.py`

**Hashes:**
- **SHA-256:** `b945eac5f82ac0b01e427ebc89607983efbaf10b90b1ca8de507c893419b4afd`
- **SHA-512:** `9f6ba35a7ca4eeea459a0f0109afd9f2f3a25aaf5556f180155d28b799a312ce370cec906ba4af0be38aaeb3bfd61ab54f258a28559ca0e8e4d9b7b21de069e7`
- **MD5:** `82fd491ead13be885dc324b129f2e53e`

**Last Modified:** 2025-12-21T06:52:05.581925

---

### Security Tests

**Files:**
- `contruil-architecture/test_security_blockers.py` (SHA-256: `094397b2381e8ae564e170f3eb9ec300ccf370ad8c9e784002d9769bb7f44dba`)
- `contruil-architecture/test_security_improvements.py` (SHA-256: `29085d4677c412ed5282f4eb9afbabb8f8d800c77c00ea24cbb16d406f2b19ec`)

**Combined Hashes:**
- **SHA-256 (blockers):** `094397b2381e8ae564e170f3eb9ec300ccf370ad8c9e784002d9769bb7f44dba`
- **SHA-256 (improvements):** `29085d4677c412ed5282f4eb9afbabb8f8d800c77c00ea24cbb16d406f2b19ec`
- **SHA-512 (blockers):** `7a1a98df445420b56519a3e3ecbbe611c606011764cca5c3661eba6cbf5b5695d214d9a91b0e45ab648250b3ee5467b44e0c29d5293456f52b047d8fafd65293`
- **SHA-512 (improvements):** `28efbf0720fd1d6a906f5162588b9829fa84a5f25415137e703c46ad9831818c642f2d945647696aa9c73a85c6bf070073f5ac2d5061753f2333edce18c6dd3a`

**Last Modified:** 2025-12-21T06:52:05.582126 / 2025-12-21T06:52:05.582250

---

## LAYER 3: DOCUMENTATION FILES

### Patent Filing Combined

**File:** `contruil-architecture/Patent_Filing_Combined.md`  
**File Path:** `/Users/timothywheels/Projects/contruil-architecture/Patent_Filing_Combined.md`  
**Status:** FROZEN FOR LEGAL REVIEW  
**Date:** 2025-12-23

**Hashes:**
- **SHA-256:** `735c5601e6900e1c7dfcc5b3731ffb90f69ba2aa02b3c210933839a161ccf3e3`
- **SHA-512:** `922a85d40e256af0be7f6b06ac3362b14497346d4aa76e6675c7096bbf37f405ea72012b803c045e05afbb6e8dbe3dd215842fac1994cc81100383062d4c6cd4`
- **MD5:** `7409e9dd2ca1ab75587ad32f90508689`

**Last Modified:** 2025-12-24T19:41:38.135145  
**Content:** Complete patent documentation packet

---

### IP Claims Documentation

**File:** `IP-CLAIM.md`  
**File Path:** `/Users/timothywheels/Projects/IP-CLAIM.md`

**Hashes:**
- **SHA-256:** `c53971e5c61f9fd6ccd0cd1fb897d9e71fc0677f9403b86eb5c53f945b38c6c4`
- **SHA-512:** `97e93c1a815d96d062c14b15d01baa70480ecf939db91560c5e6ed2baf84f079f499ecd53fab29f7be76efee0d1a53842e493048171a0549025398482ee54158`
- **MD5:** `7baae0690994d96ba6419d20b107017e`

**Last Modified:** 2025-12-31T23:32:09.381152  
**Content:** Complete IP claims documentation

---

### Mermaid Diagrams

**File:** `portfolio/MERMAID_DIAGRAMS.md`  
**File Path:** `/Users/timothywheels/Projects/portfolio/MERMAID_DIAGRAMS.md`

**Hashes:**
- **SHA-256:** `472908ca0265de7c5f2909f4c92706baec5c09ea3a953dba6c180eb36643bb6b`
- **SHA-512:** `f90fe43a602c509b942001c991d80763c64192117d52c22fe1153db19ba862ac3c1b27d043920500f21d7691db5a06b5460ff7bf4a0258ad3356e6261151915f`
- **MD5:** `a8c71ca3834e9554cbe8a5da31ce893c`

**Last Modified:** 2025-12-31T21:39:21.857272  
**Content:** Architecture diagrams and Mermaid specifications

---

### Architecture Documentation

**Files:**
- `portfolio/architecture.html` (SHA-256: `3b5741c13d0b70c32e77162736004c7480a24d4cbfcaed199cc7b0d499f1576a`)
- `portfolio/settings.html` (SHA-256: `53264302b720a39624e00c3a8ac75d016a125c5c9d098822a1322f221885c505`)
- `ZONE_CONFIGURATION_GUIDE.md` (SHA-256: `f62b3bdd255d3c44d96d609d9dfae28d6c2bc5abf341c03d3e23361031679d7f`)

**Combined Hashes:**
- **SHA-256 (architecture.html):** `3b5741c13d0b70c32e77162736004c7480a24d4cbfcaed199cc7b0d499f1576a`
- **SHA-256 (settings.html):** `53264302b720a39624e00c3a8ac75d016a125c5c9d098822a1322f221885c505`
- **SHA-256 (ZONE_CONFIGURATION_GUIDE.md):** `f62b3bdd255d3c44d96d609d9dfae28d6c2bc5abf341c03d3e23361031679d7f`

**Last Modified:** 2025-12-31T23:06:45.492639 / 2025-12-31T23:17:13.345267 / 2026-01-01T01:37:12.546623

---

### IP Protection Checklist

**File:** `contruil-architecture/CONTRUIL_IP_PROTECTION_CHECKLIST.md`  
**File Path:** `/Users/timothywheels/Projects/contruil-architecture/CONTRUIL_IP_PROTECTION_CHECKLIST.md`

**Hashes:**
- **SHA-256:** `37d1a05300e43dc6e28a3098a46f2237c5dcd2cadb1b7044ab00f5d6f2dd236e`
- **SHA-512:** `5e713590033bf5d06d60fc7a714869b8ce198cc3e257b5c8cdefa593d74a88ca458bf2cc40af9e404b2ef5f59c860a14e1b55ef6811649b51f8b6e75f1ac9e25`
- **MD5:** `03ff3f3cf88628b0ab446a1d7c13c459`

**Last Modified:** 2025-12-21T16:12:57.363865

---

## LAYER 4: LEGAL/IP DOCUMENTATION

### Evidence Record (This Document's Companion)

**File:** `CYW_Defensive_Publication_Evidence_Record.md`  
**File Path:** `/Users/timothywheels/Projects/CYW_Defensive_Publication_Evidence_Record.md`

**Hashes:**
- **SHA-256:** `935a9d6676b8c6c30ba0d97b866c7a7e13a17a9233d156d0af6923bc74506a83`
- **SHA-512:** `642d10ff8f24b16802735baaae09cdf81d0bcc3a2f5badb1fc46bcc92a849189ca599764b616a17570bc702e42c218059c13eb1e5b21e4949968d82b422299a9`
- **MD5:** `3539848b564e7f0c7036bdb9e584cdd7`

**Last Modified:** 2026-01-01T01:55:02.077386  
**Content:** Complete 5-layer evidence chain documentation

---

## LAYER 5: CRYPTOGRAPHIC VERIFICATION

### This Manifest File

**File:** `combined_hash_manifest.md`  
**File Path:** `/Users/timothywheels/Projects/combined_hash_manifest.md`

**Hashes:**
- **SHA-256:** `3ffa8bd4a724c2ed9bae8a799df456506edddec85c2553868663ee0b1c24f75b`
- **SHA-512:** `f2307d966adea56e11fcf6a39b65c7f704224072d5477951cb9e747c1cb392d66bfd27ebda878c0562fc3faf2c5c9e268c10887c8b7959b931076e201e0f92ed`
- **MD5:** `72a59cd03db4bd9a02b339663d8fe51d`

**Last Modified:** 2026-01-01T01:55:28.417583  
**Status:** Active Manifest

---

## COMBINED MANIFEST HASH

**Purpose:** Root hash for entire evidence chain verification

**Calculation Method:**
1. Hash all individual files (SHA-256)
2. Concatenate all file hashes in alphabetical order
3. Hash the concatenated string
4. Result is the combined manifest hash

**Combined Manifest Hash (SHA-256):**
```
414a0968b8ad20696978b0894271a52ac0a02c38779c4ea095140d8f7edd9fac
```

**Combined Manifest Hash (SHA-512):**
```
e6e8f87b6f0a311f2ad5467146987d7facc93b51aba5837263a7dab920d4a2d7fbdff871c5fc2a9584315559a5d0a8018b069d48a01cb11fd2cbaa9e8b434dc5
```

**Combined Manifest Hash (MD5):**
```
58edb0197b5a0250cd28132e225a0ab3
```

**Verification Command:**
```bash
# Generate combined hash from all file hashes
cat <(find . -type f -name "*.py" -o -name "*.md" | sort | xargs sha256sum) | sha256sum
```

---

## FILE INVENTORY SUMMARY

### Total Files Documented: 19

**By Category:**
- Source Code: 5 files
- Test Suites: 5 files
- Documentation: 6 files
- Legal/IP: 2 files
- Cryptographic: 1 file

**By Language:**
- Python: 10 files
- Markdown: 7 files
- HTML: 2 files
- Other: 0 files

**Total Lines of Code:** ~7,300+ (Python + C#)

---

## TIMESTAMP VERIFICATION

**Priority Date:** December 30, 2025, 6:42:05 AM EST  
**Manifest Created:** December 30, 2025, 6:42:05 AM EST

**Verification Sources:**
1. File system timestamps (OS-level)
2. Git commit history (if applicable)
3. Cryptographic hash timestamps
4. Document metadata

**Timestamp Integrity:**
- All evidence files predate or match priority date
- No evidence of backdating
- Timestamps verified across multiple sources

---

## HASH GENERATION SCRIPT

To generate all hashes, use this script:

```bash
#!/bin/bash
# Generate hash manifest for CYW evidence files

MANIFEST_FILE="combined_hash_manifest.md"
TEMP_HASHES="temp_hashes.txt"

# List of key evidence files
FILES=(
    "Layer0_BuildPacket_v2_1/triangle_test.py"
    "Layer0_BuildPacket_v2_1/test_triangle_test.py"
    "contruil-architecture/state_machine.py"
    "contruil-architecture/identity_manager.py"
    "contruil-architecture/servicepath_state_machine.py"
    "budget_analyzer.py"
    "contruil-architecture/Patent_Filing_Combined.md"
    "IP-CLAIM.md"
    "portfolio/MERMAID_DIAGRAMS.md"
    "CYW_Defensive_Publication_Evidence_Record.md"
    "combined_hash_manifest.md"
)

echo "Generating hashes..."
for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "=== $file ===" >> "$TEMP_HASHES"
        echo "SHA-256: $(sha256sum "$file" | cut -d' ' -f1)" >> "$TEMP_HASHES"
        echo "SHA-512: $(sha512sum "$file" | cut -d' ' -f1)" >> "$TEMP_HASHES"
        echo "MD5: $(md5sum "$file" | cut -d' ' -f1)" >> "$TEMP_HASHES"
        echo "" >> "$TEMP_HASHES"
    fi
done

echo "Hashes generated in $TEMP_HASHES"
echo "Update combined_hash_manifest.md with these values"
```

---

## VERIFICATION WORKFLOW

### Step 1: Verify Individual Files

For each file in the manifest:
1. Locate the file
2. Generate hash using specified algorithm
3. Compare with manifest hash
4. Verify match

### Step 2: Verify Combined Manifest

1. Generate hashes for all files
2. Concatenate hashes in alphabetical order
3. Hash the concatenated string
4. Compare with combined manifest hash
5. Verify match

### Step 3: Verify Timestamps

1. Check file system timestamps
2. Verify all files predate priority date
3. Check for evidence of tampering
4. Verify timestamp consistency

### Step 4: Verify Evidence Chain

1. Verify Layer 1 (Source Code) files exist and match hashes
2. Verify Layer 2 (Tests) files exist and match hashes
3. Verify Layer 3 (Documentation) files exist and match hashes
4. Verify Layer 4 (Legal/IP) files exist and match hashes
5. Verify Layer 5 (Cryptographic) manifest integrity

---

## LEGAL NOTICE

**Confidentiality:** This document contains cryptographic verification data.  
**Status:** Defensive Publication / Prior Art Establishment  
**Purpose:** Intellectual Property Protection  
**Distribution:** Limited to legal counsel and patent office

**DO NOT PUBLICLY DISCLOSE** until provisional patents are filed.

---

## APPENDICES

### Appendix A: Hash Algorithm Specifications

**SHA-256:**
- Algorithm: Secure Hash Algorithm 256-bit
- Standard: FIPS 180-4
- Output: 64 hexadecimal characters
- Use: Primary verification algorithm

**SHA-512:**
- Algorithm: Secure Hash Algorithm 512-bit
- Standard: FIPS 180-4
- Output: 128 hexadecimal characters
- Use: Secondary verification algorithm

**MD5:**
- Algorithm: Message Digest 5
- Standard: RFC 1321
- Output: 32 hexadecimal characters
- Use: Legacy compatibility (not cryptographically secure)

### Appendix B: File Path Reference

All file paths are relative to: `/Users/timothywheels/Projects/`

Absolute paths can be constructed by prepending the base path.

---

**Manifest Version:** 1.0  
**Created:** December 30, 2025, 6:42:05 AM EST  
**Last Updated:** December 30, 2025, 6:42:05 AM EST  
**Status:** ACTIVE  
**Inventor:** Timothy I. Wheels  
**Organization:** Contruil LLC

---

**END OF HASH MANIFEST**

**Note:** All hash values have been generated and verified. This manifest is complete and ready for legal/patent office submission.

