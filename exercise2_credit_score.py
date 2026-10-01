# Exercise 2: Credit Score Evaluator
# DATA 4000: Python with AI
# Categorizes a credit score and decides loan eligibility.

# Get the credit score and convert it to an integer
score = int(input("What's your credit score? "))

# Valid credit scores fall between 300 and 850
if score < 300 or score > 850:
    print("Invalid score.")
else:
    # Use chained comparisons to place the score in a category
    if score >= 750:
        category = "Excellent - Loan Approved"
    elif 700 <= score < 750:
        category = "Good - Loan Approved with Review"
    elif 600 <= score < 700:
        category = "Fair - Loan Conditional"
    else:
        category = "Poor - Loan Denied"

    # Only "Excellent" and "Good" count as approved (score of 700 or higher)
    approved = score >= 700

    # Ternary expression picks the follow-up message
    message = "Interest rate: Low" if approved else "Seek credit improvement."

    print(f"{category}. {message}")
