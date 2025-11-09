#!/usr/bin/env python3
"""
Script to add "Education Edition" to K-12 workbook and preview titles
"""

# Read workbook.html
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook.html', 'r', encoding='utf-8') as f:
    workbook_content = f.read()

# Read preview.html
with open('/home/ubuntu/prompted-ai-mastery/client/public/preview.html', 'r', encoding='utf-8') as f:
    preview_content = f.read()

# Define replacements for workbook
workbook_replacements = [
    ('<title>Prompted: AI Mastery Platform</title>', '<title>Prompted: AI Mastery Platform - Education Edition</title>'),
    ('Please enter the password to access the Prompted: AI Mastery Platform</p>', 'Please enter the password to access the Prompted: AI Mastery Platform - Education Edition</p>'),
    ('<h1>Prompted: AI Mastery Platform</h1>', '<h1>Prompted: AI Mastery Platform - Education Edition</h1>'),
    ('The Prompted: AI Mastery Platform was developed in close consultation', 'The Prompted: AI Mastery Platform - Education Edition was developed in close consultation'),
    ('This advisory board ensures the Prompted: AI Mastery Platform is grounded', 'This advisory board ensures the Prompted: AI Mastery Platform - Education Edition is grounded'),
]

# Define replacements for preview
preview_replacements = [
    ('<title>Prompted: AI Mastery Platform</title>', '<title>Prompted: AI Mastery Platform - Education Edition</title>'),
]

# Apply workbook replacements
for old, new in workbook_replacements:
    workbook_content = workbook_content.replace(old, new)

# Apply preview replacements
for old, new in preview_replacements:
    preview_content = preview_content.replace(old, new)

# Write updated files
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook.html', 'w', encoding='utf-8') as f:
    f.write(workbook_content)

with open('/home/ubuntu/prompted-ai-mastery/client/public/preview.html', 'w', encoding='utf-8') as f:
    f.write(preview_content)

print("✅ Education Edition branding added to K-12 files!")
print("📚 workbook.html updated")
print("👀 preview.html updated")
print("🎯 Now matches Business Edition branding format")
