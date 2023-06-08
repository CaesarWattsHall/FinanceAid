# This program prompts the user to enter their monthly income and then enter their expenses one at a time. 
# When the user is finished entering expenses, they can type “done” to finish. 
# The program then calculates the total expenses and the remaining income and prints the results.

# You can modify this program to better suit your needs. 
# For example, you could add categories for different types of expenses (e.g. housing, food, transportation) 
# or allow the user to enter expenses for different time periods (e.g. weekly, bi-weekly, monthly).

# By: Caesar R. Watts-Hall
# Date: June 08, 2023

class Budget:
    def __init__(self, income):
        self.income = income
        self.expenses = []
        self.categories = {}

    def add_expense(self, amount, category):
        self.expenses.append(amount)
        if category in self.categories:
            self.categories[category] += amount
        else:
            self.categories[category] = amount

    def get_total_expenses(self):
        return sum(self.expenses)

    def get_remaining_income(self):
        return self.income - self.get_total_expenses()

    def get_category_spending(self, category):
        if category in self.categories:
            return self.categories[category]
        else:
            return 0

income = float(input('Enter your monthly income: '))
budget = Budget(income)

while True:
    expense = input('Enter an expense (or "done" to finish): ')
    if expense == 'done':
        break
    category = input('Enter the category for this expense: ')
    budget.add_expense(float(expense), category)

print(f'Total expenses: {budget.get_total_expenses():.2f}')
print(f'Remaining income: {budget.get_remaining_income():.2f}')

for category, amount in budget.categories.items():
    print(f'{category}: {amount:.2f}')

# This program defines a Budget class that allows the user to enter their income and expenses and categorize their expenses. 
# The class also provides methods for calculating the total expenses, remaining income, and spending by category.
# This is just one example of how such a program might be structured. 
# A more comprehensive program might also include features for tracking savings and investments, calculating net worth, 
# and generating reports or visualizations of the user’s financial data.

# income = float(input('Enter your monthly income: '))
# expenses = []
# while True:
#    expense = input('Enter an expense (or "done" to finish): ')
#   if expense == 'done':
#        break
#    expenses.append(float(expense))
#
# total_expenses = sum(expenses)
# print(f'Total expenses: {total_expenses:.2f}')
# remaining_income = income - total_expenses
# print(f'Remaining income: {remaining_income:.2f}')
