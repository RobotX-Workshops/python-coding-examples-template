# RobotX Python Coding Examples Template

A template repository for creating Python coding examples and exercises for RobotX Workshops students.

## 🚀 Getting Started

### Step 1: Navigate to the Basics

```bash
cd 01_basics
python variables.py
```

### Step 2: Start with Variables

```bash
python variables.py
```

### Step 3: Follow the Learning Path

Complete each folder in numerical order:

1. **01_basics** → Master fundamental concepts
2. **02_functions** → Learn to write reusable code  
3. **03_data_structures** → Organize and manipulate data
4. **04_file_handling** → Work with external files
5. **05_packages** → Manage external libraries and dependencies  
6. **06_object_oriented** → Build complex applications
7. **07_projects** → Apply everything you've learned in this repository.

### For Students

#### Step 1: Create Your Repository

1. Click the **"Use this template"** button at the top of this repository
2. Choose **"Create a new repository"**
3. Name your repository (e.g., `python-exercises-yourname`)
4. Make sure it's set to **Public** (so instructors can review your work)
5. Click **"Create repository from template"**

#### Step 2: Clone Your Repository

```bash
# Replace 'yourusername' and 'your-repo-name' with your actual GitHub username and repository name
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

#### Step 3: Set Up Your Development Environment

##### Option A: Using VS Code (Recommended)

1. Open the folder in VS Code
2. Install the Python extension if you haven't already
3. Set up a Python interpreter (Python 3.8+ recommended)

##### Option B: Using Command Line

1. Make sure Python 3.8+ is installed on your system
2. Create a virtual environment (recommended for package management exercises):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

#### Quick Start for Package Management (Folder 05)

Before working on the package management exercises:

```bash
cd 05_packages
python -m venv package_env
source package_env/bin/activate  # On Windows: package_env\Scripts\activate
pip install -r requirements.txt
```

## 📁 Repository Structure

The exercises are organized in numbered folders that should be completed **in order**. Each folder builds on concepts from the previous ones:

```text
your-repo-name/
├── README.md                 # This file
├── .gitignore               # Git ignore file
├── 01_basics/               # START HERE - Basic Python concepts
│   ├── variables.py
│   ├── data_types.py
│   ├── conditionals.py
│   └── loops.py
├── 02_functions/            # Function exercises
│   ├── basic_functions.py
│   ├── parameters.py
│   └── return_values.py
├── 03_data_structures/      # Lists, dictionaries, etc.
│   ├── lists.py
│   ├── dictionaries.py
│   └── sets_tuples.py
├── 04_file_handling/        # Working with files
│   ├── reading_files.py
│   ├── writing_files.py
│   └── sample_data.txt
├── 05_packages/             # Package management and dependencies
│   ├── pip_basics.py
│   ├── package_basics.py
│   ├── virtual_environments.py
│   └── requirements.txt
├── 06_object_oriented/      # OOP concepts
│   ├── classes.py
│   ├── inheritance.py
│   └── encapsulation.py
├── 07_projects/            # Final projects combining all concepts
│   ├── calculator.py
│   ├── word_counter.py
│   └── simple_game.py
└── bonus_exercise/         # Advanced data analysis challenge
    ├── robot_data_analysis.ipynb
    └── robot_sensor_data.csv
```

## 📝 Exercise Instructions

### Creating Exercise Files

1. Create the folder structure shown above
2. For each Python file, include:
   - A docstring at the top explaining the exercise
   - Clear comments explaining each section
   - Your implementation of the required functions/classes
   - Test cases or example usage

### Example File Template

```python
"""
Exercise: [Exercise Name]
Description: [Brief description of what this exercise covers]
Author: [Your Name]
Date: [Date]
"""

# TODO: Complete the following exercises

def example_function():
    """
    Description of what this function should do.
    
    Returns:
        [Description of return value]
    """
    # Your code here
    pass

# Test your function
if __name__ == "__main__":
    # Add test cases here
    print("Testing example_function...")
    # result = example_function()
    # print(f"Result: {result}")
