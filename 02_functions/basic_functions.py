"""
Robot Control Functions Exercise
================================

In this exercise, you'll learn about:
- Function definition for robot commands
- Function parameters for robot configuration
- Return statements for sensor data
- Function documentation for robot operations
- Local vs global scope in robot systems

Instructions:
1. Complete each TODO section below
2. Run the file to test your implementations: python basic_functions.py
3. Make sure all test cases pass

Author: [Your Name Here]
Date: [Today's Date]
"""

# TODO 1: Robot initialization function
def initialize_robot():
    """
    Print robot initialization message.
    This function takes no parameters and returns nothing.
    """
    # TODO: Print "Robot systems online - ready for operation!"
    pass


# TODO 2: Robot command with parameters
def move_robot(direction):
    """
    Command robot to move in specified direction.
    
    Args:
        direction (str): Direction to move (forward, backward, left, right)
    """
    # TODO: Print f"Robot moving {direction} - motors engaged!"
    pass


# TODO 3: Sensor reading function with return value
def read_distance_sensor(sensor_id):
    """
    Read distance sensor and return the measurement.
    
    Args:
        sensor_id (int): ID of the distance sensor
        
    Returns:
        int/float: Sum of a and b
    """
    # TODO: Return the sum of a and b
    pass


# TODO 4: Function with multiple parameters
def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): Length of the rectangle
        width (float): Width of the rectangle
        
    Returns:
        float: Area of the rectangle
    """
    # TODO: Calculate and return length * width
    pass


# TODO 5: Function with conditional logic
def is_even(number):
    """
    Check if a number is even.
    
    Args:
        number (int): Number to check
        
    Returns:
        bool: True if even, False if odd
    """
    # TODO: Return True if number is even, False otherwise
    # Hint: Use the modulo operator (%)
    pass


# TODO 6: Function with string operations
def format_name(first_name, last_name):
    """
    Format a full name properly (Title Case).
    
    Args:
        first_name (str): First name
        last_name (str): Last name
        
    Returns:
        str: Formatted full name
    """
    # TODO: Return properly formatted name
    # Hint: Use string methods like .title() or .capitalize()
    pass


# TODO 7: Function with mathematical operations
def calculate_circle_area(radius):
    """
    Calculate the area of a circle.
    Formula: π × radius²
    
    Args:
        radius (float): Radius of the circle
        
    Returns:
        float: Area of the circle
    """
    # TODO: Calculate and return the area
    # Use 3.14159 for π or import math and use math.pi
    pass


# TODO 8: Function with input validation
def divide_numbers(dividend, divisor):
    """
    Divide two numbers with error handling.
    
    Args:
        dividend (float): Number to be divided
        divisor (float): Number to divide by
        
    Returns:
        float or str: Result of division or error message
    """
    # TODO: Check if divisor is zero
    # If zero, return "Error: Cannot divide by zero"
    # Otherwise, return the division result
    pass


# TODO 9: Function that calls other functions
def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).
    BMI = weight (kg) / height (m)²
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
        
    Returns:
        dict: Dictionary with BMI value and category
    """
    # TODO: Calculate BMI
    bmi = 0  # Replace with calculation
    
    # TODO: Determine BMI category using a helper function
    category = get_bmi_category(bmi)  # You'll implement this next
    
    return {"bmi": round(bmi, 2), "category": category}


def get_bmi_category(bmi):
    """
    Determine BMI category based on BMI value.
    
    Args:
        bmi (float): BMI value
        
    Returns:
        str: BMI category
    """
    # TODO: Return appropriate category:
    # BMI < 18.5: "Underweight"
    # 18.5 <= BMI < 25: "Normal weight"
    # 25 <= BMI < 30: "Overweight"
    # BMI >= 30: "Obese"
    pass


# TODO 10: Function with multiple return values
def analyze_numbers(numbers):
    """
    Analyze a list of numbers and return statistics.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        tuple: (min_value, max_value, average, count)
    """
    if not numbers:  # Check if list is empty
        return (0, 0, 0, 0)
    
    # TODO: Calculate and return min, max, average, and count
    # Hint: Use built-in functions min(), max(), sum(), len()
    pass


