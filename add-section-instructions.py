#!/usr/bin/env python3
"""
Add comprehensive user instructions to every section in the business workbook
"""

# Read the workbook
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'r') as f:
    content = f.read()

# Define instruction boxes for each section
instructions = {
    # Assessment section
    'assessment': '''
    <div style="background: #e3f2fd; border-left: 4px solid #2196f3; padding: 1.5rem; margin-bottom: 2rem; border-radius: 8px;">
        <h3 style="margin-top: 0; color: #1976d2;">
            <span style="font-size: 1.5rem;">ℹ️</span> AI Learning Journey Self-Reflection - Quick Guide
        </h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <strong style="color: #1976d2;">👥 WHO:</strong>
                <p style="margin: 0.5rem 0 0 0;">Individual employees at any level</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">🎯 PURPOSE:</strong>
                <p style="margin: 0.5rem 0 0 0;">Identify your current AI literacy stage and growth opportunities</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">⏱️ TIME:</strong>
                <p style="margin: 0.5rem 0 0 0;">5-10 minutes</p>
            </div>
        </div>
        
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #90caf9;">
            <strong style="color: #1976d2;">📋 HOW TO USE:</strong>
            <ol style="margin: 0.5rem 0 0 1.5rem;">
                <li>Rate each statement honestly (1=Rarely, 5=Consistently)</li>
                <li>Click "Discover Your Learning Stage" to see your profile</li>
                <li>Use results to identify which areas need development</li>
                <li>Revisit monthly to track progress</li>
            </ol>
            <p style="margin-top: 0.5rem; font-style: italic; color: #666;">Note: This is for self-reflection only—no scores are saved or shared.</p>
        </div>
    </div>
''',
    
    # ROI Calculator
    'roi-calculator': '''
    <div style="background: #e3f2fd; border-left: 4px solid #2196f3; padding: 1.5rem; margin-bottom: 2rem; border-radius: 8px;">
        <h3 style="margin-top: 0; color: #1976d2;">
            <span style="font-size: 1.5rem;">ℹ️</span> Business Impact Calculator - Quick Guide
        </h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <strong style="color: #1976d2;">👥 WHO:</strong>
                <p style="margin: 0.5rem 0 0 0;">Managers, L&D leaders, executives making training investment decisions</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">🎯 PURPOSE:</strong>
                <p style="margin: 0.5rem 0 0 0;">Quantify the financial return of AI literacy training for your organization</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">⏱️ TIME:</strong>
                <p style="margin: 0.5rem 0 0 0;">2-3 minutes</p>
            </div>
        </div>
        
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #90caf9;">
            <strong style="color: #1976d2;">📋 HOW TO USE:</strong>
            <ol style="margin: 0.5rem 0 0 1.5rem;">
                <li>Enter number of employees who will receive training</li>
                <li>Input average hourly rate for those employees</li>
                <li>Estimate hours saved per week per employee (conservative: 1-2 hrs, moderate: 3-5 hrs, aggressive: 6+ hrs)</li>
                <li>Click "Calculate ROI" to see annual productivity value and ROI multiple</li>
                <li>Use results to justify training budget and set success metrics</li>
            </ol>
        </div>
    </div>
''',
    
    # Microlearning
    'microlearning': '''
    <div style="background: #e3f2fd; border-left: 4px solid #2196f3; padding: 1.5rem; margin-bottom: 2rem; border-radius: 8px;">
        <h3 style="margin-top: 0; color: #1976d2;">
            <span style="font-size: 1.5rem;">ℹ️</span> Microlearning Modules - Quick Guide
        </h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <strong style="color: #1976d2;">👥 WHO:</strong>
                <p style="margin: 0.5rem 0 0 0;">Busy professionals who need flexible, bite-sized learning</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">🎯 PURPOSE:</strong>
                <p style="margin: 0.5rem 0 0 0;">Master the THINK Framework in 5-10 minute sessions you can complete during coffee breaks</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">⏱️ TIME:</strong>
                <p style="margin: 0.5rem 0 0 0;">5-10 minutes per module (7 modules total = 35-70 minutes)</p>
            </div>
        </div>
        
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #90caf9;">
            <strong style="color: #1976d2;">📋 HOW TO USE:</strong>
            <ol style="margin: 0.5rem 0 0 1.5rem;">
                <li>Start with Module 1 (Introduction to THINK Framework)</li>
                <li>Complete one module per day or at your own pace</li>
                <li>Apply each concept immediately in your daily work</li>
                <li>Review modules as needed for refreshers</li>
            </ol>
        </div>
    </div>
''',
    
    # Learning Paths
    'learning-paths': '''
    <div style="background: #e3f2fd; border-left: 4px solid #2196f3; padding: 1.5rem; margin-bottom: 2rem; border-radius: 8px;">
        <h3 style="margin-top: 0; color: #1976d2;">
            <span style="font-size: 1.5rem;">ℹ️</span> Role-Based Learning Paths - Quick Guide
        </h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <strong style="color: #1976d2;">👥 WHO:</strong>
                <p style="margin: 0.5rem 0 0 0;">Professionals who want training tailored to their specific job function</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">🎯 PURPOSE:</strong>
                <p style="margin: 0.5rem 0 0 0;">Learn AI literacy skills relevant to your role (Marketing, HR, Operations, etc.)</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">⏱️ TIME:</strong>
                <p style="margin: 0.5rem 0 0 0;">2-4 hours per path</p>
            </div>
        </div>
        
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #90caf9;">
            <strong style="color: #1976d2;">📋 HOW TO USE:</strong>
            <ol style="margin: 0.5rem 0 0 1.5rem;">
                <li>Select the path that matches your role</li>
                <li>Follow the customized curriculum with role-specific examples</li>
                <li>Complete the real-world applications exercises</li>
                <li>Apply learned skills to your actual work projects</li>
            </ol>
        </div>
    </div>
''',
    
    # Certification
    'certification': '''
    <div style="background: #e3f2fd; border-left: 4px solid #2196f3; padding: 1.5rem; margin-bottom: 2rem; border-radius: 8px;">
        <h3 style="margin-top: 0; color: #1976d2;">
            <span style="font-size: 1.5rem;">ℹ️</span> Certification Program - Quick Guide
        </h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <strong style="color: #1976d2;">👥 WHO:</strong>
                <p style="margin: 0.5rem 0 0 0;">Professionals who want recognized credentials to demonstrate AI proficiency</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">🎯 PURPOSE:</strong>
                <p style="margin: 0.5rem 0 0 0;">Earn stackable certificates that enhance your resume and LinkedIn profile</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">⏱️ TIME:</strong>
                <p style="margin: 0.5rem 0 0 0;">Foundation (2-3 weeks), Practitioner (4-6 weeks), Master (8-12 weeks)</p>
            </div>
        </div>
        
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #90caf9;">
            <strong style="color: #1976d2;">📋 HOW TO USE:</strong>
            <ol style="margin: 0.5rem 0 0 1.5rem;">
                <li>Review requirements for each certification level</li>
                <li>Complete the required modules, assessments, and tools</li>
                <li>Submit completion evidence (self-paced, no exams)</li>
                <li>Receive digital certificate and LinkedIn badge</li>
                <li>Progress through levels as your skills advance</li>
            </ol>
        </div>
    </div>
''',
    
    # Quick Start Guide
    'quick-start': '''
    <div style="background: #e3f2fd; border-left: 4px solid #2196f3; padding: 1.5rem; margin-bottom: 2rem; border-radius: 8px;">
        <h3 style="margin-top: 0; color: #1976d2;">
            <span style="font-size: 1.5rem;">ℹ️</span> Quick Start Guide - Quick Guide
        </h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <strong style="color: #1976d2;">👥 WHO:</strong>
                <p style="margin: 0.5rem 0 0 0;">Managers implementing AI literacy training for their team</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">🎯 PURPOSE:</strong>
                <p style="margin: 0.5rem 0 0 0;">Launch AI literacy training in just 3 days with a proven framework</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">⏱️ TIME:</strong>
                <p style="margin: 0.5rem 0 0 0;">3 days (Day 1: Setup, Day 2: Training, Day 3: Practice)</p>
            </div>
        </div>
        
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #90caf9;">
            <strong style="color: #1976d2;">📋 HOW TO USE:</strong>
            <ol style="margin: 0.5rem 0 0 1.5rem;">
                <li>Download the PDF guide</li>
                <li>Follow the day-by-day implementation plan</li>
                <li>Use provided talking points and activities</li>
                <li>Monitor team progress using the readiness checklist</li>
            </ol>
        </div>
    </div>
''',
    
    # THINK Framework
    'framework': '''
    <div style="background: #e3f2fd; border-left: 4px solid #2196f3; padding: 1.5rem; margin-bottom: 2rem; border-radius: 8px;">
        <h3 style="margin-top: 0; color: #1976d2;">
            <span style="font-size: 1.5rem;">ℹ️</span> THINK Framework - Quick Guide
        </h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <strong style="color: #1976d2;">👥 WHO:</strong>
                <p style="margin: 0.5rem 0 0 0;">Anyone using AI tools in their work</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">🎯 PURPOSE:</strong>
                <p style="margin: 0.5rem 0 0 0;">Apply a systematic approach to AI integration that maintains critical thinking</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">⏱️ TIME:</strong>
                <p style="margin: 0.5rem 0 0 0;">15-20 minutes to learn, ongoing application</p>
            </div>
        </div>
        
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #90caf9;">
            <strong style="color: #1976d2;">📋 HOW TO USE:</strong>
            <ol style="margin: 0.5rem 0 0 1.5rem;">
                <li>Learn each letter: Target, Harness, Inquire, Navigate, Keep</li>
                <li>Use the Manager Planning Tool before assigning AI-assisted work</li>
                <li>Apply the framework to every AI interaction</li>
                <li>Reference quick cards for daily reminders</li>
            </ol>
        </div>
    </div>
'''
}

