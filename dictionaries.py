# ===== TOPIC 4: DICTIONARIES =====

print("=== Creating Dictionaries ===")
# Basic dictionary
person = {
    "name": "John",
    "age": 20,
    "city": "Brisbane",
    "skills": ["Python", "Java", "AI Dev"]  # value can be a list!
}
print(f"Person: {person}")
print(f"Name  : {person['name']}")
print(f"Skills: {person['skills']}")

print("\n=== Accessing Values ===")
# [] vs .get()
print(f"Using []        : {person['name']}")
print(f"Using .get()    : {person.get('name')}")

print(f"Missing key []  : ", end="")
try:
    print(person['phone'])
except KeyError as e:
    print(f"KeyError: {e}")

print(f"Missing .get()  : {person.get('phone')}")           # None
print(f"Missing default : {person.get('phone', 'N/A')}")    # N/A

print("\n=== Modifying Dictionaries ===")
person["email"] = "john@email.com"      # add
person["age"] = 21                      # update
print(f"After add/update: {person}")
removed = person.pop("city")
print(f"Removed city    : {removed}")
print(f"After pop       : {person}")

print("\n=== Iterating ===")
config = {
    "model": "gpt-4o-mini",
    "temperature": 0.7,
    "max_tokens": 1000,
    "streaming": True
}

print("Keys   :", list(config.keys()))
print("Values :", list(config.values()))
print("\nKey-Value pairs:")
for key, value in config.items():
    print(f"  {key:<15}: {value}")

print("\n=== Nested Dictionaries ===")
# Very common in AI dev — API responses are nested dicts!
claim = {
    "claim_id": "1234",
    "status": "APPROVED",
    "customer": {
        "name": "John",
        "email": "john@email.com",
        "policy": {
            "id": "POL001",
            "type": "Comprehensive"
        }
    },
    "amount": 2500.00
}

# Accessing nested values
print(f"Claim ID      : {claim['claim_id']}")
print(f"Customer name : {claim['customer']['name']}")
print(f"Policy type   : {claim['customer']['policy']['type']}")
print(f"Amount        : ${claim['amount']:,.2f}")

print("\n=== Dictionary Methods ===")
# Merging two dictionaries
defaults = {"temperature": 0.7, "max_tokens": 1000, "model": "gpt-4o-mini"}
overrides = {"temperature": 0.2, "max_tokens": 500}
merged = {**defaults, **overrides}    # ** unpacking — we'll cover this later!
print(f"Defaults : {defaults}")
print(f"Overrides: {overrides}")
print(f"Merged   : {merged}")

print("\n=== AI Dev Use Case ===")
# Parsing a structured LLM response
llm_response = {
    "category": "CLAIMS",
    "priority": "URGENT",
    "suggested_response": "We will look into your claim immediately."
}

# Safely extract each field with defaults
category = llm_response.get("category", "GENERAL")
priority = llm_response.get("priority", "NORMAL")
response = llm_response.get("suggested_response", "Thank you for contacting us.")
confidence = llm_response.get("confidence", "N/A")  # missing key — uses default

print(f"Category   : {category}")
print(f"Priority   : {priority}")
print(f"Response   : {response}")
print(f"Confidence : {confidence}")