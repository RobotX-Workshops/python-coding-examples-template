"""
Exercise: Installing Your First Package
Description: Learn how to install and use one simple external package
Author: [Your Name]
Date: [Date]

Learning Objectives:
- Install a package using pip
- Import and use an external package
- See the difference between built-in and external modules
"""

# TODO 1: Install the 'colorama' package
# Run this command in your terminal: pip install colorama
# Then uncomment the import statement below

# from colorama import Fore, Style

def print_colored_message():
    """
    Use colorama to print a colorful welcome message.
    """
    # TODO: Uncomment these lines after installing colorama
    # print(Fore.GREEN + "🎉 Congratulations! You installed your first package!")
    # print(Fore.BLUE + "This text is blue!")
    # print(Fore.RED + "This text is red!")
    # print(Style.RESET_ALL + "Back to normal text.")
    
    print("❌ Please install colorama first: pip install colorama")


def compare_modules():
    """
    Show the difference between built-in and external modules.
    """
    print("Built-in modules (come with Python):")
    import math
    import random
    print(f"  math.pi = {math.pi}")
    print(f"  random number = {random.randint(1, 10)}")
    
    print("\nExternal modules (need to be installed):")
    try:
        import colorama
        print("  ✅ colorama is installed!")
    except ImportError:
        print("  ❌ colorama is not installed")


if __name__ == "__main__":
    print("Installing Your First Package")
    print("=" * 30)
    print()
    
    print("Step 1: Install colorama")
    print("Run this command: pip install colorama")
    print()
    
    print("Step 2: Test the installation")
    compare_modules()
    print()
    
    print("Step 3: Try colored output")
    print_colored_message()