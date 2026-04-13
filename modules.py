# ===== TOPIC 12: MODULES & IMPORTS =====

print("=== Importing Standard Library Modules ===")
import os
import sys
import json
import math
import random
from datetime import date, datetime
from pathlib import Path

# os - file system and environment
print(f"Curent dir           : {os.getcwd()}")
print(f"Python version       : {sys.version[:6]}")
print(f"Path separator       : {os.sep}")

print("\n=== os module ===")
# Environment variables — critical for AI dev (.env files)
os.environ["MY_TEST_VAR"] = "<<My Test Variable value is set here>>"
print(f"Env var set    : {os.environ.get('MY_TEST_VAR')}")
print(f"Env var missing: {os.environ.get('MISSING_VAR', 'default_value')}")

# Path operations
current = os.getcwd()
joined = os.path.join(current, "documents", "policy.txt")
print(f"Joined path     : {joined}")
print(f"Path exists     : {os.path.exists(joined)}")
print(f"Is directory    : {os.path.isdir(current)}")

print("\n=== pathlib — Modern Path Handling ===")
# pathlib is the modern way — cleaner than os.path
p = Path.cwd()
print(f"Current dir : {p}")
print(f"Parent dir  : {p.parent}")
print(f"Home dir    : {Path.home()}")

# Building paths with / operator — very clean!
config_path = Path.home() / "dev" / "py-developer" / "modules.py"
print(f"Config path : {config_path}")
print(f"File exists : {config_path.exists()}")
print(f"File name   : {config_path.name}")
print(f"Extension   : {config_path.suffix}")

print("\n=== json module ===")
# Convert Python dict to JSON string
claim = {
    "claim_id": "1234",
    "status": "APPROVED",
    "amount": 2500.00,
    "customer": {"name": "John", "email": "john@email.com"}
}

json_string = json.dumps(claim, indent=2)
print(f"Dict to JSON:\n{json_string}")

# Convert JSON string back to Python dict
parsed = json.loads(json_string)
print(f"\nJSON to Dict: {parsed['customer']['name']}")

print("\n=== datetime module ===")
now = datetime.now()
today = date.today()

print(f"Now          : {now}")
print(f"Today        : {today}")
print(f"Formatted    : {now.strftime('%d %B %Y %H:%M')}")
print(f"Year         : {now.year}")
print(f"Month        : {now.month}")
print(f"Day          : {now.day}")

# Date arithmetic — useful for policy expiry checks
from datetime import timedelta
expiry = today + timedelta(days=365)
print(f"Policy expiry: {expiry}")

days_left = (expiry - today).days
print(f"Days to expiry: {days_left}")

print("\n=== math & random ===")
print(f"Pi          : {math.pi:.4f}")
print(f"Square root : {math.sqrt(144)}")
print(f"Power       : {math.pow(2, 10)}")
print(f"Ceiling     : {math.ceil(4.2)}")
print(f"Floor       : {math.floor(4.8)}")

random.seed(42)     # seed for reproducibility
print(f"\nRandom int  : {random.randint(1, 100)}")
print(f"Random float: {random.random():.4f}")
items = ["Python", "Java", "LangChain", "Docker"]
print(f"Random choice: {random.choice(items)}")
random.shuffle(items)
print(f"Shuffled    : {items}")

print("\n=== Creating Your Own Module ===")
print("Module structure for zzz-ai-assistant:")
modules = {
    "app.py": "Main entry point",
    "agent.py": "Agent setup",
    "tools.py": "Agent tools",
    "rag.py": "RAG pipeline",
}
for module, purpose in modules.items():
    print(f"    {module:<10} -> {purpose}")

print("\n=== AI Dev Use Case ===")
# Real pattern — loading config from environment
def load_ai_config() -> dict:
    """Load AI configuration from environment variables."""
    config = {
        "openai_api_key": os.environ.get("OPENAI_API_KEY", "not_set"),
        "model": os.environ.get("AI_MODEL", "gpt-4o-mini"),
        "temperature": float(os.environ.get("AI_TEMPERATURE", "0.7")),
        "max_tokens": int(os.environ.get("AI_MAX_TOKENS", "1000")),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return config

config = load_ai_config()
print("AI Config loaded:")
for key, value in config.items():
    # Mask API key for security
    if "key" in key:
        value = value[:8] + "..." if value != "not_set" else "not_set"
    print(f"  {key:<20}: {value}")