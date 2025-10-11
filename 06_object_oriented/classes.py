"""
Robot Classes Exercise
======================

In this exercise, you'll learn about:
- Robot class definition and instantiation
- Robot attributes and control methods  
- Constructor for robot initialization
- String representation for robot status
- Class vs instance attributes for robot fleets
- Method types for robot operations

Instructions:
1. Complete each TODO section below
2. Run the file to test your implementations: python classes.py
3. Make sure all test cases pass

Author: [Your Name Here]
Date: [Today's Date]
"""

# TODO 1: Basic robot class definition
class Robot:
    """Represents an autonomous robot with ID, battery, and location."""
    
    # TODO: Add class attribute for robot type
    robot_type = "Autonomous Unit"  # This is a class attribute
    
    def __init__(self, robot_id, battery_level, location=None):
        """
        Initialize a Person object.
        
        Args:
            name (str): Person's name
            age (int): Person's age  
            email (str, optional): Person's email
        """
        # TODO: Initialize instance attributes
        # self.name = name
        # self.age = age
        # self.email = email
        pass
    
    def introduce(self):
        """Return introduction string."""
        # TODO: Return introduction like "Hi, I'm [name], [age] years old"
        # Include email if available
        pass
    
    def have_birthday(self):
        """Increment age by 1."""
        # TODO: Increase age by 1
        pass
    
    def is_adult(self):
        """Check if person is 18 or older."""
        # TODO: Return True if age >= 18, False otherwise
        pass
    
    def __str__(self):
        """String representation for users."""
        # TODO: Return user-friendly string representation
        pass
    
    def __repr__(self):
        """String representation for developers."""
        # TODO: Return technical string representation
        # Should be able to recreate object with eval()
        pass


# TODO 2: Class with validation and computed properties
class BankAccount:
    """Represents a bank account with balance and transaction history."""
    
    # Class attributes
    bank_name = "Python Bank"
    interest_rate = 0.02  # 2% annual interest
    
    def __init__(self, account_holder, initial_balance=0):
        """
        Initialize bank account.
        
        Args:
            account_holder (str): Name of account holder
            initial_balance (float): Starting balance
        """
        # TODO: Initialize attributes
        # - account_holder: store the name
        # - balance: validate it's not negative
        # - transaction_history: empty list to track transactions
        # - account_number: generate unique number (use id() or random)
        pass
    
    def deposit(self, amount):
        """
        Deposit money into account.
        
        Args:
            amount (float): Amount to deposit
            
        Returns:
            bool: True if successful, False if invalid amount
        """
        # TODO: Validate amount is positive
        # Add to balance
        # Record transaction in history
        # Return success status
        pass
    
    def withdraw(self, amount):
        """
        Withdraw money from account.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            bool: True if successful, False if insufficient funds/invalid
        """
        # TODO: Validate amount is positive and <= balance
        # Subtract from balance
        # Record transaction in history
        # Return success status
        pass
    
    def get_balance(self):
        """Get current balance."""
        # TODO: Return current balance
        pass
    
    def get_transaction_history(self):
        """Get copy of transaction history."""
        # TODO: Return copy of transaction history
        # Don't return the actual list (return a copy)
        pass
    
    def apply_interest(self):
        """Apply annual interest to balance."""
        # TODO: Add interest to balance using class interest_rate
        # Record as transaction
        pass
    
    def __str__(self):
        """String representation of account."""
        # TODO: Return account summary
        pass


# TODO 3: Class methods and static methods
class Student:
    """Represents a student with grades and GPA calculation."""
    
    # Class attributes
    school_name = "Python University"
    total_students = 0  # Track total number of students
    
    def __init__(self, student_id, name, major):
        """Initialize student."""
        # TODO: Initialize instance attributes
        # - student_id, name, major
        # - grades: empty dictionary to store subject: grade pairs
        # - Increment total_students class attribute
        pass
    
    def add_grade(self, subject, grade):
        """
        Add a grade for a subject.
        
        Args:
            subject (str): Subject name
            grade (float): Grade (0-100)
        """
        # TODO: Validate grade is between 0-100
        # Add to grades dictionary
        pass
    
    def calculate_gpa(self):
        """Calculate GPA from grades."""
        # TODO: Calculate GPA from grades dictionary
        # Use 4.0 scale: 90-100=4.0, 80-89=3.0, 70-79=2.0, 60-69=1.0, <60=0.0
        # Return average GPA
        pass
    
    def get_letter_grade(self, numeric_grade):
        """Convert numeric grade to letter grade."""
        # TODO: Convert numeric grade to letter (A, B, C, D, F)
        pass
    
    @classmethod
    def get_total_students(cls):
        """Get total number of students (class method)."""
        # TODO: Return total_students class attribute
        pass
    
    @classmethod
    def create_honor_student(cls, student_id, name, major):
        """Create student with honor status (class method)."""
        # TODO: Create new student and mark as honor student
        # Add an honor_student attribute set to True
        pass
    
    @staticmethod
    def grade_to_points(grade):
        """Convert grade to GPA points (static method)."""
        # TODO: Convert numeric grade to GPA points (0-4 scale)
        # This doesn't need access to class or instance
        pass
    
    def __str__(self):
        """String representation."""
        # TODO: Return student information including GPA
        pass


