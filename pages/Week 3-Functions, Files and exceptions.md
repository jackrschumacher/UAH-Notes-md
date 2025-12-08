---
title: Week 3-Functions, Files and exceptions
---

## I. Functions
### Introduction to Functions
  * **Definition:** A group of statements within a program that performs a specific task.
  * [cite_start]**Divide and Conquer:** A strategy of breaking a large, complex program into smaller, modularized tasks (functions) [cite: 1012-1016].
  * **Benefits:**
    * Simpler code.
    * **Code Reuse:** Write once, call multiple times.
    * Better testing and debugging (test individually).
    * [cite_start]Faster development and facilitation of teamwork [cite: 1073-1079].
### Types of Functions
  1.  [cite_start]**Void Functions:** Execute statements and terminate (do not return a value) [cite: 1087-1089].
  2.  [cite_start]**Value-Returning Functions:** Execute statements and return a value to the calling statement (e.g., `int()`, `input()`) [cite: 1090-1092].
### Defining and Calling
  * [cite_start]**Naming Rules:** Cannot use keywords, cannot contain spaces, must start with a letter or underscore, and are case-sensitive [cite: 1100-1103].
  * **Syntax:**
    ```python
    def function_name():
        statement
        statement
    ```
  * [cite_start]**Indentation:** The block of statements belonging to the function must be indented consistently [cite: 1143-1144].
  * [cite_start]**Main Function:** Defines the mainline logic of the program and calls other functions as needed [cite: 1135-1137].
### Designing with Functions
  * [cite_start]**Flowcharts:** Function calls are depicted as rectangles with vertical bars at each side[cite: 1153].
  * [cite_start]**Hierarchy Charts:** (Structure Charts) Depict relationships between functions using boxes and connecting lines to show what calls what [cite: 1173-1174].
  * [cite_start]**The `pass` Keyword:** Can be used to create empty functions as placeholders during design[cite: 1195].
### Variables and Scope
  * **Local Variables:** Created inside a function and belong only to that function. [cite_start]They cannot be accessed by code outside the function [cite: 1205-1207].
  * **Scope:** The part of the program where a variable may be accessed.
  * **Global Variables:** Created outside all functions. Accessible anywhere but make debugging difficult and programs hard to understand. [cite_start]**Avoid usage** [cite: 1340, 1348-1353].
  * **Global Constants:** Global names referencing unchangeable values. [cite_start]These are permissible[cite: 1358].
### Arguments and Parameters
  * **Argument:** Data sent *into* a function call.
  * [cite_start]**Parameter:** The variable inside the function that receives the argument[cite: 1243].
  * [cite_start]**Pass by Value:** Changes made to a parameter inside the function do *not* affect the argument outside the function [cite: 1287-1288].
  * [cite_start]**Keyword Arguments:** Specifies which parameter a value belongs to (e.g., `func(parameter=value)`), allowing arguments to be passed out of order [cite: 1331-1332].
### Return Values
  * **Syntax:** `return expression`.
  * **Multiple Values:** Python can return multiple values separated by commas.
    * [cite_start]Example: `return expression1, expression2` [cite: 1527-1528].
  * [cite_start]**None:** A special value meaning "no value," often used to indicate errors [cite: 1533-1534].
  
---
## II. Modules and Standard Library
### Standard Library
  * **Definition:** Pre-written functions that come with Python (e.g., `print`, `range`).
  * **Modules:** Files that store library functions. [cite_start]To use them, you must use the `import` statement [cite: 1386-1389].
### The `random` Module
  Requires `import random`. Useful functions include:
  * [cite_start]`randint(min, max)`: Returns a random integer in the range[cite: 1414].
  * `randrange(start, stop, step)`: Returns a randomly selected integer from the sequence.
  * `random()`: Returns a float between 0.0 and 1.0.
  * [cite_start]`uniform(min, max)`: Returns a float within a specified range [cite: 1442-1447].
  * **Seeds:** `random.seed()` initializes the random number generator. [cite_start]By default, it uses system time [cite: 1454-1456].
