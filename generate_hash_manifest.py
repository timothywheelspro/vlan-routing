#!/usr/bin/env python3
"""
Generate hash manifest for CYW Defensive Publication Evidence Record.

This script generates SHA-256, SHA-512, and MD5 hashes for all evidence files
and updates the combined_hash_manifest.md file.
"""

import hashlib
import os
from pathlib import Path
from datetime import datetime

# Base directory
BASE_DIR = Path("/Users/timothywheels/Projects")

# Key evidence files to hash
EVIDENCE_FILES = [
    # Layer 1: Source Code
    "Layer0_BuildPacket_v2_1/triangle_test.py",
    "contruil-architecture/state_machine.py",
    "contruil-architecture/identity_manager.py",
    "contruil-architecture/servicepath_state_machine.py",
    "budget_analyzer.py",
    
    # Layer 2: Tests
    "Layer0_BuildPacket_v2_1/test_triangle_test.py",
    "contruil-architecture/test_state_machine.py",
    "contruil-architecture/test_identity_integration.py",
    "contruil-architecture/test_security_blockers.py",
    "contruil-architecture/test_security_improvements.py",
    
    # Layer 3: Documentation
    "contruil-architecture/Patent_Filing_Combined.md",
    "IP-CLAIM.md",
    "portfolio/MERMAID_DIAGRAMS.md",
    "portfolio/architecture.html",
    "portfolio/settings.html",
    "ZONE_CONFIGURATION_GUIDE.md",
    "contruil-architecture/CONTRUIL_IP_PROTECTION_CHECKLIST.md",
    "Triangle_Test_1Page_Summary.md",
    "Triangle_Test_Slide_Deck_Outline.md",
    
    # Layer 4: Legal/IP
    "CYW_Defensive_Publication_Evidence_Record.md",
    
    # Layer 5: Cryptographic
    "combined_hash_manifest.md",
]

def calculate_hashes(filepath):
    """Calculate SHA-256, SHA-512, and MD5 hashes for a file."""
    if not filepath.exists():
        return None
    
    sha256 = hashlib.sha256()
    sha512 = hashlib.sha512()
    md5 = hashlib.md5()
    
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
            sha512.update(chunk)
            md5.update(chunk)
    
    return {
        'sha256': sha256.hexdigest(),
        'sha512': sha512.hexdigest(),
        'md5': md5.hexdigest(),
        'size': filepath.stat().st_size,
        'modified': datetime.fromtimestamp(filepath.stat().st_mtime).isoformat()
    }

def generate_manifest():
    """Generate hash manifest for all evidence files."""
    results = {}
    all_hashes = []
    
    print("Generating hash manifest...")
    print("=" * 60)
    
    for rel_path in EVIDENCE_FILES:
        filepath = BASE_DIR / rel_path
        
        if filepath.exists():
            hashes = calculate_hashes(filepath)
            if hashes:
                results[rel_path] = hashes
                all_hashes.append(hashes['sha256'])
                print(f"✓ {rel_path}")
                print(f"  SHA-256: {hashes['sha256']}")
                print(f"  Size: {hashes['size']} bytes")
                print(f"  Modified: {hashes['modified']}")
                print()
        else:
            print(f"✗ {rel_path} - NOT FOUND")
            print()
    
    # Calculate combined manifest hash
    combined_string = ''.join(sorted(all_hashes))
    combined_sha256 = hashlib.sha256(combined_string.encode()).hexdigest()
    combined_sha512 = hashlib.sha512(combined_string.encode()).hexdigest()
    combined_md5 = hashlib.md5(combined_string.encode()).hexdigest()
    
    print("=" * 60)
    print("Combined Manifest Hash:")
    print(f"SHA-256: {combined_sha256}")
    print(f"SHA-512: {combined_sha512}")
    print(f"MD5: {combined_md5}")
    print()
    
    # Generate output file
    output_file = BASE_DIR / "hash_manifest_output.txt"
    with open(output_file, 'w') as f:
        f.write("# Hash Manifest Output\n")
        f.write(f"Generated: {datetime.now().isoformat()}\n")
        f.write(f"Priority Date: December 30, 2025, 6:42:05 AM EST\n")
        f.write(f"Inventor: Timothy I. Wheels\n")
        f.write(f"Organization: Contruil LLC\n\n")
        f.write("=" * 60 + "\n\n")
        
        for rel_path, hashes in sorted(results.items()):
            f.write(f"File: {rel_path}\n")
            f.write(f"SHA-256: {hashes['sha256']}\n")
            f.write(f"SHA-512: {hashes['sha512']}\n")
            f.write(f"MD5: {hashes['md5']}\n")
            f.write(f"Size: {hashes['size']} bytes\n")
            f.write(f"Modified: {hashes['modified']}\n")
            f.write("\n")
        
        f.write("=" * 60 + "\n\n")
        f.write("Combined Manifest Hash:\n")
        f.write(f"SHA-256: {combined_sha256}\n")
        f.write(f"SHA-512: {combined_sha512}\n")
        f.write(f"MD5: {combined_md5}\n")
    
    print(f"Output saved to: {output_file}")
    print(f"Total files hashed: {len(results)}")
    
    return results, {
        'sha256': combined_sha256,
        'sha512': combined_sha512,
        'md5': combined_md5
    }

if __name__ == "__main__":
    results, combined = generate_manifest()
    print("\n✓ Hash manifest generation complete!")

