import json
import os

class SmartExpenseTracker:
    def __init__(self, file_path='expenses.json'):
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                json.dump({'expenses': []}, file)

    def add_expense(self, category, amount, description=''):
        expense = {
            'category': category,
            'amount': amount,
            'description': description
        }
        with open(self.file_path, 'r+') as file:
            data = json.load(file)
            data['expenses'].append(expense)
            file.seek(0)
            json.dump(data, file, indent=4)

    def get_summary(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            total = sum(expense['amount'] for expense in data['expenses'])
            categories = {}
            for expense in data['expenses']:
                category = expense['category']
                if category in categories:
                    categories[category] += expense['amount']
                else:
                    categories[category] = expense['amount']
            return {
                'total_expenses': total,
                'expenses_by_category': categories
            }

if __name__ == '__main__':
    tracker = SmartExpenseTracker()
    tracker.add_expense('Food', 20.50, 'Dinner with friends')
    tracker.add_expense('Transport', 10.00, 'Bus fare')
    tracker.add_expense('Food', 15.00, 'Lunch')
    print(tracker.get_summary())