# TODO 11: Recursive function (Advanced)
def factorial(n):
    """
    Calculate factorial of a number using recursion.
    factorial(n) = n × factorial(n-1)
    factorial(0) = 1
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
    """
    # TODO: Implement factorial using recursion
    # Base case: if n is 0 or 1, return 1
    # Recursive case: return n * factorial(n-1)
    pass


# Test your implementations
if __name__ == "__main__":
    print("Testing Basic Functions Exercise...")
    
    # Test TODO 1
    print("\\nTODO 1: Simple Greeting")
    try:
        initialize_robot()
        print("✓ greet() executed successfully")
    except Exception as e:
        print(f"✗ Error in greet(): {e}")
    
    # Test TODO 2
    print("\\nTODO 2: Personalized Greeting")
    try:
        move_robot("forward")
        print("✓ greet_person() executed successfully")
    except Exception as e:
        print(f"✗ Error in greet_person(): {e}")
    
    # Test TODO 3
    print("\\nTODO 3: Add Numbers")
    try:
        result = read_distance_sensor(1)
        print(f"add_numbers(5, 3) = {result}")
        print("✓ add_numbers() working correctly" if result == 8 else "✗ Incorrect result")
    except Exception as e:
        print(f"✗ Error in add_numbers(): {e}")
    
    # Test TODO 4
    print("\\nTODO 4: Rectangle Area")
    try:
        area = calculate_rectangle_area(5, 3)
        print(f"calculate_rectangle_area(5, 3) = {area}")
        print("✓ calculate_rectangle_area() working correctly" if area == 15 else "✗ Incorrect result")
    except Exception as e:
        print(f"✗ Error in calculate_rectangle_area(): {e}")
    
    # Test TODO 5
    print("\\nTODO 5: Even Number Check")
    test_numbers = [4, 7, 10, 13]
    for num in test_numbers:
        try:
            result = is_even(num)
            print(f"is_even({num}) = {result}")
        except Exception as e:
            print(f"✗ Error with {num}: {e}")
    
    # Test TODO 6
    print("\\nTODO 6: Format Name")
    try:
        formatted = format_name("john", "DOE")
        print(f"format_name('john', 'DOE') = '{formatted}'")
    except Exception as e:
        print(f"✗ Error in format_name(): {e}")
    
    # Test TODO 7
    print("\\nTODO 7: Circle Area")
    try:
        area = calculate_circle_area(5)
        print(f"calculate_circle_area(5) = {area}")
    except Exception as e:
        print(f"✗ Error in calculate_circle_area(): {e}")
    
    # Test TODO 8
    print("\\nTODO 8: Safe Division")
    test_cases = [(10, 2), (7, 0), (15, 3)]
    for dividend, divisor in test_cases:
        try:
            result = divide_numbers(dividend, divisor)
            print(f"divide_numbers({dividend}, {divisor}) = {result}")
        except Exception as e:
            print(f"✗ Error with ({dividend}, {divisor}): {e}")
    
    # Test TODO 9
    print("\\nTODO 9: BMI Calculator")
    try:
        bmi_result = calculate_bmi(70, 1.75)
        print(f"calculate_bmi(70, 1.75) = {bmi_result}")
    except Exception as e:
        print(f"✗ Error in calculate_bmi(): {e}")
    
    # Test TODO 10
    print("\\nTODO 10: Analyze Numbers")
    test_lists = [[1, 5, 3, 9, 2], [10], []]
    for numbers in test_lists:
        try:
            stats = analyze_numbers(numbers)
            print(f"analyze_numbers({numbers}) = {stats}")
        except Exception as e:
            print(f"✗ Error with {numbers}: {e}")
    
    # Test TODO 11
    print("\\nTODO 11: Factorial")
    test_factorials = [0, 1, 5, 7]
    for n in test_factorials:
        try:
            result = factorial(n)
            print(f"factorial({n}) = {result}")
        except Exception as e:
            print(f"✗ Error with {n}: {e}")
    
    print("\\n" + "="*50)
    print("Exercise complete! Review your implementations above.")