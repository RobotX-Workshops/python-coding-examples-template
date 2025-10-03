"""
Data Structures Examples - Robotics Edition
This file demonstrates basic Python data structures using robotics examples.
"""

# List example: Flight path with coordinate tuples
flight_path = [(0, 0), (5, 10), (10, 10)]

print("Flight Path Waypoints:")
for waypoint in flight_path:
    print(f"  Waypoint: {waypoint}")

print()  # Empty line for better readability

# Dictionary example: Sensor readings
sensor_readings = {
    "gyro": 0.05,
    "accel": 9.81,
    "temp": 25.3
}

# Access and print the "accel" value
print("Sensor Readings:")
print(f"  Accelerometer: {sensor_readings['accel']} m/s²")
