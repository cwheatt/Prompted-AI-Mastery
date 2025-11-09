#!/usr/bin/env python3
"""
Script to remove password protection from business edition workbook
"""

import re

# Read the business workbook
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and remove the password modal div (lines 812-822)
password_modal_pattern = r'    <!-- Password Protection -->\s*<div id="passwordModal".*?</div>\s*</div>'
content = re.sub(password_modal_pattern, '', content, flags=re.DOTALL)

# Find and remove the password script (lines 823-855)
password_script_pattern = r'    <script>\s*// Password protection.*?</script>'
content = re.sub(password_script_pattern, '', content, flags=re.DOTALL)

# Write the updated file
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Password protection removed from business edition!")
print("🔓 workbook-bus.html is now freely accessible")
