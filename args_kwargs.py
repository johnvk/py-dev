# ===== TOPIC 8: *args & **kwargs =====

print("=== *args — Variable Positional Arguments ===")
def add(*args):
    print(f"  args tuple: {args}")
    return sum(args)

print(f"add(1,2)       : {add(1, 2)}")
print(f"add(1,2,3)     : {add(1, 2, 3)}")
print(f"add(1,2,3,4,5) : {add(1, 2, 3, 4, 5)}")

print("\n=== *args with required params ===")
def greet(greeting, *names):
    for name in names:
        print(f"   {greeting}, {name}!")

greet("Hello", "John")
greet("hola", "Tom", "Steve", "Ron")

print("\n=== **kwargs — Variable Keyword Arguments ===")
def display_config(**kwargs):
    print(f"   kwargs dict: {kwargs}")
    for key, value in kwargs.items():
        print(f"   - {key:<15}: {value}")

display_config(model="gpt-4o-mini", temperature=0.7, max_tokens=1000)
print()
display_config(name="John", role="AI Developer", company="ZZZ Insurance")

print("\n=== **kwargs with required params ===")
def create_ticket(ticket_id, priority, **details):
    print(f"  ID       : {ticket_id}")
    print(f"  Priority : {priority}")
    print(f"  Details  : {details}")

create_ticket("T001", "URGENT", customer="John", issue="App down")
print()
create_ticket("T002", "LOW", customer="Jane", issue="Email update", channel="web")

print("\n=== Both *args and **kwargs ===")
def log(*args, **kwargs):
    print(f"  Messages : {args}")
    print(f"  Metadata : {kwargs}")

log("System started", "Agent ready",
    timestamp="2026-04-08", user="John")

print("\n=== ** Unpacking Operator ===")
# Unpack dict into function arguments
def configure_llm(model, temperature, max_tokens, streaming=False):
    print(f"  Model      : {model}")
    print(f"  Temperature: {temperature}")
    print(f"  Max tokens : {max_tokens}")
    print(f"  Streaming  : {streaming}")

# Instead of passing each argument manually
config = {
    "model": "gpt-4o-mini",
    "temperature": 0.2,
    "max_tokens": 500,
    "streaming": True
}

print("Unpacking dict into function:")
configure_llm(**config)   # same as configure_llm(model=..., temperature=..., ...)

print("\n=== Merging Dictionaries ===")
defaults = {"temperature": 0.7, "max_tokens": 1000, "model": "gpt-4o-mini"}
overrides = {"temperature": 0.2, "max_tokens": 500}
merged = {**defaults, **overrides}
print(f"  Defaults        : {defaults}")
print(f"  Overrides       : {overrides}")
print(f"  Merged          : {merged}")

print("\n=== AI Dev Use Case ===")
# Building flexible LLM config — exactly how LangChain works internally
def call_llm(prompt, **llm_config):
    """
    Call LLM with flexible configuration.
    Any extra kwargs get passed to the model.
    """
    model = llm_config.get("model", "gpt-4o-mini")
    temperature = llm_config.get("temperature", 0.7)
    max_tokens = llm_config.get("max_tokens", 1000)

    print(f"  Calling {model}")
    print(f"  Temperature : {temperature}")
    print(f"  Max tokens  : {max_tokens}")
    print(f"  Prompt      : {prompt[:50]}...")

# Call with different configs
print("Default config:")
call_llm("What does my ZZZ policy cover?")

print("\nCustom config:")
call_llm(
    "Classify this ticket urgently",
    model="gpt-4o",
    temperature=0.1,
    max_tokens=100
)
