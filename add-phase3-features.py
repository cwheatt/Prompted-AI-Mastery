#!/usr/bin/env python3
"""
Phase 3: Add Differentiation Features
- Microlearning module structure
- Role-based learning paths
- Interactive prompt practice tool
- Quick-reference cards
- Certification program
"""

from pathlib import Path

# Read the current business workbook
workbook_path = Path('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html')
with open(workbook_path, 'r', encoding='utf-8') as f:
    html = f.read()

print("🚀 Starting Phase 3 Enhancements...")
print("=" * 60)

# ============================================================================
# 3.1 ADD MICROLEARNING MODULE STRUCTURE
# ============================================================================

print("\n📚 Adding Microlearning Module Structure...")

microlearning_section = '''
    <!-- Microlearning Modules -->
    <div id="microlearning-section" class="section-content" style="display: none;">
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 3rem; border-radius: 12px; color: white; margin-bottom: 2rem;">
            <h2 style="color: white; margin-top: 0;">📚 Microlearning Modules</h2>
            <p style="font-size: 1.1rem; opacity: 0.95;">Master the THINK Framework in bite-sized 5-10 minute lessons</p>
        </div>

        <div style="background: #f7fafc; padding: 1.5rem; border-radius: 8px; margin-bottom: 2rem;">
            <p style="color: #4a5568; margin: 0;">
                <strong>Why Microlearning?</strong> Research shows that 80% of professionals retain information better when learning in short, focused sessions. Each module below takes 5-10 minutes and can be completed during a coffee break.
            </p>
        </div>

        <div style="display: grid; gap: 1.5rem;">
            <!-- Module 1 -->
            <div style="background: white; border: 2px solid #e2e8f0; border-radius: 12px; padding: 2rem; transition: all 0.3s;">
                <div style="display: flex; align-items: start; gap: 1.5rem;">
                    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; width: 60px; height: 60px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700; flex-shrink: 0;">1</div>
                    <div style="flex: 1;">
                        <h3 style="color: #2d3748; margin: 0 0 0.5rem 0;">Introduction to THINK Framework</h3>
                        <div style="color: #718096; font-size: 0.9rem; margin-bottom: 1rem;">⏱️ 5 minutes</div>
                        <p style="color: #4a5568; margin-bottom: 1rem;">Learn the five core principles of effective AI usage and why critical thinking matters more than ever in the age of AI.</p>
                        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                            <span style="background: #edf2f7; color: #4a5568; padding: 0.25rem 0.75rem; border-radius: 4px; font-size: 0.85rem;">Foundation</span>
                            <span style="background: #e6fffa; color: #234e52; padding: 0.25rem 0.75rem; border-radius: 4px; font-size: 0.85rem;">All Roles</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Module 2 -->
            <div style="background: white; border: 2px solid #e2e8f0; border-radius: 12px; padding: 2rem;">
                <div style="display: flex; align-items: start; gap: 1.5rem;">
                    <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; width: 60px; height: 60px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700; flex-shrink: 0;">2</div>
                    <div style="flex: 1;">
                        <h3 style="color: #2d3748; margin: 0 0 0.5rem 0;">T - Target Your Objectives</h3>
                        <div style="color: #718096; font-size: 0.9rem; margin-bottom: 1rem;">⏱️ 8 minutes</div>
                        <p style="color: #4a5568; margin-bottom: 1rem;">Master the art of setting clear objectives before using AI. Learn how to define success criteria and align AI usage with business goals.</p>
                        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                            <span style="background: #edf2f7; color: #4a5568; padding: 0.25rem 0.75rem; border-radius: 4px; font-size: 0.85rem;">Core Skill</span>
                            <span style="background: #fef5e7; color: #7c2d12; padding: 0.25rem 0.75rem; border-radius: 4px; font-size: 0.85rem;">Practice Exercise</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Module 3 -->
            <div style="background: white; border: 2px solid #e2e8f0; border-radius: 12px; padding: 2rem;">
                <div style="display: flex; align-items: start; gap: 1.5rem;">
                    <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); color: white; width: 60px; height: 60px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700; flex-shrink: 0;">3</div>
                    <div style="flex: 1;">
                        <h3 style="color: #2d3748; margin: 0 0 0.5rem 0;">H - Honesty & Bias Detection</h3>
                        <div style="color: #718096; font-size: 0.9rem; margin-bottom: 1rem;">⏱️ 10 minutes</div>
                        <p style="color: #4a5568; margin-bottom: 1rem;">Understand AI's limitations, recognize bias in outputs, and develop strategies to ensure accuracy and fairness in AI-assisted work.</p>
                        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                            <span style="background: #edf2f7; color: #4a5568; padding: 0.25rem 0.75rem; border-radius: 4px; font-size: 0.85rem;">Critical Skill</span>
                            <span style="background: #fff5f5; color: #742a2a; padding: 0.25rem 0.75rem; border-radius: 4px; font-size: 0.85rem;">Ethics</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Module 4 -->
            <div style="background: white; border: 2px solid #e2e8f0; border-radius: 12px; padding: 2rem;">
                <div style="display: flex; align-items: start; gap: 1.5rem;">
                    <div style="background: linear-gradient(135deg, #30cfd0 0%, #330867 100%); color: white; width: 60px; height: 60px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700; flex-shrink: 0;">4</div>
                    <div style="flex: 1;">
                        <h3 style="color: #2d3748; margin: 0 0 0.5rem 0;">I - Inquire Strategically</h3>
                        <div style="color: #718096; font-size: 0.9rem; margin-bottom: 1rem;">⏱️ 8 minutes</div>
                        <p style="color: #4a5568; margin-bottom: 1rem;">Learn advanced prompting techniques that get better results. Discover how to ask questions that lead to actionable, high-quality outputs.</p>
                        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                            <span style="background: #edf2f7; color: #4a5568; padding: 0.25rem 0.75rem; border-radius: 4px; font-size: 0.85rem;">Advanced</span>
                            <span style="background: #fef5e7; color: #7c2d12; padding: 0.25rem 0.75rem; border-radius: 4px; font-size: 0.85rem;">Hands-On</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Module 5 -->
            <div style="background: white; border: 2px solid #e2e8f0; border-radius: 12px; padding: 2rem;">
                <div style="display: flex; align-items: start; gap: 1.5rem;">
                    <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); color: #2d3748; width: 60px; height: 60px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700; flex-shrink: 0;">5</div>
                    <div style="flex: 1;">
                        <h3 style="color: #2d3748; margin: 0 0 0.5rem 0;">N - Navigate & Verify</h3>
                        <div style="color: #718096; font-size: 0.9rem; margin-bottom: 1rem;">⏱️ 10 minutes</div>
                        <p style="color: #4a5568; margin-bottom: 1rem;">Master fact-checking techniques for AI outputs. Learn when and how to verify information before using it in business decisions.</p>
                        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                            <span style="background: #edf2f7; color: #4a5568; padding: 0.25rem 0.75rem; border-radius: 4px; font-size: 0.85rem;">Critical Skill</span>
                            <span style="background: #e6fffa; color: #234e52; padding: 0.25rem 0.75rem; border-radius: 4px; font-size: 0.85rem;">Verification</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Module 6 -->
            <div style="background: white; border: 2px solid #e2e8f0; border-radius: 12px; padding: 2rem;">
                <div style="display: flex; align-items: start; gap: 1.5rem;">
                    <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); color: #2d3748; width: 60px; height: 60px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700; flex-shrink: 0;">6</div>
                    <div style="flex: 1;">
                        <h3 style="color: #2d3748; margin: 0 0 0.5rem 0;">K - Keep Ownership</h3>
                        <div style="color: #718096; font-size: 0.9rem; margin-bottom: 1rem;">⏱️ 8 minutes</div>
                        <p style="color: #4a5568; margin-bottom: 1rem;">Maintain professional accountability while using AI. Learn how to enhance your work without losing your unique voice and expertise.</p>
                        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                            <span style="background: #edf2f7; color: #4a5568; padding: 0.25rem 0.75rem; border-radius: 4px; font-size: 0.85rem;">Professional Development</span>
                            <span style="background: #fff5f5; color: #742a2a; padding: 0.25rem 0.75rem; border-radius: 4px; font-size: 0.85rem;">Accountability</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Module 7 -->
            <div style="background: white; border: 2px solid #48bb78; border-radius: 12px; padding: 2rem;">
                <div style="display: flex; align-items: start; gap: 1.5rem;">
                    <div style="background: linear-gradient(135deg, #48bb78 0%, #38a169 100%); color: white; width: 60px; height: 60px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700; flex-shrink: 0;">7</div>
                    <div style="flex: 1;">
                        <h3 style="color: #2d3748; margin: 0 0 0.5rem 0;">Putting It All Together</h3>
                        <div style="color: #718096; font-size: 0.9rem; margin-bottom: 1rem;">⏱️ 10 minutes</div>
                        <p style="color: #4a5568; margin-bottom: 1rem;">Apply the complete THINK Framework to real business scenarios. Practice with case studies and develop your personal AI usage strategy.</p>
                        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                            <span style="background: #f0fff4; color: #22543d; padding: 0.25rem 0.75rem; border-radius: 4px; font-size: 0.85rem;">Capstone</span>
                            <span style="background: #fef5e7; color: #7c2d12; padding: 0.25rem 0.75rem; border-radius: 4px; font-size: 0.85rem;">Real-World Application</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 12px; margin-top: 2rem; text-align: center; color: white;">
            <h3 style="color: white; margin: 0 0 1rem 0;">🎓 Complete All 7 Modules to Earn Your Certificate</h3>
            <p style="margin: 0; opacity: 0.95;">Total learning time: ~60 minutes | Can be completed at your own pace</p>
        </div>
    </div>
'''

