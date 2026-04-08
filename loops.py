# ===== TOPIC 6: LOOPS =====

print("=== Basic for loop ===")
skills = ["Python", "Java", "LangChain", "Docker", "FastAPI"]
for skill in skills:
    print(f"    - {skill}")

print("\n=== range() ===")
# range(start, stop, step) — stop is exclusive
for i in range(5):              # 0 to 4
    print(i, end=" ")
print()

for i in range(1, 6):           # 1 to 5
    print(i, end=" ")
print()

for i in range(0, 10, 2):       # 0, 2, 4, 6, 8
    print(i, end=" ")
print()

for i in range(5, 0, -1):       # countdown 5 to 1
    print(i, end=" ")
print()

print("\n=== enumerate() ===")
# Get index AND value — replaces Java's for(int i=0; i<list.size(); i++)
for index, skill in enumerate(skills):
    print(f"  {index}: {skill}")

# Start index from 1
print()
for index, skill in enumerate(skills, start=1):
    print(f"  {index}. {skill}")

print("\n=== zip() ===")
# Loop over two lists simultaneously
names = ["John", "Jane", "Bob"]
scores = [95, 87, 92]
roles = ["Architect", "Developer", "Manager"]

for name, score, role in zip(names, scores, roles):
    print(f"  {name:<8} {role:<12} {score}%")

print("\n=== while loop ===")
count = 0
while count < 5:
    print(f"  Count: {count}")
    count += 1

print("\n=== break & continue ===")
# break — exit loop early
print("Break example:")
for skill in skills:
    if skill == "Docker":
        print(f"  Found Docker! Stopping search.")
        break
    print(f"  Checking: {skill}")

# continue — skip current iteration
print("\nContinue example (skip Java):")
for skill in skills:
    if skill == "Java":
        continue        # skip Java
    print(f"  - {skill}")

print("\n=== Loop with else ===")
# else runs only if loop completes WITHOUT hitting break
search = "Kubernetes"
for skill in skills:
    if skill == search:
        print(f"Found {search}!")
        break
else:
    print(f"{search} not found in skills")

print("\n=== Iterating Dictionaries ===")
config = {
    "model": "gpt-4o-mini",
    "temperature": 0.7,
    "max_tokens": 1000,
    "streaming": True
}

for key, value in config.items():
    print(f"  {key:<15}: {value}")

print("\n=== AI Dev Use Case ===")
# Processing multiple tickets in a loop
tickets = [
    {"id": "T001", "text": "App is down!", "priority": "URGENT"},
    {"id": "T002", "text": "Update email", "priority": "LOW"},
    {"id": "T003", "text": "Claim pending", "priority": "NORMAL"},
    {"id": "T004", "text": "Payment failed", "priority": "URGENT"},
    {"id": "T005", "text": "Policy query", "priority": "LOW"},
]

print(f"\n{'ID':<8} {'Priority':<10} {'Action'}")
print("-" * 40)

urgent_count = 0
for ticket in tickets:
    if ticket["priority"] == "URGENT":
        action = "🚨 Escalate now"
        urgent_count += 1
    elif ticket["priority"] == "NORMAL":
        action = "📋 Queue for review"
    else:
        action = "📥 Add to backlog"

    print(f"{ticket['id']:<8} {ticket['priority']:<10} {action}")

print(f"\nTotal urgent tickets: {urgent_count}")