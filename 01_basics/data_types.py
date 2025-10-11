"""
Robotics Data Types Exercise
=============================

In this exercise, you'll learn about:
- Python's built-in data types for robotics applications
- Type conversion for sensor data processing
- String operations for robot status messages
- Boolean operations for robot control logic

Instructions:
1. Complete each TODO section below
2. Run the file to test your implementations: python data_types.py
3. Make sure all test cases pass

Author: [Your Name Here]
Date: [Today's Date]
"""

# TODO 1: Robot status strings
# Create a string variable called 'robot_status' with value "System Online"
# Create another string called 'robot_id' with your robot's identifier
# Create a third string called 'status_message' that combines them


# TODO 3: Robot message processing
def process_robot_message(message):
    """
    Process robot status messages and return formatted information.
    Return a dictionary with the following keys:
    - 'uppercase': message in uppercase for alerts
    - 'lowercase': message in lowercase for logs
    - 'word_count': number of words in message
    - 'length': length of message for transmission limits
    """
    pass


# TODO 2: Sensor data types and conversion
# Create an integer variable called 'sensor_count' with value 8
# Create a float variable called 'temperature_reading' with value 23.5
# Convert the sensor count to a string and store in 'count_to_string'
# Convert the string "25.2" to a float and store in 'string_to_temperature'


# TODO 4: Type conversion
def convert_types(value):
    """
    Convert the input value to different types and return them as a dictionary.
    Handle potential conversion errors.
    
    Args:
        value: Input value to convert
        
    Returns:
        dict: Dictionary with converted values
    """
    conversions = {}
    
    # Try to convert to int
    try:
        # TODO: Convert value to integer
        pass
    except ValueError:
        conversions['int'] = None
    
    # Try to convert to float
    try:
        # TODO: Convert value to float
        pass
    except ValueError:
        conversions['float'] = None
    
    # Convert to string (this should always work)
    # TODO: Convert value to string
    
    # Convert to boolean
    # TODO: Convert value to boolean
    
    return conversions


# TODO 5: Robot control boolean operations
def robot_safety_check(is_moving, obstacle_detected):
    """
    Perform safety boolean operations for robot control.
    
    Args:
        is_moving: Boolean indicating if robot is currently moving
        obstacle_detected: Boolean indicating if an obstacle is detected
        
    Returns:
        dict: Dictionary with results of robot safety checks
    """
    results = {}
    
    # TODO: Implement the following robot safety operations:
    # results['same_status'] = is_moving equals obstacle_detected
    # results['different_status'] = is_moving not equal to obstacle_detected
    # results['danger'] = is_moving AND obstacle_detected (both true = dangerous)
    # results['active_system'] = is_moving OR obstacle_detected (system is active)
    # results['safe_to_move'] = NOT obstacle_detected
    
    return results


# TODO 6: Sensor data type validation
def validate_sensor_data(sensor_reading):
    """
    Validate sensor data type and return diagnostic information.
    
    Args:
        sensor_reading: Sensor data value to validate
        
    Returns:
        dict: Dictionary with sensor data type information
    """
    validation = {}
    
    # TODO: Fill in the following sensor data validation:
    # validation['data_type'] = type of sensor_reading (use type() function)
    # validation['type_name'] = string name of the data type
    # validation['is_text_data'] = True if sensor_reading is a string
    # validation['is_numeric_data'] = True if sensor_reading is int or float
    # validation['is_status_flag'] = True if sensor_reading is boolean
    
    return validation


# Test your implementations
if __name__ == "__main__":
    print("Testing Data Types Exercise...")
    
        # Test TODO 1
    try:
        print(f"Robot status: {robot_status}")
        print(f"Robot ID: {robot_id}")
        print(f"Status message: {status_message}")
        print("✓ Robot status strings test passed")
    except NameError as e:
        print(f"✗ Robot status strings test failed: {e}")
        print("  Hint: Make sure you've defined robot_status, robot_id, and status_message variables")
    except Exception as e:
        print(f"✗ Robot status strings test failed: {e}")

    print("\n" + "="*50)

    # Test TODO 2
    try:
        print(f"Sensor count: {sensor_count}")
        print(f"Temperature reading: {temperature_reading}")
        print(f"Count as string: {count_to_string}")
        print(f"Temperature from string: {string_to_temperature}")
        print("✓ Sensor data conversion test passed")
    except NameError as e:
        print(f"✗ Sensor data conversion test failed: {e}")
        print("  Hint: Make sure you've defined all sensor variables and conversions")
    except Exception as e:
        print(f"✗ Sensor data conversion test failed: {e}")