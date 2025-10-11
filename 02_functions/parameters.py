"""
Robot Configuration Parameters Exercise
=======================================

In this exercise, you'll learn about:
- Positional parameters for robot commands
- Keyword arguments for robot settings
- Default parameter values for robot configuration
- *args for variable sensor inputs
- **kwargs for flexible robot options
- Parameter order and best practices for robotics

Instructions:
1. Complete each TODO section below
2. Run the file to test your implementations: python parameters.py
3. Make sure all test cases pass

Author: [Your Name Here]
Date: [Today's Date]
"""

# TODO 1: Robot configuration with default parameters
def configure_robot(robot_id, battery_level=100, location="Home Base"):
    """
    Configure a robot with optional battery level and location.
    
    Args:
        robot_id (str): Robot's identifier (required)
        battery_level (int, optional): Robot's battery percentage. Defaults to 100.
        location (str, optional): Robot's starting location. Defaults to "Home Base".
        
    Returns:
        str: Introduction string
    """
    # TODO: Create an introduction string
    # If age is provided: "Hi, I'm {name}, {age} years old, from {city}"
    # If age is None: "Hi, I'm {name} from {city}"
    pass


# TODO 2: Function with keyword-only arguments
def create_user_profile(username, *, email, full_name=None, is_active=True):
    """
    Create a user profile with keyword-only arguments.
    The * forces email and subsequent parameters to be keyword-only.
    
    Args:
        username (str): Username (positional)
        email (str): Email address (keyword-only, required)
        full_name (str, optional): Full name. Defaults to None.
        is_active (bool, optional): Active status. Defaults to True.
        
    Returns:
        dict: User profile dictionary
    """
    # TODO: Create and return a dictionary with user information
    profile = {}
    # Add your implementation here
    return profile


# TODO 3: Function with *args
def calculate_average(*numbers):
    """
    Calculate the average of any number of arguments.
    
    Args:
        *numbers: Variable number of numeric arguments
        
    Returns:
        float: Average of all numbers, or 0 if no numbers provided
    """
    # TODO: Calculate and return the average
    # Handle the case when no numbers are provided
    pass


# TODO 4: Function with **kwargs
def format_person_info(**info):
    """
    Format person information from keyword arguments.
    
    Args:
        **info: Variable keyword arguments with person information
        
    Returns:
        str: Formatted information string
    """
    # TODO: Format the information nicely
    # Example output: "Name: John, Age: 30, City: New York"
    # Handle the case when no info is provided
    pass


# TODO 5: Function with mixed parameters
def process_order(item, quantity, price, *extras, discount=0, **customer_info):
    """
    Process an order with mixed parameter types.
    
    Args:
        item (str): Item name (required positional)
        quantity (int): Quantity (required positional)
        price (float): Price per item (required positional)
        *extras: Additional items (variable positional)
        discount (float): Discount percentage. Defaults to 0.
        **customer_info: Customer information (variable keyword)
        
    Returns:
        dict: Order summary
    """
    # TODO: Calculate total cost and create order summary
    # Base cost = quantity * price
    # Add cost for extras (assume each extra costs $2)
    # Apply discount
    # Include customer info in the summary
    
    order = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "extras": list(extras),
        "discount": discount,
        "customer_info": customer_info,
        "total_cost": 0  # Calculate this
    }
    
    # Your calculation here
    
    return order


# TODO 6: Function parameter validation
def safe_divide(dividend, divisor, default_result=None):
    """
    Safely divide two numbers with parameter validation.
    
    Args:
        dividend (float): Number to be divided
        divisor (float): Number to divide by
        default_result: Value to return if division is invalid
        
    Returns:
        float or default_result: Division result or default value
    """
    # TODO: Validate parameters and perform division
    # Check if divisor is zero
    # Check if inputs are numbers
    # Return appropriate result or default_result
    pass


# TODO 7: Function with mutable default arguments (common pitfall)
def add_to_list(item, target_list=None):
    """
    Add an item to a list. Demonstrates proper handling of mutable defaults.
    
    Args:
        item: Item to add
        target_list (list, optional): List to add to. Creates new list if None.
        
    Returns:
        list: Updated list
    """
    # TODO: Properly handle mutable default argument
    # NEVER use [] as default - use None instead
    # If target_list is None, create a new empty list
    # Add item to the list and return it
    pass


# TODO 8: Function with positional-only parameters (Python 3.8+)
def calculate_distance(x1, y1, x2, y2, /):
    """
    Calculate distance between two points.
    The / makes all parameters positional-only.
    
    Args:
        x1, y1: Coordinates of first point
        x2, y2: Coordinates of second point
        
    Returns:
        float: Distance between points
    """
    # TODO: Calculate Euclidean distance
    # Formula: √[(x2-x1)² + (y2-y1)²]
    # You can use (expression) ** 0.5 for square root
    pass


# TODO 9: Function with parameter unpacking
def combine_names(*name_parts, separator=" "):
    """
    Combine name parts with a separator.
    
    Args:
        *name_parts: Variable number of name parts
        separator (str): Separator to use. Defaults to " ".
        
    Returns:
        str: Combined name
    """
    # TODO: Join all name parts with the separator
    # Handle empty name_parts case
    pass


