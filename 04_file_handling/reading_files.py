"""
Robot Data File Reading Exercise
=================================

In this exercise, you'll learn about:
- Reading robot configuration files
- Processing sensor data logs line by line  
- File context managers for robot data safety
- Parsing robot telemetry and mission files
- Error handling for robot data corruption

Instructions:
1. Complete each TODO section below
2. Run the file to test your implementations: python reading_files.py
3. Make sure all test cases pass
4. The sample_data.txt file contains robot sensor readings

Author: [Your Name Here]
Date: [Today's Date]
"""

import os

# TODO 1: Robot configuration file reading
def read_robot_config(config_filename):
    """
    Read and return the entire robot configuration file.
    
    Args:
        config_filename (str): Name of robot config file to read
        
    Returns:
        str: File contents, or None if file doesn't exist
    """
    # TODO: Use with statement to open and read file
    # Handle file not found errors
    # Return file contents as string
    pass


def count_lines_in_file(filename):
    """
    Count the number of lines in a file.
    
    Args:
        filename (str): Name of file to read
        
    Returns:
        int: Number of lines, or 0 if file doesn't exist
    """
    # TODO: Open file and count lines
    # Use with statement for proper file handling
    pass


def read_first_n_lines(filename, n):
    """
    Read and return the first n lines from a file.
    
    Args:
        filename (str): Name of file to read
        n (int): Number of lines to read
        
    Returns:
        list: List of first n lines (without newline characters)
    """
    # TODO: Read first n lines from file
    # Remove newline characters from each line
    # Return as list of strings
    pass


# TODO 2: Line-by-line processing
def find_lines_containing(filename, search_term):
    """
    Find all lines containing a specific term.
    
    Args:
        filename (str): Name of file to search
        search_term (str): Term to search for
        
    Returns:
        list: List of tuples (line_number, line_content) containing the term
    """
    # TODO: Search through file line by line
    # Return list of tuples with line number (1-based) and line content
    # Make search case-insensitive
    pass


def count_words_in_file(filename):
    """
    Count total words in a file.
    
    Args:
        filename (str): Name of file to analyze
        
    Returns:
        int: Total word count
    """
    # TODO: Count words in file
    # Split each line into words and count them
    pass


def get_longest_line(filename):
    """
    Find the longest line in a file.
    
    Args:
        filename (str): Name of file to analyze
        
    Returns:
        tuple: (line_number, line_content, length) of longest line
    """
    # TODO: Find line with most characters
    # Return tuple with line number (1-based), content, and length
    pass


# TODO 3: File parsing and data extraction
def extract_names_from_file(filename):
    """
    Extract all names from the sample file.
    Look for lines that start with "Name: ".
    
    Args:
        filename (str): Name of file to parse
        
    Returns:
        list: List of names found in the file
    """
    # TODO: Find lines starting with "Name: " and extract the names
    # Return list of names only (without "Name: " prefix)
    pass


def extract_numbers_from_file(filename):
    """
    Extract all numbers from a file.
    
    Args:
        filename (str): Name of file to parse
        
    Returns:
        list: List of numbers found in the file
    """
    # TODO: Find all numbers in the file
    # Look through each line and extract numeric values
    # Convert to integers where possible
    pass


def parse_person_data(filename):
    """
    Parse person data from the sample file.
    Extract Name, Age, City, and Occupation for each person.
    
    Args:
        filename (str): Name of file to parse
        
    Returns:
        list: List of dictionaries with person data
    """
    # TODO: Parse the structured person data
    # Each person has Name, Age, City, and Occupation on consecutive lines
    # Return list of dictionaries with this information
    pass


# TODO 4: File statistics
def analyze_file_content(filename):
    """
    Perform comprehensive analysis of file content.
    
    Args:
        filename (str): Name of file to analyze
        
    Returns:
        dict: Dictionary with file statistics
    """
    # TODO: Analyze file and return statistics:
    # - "total_lines": number of lines
    # - "total_words": number of words
    # - "total_characters": number of characters
    # - "average_line_length": average characters per line
    # - "longest_word": longest word in file
    # - "most_common_word": most frequently occurring word
    # - "empty_lines": number of empty lines
    
    stats = {}
    return stats


