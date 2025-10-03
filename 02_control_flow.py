#!/usr/bin/env python3
"""
02_control_flow.py

This file demonstrates control flow in Python:
- if/else statements (making decisions)
- for loops (repeating actions a specific number of times)
- while loops (repeating actions while a condition is true)

Control flow allows your program to make decisions and repeat actions.
"""

# ============================================================================
# IF/ELSE STATEMENTS - Making decisions in code
# ============================================================================

print("=== IF/ELSE STATEMENTS ===\n")

# Simple if statement
# This checks a condition and runs code only if the condition is True
age = 18

if age >= 18:
    print("You are an adult.")  # This runs because 18 >= 18 is True
    print("You can vote!")

print()  # Empty line for spacing

# if/else statement
# This runs one block of code if True, another if False
temperature = 75

if temperature > 80:
    print("It's hot outside!")
else:
    print("It's not too hot.")  # This runs because 75 is not > 80

print()

# if/elif/else statement
# elif means "else if" - check multiple conditions
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # This runs because score is 85 (>= 80 but < 90)
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

print()

# You can combine conditions with 'and' and 'or'
has_ticket = True
has_id = True

if has_ticket and has_id:
    print("Welcome! You can enter.")  # Both conditions must be True
else:
    print("Sorry, you cannot enter.")

print()

# Example with 'or' - at least one condition must be True
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("Yay! No work today!")  # This runs because is_holiday is True
else:
    print("Time to go to work!")

print()

# Nested if statements (if inside another if)
is_raining = True
has_umbrella = True

if is_raining:
    print("It's raining.")
    if has_umbrella:
        print("Good thing you have an umbrella!")  # This runs
    else:
        print("You'll get wet!")
else:
    print("It's not raining.")

print("\n")


# ============================================================================
# FOR LOOPS - Repeating actions a specific number of times
# ============================================================================

print("=== FOR LOOPS ===\n")

# Basic for loop - repeat 5 times
# range(5) creates numbers from 0 to 4 (5 numbers total)
print("Counting from 0 to 4:")
for i in range(5):
    print("Count:", i)

print()

# range() with start and end
# range(1, 6) creates numbers from 1 to 5 (stops before 6)
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

print()

# range() with start, end, and step
# range(0, 11, 2) creates numbers from 0 to 10, counting by 2
print("Even numbers from 0 to 10:")
for num in range(0, 11, 2):
    print(num)

print()

# Loop through a list of items
fruits = ["apple", "banana", "orange", "grape"]
print("My favorite fruits:")
for fruit in fruits:
    print("- " + fruit)

print()

# Loop through a string (strings are sequences of characters)
word = "Python"
print("Letters in 'Python':")
for letter in word:
    print(letter)

print()

# Using enumerate() to get both index and value
colors = ["red", "green", "blue"]
print("Colors with their positions:")
for index, color in enumerate(colors):
    print(f"Position {index}: {color}")
    # Note: f"..." is an f-string, a way to insert variables into strings

print()

# Nested loops (loop inside another loop)
print("Multiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} × {j} = {result}")
    print()  # Empty line after each number's table

print()


# ============================================================================
# WHILE LOOPS - Repeating while a condition is true
# ============================================================================

print("=== WHILE LOOPS ===\n")

# Basic while loop
# Keeps running as long as the condition is True
count = 1
print("Counting up to 5:")
while count <= 5:
    print("Count:", count)
    count += 1  # Increment count by 1 (same as count = count + 1)
    # IMPORTANT: You must change the variable, or the loop runs forever!

print()

# Counting down
countdown = 5
print("Countdown:")
while countdown > 0:
    print(countdown)
    countdown -= 1  # Decrement by 1 (same as countdown = countdown - 1)
print("Blast off! 🚀")

print()

# While loop with user input simulation
# In real programs, you might get input from the user
password = ""
attempts = 0
correct_password = "python123"

# Simulate trying to enter password (in real code, you'd use input())
attempts_data = ["wrong1", "wrong2", "python123"]  # Pretend user inputs

print("Password entry simulation:")
for attempt_input in attempts_data:
    attempts += 1
    password = attempt_input
    print(f"Attempt {attempts}: Trying password '{password}'")
    
    if password == correct_password:
        print("Access granted! ✓")
        break  # 'break' exits the loop immediately
    else:
        print("Incorrect password. Try again.")

print()

# Using 'continue' to skip to the next iteration
print("Printing odd numbers from 1 to 10 (using continue):")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:  # If number is even (divisible by 2)
        continue  # Skip the rest and go to next iteration
    print(num)  # This only runs for odd numbers

print()

# While loop with a flag variable
print("Finding a specific number:")
numbers = [3, 7, 12, 19, 24, 31]
target = 19
found = False
index = 0

while index < len(numbers) and not found:
    if numbers[index] == target:
        print(f"Found {target} at position {index}!")
        found = True
    else:
        print(f"Position {index}: {numbers[index]} (not the target)")
    index += 1

if not found:
    print(f"{target} not found in the list.")

print("\n")


# ============================================================================
# CONTROL FLOW BEST PRACTICES
# ============================================================================

print("=== CONTROL FLOW TIPS ===")
print("✓ Use if/elif/else for making decisions based on conditions")
print("✓ Use for loops when you know how many times to repeat")
print("✓ Use while loops when you repeat until a condition changes")
print("✓ Always ensure while loops have a way to end (avoid infinite loops)")
print("✓ Use 'break' to exit a loop early")
print("✓ Use 'continue' to skip to the next iteration")
print("✓ Indent your code properly - Python requires correct indentation!")


# ============================================================================
# SUMMARY
# ============================================================================

print("\n=== SUMMARY ===")
print("if/else: Make decisions - run different code based on conditions")
print("for loop: Repeat code a specific number of times or for each item")
print("while loop: Repeat code as long as a condition is True")
print("break: Exit a loop immediately")
print("continue: Skip to the next iteration of a loop")
print("\nControl flow makes your programs smart and flexible!")