# TODO 10: Complex parameter example
def create_report(title, *sections, author="Anonymous", format_type="text", **metadata):
    """
    Create a report with flexible parameters.
    
    Args:
        title (str): Report title
        *sections: Report sections
        author (str): Report author. Defaults to "Anonymous".
        format_type (str): Output format. Defaults to "text".
        **metadata: Additional metadata
        
    Returns:
        dict: Complete report structure
    """
    # TODO: Create comprehensive report dictionary
    report = {
        "title": title,
        "author": author,
        "format": format_type,
        "sections": list(sections),
        "metadata": metadata,
        "created_at": "2024-01-01"  # You can use actual timestamp if you want
    }
    
    return report


# Test your implementations
if __name__ == "__main__":
    print("Testing Parameters Exercise...")
    
    # Test TODO 1
    print("\\nTODO 1: Default Parameters")
    try:
        config1 = configure_robot("ROBOT-01")
        config2 = configure_robot("ROBOT-02", 85)
        config3 = configure_robot("ROBOT-03", 90, "Laboratory")
        print(f"configure_robot('ROBOT-01') = {config1}")
        print(f"configure_robot('ROBOT-02', 85) = {config2}")
        print(f"configure_robot('ROBOT-03', 90, 'Laboratory') = {config3}")
    except Exception as e:
        print(f"✗ Error in introduce_person(): {e}")
    
    # Test TODO 2
    print("\\nTODO 2: Keyword-only Arguments")
    try:
        profile = create_user_profile("john_doe", email="john@example.com", full_name="John Doe")
        print(f"User profile: {profile}")
    except Exception as e:
        print(f"✗ Error in create_user_profile(): {e}")
    
    # Test TODO 3
    print("\\nTODO 3: *args")
    try:
        avg1 = calculate_average(1, 2, 3, 4, 5)
        avg2 = calculate_average(10, 20)
        avg3 = calculate_average()
        print(f"calculate_average(1, 2, 3, 4, 5) = {avg1}")
        print(f"calculate_average(10, 20) = {avg2}")
        print(f"calculate_average() = {avg3}")
    except Exception as e:
        print(f"✗ Error in calculate_average(): {e}")
    
    # Test TODO 4
    print("\\nTODO 4: **kwargs")
    try:
        info1 = format_person_info(name="Alice", age=25, city="Boston")
        info2 = format_person_info()
        print(f"Person info: {info1}")
        print(f"Empty info: {info2}")
    except Exception as e:
        print(f"✗ Error in format_person_info(): {e}")
    
    # Test TODO 5
    print("\\nTODO 5: Mixed Parameters")
    try:
        order = process_order(
            "Pizza", 2, 15.99, 
            "Extra Cheese", "Pepperoni",
            discount=10,
            name="John", phone="123-456-7890"
        )
        print(f"Order: {order}")
    except Exception as e:
        print(f"✗ Error in process_order(): {e}")
    
    # Test TODO 6
    print("\\nTODO 6: Parameter Validation")
    try:
        result1 = safe_divide(10, 2)
        result2 = safe_divide(10, 0, "undefined")
        result3 = safe_divide("10", 2, "error")
        print(f"safe_divide(10, 2) = {result1}")
        print(f"safe_divide(10, 0, 'undefined') = {result2}")
        print(f"safe_divide('10', 2, 'error') = {result3}")
    except Exception as e:
        print(f"✗ Error in safe_divide(): {e}")
    
    # Test TODO 7
    print("\\nTODO 7: Mutable Default Arguments")
    try:
        list1 = add_to_list("apple")
        list2 = add_to_list("banana")
        list3 = add_to_list("cherry", ["existing"])
        print(f"add_to_list('apple') = {list1}")
        print(f"add_to_list('banana') = {list2}")
        print(f"add_to_list('cherry', ['existing']) = {list3}")
        print("✓ Lists are independent" if list1 != list2 else "✗ Mutable default issue!")
    except Exception as e:
        print(f"✗ Error in add_to_list(): {e}")
    
    # Test TODO 8
    print("\\nTODO 8: Positional-only Parameters")
    try:
        distance = calculate_distance(0, 0, 3, 4)
        print(f"calculate_distance(0, 0, 3, 4) = {distance}")
    except Exception as e:
        print(f"✗ Error in calculate_distance(): {e}")
    
    # Test TODO 9
    print("\\nTODO 9: Parameter Unpacking")
    try:
        name1 = combine_names("John", "Doe")
        name2 = combine_names("Mary", "Jane", "Smith", separator="-")
        print(f"combine_names('John', 'Doe') = {name1}")
        print(f"combine_names('Mary', 'Jane', 'Smith', separator='-') = {name2}")
    except Exception as e:
        print(f"✗ Error in combine_names(): {e}")
    
    # Test TODO 10
    print("\\nTODO 10: Complex Parameters")
    try:
        report = create_report(
            "Annual Report",
            "Introduction",
            "Methodology", 
            "Results",
            author="Dr. Smith",
            format_type="PDF",
            department="Research",
            year=2024
        )
        print(f"Report structure: {report}")
    except Exception as e:
        print(f"✗ Error in create_report(): {e}")
    
    print("\\n" + "="*50)
    print("Exercise complete! Review your implementations above.")