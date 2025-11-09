#!/usr/bin/env python3
"""
Transform business workbook from manager-led to employee self-directed learning
AND fix all navigation/accessibility issues
"""

import re

# Read the workbook
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'r') as f:
    content = f.read()

print("🔧 Starting transformation...")

# ============================================
# PHASE 1: Fix Navigation IDs
# ============================================
print("\n📋 Phase 1: Fixing navigation IDs...")

# Fix navigation to match actual section IDs
navigation_fixes = [
    # Current nav points to wrong IDs, fix them
    ('showSection(\'subject-guides\')', 'showSection(\'subjects\')'),
    ('showSection(\'8-week\')', 'showSection(\'implementation\')'),
    ('showSection(\'professional-development\')', 'showSection(\'worksheets\')'),
    ('showSection(\'training-sessions\')', 'showSection(\'training sessions\')'),  # Note the space!
]

for old, new in navigation_fixes:
    if old in content:
        content = content.replace(old, new)
        print(f"  ✅ Fixed: {old} → {new}")

# ============================================
# PHASE 2: Reframe Manager-Led Language
# ============================================
print("\n🔄 Phase 2: Reframing manager-led to employee self-directed...")

# Global language transformations
language_changes = [
    # Manager → Employee focus
    ("Manager's Team Readiness Checklist", "My Workplace Readiness Self-Check"),
    ("Team Implementation Readiness Assessment", "My Workplace Readiness Assessment"),
    ("Manager Planning Tool", "Personal AI Integration Planner"),
    
    # Training → Learning
    ("Training Session 1", "Learning Module 1"),
    ("Training Session 2", "Learning Module 2"),
    ("Training Session 3", "Learning Module 3"),
    ("Ethics Training Session", "Ethics Learning Module"),
    
    # Facilitation → Self-directed
    ("Deliver this session", "Complete this module"),
    ("Facilitate this training", "Work through this content"),
    ("Implement this with your team", "Apply this in your work"),
    ("Team training", "Self-paced learning"),
    
    # Manager actions → Employee actions
    ("Managers implement", "You can apply"),
    ("Manager facilitates", "You complete"),
    ("Team completes", "You complete"),
    ("Your team will", "You will"),
    
    # Quick Start reframe
    ("3-Day Implementation for Managers", "3-Day Quick Start for Employees"),
    ("Day 1: Setup (Manager)", "Day 1: Getting Started"),
    ("Day 2: Training (Manager delivers)", "Day 2: Learning the Framework"),
    ("Day 3: Practice (Manager monitors)", "Day 3: Practicing Your Skills"),
]

for old, new in language_changes:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"  ✅ Changed ({count}x): '{old}' → '{new}'")

# ============================================
# PHASE 3: Update Section Headers
# ============================================
print("\n📝 Phase 3: Updating section headers...")

# Update major section titles
section_header_changes = [
    # Implementation Guides section
    (r'<h2[^>]*>📋 Implementation Guides</h2>', '<h2 style="color: #2c5f2d; margin-bottom: 1.5rem;">📚 Self-Paced Learning Modules</h2>'),
    (r'<h2[^>]*>Training Session Plans</h2>', '<h2>Self-Paced Learning Modules</h2>'),
    
    # Professional Development section
    (r'<h2[^>]*>🛠️ Professional Development Tools</h2>', '<h2 style="color: #2c5f2d; margin-bottom: 1.5rem;">📊 Personal Progress Tracking Tools</h2>'),
]

for pattern, replacement in section_header_changes:
    content = re.sub(pattern, replacement, content)
    print(f"  ✅ Updated section header")

# ============================================
# PHASE 4: Update Instructions for Self-Paced
# ============================================
print("\n💡 Phase 4: Updating instructions...")

# Update the Implementation Guides instruction box
old_impl_instruction = '''<div style="background: #e3f2fd; border-left: 4px solid #2196f3; padding: 1.5rem; margin-bottom: 2rem; border-radius: 8px;">
        <h3 style="margin-top: 0; color: #1976d2;">
            <span style="font-size: 1.5rem;">ℹ️</span> Implementation Guides - Quick Guide
        </h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <strong style="color: #1976d2;">👥 WHO:</strong>
                <p style="margin: 0.5rem 0 0 0;">Managers, trainers, L&D professionals delivering AI literacy training</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">🎯 PURPOSE:</strong>
                <p style="margin: 0.5rem 0 0 0;">Ready-to-use training session plans with scripts and activities</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">⏱️ TIME:</strong>
                <p style="margin: 0.5rem 0 0 0;">45-60 minutes per session</p>
            </div>
        </div>
        
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #90caf9;">
            <strong style="color: #1976d2;">📋 HOW TO USE:</strong>
            <ol style="margin: 0.5rem 0 0 1.5rem;">
                <li>Select the training session topic</li>
                <li>Review the session plan and materials</li>
                <li>Deliver training using provided scripts and activities</li>
                <li>Customize examples for your industry/team</li>
            </ol>
        </div>
    </div>'''

new_impl_instruction = '''<div style="background: #e3f2fd; border-left: 4px solid #2196f3; padding: 1.5rem; margin-bottom: 2rem; border-radius: 8px;">
        <h3 style="margin-top: 0; color: #1976d2;">
            <span style="font-size: 1.5rem;">ℹ️</span> Self-Paced Learning Modules - Quick Guide
        </h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <strong style="color: #1976d2;">👥 WHO:</strong>
                <p style="margin: 0.5rem 0 0 0;">Individual employees learning AI literacy at their own pace</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">🎯 PURPOSE:</strong>
                <p style="margin: 0.5rem 0 0 0;">Structured learning modules you complete independently to build AI skills</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">⏱️ TIME:</strong>
                <p style="margin: 0.5rem 0 0 0;">30-45 minutes per module (complete at your own pace)</p>
            </div>
        </div>
        
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #90caf9;">
            <strong style="color: #1976d2;">📋 HOW TO USE:</strong>
            <ol style="margin: 0.5rem 0 0 1.5rem;">
                <li>Select a learning module that matches your current skill level</li>
                <li>Work through the content at your own pace</li>
                <li>Complete the practice activities independently</li>
                <li>Apply what you learned to your actual work</li>
                <li>Return to review modules anytime you need a refresher</li>
            </ol>
            <p style="margin-top: 0.5rem; font-style: italic; color: #666;">Tip: Complete one module per week for steady progress.</p>
        </div>
    </div>'''

content = content.replace(old_impl_instruction, new_impl_instruction)
print("  ✅ Updated Implementation Guides instruction box")

# ============================================
# PHASE 5: Fix Specific Content Issues
# ============================================
print("\n🔧 Phase 5: Fixing specific content...")

# Update Quick Start Guide content
content = content.replace(
    "This 3-day implementation plan helps managers introduce AI literacy training to their teams quickly and effectively.",
    "This 3-day quick start helps you begin your AI literacy journey immediately, even if you're completely new to AI."
)

content = content.replace(
    "Download the comprehensive guide for managers",
    "Download your personal quick start guide"
)

print("  ✅ Updated Quick Start Guide content")

# Write back
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'w') as f:
    f.write(content)

print("\n✅ TRANSFORMATION COMPLETE!")
print("\nSummary:")
print("  - Fixed navigation IDs to match section IDs")
print("  - Reframed manager-led to employee self-directed")
print("  - Updated all training/facilitation language")
print("  - Changed instruction boxes for self-paced learning")
print("  - Updated section headers and content")
print("\n🎉 Workbook is now self-paced employee-focused!")
