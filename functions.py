# ===== TOPIC 7: FUNCTIONS =====

print("=== Basic Functions ===")
def greet(name):
    return f"Hello {name}!"

print(greet("John"))
print(greet("Jane"))

print("\n=== Default Parameters ===")
def greet_role(name, role="Developer", company="ZZZ Insurance"):
    return f"Hello {name}, {role} at {company}"

print(greet_role("John"))
print(greet_role("Jane", "Architect"))
print(greet_role("Bob", "Manager", "SpaceTech"))

print("\n=== Keyword Arguments ===")
# Call with named parameters — order doesn't matter
print(greet_role(role="AI Developer", name="John"))
print(greet_role(company="Anthropic", name="Jane", role="Engineer"))

print("\n=== Multiple Return Values ===")
# Python can return multiple values as a tuple
def get_claim_info(claim_id):
    # Simulating a DB lookup
    claims = {
        "1234": ("APPROVED", 2500.00),
        "5678": ("PENDING", 800.00),
        "9999": ("REJECTED", 1200.00)
    }
    return claims.get(claim_id, ("NOT_FOUND", 0.00))

status, amount = get_claim_info("1234")
print(f"Status: {status}, Amount: ${amount:,.2f}")

status, amount = get_claim_info("9999")
print(f"Status: {status}, Amount: ${amount:,.2f}")

status, amount = get_claim_info("0000")
print(f"Status: {status}, Amount: ${amount:,.2f}")

print("\n=== Functions as First Class Objects ===")
# In Python, functions can be stored in variables,
# passed as arguments, returned from other functions
# — unlike Java (before lambdas)

def classify_urgent(ticket):
    return "URGENT" in ticket.upper()

def classify_billing(ticket):
    return "PAYMENT" in ticket.upper() or "BILLING" in ticket.upper()

# Store functions in a list
classifiers = [classify_urgent, classify_billing]

tickets = [
    "App is down urgently!",
    "Payment failed twice",
    "Update my email address"
]

for ticket in tickets:
    results = [f.__name__ for f in classifiers if f(ticket)]
    print(f"  '{ticket}' → {results if results else ['GENERAL']}")

print("\n=== Lambda Functions ===")
# Anonymous one-line functions — like Java lambdas
# Java: (x) -> x * 2
# Python:
double = lambda x: x * 2
square = lambda x: x ** 2
add = lambda x, y: x + y

print(f"double(5)  : {double(5)}")
print(f"square(4)  : {square(4)}")
print(f"add(3, 4)  : {add(3, 4)}")

# Very useful with sorted()
claims = [
    {"id": "T001", "amount": 1500},
    {"id": "T002", "amount": 800},
    {"id": "T003", "amount": 3200},
    {"id": "T004", "amount": 250},
]

sorted_claims = sorted(claims, key=lambda c: c["amount"], reverse=True)
print("\nClaims sorted by amount (highest first):")
for claim in sorted_claims:
    print(f"  {claim['id']}: ${claim['amount']:,}")

print("\n=== Docstrings ===")
# Document your functions — LangChain reads these for tools!
def calculate_premium(vehicle_age: int, claim_count: int) -> float:
    """
    Calculate monthly insurance premium for ZZZ Insurance.

    Args:
        vehicle_age: Age of vehicle in years
        claim_count: Number of past claims

    Returns:
        Estimated monthly premium in dollars
    """
    base = 100.0
    age_factor = vehicle_age * 5
    claim_factor = claim_count * 20
    return base + age_factor + claim_factor

premium = calculate_premium(3, 2)
print(f"Premium: ${premium:.2f}")
print(f"Docstring: {calculate_premium.__doc__}")

print("\n=== AI Dev Use Case ===")
# Building a reusable prompt builder function
def build_prompt(
    question: str,
    company: str = "ZZZ Insurance",
    tone: str = "professional",
    max_words: int = 100
) -> str:
    """Build a structured prompt for the LLM."""
    return (
        f"You are a {tone} assistant for {company}.\n"
        f"Answer in under {max_words} words.\n"
        f"Question: {question}"
    )

# Different prompt variations
print(build_prompt("What does my policy cover?"))
print()
print(build_prompt(
    question="How do I file a claim?",
    tone="friendly",
    max_words=50
))