"""
Robot Waypoint Lists Exercise
==============================

In this exercise, you'll learn about:
- List creation for robot waypoints and sensor data
- List methods for robot path management
- List slicing for sensor data processing
- List comprehensions for sensor filtering
- Nested lists for robot grid navigation

Instructions:
1. Complete each TODO section below
2. Run the file to test your implementations: python lists.py
3. Make sure all test cases pass

Author: [Your Name Here]
Date: [Today's Date]
"""

# TODO 1: Robot waypoint creation
def create_waypoint_sequence(start_x, end_x):
    """
    Create a list of x-coordinates for robot waypoints.
    
    Args:
        start_x (int): Starting x-coordinate
        end_x (int): Ending x-coordinate
        
    Returns:
        list: List of numbers from start to end
    """
    # TODO: Create and return list of numbers
    # Hint: Use range() and list() or list comprehension
    pass


def get_list_info(lst):
    """
    Get basic information about a list.
    
    Args:
        lst (list): Input list
        
    Returns:
        dict: Dictionary with list information
    """
    # TODO: Return dictionary with:
    # - "length": length of list
    # - "first": first element (or None if empty)
    # - "last": last element (or None if empty)
    # - "middle": middle element (or None if empty)
    pass


# TODO 2: List modification methods
def modify_shopping_list():
    """
    Demonstrate list modification methods.
    
    Returns:
        list: Final shopping list after all operations
    """
    # TODO: Start with empty list
    shopping_list = []
    
    # TODO: Add these items using different methods:
    # - Add "milk" using append()
    # - Add "bread" using append()
    # - Insert "eggs" at position 0 using insert()
    # - Add "cheese" using append()
    # - Remove "bread" using remove()
    # - Add multiple items ["apples", "bananas"] using extend()
    
    return shopping_list


def list_operations_demo(numbers):
    """
    Demonstrate various list operations.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        dict: Results of various operations
    """
    results = {}
    
    # TODO: Perform operations and store results:
    # results["original"] = copy of original list
    # results["sorted"] = sorted version (don't modify original)
    # results["reversed"] = reversed version  
    # results["sum"] = sum of all numbers
    # results["max"] = maximum number
    # results["min"] = minimum number
    # results["count_5"] = count of number 5 in list
    
    return results


# TODO 3: List slicing
def slice_operations(lst):
    """
    Demonstrate list slicing operations.
    
    Args:
        lst (list): Input list
        
    Returns:
        dict: Dictionary with slicing results
    """
    results = {}
    
    # TODO: Perform slicing operations:
    # results["first_three"] = first 3 elements
    # results["last_three"] = last 3 elements  
    # results["middle"] = middle elements (skip first and last)
    # results["every_second"] = every second element
    # results["reverse"] = entire list reversed using slicing
    
    return results


# TODO 4: List searching and filtering
def find_elements(lst, target):
    """
    Find all occurrences of target in list.
    
    Args:
        lst (list): List to search
        target: Element to find
        
    Returns:
        list: List of indices where target is found
    """
    # TODO: Find all indices where target appears
    indices = []
    # Use a loop to find all occurrences
    return indices


def filter_numbers(numbers, condition):
    """
    Filter numbers based on condition.
    
    Args:
        numbers (list): List of numbers
        condition (str): "even", "odd", "positive", "negative"
        
    Returns:
        list: Filtered numbers
    """
    # TODO: Filter based on condition
    # Use if statements to check the condition
    result = []
    
    return result


# TODO 5: List comprehensions
def squares_comprehension(n):
    """
    Create list of squares using list comprehension.
    
    Args:
        n (int): Create squares from 1 to n
        
    Returns:
        list: List of squares [1, 4, 9, 16, ...]
    """
    # TODO: Use list comprehension to create squares
    pass


def filtered_comprehension(numbers, threshold):
    """
    Create list of numbers greater than threshold using comprehension.
    
    Args:
        numbers (list): Input numbers
        threshold (int): Minimum value
        
    Returns:
        list: Numbers greater than threshold
    """
    # TODO: Use list comprehension with condition
    pass


def string_lengths(words):
    """
    Get lengths of all words using list comprehension.
    
    Args:
        words (list): List of strings
        
    Returns:
        list: List of word lengths
    """
    # TODO: Use list comprehension to get lengths
    pass


# TODO 6: Nested lists (2D arrays)
def create_matrix(rows, cols, default_value=0):
    """
    Create a 2D matrix filled with default value.
    
    Args:
        rows (int): Number of rows
        cols (int): Number of columns  
        default_value: Value to fill matrix with
        
    Returns:
        list: 2D list (matrix)
    """
    # TODO: Create nested list representing matrix
    # Use list comprehension or nested loops
    pass