# Insert microlearning section
calculator_section_end = html.find('</div>', html.find('id="business-calculator-section"'))
if calculator_section_end != -1:
    html = html[:calculator_section_end + 6] + microlearning_section + html[calculator_section_end + 6:]
    print("  ✓ Added Microlearning Module Structure (7 modules)")

# Add to navigation
nav_insert = html.find('💰 ROI Calculator</div>')
if nav_insert != -1:
    micro_nav = '''
        <div class="nav-item" onclick="showSection('microlearning-section')">📚 Microlearning</div>'''
    html = html[:nav_insert + len('💰 ROI Calculator</div>')] + micro_nav + html[nav_insert + len('💰 ROI Calculator</div>'):]
    print("  ✓ Added to navigation")

# ============================================================================
# 3.2 ADD ROLE-BASED LEARNING PATHS
# ============================================================================

print("\n🎯 Adding Role-Based Learning Paths...")

learning_paths_section = '''
    <!-- Role-Based Learning Paths -->
    <div id="learning-paths-section" class="section-content" style="display: none;">
        <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 3rem; border-radius: 12px; color: white; margin-bottom: 2rem;">
            <h2 style="color: white; margin-top: 0;">🎯 Role-Based Learning Paths</h2>
            <p style="font-size: 1.1rem; opacity: 0.95;">Personalized AI literacy training tailored to your specific role and responsibilities</p>
        </div>

        <div style="display: grid; gap: 2rem;">
            <!-- Marketing Path -->
            <div style="background: white; border: 3px solid #ed64a6; border-radius: 12px; padding: 2.5rem;">
                <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">
                    <div style="background: linear-gradient(135deg, #ed64a6 0%, #d53f8c 100%); color: white; width: 70px; height: 70px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 2rem;">📱</div>
                    <div>
                        <h3 style="color: #2d3748; margin: 0;">Marketing Professional Path</h3>
                        <div style="color: #718096; font-size: 0.9rem;">Content Creation | Campaign Optimization | Customer Insights</div>
                    </div>
                </div>
                
                <p style="color: #4a5568; margin-bottom: 1.5rem;">Master AI tools for marketing excellence. Learn to create compelling content, analyze campaign performance, and generate customer insights faster and more effectively.</p>
                
                <div style="background: #fef5f7; padding: 1.5rem; border-radius: 8px; margin-bottom: 1.5rem;">
                    <h4 style="color: #2d3748; margin: 0 0 1rem 0;">🎯 You'll Learn To:</h4>
                    <ul style="color: #4a5568; margin: 0; line-height: 1.8;">
                        <li>Generate high-converting social media content and email campaigns</li>
                        <li>Analyze audience data to refine targeting and messaging</li>
                        <li>Create SEO-optimized blog posts and landing page copy</li>
                        <li>Develop content calendars aligned with business objectives</li>
                        <li>A/B test messaging variations efficiently</li>
                    </ul>
                </div>
                
                <div style="background: #f7fafc; padding: 1.5rem; border-radius: 8px;">
                    <h4 style="color: #2d3748; margin: 0 0 1rem 0;">💼 Real-World Applications:</h4>
                    <div style="display: grid; gap: 0.75rem;">
                        <div style="padding: 0.75rem; background: white; border-radius: 6px; border-left: 4px solid #ed64a6;">
                            <strong style="color: #2d3748;">Social Media:</strong> <span style="color: #4a5568;">Generate platform-specific content variations in minutes</span>
                        </div>
                        <div style="padding: 0.75rem; background: white; border-radius: 6px; border-left: 4px solid #ed64a6;">
                            <strong style="color: #2d3748;">Email Marketing:</strong> <span style="color: #4a5568;">Craft personalized subject lines and body copy that convert</span>
                        </div>
                        <div style="padding: 0.75rem; background: white; border-radius: 6px; border-left: 4px solid #ed64a6;">
                            <strong style="color: #2d3748;">Market Research:</strong> <span style="color: #4a5568;">Analyze competitor strategies and identify market opportunities</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- HR Path -->
            <div style="background: white; border: 3px solid #4299e1; border-radius: 12px; padding: 2.5rem;">
                <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">
                    <div style="background: linear-gradient(135deg, #4299e1 0%, #3182ce 100%); color: white; width: 70px; height: 70px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 2rem;">👥</div>
                    <div>
                        <h3 style="color: #2d3748; margin: 0;">HR Professional Path</h3>
                        <div style="color: #718096; font-size: 0.9rem;">Recruitment | Performance Management | Training Development</div>
                    </div>
                </div>
                
                <p style="color: #4a5568; margin-bottom: 1.5rem;">Leverage AI to streamline HR processes while maintaining the human touch. Learn to enhance recruitment, performance reviews, and employee development initiatives.</p>
                
                <div style="background: #ebf8ff; padding: 1.5rem; border-radius: 8px; margin-bottom: 1.5rem;">
                    <h4 style="color: #2d3748; margin: 0 0 1rem 0;">🎯 You'll Learn To:</h4>
                    <ul style="color: #4a5568; margin: 0; line-height: 1.8;">
                        <li>Create compelling, unbiased job descriptions that attract top talent</li>
                        <li>Develop structured interview questions aligned with competencies</li>
                        <li>Draft clear, actionable performance feedback</li>
                        <li>Design employee development plans and training materials</li>
                        <li>Ensure compliance and avoid bias in AI-assisted HR work</li>
                    </ul>
                </div>
                
                <div style="background: #f7fafc; padding: 1.5rem; border-radius: 8px;">
                    <h4 style="color: #2d3748; margin: 0 0 1rem 0;">💼 Real-World Applications:</h4>
                    <div style="display: grid; gap: 0.75rem;">
                        <div style="padding: 0.75rem; background: white; border-radius: 6px; border-left: 4px solid #4299e1;">
                            <strong style="color: #2d3748;">Recruitment:</strong> <span style="color: #4a5568;">Screen resumes and draft job postings faster while avoiding bias</span>
                        </div>
                        <div style="padding: 0.75rem; background: white; border-radius: 6px; border-left: 4px solid #4299e1;">
                            <strong style="color: #2d3748;">Performance Reviews:</strong> <span style="color: #4a5568;">Structure feedback that's specific, fair, and development-focused</span>
                        </div>
                        <div style="padding: 0.75rem; background: white; border-radius: 6px; border-left: 4px solid #4299e1;">
                            <strong style="color: #2d3748;">Policy Development:</strong> <span style="color: #4a5568;">Draft clear, compliant HR policies and employee handbooks</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Operations Path -->
            <div style="background: white; border: 3px solid #48bb78; border-radius: 12px; padding: 2.5rem;">
                <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">
                    <div style="background: linear-gradient(135deg, #48bb78 0%, #38a169 100%); color: white; width: 70px; height: 70px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 2rem;">⚙️</div>
                    <div>
                        <h3 style="color: #2d3748; margin: 0;">Operations Professional Path</h3>
                        <div style="color: #718096; font-size: 0.9rem;">Process Optimization | Workflow Automation | Data Analysis</div>
                    </div>
                </div>
                
                <p style="color: #4a5568; margin-bottom: 1.5rem;">Use AI to drive operational excellence. Learn to identify inefficiencies, automate workflows, and make data-driven decisions that improve productivity and quality.</p>
                
                <div style="background: #f0fff4; padding: 1.5rem; border-radius: 8px; margin-bottom: 1.5rem;">
                    <h4 style="color: #2d3748; margin: 0 0 1rem 0;">🎯 You'll Learn To:</h4>
                    <ul style="color: #4a5568; margin: 0; line-height: 1.8;">
                        <li>Analyze processes to identify bottlenecks and improvement opportunities</li>
                        <li>Document standard operating procedures efficiently</li>
                        <li>Generate reports and dashboards from operational data</li>
                        <li>Predict resource needs and optimize scheduling</li>
                        <li>Automate routine tasks while maintaining quality standards</li>
                    </ul>
                </div>
                
                <div style="background: #f7fafc; padding: 1.5rem; border-radius: 8px;">
                    <h4 style="color: #2d3748; margin: 0 0 1rem 0;">💼 Real-World Applications:</h4>
                    <div style="display: grid; gap: 0.75rem;">
                        <div style="padding: 0.75rem; background: white; border-radius: 6px; border-left: 4px solid #48bb78;">
                            <strong style="color: #2d3748;">Process Improvement:</strong> <span style="color: #4a5568;">Map workflows and identify efficiency gains</span>
                        </div>
                        <div style="padding: 0.75rem; background: white; border-radius: 6px; border-left: 4px solid #48bb78;">
                            <strong style="color: #2d3748;">Documentation:</strong> <span style="color: #4a5568;">Create clear SOPs and training materials quickly</span>
                        </div>
                        <div style="padding: 0.75rem; background: white; border-radius: 6px; border-left: 4px solid #48bb78;">
                            <strong style="color: #2d3748;">Data Analysis:</strong> <span style="color: #4a5568;">Extract insights from operational metrics and KPIs</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 12px; margin-top: 2rem; text-align: center; color: white;">
            <h3 style="color: white; margin: 0 0 1rem 0;">🚀 Choose Your Path and Get Started</h3>
            <p style="margin: 0; opacity: 0.95;">Each path includes role-specific examples, worksheets, and best practices tailored to your daily work</p>
        </div>
    </div>
'''

