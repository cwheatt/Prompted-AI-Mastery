#!/usr/bin/env python3
"""
Add instructions to remaining sections (worksheets, implementation, ethics, etc.)
"""

# Read the workbook
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'r') as f:
    content = f.read()

# Define instruction boxes for remaining sections
instructions = {
    # Building Independence
    'independence': '''
    <div style="background: #e3f2fd; border-left: 4px solid #2196f3; padding: 1.5rem; margin-bottom: 2rem; border-radius: 8px;">
        <h3 style="margin-top: 0; color: #1976d2;">
            <span style="font-size: 1.5rem;">ℹ️</span> Building Independence - Quick Guide
        </h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <strong style="color: #1976d2;">👥 WHO:</strong>
                <p style="margin: 0.5rem 0 0 0;">Managers assessing employee AI literacy, employees self-checking understanding</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">🎯 PURPOSE:</strong>
                <p style="margin: 0.5rem 0 0 0;">Ensure employees maintain ownership of their work when using AI</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">⏱️ TIME:</strong>
                <p style="margin: 0.5rem 0 0 0;">5 minutes per check</p>
            </div>
        </div>
        
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #90caf9;">
            <strong style="color: #1976d2;">📋 HOW TO USE:</strong>
            <ol style="margin: 0.5rem 0 0 1.5rem;">
                <li>Review the 7 ownership indicators</li>
                <li>Check boxes for demonstrated skills</li>
                <li>Identify gaps where additional support is needed</li>
                <li>Use as a coaching tool, not a grading system</li>
            </ol>
            <p style="margin-top: 0.5rem; font-style: italic; color: #666;">Note: This is for development, not evaluation.</p>
        </div>
    </div>
''',
    
    # Implementation Guides (Training Sessions)
    'training sessions': '''
    <div style="background: #e3f2fd; border-left: 4px solid #2196f3; padding: 1.5rem; margin-bottom: 2rem; border-radius: 8px;">
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
    </div>
''',
    
    # AI Ethics
    'ethics': '''
    <div style="background: #e3f2fd; border-left: 4px solid #2196f3; padding: 1.5rem; margin-bottom: 2rem; border-radius: 8px;">
        <h3 style="margin-top: 0; color: #1976d2;">
            <span style="font-size: 1.5rem;">ℹ️</span> AI Ethics - Quick Guide
        </h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <strong style="color: #1976d2;">👥 WHO:</strong>
                <p style="margin: 0.5rem 0 0 0;">All employees, especially those in decision-making roles</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">🎯 PURPOSE:</strong>
                <p style="margin: 0.5rem 0 0 0;">Understand and apply ethical AI principles in your work</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">⏱️ TIME:</strong>
                <p style="margin: 0.5rem 0 0 0;">30-45 minutes</p>
            </div>
        </div>
        
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #90caf9;">
            <strong style="color: #1976d2;">📋 HOW TO USE:</strong>
            <ol style="margin: 0.5rem 0 0 1.5rem;">
                <li>Explore each ethics topic (Bias, Privacy, Integrity, Impact)</li>
                <li>Review real-world scenarios</li>
                <li>Apply ethics checklist to your AI use</li>
                <li>Discuss ethical dilemmas with your team</li>
            </ol>
        </div>
    </div>
''',
    
    # Activities
    'activities': '''
    <div style="background: #e3f2fd; border-left: 4px solid #2196f3; padding: 1.5rem; margin-bottom: 2rem; border-radius: 8px;">
        <h3 style="margin-top: 0; color: #1976d2;">
            <span style="font-size: 1.5rem;">ℹ️</span> Activities & Worksheets - Quick Guide
        </h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <strong style="color: #1976d2;">👥 WHO:</strong>
                <p style="margin: 0.5rem 0 0 0;">Employees developing practical AI skills</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">🎯 PURPOSE:</strong>
                <p style="margin: 0.5rem 0 0 0;">Hands-on practice with AI tools and critical thinking exercises</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">⏱️ TIME:</strong>
                <p style="margin: 0.5rem 0 0 0;">10-20 minutes per activity</p>
            </div>
        </div>
        
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #90caf9;">
            <strong style="color: #1976d2;">📋 HOW TO USE:</strong>
            <ol style="margin: 0.5rem 0 0 1.5rem;">
                <li>Choose an activity based on your skill level</li>
                <li>Complete the exercise independently</li>
                <li>Compare your results with provided examples</li>
                <li>Repeat activities to build muscle memory</li>
            </ol>
            <p style="margin-top: 0.5rem; font-style: italic; color: #666;">Tip: Practice makes perfect—repeat these weekly for best results.</p>
        </div>
    </div>
''',
    
    # Subject Guides
    'subject-guides': '''
    <div style="background: #e3f2fd; border-left: 4px solid #2196f3; padding: 1.5rem; margin-bottom: 2rem; border-radius: 8px;">
        <h3 style="margin-top: 0; color: #1976d2;">
            <span style="font-size: 1.5rem;">ℹ️</span> Subject Guides - Quick Guide
        </h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <strong style="color: #1976d2;">👥 WHO:</strong>
                <p style="margin: 0.5rem 0 0 0;">Professionals in specific industries or functions</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">🎯 PURPOSE:</strong>
                <p style="margin: 0.5rem 0 0 0;">See how AI literacy applies to your specific field</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">⏱️ TIME:</strong>
                <p style="margin: 0.5rem 0 0 0;">15-20 minutes per guide</p>
            </div>
        </div>
        
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #90caf9;">
            <strong style="color: #1976d2;">📋 HOW TO USE:</strong>
            <ol style="margin: 0.5rem 0 0 1.5rem;">
                <li>Select your industry/function</li>
                <li>Review industry-specific AI use cases</li>
                <li>Apply examples to your actual work</li>
                <li>Adapt frameworks for your context</li>
            </ol>
        </div>
    </div>
''',
    
    # 8-Week Plan
    '8-week': '''
    <div style="background: #e3f2fd; border-left: 4px solid #2196f3; padding: 1.5rem; margin-bottom: 2rem; border-radius: 8px;">
        <h3 style="margin-top: 0; color: #1976d2;">
            <span style="font-size: 1.5rem;">ℹ️</span> 8-Week Implementation Plan - Quick Guide
        </h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <strong style="color: #1976d2;">👥 WHO:</strong>
                <p style="margin: 0.5rem 0 0 0;">Managers rolling out AI literacy training organization-wide</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">🎯 PURPOSE:</strong>
                <p style="margin: 0.5rem 0 0 0;">Structured timeline for comprehensive AI literacy program</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">⏱️ TIME:</strong>
                <p style="margin: 0.5rem 0 0 0;">8 weeks (progressive implementation)</p>
            </div>
        </div>
        
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #90caf9;">
            <strong style="color: #1976d2;">📋 HOW TO USE:</strong>
            <ol style="margin: 0.5rem 0 0 1.5rem;">
                <li>Review the full 8-week plan</li>
                <li>Customize timeline for your organization</li>
                <li>Follow week-by-week activities and milestones</li>
                <li>Track progress using provided checkpoints</li>
            </ol>
        </div>
    </div>
''',
    
    # Professional Development Tools
    'professional-development': '''
    <div style="background: #e3f2fd; border-left: 4px solid #2196f3; padding: 1.5rem; margin-bottom: 2rem; border-radius: 8px;">
        <h3 style="margin-top: 0; color: #1976d2;">
            <span style="font-size: 1.5rem;">ℹ️</span> Professional Development Tools - Quick Guide
        </h3>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div>
                <strong style="color: #1976d2;">👥 WHO:</strong>
                <p style="margin: 0.5rem 0 0 0;">Individual employees tracking their AI learning journey</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">🎯 PURPOSE:</strong>
                <p style="margin: 0.5rem 0 0 0;">Document AI usage, practice prompts, detect errors, track progress</p>
            </div>
            
            <div>
                <strong style="color: #1976d2;">⏱️ TIME:</strong>
                <p style="margin: 0.5rem 0 0 0;">5-10 minutes per worksheet</p>
            </div>
        </div>
        
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #90caf9;">
            <strong style="color: #1976d2;">📋 HOW TO USE:</strong>
            <ol style="margin: 0.5rem 0 0 1.5rem;">
                <li>Select the appropriate worksheet (Interaction Log, Prompt Practice, Error Detection, Weekly Check)</li>
                <li>Complete regularly (daily or weekly)</li>
                <li>Review patterns in your AI usage</li>
                <li>Identify areas for improvement</li>
                <li>Share insights with manager during check-ins</li>
            </ol>
            <p style="margin-top: 0.5rem; font-style: italic; color: #666;">Tip: Consistent use of these tools accelerates your AI literacy development.</p>
        </div>
    </div>
'''
}