# TODO 4: Class with private attributes and property decorators
class Temperature:
    """Temperature class with Celsius/Fahrenheit conversion."""
    
    def __init__(self, celsius=0):
        """Initialize with Celsius temperature."""
        # TODO: Initialize private _celsius attribute
        # Validate temperature is not below absolute zero (-273.15°C)
        pass
    
    @property
    def celsius(self):
        """Get temperature in Celsius."""
        # TODO: Return celsius temperature
        pass
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius."""
        # TODO: Validate and set celsius temperature
        # Raise ValueError if below absolute zero
        pass
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit."""
        # TODO: Convert celsius to fahrenheit and return
        # Formula: F = C * 9/5 + 32
        pass
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature in Fahrenheit."""
        # TODO: Convert fahrenheit to celsius and set
        # Formula: C = (F - 32) * 5/9
        pass
    
    @property
    def kelvin(self):
        """Get temperature in Kelvin."""
        # TODO: Convert celsius to kelvin
        # Formula: K = C + 273.15
        pass
    
    def is_freezing(self):
        """Check if temperature is at or below water freezing point."""
        # TODO: Return True if <= 0°C
        pass
    
    def is_boiling(self):
        """Check if temperature is at or above water boiling point."""
        # TODO: Return True if >= 100°C
        pass
    
    def __str__(self):
        """String representation."""
        # TODO: Return temperature in all three scales
        pass


# TODO 5: Class composition (has-a relationship)
class Address:
    """Represents a physical address."""
    
    def __init__(self, street, city, state, zip_code):
        """Initialize address."""
        # TODO: Initialize all address components
        pass
    
    def __str__(self):
        """Format address as string."""
        # TODO: Return formatted address
        pass


class Employee:
    """Employee class that uses Address (composition)."""
    
    def __init__(self, emp_id, name, position, salary, address):
        """
        Initialize employee.
        
        Args:
            emp_id (str): Employee ID
            name (str): Employee name
            position (str): Job position
            salary (float): Annual salary
            address (Address): Address object
        """
        # TODO: Initialize all employee attributes
        # Validate that address is an Address object
        pass
    
    def give_raise(self, amount):
        """Give employee a raise."""
        # TODO: Increase salary by amount
        # Validate amount is positive
        pass
    
    def relocate(self, new_address):
        """Update employee address."""
        # TODO: Update address
        # Validate new_address is Address object
        pass
    
    def get_monthly_salary(self):
        """Calculate monthly salary."""
        # TODO: Return annual salary divided by 12
        pass
    
    def __str__(self):
        """String representation."""
        # TODO: Return employee information including address
        pass


# Test your implementations
if __name__ == "__main__":
    print("Testing Classes Exercise...")
    
    # Test TODO 1: Person class
    print("\\nTODO 1: Person Class")
    try:
        robot = Robot("ATLAS-01", 87, "Warehouse A")
        print(f"Robot created: {robot}")
        print(f"Status report: {robot.status_report()}")
        print(f"Battery low: {robot.is_battery_low()}")
        robot.charge_battery(10)
        print(f"After charging: {robot}")
    except Exception as e:
        print(f"✗ Error in Person class: {e}")
    
    # Test TODO 2: BankAccount class
    print("\\nTODO 2: BankAccount Class")
    try:
        account = BankAccount("John Doe", 1000)
        print(f"Account created: {account}")
        print(f"Deposit 500: {account.deposit(500)}")
        print(f"Withdraw 200: {account.withdraw(200)}")
        print(f"Current balance: {account.get_balance()}")
        account.apply_interest()
        print(f"After interest: {account.get_balance()}")
    except Exception as e:
        print(f"✗ Error in BankAccount class: {e}")
    
    # Test TODO 3: Student class
    print("\\nTODO 3: Student Class")
    try:
        student = Student("S001", "Bob", "Computer Science")
        student.add_grade("Math", 85)
        student.add_grade("Physics", 92)
        print(f"Student: {student}")
        print(f"GPA: {student.calculate_gpa()}")
        print(f"Total students: {Student.get_total_students()}")
        print(f"Grade to points (85): {Student.grade_to_points(85)}")
    except Exception as e:
        print(f"✗ Error in Student class: {e}")
    
    # Test TODO 4: Temperature class
    print("\\nTODO 4: Temperature Class")
    try:
        temp = Temperature(25)
        print(f"Temperature: {temp}")
        print(f"Celsius: {temp.celsius}")
        print(f"Fahrenheit: {temp.fahrenheit}")
        print(f"Kelvin: {temp.kelvin}")
        print(f"Is freezing: {temp.is_freezing()}")
        temp.fahrenheit = 100
        print(f"After setting to 100°F: {temp}")
    except Exception as e:
        print(f"✗ Error in Temperature class: {e}")
    
    # Test TODO 5: Employee and Address classes
    print("\\nTODO 5: Employee and Address Classes")
    try:
        address = Address("123 Main St", "Anytown", "CA", "12345")
        employee = Employee("E001", "Jane Smith", "Developer", 75000, address)
        print(f"Employee: {employee}")
        employee.give_raise(5000)
        print(f"Monthly salary: ${employee.get_monthly_salary():.2f}")
        
        new_address = Address("456 Oak Ave", "Newtown", "NY", "67890")
        employee.relocate(new_address)
        print(f"After relocation: {employee}")
    except Exception as e:
        print(f"✗ Error in Employee/Address classes: {e}")
    
    print("\\n" + "="*50)
    print("Exercise complete! Review your implementations above.")