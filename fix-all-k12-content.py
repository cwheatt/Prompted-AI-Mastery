#!/usr/bin/env python3
"""
Comprehensive script to remove ALL K-12 content from business workbook
"""

import re

# Read the workbook
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'r') as f:
    content = f.read()

print("🔍 Starting comprehensive K-12 content removal...")

# 1. Replace K-12 subjects with business departments in Subject Guides section
print("\n1️⃣ Replacing K-12 subjects with business departments...")

# Replace subject tabs
content = re.sub(
    r'<button class="tab active" data-subject="english">English/Language Arts</button>',
    '<button class="tab active" data-subject="marketing">Marketing</button>',
    content
)
content = re.sub(
    r'<button class="tab" data-subject="math">Mathematics</button>',
    '<button class="tab" data-subject="hr">Human Resources</button>',
    content
)
content = re.sub(
    r'<button class="tab" data-subject="science">Science</button>',
    '<button class="tab" data-subject="operations">Operations</button>',
    content
)
content = re.sub(
    r'<button class="tab" data-subject="history">Social Studies/History</button>',
    '<button class="tab" data-subject="sales">Sales</button>',
    content
)

# Replace subject content sections
# English → Marketing
content = re.sub(
    r'<div class="subject-content active" data-subject="english">.*?</div>\s*<!-- End English -->',
    '''<div class="subject-content active" data-subject="marketing">
                        <h3>Marketing AI Integration</h3>
                        
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 1.5rem 0;">
                            <div style="background: var(--card-bg); padding: 1.5rem; border-radius: 12px; border-left: 4px solid var(--primary-color);">
                                <h4 style="color: var(--primary-color); margin-bottom: 1rem;">📊 Content Creation</h4>
                                <ul style="margin: 0; padding-left: 1.5rem;">
                                    <li>Use AI to generate blog post outlines</li>
                                    <li>Get feedback on email campaign copy</li>
                                    <li>Employee develops final messaging</li>
                                    <li>AI helps identify target audience insights</li>
                                </ul>
                            </div>
                            
                            <div style="background: var(--card-bg); padding: 1.5rem; border-radius: 12px; border-left: 4px solid var(--secondary-color);">
                                <h4 style="color: var(--secondary-color); margin-bottom: 1rem;">✍️ Campaign Strategy</h4>
                                <ul style="margin: 0; padding-left: 1.5rem;">
                                    <li>AI for market research and trend analysis</li>
                                    <li>Get feedback on campaign positioning</li>
                                    <li>Employee maintains brand voice</li>
                                    <li>AI suggests A/B testing variations</li>
                                </ul>
                            </div>
                        </div>
                        
                        <div style="background: var(--success-bg); padding: 1.5rem; border-radius: 12px; margin: 1.5rem 0;">
                            <h4 style="color: var(--success-color); margin-bottom: 1rem;">Sample Prompt Progression:</h4>
                            <ol style="margin: 0; padding-left: 1.5rem;">
                                <li>"What are effective email subject lines for B2B software launches?"</li>
                                <li>"How can I improve this subject line: 'New Product Available'?"</li>
                                <li>"I want to emphasize time-saving benefits. What subject line variations might work better?"</li>
                            </ol>
                        </div>
                    </div>
                    <!-- End Marketing -->''',
    content,
    flags=re.DOTALL
)

# Math → HR
content = re.sub(
    r'<div class="subject-content" data-subject="math">.*?</div>\s*<!-- End Math -->',
    '''<div class="subject-content" data-subject="hr">
                        <h3>Human Resources AI Integration</h3>
                        
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 1.5rem 0;">
                            <div style="background: var(--card-bg); padding: 1.5rem; border-radius: 12px; border-left: 4px solid var(--primary-color);">
                                <h4 style="color: var(--primary-color); margin-bottom: 1rem;">👥 Recruitment</h4>
                                <ul style="margin: 0; padding-left: 1.5rem;">
                                    <li>Use AI to draft job descriptions</li>
                                    <li>Get feedback on interview questions</li>
                                    <li>Employee ensures compliance and fairness</li>
                                    <li>AI helps identify skill requirements</li>
                                </ul>
                            </div>
                            
                            <div style="background: var(--card-bg); padding: 1.5rem; border-radius: 12px; border-left: 4px solid var(--secondary-color);">
                                <h4 style="color: var(--secondary-color); margin-bottom: 1rem;">📋 Policy Development</h4>
                                <ul style="margin: 0; padding-left: 1.5rem;">
                                    <li>AI for policy research and benchmarking</li>
                                    <li>Get feedback on policy clarity</li>
                                    <li>Employee maintains legal compliance</li>
                                    <li>AI suggests communication strategies</li>
                                </ul>
                            </div>
                        </div>
                        
                        <div style="background: var(--success-bg); padding: 1.5rem; border-radius: 12px; margin: 1.5rem 0;">
                            <h4 style="color: var(--success-color); margin-bottom: 1rem;">Sample Prompt Progression:</h4>
                            <ol style="margin: 0; padding-left: 1.5rem;">
                                <li>"What are key competencies for a senior data analyst role?"</li>
                                <li>"How can I assess problem-solving skills in an interview?"</li>
                                <li>"I need behavioral interview questions that reveal analytical thinking. What would you suggest?"</li>
                            </ol>
                        </div>
                    </div>
                    <!-- End HR -->''',
    content,
    flags=re.DOTALL
)

