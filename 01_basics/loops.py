"""
Robot Control Loops Exercise
=============================

In this exercise, you'll learn about:
- for loops for sensor polling and waypoint navigation
- while loops for continuous robot operation
- Loop control statements for emergency stops and skip conditions
- Nested loops for multi-dimensional robot grid navigation
- List comprehensions for sensor data processing

Instructions:
1. Complete each TODO section below
2. Run the file to test your implementations: python loops.py
3. Make sure all test cases pass

Author: [Your Name Here]
Date: [Today's Date]
"""

# TODO 1: Robot startup sequence
def robot_startup_sequence(sensor_count):
    """
    Initialize sensors from 1 to sensor_count using a for loop.
    
    Args:
        sensor_count: Number of sensors to initialize
    """
    # TODO: Use a for loop with range() to print "Initializing sensor X" for each sensor
    pass


# TODO 2: Sensor data aggregation
def calculate_average_reading(sensor_readings):
    """
    Calculate the average of all sensor readings using a for loop.
    
    Args:
        sensor_readings: List of sensor readings
        
    Returns:
        int/float: Sum of all numbers
    """
    # TODO: Use a for loop to calculate the sum
    total = 0
    # Your code here
    return total


# TODO 3: String iteration
def count_vowels(text):
    """
    Count the number of vowels in a string.
    
    Args:
        text: Input string
        
    Returns:
        int: Number of vowels
    """
    vowels = "aeiouAEIOU"
    count = 0
    
    # TODO: Use a for loop to iterate through each character
    # and count vowels
    
    return count


# TODO 4: While loop
def countdown(start):
    """
    Create a countdown from start to 1 using a while loop.
    Print each number, then print "Blast off!"
    
    Args:
        start: Starting number
    """
    # TODO: Implement countdown using while loop
    pass


# TODO 5: User input with while loop
def guess_number():
    """
    Simple number guessing game using while loop.
    The secret number is 42.
    Keep asking for input until user guesses correctly.
    
    Note: This function won't work in automated testing,
    but you can test it manually by calling it.
    """
    secret_number = 42
    guessed = False
    
    print("Guess the secret number (between 1-100)!")
    
    # TODO: Use while loop to keep asking for guesses
    # Use input() to get user input
    # Convert input to int and compare with secret_number
    # Print appropriate messages
    
    # Uncomment and complete:
    # while not guessed:
    #     # Your code here
    #     pass
    
    pass


# TODO 6: Break and continue
def process_numbers(numbers):
    """
    Process a list of numbers with special rules:
    - Skip negative numbers (use continue)
    - Stop processing when you encounter 0 (use break)
    - For positive numbers, add them to result list
    
    Args:
        numbers: List of numbers
        
    Returns:
        list: Processed positive numbers (before first 0)
    """
    result = []
    
    # TODO: Implement using for loop with break and continue
    
    return result


# TODO 7: Nested loops - multiplication table
def multiplication_table(size):
    """
    Create a multiplication table using nested loops.
    
    Args:
        size: Size of the table (e.g., 5 creates 5x5 table)
        
    Returns:
        list: 2D list representing multiplication table
    """
    table = []
    
    # TODO: Use nested for loops to create multiplication table
    # Outer loop for rows, inner loop for columns
    # Each cell should contain row * column
    
    return table


# TODO 8: Pattern printing
def print_triangle(height):
    """
    Print a triangle pattern using nested loops.
    Example for height=4:
    *
    **
    ***
    ****
    
    Args:
        height: Height of the triangle
    """
    # TODO: Use nested loops to print the pattern
    pass


# TODO 9: List comprehension (Bonus)
def squares_comprehension(n):
    """
    Create a list of squares from 1 to n using list comprehension.
    
    Args:
        n: Upper limit
        
    Returns:
        list: List of squares [1, 4, 9, 16, ...]
    """
    # TODO: Use list comprehension to create list of squares
    # Hint: [expression for item in iterable]
    pass


# TODO 10: Filtered list comprehension (Bonus)
def even_squares(n):
    """
    Create a list of squares of even numbers from 1 to n.
    
    Args:
        n: Upper limit
        
    Returns:
        list: List of squares of even numbers
    """
    # TODO: Use list comprehension with condition
    # Hint: [expression for item in iterable if condition]
    pass


# Test your implementations
if __name__ == "__main__":
    print("Testing Loops Exercise...")
    
    # Test TODO 1
    print("\\nTODO 1: Count to N")
    print("count_to_n(5):")
    try:
        robot_startup_sequence(5)
        print("✓ Function executed")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test TODO 2
    print("\\nTODO 2: Calculate Sum")
    test_lists = [[1, 2, 3, 4, 5], [10, 20, 30], []]
    for lst in test_lists:
        try:
            result = calculate_average_reading(lst)
            print(f"calculate_sum({lst}) = {result}")
        except Exception as e:
            print(f"✗ Error with {lst}: {e}")
    
    # Test TODO 3
    print("\\nTODO 3: Count Vowels")
    test_strings = ["hello", "programming", "xyz", "AEIOU"]
    for text in test_strings:
        try:
            count = count_vowels(text)
            print(f"count_vowels('{text}') = {count}")
        except Exception as e:
            print(f"✗ Error with '{text}': {e}")
    
    # Test TODO 4
    print("\\nTODO 4: Countdown")
    print("countdown(3):")
    try:
        countdown(3)
        print("✓ Function executed")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test TODO 6
    print("\\nTODO 6: Process Numbers")
    test_number_lists = [
        [1, 2, -3, 4, 0, 5, 6],
        [5, -1, -2, 0, 10],
        [1, 2, 3, 4, 5]
    ]
    for numbers in test_number_lists:
        try:
            result = process_numbers(numbers)
            print(f"process_numbers({numbers}) = {result}")
        except Exception as e:
            print(f"✗ Error with {numbers}: {e}")
    
    # Test TODO 7
    print("\\nTODO 7: Multiplication Table")
    try:
        table = multiplication_table(3)
        print("multiplication_table(3):")
        for row in table:
            print(row)
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test TODO 8
    print("\\nTODO 8: Triangle Pattern")
    print("print_triangle(4):")
    try:
        print_triangle(4)
        print("✓ Function executed")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test TODO 9
    print("\\nTODO 9: Squares Comprehension")
    try:
        squares = squares_comprehension(5)
        print(f"squares_comprehension(5) = {squares}")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test TODO 10
    print("\\nTODO 10: Even Squares")
    try:
        even_sq = even_squares(10)
        print(f"even_squares(10) = {even_sq}")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    print("\\n" + "="*50)
    print("Exercise complete! Review your implementations above.")
    print("\\nTo test the guessing game (TODO 5), call guess_number() manually.")