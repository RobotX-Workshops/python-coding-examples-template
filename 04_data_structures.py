#!/usr/bin/env python3
"""
04_data_structures.py

This file demonstrates two fundamental data structures in Python:
- Lists: Ordered, changeable collections of items
- Dictionaries: Key-value pairs for organizing related data

Data structures help you organize and store multiple pieces of data efficiently.
"""

# ============================================================================
# LISTS - Ordered collections of items
# ============================================================================

print("=== LISTS ===\n")

# Creating a list
# Lists are created using square brackets []
# Items are separated by commas
fruits = ["apple", "banana", "orange", "grape"]
print("List of fruits:", fruits)
print("Type:", type(fruits))

print()

# Lists can contain different data types
mixed_list = [1, "hello", 3.14, True]
print("Mixed list:", mixed_list)

print()

# Creating an empty list
empty_list = []
print("Empty list:", empty_list)

print("\n")


# ============================================================================
# ACCESSING LIST ITEMS - Using index numbers
# ============================================================================

print("=== ACCESSING LIST ITEMS ===\n")

# Lists are indexed starting from 0
# First item is at index 0, second at index 1, etc.
colors = ["red", "green", "blue", "yellow"]

print("All colors:", colors)
print("First color (index 0):", colors[0])  # red
print("Second color (index 1):", colors[1])  # green
print("Third color (index 2):", colors[2])   # blue
print("Fourth color (index 3):", colors[3])  # yellow

print()

# Negative indices count from the end
# -1 is the last item, -2 is second-to-last, etc.
print("Last color (index -1):", colors[-1])    # yellow
print("Second-to-last (index -2):", colors[-2])  # blue

print()

# List slicing - get a portion of the list
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("All numbers:", numbers)
print("First 3 items [0:3]:", numbers[0:3])  # [0, 1, 2] - stops before index 3
print("Items 3 to 6 [3:6]:", numbers[3:6])   # [3, 4, 5] - stops before index 6
print("From index 5 to end [5:]:", numbers[5:])  # [5, 6, 7, 8, 9]
print("Up to index 4 [:4]:", numbers[:4])    # [0, 1, 2, 3]

print("\n")


# ============================================================================
# MODIFYING LISTS - Change, add, and remove items
# ============================================================================

print("=== MODIFYING LISTS ===\n")

# Lists are mutable (changeable)
fruits = ["apple", "banana", "orange"]
print("Original list:", fruits)

# Change an item by index
fruits[1] = "strawberry"  # Replace "banana" with "strawberry"
print("After changing index 1:", fruits)

print()

# Add items to a list
shopping_list = ["milk", "eggs"]
print("Shopping list:", shopping_list)

# append() adds an item to the end
shopping_list.append("bread")
print("After appending 'bread':", shopping_list)

# insert() adds an item at a specific position
shopping_list.insert(1, "cheese")  # Insert "cheese" at index 1
print("After inserting 'cheese' at index 1:", shopping_list)

print()

# Remove items from a list
tasks = ["homework", "laundry", "shopping", "cleaning"]
print("Tasks:", tasks)

# remove() removes the first occurrence of a value
tasks.remove("shopping")
print("After removing 'shopping':", tasks)

# pop() removes and returns an item by index (default: last item)
last_task = tasks.pop()  # Removes last item
print(f"Popped '{last_task}':", tasks)

first_task = tasks.pop(0)  # Removes first item (index 0)
print(f"Popped '{first_task}':", tasks)

print("\n")


# ============================================================================
# LIST OPERATIONS AND METHODS
# ============================================================================

print("=== LIST OPERATIONS ===\n")

# Length of a list
numbers = [10, 20, 30, 40, 50]
print("Numbers:", numbers)
print("Length:", len(numbers))  # How many items in the list

print()

# Check if item exists in list
fruits = ["apple", "banana", "orange"]
print("Fruits:", fruits)
print("Is 'banana' in list?", "banana" in fruits)  # True
print("Is 'grape' in list?", "grape" in fruits)    # False