### The `math` Module
  Requires `import math`.
  
  | Function | Description | Citation |
  | :--- | :--- | :--- |
  | `ceil(x)` | [cite_start]Smallest integer >= x | [cite: 1554] |
  | `floor(x)` | [cite_start]Largest integer <= x | [cite: 1554] |
  | `sqrt(x)` | [cite_start]Square root of x | [cite: 1554] |
  | `pow(x, y)` | x raised to power of y | |
  | `pi` | [cite_start]Constant value of $\pi$ | [cite: 1559] |
### Creating Modules
  * Any file ending in `.py` can be imported as a module.
  * **Conditional Execution:** To prevent code from running when imported, use:
    ```python
    if __name__ == '__main__':
        main()
    ```
    [cite_start]This ensures `main()` only runs if the file is executed as a standalone program [cite: 1610-1611].
  
---
## III. Files and File Input/Output
### Basics of File I/O
  * **Purpose:** To retain data between program runs (save to disk).
  * **Types of Files:**
    * **Text:** Encoded as text.
    * [cite_start]**Binary:** Raw data not converted to text [cite: 1724-1725].
  * **Access Methods:**
    * **Sequential:** Read from beginning to end (e.g., tape).
    * [cite_start]**Direct:** Jump to any piece of data [cite: 1727-1728].
### File Operations
  1.  **Open:** Creates a file object. `file_variable = open(filename, mode)`.
  2.  **Process:** Read or write data.
  3.  **Close:** Disconnects the program from the file. [cite_start]`file_variable.close()` [cite: 1700-1703].
### File Modes
  * `'r'`: **Read** only.
  * `'w'`: **Write**. Overwrites existing file or creates a new one.
  * `'a'`: **Append**. [cite_start]Adds to the end of the file or creates a new one[cite: 1757, 1799].
### Reading and Writing
  * **Writing:** `file.write(string)`.
    * [cite_start]*Note:* You usually need to concatenate a newline `\n` to the string[cite: 1773, 1790].
    * [cite_start]**Numeric Data:** Must be converted to string (`str()`) before writing[cite: 1809].
  * **Reading:**
    * `read()`: Reads entire file into memory.
    * `readline()`: Reads a single line (including `\n`).
    * [cite_start]`rstrip()`: Removes specific characters (like `\n`) from the end of a string [cite: 1780-1783, 1792].
    * [cite_start]**Numeric Data:** Must be converted to `int` or `float` after reading[cite: 1812].
### Processing Files with Loops
  * **While Loop:** Use `readline` and check for an empty string (end of file sentinel).
    ```python
    while line != '':
        # process
    ```
    [cite_start][cite: 1821-1822]
  * **For Loop:** Python automatically iterates over lines in a file.
    ```python
    for line in file_object:
        statements
    ```
    [cite_start][cite: 1844].
  
---
## IV. Exceptions
### Concepts
  * [cite_start]**Exception:** An error that occurs during runtime (e.g., division by zero, file not found) that typically crashes the program[cite: 1871].
  * [cite_start]**Traceback:** The error message indicating where the error occurred[cite: 1872].
### Exception Handling (`try` / `except`)
  Used to prevent crashes by handling errors gracefully.
  
  * **Try Suite:** Statements that might cause an exception.
  * **Except Clause:** Code that executes if a specific exception occurs.
  * [cite_start]**Else Clause (Optional):** Executes *only* if no exception was raised[cite: 1934].
  * [cite_start]**Finally Clause (Optional):** Executes *always*, regardless of exceptions (used for cleanup) [cite: 1946-1947].
  
  **Syntax:**
  ```python
  try:
    statements
  except ValueError:
    print("Invalid number")
  except IOError as err:
    [cite_start]print(err) # Prints default error message [cite: 1925]
  else:
    print("Success")
  finally:
    print("Cleanup")