def matrix_operations(matrix):
    """
    Perform operations on a 2D matrix.
    
    Args:
        matrix (list): 2D list
        
    Returns:
        dict: Dictionary with matrix information
    """
    results = {}
    
    # TODO: Calculate and return:
    # results["dimensions"] = (rows, columns)
    # results["total_elements"] = total number of elements
    # results["flat_list"] = flattened version of matrix
    # results["diagonal"] = diagonal elements (if square matrix)
    
    return results


# TODO 7: Advanced list operations
def merge_and_sort(*lists):
    """
    Merge multiple lists and return sorted result.
    
    Args:
        *lists: Variable number of lists
        
    Returns:
        list: Merged and sorted list
    """
    # TODO: Merge all lists and sort the result
    pass


def remove_duplicates(lst):
    """
    Remove duplicates while preserving order.
    
    Args:
        lst (list): List with potential duplicates
        
    Returns:
        list: List without duplicates
    """
    # TODO: Remove duplicates while keeping original order
    # Don't use set() as it doesn't preserve order
    pass


def list_statistics(numbers):
    """
    Calculate comprehensive statistics for a list of numbers.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        dict: Dictionary with statistics
    """
    if not numbers:
        return {}
    
    # TODO: Calculate and return:
    # - "count": number of elements
    # - "sum": sum of all numbers
    # - "average": average value
    # - "median": median value
    # - "mode": most frequent number
    # - "range": difference between max and min
    
    stats = {}
    return stats


# Test your implementations
if __name__ == "__main__":
    print("Testing Lists Exercise...")
    
    # Test TODO 1
    print("\\nTODO 1: Basic List Operations")
    try:
        waypoints = create_waypoint_sequence(1, 5)
        info = get_list_info([1, 2, 3, 4, 5])
        print(f"create_waypoint_sequence(1, 5) = {waypoints}")
        print(f"List info: {info}")
    except Exception as e:
        print(f"✗ Error in basic operations: {e}")
    
    # Test TODO 2
    print("\\nTODO 2: List Modification")
    try:
        shopping = modify_shopping_list()
        print(f"Final shopping list: {shopping}")
        
        operations = list_operations_demo([3, 1, 4, 1, 5, 9, 2, 6])
        print(f"List operations: {operations}")
    except Exception as e:
        print(f"✗ Error in list modification: {e}")
    
    # Test TODO 3
    print("\\nTODO 3: List Slicing")
    try:
        slices = slice_operations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        print(f"Slicing results: {slices}")
    except Exception as e:
        print(f"✗ Error in slicing: {e}")
    
    # Test TODO 4
    print("\\nTODO 4: Searching and Filtering")
    try:
        indices = find_elements([1, 2, 3, 2, 4, 2, 5], 2)
        even_nums = filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "even")
        print(f"Indices of 2: {indices}")
        print(f"Even numbers: {even_nums}")
    except Exception as e:
        print(f"✗ Error in searching/filtering: {e}")
    
    # Test TODO 5
    print("\\nTODO 5: List Comprehensions")
    try:
        squares = squares_comprehension(5)
        filtered = filtered_comprehension([1, 5, 3, 8, 2, 9], 4)
        lengths = string_lengths(["hello", "world", "python", "list"])
        print(f"Squares: {squares}")
        print(f"Filtered: {filtered}")
        print(f"Lengths: {lengths}")
    except Exception as e:
        print(f"✗ Error in comprehensions: {e}")
    
    # Test TODO 6
    print("\\nTODO 6: Nested Lists")
    try:
        matrix = create_matrix(3, 3, 1)
        matrix_info = matrix_operations([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print(f"3x3 matrix: {matrix}")
        print(f"Matrix info: {matrix_info}")
    except Exception as e:
        print(f"✗ Error in nested lists: {e}")
    
    # Test TODO 7
    print("\\nTODO 7: Advanced Operations")
    try:
        merged = merge_and_sort([3, 1, 4], [1, 5, 9], [2, 6, 5])
        no_dups = remove_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 5])
        stats = list_statistics([1, 2, 3, 4, 5, 3, 3])
        print(f"Merged and sorted: {merged}")
        print(f"No duplicates: {no_dups}")
        print(f"Statistics: {stats}")
    except Exception as e:
        print(f"✗ Error in advanced operations: {e}")
    
    print("\\n" + "="*50)
    print("Exercise complete! Review your implementations above.")