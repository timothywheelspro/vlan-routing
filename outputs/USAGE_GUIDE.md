# Budget Analyzer Usage Guide

## Quick Start

### Option 1: Use Example Data (Demo)

```bash
cd outputs
python3 budget_analyzer.py budget_data_example.json
```

This will analyze the example data and generate a report showing how the analyzer works.

### Option 2: Use Your Own Data

1. **Fill out the template**: Complete `BUDGET_AUDIT_TEMPLATE.md` with your financial data

2. **Create JSON file**: Copy `budget_data_template.json` to `budget_data.json` and fill it in:

```bash
cp budget_data_template.json budget_data.json
# Edit budget_data.json with your data
```

3. **Run the analyzer**:

```bash
python3 budget_analyzer.py budget_data.json
```

4. **View the report**: The analyzer will:
   - Print the report to the terminal
   - Save it to `budget_analysis_report.txt`

---

## JSON Data Format

Your `budget_data.json` should follow this structure:

```json
{
  "income": {
    "monthly": 5000,
    "annual": 60000
  },
  "expenses": {
    "fixed": 3000,
    "variable_essential": 500,
    "subscriptions": 150,
    "debt": 400
  },
  "subscriptions": [
    {
      "name": "Netflix",
      "monthly_cost": 15.99,
      "annual_cost": 191.88,
      "status": "active",
      "last_used": "2025-12-25",
      "category": "entertainment"
    }
  ],
  "nsf_fees": 0,
  "bank_fees": 0,
  "accounts": [
    {
      "name": "Primary Checking",
      "current_balance": 1000,
      "type": "checking"
    }
  ]
}
```

---

## What the Analyzer Does

### 1. Calculates Cash Flow
- Monthly income vs expenses
- Net cash flow (surplus or deficit)

### 2. Analyzes Subscriptions
- Identifies unused subscriptions to cancel
- Flags high-cost subscriptions for review
- Calculates potential savings

### 3. Analyzes Account Buffers
- Calculates recommended buffer for each account
- Identifies shortfalls
- Provides buffer targets

### 4. Creates NSF Prevention Plan
- Identifies actions to prevent NSF fees
- Prioritizes recommendations
- Projects potential savings

---

## Example Output

The analyzer generates a comprehensive report including:

- **Monthly Cash Flow Summary**: Income, expenses, net flow
- **Subscription Analysis**: What to keep, cancel, or review
- **Account Buffer Analysis**: Recommended buffers and shortfalls
- **NSF Prevention Plan**: Actionable steps with priorities
- **Projected Savings**: Monthly and annual savings potential

---

## Tips

1. **Be Accurate**: Use real numbers from your financial statements
2. **Update Regularly**: Re-run analysis monthly or quarterly
3. **Use Results**: Act on the recommendations to improve your finances
4. **Track Progress**: Compare reports over time to see improvement

---

## Troubleshooting

**Error: File not found**
- Make sure you're in the `outputs/` directory
- Check that your JSON file exists and is named correctly

**Error: Invalid JSON**
- Validate your JSON at jsonlint.com
- Check for missing commas, brackets, or quotes

**No subscriptions found**
- Make sure subscriptions array exists (can be empty: `[]`)
- Check subscription object format matches template

---

## Next Steps After Analysis

1. **Review the report** - Understand your financial situation
2. **Cancel unused subscriptions** - Use the cancellation guides
3. **Build account buffers** - Set up automatic transfers
4. **Track progress** - Re-run analysis monthly
5. **Implement recommendations** - Follow the action plan

