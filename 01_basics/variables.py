"""
Robotics Variables Exercise
===========================

In this exercise, you'll learn about:
- Variable declaration and assignment for robot parameters
- Variable naming conventions in robotics programming
- Variable scope (global vs local) in robot control systems
- Variable reassignment for changing robot states

Instructions:
1. Complete each TODO section below
2. Run the file to test your implementations: python variables.py
3. Make sure all test cases pass

Author: [Your Name Here]
Date: [Today's Date]
"""

# TODO 1: Create robot configuration variables
# Create a variable called 'robot_name' and assign your robot's name as a string
# Create a variable called 'battery_level' and assign a percentage (0-100) as an integer
# Create a variable called 'max_speed' and assign maximum speed in m/s as a float
# Create a variable called 'is_autonomous' and assign True or False


# TODO 2: Robot state management
# Create a variable called 'sensor_reading' with initial value 0
# Then reassign it to 25 (representing a distance in cm)
# Then reassign it to the string "out_of_range"


# TODO 3: Robot position coordinates
# Assign the values 0, 0, 0 to variables x, y, z in a single line (robot's 3D position)


# TODO 4: Variable scope in robot functions
def demonstrate_scope():
    """
    Create a local variable inside this function called 'local_sensor_data'
    and assign it any sensor reading value you want.
    """
    pass

# TODO 5: Global robot state
# Create a global variable called 'robot_status' with value "READY"
# Create a function called 'update_status' that changes robot_status to "MOVING"


# Test your implementations
if __name__ == "__main__":
    print("Testing Variables Exercise...")
    
    # Test TODO 1
    try:
        print(f"Robot Name: {robot_name}")
        print(f"Battery Level: {battery_level}%")
        print(f"Max Speed: {max_speed} m/s")
        print(f"Is Autonomous: {is_autonomous}")
        print("✓ TODO 1 completed successfully!")
    except NameError as e:
        print(f"✗ TODO 1 incomplete: {e}")
    
    # Test TODO 2
    try:
        print(f"Sensor reading value: {sensor_reading}")
        print("✓ TODO 2 completed successfully!")
    except NameError as e:
        print(f"✗ TODO 2 incomplete: {e}")
    
    # Test TODO 3
    try:
        print(f"x={x}, y={y}, z={z}")
        print("✓ TODO 3 completed successfully!")
    except NameError as e:
        print(f"✗ TODO 3 incomplete: {e}")
    
    # Test TODO 4
    demonstrate_scope()
    print("✓ TODO 4 function created!")
    
    # Test TODO 5
    try:
        print(f"Robot status before: {robot_status}")
        update_status()
        print(f"Robot status after: {robot_status}")
        print("✓ TODO 5 completed successfully!")
    except NameError as e:
        print(f"✗ TODO 5 incomplete: {e}")