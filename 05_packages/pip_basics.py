"""
Exercise: Using pip Commands
Description: Practice the most important pip commands
Author: [Your Name]
Date: [Date]

Learning Objectives:
- Learn essential pip commands
- Check what packages are installed
- Understand the difference between built-in and installed packages
"""

import sys

def show_python_info():
    """
    Show basic information about your Python installation.
    """
    print("🐍 Your Python Information:")
    print(f"  Python version: {sys.version.split()[0]}")
    print(f"  Python location: {sys.executable}")


def show_pip_commands():
    """
    Display the most useful pip commands.
    """
    print("📦 Essential pip commands:")
    print()
    print("Install a package:")
    print("  pip install colorama")
    print()
    print("See what's installed:")
    print("  pip list")
    print()
    print("Get details about a package:")
    print("  pip show colorama")
    print()
    print("Uninstall a package:")
    print("  pip uninstall colorama")
    print()
    print("Install from requirements file:")
    print("  pip install -r requirements.txt")


def check_package_installed(package_name):
    """
    Check if a specific package is installed.
    
    Args:
        package_name (str): Name of the package to check
    """
    try:
        __import__(package_name)
        print(f"✅ {package_name} is installed")
        return True
    except ImportError:
        print(f"❌ {package_name} is not installed")
        print(f"   Install it with: pip install {package_name}")
        return False


def test_built_in_modules():
    """
    Test some built-in modules that come with Python.
    """
    print("🔧 Testing built-in modules (no installation needed):")
    
    # Test math module
    import math
    print(f"  math.pi = {math.pi:.2f}")
    
    # Test random module
    import random
    print(f"  random number = {random.randint(1, 100)}")
    
    # Test datetime module
    from datetime import datetime
    print(f"  current time = {datetime.now().strftime('%Y-%m-%d %H:%M')}")


if __name__ == "__main__":
    print("Learning pip Commands")
    print("=" * 25)
    print()
    
    print("Step 1: Check your Python")
    show_python_info()
    print()
    
    print("Step 2: Learn pip commands")
    show_pip_commands()
    print()
    
    print("Step 3: Test built-in modules")
    test_built_in_modules()
    print()
    
    print("Step 4: Check for external packages")
    check_package_installed("colorama")
    print()
    
    print("🎯 Try this:")
    print("1. Run: pip list")
    print("2. Install colorama: pip install colorama")  
    print("3. Run this script again to see the difference!")