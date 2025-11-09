#!/usr/bin/env python3
"""
Fixed script to properly insert all premium features into business workbook
"""

from pathlib import Path
import re

# Read the current business workbook
workbook_path = Path('/home/ubuntu/prompted-ai-mastery/client/public/workbook-bus.html')
with open(workbook_path, 'r', encoding='utf-8') as f:
    html = f.read()

print("🚀 Inserting Premium Features (Fixed Version)...")
print("=" * 60)

# Find the assessment section div closing tag
# We'll insert all new sections right after the assessment section
assessment_pattern = r'(<div id="assessment-section"[^>]*>.*?</div>\s*</div>)'
match = re.search(assessment_pattern, html, re.DOTALL)

if not match:
    print("❌ Could not find assessment section!")
    # Try alternative pattern
    assessment_pattern = r'(<!-- Assessment Section -->.*?</div>\s*<!-- End Assessment Section -->)'
    match = re.search(assessment_pattern, html, re.DOTALL)
    
if not match:
    print("❌ Trying to find by section content marker...")
    # Find by looking for the Quick Start Guide section which comes after
    quick_start_pattern = r'(.*?)(<!-- Quick Start Guide Section -->)'
    match = re.search(quick_start_pattern, html, re.DOTALL)
    if match:
        insertion_point = match.end(1)
        print(f"✓ Found insertion point at position {insertion_point}")
    else:
        print("❌ Could not find insertion point. Exiting.")
        exit(1)
else:
    insertion_point = match.end()
    print(f"✓ Found insertion point after assessment section at position {insertion_point}")

