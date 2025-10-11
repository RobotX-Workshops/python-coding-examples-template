"""
Robot Configuration Dictionaries Exercise
==========================================

In this exercise, you'll learn about:
- Dictionary creation for robot configurations
- Dictionary methods for robot data management
- Dictionary comprehensions for sensor processing
- Nested dictionaries for complex robot systems
- Dictionary patterns for robotics applications

Instructions:
1. Complete each TODO section below
2. Run the file to test your implementations: python dictionaries.py
3. Make sure all test cases pass

Author: [Your Name Here]
Date: [Today's Date]
"""

# TODO 1: Robot profile creation
def create_robot_profile(robot_id, battery_level, status, sensors):
    """
    Create a robot profile dictionary.
    
    Args:
        robot_id (str): Robot identifier
        battery_level (int): Battery percentage
        status (str): Current operational status
        sensors (list): List of available sensors
        
    Returns:
        dict: Student record dictionary
    """
    # TODO: Create and return dictionary with student information
    pass


def access_dictionary_data(student_dict):
    """
    Access various pieces of data from student dictionary.
    
    Args:
        student_dict (dict): Student dictionary
        
    Returns:
        dict: Dictionary with accessed information
    """
    results = {}
    
    # TODO: Access data safely and store in results:
    # results["name"] = student name
    # results["age"] = student age  
    # results["subjects_count"] = number of subjects
    # results["has_math"] = True if "Math" in subjects, False otherwise
    # results["gpa"] = GPA if exists, "Not Available" otherwise
    
    return results


# TODO 2: Dictionary methods
def dictionary_methods_demo():
    """
    Demonstrate various dictionary methods.
    
    Returns:
        dict: Results of method demonstrations
    """
    # Start with a sample dictionary
    inventory = {
        "apples": 50,
        "bananas": 30,
        "oranges": 25,
        "grapes": 40
    }
    
    results = {}
    
    # TODO: Use dictionary methods and store results:
    # results["all_keys"] = list of all keys
    # results["all_values"] = list of all values
    # results["all_items"] = list of all key-value pairs
    # results["apple_count"] = count of apples using get()
    # results["pears_count"] = count of pears using get() with default 0
    
    # TODO: Add new items
    # Add "pears": 15 to inventory
    # Add "kiwis": 20 to inventory
    
    # TODO: Update and remove
    # Update bananas to 35
    # Remove oranges from inventory
    
    results["final_inventory"] = inventory
    return results


# TODO 3: Dictionary iteration
def analyze_grades(grade_dict):
    """
    Analyze a dictionary of student grades.
    
    Args:
        grade_dict (dict): Dictionary with student names as keys, grades as values
        
    Returns:
        dict: Analysis results
    """
    results = {}
    
    # TODO: Analyze the grades and calculate:
    # results["total_students"] = number of students
    # results["average_grade"] = average of all grades
    # results["highest_grade"] = highest grade
    # results["lowest_grade"] = lowest grade
    # results["passing_students"] = list of students with grade >= 60
    # results["top_student"] = name of student with highest grade
    
    return results


def count_letters(text):
    """
    Count frequency of each letter in text.
    
    Args:
        text (str): Input text
        
    Returns:
        dict: Dictionary with letter counts
    """
    # TODO: Count frequency of each letter (case-insensitive)
    # Ignore spaces and punctuation, only count letters
    letter_counts = {}
    
    return letter_counts


# TODO 4: Dictionary comprehensions
def square_dict(numbers):
    """
    Create dictionary mapping numbers to their squares.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        dict: Dictionary with number: square pairs
    """
    # TODO: Use dictionary comprehension
    pass


def filter_dict(original_dict, condition):
    """
    Filter dictionary based on condition.
    
    Args:
        original_dict (dict): Original dictionary
        condition (str): "even_values", "odd_values", "long_keys" (>3 chars)
        
    Returns:
        dict: Filtered dictionary
    """
    # TODO: Use dictionary comprehension with conditions
    pass


def word_lengths_dict(words):
    """
    Create dictionary mapping words to their lengths.
    
    Args:
        words (list): List of words
        
    Returns:
        dict: Dictionary with word: length pairs
    """
    # TODO: Use dictionary comprehension
    pass


# TODO 5: Nested dictionaries
def create_company_data():
    """
    Create nested dictionary representing company data.
    
    Returns:
        dict: Nested dictionary with company information
    """
    # TODO: Create nested dictionary structure:
    # {
    #     "departments": {
    #         "engineering": {
    #             "employees": ["Alice", "Bob"],
    #             "budget": 100000
    #         },
    #         "marketing": {
    #             "employees": ["Carol", "Dave"],
    #             "budget": 75000
    #         }
    #     },
    #     "company_info": {
    #         "name": "Tech Corp",
    #         "founded": 2020
    #     }
    # }
    pass


def navigate_nested_dict(nested_dict, path):
    """
    Navigate through nested dictionary using a path.
    
    Args:
        nested_dict (dict): Nested dictionary
        path (list): List of keys representing path
        
    Returns:
        Any: Value at the path, or None if path doesn't exist
    """
    # TODO: Navigate through dictionary following the path
    # Example: path ["departments", "engineering", "budget"] should return 100000
    # Return None if any key in path doesn't exist
    pass


