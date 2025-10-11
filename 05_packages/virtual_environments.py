"""
Exercise: Creating a requirements.txt File
Description: Learn to create a simple requirements file for your project
Author: [Your Name]
Date: [Date]

Learning Objectives:
- Understand what a requirements.txt file is
- Create a simple requirements.txt file
- Learn basic pip commands
"""

def show_pip_basics():
    """
    Show the most important pip commands.
    """
    print("📦 Basic pip commands:")
    print("  pip install package_name    # Install a package")
    print("  pip list                    # Show installed packages")
    print("  pip freeze                  # Show packages for requirements.txt")
    print("  pip freeze > requirements.txt  # Create requirements file")


def create_simple_requirements():
    """
    Create a simple requirements.txt file.
    """
    # TODO: Create a requirements.txt file with just one package
    requirements_content = """# My first requirements file
# This file lists the packages needed for this project

colorama>=0.4.4
"""
    
    try:
        with open('my_requirements.txt', 'w') as f:
            f.write(requirements_content)
        print("✅ Created my_requirements.txt")
        print("📝 Look at the file to see what's inside!")
    except Exception as e:
        print(f"❌ Error creating file: {e}")


def read_requirements_file():
    """
    Read and display a requirements file.  
    """
    filename = "my_requirements.txt"
    
    try:
        with open(filename, 'r') as f:
            content = f.read()
        
        print(f"📋 Contents of {filename}:")
        print("-" * 30)
        print(content)
        print("-" * 30)
        
    except FileNotFoundError:
        print(f"❌ {filename} not found!")
        print("Run create_simple_requirements() first")


if __name__ == "__main__":
    print("Creating a Requirements File")
    print("=" * 30)
    print()
    
    print("Step 1: Learn basic pip commands")
    show_pip_basics()
    print()
    
    print("Step 2: Create a requirements file")
    create_simple_requirements()
    print()
    
    print("Step 3: Read the requirements file")
    read_requirements_file()
    print()
    
    print("🎯 Try this:")
    print("1. Install from the file: pip install -r my_requirements.txt") 
    print("2. Check installed packages: pip list")
    print("3. Create your own requirements: pip freeze > my_project_requirements.txt")