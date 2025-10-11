"""
Robot Command Log Analyzer Project
===================================

Create a program that analyzes robot command logs and sensor data files:
- Command frequency analysis
- Sensor data statistics
- Mission duration tracking
- Robot performance analysis

This project combines file handling, dictionaries, data processing, and robotics analytics.

Instructions:
1. Complete each TODO section below
2. Run the file to test with sample_data.txt: python word_counter.py
3. Test with different robot log files

Author: [Your Name Here]
Date: [Today's Date]
"""

import os
import string
from collections import Counter

# TODO 1: Basic robot command counting functions
def count_commands(log_text):
    """Count total robot commands in log text."""
    # TODO: Split log text and count commands
    pass

def count_unique_words(text):
    """Count unique words in text."""
    # TODO: Count unique words (case-insensitive)
    pass

def word_frequency(text):
    """Get word frequency dictionary."""
    # TODO: Return dictionary with word frequencies
    pass

# TODO 2: Text analysis functions
def analyze_text_file(filename):
    """Analyze a text file and return comprehensive statistics."""
    # TODO: Read file and analyze:
    # - Total words, lines, characters
    # - Average words per line
    # - Most common words
    # - Longest and shortest words
    pass

def find_longest_words(text, n=5):
    """Find the n longest words."""
    # TODO: Return list of n longest words
    pass

# TODO 3: Advanced analysis
def reading_level_analysis(text):
    """Estimate reading level of text."""
    # TODO: Calculate average sentence length and word length
    # Return difficulty estimate
    pass

# Test implementations
if __name__ == "__main__":
    print("Testing Word Counter Project...")
    
    sample_file = "../file_handling/sample_data.txt"
    
    if os.path.exists(sample_file):
        try:
            # Test with sample file
            with open(sample_file, 'r') as f:
                content = f.read()
            
            print(f"Command count: {count_commands(content)}")
            print(f"Unique words: {count_unique_words(content)}")
            
            freq = word_frequency(content)
            if freq:
                most_common = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
                print(f"Most common words: {most_common}")
            
            analysis = analyze_text_file(sample_file)
            print(f"File analysis: {analysis}")
            
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Sample file not found: {sample_file}")
        print("Test with a different text file!")
    
    print("\\nComplete the remaining TODOs to finish this project!")