# Insert instructions after each section header
# Assessment section
content = content.replace(
    '<div id="assessment" class="section active">',
    '<div id="assessment" class="section active">\n' + instructions['assessment']
)

# ROI Calculator
content = content.replace(
    '<div id="business-calculator-section" class="section" style="display: none;">',
    '<div id="business-calculator-section" class="section" style="display: none;">\n' + instructions['roi-calculator']
)

# Microlearning
content = content.replace(
    '<div id="microlearning-section" class="section" style="display: none;">',
    '<div id="microlearning-section" class="section" style="display: none;">\n' + instructions['microlearning']
)

# Learning Paths
content = content.replace(
    '<div id="learning-paths-section" class="section" style="display: none;">',
    '<div id="learning-paths-section" class="section" style="display: none;">\n' + instructions['learning-paths']
)

# Certification
content = content.replace(
    '<div id="certification-section" class="section" style="display: none;">',
    '<div id="certification-section" class="section" style="display: none;">\n' + instructions['certification']
)

# Quick Start
content = content.replace(
    '<div id="quick-start" class="section" style="display: none;">',
    '<div id="quick-start" class="section" style="display: none;">\n' + instructions['quick-start']
)

# THINK Framework
content = content.replace(
    '<div id="framework" class="section">',
    '<div id="framework" class="section">\n' + instructions['framework']
)

# Write back
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'w') as f:
    f.write(content)

print("✅ Instructions added to 7 sections")
print("   - Assessment")
print("   - ROI Calculator")
print("   - Microlearning")
print("   - Learning Paths")
print("   - Certification")
print("   - Quick Start Guide")
print("   - THINK Framework")
