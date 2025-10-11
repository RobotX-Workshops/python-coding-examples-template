"""
Robot Sensor Sets and Coordinate Tuples Exercise
=================================================

In this exercise, you'll learn about:
- Set operations for sensor management
- Tuple packing for robot coordinates
- When to use sets vs lists vs tuples in robotics
- Set and tuple methods for robot data processing

Instructions:
1. Complete each TODO section below
2. Run the file to test your implementations: python sets_tuples.py
3. Make sure all test cases pass

Author: [Your Name Here]
Date: [Today's Date]
"""

# TODO 1: Sensor management with sets
def get_unique_sensors(sensor_readings):
    """Remove duplicate sensor types from readings list."""
    # TODO: Convert list to set and back to list to remove duplicate sensor types
    pass

def find_shared_sensors(robot1_sensors, robot2_sensors):
    """Find common sensors between two robots."""
    # TODO: Use set intersection to find shared sensor types
    pass

# TODO 2: Basic tuple operations  
def get_coordinates():
    """Return a tuple representing x, y coordinates."""
    # TODO: Return tuple with coordinates (10, 20)
    pass

def unpack_person_info(person_tuple):
    """Unpack person tuple into individual variables."""
    # TODO: Unpack tuple (name, age, city) and return as dictionary
    pass

# Test implementations
if __name__ == "__main__":
    print("Testing Sets and Tuples Exercise...")
    
    # Add basic tests here
    try:
        unique = get_unique_sensors(["camera", "lidar", "lidar", "imu", "imu", "gps"])
        shared = find_shared_sensors(["camera", "lidar", "imu"], ["lidar", "imu", "gps"])
        coords = get_coordinates()
        person_dict = unpack_person_info(("Alice", 25, "New York"))
        
        print(f"Unique items: {unique}")
        print(f"Shared sensors: {shared}")
        print(f"Coordinates: {coords}")
        print(f"Person info: {person_dict}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\\nComplete the remaining TODOs to finish this exercise!")