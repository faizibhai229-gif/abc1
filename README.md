# Smart Expense Tracker Bot

This bot helps you track your expenses and provides summaries of your spending.

## Features
- Add expenses with category, amount, and description
- View total expenses and expenses by category
- Data is saved in a JSON file

## Usage
1. Install the dependencies
2. Run the bot script
3. Use the `add_expense` method to log your expenses
4. Use the `get_summary` method to view your spending summary

## Example
python
from bot import SmartExpenseTracker

tracker = SmartExpenseTracker()
tracker.add_expense('Food', 20.50, 'Dinner with friends')
print(tracker.get_summary())