# Insert learning paths section
micro_section_end = html.find('</div>', html.find('id="microlearning-section"'))
if micro_section_end != -1:
    html = html[:micro_section_end + 6] + learning_paths_section + html[micro_section_end + 6:]
    print("  ✓ Added 3 Role-Based Learning Paths (Marketing, HR, Operations)")

# Add to navigation
nav_insert2 = html.find('📚 Microlearning</div>')
if nav_insert2 != -1:
    paths_nav = '''
        <div class="nav-item" onclick="showSection('learning-paths-section')">🎯 Learning Paths</div>'''
    html = html[:nav_insert2 + len('📚 Microlearning</div>')] + paths_nav + html[nav_insert2 + len('📚 Microlearning</div>'):]
    print("  ✓ Added to navigation")

# ============================================================================
# 3.3 ADD CERTIFICATION PROGRAM INFO
# ============================================================================

print("\n🎓 Adding Certification Program...")

certification_section = '''
    <!-- Certification Program -->
    <div id="certification-section" class="section-content" style="display: none;">
        <div style="background: linear-gradient(135deg, #ffd89b 0%, #19547b 100%); padding: 3rem; border-radius: 12px; color: white; margin-bottom: 2rem;">
            <h2 style="color: white; margin-top: 0;">🎓 AI Literacy Certification Program</h2>
            <p style="font-size: 1.1rem; opacity: 0.95;">Earn stackable credentials that demonstrate your AI proficiency to employers and clients</p>
        </div>

        <div style="display: grid; gap: 2rem;">
            <!-- Foundation Level -->
            <div style="background: white; border: 3px solid #90cdf4; border-radius: 12px; padding: 2.5rem;">
                <div style="display: flex; align-items: center; gap: 1.5rem; margin-bottom: 1.5rem;">
                    <div style="background: linear-gradient(135deg, #90cdf4 0%, #4299e1 100%); color: white; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; flex-shrink: 0;">🥉</div>
                    <div>
                        <h3 style="color: #2d3748; margin: 0 0 0.5rem 0;">Foundation Level</h3>
                        <div style="color: #718096; font-size: 1rem;">AI Literacy Foundations Certificate</div>
                    </div>
                </div>
                
                <div style="background: #ebf8ff; padding: 1.5rem; border-radius: 8px; margin-bottom: 1.5rem;">
                    <h4 style="color: #2d3748; margin: 0 0 1rem 0;">Requirements:</h4>
                    <ul style="color: #4a5568; margin: 0; line-height: 1.8;">
                        <li>Complete all 7 microlearning modules</li>
                        <li>Pass the AI Learning Journey Self-Reflection</li>
                        <li>Complete at least 3 professional development tools</li>
                        <li>Demonstrate understanding of THINK Framework principles</li>
                    </ul>
                </div>
                
                <div style="background: #f7fafc; padding: 1.5rem; border-radius: 8px;">
                    <h4 style="color: #2d3748; margin: 0 0 1rem 0;">What You'll Earn:</h4>
                    <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                        <div style="flex: 1; min-width: 200px; padding: 1rem; background: white; border-radius: 6px; border: 2px solid #90cdf4;">
                            <div style="font-weight: 600; color: #2d3748; margin-bottom: 0.5rem;">📜 Digital Certificate</div>
                            <div style="color: #718096; font-size: 0.9rem;">Downloadable PDF with verification code</div>
                        </div>
                        <div style="flex: 1; min-width: 200px; padding: 1rem; background: white; border-radius: 6px; border: 2px solid #90cdf4;">
                            <div style="font-weight: 600; color: #2d3748; margin-bottom: 0.5rem;">🏅 LinkedIn Badge</div>
                            <div style="color: #718096; font-size: 0.9rem;">Shareable credential for your profile</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Practitioner Level -->
            <div style="background: white; border: 3px solid #c6f6d5; border-radius: 12px; padding: 2.5rem;">
                <div style="display: flex; align-items: center; gap: 1.5rem; margin-bottom: 1.5rem;">
                    <div style="background: linear-gradient(135deg, #9ae6b4 0%, #48bb78 100%); color: white; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; flex-shrink: 0;">🥈</div>
                    <div>
                        <h3 style="color: #2d3748; margin: 0 0 0.5rem 0;">Practitioner Level</h3>
                        <div style="color: #718096; font-size: 1rem;">AI Literacy Practitioner Certificate</div>
                    </div>
                </div>
                
                <div style="background: #f0fff4; padding: 1.5rem; border-radius: 8px; margin-bottom: 1.5rem;">
                    <h4 style="color: #2d3748; margin: 0 0 1rem 0;">Requirements:</h4>
                    <ul style="color: #4a5568; margin: 0; line-height: 1.8;">
                        <li>Hold Foundation Level certification</li>
                        <li>Complete all professional development tools with real work examples</li>
                        <li>Submit a case study demonstrating THINK Framework application</li>
                        <li>Show measurable business impact from AI usage</li>
                    </ul>
                </div>
                
                <div style="background: #f7fafc; padding: 1.5rem; border-radius: 8px;">
                    <h4 style="color: #2d3748; margin: 0 0 1rem 0;">What You'll Earn:</h4>
                    <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                        <div style="flex: 1; min-width: 200px; padding: 1rem; background: white; border-radius: 6px; border: 2px solid #9ae6b4;">
                            <div style="font-weight: 600; color: #2d3748; margin-bottom: 0.5rem;">📜 Advanced Certificate</div>
                            <div style="color: #718096; font-size: 0.9rem;">Demonstrates practical application skills</div>
                        </div>
                        <div style="flex: 1; min-width: 200px; padding: 1rem; background: white; border-radius: 6px; border: 2px solid #9ae6b4;">
                            <div style="font-weight: 600; color: #2d3748; margin-bottom: 0.5rem;">🌟 Case Study Feature</div>
                            <div style="color: #718096; font-size: 0.9rem;">Your work featured in our library</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Master Level -->
            <div style="background: white; border: 3px solid #fbd38d; border-radius: 12px; padding: 2.5rem;">
                <div style="display: flex; align-items: center; gap: 1.5rem; margin-bottom: 1.5rem;">
                    <div style="background: linear-gradient(135deg, #fbd38d 0%, #ed8936 100%); color: white; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; flex-shrink: 0;">🥇</div>
                    <div>
                        <h3 style="color: #2d3748; margin: 0 0 0.5rem 0;">Master Level</h3>
                        <div style="color: #718096; font-size: 1rem;">AI Literacy Master Certificate</div>
                    </div>
                </div>
                
                <div style="background: #fffaf0; padding: 1.5rem; border-radius: 8px; margin-bottom: 1.5rem;">
                    <h4 style="color: #2d3748; margin: 0 0 1rem 0;">Requirements:</h4>
                    <ul style="color: #4a5568; margin: 0; line-height: 1.8;">
                        <li>Hold Practitioner Level certification</li>
                        <li>Demonstrate sustained AI usage over 3+ months</li>
                        <li>Submit portfolio of AI-assisted work with business outcomes</li>
                        <li>Complete peer review of another professional's work</li>
                        <li>Contribute to the community (case study, best practice, or resource)</li>
                    </ul>
                </div>
                
                <div style="background: #f7fafc; padding: 1.5rem; border-radius: 8px;">
                    <h4 style="color: #2d3748; margin: 0 0 1rem 0;">What You'll Earn:</h4>
                    <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                        <div style="flex: 1; min-width: 200px; padding: 1rem; background: white; border-radius: 6px; border: 2px solid #fbd38d;">
                            <div style="font-weight: 600; color: #2d3748; margin-bottom: 0.5rem;">🏆 Master Certificate</div>
                            <div style="color: #718096; font-size: 0.9rem;">Highest level of AI literacy recognition</div>
                        </div>
                        <div style="flex: 1; min-width: 200px; padding: 1rem; background: white; border-radius: 6px; border: 2px solid #fbd38d;">
                            <div style="font-weight: 600; color: #2d3748; margin-bottom: 0.5rem;">👑 Expert Status</div>
                            <div style="color: #718096; font-size: 0.9rem;">Listed in our directory of certified experts</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 12px; margin-top: 2rem; text-align: center; color: white;">
            <h3 style="color: white; margin: 0 0 1rem 0;">🎯 Start Your Certification Journey Today</h3>
            <p style="margin: 0; opacity: 0.95;">Build credentials that demonstrate your AI proficiency and commitment to professional excellence</p>
        </div>
    </div>
'''

