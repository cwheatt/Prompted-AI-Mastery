#!/usr/bin/env python3
"""
Script to adapt preview page from K-12 to Business edition
"""

# Read the preview page
with open('/home/ubuntu/prompted-ai-mastery/client/public/preview-bus.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define replacement mappings for preview page
replacements = [
    # Title and branding
    ('Prompted: AI Mastery for K-12 Education', 'Prompted: AI Mastery for Business Professionals'),
    ('K-12', 'Business'),
    
    # Audience terms
    ('students', 'employees'),
    ('Students', 'Employees'),
    ('student', 'employee'),
    ('Student', 'Employee'),
    ('teachers', 'managers'),
    ('Teachers', 'Managers'),
    ('teacher', 'manager'),
    ('Teacher', 'Manager'),
    ('educators', 'business leaders'),
    ('Educators', 'Business Leaders'),
    ('educator', 'business leader'),
    ('Educator', 'Business Leader'),
    
    # Settings
    ('classroom', 'workplace'),
    ('Classroom', 'Workplace'),
    ('classrooms', 'workplaces'),
    ('Classrooms', 'Workplaces'),
    ('school', 'organization'),
    ('School', 'Organization'),
    ('schools', 'organizations'),
    ('Schools', 'Organizations'),
    
    # Academic terms
    ('homework', 'work tasks'),
    ('Homework', 'Work Tasks'),
    ('assignment', 'project'),
    ('Assignment', 'Project'),
    ('assignments', 'projects'),
    ('Assignments', 'Projects'),
    ('lesson', 'training'),
    ('Lesson', 'Training'),
    ('lessons', 'training sessions'),
    ('Lessons', 'Training Sessions'),
    ('curriculum', 'program'),
    ('Curriculum', 'Program'),
    ('study', 'work'),
    ('Study', 'Work'),
    
    # Assessment
    ('test', 'evaluation'),
    ('Test', 'Evaluation'),
    ('quiz', 'assessment'),
    ('Quiz', 'Assessment'),
    ('grade', 'performance'),
    ('Grade', 'Performance'),
    
    # Learning
    ('learning', 'professional development'),
    ('Learning', 'Professional Development'),
    ('learner', 'professional'),
    ('Learner', 'Professional'),
    
    # Specific contexts
    ('research paper', 'business report'),
    ('Research paper', 'Business report'),
    ('essay', 'document'),
    ('Essay', 'Document'),
    ('class project', 'team project'),
    ('Class project', 'Team project'),
    
    # Email and contact
    ('education platform', 'business training platform'),
    ('Education platform', 'Business training platform'),
    ('educational', 'business'),
    ('Educational', 'Business'),
    
    # Platform description
    ('teaching AI literacy', 'building AI literacy'),
    ('Teaching AI literacy', 'Building AI literacy'),
    
    # Specific phrases
    ('young minds', 'professionals'),
    ('next generation', 'workforce'),
    ('future-ready', 'AI-ready'),
]

# Apply replacements
for old, new in replacements:
    content = content.replace(old, new)

# Write business preview
with open('/home/ubuntu/prompted-ai-mastery/client/public/preview-bus.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Business preview page created!")
print("🎯 Adapted for business professional audience")
print("📧 Ready for business marketing")
