#!/usr/bin/env python3
"""
Script to adapt Prompted AI Mastery Platform from K-12 (EDU) to Business (BUS) edition
Systematically replaces educational terms with business equivalents
"""

import re

# Read the K-12 workbook
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define replacement mappings (case-sensitive where needed)
replacements = [
    # Title and branding
    ('Prompted: AI Mastery Platform', 'Prompted: AI Mastery Platform - Business Edition'),
    ('Site Development Contributors Access', 'Business Platform Access'),
    ('PromptedAI2025', 'PromptedBUS2025'),
    
    # Core audience terms
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
    
    # Educational settings
    ('classroom', 'workplace'),
    ('Classroom', 'Workplace'),
    ('classrooms', 'workplaces'),
    ('Classrooms', 'Workplaces'),
    ('school', 'organization'),
    ('School', 'Organization'),
    ('schools', 'organizations'),
    ('Schools', 'Organizations'),
    ('K-12', 'corporate'),
    ('grade', 'level'),
    ('Grade', 'Level'),
    
    # Academic terms
    ('homework', 'work tasks'),
    ('Homework', 'Work Tasks'),
    ('assignment', 'project'),
    ('Assignment', 'Project'),
    ('assignments', 'projects'),
    ('Assignments', 'Projects'),
    ('lesson', 'training session'),
    ('Lesson', 'Training Session'),
    ('lessons', 'training sessions'),
    ('Lessons', 'Training Sessions'),
    ('curriculum', 'training program'),
    ('Curriculum', 'Training Program'),
    ('study', 'work'),
    ('Study', 'Work'),
    ('studying', 'working'),
    ('Studying', 'Working'),
    
    # Assessment terms
    ('test', 'evaluation'),
    ('Test', 'Evaluation'),
    ('tests', 'evaluations'),
    ('Tests', 'Evaluations'),
    ('quiz', 'assessment'),
    ('Quiz', 'Assessment'),
    ('quizzes', 'assessments'),
    ('Quizzes', 'Assessments'),
    ('exam', 'review'),
    ('Exam', 'Review'),
    ('exams', 'reviews'),
    ('Exams', 'Reviews'),
    ('grade', 'performance'),
    ('Grade', 'Performance'),
    ('grades', 'performance metrics'),
    ('Grades', 'Performance Metrics'),
    
    # Learning terms
    ('learning', 'professional development'),
    ('Learning', 'Professional Development'),
    ('learner', 'professional'),
    ('Learner', 'Professional'),
    ('learners', 'professionals'),
    ('Learners', 'Professionals'),
    
    # Specific contexts
    ('research paper', 'business report'),
    ('Research paper', 'Business report'),
    ('Research Paper', 'Business Report'),
    ('essay', 'document'),
    ('Essay', 'Document'),
    ('essays', 'documents'),
    ('Essays', 'Documents'),
    ('book report', 'analysis'),
    ('Book report', 'Analysis'),
    ('Book Report', 'Analysis'),
    ('class project', 'team deliverable'),
    ('Class project', 'Team deliverable'),
    ('Class Project', 'Team Deliverable'),
    ('study guide', 'reference material'),
    ('Study guide', 'Reference material'),
    ('Study Guide', 'Reference Material'),
    
    # Roles
    ('parent', 'supervisor'),
    ('Parent', 'Supervisor'),
    ('parents', 'supervisors'),
    ('Parents', 'Supervisors'),
    ('principal', 'executive'),
    ('Principal', 'Executive'),
    ('administrator', 'manager'),
    ('Administrator', 'Manager'),
    
    # Specific platform terms
    ('Advisory Board', 'Beta Program'),
    ('educational', 'business'),
    ('Educational', 'Business'),
    ('education', 'training'),
    ('Education', 'Training'),
    ('academic', 'professional'),
    ('Academic', 'Professional'),
    
    # Time periods
    ('semester', 'quarter'),
    ('Semester', 'Quarter'),
    ('school year', 'fiscal year'),
    ('School year', 'Fiscal year'),
    ('School Year', 'Fiscal Year'),
]

# Apply replacements
for old, new in replacements:
    content = content.replace(old, new)

# Special case: Fix "Educator's" possessive
content = content.replace("Business Leader's Workplace Readiness Checklist", "Manager's Workplace Readiness Checklist")

# Write the business version
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Basic adaptation complete!")
print("📝 Replaced educational terms with business equivalents")
print("🎯 Next: Manual review and enhancement of specific sections")
