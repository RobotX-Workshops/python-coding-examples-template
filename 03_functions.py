"""
Python Coding Examples - Functions Module
This module demonstrates robotics-themed functions for drone operations.
"""


def calculate_distance(speed, time):
    """
    Calculate the distance traveled by a drone.
    
    Args:
        speed (float): Speed in meters per second
        time (float): Time in seconds
    
    Returns:
        float: Distance traveled in meters
    
    Example:
        >>> calculate_distance(5.0, 10.0)
        50.0
    """
    distance = speed * time
    return distance


def format_sensor_data(x, y, z):
    """
    Format sensor position data into a human-readable string.
    
    Args:
        x (float): X coordinate
        y (float): Y coordinate
        z (float): Z coordinate
    
    Returns:
        str: Formatted string with position data
    
    Example:
        >>> format_sensor_data(10, 20, 5)
        'Position: (x=10, y=20, z=5)'
    """
    formatted_string = f"Position: (x={x}, y={y}, z={z})"
    return formatted_string


# Example usage
if __name__ == "__main__":
    # Example 1: Calculate distance
    drone_speed = 5.0  # meters per second
    flight_time = 10.0  # seconds
    distance = calculate_distance(drone_speed, flight_time)
    print(f"Example 1: Distance traveled")
    print(f"  Speed: {drone_speed} m/s")
    print(f"  Time: {flight_time} s")
    print(f"  Distance: {distance} m")
    print()
    
    # Example 2: Format sensor data
    x_pos = 10
    y_pos = 20
    z_pos = 5
    formatted_data = format_sensor_data(x_pos, y_pos, z_pos)
    print(f"Example 2: Sensor data formatting")
    print(f"  Raw coordinates: x={x_pos}, y={y_pos}, z={z_pos}")
    print(f"  Formatted: {formatted_data}")
