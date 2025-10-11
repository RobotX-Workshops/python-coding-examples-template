"""
Robot Control Conditionals Exercise
===================================

In this exercise, you'll learn about:
- if, elif, and else statements for robot decision making
- Comparison operators for sensor data evaluation
- Logical operators for complex robot behavior
- Nested conditionals for multi-stage robot operations

Instructions:
1. Complete each TODO section below
2. Run the file to test your implementations: python conditionals.py
3. Make sure all test cases pass

Author: [Your Name Here]
Date: [Today's Date]
"""

# TODO 1: Battery level check
def check_battery_level(battery_percentage):
    """
    Check robot battery level and return status.
    
    Args:
        battery_percentage: Battery level (0-100)
        
    Returns:
        str: "critical", "low", "normal", or "full"
    """
    # TODO: Use if/elif/else to return appropriate battery status
    # critical: below 15%, low: 15-30%, normal: 31-80%, full: above 80%
    pass


# TODO 2: Robot speed controller
def set_robot_speed(distance_to_obstacle):
    """
    Set robot speed based on distance to nearest obstacle.
    
    Args:
        distance_to_obstacle: Distance in meters
        
    Returns:
        str: Speed setting ("stop", "slow", "medium", "fast")
    """
    # TODO: Implement speed control using if/elif/else
    # stop: less than 0.5m, slow: 0.5-1.5m, medium: 1.5-3m, fast: over 3m
    pass


# TODO 3: Age category
def get_age_category(age):
    """
    Categorize age into different life stages.
    
    Args:
        age: Age in years
        
    Returns:
        str: Age category
    """
    # TODO: Implement age categorization:
    # 0-12: "child"
    # 13-19: "teenager" 
    # 20-64: "adult"
    # 65+: "senior"
    pass


# TODO 4: Multiple conditions
def check_triangle(a, b, c):
    """
    Check if three sides can form a valid triangle.
    A triangle is valid if the sum of any two sides is greater than the third side.
    
    Args:
        a, b, c: Three side lengths
        
    Returns:
        bool: True if valid triangle, False otherwise
    """
    # TODO: Check all three triangle inequality conditions
    # Hint: Use logical operators (and, or)
    pass


# TODO 5: Login system
def authenticate_user(username, password, is_active=True):
    """
    Simulate a simple user authentication system.
    
    Args:
        username: Username string
        password: Password string
        is_active: Whether the account is active
        
    Returns:
        dict: Authentication result with status and message
    """
    # TODO: Implement authentication logic:
    # - Username must be at least 3 characters
    # - Password must be at least 8 characters
    # - Account must be active
    # Return format: {"success": bool, "message": str}
    
    result = {"success": False, "message": ""}
    
    # TODO: Add your logic here
    
    return result


# TODO 6: Nested conditionals
def analyze_weather(temperature, humidity, is_raining):
    """
    Analyze weather conditions and provide recommendations.
    
    Args:
        temperature: Temperature in Celsius
        humidity: Humidity percentage (0-100)
        is_raining: Boolean indicating if it's raining
        
    Returns:
        str: Weather recommendation
    """
    # TODO: Implement nested conditional logic:
    # If raining:
    #   - "Stay inside and keep dry"
    # If not raining:
    #   - If temp > 30: "Very hot! Stay hydrated"
    #   - If temp 20-30: 
    #     - If humidity > 70: "Warm and humid"
    #     - Else: "Perfect weather!"
    #   - If temp 10-20: "Cool weather, light jacket recommended"
    #   - If temp < 10: "Cold! Dress warmly"
    pass


# TODO 7: Boolean logic practice
def logical_operations(a, b, c):
    """
    Practice with logical operators.
    
    Args:
        a, b, c: Three boolean values
        
    Returns:
        dict: Results of various logical operations
    """
    results = {}
    
    # TODO: Calculate the following and store in results dictionary:
    # results['all_true'] = all three are True
    # results['any_true'] = at least one is True
    # results['none_true'] = none are True
    # results['exactly_one'] = exactly one is True
    # results['at_least_two'] = at least two are True
    
    return results


# Test your implementations
if __name__ == "__main__":
    print("Testing Conditionals Exercise...")
    
    # Test TODO 1
    print("\\nTODO 1: Check Positive Numbers")
    test_numbers = [5, -3, 0, 10, -7]
    for num in test_numbers:
        try:
            result = check_battery_level(num)
            print(f"check_positive({num}) = {result}")
        except Exception as e:
            print(f"✗ Error with {num}: {e}")
    
    # Test TODO 2
    print("\\nTODO 2: Grade Calculator")
    test_scores = [95, 87, 76, 65, 45]
    for score in test_scores:
        try:
            speed = set_robot_speed(score)
            print(f"set_robot_speed({score}) = {speed}")
        except Exception as e:
            print(f"✗ Error with {score}: {e}")
    
    # Test TODO 3
    print("\\nTODO 3: Age Categories")
    test_ages = [8, 16, 25, 70, 5]
    for age in test_ages:
        try:
            category = get_age_category(age)
            print(f"get_age_category({age}) = {category}")
        except Exception as e:
            print(f"✗ Error with {age}: {e}")
    
    # Test TODO 4
    print("\\nTODO 4: Triangle Validation")
    test_triangles = [(3, 4, 5), (1, 2, 5), (5, 5, 5), (10, 1, 1)]
    for a, b, c in test_triangles:
        try:
            is_valid = check_triangle(a, b, c)
            print(f"check_triangle({a}, {b}, {c}) = {is_valid}")
        except Exception as e:
            print(f"✗ Error with ({a}, {b}, {c}): {e}")
    
    # Test TODO 5
    print("\\nTODO 5: User Authentication")
    test_users = [
        ("admin", "password123", True),
        ("user", "123", True),
        ("validuser", "validpass123", False),
        ("ok", "shortpass", True)
    ]
    for username, password, is_active in test_users:
        try:
            auth_result = authenticate_user(username, password, is_active)
            print(f"authenticate_user('{username}', '***', {is_active}) = {auth_result}")
        except Exception as e:
            print(f"✗ Error with {username}: {e}")
    
    # Test TODO 6
    print("\\nTODO 6: Weather Analysis")
    test_weather = [
        (25, 60, False),
        (35, 80, False),
        (15, 50, False),
        (5, 70, False),
        (20, 90, True)
    ]
    for temp, humidity, raining in test_weather:
        try:
            recommendation = analyze_weather(temp, humidity, raining)
            print(f"analyze_weather({temp}°C, {humidity}%, {raining}) = {recommendation}")
        except Exception as e:
            print(f"✗ Error with weather data: {e}")
    
    # Test TODO 7
    print("\\nTODO 7: Logical Operations")
    test_booleans = [
        (True, True, True),
        (True, False, False),
        (False, False, False),
        (True, False, True)
    ]
    for a, b, c in test_booleans:
        try:
            logic_results = logical_operations(a, b, c)
            print(f"logical_operations({a}, {b}, {c}) = {logic_results}")
        except Exception as e:
            print(f"✗ Error with ({a}, {b}, {c}): {e}")
    
    print("\\n" + "="*50)
    print("Exercise complete! Review your implementations above.")