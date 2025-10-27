"""
Variables and Data Types - Drone Example
==========================================
This example demonstrates different data types using a drone scenario
from RobotX Workshops.
"""

# Integer: Used for whole number values
# altitude_meters represents the drone's altitude in meters
# We use an integer because altitude is typically measured in whole meters
# Example: 15 meters, 50 meters, 100 meters
altitude_meters = 50
print(f"Drone altitude: {altitude_meters} meters")

# Float: Used for decimal/precise numerical values
# battery_voltage represents the drone's battery voltage
# We use a float because voltage requires precision with decimal points
# Example: 12.6V, 11.4V, 10.8V
battery_voltage = 12.6
print(f"Battery voltage: {battery_voltage}V")

# String: Used for text data
# drone_model represents the name/model of the drone
# We use a string because model names contain text characters
# Example: "DJI Mavic", "Parrot Anafi", "Custom Quadcopter"
drone_model = "DJI Mavic Air 2"
print(f"Drone model: {drone_model}")

# Boolean: Used for true/false states
# is_armed indicates whether the drone motors are armed and ready for flight
# We use a boolean because the drone can only be armed (True) or disarmed (False)
# This is critical for safety - motors won't spin when False
is_armed = False
print(f"Drone armed status: {is_armed}")

# Display all variables together
print("\n--- Drone Status Summary ---")
print(f"Model: {drone_model}")
print(f"Altitude: {altitude_meters} meters")
print(f"Battery: {battery_voltage}V")
print(f"Armed: {is_armed}")
