#!/usr/bin/env python3
"""
03_functions.py

This file demonstrates functions in Python:
- Defining functions
- Function parameters/arguments
- Return values
- Why functions are useful

Functions are reusable blocks of code that perform specific tasks.
Think of them as mini-programs within your program!
"""

# ============================================================================
# BASIC FUNCTIONS - No parameters, no return value
# ============================================================================

print("=== BASIC FUNCTIONS ===\n")

# Define a simple function using 'def' keyword
# This function just prints a greeting
def greet():
    """This is a docstring - it describes what the function does."""
    print("Hello! Welcome to Python functions!")

# Call (use) the function by writing its name with ()
greet()  # Output: Hello! Welcome to Python functions!

print()

# Another simple function
def say_goodbye():
    """Prints a goodbye message."""
    print("Goodbye!")
    print("Thanks for learning functions!")

say_goodbye()  # Calls the function

print("\n")


# ============================================================================
# FUNCTIONS WITH PARAMETERS - Accept input
# ============================================================================

print("=== FUNCTIONS WITH PARAMETERS ===\n")

# Function with one parameter
# Parameters are variables that receive values when the function is called
def greet_person(name):
    """Greets a person by name."""
    print(f"Hello, {name}! Nice to meet you!")

# Call the function with different arguments
greet_person("Alice")  # Output: Hello, Alice! Nice to meet you!
greet_person("Bob")    # Output: Hello, Bob! Nice to meet you!

print()

# Function with multiple parameters
def introduce(name, age, city):
    """Introduces a person with their name, age, and city."""
    print(f"Hi! My name is {name}.")
    print(f"I am {age} years old.")
    print(f"I live in {city}.")

# Call with multiple arguments (order matters!)
introduce("Charlie", 25, "New York")
print()
introduce("Diana", 30, "San Francisco")

print()

# Function with default parameter values
# If no argument is provided, the default value is used
def greet_with_title(name, title="Friend"):
    """Greets a person with an optional title."""
    print(f"Hello, {title} {name}!")

greet_with_title("Emma")  # Uses default title "Friend"
greet_with_title("Frank", "Dr.")  # Uses provided title "Dr."
greet_with_title("Grace", "Professor")

print("\n")


# ============================================================================
# FUNCTIONS WITH RETURN VALUES - Send back results
# ============================================================================

print("=== FUNCTIONS WITH RETURN VALUES ===\n")

# Function that returns a value
# 'return' sends a value back to whoever called the function
def add_numbers(a, b):
    """Adds two numbers and returns the result."""
    result = a + b
    return result  # Send the result back

# Call the function and store the returned value
sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")

# You can use the returned value directly
print(f"10 + 7 = {add_numbers(10, 7)}")

print()

# Function with multiple parameters and return value
def calculate_rectangle_area(length, width):
    """Calculates the area of a rectangle."""
    area = length * width
    return area

# Use the function
rectangle_area = calculate_rectangle_area(5, 3)
print(f"Rectangle area (5 × 3): {rectangle_area}")

print()

# Function that returns different values based on conditions
def check_even_or_odd(number):
    """Returns 'even' if number is even, 'odd' if odd."""
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Test the function
print(f"4 is {check_even_or_odd(4)}")
print(f"7 is {check_even_or_odd(7)}")

print()

# Function returning multiple values (as a tuple)
def get_min_max(numbers):
    """Returns both the minimum and maximum values from a list."""
    minimum = min(numbers)  # Built-in function to find smallest value
    maximum = max(numbers)  # Built-in function to find largest value
    return minimum, maximum  # Return both values

# Call the function and unpack the returned values
values = [10, 3, 45, 7, 23]
min_val, max_val = get_min_max(values)
print(f"In {values}:")
print(f"Minimum: {min_val}")
print(f"Maximum: {max_val}")

print("\n")


# ============================================================================
# PRACTICAL FUNCTION EXAMPLES
# ============================================================================

print("=== PRACTICAL EXAMPLES ===\n")

# Example 1: Temperature converter
def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

print()

