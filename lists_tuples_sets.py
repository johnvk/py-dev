# ===== TOPIC 3: LISTS, TUPLES & SETS =====

print(f"\n=== Lists ===")
skills = ["Python", "Java", "Angular", "Docker"]
print(f"Original   : {skills}")
print(f"First      : {skills[0]}")
print(f"Last       : {skills[-1]}")
print(f"Slice 0-2  : {skills[:2]}")
print(f"Length     : {len(skills)}")

# Modifying lists
skills.append("AI Dev")
print(f"After append  : {skills}")
skills.remove("Java")
print(f"After remove  : {skills}")
skills.insert(1, "LangChain")
print(f"After insert  : {skills}")
skills[0] = "Python 3.11"
print(f"After update  : {skills}")
print(f"Sorted list   : {sorted(skills)}")

# Useful list methods
numbers = [5, 3, 8, 1, 9, 2]
print(f"\nNumbers       : {numbers}")
print(f"Sorted        : {sorted(numbers)}")
print(f"Reversed      : {sorted(numbers, reverse=True)}")
print(f"Min           : {min(numbers)}")
print(f"Max           : {max(numbers)}")
print(f"Sum           : {sum(numbers)}")

# Checking membership
print(f"\n'doCKer' in skills  : {'doCKer' in skills}")
print(f"'Docker' in skills  : {'Docker' in skills}")
print(f"'LangChain' in skills: {'LangChain' in skills}")

print("\n=== Tuples ===")
# Good for fixed data that shouldn't change
person = ("Tom", 20, "Brisbane")
name, age, city = person     # unpacking — very Pythonic!
print(f"Tuple    : {person}")
print(f"Name     : {name}")
print(f"Age      : {age}")
print(f"City     : {city}")

# Common use — returning multiple values from a function
def get_dimensions():
    return (1920, 1080)     # returns a tuple

width, height = get_dimensions()
print(f"Width: {width}, Height: {height}")

print("\n=== Sets ===")
# Automatically removes duplicates
tags = {"python", "ai", "java", "python", "ai", "docker"}
print(f"Set (no duplicates): {tags}")

# Set operations — very useful!
backend_skills = {"Java", "Spring Boot", "Docker", "Kafka"}
ai_skills = {"Python", "LangChain", "Docker", "FastAPI"}

print(f"\nBackend skills : {backend_skills}")
print(f"AI skills      : {ai_skills}")
print(f"Common (intersection) : {backend_skills & ai_skills}")
print(f"All combined (union)  : {backend_skills | ai_skills}")
print(f"Backend only (diff)   : {backend_skills - ai_skills}")

print("\n=== AI Dev Use Case ===")
# Deduplicating retrieved document chunks in RAG
retrieved_chunks = [
    "ZZZ covers flood damage",
    "Claims must be filed within 48 hours",
    "ZZZ covers flood damage",      # duplicate!
    "Premium is due on 1st of month",
    "Claims must be filed within 48 hours"  # duplicate!
]
unique_chunks = list(set(retrieved_chunks))
print(f"Raw chunks    : {len(retrieved_chunks)} items")
print(f"Unique chunks : {len(unique_chunks)} items")
for chunk in unique_chunks:
    print(f"  - {chunk}")