# Bonus Challenge: Integrated Decision Tool
# DATA 4000: Python with AI
# Combines functions, conditionals, and match-case to suggest a business decision.


def get_category(product):
    """Return the margin category for a product (same rules as Exercise 5)."""
    product = product.strip().lower()
    match product:
        case "electronics" | "gadget":
            return "High Margin"
        case name if name.startswith("tech"):
            return "High Margin"
        case "clothing" | "apparel":
            return "Medium Margin"
        case "food" | "grocery":
            return "Low Margin"
        case _:
            return "Uncategorized - Review Needed"


def is_profitable(revenue, cost):
    """Return True if revenue is greater than cost, otherwise False."""
    return revenue > cost


def get_suggestion(category):
    """Return an investment suggestion based on the margin category."""
    match category:
        case "High Margin":
            return "Reinvest"
        case "Medium Margin":
            return "Maintain and monitor"
        case "Low Margin":
            return "Focus on cost reduction"
        case _:
            return "Review category before investing"


def main():
    revenue = float(input("What's the revenue? "))
    cost = float(input("What's the cost? "))
    product = input("What's the product category? ")

    category = get_category(product)

    if is_profitable(revenue, cost):
        profit = revenue - cost
        print(f"Profitable! Profit: ${profit:,.2f}")
        print(f"Category: {category} | Suggestion: {get_suggestion(category)}")
    else:
        print(f"Not profitable (loss of ${cost - revenue:,.2f}). Hold off on new investment.")


main()
