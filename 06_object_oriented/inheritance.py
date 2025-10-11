"""
Robot Inheritance Exercise
===========================

In this exercise, you'll learn about:
- Robot class inheritance (base and specialized robots)
- Method overriding for different robot behaviors
- super() function for robot initialization
- Multiple inheritance for complex robot capabilities
- Abstract base classes for robot interfaces

Instructions:
1. Complete each TODO section below
2. Run the file to test your implementations: python inheritance.py
3. Make sure all test cases pass

Author: [Your Name Here]
Date: [Today's Date]
"""

# TODO 1: Basic robot inheritance
class BaseRobot:
    """Base robot class for all robot types."""
    
    def __init__(self, robot_id, model):
        # TODO: Initialize robot_id and model
        pass
    
    def activate(self):
        """Activate robot systems."""
        # TODO: Return generic sound message
        pass
    
    def sleep(self):
        """Animal sleeping behavior."""
        # TODO: Return sleep message
        pass

class DroneRobot(BaseRobot):
    """Drone robot class that inherits from BaseRobot."""
    
    def __init__(self, robot_id, flight_altitude):
        # TODO: Initialize using super() and add flight_altitude
        pass
    
    def activate(self):
        """Override to activate drone systems."""
        # TODO: Return "Drone systems online - ready for flight!" or similar
        pass
    
    def fetch(self):
        """Dog-specific behavior."""
        # TODO: Return fetch message
        pass

# TODO 2: Method overriding and super()
class Vehicle:
    """Base vehicle class."""
    
    def __init__(self, make, model, year):
        # TODO: Initialize vehicle attributes
        pass
    
    def start_engine(self):
        # TODO: Return engine start message
        pass
    
    def get_info(self):
        # TODO: Return vehicle information
        pass

class ElectricCar(Vehicle):
    """Electric car that inherits from Vehicle."""
    
    def __init__(self, make, model, year, battery_capacity):
        # TODO: Initialize using super() and add battery_capacity
        pass
    
    def start_engine(self):
        """Override engine start for electric car."""
        # TODO: Return electric car start message
        pass
    
    def charge_battery(self):
        """Electric car specific method."""
        # TODO: Return charging message
        pass

# Test implementations
if __name__ == "__main__":
    print("Testing Inheritance Exercise...")
    
    try:
        # Test basic inheritance
        drone = DroneRobot("SKY-01", 100)
        print(f"Drone activation: {drone.activate()}")
        print(f"Drone shutdown: {drone.shutdown()}")
        print(f"Drone takeoff: {drone.takeoff()}")
        
        # Test method overriding
        car = ElectricCar("Tesla", "Model 3", 2023, "75kWh")
        print(f"Car start: {car.start_engine()}")
        print(f"Car info: {car.get_info()}")
        print(f"Car charge: {car.charge_battery()}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\\nComplete the remaining TODOs to finish this exercise!")