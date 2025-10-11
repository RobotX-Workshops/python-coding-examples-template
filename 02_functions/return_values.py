"""
Robot Sensor Return Values Exercise
====================================

In this exercise, you'll learn about:
- Different types of sensor return values
- Multiple return values for robot status (tuples)
- Early returns for safety conditions
- Functions that process vs. return sensor data
- None returns for sensor failures

Instructions:
1. Complete each TODO section below
2. Run the file to test your implementations: python return_values.py
3. Make sure all test cases pass

Author: [Your Name Here]
Date: [Today's Date]
"""

# TODO 1: Simple sensor calculations
def calculate_power_consumption(voltage, current):
    """
    Calculate power consumption of robot motors.
    
    Args:
        voltage (float): Motor voltage in volts
        current (float): Motor current in amps
        
    Returns:
        float: Power consumption in watts
    """
    # TODO: Return number squared
    pass


def get_absolute_value(number):
    """
    Return the absolute value of a number.
    
    Args:
        number (int/float): Input number
        
    Returns:
        int/float: Absolute value
    """
    # TODO: Return absolute value (positive version of number)
    pass


# TODO 2: Multiple return values
def get_name_parts(full_name):
    """
    Split a full name into first and last name.
    
    Args:
        full_name (str): Full name as "First Last"
        
    Returns:
        tuple: (first_name, last_name)
    """
    # TODO: Split the name and return as tuple
    # Handle cases where there might be only one name
    pass


def calculate_circle_properties(radius):
    """
    Calculate both area and circumference of a circle.
    
    Args:
        radius (float): Circle radius
        
    Returns:
        tuple: (area, circumference)
    """
    # TODO: Calculate and return both area and circumference
    # Area = π × radius², Circumference = 2 × π × radius
    # Use 3.14159 for π
    pass


# TODO 3: Conditional returns
def categorize_temperature(temp_celsius):
    """
    Categorize temperature and return appropriate message.
    
    Args:
        temp_celsius (float): Temperature in Celsius
        
    Returns:
        str: Temperature category
    """
    # TODO: Return different messages based on temperature:
    # temp >= 30: "Hot"
    # 20 <= temp < 30: "Warm"
    # 10 <= temp < 20: "Cool" 
    # temp < 10: "Cold"
    pass


def validate_age(age):
    """
    Validate age and return status.
    
    Args:
        age (int): Age to validate
        
    Returns:
        dict: {"valid": bool, "message": str}
    """
    # TODO: Return validation result
    # Valid if age is between 0 and 150 (inclusive)
    # Return appropriate message for each case
    pass


# TODO 4: Early returns
def find_first_negative(numbers):
    """
    Find the first negative number in a list.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int/float or None: First negative number, or None if not found
    """
    # TODO: Use early return to find first negative number
    # Return None if no negative numbers found
    pass


def check_password_strength(password):
    """
    Check password strength with early returns.
    
    Args:
        password (str): Password to check
        
    Returns:
        str: "Weak", "Medium", or "Strong"
    """
    # TODO: Check password criteria with early returns:
    # Weak: length < 6
    # Medium: length >= 6 but no numbers or uppercase
    # Strong: length >= 6, has numbers, and has uppercase letters
    pass


# TODO 5: Return different data types
def analyze_text(text):
    """
    Analyze text and return various statistics.
    
    Args:
        text (str): Text to analyze
        
    Returns:
        dict: Dictionary with analysis results
    """
    # TODO: Return dictionary with:
    # - "length": number of characters
    # - "words": number of words
    # - "sentences": number of sentences (count periods)
    # - "uppercase_letters": number of uppercase letters
    # - "lowercase_letters": number of lowercase letters
    pass


def get_user_choice(prompt, valid_choices):
    """
    Simulate getting user choice (for testing, return first valid choice).
    
    Args:
        prompt (str): Prompt message
        valid_choices (list): List of valid choices
        
    Returns:
        str or None: User choice or None if no valid choices
    """
    # TODO: For this exercise, just return the first valid choice
    # In real implementation, this would use input()
    pass


# TODO 6: Functions that return functions (Advanced)
def create_multiplier(factor):
    """
    Create and return a function that multiplies by a factor.
    
    Args:
        factor (int/float): Multiplication factor
        
    Returns:
        function: Function that multiplies input by factor
    """
    # TODO: Define and return an inner function
    # The inner function should take one parameter and multiply it by factor
    pass


def create_validator(min_value, max_value):
    """
    Create and return a validation function.
    
    Args:
        min_value: Minimum valid value
        max_value: Maximum valid value
        
    Returns:
        function: Validation function
    """
    # TODO: Create and return a function that validates if a number
    # is between min_value and max_value (inclusive)
    pass


# TODO 7: Generator functions (return with yield)
def count_up_to(max_count):
    """
    Generator function that yields numbers from 1 to max_count.
    
    Args:
        max_count (int): Maximum number to count to
        
    Yields:
        int: Numbers from 1 to max_count
    """
    # TODO: Use yield to generate numbers from 1 to max_count
    pass


