# ===== F-STRINGS DEEP DIVE =====

print("\n=== Basic f-strings ===")
name = "John"
age = 33
role = "AI Developer"
print(f"Name: {name}, Age: {age}, Role: {role}")

print("\n=== Expressions inside {} ===")
print(f"Next year age : {age + 1}")
print(f"Is adult      : {age >= 18}")
print(f"Name length   : {len(name)}")
print(f"Name upper    : {name.upper()}")
print(f"Ternary       : {'Senior' if age > 30 else 'Junior'}")

print("\n=== Number Formatting ===")
pi = 3.14159265
salary = 123456
score = 0.678
print(f"Pi default      : {pi}")
print(f"Pi 2 decimals   : {pi:.2f}")
print(f"Salary          : ${salary:,}")
print(f"Salary float    : ${salary:,.2f}")
print(f"Score           : {score:.1%}")

print("\n=== Alignment & Padding ===")
skills = [("Python", 95), ("Java", 90), ("Angular", 80)]
print(f"{'Skill':<10} {'Score':>6}%")
print(f"-" * 18)
for skill, score in skills:
    print(f"{skill:<10} {f'{score} %':>6}")

print("\n=== AI Dev Prompt Building ===")
company = "ZZZ Insurance"
customer = "John"
claim_id = "1234"

prompt = (
    f"You are a helpful assistant for {company}.\n"
    f"Customer: {customer}\n"
    f"Claim ID: {claim_id}\n"
    f"Answer professionally and concisely."
)
print(prompt)