# Insert instructions for each section
# Building Independence
content = content.replace(
    '<div id="independence" class="section">',
    '<div id="independence" class="section">\n' + instructions['independence']
)

# Implementation Guides (Training Sessions)
content = content.replace(
    '<div id="training sessions" class="section">',
    '<div id="training sessions" class="section">\n' + instructions['training sessions']
)

# AI Ethics
content = content.replace(
    '<div id="ethics" class="section">',
    '<div id="ethics" class="section">\n' + instructions['ethics']
)

# Activities
content = content.replace(
    '<div id="activities" class="section">',
    '<div id="activities" class="section">\n' + instructions['activities']
)

# Subject Guides
content = content.replace(
    '<div id="subject-guides" class="section">',
    '<div id="subject-guides" class="section">\n' + instructions['subject-guides']
)

# 8-Week Plan
content = content.replace(
    '<div id="8-week" class="section">',
    '<div id="8-week" class="section">\n' + instructions['8-week']
)

# Professional Development Tools
content = content.replace(
    '<div id="professional-development" class="section">',
    '<div id="professional-development" class="section">\n' + instructions['professional-development']
)

# Write back
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'w') as f:
    f.write(content)

print("✅ Instructions added to 7 more sections")
print("   - Building Independence")
print("   - Implementation Guides")
print("   - AI Ethics")
print("   - Activities")
print("   - Subject Guides")
print("   - 8-Week Plan")
print("   - Professional Development Tools")
print("\n🎉 ALL 14 SECTIONS NOW HAVE CLEAR INSTRUCTIONS!")
