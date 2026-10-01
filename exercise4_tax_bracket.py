# Exercise 4: Tax Bracket Determiner
# DATA 4000: Python with AI
# Determines an income tax bracket and estimates the tax owed.


def get_tax_bracket(income, check_deduction=False):
    """Return the tax bracket for an income as a string.

    If check_deduction is True (bonus), the bracket is labeled
    "(Deduction Eligible)" when the income is an even number.
    """
    if income < 0:
        return "Invalid income."

    if income < 50000:
        bracket = "Low (10%)"
    elif income < 100000:
        bracket = "Medium (20%)"
    else:
        bracket = "High (30%)"

    # Bonus: modulo checks if income is even; ternary adds the label
    if check_deduction:
        return bracket + " (Deduction Eligible)" if income % 2 == 0 else bracket

    return bracket


def get_tax_rate(income):
    """Return the tax rate (as a decimal) that matches the income."""
    if income < 50000:
        return 0.10
    elif income < 100000:
        return 0.20
    else:
        return 0.30


# Main code
income = float(input("What's your annual income? "))
bracket = get_tax_bracket(income)

if bracket == "Invalid income.":
    print(bracket)
else:
    estimated_tax = round(income * get_tax_rate(income), 2)
    print(f"Your bracket: {bracket}. Estimated tax: {estimated_tax}")
    # Bonus: show the deduction check
    print(f"Deduction check: {get_tax_bracket(income, check_deduction=True)}")
