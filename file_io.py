# ===== TOPIC 13: FILE I/O =====

import json
import os
from pathlib import Path
from datetime import datetime

# Use current directory for all files
BASE_DIR = Path.cwd()

print("=== Writing Files ===")
# Write a simple text file
file_path = BASE_DIR / "test_output.txt"

with open(file_path, "w") as f:
    f.write("ZZZ Insurance AI Assistant\n")
    f.write("=" * 30 + "\n")
    f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

print(f"✅ Written to: {file_path}")

print("\n=== Reading Files ===")
# Read entire file at once
with open(file_path, "r") as f:
    content = f.read()
print(f"Full content:\n{content}")

# Read line by line
with open(file_path, "r") as f:
    lines = f.readlines()
print(f"Lines: {lines}")
print(f"Line count: {len(lines)}")

# Read line by line with loop — memory efficient for large files
print("Line by line:")
with open(file_path, "r") as f:
    for line in f:
        print(f"    {line.strip()}")

print("\n=== Appending to Files ===")
with open(file_path, "a") as f:
    f.write(f"Appended at: {datetime.now().strftime('%H:%M:%S')}\n")

with open(file_path, "r") as f:
    print(f.read())

print("\n=== Working with JSON Files ===")
# Save Python dict as JSON file
claim_data = {
    "claims": [
        {"id": "1234", "status": "APPROVED", "amount": 2500.00},
        {"id": "5678", "status": "PENDING", "amount": 800.00},
        {"id": "9999", "status": "REJECTED", "amount": 1200.00}
    ],
    "total": 3,
    "generated": datetime.now().strftime("%Y-%m-%d")
}

json_path = BASE_DIR / "claims.json"

# Write JSON
with open(json_path, "w") as f:
    json.dump(claim_data, f, indent=2)
print(f"✅ JSON written to: {json_path}")

# Read JSON
with open(json_path, "r") as f:
    loaded = json.load(f)

print(f"Total claims : {loaded['total']}")
print(f"Generated    : {loaded['generated']}")
for claim in loaded["claims"]:
    print(f"  {claim['id']}: {claim['status']} - ${claim['amount']:,.2f}")

print("\n=== Checking Files & Directories ===")
print(f"File exists  : {json_path.exists()}")
print(f"Is file      : {json_path.is_file()}")
print(f"File size    : {json_path.stat().st_size} bytes")

# List files in directory
print("\nPy files in current dir:")
for f in BASE_DIR.glob("*.py"):
    print(f"  {f.name}")

print("\n=== Safe File Handling with Exceptions ===")
def read_file_safely(filepath: str) -> str:
    """Read a file safely with proper error handling."""
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        return f"❌ File not found: {filepath}"
    except PermissionError:
        return f"❌ Permission denied: {filepath}"
    except Exception as e:
        return f"❌ Error reading file: {e}"

print(read_file_safely(str(file_path)))
print(read_file_safely("nonexistent.txt"))

print("\n=== AI Dev Use Case ===")
# Saving and loading conversation history
def save_conversation(session_id: str, history: list):
    """Save chat history to JSON file."""
    path = BASE_DIR / f"session_{session_id}.json"
    data = {
        "session_id": session_id,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "messages": history
    }
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Session saved: {path.name}")
    return path

def load_conversation(session_id: str) -> list:
    """Load chat history from JSON file."""
    path = BASE_DIR / f"session_{session_id}.json"
    try:
        with open(path, "r") as f:
            data = json.load(f)
        print(f"✅ Session loaded: {len(data['messages'])} messages")
        return data["messages"]
    except FileNotFoundError:
        print(f"⚠️  No session found for: {session_id}")
        return []

# Simulate a conversation
history = [
    {"role": "user", "content": "Check claim 1234"},
    {"role": "assistant", "content": "Claim 1234 is APPROVED for $2,500"},
    {"role": "user", "content": "What is my premium?"},
    {"role": "assistant", "content": "Your premium is $120/month"}
]

# Save it
save_conversation("john_001", history)

# Load it back
loaded_history = load_conversation("john_001")
print("\nLoaded conversation:")
for msg in loaded_history:
    icon = "👤" if msg["role"] == "user" else "🤖"
    print(f"  {icon} {msg['content']}")


# Cleanup test files
print("\n=== Cleanup ===")
for test_file in ["test_output.txt", "claims.json", "session_john_001.json"]:
    path = BASE_DIR / test_file
    if path.exists():
        path.unlink()   # delete file — like Java's File.delete()
        print(f"  🗑️  Deleted: {test_file}")