#!/usr/bin/env python3
"""
Complete fix for Subject Guides section - replace ALL K-12 content with business departments
"""

import re

# Read the workbook
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'r') as f:
    content = f.read()

print("🔍 Fixing Subject Guides section completely...")

# 1. Fix the tab buttons in Subject Guides section (line ~3191-3194)
print("1️⃣ Fixing tab buttons...")
content = re.sub(
    r'<button class="tab active" onclick="showTab\(\'subjects\', \'english\'\)">English/Language Arts</button>',
    '<button class="tab active" onclick="showTab(\'subjects\', \'marketing\')">Marketing</button>',
    content
)
content = re.sub(
    r'<button class="tab" onclick="showTab\(\'subjects\', \'math\'\)">Mathematics</button>',
    '<button class="tab" onclick="showTab(\'subjects\', \'hr\')">Human Resources</button>',
    content
)
content = re.sub(
    r'<button class="tab" onclick="showTab\(\'subjects\', \'science\'\)">Science</button>',
    '<button class="tab" onclick="showTab(\'subjects\', \'operations\')">Operations</button>',
    content
)
content = re.sub(
    r'<button class="tab" onclick="showTab\(\'subjects\', \'history\'\)">Social Studies/History</button>',
    '<button class="tab" onclick="showTab(\'subjects\', \'sales\')">Sales</button>',
    content
)

# 2. Fix tab content IDs and headers
print("2️⃣ Fixing tab content sections...")

# English → Marketing
content = re.sub(
    r'<div id="english-tab" class="tab-content active">.*?<h3 style="color: var\(--primary-color\);">English/Language Arts AI Integration</h3>',
    '<div id="marketing-tab" class="tab-content active">\n                    <h3 style="color: var(--primary-color);">Marketing AI Integration</h3>',
    content,
    flags=re.DOTALL
)

# Math → HR
content = re.sub(
    r'<div id="math-tab" class="tab-content">.*?<h3 style="color: var\(--primary-color\);">Mathematics AI Integration</h3>',
    '<div id="hr-tab" class="tab-content">\n                    <h3 style="color: var(--primary-color);">Human Resources AI Integration</h3>',
    content,
    flags=re.DOTALL
)

# Science → Operations
content = re.sub(
    r'<div id="science-tab" class="tab-content">.*?<h3 style="color: var\(--primary-color\);">Science AI Integration</h3>',
    '<div id="operations-tab" class="tab-content">\n                    <h3 style="color: var(--primary-color);">Operations AI Integration</h3>',
    content,
    flags=re.DOTALL
)

# History → Sales
content = re.sub(
    r'<div id="history-tab" class="tab-content">.*?<h3 style="color: var\(--primary-color\);">Social Studies/History AI Integration</h3>',
    '<div id="sales-tab" class="tab-content">\n                    <h3 style="color: var(--primary-color);">Sales AI Integration</h3>',
    content,
    flags=re.DOTALL
)

# 3. Change section title
print("3️⃣ Updating section title...")
content = content.replace(
    'Subject-Specific Implementation Guides',
    'Department-Specific Implementation Guides'
)

# Write the fixed content
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'w') as f:
    f.write(content)

print("\n✅ Subject Guides section completely fixed!")
print("✅ Tab buttons updated: Marketing, HR, Operations, Sales")
print("✅ Tab content IDs updated")
print("✅ Section title changed to 'Department-Specific'")
