# ===== TOPIC 9: LIST COMPREHENSIONS =====

print("=== Basic List Comprehension ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Traditional loop
doubled_loop = []
for n in numbers:
    doubled_loop.append(n * 2)

# List comprehension
doubled_comp = [n * 2 for n in numbers]

print(f"Traditional : {doubled_loop}")
print(f"Comprehension: {doubled_comp}")

print("\n=== With Condition (Filter) ===")
# Only even numbers
evens = [n for n in numbers if n % 2 == 0]
print(f"Evens       : {evens}")

# Only odd numbers
odds = [n for n in numbers if n % 2 != 0]
print(f"Odds        : {odds}")

# Numbers greater than 5
big = [n for n in numbers if n > 5]
print(f"Greater > 5 : {big}")

print("\n=== Transformation + Filter ===")
# Double only even numbers
doubled_evens = [n * 2 for n in numbers if n % 2 == 0]
print(f"Doubled evens: {doubled_evens}")

# Square numbers greater than 5
squared_big = [n ** 2 for n in numbers if n > 5]
print(f"Squared > 5  : {squared_big}")

print("\n=== String List Comprehensions ===")
skills = ["python", "java", "langchain", "docker", "fastapi"]

# Uppercase all
upper = [s.upper() for s in skills]
print(f"Uppercase : {upper}")

# Only skills longer than 5 chars
long_skills = [s for s in skills if len(s) > 5]
print(f"Long skills : {long_skills}")

# Capitalise and add emoji
fancy = [f"✅ {s.title()}" for s in skills]
print(f"Fancy       : {fancy}")

print("\n=== Dictionary Comprehensions ===")
# Same concept but for dictionaries
skill_lengths = {skill: len(skill) for skill in skills}
print(f"Skill lengths: {skill_lengths}")

# Filter — only skills with length > 5
long_skill_dict = {k: v for k, v in skill_lengths.items() if v > 5}
print(f"Long skills  : {long_skill_dict}")

print("\n=== Set Comprehensions ===")
words = ["python", "java", "python", "ai", "java", "docker"]
unique_upper = {w.upper() for w in words}   # {} = set comprehension
print(f"Unique upper: {unique_upper}")

print("\n=== Nested List Comprehensions ===")
# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [n for row in matrix for n in row]
print(f"Matrix : {matrix}")
print(f"Flat   : {flat}")

print("\n=== AI Dev Use Cases ===")
# 1. Extract content from LLM message objects
messages = [
    {"role": "user", "content": "What is my claim status?"},
    {"role": "assistant", "content": "Your claim is approved."},
    {"role": "user", "content": "What is my premium?"},
    {"role": "assistant", "content": "Your premium is $120/month."},
]

# Extract only user messages
user_messages = [m["content"] for m in messages if m["role"] == "user"]
print(f"User messages: {user_messages}")

# 2. Clean and prepare document chunks for RAG
raw_chunks = [
    "  ZZZ covers flood damage  ",
    "",
    "Claims within 48 hours   ",
    "   ",
    "Premium due 1st of month  "
]

# Clean — strip whitespace and remove empty strings
clean_chunks = [c.strip() for c in raw_chunks if c.strip()]
print(f"\nRaw chunks   : {len(raw_chunks)} items")
print(f"Clean chunks : {len(clean_chunks)} items")
for chunk in clean_chunks:
    print(f"  '{chunk}'")

# 3. Build batch prompts for multiple tickets
tickets = ["App down", "Payment failed", "Update email"]
prompts = [f"Classify this support ticket: '{t}'" for t in tickets]

print(f"\nBatch prompts: ")
for p in prompts:
    print(f"  {p}")