# Prepare all premium feature sections
premium_sections = '''

    <!-- ============================================ -->
    <!-- PREMIUM FEATURE: BUSINESS IMPACT CALCULATOR -->
    <!-- ============================================ -->
    <div id="business-calculator-section" class="section-content" style="display: none;">
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 3rem; border-radius: 12px; color: white; margin-bottom: 2rem;">
            <h2 style="color: white; margin-top: 0;">💰 Business Impact Calculator</h2>
            <p style="font-size: 1.1rem; opacity: 0.95;">Quantify the ROI of AI literacy training for your organization</p>
        </div>

        <div style="background: #f8f9fa; padding: 2rem; border-radius: 8px; margin-bottom: 2rem;">
            <h3 style="color: #2d3748; margin-top: 0;">Calculate Your Productivity Gains</h3>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin-bottom: 2rem;">
                <div>
                    <label style="display: block; font-weight: 600; margin-bottom: 0.5rem; color: #4a5568;">
                        Number of Employees
                    </label>
                    <input type="number" id="calc-employees" value="50" min="1" 
                           style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 1rem;">
                </div>
                
                <div>
                    <label style="display: block; font-weight: 600; margin-bottom: 0.5rem; color: #4a5568;">
                        Average Hourly Rate ($)
                    </label>
                    <input type="number" id="calc-hourly-rate" value="50" min="1" 
                           style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 1rem;">
                </div>
                
                <div>
                    <label style="display: block; font-weight: 600; margin-bottom: 0.5rem; color: #4a5568;">
                        Hours Saved Per Week (per employee)
                    </label>
                    <input type="number" id="calc-hours-saved" value="3" min="0" step="0.5" 
                           style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 6px; font-size: 1rem;">
                </div>
            </div>

            <button onclick="calculateBusinessImpact()" 
                    style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; padding: 1rem 2rem; border-radius: 6px; font-size: 1.1rem; font-weight: 600; cursor: pointer; width: 100%;">
                Calculate ROI
            </button>
        </div>

        <div id="calculator-results" style="display: none;">
            <div style="background: white; border: 3px solid #48bb78; border-radius: 12px; padding: 2rem; margin-bottom: 2rem;">
                <h3 style="color: #2d3748; margin-top: 0; display: flex; align-items: center; gap: 0.5rem;">
                    <span style="font-size: 2rem;">📊</span> Your Estimated Annual Impact
                </h3>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">
                    <div style="text-align: center; padding: 1.5rem; background: #f7fafc; border-radius: 8px;">
                        <div style="font-size: 2.5rem; font-weight: 700; color: #48bb78;" id="result-annual-value">$0</div>
                        <div style="color: #718096; margin-top: 0.5rem; font-weight: 600;">Annual Productivity Value</div>
                    </div>
                    
                    <div style="text-align: center; padding: 1.5rem; background: #f7fafc; border-radius: 8px;">
                        <div style="font-size: 2.5rem; font-weight: 700; color: #667eea;" id="result-hours-saved">0</div>
                        <div style="color: #718096; margin-top: 0.5rem; font-weight: 600;">Total Hours Saved Annually</div>
                    </div>
                    
                    <div style="text-align: center; padding: 1.5rem; background: #f7fafc; border-radius: 8px;">
                        <div style="font-size: 2.5rem; font-weight: 700; color: #f6ad55;" id="result-roi">0x</div>
                        <div style="color: #718096; margin-top: 0.5rem; font-weight: 600;">ROI Multiple</div>
                    </div>
                </div>

                <div style="background: #edf2f7; padding: 1.5rem; border-radius: 8px; margin-top: 1.5rem;">
                    <h4 style="color: #2d3748; margin-top: 0;">💡 What This Means</h4>
                    <p style="color: #4a5568; margin: 0;" id="result-interpretation"></p>
                </div>
            </div>

            <div style="background: #fff5f5; border-left: 4px solid #fc8181; padding: 1.5rem; border-radius: 6px;">
                <p style="margin: 0; color: #742a2a;">
                    <strong>Note:</strong> These calculations are estimates based on industry benchmarks showing 3-5 hours saved per week per employee after AI literacy training. Actual results may vary based on role, industry, and implementation.
                </p>
            </div>
        </div>

        <script>
        function calculateBusinessImpact() {
            const employees = parseFloat(document.getElementById('calc-employees').value) || 0;
            const hourlyRate = parseFloat(document.getElementById('calc-hourly-rate').value) || 0;
            const hoursSaved = parseFloat(document.getElementById('calc-hours-saved').value) || 0;
            
            // Calculate annual impact
            const weeksPerYear = 50; // Account for vacation/holidays
            const annualHoursSaved = employees * hoursSaved * weeksPerYear;
            const annualValue = annualHoursSaved * hourlyRate;
            
            // Estimate training cost (conservative: $500 per employee)
            const trainingCost = employees * 500;
            const roi = annualValue / trainingCost;
            
            // Display results
            document.getElementById('calculator-results').style.display = 'block';
            document.getElementById('result-annual-value').textContent = '$' + annualValue.toLocaleString();
            document.getElementById('result-hours-saved').textContent = annualHoursSaved.toLocaleString();
            document.getElementById('result-roi').textContent = roi.toFixed(1) + 'x';
            
            // Interpretation
            let interpretation = `With ${employees} employees saving ${hoursSaved} hours per week through effective AI usage, your organization could realize approximately <strong>$${annualValue.toLocaleString()}</strong> in annual productivity value. `;
            
            if (roi >= 5) {
                interpretation += `With an estimated ${roi.toFixed(1)}x ROI, this represents an <strong>exceptional investment</strong> in your team's capabilities.`;
            } else if (roi >= 3) {
                interpretation += `With an estimated ${roi.toFixed(1)}x ROI, this represents a <strong>strong return</strong> on your training investment.`;
            } else {
                interpretation += `With an estimated ${roi.toFixed(1)}x ROI, this represents a <strong>positive return</strong> on your training investment.`;
            }
            
            document.getElementById('result-interpretation').innerHTML = interpretation;
            
            // Scroll to results
            document.getElementById('calculator-results').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
        </script>
    </div>

'''

# Insert the premium sections
html = html[:insertion_point] + premium_sections + html[insertion_point:]
print("✓ Inserted Business Impact Calculator")

# Save the file
with open(workbook_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("\n" + "=" * 60)
print("✅ PREMIUM FEATURES INSERTED!")
print("=" * 60)
print("\n📊 Summary:")
print("  ✓ Business Impact Calculator with ROI tool")
print("  ✓ Interactive calculator with real-time results")
print("  ✓ Professional design with gradient headers")
print("\n🎯 Next: Test the calculator in browser")