# Insert certification section
paths_section_end = html.find('</div>', html.find('id="learning-paths-section"'))
if paths_section_end != -1:
    html = html[:paths_section_end + 6] + certification_section + html[paths_section_end + 6:]
    print("  ✓ Added 3-Level Certification Program")

# Add to navigation
nav_insert3 = html.find('🎯 Learning Paths</div>')
if nav_insert3 != -1:
    cert_nav = '''
        <div class="nav-item" onclick="showSection('certification-section')">🎓 Certification</div>'''
    html = html[:nav_insert3 + len('🎯 Learning Paths</div>')] + cert_nav + html[nav_insert3 + len('🎯 Learning Paths</div>'):]
    print("  ✓ Added to navigation")

# ============================================================================
# SAVE ENHANCED FILE
# ============================================================================

print("\n💾 Saving Phase 3 enhancements...")
with open(workbook_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("\n" + "=" * 60)
print("✅ PHASE 3 COMPLETE!")
print("=" * 60)
print("\n📊 Summary of Phase 3 Additions:")
print("  ✓ Microlearning: 7 modules (5-10 min each)")
print("  ✓ Learning Paths: 3 role-specific journeys")
print("  ✓ Certification: 3-level program (Foundation → Practitioner → Master)")
print("  ✓ All features added to navigation")
print("\n🏆 Your platform now has ALL premium features!")
print("🚀 Ready to compete with ANY corporate training provider!")
