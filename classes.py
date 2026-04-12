# ===== TOPIC 11: CLASSES & OOP =====

print("=== Basic Class ===")
class Person:
    def __init__(self, name: str, age: int, role: str = "Developer"):
        self.name = name
        self.age = age
        self.role = role

    def greet(self) -> str:
        return f"Hi I'm {self.name}, {self.role}, age {self.age}"

    def is_senior(self) -> bool:
        return self.age >= 30

    def __str__(self) -> str:
        """Called when you print() the object — like Java's toString()"""
        return f"Person({self.name}, {self.age}, {self.role})"

    def __repr__(self) -> str:
        """Developer-friendly representation"""
        return f"Person(name='{self.name}', age={self.age}, role='{self.role}')"

john = Person("John", 45, "Python Developer")
jane = Person("Jane", 28)

print(john.greet())
print(jane.greet())
print(f"John is senior: {john.is_senior()}")
print(f"Jane is senior: {jane.is_senior()}")
print(f"str()  : {john}")
print(f"repr() : {repr(john)}")

print("\n=== Class Variables vs Instance Variables ===")
class ZZZPolicy:
    # Class variable — shared across ALL instances (like Java's static)
    company = "ZZZ Insurance"
    total_policies = 0

    def __init__(self, policy_id: str, policy_type: str, premium: float):
        # Instance variables — unique to each instance
        self.policy_id = policy_id
        self.policy_type = policy_type
        self.premium = premium
        ZZZPolicy.total_policies += 1   # increment class variable

    def describe(self) -> str:
        return (f"{self.company} | {self.policy_id} | "
                f"{self.policy_type} | ${self.premium}/month")

p1 = ZZZPolicy("POL001", "Comprehensive", 120.00)
p2 = ZZZPolicy("POL002", "Third Party", 60.00)
p3 = ZZZPolicy("POL003", "Comprehensive", 140.00)

print(p1.describe())
print(p2.describe())
print(f"Total policies created: {ZZZPolicy.total_policies}")

print("\n=== Inheritance ===")
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return f"{self.name} makes a sound"

    def describe(self) -> str:
        return f"I am {self.name}"

# Inherits from Animal — like Java's extends
class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)      # calls parent __init__ — like Java's super()
        self.breed = breed

    def speak(self) -> str:         # override parent method
        return f"{self.name} says Woof!"

    def describe(self) -> str:
        return f"I am {self.name}, a {self.breed}"

class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says Meow!"

dog = Dog("Rex", "Labrador")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())
print(dog.describe())
print(cat.describe())

# isinstance checks — like Java's instanceof
print(f"\nisinstance(dog, Dog)    : {isinstance(dog, Dog)}")
print(f"isinstance(dog, Animal) : {isinstance(dog, Animal)}")
print(f"isinstance(cat, Dog)    : {isinstance(cat, Dog)}")

print("\n=== Polymorphism ===")
# Same method, different behaviour — like Java polymorphism
animals = [Dog("Rex", "Labrador"), Cat("Whiskers"), Dog("Buddy", "Poodle")]

for animal in animals:
    print(f"  {animal.speak()}")    # calls correct speak() for each type

print("\n=== AI Dev Use Case — Modelling ZZZ Assistant ===")
class BaseAgent:
    """Base class for all ZZZ Insurance agents"""

    def __init__(self, name: str, model: str = "gpt-4o-mini"):
        self.name = name
        self.model = model
        self.chat_history = []

    def add_to_history(self, role: str, content: str):
        self.chat_history.append({"role": role, "content": content})

    def get_history(self) -> list:
        return self.chat_history

    def process(self, message: str) -> str:
        raise NotImplementedError("Subclasses must implement process()")

    def __str__(self):
        return f"{self.name} (model={self.model})"


class ClaimsAgent(BaseAgent):
    """Specialised agent for handling claims"""

    def __init__(self):
        super().__init__(name="Claims Agent", model="gpt-4o-mini")
        self.claims_handled = 0

    def process(self, message: str) -> str:
        self.claims_handled += 1
        self.add_to_history("user", message)
        response = f"Claims Agent handling: '{message}'"
        self.add_to_history("assistant", response)
        return response


class BillingAgent(BaseAgent):
    """Specialised agent for handling billing"""

    def __init__(self):
        super().__init__(name="Billing Agent", model="gpt-4o-mini")

    def process(self, message: str) -> str:
        self.add_to_history("user", message)
        response = f"Billing Agent handling: '{message}'"
        self.add_to_history("assistant", response)
        return response


# Test the agents
claims = ClaimsAgent()
billing = BillingAgent()

print(f"Agent 1: {claims}")
print(f"Agent 2: {billing}")

print(f"\nClaims responses:")
print(f"  {claims.process('Check claim 1234')}")
print(f"  {claims.process('File new claim')}")
print(f"  Claims handled: {claims.claims_handled}")

print(f"\nBilling responses:")
print(f"  {billing.process('Why is my premium high?')}")

print(f"\nClaims history:")
for msg in claims.get_history():
    print(f"  [{msg['role']}]: {msg['content']}")