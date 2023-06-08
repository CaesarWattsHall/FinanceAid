# This program prompts the user to enter their monthly income and then enter their expenses one at a time. 
# When the user is finished entering expenses, they can type “done” to finish. 
# The program then calculates the total expenses and the remaining income and prints the results.

# You can modify this program to better suit your needs. 
# For example, you could add categories for different types of expenses (e.g. housing, food, transportation) 
# or allow the user to enter expenses for different time periods (e.g. weekly, bi-weekly, monthly).

# By: Caesar R. Watts-Hall
# Date: June 08, 2023

income = float(input('Enter your monthly income: '))
expenses = []
while True:
    expense = input('Enter an expense (or "done" to finish): ')
    if expense == 'done':
        break
    expenses.append(float(expense))

total_expenses = sum(expenses)
print(f'Total expenses: {total_expenses:.2f}')
remaining_income = income - total_expenses
print(f'Remaining income: {remaining_income:.2f}')