def word_frequency(filename):
    """
    Count frequency of each word in the file.
    
    Args:
        filename (str): Name of file to analyze
        
    Returns:
        dict: Dictionary with word frequencies (case-insensitive)
    """
    # TODO: Count frequency of each word
    # Make counting case-insensitive
    # Remove punctuation from words
    # Return dictionary with word: count pairs
    pass


# TODO 5: Error handling and validation
def safe_file_reader(filename, encoding='utf-8'):
    """
    Safely read a file with comprehensive error handling.
    
    Args:
        filename (str): Name of file to read
        encoding (str): File encoding
        
    Returns:
        dict: Result dictionary with success status and data/error message
    """
    result = {
        "success": False,
        "data": None,
        "error": None,
        "file_info": {}
    }
    
    # TODO: Implement comprehensive error handling:
    # - Check if file exists
    # - Handle permission errors
    # - Handle encoding errors
    # - Get file size and modification time
    # - Return detailed result dictionary
    
    return result


def validate_file_format(filename, expected_lines=None, required_keywords=None):
    """
    Validate that a file meets certain format requirements.
    
    Args:
        filename (str): Name of file to validate
        expected_lines (int, optional): Expected number of lines
        required_keywords (list, optional): Keywords that must be present
        
    Returns:
        dict: Validation results
    """
    # TODO: Validate file format
    # Check if file has expected number of lines
    # Check if all required keywords are present
    # Return validation results with detailed information
    
    validation = {
        "valid": True,
        "errors": [],
        "warnings": []
    }
    
    return validation


# Test your implementations
if __name__ == "__main__":
    print("Testing File Reading Exercise...")
    
    # Check if sample file exists
    sample_file = "sample_data.txt"
    if not os.path.exists(sample_file):
        print(f"✗ Sample file '{sample_file}' not found!")
        print("Make sure sample_data.txt is in the same directory as this script.")
        exit(1)
    
    # Test TODO 1
    print("\\nTODO 1: Basic File Reading")
    try:
        content = read_robot_config(sample_file)
        line_count = count_lines_in_file(sample_file)
        first_lines = read_first_n_lines(sample_file, 3)
        
        print(f"File exists and readable: {content is not None}")
        print(f"Line count: {line_count}")
        print(f"First 3 lines: {first_lines}")
    except Exception as e:
        print(f"✗ Error in basic reading: {e}")
    
    # Test TODO 2
    print("\\nTODO 2: Line-by-line Processing")
    try:
        python_lines = find_lines_containing(sample_file, "python")
        word_count = count_words_in_file(sample_file)
        longest = get_longest_line(sample_file)
        
        print(f"Lines containing 'python': {len(python_lines)}")
        print(f"Total words: {word_count}")
        print(f"Longest line info: {longest}")
    except Exception as e:
        print(f"✗ Error in line processing: {e}")
    
    # Test TODO 3
    print("\\nTODO 3: Data Extraction")
    try:
        names = extract_names_from_file(sample_file)
        numbers = extract_numbers_from_file(sample_file)
        persons = parse_person_data(sample_file)
        
        print(f"Names found: {names}")
        print(f"Numbers found: {numbers[:10]}...")  # Show first 10
        print(f"Person records: {len(persons)}")
    except Exception as e:
        print(f"✗ Error in data extraction: {e}")
    
    # Test TODO 4
    print("\\nTODO 4: File Statistics")
    try:
        stats = analyze_file_content(sample_file)
        frequencies = word_frequency(sample_file)
        
        print(f"File statistics: {stats}")
        print(f"Word frequency count: {len(frequencies)}")
    except Exception as e:
        print(f"✗ Error in statistics: {e}")
    
    # Test TODO 5
    print("\\nTODO 5: Error Handling")
    try:
        safe_result = safe_file_reader(sample_file)
        validation = validate_file_format(sample_file, expected_lines=28)
        
        print(f"Safe read success: {safe_result['success']}")
        print(f"Validation result: {validation}")
        
        # Test with non-existent file
        safe_result_bad = safe_file_reader("nonexistent.txt")
        print(f"Non-existent file handled: {not safe_result_bad['success']}")
    except Exception as e:
        print(f"✗ Error in error handling: {e}")
    
    print("\\n" + "="*50)
    print("Exercise complete! Review your implementations above.")