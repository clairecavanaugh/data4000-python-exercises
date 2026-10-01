# Exercise 3: Customer Greeting Formatter
# DATA 4000: Python with AI
# Builds a personalized email greeting from a customer's name.


def format_greeting(name, title="Customer"):
    """Return a greeting using the customer's first name and a title.

    title has a default of "Customer" but can be overridden,
    e.g. format_greeting("jane smith", "VIP") -> "Hello, Jane (VIP)!"
    """
    # strip() removes leading/trailing spaces, like "   john doe  " -> "john doe"
    name = name.strip()

    # If nothing is left after stripping, use a generic greeting
    if name == "":
        return "Hello, Valued Customer!"

    # title() capitalizes each word: "john doe" -> "John Doe"
    name = name.title()

    # split() breaks the name on spaces; [0] grabs the first name
    first_name = name.split()[0]

    return f"Hello, {first_name} ({title})!"


# Main code: ask for the full name and print the greeting
full_name = input("What's your full name? ")
print(format_greeting(full_name))
