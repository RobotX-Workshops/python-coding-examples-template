"""
Control Flow Example: Drone Pre-Flight Check
This example demonstrates if-elif-else statements using a practical robotics scenario.
"""

# Drone pre-flight check scenario
battery_percentage = 80  # Example value - you can change this to test different conditions

# Check battery level and provide flight recommendation
if battery_percentage < 25:
    print("Warning: Battery critically low. Do not fly.")
elif battery_percentage <= 75:
    print("Battery OK for short flight.")
else:
    print("Battery optimal. Ready for flight.")
