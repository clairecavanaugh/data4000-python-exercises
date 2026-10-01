# DATA 4000: Python with AI — Exercises

Solutions to the Functions, Variables, and Conditionals exercises. Written in Python 3.10+ (match-case requires 3.10 or newer). Run any file with `python <filename>.py`.

## Exercise 1: Profit Margin Calculator
`exercise1_profit_calculator.py` — Asks for revenue and cost, then prints profit and margin.

Assumptions: revenue of 0 or less prints "Invalid revenue." Negative profit (a loss) is allowed and shown as a negative margin.

```
What's the revenue? 5000.0
What's the cost? 3500.0
Profit: $1,500.00 | Margin: 30.00%
```

## Exercise 2: Credit Score Evaluator
`exercise2_credit_score.py` — Categorizes a credit score from 300–850 and decides loan eligibility.

Assumptions: only Excellent (750+) and Good (700–749) count as "approved" and get the low interest rate. Fair (Loan Conditional) and Poor get "Seek credit improvement."

```
What's your credit score? 720
Good - Loan Approved with Review. Interest rate: Low
```

## Exercise 3: Customer Greeting Formatter
`exercise3_greeting_formatter.py` — `format_greeting(name, title="Customer")` strips, title-cases, and splits the name to greet the customer by first name.

Assumptions: a blank name returns "Hello, Valued Customer!" The optional title parameter is included (e.g. `format_greeting("jane smith", "VIP")` → `Hello, Jane (VIP)!`).

```
What's your full name?   john doe
Hello, John (Customer)!
```

## Exercise 4: Tax Bracket Determiner
`exercise4_tax_bracket.py` — `get_tax_bracket(income)` returns the bracket; `get_tax_rate(income)` returns the matching rate for the tax estimate.

Assumptions: negative income prints "Invalid income." For the bonus, `get_tax_bracket(income, check_deduction=True)` uses modulo and a ternary to add "(Deduction Eligible)" for even incomes.

```
What's your annual income? 75000.0
Your bracket: Medium (20%). Estimated tax: 15000.0
Deduction check: Medium (20%) (Deduction Eligible)
```

## Exercise 5: Product Category Matcher
`exercise5_product_category.py` — Uses match-case (with a guard for names starting with "tech") to assign a margin category.

Assumptions: input is stripped and lowercased, so "  TECH Phone " and "tech phone" match the same way.

```
What's the product name?  Tech Phone
Product: tech phone | Category: High Margin
```

## Bonus: Integrated Decision Tool
`bonus_decision_tool.py` (on branch `bonus-decision-tool`) — Prompts for revenue, cost, and product category; uses `is_profitable()` and match-case to suggest an action.

Assumptions: suggestions are High Margin → Reinvest, Medium → Maintain and monitor, Low → Focus on cost reduction, other → Review category.

```
What's the revenue? 10000
What's the cost? 6000
What's the product category? electronics
Profitable! Profit: $4,000.00
Category: High Margin | Suggestion: Reinvest
```