print()

# Sorting a list
unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
print("Original list:", unsorted)

# sort() modifies the list in place
unsorted.sort()
print("After sort():", unsorted)

# sorted() returns a new sorted list (doesn't modify original)
names = ["Charlie", "Alice", "Bob"]
sorted_names = sorted(names)
print("Original names:", names)
print("Sorted names:", sorted_names)

print()

# Reverse a list
numbers = [1, 2, 3, 4, 5]
print("Original:", numbers)
numbers.reverse()
print("After reverse():", numbers)

print()

# List concatenation (combining lists)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"{list1} + {list2} = {combined}")

print()

# List repetition
pattern = ["A", "B"]
repeated = pattern * 3  # Repeat the list 3 times
print(f"{pattern} * 3 = {repeated}")

print("\n")


# ============================================================================
# LOOPING THROUGH LISTS
# ============================================================================

print("=== LOOPING THROUGH LISTS ===\n")

# Use a for loop to access each item
pets = ["dog", "cat", "fish", "bird"]
print("My pets:")
for pet in pets:
    print(f"- {pet}")

print()

# Loop with index using enumerate()
scores = [85, 92, 78, 95]
print("Test scores:")
for index, score in enumerate(scores):
    print(f"Test {index + 1}: {score}")

print("\n")


# ============================================================================
# LIST COMPREHENSIONS - Create lists efficiently
# ============================================================================

print("=== LIST COMPREHENSIONS ===\n")

# Traditional way: create a list of squares
squares = []
for i in range(1, 6):
    squares.append(i * i)
print("Squares (traditional way):", squares)

# List comprehension: more concise way
squares = [i * i for i in range(1, 6)]
print("Squares (list comprehension):", squares)

print()

# List comprehension with condition
# Get only even numbers from 0 to 10
evens = [num for num in range(11) if num % 2 == 0]
print("Even numbers:", evens)

print("\n")


# ============================================================================
# DICTIONARIES - Key-value pairs
# ============================================================================

print("=== DICTIONARIES ===\n")

# Creating a dictionary
# Dictionaries use curly braces {} with key:value pairs
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "enrolled": True
}

print("Student dictionary:", student)
print("Type:", type(student))

print()

# Creating an empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)

print("\n")


# ============================================================================
# ACCESSING DICTIONARY VALUES - Using keys
# ============================================================================

print("=== ACCESSING DICTIONARY VALUES ===\n")

# Access values using keys in square brackets
person = {
    "name": "Bob",
    "age": 25,
    "city": "New York"
}

print("Person:", person)
print("Name:", person["name"])  # Access value with key "name"
print("Age:", person["age"])
print("City:", person["city"])

print()

# Using get() method (safer - doesn't error if key doesn't exist)
print("Name (using get):", person.get("name"))
print("Country (using get):", person.get("country", "Not specified"))
# get() with default value: if key doesn't exist, returns the default

print("\n")


# ============================================================================
# MODIFYING DICTIONARIES - Add, change, and remove items
# ============================================================================

print("=== MODIFYING DICTIONARIES ===\n")

# Dictionaries are mutable (changeable)
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020
}

print("Original car:", car)

# Change a value
car["year"] = 2021  # Update the year
print("After changing year:", car)

print()

# Add a new key-value pair
car["color"] = "blue"  # Add new key "color"
print("After adding color:", car)

print()

# Remove a key-value pair
car.pop("model")  # Remove the "model" key
print("After removing model:", car)

# Alternative: use del
del car["year"]
print("After deleting year:", car)

print("\n")


# ============================================================================
# DICTIONARY METHODS AND OPERATIONS
# ============================================================================

print("=== DICTIONARY METHODS ===\n")

book = {
    "title": "Python Basics",
    "author": "John Doe",
    "pages": 300,
    "rating": 4.5
}

print("Book:", book)

# Get all keys
print("Keys:", list(book.keys()))

# Get all values
print("Values:", list(book.values()))