# TODO 6: Dictionary advanced operations
def merge_dictionaries(*dicts):
    """
    Merge multiple dictionaries into one.
    
    Args:
        *dicts: Variable number of dictionaries
        
    Returns:
        dict: Merged dictionary (later values override earlier ones)
    """
    # TODO: Merge all dictionaries
    # If same key exists in multiple dicts, last one wins
    pass


def invert_dictionary(original_dict):
    """
    Invert dictionary (swap keys and values).
    
    Args:
        original_dict (dict): Original dictionary
        
    Returns:
        dict: Inverted dictionary
    """
    # TODO: Create new dictionary with values as keys and keys as values
    # Assume all values are unique and hashable
    pass


def group_by_value(original_dict):
    """
    Group keys by their values.
    
    Args:
        original_dict (dict): Dictionary to group
        
    Returns:
        dict: Dictionary where keys are original values, values are lists of original keys
    """
    # TODO: Group keys that have the same value
    # Example: {"a": 1, "b": 2, "c": 1} -> {1: ["a", "c"], 2: ["b"]}
    pass


# TODO 7: Real-world dictionary applications
def process_survey_data(responses):
    """
    Process survey response data.
    
    Args:
        responses (list): List of dictionaries with survey responses
        
    Returns:
        dict: Processed survey statistics
    """
    # TODO: Process survey data and return:
    # - Total number of responses
    # - Average age of respondents  
    # - Most common favorite color
    # - Percentage of satisfied customers (rating >= 4)
    
    # Example input: [
    #     {"name": "Alice", "age": 25, "color": "blue", "rating": 5},
    #     {"name": "Bob", "age": 30, "color": "red", "rating": 3}
    # ]
    
    pass


def create_index(documents):
    """
    Create an index of words to document IDs.
    
    Args:
        documents (dict): Dictionary with doc_id: content pairs
        
    Returns:
        dict: Index where keys are words, values are lists of document IDs
    """
    # TODO: Create inverted index
    # For each word in each document, track which documents contain it
    # Example: {"doc1": "hello world", "doc2": "hello python"}
    # Result: {"hello": ["doc1", "doc2"], "world": ["doc1"], "python": ["doc2"]}
    
    pass


# Test your implementations
if __name__ == "__main__":
    print("Testing Dictionaries Exercise...")
    
    # Test TODO 1
    print("\\nTODO 1: Basic Dictionary Operations")
    try:
        robot = create_robot_profile("ROBOT-A1", 87, "Active", ["Camera", "Ultrasonic", "IMU"])
        access_info = access_dictionary_data(robot)
        print(f"Robot profile: {robot}")
        print(f"Accessed info: {access_info}")
    except Exception as e:
        print(f"✗ Error in basic operations: {e}")
    
    # Test TODO 2
    print("\\nTODO 2: Dictionary Methods")
    try:
        methods_result = dictionary_methods_demo()
        print(f"Methods demo: {methods_result}")
    except Exception as e:
        print(f"✗ Error in dictionary methods: {e}")
    
    # Test TODO 3
    print("\\nTODO 3: Dictionary Iteration")
    try:
        grades = {"Alice": 85, "Bob": 92, "Carol": 78, "Dave": 96, "Eve": 55}
        grade_analysis = analyze_grades(grades)
        letter_count = count_letters("hello world")
        print(f"Grade analysis: {grade_analysis}")
        print(f"Letter counts: {letter_count}")
    except Exception as e:
        print(f"✗ Error in iteration: {e}")
    
    # Test TODO 4
    print("\\nTODO 4: Dictionary Comprehensions")
    try:
        squares = square_dict([1, 2, 3, 4, 5])
        lengths = word_lengths_dict(["hello", "world", "python"])
        print(f"Squares dict: {squares}")
        print(f"Word lengths: {lengths}")
    except Exception as e:
        print(f"✗ Error in comprehensions: {e}")
    
    # Test TODO 5
    print("\\nTODO 5: Nested Dictionaries")
    try:
        company = create_company_data()
        budget = navigate_nested_dict(company, ["departments", "engineering", "budget"])
        print(f"Company data created: {company is not None}")
        print(f"Engineering budget: {budget}")
    except Exception as e:
        print(f"✗ Error in nested dictionaries: {e}")
    
    # Test TODO 6
    print("\\nTODO 6: Advanced Operations")
    try:
        dict1 = {"a": 1, "b": 2}
        dict2 = {"b": 3, "c": 4}
        merged = merge_dictionaries(dict1, dict2)
        inverted = invert_dictionary({"a": 1, "b": 2, "c": 3})
        grouped = group_by_value({"a": 1, "b": 2, "c": 1, "d": 2})
        print(f"Merged: {merged}")
        print(f"Inverted: {inverted}")
        print(f"Grouped: {grouped}")
    except Exception as e:
        print(f"✗ Error in advanced operations: {e}")
    
    print("\\n" + "="*50)
    print("Exercise complete! Review your implementations above.")