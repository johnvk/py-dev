# ===== TOPIC 5: CONDITIONALS =====

print("=== Basic if/elif/else ===")
age = 20

if age >= 65:
    print("Senior")
elif age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

print("\n=== Comparison Operators ===")
x, y = 10, 20
print(f"x == y  : {x == y}")    # equal
print(f"x != y  : {x != y}")    # not equal
print(f"x > y   : {x > y}")     # greater than
print(f"x < y   : {x < y}")     # less than
print(f"x >= y  : {x >= y}")    # greater or equal
print(f"x <= y  : {x <= y}")    # less or equal

print("\n=== Logical Operators ===")
has_experience = True
knows_python = True
has_degree = False

print(f"and : {has_experience and knows_python}")   # both True
print(f"or  : {has_experience or has_degree}")      # at least one True
print(f"not : {not has_degree}")                    # opposite

# Combined
if has_experience and knows_python:
    print("Eligible for AI Developer role!")

if has_experience and not has_degree:
    print("Experience matters more than degree in AI!")

print("\n=== Membership & Identity ===")
skills = ["Python", "Java", "LangChain"]

# in / not in
print(f"Python in skills    : {'Python' in skills}")
print(f"Angular in skills   : {'Angular' in skills}")
print(f"Angular not in skills: {'Angular' not in skills}")

# is / is not — checks identity not equality
x = None
print(f"x is None     : {x is None}")
print(f"x is not None : {x is not None}")

print("\n=== Ternary Operator ===")
# Java: String status = age >= 18 ? "Adult" : "Minor"
# Python:
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# Nested ternary — use sparingly!
level = "Senior" if age >= 30 else "Mid" if age >= 25 else "Junior"
print(f"Level: {level}")

print("\n=== match/case (Python 3.10+) ===")
# Like Java's switch statement but more powerful
priority = "URGENT"

match priority:
    case "URGENT":
        print("Escalate immediately!")
    case "NORMAL":
        print("Handle within 24 hours")
    case "LOW":
        print("Handle within 72 hours")
    case _:                          # default case
        print("Unknown priority")

print("\n=== AI Dev Use Case ===")
# Routing logic based on LLM classification
def route_ticket(category, priority):
    if category == "CLAIMS" and priority == "URGENT":
        return "Escalate to senior claims handler"
    elif category == "CLAIMS":
        return "Assign to claims team"
    elif category == "BILLING":
        return "Assign to billing team"
    elif category == "TECHNICAL" and priority == "URGENT":
        return "Page on-call engineer immediately"
    elif category == "TECHNICAL":
        return "Create support ticket"
    else:
        return "Assign to general support"

# Test the routing
tickets = [
    ("CLAIMS", "URGENT"),
    ("CLAIMS", "NORMAL"),
    ("BILLING", "LOW"),
    ("TECHNICAL", "URGENT"),
    ("GENERAL", "NORMAL"),
]

print(f"\n{'Category':<12} {'Priority':<10} {'Action'}")
print("-" * 55)
for category, priority in tickets:
    action = route_ticket(category, priority)
    print(f"{category:<12} {priority:<10} {action}")