# Get all key-value pairs as tuples
print("Items:", list(book.items()))

print()

# Check if key exists
print("Does 'title' exist?", "title" in book)  # True
print("Does 'price' exist?", "price" in book)  # False

print()

# Length of dictionary (number of key-value pairs)
print("Number of items:", len(book))

print("\n")


# ============================================================================
# LOOPING THROUGH DICTIONARIES
# ============================================================================

print("=== LOOPING THROUGH DICTIONARIES ===\n")

scores = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92
}

# Loop through keys
print("Students:")
for name in scores:
    print(f"- {name}")

print()

# Loop through key-value pairs
print("Scores:")
for name, score in scores.items():
    print(f"{name}: {score}")

print("\n")


# ============================================================================
# NESTED DATA STRUCTURES - Lists in dictionaries, dictionaries in lists
# ============================================================================

print("=== NESTED DATA STRUCTURES ===\n")

# Dictionary containing a list
student = {
    "name": "Diana",
    "grades": [85, 90, 88, 92],  # List inside dictionary
    "subjects": ["Math", "Science", "English"]
}

print("Student:", student)
print("Name:", student["name"])
print("Grades:", student["grades"])
print("First grade:", student["grades"][0])  # Access list item

print()

# List of dictionaries
students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 21, "grade": "B"},
    {"name": "Charlie", "age": 19, "grade": "A"}
]

print("All students:")
for student in students:
    print(f"  {student['name']}, age {student['age']}, grade {student['grade']}")

print("\n")


# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

print("=== PRACTICAL EXAMPLES ===\n")

# Example 1: Phonebook using dictionary
phonebook = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}

print("Phonebook:")
for name, number in phonebook.items():
    print(f"{name}: {number}")

print()

# Example 2: Inventory using dictionary
inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 45
}

print("Inventory:")
for item, quantity in inventory.items():
    print(f"{item.capitalize()}: {quantity}")

# Add to inventory
inventory["bananas"] += 20  # Add 20 bananas
print(f"After restocking bananas: {inventory['bananas']}")

print()

# Example 3: Student grade tracker using nested structures
classroom = {
    "students": ["Alice", "Bob", "Charlie"],
    "grades": {
        "Alice": [85, 90, 88],
        "Bob": [78, 82, 85],
        "Charlie": [92, 95, 90]
    }
}

print("Grade Report:")
for student in classroom["students"]:
    grades = classroom["grades"][student]
    average = sum(grades) / len(grades)
    print(f"{student}: {grades} → Average: {average:.1f}")

print("\n")


# ============================================================================
# CHOOSING BETWEEN LISTS AND DICTIONARIES
# ============================================================================

print("=== WHEN TO USE LISTS VS DICTIONARIES ===")
print("\nUse LISTS when:")
print("  ✓ You have a sequence of items")
print("  ✓ Order matters")
print("  ✓ You need to access items by position/index")
print("  ✓ Items are similar (like a list of names)")
print("\nUse DICTIONARIES when:")
print("  ✓ You have key-value relationships")
print("  ✓ You need to look up values by name (key)")
print("  ✓ Order doesn't matter (though Python 3.7+ maintains insertion order)")
print("  ✓ Items have different attributes (like a person's details)")


# ============================================================================
# SUMMARY
# ============================================================================

print("\n=== SUMMARY ===")
print("LISTS:")
print("  - Created with []: my_list = [1, 2, 3]")
print("  - Ordered and indexed (start at 0)")
print("  - Access by index: my_list[0]")
print("  - Mutable: can change, add, remove items")
print("  - Methods: append(), insert(), remove(), pop(), sort()")
print("\nDICTIONARIES:")
print("  - Created with {}: my_dict = {'key': 'value'}")
print("  - Key-value pairs")
print("  - Access by key: my_dict['key']")
print("  - Mutable: can change, add, remove items")
print("  - Methods: keys(), values(), items(), get()")
print("\nBoth are essential for organizing data in Python!")
