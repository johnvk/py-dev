# ===== TOPIC 10: EXCEPTION HANDLING =====

print("=== Basic try/except ===")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"  Caught: {e}")

print("\n=== Multiple except blocks ===")
def parse_input(value):
    try:
        number = int(value)
        result = 100 / number
        return result
    except ValueError as e:
        print(f"  ValueError  : '{value}' is not a number")
    except ZeroDivisionError as e:
        print(f"  ZeroDivision: Cannot divide by zero")
    except Exception as e:
        print(f"  Unexpected  : {e}")

parse_input("abc")      # ValueError
parse_input(0)          # ZeroDivisionError
parse_input(5)          # Success
print(f"  Result: {parse_input(5)}")

print("\n=== try/except/else/finally ===")
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"  Cannot divide {a} by zero")
        return None
    else:
        # Runs only if NO exception occurred
        print(f"  {a} / {b} = {result}")
        return result
    finally:
        # Always runs — like Java's finally
        print(f"  Division attempt complete")

divide(10, 2)
print()
divide(10, 0)

print("\n=== Raising Exceptions ===")
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    if age > 150:
        raise ValueError(f"Age seems unrealistic: {age}")
    return f"Valid age: {age}"

# Test validation
tests = [25, -5, 200, "twenty"]
for test in tests:
    try:
        print(f"  {validate_age(test)}")
    except (TypeError, ValueError) as e:
        print(f"  ❌ {e}")

print("\n=== Custom Exceptions ===")
# Create your own exceptions — like Java custom exceptions
class InsuranceError(Exception):
    """Base exception for ZZZ Insurance"""
    pass

class ClaimNotFoundError(InsuranceError):
    """Raised when claim ID doesn't exist"""
    def __init__(self, claim_id):
        self.claim_id = claim_id
        super().__init__(f"Claim {claim_id} not found")

class PolicyExpiredError(InsuranceError):
    """Raised when policy has expired"""
    def __init__(self, policy_id, expiry_date):
        self.policy_id = policy_id
        super().__init__(f"Policy {policy_id} expired on {expiry_date}")

def get_claim(claim_id):
    claims = {"1234": "APPROVED", "5678": "PENDING"}
    if claim_id not in claims:
        raise ClaimNotFoundError(claim_id)
    return claims[claim_id]

def get_policy(policy_id):
    expired = {"POL999": "2024-01-01"}
    if policy_id in expired:
        raise PolicyExpiredError(policy_id, expired[policy_id])
    return "ACTIVE"

# Test custom exceptions
for claim_id in ["1234", "9999"]:
    try:
        status = get_claim(claim_id)
        print(f"  ✅ Claim {claim_id}: {status}")
    except ClaimNotFoundError as e:
        print(f"  ❌ {e}")

for policy_id in ["POL001", "POL999"]:
    try:
        status = get_policy(policy_id)
        print(f"  ✅ Policy {policy_id}: {status}")
    except PolicyExpiredError as e:
        print(f"  ❌ {e}")

print("\n=== AI Dev Use Case ===")
# Safely calling LLM APIs — always wrap in try/except
def safe_llm_call(prompt: str, max_retries: int = 3) -> str:
    """
    Safely call LLM with retry logic.
    Returns response or error message.
    """
    import random  # simulating random failures

    for attempt in range(1, max_retries + 1):
        try:
            # Simulate occasional API failures
            if random.random() < 0.4:  # 40% chance of failure
                raise ConnectionError("LLM API timeout")

            # Simulate successful response
            return f"LLM response to: '{prompt[:30]}...'"

        except ConnectionError as e:
            print(f"  ⚠️  Attempt {attempt}/{max_retries} failed: {e}")
            if attempt == max_retries:
                return "❌ LLM unavailable after max retries"

    return "❌ Unexpected error"

# Test retry logic
prompts = [
    "What does my ZZZ policy cover?",
    "Check claim status 1234",
    "Calculate my premium"
]

print("Testing LLM calls with retry logic:")
for prompt in prompts:
    result = safe_llm_call(prompt)
    print(f"  Result: {result}")