def fibonacci_generator(n):
    """
    Generate first n Fibonacci numbers.
    
    Args:
        n (int): Number of Fibonacci numbers to generate
        
    Yields:
        int: Fibonacci numbers
    """
    # TODO: Generate Fibonacci sequence using yield
    # Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ...
    pass


# TODO 8: Return value error handling
def safe_list_access(lst, index, default=None):
    """
    Safely access list element with default value.
    
    Args:
        lst (list): List to access
        index (int): Index to access
        default: Default value if index is invalid
        
    Returns:
        Any: List element or default value
    """
    # TODO: Try to access list[index], return default if index is invalid
    pass


def parse_integer(value, default=0):
    """
    Parse string to integer with error handling.
    
    Args:
        value (str): String to parse
        default (int): Default value if parsing fails
        
    Returns:
        int: Parsed integer or default value
    """
    # TODO: Try to convert value to int, return default if it fails
    pass


# Test your implementations
if __name__ == "__main__":
    print("Testing Return Values Exercise...")
    
    # Test TODO 1
    print("\\nTODO 1: Simple Returns")
    try:
        power = calculate_power_consumption(12.0, 2.5)
        abs_val = get_absolute_value(-7)
        print(f"calculate_power_consumption(12.0, 2.5) = {power}")
        print(f"get_absolute_value(-7) = {abs_val}")
    except Exception as e:
        print(f"✗ Error in simple returns: {e}")
    
    # Test TODO 2
    print("\\nTODO 2: Multiple Returns")
    try:
        first, last = get_name_parts("John Doe")
        area, circumference = calculate_circle_properties(5)
        print(f"get_name_parts('John Doe') = {first}, {last}")
        print(f"calculate_circle_properties(5) = area:{area}, circumference:{circumference}")
    except Exception as e:
        print(f"✗ Error in multiple returns: {e}")
    
    # Test TODO 3
    print("\\nTODO 3: Conditional Returns")
    temps = [35, 25, 15, 5]
    for temp in temps:
        try:
            category = categorize_temperature(temp)
            print(f"categorize_temperature({temp}) = {category}")
        except Exception as e:
            print(f"✗ Error with temperature {temp}: {e}")
    
    ages = [25, -5, 200, 0]
    for age in ages:
        try:
            validation = validate_age(age)
            print(f"validate_age({age}) = {validation}")
        except Exception as e:
            print(f"✗ Error with age {age}: {e}")
    
    # Test TODO 4
    print("\\nTODO 4: Early Returns")
    try:
        first_neg = find_first_negative([1, 2, -3, 4, -5])
        no_neg = find_first_negative([1, 2, 3, 4, 5])
        print(f"find_first_negative([1, 2, -3, 4, -5]) = {first_neg}")
        print(f"find_first_negative([1, 2, 3, 4, 5]) = {no_neg}")
        
        passwords = ["123", "password", "Password123"]
        for pwd in passwords:
            strength = check_password_strength(pwd)
            print(f"check_password_strength('{pwd}') = {strength}")
    except Exception as e:
        print(f"✗ Error in early returns: {e}")
    
    # Test TODO 5
    print("\\nTODO 5: Different Data Types")
    try:
        analysis = analyze_text("Hello World! This is a test.")
        print(f"Text analysis: {analysis}")
        
        choice = get_user_choice("Choose:", ["A", "B", "C"])
        print(f"User choice: {choice}")
    except Exception as e:
        print(f"✗ Error in data type returns: {e}")
    
    # Test TODO 6
    print("\\nTODO 6: Returning Functions")
    try:
        times_three = create_multiplier(3)
        result = times_three(5)
        print(f"Multiplier function result: {result}")
        
        validator = create_validator(1, 10)
        is_valid = validator(5)
        print(f"Validator result: {is_valid}")
    except Exception as e:
        print(f"✗ Error in function returns: {e}")
    
    # Test TODO 7
    print("\\nTODO 7: Generator Functions")
    try:
        numbers = list(count_up_to(5))
        print(f"count_up_to(5): {numbers}")
        
        fib_numbers = list(fibonacci_generator(8))
        print(f"fibonacci_generator(8): {fib_numbers}")
    except Exception as e:
        print(f"✗ Error in generators: {e}")
    
    # Test TODO 8
    print("\\nTODO 8: Error Handling Returns")
    try:
        safe_access = safe_list_access([1, 2, 3], 5, "not found")
        valid_access = safe_list_access([1, 2, 3], 1, "not found")
        print(f"safe_list_access([1,2,3], 5) = {safe_access}")
        print(f"safe_list_access([1,2,3], 1) = {valid_access}")
        
        parsed_int = parse_integer("123", -1)
        failed_parse = parse_integer("abc", -1)
        print(f"parse_integer('123') = {parsed_int}")
        print(f"parse_integer('abc') = {failed_parse}")
    except Exception as e:
        print(f"✗ Error in error handling: {e}")
    
    print("\\n" + "="*50)
    print("Exercise complete! Review your implementations above.")