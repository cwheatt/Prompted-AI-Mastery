#!/usr/bin/env python3
"""
Script to enhance business edition with specific business examples and scenarios
"""

import re

# Read the adapted workbook
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Additional business-specific replacements for context
business_enhancements = [
    # Fix awkward replacements
    ('reviewple', 'example'),
    ('working', 'studying'),  # Some contexts need this back
    
    # Specific business scenarios
    ('book report', 'market analysis'),
    ('science fair project', 'business proposal'),
    ('history essay', 'strategic report'),
    ('math problem', 'financial calculation'),
    ('vocabulary list', 'industry terminology'),
    ('reading comprehension', 'document analysis'),
    
    # Business-specific tools and platforms
    ('Google Workplace', 'Google Workspace'),
    ('training program materials', 'curriculum materials'),
    
    # Professional context
    ('peer review', 'colleague feedback'),
    ('group work', 'team collaboration'),
    ('presentation skills', 'business communication'),
    
    # Assessment context
    ('standardized testing', 'performance reviews'),
    ('report card', 'performance evaluation'),
    
    # Specific K-12 references that need business equivalents
    ('elementary', 'entry-level'),
    ('middle organization', 'mid-size company'),
    ('high organization', 'enterprise'),
    
    # Fix password reference
    ('PromptedBUS2025', 'PromptedBUS2025'),  # Keep this consistent
    
    # Navigation items that need business framing
    ('Workplace Readiness', 'Team Readiness'),
    ('Manager Tools', 'Leadership Tools'),
    
    # Specific business applications
    ('help with work tasks', 'assist with projects'),
    ('complete work tasks', 'complete assignments'),
    ('work tasks help', 'project assistance'),
]

# Apply enhancements
for old, new in business_enhancements:
    content = content.replace(old, new)

# Fix specific problematic phrases with regex
content = re.sub(r'employees can access', 'team members can access', content)
content = re.sub(r'Direct employees to', 'Direct team members to', content)

# Write enhanced version
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Business enhancements applied!")
print("📊 Added business-specific scenarios and context")
print("🔧 Fixed awkward automated replacements")
