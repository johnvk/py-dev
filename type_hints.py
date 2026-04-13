# ===== TOPIC 14: TYPE HINTS =====

from typing import Optional, Union, Any

print("=== Basic Type Hints ===")
# Variable annotations
name: str = "John"
age: int = 45
salary: float = 152838.00
is_active: bool = True
nothing: None = None

print(f"name    : {name} ({type(name).__name__})")
print(f"age     : {age} ({type(age).__name__})")
print(f"salary  : ${salary:,.2f} ({type(salary).__name__})")
print(f"active  : {is_active} ({type(is_active).__name__})")

print("\n=== Function Type Hints ===")
def greet(name: str, role: str = "Developer") -> str:
    return f"Hello {name}, {role}!"

def calculate_premium(vehicle_age: int, claim_count: int) -> float:
    return 100.0 + (vehicle_age * 5) + (claim_count * 20)

def log_message(message: str) -> None:
    print(f"  LOG: {message}")

print(greet("John", "Java Developer"))
print(f"Premium: ${calculate_premium(3, 2):.2f}")
log_message("System started")

print("\n=== Collection Type Hints ===")
# Python 3.9+ — use built-in types directly
def process_skills(skills: list[str]) -> list[str]:
    return [s.upper() for s in skills]

def build_config(settings: dict[str, Any]) -> dict[str, Any]:
    defaults = {"temperature": 0.7, "max_tokens": 1000}
    return {**defaults, **settings}

def get_dimensions() -> tuple[int, int]:
    return (1920, 1080)

skills = ["python", "java", "langchain"]
print(f"Skills     : {process_skills(skills)}")
print(f"Config     : {build_config({'model': 'gpt-4o-mini'})}")
print(f"Dimensions : {get_dimensions()}")

print("\n=== Optional — Can be None ===")
# Optional[str] means str or None
# Python 3.10+ shorthand: str | None
def find_claim(claim_id: str) -> str | None:
    claims = {"1234": "APPROVED", "5678": "PENDING"}
    return claims.get(claim_id)  # returns None if not found

result = find_claim("1234")
missing = find_claim("9999")

print(f"Found   : {result}")
print(f"Missing : {missing}")

# Always check for None before using Optional values
if result is not None:
    print(f"Status  : {result.lower()}")

print("\n=== Union — Multiple Types ===")
# Union[str, int] means str OR int
# Python 3.10+ shorthand: str | int
def parse_id(value: str | int) -> str:
    return str(value).upper()

print(f"String ID : {parse_id('pol001')}")
print(f"Int ID    : {parse_id(1234)}")

print("\n=== Type Hints in Classes ===")
class ZZZClaim:
    claim_id: str
    status: str
    amount: float
    notes: str | None

    def __init__(
        self,
        claim_id: str,
        status: str,
        amount: float,
        notes: str | None = None
    ) -> None:
        self.claim_id = claim_id
        self.status = status
        self.amount = amount
        self.notes = notes

    def summarise(self) -> str:
        note_text = f" | Notes: {self.notes}" if self.notes else ""
        return f"Claim {self.claim_id}: {self.status} ${self.amount:,.2f}{note_text}"

c1 = ZZZClaim("1234", "APPROVED", 2500.00)
c2 = ZZZClaim("5678", "PENDING", 800.00, "Awaiting police report")

print(c1.summarise())
print(c2.summarise())

print("\n=== AI Dev Use Case — Typed Functions ===")
# Type hints make AI dev code much more readable and maintainable

def build_prompt(
    question: str,
    context: list[str],
    company: str = "ZZZ Insurance",
    tone: str = "professional",
    max_words: int = 100
) -> str:
    """Build a structured RAG prompt with retrieved context."""
    context_text = "\n".join(f"- {c}" for c in context)
    return (
        f"You are a {tone} assistant for {company}.\n"
        f"Answer in under {max_words} words.\n\n"
        f"Context:\n{context_text}\n\n"
        f"Question: {question}"
    )

def parse_llm_response(response: dict[str, Any]) -> tuple[str, str, float]:
    """
    Parse LLM structured response.

    Returns:
        Tuple of (category, priority, confidence)
    """
    category: str = response.get("category", "GENERAL")
    priority: str = response.get("priority", "NORMAL")
    confidence: float = float(response.get("confidence", 0.0))
    return category, priority, confidence

# Test
context = [
    "ZZZ covers flood damage with Premium add-on",
    "Claims must be filed within 48 hours",
    "Maximum claim amount is $50,000"
]

prompt = build_prompt(
    question="Does my policy cover flood damage?",
    context=context,
    tone="friendly"
)
print("Built prompt:")
print(prompt)

# Parse response
response = {"category": "CLAIMS", "priority": "NORMAL", "confidence": 0.95}
category, priority, confidence = parse_llm_response(response)
print(f"\nParsed: {category} | {priority} | {confidence:.0%} confidence")