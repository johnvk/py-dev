# ===== TOPIC 15: DECORATORS =====

import time
import functools
from datetime import datetime

print("=== Basic Decorator ===")
def add_logging(func):
    def wrapper():
        print(f"  ▶ Calling {func.__name__}()")
        func()
        print(f"  ✅ {func.__name__}() complete")
    return wrapper

@add_logging
def greet():
    print("  Hello from greet!")

greet()

print("\n=== Decorator with Arguments ===")
# Use functools.wraps to preserve original function metadata
def add_logging_args(func):
    @functools.wraps(func)      # preserves func.__name__, __doc__ etc
    def wrapper(*args, **kwargs):
        print(f"  ▶ Calling {func.__name__}() with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"  ✅ {func.__name__}() returned: {result}")
        return result
    return wrapper

@add_logging_args
def add(a: int, b: int) -> int:
    return a + b

@add_logging_args
def greet_person(name: str, role: str = "Developer") -> str:
    return f"Hello {name}, {role}!"

add(3, 4)
print()
greet_person("John", role="AI Architect")

print("\n=== Timing Decorator ===")
def timer(func):
    """Measures how long a function takes to run."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  ⏱️  {func.__name__}() took {(end-start)*1000:.2f}ms")
        return result
    return wrapper

@timer
def process_claims(claims: list) -> list:
    """Process a list of claims."""
    time.sleep(0.1)     # simulate processing time
    return [c.upper() for c in claims]

result = process_claims(["claim_1234", "claim_5678", "claim_9999"])
print(f"  Processed: {result}")

print("\n=== Retry Decorator ===")
# Remember the retry logic from Topic 10? Now as a reusable decorator!
def retry(max_attempts: int = 3, delay: float = 0.1):
    """Retry decorator with configurable attempts and delay."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  ⚠️  Attempt {attempt}/{max_attempts} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise Exception(f"Failed after {max_attempts} attempts")
        return wrapper
    return decorator

import random
random.seed(42)

@retry(max_attempts=3, delay=0.1)
def unstable_api_call(endpoint: str) -> str:
    """Simulates an unstable API call."""
    if random.random() < 0.6:   # 60% chance of failure
        raise ConnectionError(f"API timeout: {endpoint}")
    return f"✅ Success from {endpoint}"

try:
    result = unstable_api_call("/api/claims")
    print(f"  Result: {result}")
except Exception as e:
    print(f"  ❌ {e}")

print("\n=== Validation Decorator ===")
def validate_inputs(func):
    """Validates that no arguments are None."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for i, arg in enumerate(args):
            if arg is None:
                raise ValueError(f"Argument {i+1} cannot be None")
        for key, value in kwargs.items():
            if value is None:
                raise ValueError(f"Argument '{key}' cannot be None")
        return func(*args, **kwargs)
    return wrapper

@validate_inputs
def create_claim(claim_id: str, customer: str, amount: float) -> dict:
    return {"id": claim_id, "customer": customer, "amount": amount}

# Valid call
print(f"  Valid   : {create_claim('1234', 'John', 2500.00)}")

# Invalid call
try:
    create_claim('1234', None, 2500.00)
except ValueError as e:
    print(f"  ❌ {e}")

print("\n=== Stacking Decorators ===")
# Multiple decorators — applied bottom up
@timer
@add_logging_args
def calculate_premium(vehicle_age: int, claim_count: int) -> float:
    """Calculate ZZZ Insurance premium."""
    time.sleep(0.05)
    return 100.0 + (vehicle_age * 5) + (claim_count * 20)

result = calculate_premium(3, 2)
print(f"  Premium: ${result:.2f}")

print("\n=== AI Dev Use Case ===")
# Cache decorator — avoid calling LLM twice for same question
def cache_response(func):
    """Simple cache — store LLM responses to avoid duplicate API calls."""
    cache = {}

    @functools.wraps(func)
    def wrapper(prompt: str, *args, **kwargs):
        if prompt in cache:
            print(f"  💾 Cache hit for: '{prompt[:40]}...'")
            return cache[prompt]

        print(f"  🔄 Cache miss — calling LLM for: '{prompt[:40]}...'")
        result = func(prompt, *args, **kwargs)
        cache[prompt] = result
        return result

    return wrapper

@cache_response
@timer
def call_llm(prompt: str) -> str:
    """Simulate an LLM API call."""
    time.sleep(0.1)     # simulate API latency
    return f"LLM response to: '{prompt[:30]}...'"

# First call — hits LLM
r1 = call_llm("Does my ZZZ policy cover flood damage?")
print(f"  Response: {r1}")

# Second call — same prompt, uses cache!
r2 = call_llm("Does my ZZZ policy cover flood damage?")
print(f"  Response: {r2}")

# Different prompt — hits LLM again
r3 = call_llm("What is my monthly premium?")
print(f"  Response: {r3}")

print("\n=== How @tool Works in LangChain ===")
# Now you understand what @tool does under the hood!
# It's a decorator that:
# 1. Takes your function
# 2. Wraps it with LangChain's Tool class
# 3. Reads your docstring for the LLM description
# 4. Reads your type hints for the parameter schema
# 5. Returns a Tool object the agent can call

def tool_decorator(func):
    """Simplified version of LangChain's @tool decorator."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  🔧 Tool '{func.__name__}' called")
        print(f"  📖 Description: {func.__doc__}")
        result = func(*args, **kwargs)
        print(f"  ✅ Tool returned: {result}")
        return result
    wrapper.is_tool = True
    wrapper.tool_name = func.__name__
    return wrapper

@tool_decorator
def get_claim_status(claim_id: str) -> str:
    """Look up the status of an insurance claim. Use when user asks about a claim."""
    return f"Claim {claim_id}: APPROVED"

get_claim_status("1234")