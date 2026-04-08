# ===== TOPIC 1: VARIABLES & DATA TYPES =====

# Basic variables
name = "John"
age = 20
height = 5.11
is_developer = True
no_value = None

# Print values and their types
print("=== Basic Variables ===")
print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Is Developer: {is_developer}, Type: {type(is_developer)}")
print(f"No Value: {no_value}, Type: {type(no_value)}")

# Type conversion
print("\n=== Type Conversion ===")
age_as_string = str(age)
print(f"Age as string: {age_as_string}, Type: {type(age_as_string)}")

price = "29.99"
price_as_float = float(price)
print(f"Price as float: {price_as_float}, Type: {type(price_as_float)}")

# Dynamic typing — Python allows reassigning to different types
print("\n=== Dynamic Typing ===")
x = 10
print(f"x = {x}, Type: {type(x)}")
x = "hello"
print(f"x = {x}, Type: {type(x)}")
x = True
print(f"x = {x}, Type: {type(x)}")

# Checking types
print("\n=== Type Checking ===")
print(f"Is name a string? {isinstance(name, str)}")
print(f"Is age an int? {isinstance(age, int)}")
print(f"Is height a float? {isinstance(height, float)}")