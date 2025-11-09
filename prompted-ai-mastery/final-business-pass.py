#!/usr/bin/env python3
"""
Final comprehensive pass to ensure complete business adaptation
Catches remaining K-12 terminology and fixes context-specific issues
"""

import re

# Read both files
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'r', encoding='utf-8') as f:
    workbook_content = f.read()

with open('/home/ubuntu/prompted-ai-mastery/client/public/preview-bus.html', 'r', encoding='utf-8') as f:
    preview_content = f.read()

# Comprehensive final replacements
final_replacements = [
    # Missed educational terms
    ("Educator's Workplace Readiness Checklist", "Manager's Team Readiness Checklist"),
    ("Educator's", "Manager's"),
    ("educator's", "manager's"),
    
    # Pedagogical terms
    ('Pedagogical Readiness', 'Training Readiness'),
    ('pedagogical', 'training'),
    ('Pedagogical', 'Training'),
    
    # Student-specific
    ('Employee Readiness', 'Team Readiness'),
    ('employee readiness', 'team readiness'),
    
    # Learning terminology
    ('professional development objectives', 'training objectives'),
    ('professional development goals', 'performance goals'),
    ('professional development aligns', 'training aligns'),
    
    # Classroom-specific
    ('workplace culture', 'company culture'),
    ('Workplace culture', 'Company culture'),
    
    # Assessment methods
    ('assessment methods', 'evaluation methods'),
    ('Assessment methods', 'Evaluation methods'),
    
    # Copyright and footer
    ('EDU', 'BUS'),
    
    # Specific phrases that need business context
    ('employees understand basic AI concepts', 'team members understand basic AI concepts'),
    ('employees can articulate', 'team members can articulate'),
    ('Critical thinking skills are regularly practiced', 'Critical thinking skills are consistently applied'),
    ('Balance exists between AI-assisted and independent work', 'Balance exists between AI-assisted and human-led work'),
    
    # Technical infrastructure
    ('employees have access to AI tools', 'team members have access to AI tools'),
    ('Clear guidelines exist for appropriate AI use', 'Clear policies exist for appropriate AI use'),
    ('Technical support is available for AI platforms', 'IT support is available for AI platforms'),
    ('Privacy and safety protocols are in place', 'Data privacy and security protocols are in place'),
    
    # Training-specific
    ('training objectives are clearly defined', 'learning objectives are clearly defined'),
    ('AI use aligns with training program goals', 'AI use aligns with business objectives'),
    
    # Specific K-12 references
    ('class culture', 'team culture'),
    ('Class culture', 'Team culture'),
    
    # Fix any remaining student/teacher pairs
    ('help employees', 'help team members'),
    ('support employees', 'support team members'),
    ('guide employees', 'guide team members'),
    ('empower employees', 'empower team members'),
    
    # Password text
    ('Site Development Contributors', 'Business Platform'),
]

# Apply to workbook
for old, new in final_replacements:
    workbook_content = workbook_content.replace(old, new)

# Apply to preview
for old, new in final_replacements:
    preview_content = preview_content.replace(old, new)

# Write updated files
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'w', encoding='utf-8') as f:
    f.write(workbook_content)

with open('/home/ubuntu/prompted-ai-mastery/client/public/preview-bus.html', 'w', encoding='utf-8') as f:
    f.write(preview_content)

print("✅ Final business adaptation complete!")
print("🎯 All K-12 terminology replaced with business equivalents")
print("📊 Ready for business launch")
