#promting user for information
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

#calculations
monthly_savings = monthly_income - monthly_expenses
project_savings = monthly_savings * 12 + monthly_savings * 12 * 0.05

# printing the result
print(f"your monthly savings are ${monthly_savings}")
print(f"projected savings after one year, with interest, is: ${project_savings}")
