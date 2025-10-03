#!/usr/bin/env python3
"""
01_variables.py

This file demonstrates the four basic data types in Python:
- int (integers/whole numbers)
- float (floating-point/decimal numbers)
- string (text)
- bool (boolean - True or False)

Variables are like containers that store information.
You can create a variable by giving it a name and assigning it a value using =
"""

# ============================================================================
# INTEGER (int) - Whole numbers without decimal points
# ============================================================================

# Create an integer variable called 'age'
age = 25
print("Age:", age)  # Output: Age: 25
print("Type of age:", type(age))  # type() tells us what kind of data it is

# Integers can be positive, negative, or zero
score = 100
temperature = -5
zero = 0

print("\nInteger examples:")
print("Score:", score)
print("Temperature:", temperature)
print("Zero:", zero)

# You can do math with integers
sum_result = 10 + 5  # Addition
difference = 10 - 3  # Subtraction
product = 4 * 7      # Multiplication
quotient = 20 // 4   # Integer division (gives whole number result)

print("\nMath with integers:")
print("10 + 5 =", sum_result)
print("10 - 3 =", difference)
print("4 * 7 =", product)
print("20 // 4 =", quotient)


# ============================================================================
# FLOAT (float) - Numbers with decimal points
# ============================================================================

# Create a float variable called 'pi'
pi = 3.14159
print("\n\nPi:", pi)
print("Type of pi:", type(pi))

# Floats are used when you need precision with decimals
height = 5.9     # Height in feet
price = 19.99    # Price in dollars
temperature_celsius = 36.6  # Body temperature

print("\nFloat examples:")
print("Height:", height, "feet")
print("Price: $", price)
print("Temperature:", temperature_celsius, "°C")

# Math with floats
result1 = 10.5 + 2.3  # Addition with floats
result2 = 7.5 - 1.2   # Subtraction with floats
result3 = 3.0 * 2.5   # Multiplication with floats
result4 = 9.0 / 2.0   # Division with floats (always gives float result)

print("\nMath with floats:")
print("10.5 + 2.3 =", result1)
print("7.5 - 1.2 =", result2)
print("3.0 * 2.5 =", result3)
print("9.0 / 2.0 =", result4)


# ============================================================================
# STRING (str) - Text data enclosed in quotes
# ============================================================================

# Create a string variable called 'name'
# You can use single quotes ' ' or double quotes " "
name = "Alice"
print("\n\nName:", name)
print("Type of name:", type(name))

# Strings can contain letters, numbers, spaces, and special characters
greeting = "Hello, World!"
address = '123 Main Street'
message = "I am learning Python!"

print("\nString examples:")
print(greeting)
print("Address:", address)
print(message)

# You can combine (concatenate) strings with +
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Notice the space in the middle
print("\nCombining strings:")
print("Full name:", full_name)

# You can repeat strings with *
laugh = "Ha" * 3  # Repeats "Ha" three times
print("Laugh:", laugh)  # Output: HaHaHa

# Strings have many useful methods (functions that work on strings)
sentence = "python is awesome"
print("\nString methods:")
print("Original:", sentence)
print("Uppercase:", sentence.upper())  # Converts to UPPERCASE
print("Capitalized:", sentence.capitalize())  # Capitalizes first letter
print("Length:", len(sentence))  # len() gives the number of characters


# ============================================================================
# BOOLEAN (bool) - True or False values
# ============================================================================

# Create boolean variables
is_student = True
is_raining = False
print("\n\nIs student:", is_student)
print("Is raining:", is_raining)
print("Type of is_student:", type(is_student))

# Booleans are often the result of comparisons
is_greater = 10 > 5   # Is 10 greater than 5? True
is_equal = 7 == 7     # Is 7 equal to 7? True
is_less = 3 < 2       # Is 3 less than 2? False

print("\nBoolean comparisons:")
print("10 > 5:", is_greater)
print("7 == 7:", is_equal)
print("3 < 2:", is_less)

# More comparison operators:
print("\nMore comparisons:")
print("5 != 3:", 5 != 3)    # != means "not equal to"
print("8 >= 8:", 8 >= 8)    # >= means "greater than or equal to"
print("4 <= 2:", 4 <= 2)    # <= means "less than or equal to"

# You can use logical operators: and, or, not
has_ticket = True
has_id = True
can_enter = has_ticket and has_id  # Both must be True

print("\nLogical operators:")
print("Has ticket:", has_ticket)
print("Has ID:", has_id)
print("Can enter (needs both):", can_enter)

is_weekend = False
is_holiday = True
can_sleep_in = is_weekend or is_holiday  # At least one must be True

print("Is weekend:", is_weekend)
print("Is holiday:", is_holiday)
print("Can sleep in (needs one):", can_sleep_in)

is_awake = False
is_asleep = not is_awake  # not flips True to False and vice versa

print("Is awake:", is_awake)
print("Is asleep (opposite of awake):", is_asleep)


# ============================================================================
# VARIABLE NAMING RULES AND BEST PRACTICES
# ============================================================================

print("\n\n=== Variable Naming Tips ===")
print("✓ Use descriptive names: 'student_age' instead of 'x'")
print("✓ Use lowercase with underscores: 'first_name' not 'firstName'")
print("✓ Start with letter or underscore: 'name' or '_value'")
print("✗ Don't start with numbers: '1name' is invalid")
print("✗ Don't use Python keywords: 'if', 'for', 'while', etc.")
print("✗ Don't use spaces: 'my name' is invalid, use 'my_name'")


# ============================================================================
# SUMMARY
# ============================================================================

print("\n\n=== SUMMARY ===")
print("int: Whole numbers (no decimals)")
print("float: Numbers with decimals")
print("string: Text enclosed in quotes")
print("bool: True or False values")
print("\nYou can check any variable's type using type(variable_name)")
print("Variables can be reassigned to new values at any time!")
