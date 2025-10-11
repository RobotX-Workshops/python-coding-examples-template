"""
Robot Security Encapsulation Exercise
======================================

In this exercise, you'll learn about:
- Private robot attributes and security methods
- Property decorators for robot access control
- Getters and setters for robot configuration
- Data validation for robot safety parameters
- Access control for robot operations

Instructions:
1. Complete each TODO section below
2. Run the file to test your implementations: python encapsulation.py
3. Make sure all test cases pass

Author: [Your Name Here]
Date: [Today's Date]
"""

# TODO 1: Secure robot with private attributes
class SecureRobot:
    """Secure robot with private configuration attributes."""
    
    def __init__(self, robot_id, initial_battery=100):
        # TODO: Create private attributes using underscore prefix
        # _robot_id, _battery_level, _access_code
        pass
    
    def _validate_access_code(self, code):
        """Private method to validate PIN."""
        # TODO: Check if provided pin matches stored pin
        pass
    
    def deposit(self, amount, pin):
        """Deposit money with PIN validation."""
        # TODO: Validate PIN and amount, then add to balance
        pass
    
    def get_balance(self, pin):
        """Get balance with PIN validation."""
        # TODO: Return balance if PIN is correct
        pass

# TODO 2: Property decorators
class Temperature:
    """Temperature class with property validation."""
    
    def __init__(self, celsius=0):
        # TODO: Initialize private _celsius attribute
        pass
    
    @property
    def celsius(self):
        """Get temperature in Celsius."""
        # TODO: Return celsius value
        pass
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature with validation."""
        # TODO: Validate temperature (not below absolute zero)
        pass
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit."""
        # TODO: Convert and return Fahrenheit
        pass

# Test implementations
if __name__ == "__main__":
    print("Testing Encapsulation Exercise...")
    
    try:
        # Test private attributes
        robot = SecureRobot("GUARDIAN-01", 95)
        print("Account created successfully")
        
        # Test property decorators
        temp = Temperature(25)
        print(f"Temperature: {temp.celsius}°C")
        print(f"Fahrenheit: {temp.fahrenheit}°F")
        
        temp.celsius = 30
        print(f"Updated: {temp.celsius}°C")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\\nComplete the remaining TODOs to finish this exercise!")