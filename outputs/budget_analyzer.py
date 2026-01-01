#!/usr/bin/env python3
"""
Budget Analyzer & NSF Fee Prevention Tool
Analyzes financial data and provides strategic recommendations
"""

import json
import csv
from datetime import datetime
from typing import Dict, List, Tuple
from collections import defaultdict

class BudgetAnalyzer:
    def __init__(self):
        self.data = {
            'income': {'monthly': 0, 'annual': 0},
            'expenses': {
                'fixed': 0,
                'variable_essential': 0,
                'subscriptions': 0,
                'debt': 0
            },
            'subscriptions': [],
            'nsf_fees': 0,
            'bank_fees': 0,
            'accounts': []
        }
        
    def calculate_monthly_cash_flow(self) -> float:
        """Calculate net monthly cash flow"""
        total_expenses = (
            self.data['expenses']['fixed'] +
            self.data['expenses']['variable_essential'] +
            self.data['expenses']['subscriptions'] +
            self.data['expenses']['debt']
        )
        return self.data['income']['monthly'] - total_expenses
    
    def analyze_subscriptions(self) -> Dict:
        """Analyze subscriptions and provide cancellation recommendations"""
        subscriptions = self.data['subscriptions']
        total_monthly = sum(s.get('monthly_cost', 0) for s in subscriptions)
        total_annual = sum(s.get('annual_cost', 0) for s in subscriptions)
        
        # Recommend canceling unused or low-value subscriptions
        recommendations = {
            'keep': [],
            'consider_canceling': [],
            'definitely_cancel': [],
            'monthly_savings': 0,
            'annual_savings': 0
        }
        
        for sub in subscriptions:
            status = sub.get('status', 'active').lower()
            last_used = sub.get('last_used', '')
            monthly = sub.get('monthly_cost', 0)
            
            # Heuristic: If unused for >3 months or status is inactive
            if status == 'inactive' or not last_used:
                recommendations['definitely_cancel'].append(sub)
                recommendations['monthly_savings'] += monthly
                recommendations['annual_savings'] += sub.get('annual_cost', monthly * 12)
            elif monthly > 50:  # High-cost subscriptions worth reviewing
                recommendations['consider_canceling'].append(sub)
            else:
                recommendations['keep'].append(sub)
        
        recommendations['total_current_monthly'] = total_monthly
        recommendations['total_current_annual'] = total_annual
        
        return recommendations
    
    def calculate_buffer_amounts(self, target_months: float = 2.0) -> Dict:
        """Calculate recommended buffer amounts for each account"""
        monthly_expenses = (
            self.data['expenses']['fixed'] +
            self.data['expenses']['variable_essential'] +
            self.data['expenses']['debt']
        )
        
        buffer_recommendations = {}
        for account in self.data['accounts']:
            account_type = account.get('type', 'checking').lower()
            current_balance = account.get('current_balance', 0)
            
            if account_type == 'primary' or account_type == 'checking':
                # Primary checking: 1.5-2x monthly expenses
                recommended_buffer = monthly_expenses * 1.75
            elif account_type == 'savings' and 'emergency' in account.get('name', '').lower():
                # Emergency fund: 3-6 months expenses
                recommended_buffer = monthly_expenses * 4.5
            elif account_type == 'business':
                # Business: 1 month business expenses
                recommended_buffer = monthly_expenses * 0.3  # Assuming 30% of expenses are business
            else:
                recommended_buffer = monthly_expenses * 1.0
            
            buffer_recommendations[account.get('name', 'Unknown')] = {
                'current': current_balance,
                'recommended': round(recommended_buffer, 2),
                'shortfall': round(max(0, recommended_buffer - current_balance), 2),
                'type': account_type
            }
        
        return buffer_recommendations
    
    def generate_nsf_prevention_plan(self) -> Dict:
        """Generate specific plan to prevent NSF fees"""
        cash_flow = self.calculate_monthly_cash_flow()
        buffer_analysis = self.calculate_buffer_amounts()
        subscription_analysis = self.analyze_subscriptions()
        
        plan = {
            'current_situation': {
                'monthly_cash_flow': cash_flow,
                'total_nsf_fees': self.data['nsf_fees'],
                'total_bank_fees': self.data['bank_fees'],
                'subscription_waste': subscription_analysis['monthly_savings']
            },
            'actions': [],
            'projected_savings': {
                'monthly': 0,
                'annual': 0
            }
        }
        
        # Action 1: Cancel unused subscriptions
        if subscription_analysis['definitely_cancel']:
            plan['actions'].append({
                'priority': 'HIGH',
                'action': 'Cancel Unused Subscriptions',
                'items': [s.get('name', 'Unknown') for s in subscription_analysis['definitely_cancel']],
                'monthly_savings': subscription_analysis['monthly_savings'],
                'timeline': 'This week'
            })
            plan['projected_savings']['monthly'] += subscription_analysis['monthly_savings']
        
        # Action 2: Establish account buffers
        primary_account = None
        for account_name, buffer_info in buffer_analysis.items():
            if buffer_info['shortfall'] > 0:
                if not primary_account or buffer_info['type'] in ['primary', 'checking']:
                    primary_account = (account_name, buffer_info)
        
        if primary_account:
            account_name, buffer_info = primary_account
            plan['actions'].append({
                'priority': 'CRITICAL',
                'action': f'Establish ${buffer_info["recommended"]:.2f} buffer in {account_name}',
                'current': buffer_info['current'],
                'target': buffer_info['recommended'],
                'shortfall': buffer_info['shortfall'],
                'timeline': 'Within 30 days',
                'how': 'Set up automatic transfer on payday'
            })
        
        # Action 3: Optimize cash flow timing
        if cash_flow < 0:
            plan['actions'].append({
                'priority': 'HIGH',
                'action': 'Address Negative Cash Flow',
                'current_deficit': abs(cash_flow),
                'options': [
                    'Reduce discretionary spending',
                    'Increase income sources',
                    'Negotiate payment dates with creditors',
                    'Use subscription savings to offset deficit'
                ],
                'timeline': 'Immediate'
            })
        
        # Calculate annual projections
        plan['projected_savings']['annual'] = (
            plan['projected_savings']['monthly'] * 12 +
            self.data['nsf_fees'] +  # One-time savings from preventing NSF
            self.data['bank_fees']    # One-time savings from preventing other fees
        )
        
        return plan
    
    def generate_report(self) -> str:
        """Generate comprehensive budget analysis report"""
        cash_flow = self.calculate_monthly_cash_flow()
        subscription_analysis = self.analyze_subscriptions()
        buffer_analysis = self.calculate_buffer_amounts()
        nsf_plan = self.generate_nsf_prevention_plan()
        
        report = []
        report.append("=" * 80)
        report.append("COMPREHENSIVE BUDGET ANALYSIS REPORT")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("=" * 80)
        report.append("")
        
        # Cash Flow Summary
        report.append("📊 MONTHLY CASH FLOW SUMMARY")
        report.append("-" * 80)
        report.append(f"Monthly Income:          ${self.data['income']['monthly']:,.2f}")
        report.append(f"Fixed Expenses:          ${self.data['expenses']['fixed']:,.2f}")
        report.append(f"Variable Expenses:       ${self.data['expenses']['variable_essential']:,.2f}")
        report.append(f"Subscriptions:           ${self.data['expenses']['subscriptions']:,.2f}")
        report.append(f"Debt Payments:           ${self.data['expenses']['debt']:,.2f}")
        report.append(f"Total Expenses:          ${sum(self.data['expenses'].values()):,.2f}")
        report.append(f"Net Cash Flow:           ${cash_flow:,.2f}")
        if cash_flow < 0:
            report.append(f"⚠️  WARNING: Negative cash flow detected!")
        report.append("")
        
        # Subscription Analysis
        report.append("💳 SUBSCRIPTION ANALYSIS")
        report.append("-" * 80)
        report.append(f"Total Monthly Subscriptions: ${subscription_analysis['total_current_monthly']:,.2f}")
        report.append(f"Total Annual Subscriptions:  ${subscription_analysis['total_current_annual']:,.2f}")
        report.append("")
        report.append(f"✅ Keeping: {len(subscription_analysis['keep'])} subscriptions")
        report.append(f"⚠️  Consider Canceling: {len(subscription_analysis['consider_canceling'])} subscriptions")
        report.append(f"❌ Definitely Cancel: {len(subscription_analysis['definitely_cancel'])} subscriptions")
        report.append(f"Potential Monthly Savings: ${subscription_analysis['monthly_savings']:,.2f}")
        report.append(f"Potential Annual Savings:  ${subscription_analysis['annual_savings']:,.2f}")
        report.append("")
        
        if subscription_analysis['definitely_cancel']:
            report.append("SUBSCRIPTIONS TO CANCEL:")
            for sub in subscription_analysis['definitely_cancel']:
                report.append(f"  - {sub.get('name', 'Unknown')}: ${sub.get('monthly_cost', 0):,.2f}/month")
        report.append("")
        
        # Buffer Analysis
        report.append("💰 ACCOUNT BUFFER ANALYSIS")
        report.append("-" * 80)
        for account_name, buffer_info in buffer_analysis.items():
            report.append(f"{account_name}:")
            report.append(f"  Current Balance:  ${buffer_info['current']:,.2f}")
            report.append(f"  Recommended:      ${buffer_info['recommended']:,.2f}")
            if buffer_info['shortfall'] > 0:
                report.append(f"  ⚠️  Shortfall:      ${buffer_info['shortfall']:,.2f}")
            else:
                report.append(f"  ✅ Buffer adequate")
        report.append("")
        
        # NSF Prevention Plan
        report.append("🛡️  NSF FEE PREVENTION PLAN")
        report.append("-" * 80)
        report.append(f"Current NSF Fees (past 12 months): ${nsf_plan['current_situation']['total_nsf_fees']:,.2f}")
        report.append(f"Current Bank Fees:                 ${nsf_plan['current_situation']['total_bank_fees']:,.2f}")
        report.append("")
        report.append("RECOMMENDED ACTIONS:")
        for i, action in enumerate(nsf_plan['actions'], 1):
            report.append(f"{i}. [{action['priority']}] {action['action']}")
            if 'monthly_savings' in action:
                report.append(f"   Monthly Savings: ${action['monthly_savings']:,.2f}")
            if 'shortfall' in action:
                report.append(f"   Current Shortfall: ${action['shortfall']:,.2f}")
            if 'timeline' in action:
                report.append(f"   Timeline: {action['timeline']}")
            report.append("")
        
        report.append("PROJECTED SAVINGS:")
        report.append(f"  Monthly: ${nsf_plan['projected_savings']['monthly']:,.2f}")
        report.append(f"  Annual:  ${nsf_plan['projected_savings']['annual']:,.2f}")
        report.append("")
        
        report.append("=" * 80)
        
        return "\n".join(report)
    
    def load_from_json(self, filename: str):
        """Load budget data from JSON file"""
        with open(filename, 'r') as f:
            self.data = json.load(f)
    
    def save_to_json(self, filename: str):
        """Save budget data to JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=2)


def main():
    """Main function - processes budget data"""
    import sys
    import os
    
    analyzer = BudgetAnalyzer()
    
    # Check for command line argument or default files
    json_file = 'budget_data.json'
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
    
    # Try to load data
    try:
        analyzer.load_from_json(json_file)
        print(f"✓ Loaded data from {json_file}\n")
    except FileNotFoundError:
        # Try example file
        if json_file == 'budget_data.json' and os.path.exists('budget_data_example.json'):
            print("No budget_data.json found. Using example data for demonstration.\n")
            print("To use your own data:")
            print("  1. Fill out BUDGET_AUDIT_TEMPLATE.md")
            print("  2. Create budget_data.json based on budget_data_template.json")
            print("  3. Run: python3 budget_analyzer.py budget_data.json\n")
            json_file = 'budget_data_example.json'
            analyzer.load_from_json(json_file)
        else:
            print(f"Error: {json_file} not found.")
            print("\nPlease fill out BUDGET_AUDIT_TEMPLATE.md first,")
            print("then create budget_data.json based on budget_data_template.json structure.")
            print("\nOr run with example: python3 budget_analyzer.py budget_data_example.json")
            return
    
    # Generate and print report
    report = analyzer.generate_report()
    print(report)
    
    # Save report to file
    report_file = 'budget_analysis_report.txt'
    with open(report_file, 'w') as f:
        f.write(report)
    print(f"\n✓ Report saved to {report_file}")


if __name__ == '__main__':
    main()