# Science → Operations
content = re.sub(
    r'<div class="subject-content" data-subject="science">.*?</div>\s*<!-- End Science -->',
    '''<div class="subject-content" data-subject="operations">
                        <h3>Operations AI Integration</h3>
                        
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 1.5rem 0;">
                            <div style="background: var(--card-bg); padding: 1.5rem; border-radius: 12px; border-left: 4px solid var(--primary-color);">
                                <h4 style="color: var(--primary-color); margin-bottom: 1rem;">⚙️ Process Optimization</h4>
                                <ul style="margin: 0; padding-left: 1.5rem;">
                                    <li>Use AI to analyze workflow bottlenecks</li>
                                    <li>Get feedback on process improvements</li>
                                    <li>Employee validates with real-world data</li>
                                    <li>AI helps identify efficiency opportunities</li>
                                </ul>
                            </div>
                            
                            <div style="background: var(--card-bg); padding: 1.5rem; border-radius: 12px; border-left: 4px solid var(--secondary-color);">
                                <h4 style="color: var(--secondary-color); margin-bottom: 1rem;">📦 Supply Chain</h4>
                                <ul style="margin: 0; padding-left: 1.5rem;">
                                    <li>AI for demand forecasting</li>
                                    <li>Get feedback on inventory strategies</li>
                                    <li>Employee maintains vendor relationships</li>
                                    <li>AI suggests cost optimization</li>
                                </ul>
                            </div>
                        </div>
                        
                        <div style="background: var(--success-bg); padding: 1.5rem; border-radius: 12px; margin: 1.5rem 0;">
                            <h4 style="color: var(--success-color); margin-bottom: 1rem;">Sample Prompt Progression:</h4>
                            <ol style="margin: 0; padding-left: 1.5rem;">
                                <li>"What are common causes of production delays in manufacturing?"</li>
                                <li>"How can I reduce order fulfillment time from 5 days to 3 days?"</li>
                                <li>"I need to optimize our warehouse layout for faster picking. What factors should I consider?"</li>
                            </ol>
                        </div>
                    </div>
                    <!-- End Operations -->''',
    content,
    flags=re.DOTALL
)

# History → Sales
content = re.sub(
    r'<div class="subject-content" data-subject="history">.*?</div>\s*<!-- End History -->',
    '''<div class="subject-content" data-subject="sales">
                        <h3>Sales AI Integration</h3>
                        
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 1.5rem 0;">
                            <div style="background: var(--card-bg); padding: 1.5rem; border-radius: 12px; border-left: 4px solid var(--primary-color);">
                                <h4 style="color: var(--primary-color); margin-bottom: 1rem;">💼 Prospecting</h4>
                                <ul style="margin: 0; padding-left: 1.5rem;">
                                    <li>Use AI to research prospect companies</li>
                                    <li>Get feedback on outreach messaging</li>
                                    <li>Employee builds authentic relationships</li>
                                    <li>AI helps identify decision-makers</li>
                                </ul>
                            </div>
                            
                            <div style="background: var(--card-bg); padding: 1.5rem; border-radius: 12px; border-left: 4px solid var(--secondary-color);">
                                <h4 style="color: var(--secondary-color); margin-bottom: 1rem;">📈 Proposal Development</h4>
                                <ul style="margin: 0; padding-left: 1.5rem;">
                                    <li>AI for competitive analysis</li>
                                    <li>Get feedback on value propositions</li>
                                    <li>Employee customizes for client needs</li>
                                    <li>AI suggests pricing strategies</li>
                                </ul>
                            </div>
                        </div>
                        
                        <div style="background: var(--success-bg); padding: 1.5rem; border-radius: 12px; margin: 1.5rem 0;">
                            <h4 style="color: var(--success-color); margin-bottom: 1rem;">Sample Prompt Progression:</h4>
                            <ol style="margin: 0; padding-left: 1.5rem;">
                                <li>"What are common objections to enterprise software purchases?"</li>
                                <li>"How can I address concerns about implementation time?"</li>
                                <li>"I need to show ROI for a $50K annual subscription. What metrics should I emphasize?"</li>
                            </ol>
                        </div>
                    </div>
                    <!-- End Sales -->''',
    content,
    flags=re.DOTALL
)

# 2. Remove Supervisor Communication section
print("2️⃣ Removing Supervisor Communication section...")
content = re.sub(
    r'<div style="background: var\(--card-bg\); padding: 1\.5rem; border-radius: 12px; margin-top: 1\.5rem;">.*?<h3 style="color: var\(--primary-color\);">📧 Supervisor Communication</h3>.*?</div>',
    '',
    content,
    flags=re.DOTALL
)

# 3. Remove generateSupervisorLetter function
print("3️⃣ Removing supervisor letter generator function...")
content = re.sub(
    r'function generateSupervisorLetter\(\) \{.*?\}',
    '',
    content,
    flags=re.DOTALL
)

# 4. Replace dropdown subject options
print("4️⃣ Replacing dropdown menu subjects...")
content = content.replace(
    '<option>English/Language Arts</option>',
    '<option>Marketing</option>'
)
content = content.replace(
    '<option>Mathematics</option>',
    '<option>Human Resources</option>'
)
content = content.replace(
    '<option>Science</option>',
    '<option>Operations</option>'
)
content = content.replace(
    '<option>History/Social Studies</option>',
    '<option>Sales</option>'
)
content = content.replace(
    '<option>Social Studies</option>',
    '<option>Finance</option>'
)

# 5. Remove any remaining K-12 references
print("5️⃣ Cleaning up remaining K-12 language...")
content = content.replace('studying', 'working')
content = content.replace('What project were you studying on?', 'What project were you working on?')

# Write the fixed content
with open('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html', 'w') as f:
    f.write(content)

print("\n✅ All K-12 content removed successfully!")
print("✅ Business departments added: Marketing, HR, Operations, Sales")
print("✅ Supervisor communication removed")
print("✅ Dropdown menus updated")