```

## 🎯 Learning Path - Complete in Order

### 1. Basics (`01_basics/` folder) - **START HERE** 🚀

Master fundamental Python concepts before moving on:

- **variables.py**: Variable declaration, assignment, and scope
- **data_types.py**: Strings, integers, floats, booleans
- **conditionals.py**: if/elif/else statements
- **loops.py**: for loops, while loops, loop control

### 2. Functions (`02_functions/` folder)

Build on basics to create reusable code:

- **basic_functions.py**: Function definition and calling
- **parameters.py**: Parameters, arguments, default values
- **return_values.py**: Return statements and multiple return values

### 3. Data Structures (`03_data_structures/` folder)

Learn to organize and manipulate data:

- **lists.py**: List operations, methods, list comprehensions
- **dictionaries.py**: Dictionary operations, methods, iteration
- **sets_tuples.py**: Set and tuple operations

### 4. File Handling (`04_file_handling/` folder)

Work with external data and files:

- **reading_files.py**: Reading from text files
- **writing_files.py**: Writing to text files
- **sample_data.txt**: Sample data file for exercises

### 5. Package Management (`05_packages/` folder)

Learn to use external libraries and manage dependencies:

- **pip_basics.py**: Learn essential pip commands and check installations
- **package_basics.py**: Install and use your first external package (colorama)
- **virtual_environments.py**: Create simple requirements.txt files
- **requirements.txt**: Sample dependency file for practice

### 6. Object-Oriented Programming (`06_object_oriented/` folder)

Create complex, organized programs:

- **classes.py**: Class definition, constructors, methods
- **inheritance.py**: Class inheritance and method overriding
- **encapsulation.py**: Private attributes and methods

### 7. Final Projects (`07_projects/` folder) - **Capstone** 🎯

Apply everything you've learned:

- **calculator.py**: Feature-rich calculator (combines functions, conditionals, loops)
- **word_counter.py**: Text analysis tool (combines file handling, data structures, packages)
- **simple_game.py**: Interactive game (combines OOP, user input, game logic)

## � Package Management - Why It Matters

**Real-world Python development relies heavily on external packages!** The `05_packages/` folder teaches essential skills:

### Key Concepts You'll Learn

- **Package Installation**: Use `pip` to install powerful libraries like `requests`, `pandas`, `matplotlib`
- **Virtual Environments**: Isolate project dependencies to avoid conflicts
- **Requirements Files**: Share and reproduce project environments with `requirements.txt`
- **Dependency Management**: Understand versioning and compatibility

### Why This Matters

🎯 **Professional Development**: Every Python project uses external packages
🛡️ **Environment Safety**: Virtual environments prevent dependency conflicts  
🤝 **Team Collaboration**: Requirements files ensure everyone has the same setup
📦 **Package Ecosystem**: Access to 400,000+ packages on PyPI

**Complete the package management exercises before moving to OOP** - you'll use these skills in the final projects!

## �💡 Tips for Success

1. **Follow the Order**: The numbered folders build on each other - don't skip ahead!
2. **Complete All TODOs**: Each file has multiple TODO sections - finish them all
3. **Test Frequently**: Run each file after completing TODOs to verify your code works
4. **Read Error Messages**: They're helpful guides to fix your code
5. **Use the Built-in Tests**: Each file has test functions to validate your implementations
6. **Take Your Time**: Understanding is more important than speed
7. **Practice Regularly**: Consistency is key to learning programming
8. **Create Virtual Environments**: Use `python -m venv venv` for each new project
9. **Ask Questions**: Don't hesitate to ask instructors for help

## 📤 Submitting Your Work

### Regular Commits

Make frequent commits as you complete exercises:

```bash
git add .
git commit -m "Complete variables.py exercises"
git push origin main
```

### Final Submission

1. Ensure all exercises are completed
2. Test all your code to make sure it works
3. Update this README with any additional notes about your solutions
4. Make a final commit:

   ```bash
   git add .
   git commit -m "Final submission - all exercises completed"
   git push origin main
   ```

## 🆘 Getting Help

- **Documentation**: [Python Official Documentation](https://docs.python.org/3/)
- **Tutorial**: [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- **Interactive Learning**: [Python.org Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide)
- **Ask Instructors**: Don't hesitate to reach out during workshops

## 📋 Checklist

Use this checklist to track your progress:

### Basics

- [ ] `variables.py` - Variable exercises completed
- [ ] `data_types.py` - Data type exercises completed
- [ ] `conditionals.py` - Conditional logic exercises completed
- [ ] `loops.py` - Loop exercises completed

### Functions

- [ ] `basic_functions.py` - Basic function exercises completed
- [ ] `parameters.py` - Parameter exercises completed
- [ ] `return_values.py` - Return value exercises completed

### Data Structures

- [ ] `lists.py` - List exercises completed
- [ ] `dictionaries.py` - Dictionary exercises completed
- [ ] `sets_tuples.py` - Set and tuple exercises completed

### File Handling

- [ ] `reading_files.py` - File reading exercises completed
- [ ] `writing_files.py` - File writing exercises completed

### Package Management

- [ ] `pip_basics.py` - Basic pip commands learned
- [ ] `package_basics.py` - First external package installed and used
- [ ] `virtual_environments.py` - Requirements.txt file created

### Object-Oriented Programming

- [ ] `classes.py` - Class exercises completed
- [ ] `inheritance.py` - Inheritance exercises completed
- [ ] `encapsulation.py` - Encapsulation exercises completed

### Projects

- [ ] `calculator.py` - Calculator project completed
- [ ] `word_counter.py` - Word counter project completed
- [ ] `simple_game.py` - Game project completed

### Bonus Challenge 🏆

- [ ] `robot_data_analysis.ipynb` - Data visualization and analysis completed

---

## 🎁 Bonus Exercise: Robot Data Analysis

**For advanced students who want extra challenge!**

Located in the `bonus_exercise/` folder, this Jupyter notebook exercise teaches:

- **Data Analysis**: Load and analyze real robot sensor data from CSV files
- **Statistical Methods**: Calculate means, medians, and detect anomalies  
- **Data Visualization**: Create charts, histograms, and correlation heatmaps
- **Jupyter Notebooks**: Interactive data science workflows
- **Python Libraries**: pandas, matplotlib, seaborn, numpy

### Setup Instructions

1. Install required packages:

   ```bash
   cd bonus_exercise/
   pip install -r requirements.txt
   ```

2. Launch Jupyter:

   ```bash
   jupyter notebook robot_data_analysis.ipynb
   ```

3. Complete all TODO sections in the notebook cells

**Skills Gained**: Professional data analysis techniques used in robotics and AI!

---

Good luck with your Python learning journey! 🐍✨