# Example 2: Grade calculator
def calculate_grade(score):
    """Returns a letter grade based on numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

student_score = 85
grade = calculate_grade(student_score)
print(f"Score: {student_score} → Grade: {grade}")

print()

# Example 3: String formatter
def format_name(first_name, last_name):
    """Returns a formatted full name in title case."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()  # Capitalizes first letter of each word

formatted = format_name("john", "doe")
print(f"Formatted name: {formatted}")

print()

# Example 4: List operations
def get_list_statistics(numbers):
    """Returns statistics about a list of numbers."""
    total = sum(numbers)  # Sum of all numbers
    count = len(numbers)  # How many numbers
    average = total / count  # Calculate average
    
    print(f"Numbers: {numbers}")
    print(f"Total: {total}")
    print(f"Count: {count}")
    print(f"Average: {average}")
    
    return average  # Return just the average

scores = [85, 90, 78, 92, 88]
avg_score = get_list_statistics(scores)
print(f"The average score is: {avg_score}")

print("\n")


# ============================================================================
# FUNCTIONS CALLING OTHER FUNCTIONS
# ============================================================================

print("=== FUNCTIONS CALLING FUNCTIONS ===\n")

# Functions can call other functions!
def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def calculate_circle_area(radius):
    """Calculates the area of a circle using the formula: π × r²"""
    pi = 3.14159
    # Call multiply function to calculate radius squared
    radius_squared = multiply(radius, radius)
    area = multiply(pi, radius_squared)
    return area

circle_radius = 5
circle_area = calculate_circle_area(circle_radius)
print(f"Circle with radius {circle_radius} has area: {circle_area:.2f}")
# Note: {circle_area:.2f} formats the number to 2 decimal places

print("\n")


# ============================================================================
# VARIABLE SCOPE - Where variables exist
# ============================================================================

print("=== VARIABLE SCOPE ===\n")

# Global variable - can be accessed anywhere
global_message = "I'm global!"

def demo_scope():
    """Demonstrates local vs global variables."""
    # Local variable - only exists inside this function
    local_message = "I'm local!"
    
    print("Inside function:")
    print(f"  Local: {local_message}")
    print(f"  Global: {global_message}")

demo_scope()

print("\nOutside function:")
print(f"  Global: {global_message}")
print("  Local: Not accessible here! (Would cause an error)")

print("\n")


# ============================================================================
# WHY USE FUNCTIONS?
# ============================================================================

print("=== WHY USE FUNCTIONS? ===\n")

# Without functions - repetitive code
print("Without functions (repetitive):")
name1 = "Alice"
age1 = 25
print(f"{name1} will be {age1 + 1} next year")
print(f"{name1} will be {age1 + 5} in 5 years")

name2 = "Bob"
age2 = 30
print(f"{name2} will be {age2 + 1} next year")
print(f"{name2} will be {age2 + 5} in 5 years")

print()

# With functions - reusable, cleaner code
print("With functions (reusable):")

def calculate_future_age(name, current_age, years_ahead):
    """Calculates and displays future age."""
    future_age = current_age + years_ahead
    print(f"{name} will be {future_age} in {years_ahead} year(s)")

# Now we can reuse this function easily!
calculate_future_age("Alice", 25, 1)
calculate_future_age("Alice", 25, 5)
calculate_future_age("Bob", 30, 1)
calculate_future_age("Bob", 30, 5)

print("\n")


# ============================================================================
# FUNCTION BEST PRACTICES
# ============================================================================

print("=== FUNCTION BEST PRACTICES ===")
print("✓ Give functions descriptive names (use verbs like 'calculate', 'get', 'check')")
print("✓ Functions should do ONE thing and do it well")
print("✓ Use parameters to make functions flexible and reusable")
print("✓ Use return values to send results back")
print("✓ Add docstrings to explain what the function does")
print("✓ Keep functions short and simple (easier to understand and debug)")
print("✓ Use functions to avoid repeating code")


# ============================================================================
# SUMMARY
# ============================================================================

print("\n=== SUMMARY ===")
print("Functions are reusable blocks of code that:")
print("1. Are defined with 'def function_name():'")
print("2. Can accept parameters (input)")
print("3. Can return values (output)")
print("4. Help organize code and avoid repetition")
print("5. Make code easier to read, test, and maintain")
print("\nFunctions are one of the most important concepts in programming!")
