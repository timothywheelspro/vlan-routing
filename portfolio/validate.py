#!/usr/bin/env python3
"""
Quick validation script for portfolio HTML files.
Checks for common issues before deployment.
"""

import re
from pathlib import Path

def validate_html_file(filepath):
    """Validate an HTML file for common issues."""
    issues = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = Path(filepath).name
        
        # Check for basic HTML structure
        if '<!doctype html>' not in content.lower() and '<!DOCTYPE html>' not in content:
            issues.append(f"{filename}: Missing DOCTYPE declaration")
        
        if '<html' not in content:
            issues.append(f"{filename}: Missing <html> tag")
        
        if '</html>' not in content:
            issues.append(f"{filename}: Missing closing </html> tag")
        
        # Check for title
        if '<title>' not in content:
            issues.append(f"{filename}: Missing <title> tag")
        
        # Check for viewport meta tag
        if 'viewport' not in content:
            issues.append(f"{filename}: Missing viewport meta tag")
        
        # Check for common broken links
        broken_patterns = [
            (r'href="\.\./styles\.css"', 'References external styles.css (styles are inline, this is fine if intentional)'),
        ]
        
        # Check email links
        if 'mailto:' in content:
            emails = re.findall(r'mailto:([^\s"]+)', content)
            if not emails or 'timothy@timothywheels.com' not in emails[0]:
                issues.append(f"{filename}: Check email addresses in mailto links")
        
        # Check for relative links between pages
        if filename == 'landing.html' and 'index.html' not in content:
            issues.append(f"{filename}: No link to index.html found")
        
        if filename == 'index.html' and 'landing.html' not in content:
            issues.append(f"{filename}: No link back to landing.html found")
        
        return issues
        
    except FileNotFoundError:
        return [f"{filepath}: File not found"]
    except Exception as e:
        return [f"{filepath}: Error reading file - {str(e)}"]

def main():
    """Main validation function."""
    portfolio_dir = Path(__file__).parent
    html_files = ['landing.html', 'index.html']
    
    print("=" * 60)
    print("Portfolio HTML Validation")
    print("=" * 60)
    print()
    
    all_issues = []
    
    for html_file in html_files:
        filepath = portfolio_dir / html_file
        if filepath.exists():
            issues = validate_html_file(filepath)
            if issues:
                print(f"⚠️  {html_file}:")
                for issue in issues:
                    print(f"   - {issue}")
                    all_issues.append(f"{html_file}: {issue}")
                print()
            else:
                print(f"✅ {html_file}: No issues found")
                print()
        else:
            print(f"❌ {html_file}: File not found")
            all_issues.append(f"{html_file}: File not found")
            print()
    
    print("=" * 60)
    if all_issues:
        print(f"Found {len(all_issues)} potential issue(s)")
        print("Review the issues above before deploying")
        return 1
    else:
        print("✅ All files passed validation!")
        print("Ready to deploy.")
        return 0

if __name__ == "__main__":
    exit(main())

