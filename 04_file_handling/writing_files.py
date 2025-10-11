"""
Robot Data File Writing Exercise
=================================

In this exercise, you'll learn about:
- Writing robot configuration files
- Different file modes for robot data logging
- Creating robot mission reports and logs
- CSV file writing for sensor data
- Error handling for robot data persistence

Instructions:
1. Complete each TODO section below
2. Run the file to test your implementations: python writing_files.py
3. Check the created robot data files to verify output

Author: [Your Name Here]
Date: [Today's Date]
"""

# TODO 1: Robot configuration file writing
def write_robot_config(config_filename, robot_config):
    """Write robot configuration to a file."""
    # TODO: Write robot config data to file using with statement
    pass

def log_robot_activity(log_filename, activity_data):
    """Append robot activity to existing log file."""
    # TODO: Append new activity data to robot log file
    pass

# TODO 2: Create formatted output
def create_report(filename, data):
    """Create a formatted report file."""
    # TODO: Write formatted report with headers and data
    pass

# Test implementations
if __name__ == "__main__":
    print("Testing File Writing Exercise...")
    
    try:
        write_robot_config("robot_config.txt", "Robot ID: EXPLORER-01\\nBattery: 100%\\nStatus: Online")
        log_robot_activity("robot_log.txt", "\\n[2024-01-01 10:00] Robot started patrol mission")
        
        sample_data = [
            {"name": "Alice", "score": 85},
            {"name": "Bob", "score": 92}
        ]
        create_report("report.txt", sample_data)
        
        print("Files created successfully!")
        print("Check test_output.txt and report.txt")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\\nComplete the remaining TODOs to finish this exercise!")