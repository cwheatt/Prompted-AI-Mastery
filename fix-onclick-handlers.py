#!/usr/bin/env python3
"""
Fix all onclick handlers to pass event parameter to showSection
"""

import re

# Read the workbook
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'r') as f:
    content = f.read()

print("🔧 Fixing onclick handlers to pass event parameter...")

# Replace all onclick="showSection('...')" with onclick="showSection('...', event)"
content = re.sub(
    r'onclick="showSection\(\'([^\']+)\'\)"',
    r'onclick="showSection(\'\1\', event)"',
    content
)

# Write the fixed content
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'w') as f:
    f.write(content)

print("✅ All onclick handlers fixed!")
print("✅ Navigation should now work correctly")
