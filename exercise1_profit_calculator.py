# Exercise 1: Profit Margin Calculator
# DATA 4000: Python with AI
# Calculates profit and profit margin from user-entered revenue and cost.

# Get revenue and cost from the user and convert them to floats
revenue = float(input("What's the revenue? "))
cost = float(input("What's the cost? "))

# Profit is simply revenue minus cost
profit = revenue - cost

# Only calculate margin when revenue is positive (avoids dividing by zero)
if revenue > 0:
    margin = (profit / revenue) * 100
    # :,.2f adds thousands separators and rounds to 2 decimal places
    print(f"Profit: ${profit:,.2f} | Margin: {margin:.2f}%")
else:
    print("Invalid revenue.")
