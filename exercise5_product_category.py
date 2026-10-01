# Exercise 5: Product Category Matcher
# DATA 4000: Python with AI
# Uses match-case to assign a margin category to a product.

# strip() removes extra spaces, lower() makes matching case-insensitive
product = input("What's the product name? ").strip().lower()

match product:
    case "electronics" | "gadget":
        category = "High Margin"
    # A guard (if ...) lets us match anything that starts with "tech"
    case name if name.startswith("tech"):
        category = "High Margin"
    case "clothing" | "apparel":
        category = "Medium Margin"
    case "food" | "grocery":
        category = "Low Margin"
    # _ is the wildcard: it catches everything else
    case _:
        category = "Uncategorized - Review Needed"

print(f"Product: {product} | Category: {category}")
